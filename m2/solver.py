# m2/solver.py — M2 活动穿底确定性求解器
import itertools
import os
import re
import sys
from collections import Counter

# 避免 Windows 终端 GBK 编码输出崩溃
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 保证项目根目录在 sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m2.mock_menus import MOCK_STORES, FIX_RULE

def translate_rule(rule_text):
    """
    规则翻译演示桩：
    正式版这里调 DeepSeek JSON Only 做翻译，把人话规则解析成确定性结构化约束；
    Demo 阶段用正则桩代替，省 API 钱。
    Text-to-Solver 架构分工：规则翻译占 15%，确定性暴力求解占 85%，LLM 不直接算账。
    """
    match = re.search(r"满(\d+)减(\d+)", rule_text)
    if match:
        threshold = int(match.group(1))
        off = int(match.group(2))
        return {"type": "满减", "threshold": threshold, "off": off}
    return {"type": "无", "threshold": 0, "off": 0}

def format_combo_text(skus_in_combo):
    """把商品列表格式化为人话，如：引流烤肠×3 + 薯条×1 + 可乐×1"""
    counter = Counter(s["name"] for s in skus_in_combo)
    return " + ".join(f"{name}×{count}" if count > 1 else name for name, count in counter.items())

def calc_profit(store, skus_in_combo, custom_discount=None):
    """
    按锁死公式计算组合成本与利润：
      实收 = 总价 - 满减 - 佣金，佣金 = 该店佣金率 × (总价 - 满减)
      利润 = 实收 - 总成本 - 该店配送/物流成本
      利润 < 0 就是穿底（负毛利组合）
    """
    total_price = sum(s["price"] for s in skus_in_combo)
    total_cost = sum(s["cost"] for s in skus_in_combo)
    commission_rate = store["commission_rate"]
    delivery_cost = store["delivery_cost_yuan"]
    
    if custom_discount is not None:
        discount = custom_discount
    else:
        rule = store.get("rule", {})
        threshold = rule.get("threshold", 0)
        off = rule.get("off", 0)
        discount = off if total_price >= threshold else 0.0

    post_discount_price = max(0.0, total_price - discount)
    commission = commission_rate * post_discount_price
    net_receipt = post_discount_price - commission
    profit = net_receipt - total_cost - delivery_cost

    return {
        "total_price": round(total_price, 1),
        "discount": round(discount, 1),
        "commission": round(commission, 1),
        "net_receipt": round(net_receipt, 1),
        "total_cost": round(total_cost, 1),
        "profit": round(profit, 1),
    }

def enumerate_combos(store):
    """
    用 combinations_with_replacement 穷举该店所有 2–5 件的组合（同一菜可点多份），
    对每个组合算利润，返回全部组合 + 穿底组合清单，按利润从低到高排序。
    """
    skus = store["skus"]
    all_combos = []
    underwater_combos = []

    for r in range(2, 6):
        for combo in itertools.combinations_with_replacement(skus, r):
            metrics = calc_profit(store, combo)
            combo_record = {
                "skus": combo,
                "combo_text": format_combo_text(combo),
                "item_count": r,
                **metrics,
            }
            all_combos.append(combo_record)
            if metrics["profit"] < 0:
                underwater_combos.append(combo_record)

    # 按利润从低到高排（亏损最大排在前面）
    all_combos.sort(key=lambda x: x["profit"])
    underwater_combos.sort(key=lambda x: x["profit"])
    return all_combos, underwater_combos

def apply_fix(store):
    """
    按 FIX_RULE ('引流菜限购1份且不与满减同享') 重跑：
    1. 组合里引流菜超过 1 份的直接作废；
    2. 含引流菜（恰好 1 份）的组合不享受满减（满减按 0 算）；
    3. 不含引流菜的组合正常享受满减。
    返回修复后的穿底组合清单、穿底数量以及下降比例。
    """
    loss_leader_id = store.get("loss_leader_id")
    _, original_underwater = enumerate_combos(store)
    before_count = len(original_underwater)

    skus = store["skus"]
    fixed_underwater = []
    fixed_all_valid = []

    for r in range(2, 6):
        for combo in itertools.combinations_with_replacement(skus, r):
            loss_leader_count = sum(1 for s in combo if s["id"] == loss_leader_id)
            # 规则 1：引流菜超过 1 份直接作废
            if loss_leader_count > 1:
                continue

            # 规则 2：含引流菜（1 份）不与满减同享（满减按 0）
            if loss_leader_count == 1:
                metrics = calc_profit(store, combo, custom_discount=0.0)
            else:
                metrics = calc_profit(store, combo)

            combo_record = {
                "skus": combo,
                "combo_text": format_combo_text(combo),
                "item_count": r,
                **metrics,
            }
            fixed_all_valid.append(combo_record)
            if metrics["profit"] < 0:
                fixed_underwater.append(combo_record)

    fixed_underwater.sort(key=lambda x: x["profit"])
    after_count = len(fixed_underwater)
    
    if before_count > 0:
        decrease_pct = ((before_count - after_count) / before_count) * 100.0
    else:
        decrease_pct = 0.0

    return {
        "before_count": before_count,
        "after_count": after_count,
        "decrease_pct": round(decrease_pct, 1),
        "fixed_underwater": fixed_underwater,
    }

if __name__ == "__main__":
    print("=" * 75)
    print("MarginKeeper (MK) M2 活动穿底沙盘 — 求解器实跑运行")
    print("=" * 75)
    
    for store in MOCK_STORES:
        sid = store["store_id"]
        sname = store["store_name"]
        channel = "外卖" if store["channel"] == "takeaway" else "电商"
        
        all_combos, underwater = enumerate_combos(store)
        fix_res = apply_fix(store)
        
        print(f"\n【店铺 {sid}】{sname}（渠道: {channel}）")
        print(f"  - 人话规则: {store['rule_text']}")
        print(f"  - 规则翻译解析: {translate_rule(store['rule_text'])}")
        print(f"  - 穷举 2-5 件总组合数: {len(all_combos)} 种")
        print(f"  - 穿底组合数 (利润 < 0): {len(underwater)} 种 (穿底率: {len(underwater)/len(all_combos)*100:.1f}%)")
        print(f"  - Top 5 最亏组合 (亏损最大):")
        for i, c in enumerate(underwater[:5], 1):
            print(f"      {i}. {c['combo_text']} | 总价: ¥{c['total_price']} | 实收: ¥{c['net_receipt']} | 利润: ¥{c['profit']}")
        print(f"  - 修复建议: {FIX_RULE}")
        print(f"  - 修复后穿底组合数: {fix_res['after_count']} 种 (下降: {fix_res['decrease_pct']}%)")
    print("=" * 75)

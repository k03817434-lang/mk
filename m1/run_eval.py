# -*- coding: utf-8 -*-
"""m1/run_eval.py — M1 SpecDiff 50 题评测脚本
模板化生成 50 道商品质检题，执行确定性比对，输出控制台结果及 m1/eval_report.md。
"""
import os
import sys

# 避免 Windows 控制台输出编码问题
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m1.specdiff import diff_product

def generate_eval_cases():
    cases = []
    case_idx = 1

    # ==================== 1. 冲突类 20 条 (5 种模板 x 4 变体) ====================
    # 模板 1.1: 材质互换 (4 变体)
    m_variants = [
        ("C01", "纯棉休闲衬衫", "纯棉", "涤纶", "纯棉"),
        ("C02", "羊皮机车夹克", "羊皮", "PU人造革", "羊皮"),
        ("C03", "真丝印花丝巾", "真丝", "仿真丝涤纶", "真丝"),
        ("C04", "高弹运动长裤", "锦纶", "氨纶90%", "锦纶"),
    ]
    for cid, name, t_m, a_m, d_m in m_variants:
        cases.append({
            "id": f"EVAL-{case_idx:03d}", "name": name, "category": "服装",
            "title": f"热销款 {name}",
            "title_material": t_m, "attr_material": a_m, "detail_material": d_m,
            "title_net": None, "attr_net": None, "detail_net": None,
            "title_count": "1件", "attr_count": "1件", "detail_count": "1件",
            "title_shelf": None, "attr_shelf": None, "detail_shelf": None,
            "sku_pack": "单件装", "promo": "无",
            "gold": "conflict",
        })
        case_idx += 1

    # 模板 1.2: 净含量互换 (4 变体)
    net_variants = [
        ("C05", "浓缩洗衣液", "2kg", "1.5kg", "2kg"),
        ("C06", "纯正百花蜂蜜", "500g", "450g", "500g"),
        ("C07", "高山日照绿茶", "250g", "200g", "250g"),
        ("C08", "水果即食麦片", "1000g", "800g", "1000g"),
    ]
    for cid, name, t_n, a_n, d_n in net_variants:
        cases.append({
            "id": f"EVAL-{case_idx:03d}", "name": name, "category": "日化/食品",
            "title": f"特惠装 {name}",
            "title_material": None, "attr_material": None, "detail_material": None,
            "title_net": t_n, "attr_net": a_n, "detail_net": d_n,
            "title_count": "1袋", "attr_count": "1袋", "detail_count": "1袋",
            "title_shelf": "12个月", "attr_shelf": "12个月", "detail_shelf": "12个月",
            "sku_pack": "单袋装", "promo": "无",
            "gold": "conflict",
        })
        case_idx += 1

    # 模板 1.3: 保质期互换 (4 变体)
    shelf_variants = [
        ("C09", "纯鲜牛奶", "6个月", "3个月", "6个月"),
        ("C10", "麻辣素毛肚", "12个月", "6个月", "12个月"),
        ("C11", "提拉米苏蛋糕", "30天", "15天", "30天"),
        ("C12", "特调牛肉酱", "18个月", "12个月", "18个月"),
    ]
    for cid, name, t_s, a_s, d_s in shelf_variants:
        cases.append({
            "id": f"EVAL-{case_idx:03d}", "name": name, "category": "食品",
            "title": f"新鲜直达 {name}",
            "title_material": None, "attr_material": None, "detail_material": None,
            "title_net": "300g", "attr_net": "300g", "detail_net": "300g",
            "title_count": "1盒", "attr_count": "1盒", "detail_count": "1盒",
            "title_shelf": t_s, "attr_shelf": a_s, "detail_shelf": d_s,
            "sku_pack": "单盒装", "promo": "无",
            "gold": "conflict",
        })
        case_idx += 1

    # 模板 1.4: 件数互换（买一送一 vs 单件装）(4 变体)
    count_variants = [
        ("C13", "软毛电动牙刷", "买一送一", "2件", "1件", "2件"),
        ("C14", "香氛沐浴露", "买一送一", "2瓶", "1瓶", "2瓶"),
        ("C15", "原木抽纸整箱", "买一送一", "2提", "1提", "2提"),
        ("C16", "去屑洗发水", "买一送一", "2瓶", "1瓶", "2瓶"),
    ]
    for cid, name, promo, t_c, a_c, d_c in count_variants:
        cases.append({
            "id": f"EVAL-{case_idx:03d}", "name": name, "category": "百货",
            "title": f"{name} {promo}",
            "title_material": None, "attr_material": None, "detail_material": None,
            "title_net": None, "attr_net": None, "detail_net": None,
            "title_count": t_c, "attr_count": a_c, "detail_count": d_c,
            "title_shelf": None, "attr_shelf": None, "detail_shelf": None,
            "sku_pack": "单件装", "promo": promo,
            "gold": "conflict",
        })
        case_idx += 1

    # 模板 1.5: 百分比互换 (4 变体)
    pct_variants = [
        ("C17", "羊绒针织衫", "100%羊绒", "羊绒50%", "100%羊绒"),
        ("C18", "手工蚕丝被", "100%桑蚕丝", "蚕丝20%", "100%桑蚕丝"),
        ("C19", "极寒加厚羽绒服", "90%白鹅绒", "鹅绒50%", "90%白鹅绒"),
        ("C20", "透气亚麻衬衫", "100%亚麻", "亚麻40%", "100%亚麻"),
    ]
    for cid, name, t_m, a_m, d_m in pct_variants:
        cases.append({
            "id": f"EVAL-{case_idx:03d}", "name": name, "category": "家纺/女装",
            "title": f"高端品质 {name}",
            "title_material": t_m, "attr_material": a_m, "detail_material": d_m,
            "title_net": None, "attr_net": None, "detail_net": None,
            "title_count": "1件", "attr_count": "1件", "detail_count": "1件",
            "title_shelf": None, "attr_shelf": None, "detail_shelf": None,
            "sku_pack": "单件装", "promo": "无",
            "gold": "conflict",
        })
        case_idx += 1

    # ==================== 2. 合规类 20 条 (10 个模板 x 2 变体) ====================
    comp_templates = [
        ("基础圆领T恤", "女装", "纯棉", "200g", "1件", None, "单件装"),
        ("精品原味坚果", "食品", None, "500g", "1袋", "12个月", "单袋装"),
        ("304不锈钢保温杯", "日用", "304不锈钢", "500ml", "1个", None, "单个装"),
        ("东北五常大米", "食品", None, "5kg", "1袋", "12个月", "单袋装"),
        ("透气网面跑鞋", "鞋靴", "网布", None, "1双", None, "单双装"),
        ("复古微喇牛仔裤", "女装", "牛仔布", None, "1条", None, "单件装"),
        ("非转基因压榨花生油", "食品", None, "5L", "1桶", "18个月", "单桶装"),
        ("北欧风陶瓷马克杯", "家居", "陶瓷", "400ml", "1个", None, "单个装"),
        ("原生木浆抽纸整箱", "日用", None, None, "10包", None, "整箱装"),
        ("速干运动短裤", "男装", "涤纶", None, "1件", None, "单件装"),
    ]
    for t_idx, (t_name, cat, mat, net, cnt, shf, pack) in enumerate(comp_templates, 1):
        for var_idx in (1, 2):
            v_name = f"{t_name} 款式{var_idx}"
            cases.append({
                "id": f"EVAL-{case_idx:03d}", "name": v_name, "category": cat,
                "title": f"正品保证 {v_name}",
                "title_material": mat, "attr_material": mat, "detail_material": mat,
                "title_net": net, "attr_net": net, "detail_net": net,
                "title_count": cnt, "attr_count": cnt, "detail_count": cnt,
                "title_shelf": shf, "attr_shelf": shf, "detail_shelf": shf,
                "sku_pack": pack, "promo": "无",
                "gold": "compliant",
            })
            case_idx += 1

    # ==================== 3. 模糊类 10 条 (5 个模板 x 2 变体) ====================
    fuzzy_templates = [
        ("休闲风衣外套", "女装", "未注明", "其他/见包装", "未注明", None, None, None, "单件装"),
        ("时尚针织开衫", "女装", "其他", "其他/见包装", "其他", None, None, None, "单件装"),
        ("风味爆米花", "食品", None, None, None, "超大份", None, "超大份", "单袋装"),
        ("手工蔓越莓曲奇", "食品", None, None, None, "大包特惠", None, "大包特惠", "单袋装"),
        ("加绒防风保暖衣", "内衣", "见包装", "见包装", "其他", None, None, None, "单件装"),
    ]
    for f_idx, (f_name, cat, tm, am, dm, tn, an, dn, pack) in enumerate(fuzzy_templates, 1):
        for var_idx in (1, 2):
            v_name = f"{f_name} 系列{var_idx}"
            cases.append({
                "id": f"EVAL-{case_idx:03d}", "name": v_name, "category": cat,
                "title": f"特价清仓 {v_name}",
                "title_material": tm, "attr_material": am, "detail_material": dm,
                "title_net": tn, "attr_net": an, "detail_net": dn,
                "title_count": "1件", "attr_count": "1件", "detail_count": "1件",
                "title_shelf": None, "attr_shelf": None, "detail_shelf": None,
                "sku_pack": pack, "promo": "无",
                "gold": "fuzzy",
            })
            case_idx += 1

    return cases

def run_evaluation():
    cases = generate_eval_cases()
    total = len(cases)
    correct = 0
    category_stats = {
        "conflict": {"total": 0, "correct": 0, "name": "冲突类 (拦截)"},
        "compliant": {"total": 0, "correct": 0, "name": "合规类 (通过)"},
        "fuzzy": {"total": 0, "correct": 0, "name": "模糊类 (人工核验)"},
    }
    
    wrong_cases = []

    for c in cases:
        res = diff_product(c)
        gold = c["gold"]
        pred = res["verdict"]
        
        category_stats[gold]["total"] += 1
        if pred == gold:
            correct += 1
            category_stats[gold]["correct"] += 1
        else:
            wrong_cases.append({
                "id": c["id"],
                "name": c["name"],
                "gold": gold,
                "pred": pred,
            })

    accuracy = (correct / total) * 100.0 if total > 0 else 0.0

    # 1. 终端打印
    print("=" * 65)
    print("MarginKeeper (MK) M1 SpecDiff 上架质检 — 50 题评测结果")
    print("=" * 65)
    print(f"总题数: {total} 道 | 做对: {correct} 道 | 总体准确率: {accuracy:.1f}%\n")
    print("分项评测结果:")
    for g_key, stat in category_stats.items():
        g_tot = stat["total"]
        g_cor = stat["correct"]
        g_acc = (g_cor / g_tot) * 100.0 if g_tot > 0 else 0.0
        print(f"  - {stat['name']}: {g_cor}/{g_tot} ({g_acc:.1f}%)")

    if wrong_cases:
        print("\n错题清单:")
        for w in wrong_cases:
            print(f"  - [{w['id']}] {w['name']}: 期望={w['gold']}, 预测={w['pred']}")
    else:
        print("\n错题清单: 无错题（全部命中标准答案）")

    caveat = "50 题为模板构造集，判对率高不代表真实检出率，只证明比对管线跑通；真实验证需要真实商品数据。"
    print(f"\n【重要声明】: {caveat}")
    print("=" * 65)

    # 2. 输出 m1/eval_report.md
    report_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eval_report.md")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# M1 SpecDiff 上架质检评测报告\n\n")
        f.write("> **特别声明**：50 题为模板构造集，判对率高不代表真实检出率，只证明比对管线跑通；真实验证需要真实商品数据。\n\n")
        f.write("## 1. 总体指标概览\n\n")
        f.write(f"- **总评测样本数**：{total} 道商品上架质检用例\n")
        f.write(f"- **正确判别数**：{correct} 道\n")
        f.write(f"- **总体判定准确率**：**{accuracy:.1f}%**\n\n")
        f.write("## 2. 细分项判别统计\n\n")
        f.write("| 分类 | 对应裁决 | 样本数 | 命中数 | 分项准确率 |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for g_key, stat in category_stats.items():
            g_tot = stat["total"]
            g_cor = stat["correct"]
            g_acc = (g_cor / g_tot) * 100.0 if g_tot > 0 else 0.0
            f.write(f"| `{g_key}` | {stat['name']} | {g_tot} | {g_cor} | {g_acc:.1f}% |\n")
        
        f.write("\n## 3. 错题明细记录\n\n")
        if wrong_cases:
            f.write("| 样本编号 | 商品名称 | 预期目标 (gold) | 预测结果 |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for w in wrong_cases:
                f.write(f"| `{w['id']}` | {w['name']} | `{w['gold']}` | `{w['pred']}` |\n")
        else:
            f.write("本次 50 道模板用例全部命中预期裁决，无未决或误判样本。\n\n")

        f.write("## 4. 架构与测试声明\n\n")
        f.write(f"- **真实性说明**：{caveat}\n")
        f.write("- **算法特性**：本评测全流程基于确定性规则与交叉字段比对，不调用外部大模型 API，保证 100% 毫秒级确定性响应与 0 算力费用。\n")

    print(f"\n评测报告已成功写入: {report_file}")
    return accuracy, category_stats

if __name__ == "__main__":
    run_evaluation()

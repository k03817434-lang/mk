# -*- coding: utf-8 -*-
"""m1/specdiff.py — M1 SpecDiff 商品上架确定性质检比对引擎
纯确定性代码，不调大模型 API。
"""
import os
import sys

# 保证项目根目录在 sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m1.mock_products import RULES, FUZZY_MARKERS

SINGLE_PACKS = ("单件装", "单个装", "单双装", "单袋装", "单盒装")

FIELD_NAMES = [
    ("material", "材质"),
    ("net", "净含量"),
    ("count", "件数"),
    ("shelf", "保质期"),
]

def llm_adjudicate_stub():
    """
    LLM 语义裁决桩函数：
    Demo 阶段确定性比对已覆盖全部 12 个案例，LLM 语义裁决留到集成时接 Qwen-Turbo
    （JSON Only，只判冲突字段对，不直接算账）。不要真的调 API。
    """
    return None

def find_rule(field_name, status, vals, promo="", sku_pack=""):
    """按字段查 RULES 获取对应规则"""
    rule_map = {r["id"]: r for r in RULES}
    
    if status == "fuzzy":
        if field_name == "材质":
            return rule_map.get("R5")
        elif field_name == "净含量":
            return rule_map.get("R6")
        return None

    if status == "conflict":
        if field_name == "材质":
            # 百分比冲突用 R8，否则优先 R1
            val_str = " ".join(str(v) for v in vals if v)
            if "%" in val_str:
                return rule_map.get("R8")
            return rule_map.get("R1")
        elif field_name == "件数":
            return rule_map.get("R3")
        elif field_name == "保质期":
            return rule_map.get("R4")
        elif field_name == "净含量":
            return rule_map.get("R2")
            
    return None

def generate_suggestion(field_name, status, t_val, a_val, d_val, promo="", sku_pack=""):
    """生成一句话修正建议"""
    if status == "fuzzy":
        if field_name == "材质":
            return "材质写成具体成分，不要写其他/见包装"
        elif field_name == "净含量":
            return "净含量补全具体数值与单位，不要写超大份等模糊描述"
        return f"{field_name}存在模糊或缺失表述，请补全具体信息"

    if status == "conflict":
        if field_name == "件数" and ("买一送一" in promo or "买一送一" in str(t_val)):
            return "标题写买一送一，但SKU规格为单件装，请修改SKU包装为多件装或调整活动描述"
        
        if t_val == d_val and a_val and t_val != a_val:
            return f"标题与详情写{t_val}，属性表写{a_val}，统一改成{a_val}再上架"
        
        return f"标题写{t_val}，属性写{a_val}，详情写{d_val}，三处不一致，请统一后再上架"

    return "三处字段信息一致，符合上架规范"

def diff_product(product):
    """
    对单个商品执行比对检查：
    比对 4 个字段：材质、净含量、件数、保质期。
    返回比对明细、最终裁决、命中规则与一句话建议。
    """
    field_diffs = []
    has_conflict = False
    has_fuzzy = False
    hit_rules = []
    suggestions = []

    promo = product.get("promo", "") or ""
    sku_pack = product.get("sku_pack", "") or ""
    title = product.get("title", "") or ""

    for key, name in FIELD_NAMES:
        t_val = product.get(f"title_{key}")
        a_val = product.get(f"attr_{key}")
        d_val = product.get(f"detail_{key}")

        # 三处都为 None 则该字段不适用，跳过
        if t_val is None and a_val is None and d_val is None:
            continue

        raw_vals = [t_val, a_val, d_val]
        
        # 1. 检查 fuzzy: 必填缺失（部分为 None 部分不是）或含有模糊词
        is_missing = any(v is None for v in raw_vals) and not all(v is None for v in raw_vals)
        has_fuzzy_word = any(
            any(marker in str(v) for marker in FUZZY_MARKERS)
            for v in raw_vals if v is not None
        )

        field_status = "ok"
        if is_missing or has_fuzzy_word:
            field_status = "fuzzy"
            has_fuzzy = True
        else:
            # 2. 检查非 None 去重后是否多于 1 个不同值
            non_none = [v for v in raw_vals if v is not None]
            if len(set(non_none)) > 1:
                field_status = "conflict"
                has_conflict = True
            
            # 3. 件数额外规则：买一送一 vs 单件装
            if key == "count":
                if ("买一送一" in promo or "买一送一" in title) and sku_pack in SINGLE_PACKS:
                    field_status = "conflict"
                    has_conflict = True

        rule = None
        sug = None
        if field_status != "ok":
            rule = find_rule(name, field_status, raw_vals, promo, sku_pack)
            if rule and rule not in hit_rules:
                hit_rules.append(rule)
            sug = generate_suggestion(name, field_status, t_val, a_val, d_val, promo, sku_pack)
            if sug and sug not in suggestions:
                suggestions.append(sug)

        field_diffs.append({
            "key": key,
            "name": name,
            "title_val": t_val if t_val is not None else "-",
            "attr_val": a_val if a_val is not None else "-",
            "detail_val": d_val if d_val is not None else "-",
            "status": field_status,  # ok, conflict, fuzzy
            "rule": rule,
            "suggestion": sug,
        })

    # 裁决判断
    if has_conflict:
        verdict = "conflict"
        verdict_zh = "拦截"
    elif has_fuzzy:
        verdict = "fuzzy"
        verdict_zh = "人工核验"
    else:
        verdict = "compliant"
        verdict_zh = "通过"

    summary_suggestion = "；".join(suggestions) if suggestions else "三处字段信息一致，符合规范，准予上架。"

    return {
        "id": product.get("id"),
        "name": product.get("name"),
        "category": product.get("category"),
        "title": title,
        "sku_pack": sku_pack,
        "promo": promo,
        "gold": product.get("gold"),
        "verdict": verdict,
        "verdict_zh": verdict_zh,
        "field_diffs": field_diffs,
        "hit_rules": hit_rules,
        "suggestion": summary_suggestion,
    }

if __name__ == "__main__":
    from m1.mock_products import PRODUCTS
    for p in PRODUCTS:
        res = diff_product(p)
        print(f"[{res['id']}] {res['name']}: 预测={res['verdict_zh']} (gold={res['gold']}) | 命中规则={[r['id'] for r in res['hit_rules']]} | 建议={res['suggestion']}")

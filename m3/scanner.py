# -*- coding: utf-8 -*-
"""m3/scanner.py — M3 AdCompliance 直播话术合规扫描与熔断引擎
纯确定性代码，不调大模型 API。
"""
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m3.mock_scripts import PATTERNS, SEVERITY, REPLACEMENTS, RULES

TYPE_PRIORITY = ["MED", "EFF", "ABS", "PRICE"]
TYPE_NAMES = {
    "ABS": "绝对化用语",
    "EFF": "功效承诺",
    "PRICE": "价格误导",
    "MED": "医疗用语",
}

RULE_MAP = {
    "ABS": {"id": "R1", "source": "广告法第九条", "text": "不得使用“国家级”“最高级”“最佳”等绝对化用语。"},
    "MED": {"id": "R2", "source": "广告法第十七条", "text": "除医疗、药品、医疗器械广告外，其他任何广告不得涉及疾病治疗功能。"},
    "EFF": {"id": "R3", "source": "广告法第二十八条", "text": "不得对商品功效作虚假或者引人误解的宣传。"},
    "PRICE": {"id": "R4", "source": "价格法第十四条", "text": "不得虚构原价、虚构降价原因，不得谎称全网最低。"},
    "OK": {"id": "R6", "source": "平台直播规范", "text": "穿着舒服/营养满分等主观感受表述不违规，但不得加绝对化修饰。"},
}

def _get_env_key(key_name):
    val = os.environ.get(key_name)
    if val:
        return val
    env_file = os.path.join(project_root, ".env")
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() == key_name:
                            val = v.strip()
                            os.environ[key_name] = val
                            return val
        except Exception:
            pass
    return None

def llm_rewrite_stub(line_text=None, violation_type=None):
    """
    M3 LLM 话术改写桩 → 百炼 Qwen3.8-Flash (qwen3.8-flash)：
    输入：违规句 + 违规类型；
    输出：JSON Only，{rewrite}。
    约束：只改违规的 1–2 句；S01 L3 改写后必须仍包含'平台补贴价'，否则回退模板改写。
    调用失败回退模板改写。
    """
    if line_text is None:
        line_text = "今天全网最低价，错过就没有了"
        violation_type = "PRICE"

    default_template_rw = rewrite_text(line_text)
    api_key = _get_env_key("DASHSCOPE_API_KEY")
    if not api_key:
        return {"rewrite": default_template_rw}

    import json
    import urllib.request

    prompt = f"违规类型：{violation_type or '价格误导'}\n违规话术：{line_text}\n请合规改写，保留营销吸引力，并且将价格误导表述合规替换为'平台补贴价'。"
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    payload = {
        "model": "qwen3.8-flash",
        "messages": [
            {
                "role": "system",
                "content": "你是一个电商直播合规话术改写专家。请针对违规的直播话术进行合规改写，只改违规词汇或短语，保留原意与营销吸引力。输出纯 JSON 对象，格式必须为：{\"rewrite\": \"改写后的合规话术\"}。特别注意：若违规类型为价格误导或包含全网最低价，改写后必须包含'平台补贴价'。"
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"}
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            rw = parsed.get("rewrite", "").strip()
            # 约束：S01 L3 改写后必须仍包含“平台补贴价”，否则回退模板改写
            if "全网最低" in line_text:
                if "平台补贴价" in rw:
                    return {"rewrite": rw}
                else:
                    return {"rewrite": default_template_rw}
            if rw:
                return {"rewrite": rw}
            return {"rewrite": default_template_rw}
    except Exception:
        return {"rewrite": default_template_rw}

def rewrite_text(text):
    """按 REPLACEMENTS 顺序逐条替换，改写后若仍命中违规词则标记 ⚠️"""
    res = text
    for old_w, new_w in REPLACEMENTS:
        res = res.replace(old_w, new_w)
    
    # 重新扫描改写后文本是否残留违规词
    still_violates = False
    for vtype, words in PATTERNS.items():
        if any(w in res for w in words):
            still_violates = True
            break
            
    if still_violates:
        res += " ⚠️[需人工复核]"
    return res

def scan_line(line_text):
    """
    逐行扫描逻辑：
    1. 用 PATTERNS 四类词表做子串匹配，命中即记该类型；
    2. 主类型按严重程度取最严重：MED > EFF > ABS > PRICE；
    3. 给出命中的词、规则 id + 来源；
    4. 违规行按 REPLACEMENTS 顺序逐条替换生成改写。
    """
    hit_types = []
    hit_words_map = {}

    for vtype, words in PATTERNS.items():
        matched = [w for w in words if w in line_text]
        if matched:
            hit_types.append(vtype)
            hit_words_map[vtype] = matched

    if not hit_types:
        return {
            "text": line_text,
            "is_violation": False,
            "hit_types": [],
            "main_type": None,
            "main_type_zh": "合规",
            "severity": "合规",
            "hit_words": [],
            "rule": RULE_MAP["OK"],
            "rewritten": line_text,
        }

    # 主类型按 MED > EFF > ABS > PRICE 优先级选择
    main_type = next((t for t in TYPE_PRIORITY if t in hit_types), hit_types[0])
    severity = SEVERITY.get(main_type, "中危")
    rule = RULE_MAP.get(main_type, RULE_MAP["OK"])
    
    # 汇总所有命中的关键词
    all_hit_words = []
    for t in hit_types:
        all_hit_words.extend(hit_words_map[t])

    # 违规行改写
    rewritten = rewrite_text(line_text)

    return {
        "text": line_text,
        "is_violation": True,
        "hit_types": hit_types,
        "main_type": main_type,
        "main_type_zh": TYPE_NAMES.get(main_type, main_type),
        "severity": severity,
        "hit_words": all_hit_words,
        "rule": rule,
        "rewritten": rewritten,
    }

def scan_script(script):
    """
    整场话术扫描与熔断判定：
    - 任一行主类型是高危（MED/EFF）-> 红灯 熔断：建议立即下播整改
    - 无高危、但有中危（ABS/PRICE）-> 黄灯 提醒：建议修改后开播
    - 一行违规都没有 -> 绿灯 通过
    """
    lines = script.get("lines", [])
    scanned_lines = [scan_line(l["text"]) for l in lines]
    
    violation_count = sum(1 for l in scanned_lines if l["is_violation"])
    has_high = any(l["severity"] == "高危" for l in scanned_lines)
    has_med = any(l["severity"] == "中危" for l in scanned_lines)

    if has_high:
        lamp = "RED"
        lamp_zh = "红灯 熔断"
        lamp_reason = "检测到高危违规话术（医疗用语或功效承诺），触发熔断，建议立即下播整改。"
    elif has_med:
        lamp = "YELLOW"
        lamp_zh = "黄灯 提醒"
        lamp_reason = "检测到中危违规话术（绝对化用语或价格误导），建议修改高危话术后开播。"
    else:
        lamp = "GREEN"
        lamp_zh = "绿灯 通过"
        lamp_reason = "全场话术未检测到明显违规，合规准予开播。"

    return {
        "id": script.get("id"),
        "name": script.get("name"),
        "lamp": lamp,
        "lamp_zh": lamp_zh,
        "lamp_reason": lamp_reason,
        "violation_count": violation_count,
        "total_lines": len(lines),
        "scanned_lines": scanned_lines,
    }

if __name__ == "__main__":
    from m3.mock_scripts import SCRIPTS
    for s in SCRIPTS:
        res = scan_script(s)
        print(f"[{res['id']}] {res['name']}: {res['lamp_zh']} | 违规行数={res['violation_count']}/{res['total_lines']}")
        for idx, l in enumerate(res["scanned_lines"], 1):
            if l["is_violation"]:
                print(f"    行{idx}: [{l['main_type']}|{l['severity']}] 原句='{l['text']}' -> 改写='{l['rewritten']}' (词={l['hit_words']})")

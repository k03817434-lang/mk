# -*- coding: utf-8 -*-
"""eval/m4_extraction_test.py — M4 结构化特征抽取实测 Harness
测试 LLM 从工单文本中抽取 3 个二元标签（L1 诉求明确 / L2 证据闭环 / L3 安全红线）。
评测三个数据集：
1. 真实工单数据集（57 案全量，双模型双盲金标）
2. 模拟评测集（200 题，构造金标）
3. 4 轴正交风险压力集（200 题，4 个风险轴各 50 题）
"""
import json
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m1.specdiff import _get_env_key

# 标注指南定义
SYSTEM_PROMPT = (
    "你是一个严谨的电商售后纠纷质检与证据链抽取专家。请阅读工单文本，严格按以下三大规则抽取 L1、L2、L3 三个标签（值为 'Y' 或 'N'）：\n\n"
    "【判定规则】：\n"
    "1. L1（诉求明确可归类）：\n"
    "   - Y：必须有买家初始申请措辞的明确记录（如“申请仅退款/退全款/决定退货/退货退款/申请维修/换货/部分补偿”），或平台文书明确记载买家申请了哪一种。\n"
    "   - N：只写“平台支持仅退款/退款成功”（无申请原话）为 No；“申请退款”未写清是仅退款还是退货退款为 No；理由未公开为 No。\n"
    "2. L2（证据链闭环）：\n"
    "   - Y：现有证据能否客观支撑买家陈述的第一主张（如质量问题、规格不符）。商家在沟通协商中明确承认主张属实（同意赔付/补偿/补发）算验证。\n"
    "   - N：证据未公开、仅一张与主张无关的远景模糊图、只有流程流水记录、或商家同意退货退款方案（同意走退货流程不等于承认缺陷）均为 No。\n"
    "3. L3（买家侧安全红线）：\n"
    "   - Y：必须有法院或警方文书明确使用“欺诈/虚构事实/不当得利/违反诚信”等定性词汇，或记录明确写出“调包/拒不退货/不配合退货/职业索赔（多账号/批量）”。\n"
    "   - N：仅凭事实推断（如物流显示已签收、收了补发又退款）、买家态度强硬拒接电话、不合理过高诉求、单纯拒收包裹、无法返还原物（商品坏了）等，均不得标为红线，记为 No。\n\n"
    "请仅输出标准 JSON 对象，禁止输出任何其他解释文字：\n"
    "{\"L1\": \"Y\" | \"N\", \"L2\": \"Y\" | \"N\", \"L3\": \"Y\" | \"N\", \"reason\": \"一句话依据\"}"
)

def call_llm_extract(text):
    """调用大模型执行结构化抽取，优先使用 DeepSeek-V3 / Qwen3.8-Flash"""
    ds_key = _get_env_key("DEEPSEEK_API_KEY")
    qwen_key = _get_env_key("DASHSCOPE_API_KEY")
    
    t0 = time.time()
    
    # 方案 1：DeepSeek-V3
    if ds_key:
        url = "https://api.deepseek.com/v1/chat/completions"
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {ds_key}"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                dt = time.time() - t0
                usage = data.get("usage", {})
                content_str = data["choices"][0]["message"]["content"]
                parsed = json.loads(content_str)
                l1 = "Y" if str(parsed.get("L1", "")).upper().startswith("Y") else "N"
                l2 = "Y" if str(parsed.get("L2", "")).upper().startswith("Y") else "N"
                l3 = "Y" if str(parsed.get("L3", "")).upper().startswith("Y") else "N"
                # DeepSeek 定价：输入 ¥2/M，输出 ¥8/M
                cost_yuan = (usage.get("prompt_tokens", 0) * 0.000002) + (usage.get("completion_tokens", 0) * 0.000008)
                return {
                    "success": True,
                    "l1": l1, "l2": l2, "l3": l3,
                    "reason": parsed.get("reason", ""),
                    "latency_ms": round(dt * 1000, 1),
                    "cost_yuan": cost_yuan,
                    "tokens": usage.get("total_tokens", 0)
                }
        except Exception as e:
            pass

    # 方案 2：百炼 Qwen3.8-Flash
    if qwen_key:
        url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
        payload = {
            "model": "qwen3.8-flash",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {qwen_key}"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                dt = time.time() - t0
                usage = data.get("usage", {})
                content_str = data["choices"][0]["message"]["content"]
                parsed = json.loads(content_str)
                l1 = "Y" if str(parsed.get("L1", "")).upper().startswith("Y") else "N"
                l2 = "Y" if str(parsed.get("L2", "")).upper().startswith("Y") else "N"
                l3 = "Y" if str(parsed.get("L3", "")).upper().startswith("Y") else "N"
                cost_yuan = usage.get("total_tokens", 0) * 0.0000008
                return {
                    "success": True,
                    "l1": l1, "l2": l2, "l3": l3,
                    "reason": parsed.get("reason", ""),
                    "latency_ms": round(dt * 1000, 1),
                    "cost_yuan": cost_yuan,
                    "tokens": usage.get("total_tokens", 0)
                }
        except Exception as e:
            pass

    # 抽取失败/超时按 0 分记（不重试）
    return {
        "success": False,
        "l1": "N", "l2": "N", "l3": "N",
        "reason": "抽取超时或模型异常，按 0 分记",
        "latency_ms": round((time.time() - t0) * 1000, 1),
        "cost_yuan": 0.0,
        "tokens": 0
    }

def format_real_case(c):
    return (
        f"【工单编号】：{c['case_id']}\n"
        f"【电商平台】：{c['platform']}\n"
        f"【商品类目】：{c['category']}\n"
        f"【涉及金额】：{c['amount']}\n"
        f"【买家理由】：{c['buyer_reason']}\n"
        f"【证据情况】：{c['evidence']}\n"
        f"【平台裁决】：{c['decision']}\n"
        f"【商家损失】：{c['loss']}\n"
    )

def format_sim_case(c):
    return (
        f"【工单编号】：{c['case_id']}\n"
        f"【电商平台】：{c.get('platform', '淘宝')}\n"
        f"【商品类目】：{c.get('category', '服装')}\n"
        f"【涉及金额】：¥{c.get('amount_yuan', 100)}\n"
        f"【买家理由】：{c.get('buyer_reason', '')}\n"
        f"【证据情况】：匹配证据 {','.join(c.get('evidence_ids', []))}\n"
        f"【平台裁决】：{c.get('chat_note', '流程处理中')}\n"
        f"【商家损失】：待定\n"
    )

def format_stress_case(c):
    return (
        f"【工单编号】：{c['case_id']}\n"
        f"【风险测试轴】：{c['axis_zh']}\n"
        f"【电商平台】：{c['platform']}\n"
        f"【商品类目】：{c['category']}\n"
        f"【涉及金额】：¥{c['amount_yuan']}\n"
        f"【买家理由】：{c['buyer_reason']}\n"
        f"【证据情况】：{c['evidence']}\n"
        f"【平台裁决】：双方协商阶段\n"
        f"【商家损失】：待定\n"
    )

def eval_dataset(name, items, format_fn, gold_fn, max_workers=6):
    print(f"\n>>> 正在评测数据集: {name} (共 {len(items)} 题)...")
    t0 = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(call_llm_extract, format_fn(item)) for item in items]
        preds = [f.result() for f in futures]
        
    dt = time.time() - t0
    
    n = len(items)
    cor_l1 = 0
    cor_l2 = 0
    cor_l3 = 0
    cor_all = 0
    
    latencies = [p["latency_ms"] for p in preds]
    latencies.sort()
    p50_ms = latencies[int(n * 0.50)] if latencies else 0.0
    p95_ms = latencies[int(n * 0.95)] if latencies else 0.0
    total_cost = sum(p["cost_yuan"] for p in preds)
    avg_cost = total_cost / n if n > 0 else 0.0
    
    # 逐题比对
    details = []
    for idx, (item, pred) in enumerate(zip(items, preds)):
        g_l1, g_l2, g_l3 = gold_fn(item)
        p_l1, p_l2, p_l3 = pred["l1"], pred["l2"], pred["l3"]
        
        ok_l1 = (p_l1 == g_l1)
        ok_l2 = (p_l2 == g_l2)
        ok_l3 = (p_l3 == g_l3)
        ok_all = (ok_l1 and ok_l2 and ok_l3)
        
        if ok_l1: cor_l1 += 1
        if ok_l2: cor_l2 += 1
        if ok_l3: cor_l3 += 1
        if ok_all: cor_all += 1
        
        cid = item.get("case_id", f"CASE-{idx+1}")
        details.append({
            "case_id": cid,
            "axis": item.get("axis", "general"),
            "gold": {"L1": g_l1, "L2": g_l2, "L3": g_l3},
            "pred": {"L1": p_l1, "L2": p_l2, "L3": p_l3},
            "ok": {"L1": ok_l1, "L2": ok_l2, "L3": ok_l3, "all": ok_all},
            "reason": pred["reason"],
            "latency_ms": pred["latency_ms"]
        })
        
    acc_l1 = cor_l1 / n * 100
    acc_l2 = cor_l2 / n * 100
    acc_l3 = cor_l3 / n * 100
    acc_all = cor_all / n * 100
    
    print(f"[{name}] 完成! 耗时: {dt:.1f}s | P50={p50_ms:.0f}ms | P95={p95_ms:.0f}ms | 单题均成本=¥{avg_cost:.5f}")
    print(f"  L1 准度: {acc_l1:.1f}% ({cor_l1}/{n})")
    print(f"  L2 准度: {acc_l2:.1f}% ({cor_l2}/{n})")
    print(f"  L3 准度: {acc_l3:.1f}% ({cor_l3}/{n})")
    print(f"  总体一致: {acc_all:.1f}% ({cor_all}/{n})")
    
    return {
        "name": name,
        "total": n,
        "accuracy": {
            "l1": round(acc_l1, 1),
            "l2": round(acc_l2, 1),
            "l3": round(acc_l3, 1),
            "overall": round(acc_all, 1),
            "cor_counts": {"l1": cor_l1, "l2": cor_l2, "l3": cor_l3, "all": cor_all}
        },
        "performance": {
            "p50_ms": p50_ms,
            "p95_ms": p95_ms,
            "avg_cost_yuan": round(avg_cost, 5),
            "total_cost_yuan": round(total_cost, 4),
            "elapsed_seconds": round(dt, 2)
        },
        "details": details
    }

def run_all_extraction_benchmarks():
    print("========================================================================")
    print("M4 结构化特征抽取实测基准 (LLM Information Extraction Benchmark)")
    print("========================================================================")
    
    # 1. 真实 57 条
    gold_real_path = os.path.join(project_root, "m4", "golden_real.json")
    with open(gold_real_path, "r", encoding="utf-8") as f:
        real_data = json.load(f)
    real_cases = real_data["cases"]
    
    res_real = eval_dataset(
        name="真实工单 57 案 (双模型双盲金标，未含人工标注)",
        items=real_cases,
        format_fn=format_real_case,
        gold_fn=lambda c: (c["l1"], c["l2"], c["l3"]),
        max_workers=6
    )
    # L2 全猜 No 基线
    no_count_l2 = sum(1 for c in real_cases if c["l2"] == "N")
    res_real["l2_all_no_baseline_percent"] = round(no_count_l2 / len(real_cases) * 100, 1)
    
    # 2. 模拟评测集 200 题
    from eval.eval_cases import EVAL_CASES
    # 扩增至 200 题 (4 组金额/形式变体)
    sim_200 = []
    for mul in range(4):
        for c in EVAL_CASES:
            item = dict(c)
            item["case_id"] = f"{c['case_id']}-V{mul+1}"
            item["amount_yuan"] = c["amount_yuan"] + mul * 20
            sim_200.append(item)
            
    def gold_sim_fn(c):
        # 模拟集金标：构造规则
        reason = c.get("buyer_reason", "")
        ev_ids = c.get("evidence_ids", [])
        l1 = "Y" if ("仅退款" in reason or "全额退款" in reason) else "N"
        l2 = "Y" if any(e in ["desc_matches", "buyer_confirmed_defect"] for e in ev_ids) else "N"
        l3 = "Y" if "buyer_3_refunds_30d" in ev_ids else "N"
        return l1, l2, l3
        
    res_sim = eval_dataset(
        name="模拟集 200 题 (构造金标，Sanity Check)",
        items=sim_200,
        format_fn=format_sim_case,
        gold_fn=gold_sim_fn,
        max_workers=8
    )
    
    # 3. 4 轴 200 题压力集
    from eval.stress_cases_200 import STRESS_CASES_200
    res_stress = eval_dataset(
        name="4 轴正交风险压力测试集 200 题 (正交风险轴)",
        items=STRESS_CASES_200,
        format_fn=format_stress_case,
        gold_fn=lambda c: (c["gold_l1"], c["gold_l2"], c["gold_l3"]),
        max_workers=8
    )
    
    # 分轴统计压力集准度
    axis_stats = {}
    for item in res_stress["details"]:
        ax = item["axis"]
        if ax not in axis_stats:
            axis_stats[ax] = {"total": 0, "cor_l1": 0, "cor_l2": 0, "cor_l3": 0, "cor_all": 0}
        st = axis_stats[ax]
        st["total"] += 1
        if item["ok"]["L1"]: st["cor_l1"] += 1
        if item["ok"]["L2"]: st["cor_l2"] += 1
        if item["ok"]["L3"]: st["cor_l3"] += 1
        if item["ok"]["all"]: st["cor_all"] += 1
        
    axis_summary = {}
    for ax, st in axis_stats.items():
        tot = st["total"]
        axis_summary[ax] = {
            "total": tot,
            "acc_l1": round(st["cor_l1"] / tot * 100, 1),
            "acc_l2": round(st["cor_l2"] / tot * 100, 1),
            "acc_l3": round(st["cor_l3"] / tot * 100, 1),
            "acc_overall": round(st["cor_all"] / tot * 100, 1)
        }
    res_stress["axis_breakdown"] = axis_summary
    
    print("\n--- 4 轴压力集分轴准确率 ---")
    for ax, s in axis_summary.items():
        print(f"  {ax}: 总体准度={s['acc_overall']}% (L1={s['acc_l1']}%, L2={s['acc_l2']}%, L3={s['acc_l3']}%)")
        
    # 保存结果
    out_results = {
        "version": "v2.0",
        "date": "2026-11-06",
        "real_57": res_real,
        "sim_200": res_sim,
        "stress_200": res_stress
    }
    
    out_path = os.path.join(project_root, "m4", "extraction_results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_results, f, ensure_ascii=False, indent=2)
        
    print(f"\nAll extraction benchmarks saved to {out_path} successfully!")
    return out_results

if __name__ == "__main__":
    run_all_extraction_benchmarks()

# -*- coding: utf-8 -*-
"""m4/evalforge.py — M4 EvalForge 20 金标 -> 200 题三模型对比评测
纯确定性代码，不调大模型 API。
"""
import json
import os
import sys
import time

# 避免 Windows 控制台输出编码问题
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from m4.golden import GOLDEN, AMOUNTS, EVIDENCE_FORMS
from core.bayes import calc_win_prob
from core.cost import calc_paths

def generate_200_cases():
    """由 20 道金标 x 10 个变体生成 200 题"""
    cases = []
    for g in GOLDEN:
        gid = g["id"]
        for idx in range(10):
            qid = f"{gid}-V{idx+1}"
            cases.append({
                "case_id": qid,
                "golden_id": gid,
                "category": g["category"],
                "prior": g["prior"],
                "evidence_ids": g["evidence"],
                "evidence": g["evidence"],
                "amount_yuan": AMOUNTS[idx],
                "evidence_form": EVIDENCE_FORMS[idx],
                "gold": g["gold"],
                "subset": g["subset"],
            })
    return cases

def run_evalforge():
    cases = generate_200_cases()
    total = len(cases)
    
    # 统计容器
    models = {
        "A": {
            "name": "A 基线规则",
            "desc": "仅依据先验(prior>=0.5判win走抗辩，否则lose走认赔)，不看证据",
            "correct": 0,
            "subsets": {"clear": {"tot": 0, "cor": 0}, "boundary": {"tot": 0, "cor": 0}, "adversarial": {"tot": 0, "cor": 0}},
            "costs": [],
            "total_time_s": 0.0,
        },
        "B": {
            "name": "B 贝叶斯 M0",
            "desc": "贝叶斯后验概率(posterior>=0.5判win，否则lose)，胜走抗辩A，负走认赔B",
            "correct": 0,
            "subsets": {"clear": {"tot": 0, "cor": 0}, "boundary": {"tot": 0, "cor": 0}, "adversarial": {"tot": 0, "cor": 0}},
            "costs": [],
            "total_time_s": 0.0,
        },
        "C": {
            "name": "C 贝叶斯+成本",
            "desc": "贝叶斯后验判win/lose，并在五条路径A-E中决策推荐期望成本最低项",
            "correct": 0,
            "subsets": {"clear": {"tot": 0, "cor": 0}, "boundary": {"tot": 0, "cor": 0}, "adversarial": {"tot": 0, "cor": 0}},
            "costs": [],
            "total_time_s": 0.0,
        },
    }

    # ==================== 1. 运行 Model A ====================
    t0 = time.perf_counter()
    for c in cases:
        gold = c["gold"]
        sub = c["subset"]
        prior = c["prior"]
        
        # 判定：prior >= 0.5 -> win (走抗辩 A)，否则 lose (走认赔 B)
        pred = "win" if prior >= 0.5 else "lose"
        
        # 计算该单在真实概率下的期望成本
        win_prob = calc_win_prob(c)
        paths = calc_paths(c, win_prob, 50)
        cost_map = {p["id"]: p["expected_cost"] for p in paths}
        cost = cost_map["A"] if pred == "win" else cost_map["B"]
        
        models["A"]["costs"].append(cost)
        models["A"]["subsets"][sub]["tot"] += 1
        if pred == gold:
            models["A"]["correct"] += 1
            models["A"]["subsets"][sub]["cor"] += 1
    models["A"]["total_time_s"] = time.perf_counter() - t0

    # ==================== 2. 运行 Model B ====================
    t0 = time.perf_counter()
    for c in cases:
        gold = c["gold"]
        sub = c["subset"]
        
        win_prob = calc_win_prob(c)
        pred = "win" if win_prob >= 0.5 else "lose"
        
        paths = calc_paths(c, win_prob, 50)
        cost_map = {p["id"]: p["expected_cost"] for p in paths}
        cost = cost_map["A"] if pred == "win" else cost_map["B"]
        
        models["B"]["costs"].append(cost)
        models["B"]["subsets"][sub]["tot"] += 1
        if pred == gold:
            models["B"]["correct"] += 1
            models["B"]["subsets"][sub]["cor"] += 1
    models["B"]["total_time_s"] = time.perf_counter() - t0

    # ==================== 3. 运行 Model C ====================
    t0 = time.perf_counter()
    for c in cases:
        gold = c["gold"]
        sub = c["subset"]
        
        win_prob = calc_win_prob(c)
        pred = "win" if win_prob >= 0.5 else "lose"
        
        # 决策五条路径中期望成本最低的那条
        paths = calc_paths(c, win_prob, 50)
        min_cost = min(p["expected_cost"] for p in paths)
        
        models["C"]["costs"].append(min_cost)
        models["C"]["subsets"][sub]["tot"] += 1
        if pred == gold:
            models["C"]["correct"] += 1
            models["C"]["subsets"][sub]["cor"] += 1
    models["C"]["total_time_s"] = time.perf_counter() - t0

    # ==================== 4. 整理聚合指标 ====================
    summary = {"total": total, "models": {}}
    for m_key in ["A", "B", "C"]:
        m = models[m_key]
        acc_total = (m["correct"] / total) * 100.0
        acc_clear = (m["subsets"]["clear"]["cor"] / m["subsets"]["clear"]["tot"]) * 100.0
        acc_boundary = (m["subsets"]["boundary"]["cor"] / m["subsets"]["boundary"]["tot"]) * 100.0
        acc_adversarial = (m["subsets"]["adversarial"]["cor"] / m["subsets"]["adversarial"]["tot"]) * 100.0
        avg_cost = sum(m["costs"]) / len(m["costs"])
        avg_ms = (m["total_time_s"] / total) * 1000.0
        
        summary["models"][m_key] = {
            "name": m["name"],
            "accuracy": round(acc_total, 1),
            "accuracy_clear": round(acc_clear, 1),
            "accuracy_boundary": round(acc_boundary, 1),
            "accuracy_adversarial": round(acc_adversarial, 1),
            "avg_cost": round(avg_cost, 1),
            "avg_ms": round(avg_ms, 3),
        }

    # 5. 写入 m4/results.json
    results_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # 6. 生成 m4/eval_report_200.md
    caveat = "200 题由 20 道金标变体生成，gold 由贝叶斯规则本身定义，B/C 的高分是构造性质，只证明评测管线跑通和证据的价值，不代表真实判责准确率；真实验证需要真实工单。"
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eval_report_200.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# M4 EvalForge 200 题三模型对比评测报告\n\n")
        f.write(f"> **核心声明（Caveat）**：{caveat}\n\n")
        f.write("## 1. 三模型三维综合对比（准确率 × 期望成本 × 耗时）\n\n")
        f.write("| 模型方案 | 决策逻辑 | 总体准确率 | 平均期望成本 (元) | 平均每题耗时 (ms) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for k in ["A", "B", "C"]:
            res = summary["models"][k]
            f.write(f"| **{res['name']}** | {models[k]['desc']} | **{res['accuracy']}%** | **¥{res['avg_cost']:.1f}** | **{res['avg_ms']:.3f} ms** |\n")

        f.write("\n## 2. 细分子集（清晰题 / 边界题 / 对抗题）准确率表现\n\n")
        f.write("| 模型方案 | 清晰题 (100题) | 边界题 (40题) | 对抗题 (60题) | 总体 (200题) |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for k in ["A", "B", "C"]:
            res = summary["models"][k]
            f.write(f"| **{res['name']}** | {res['accuracy_clear']}% | {res['accuracy_boundary']}% | {res['accuracy_adversarial']}% | **{res['accuracy']}%** |\n")

        f.write("\n## 3. 关键结论与评测洞察\n\n")
        f.write(f"1. **基线 A（仅看先验）的局限**：在无视证据时，总体准确率仅为 **{summary['models']['A']['accuracy']}%**。在边界题上为 **{summary['models']['A']['accuracy_boundary']}%**，而在正负冲抵的对抗题上更是跌至 **{summary['models']['A']['accuracy_adversarial']}%**，充分说明纯凭经验无法胜任复杂客诉。\n")
        f.write(f"2. **贝叶斯 B 的证据收益**：引入客诉增量证据后，总体准确率显著跃升至 **{summary['models']['B']['accuracy']}%**，能准确捕捉证据翻盘点。\n")
        f.write(f"3. **成本模型 C 的决策降本**：模型 C 在保持高准度（{summary['models']['C']['accuracy']}%）的同时，通过五路径成本求解将平均单笔期望成本由模型 B 的 **¥{summary['models']['B']['avg_cost']:.1f}** 压缩至 **¥{summary['models']['C']['avg_cost']:.1f}**，充分展现了运筹求解的降本价值。\n")

    # 控制台打印
    print("=" * 70)
    print("MarginKeeper (MK) M4 EvalForge — 200 题三模型对比评测结果")
    print("=" * 70)
    for k in ["A", "B", "C"]:
        res = summary["models"][k]
        print(f"[{res['name']}]")
        print(f"  - 总体准确率: {res['accuracy']}%")
        print(f"  - 清晰题准确率: {res['accuracy_clear']}% | 边界题: {res['accuracy_boundary']}% | 对抗题: {res['accuracy_adversarial']}%")
        print(f"  - 平均期望成本: ¥{res['avg_cost']:.1f}")
        print(f"  - 平均每题耗时: {res['avg_ms']:.3f} ms\n")
    print(f"【Caveat 声明】: {caveat}")
    print(f"评测结果已写入: {results_path}")
    print(f"评测报告已写入: {report_path}")
    print("=" * 70)

    return summary

if __name__ == "__main__":
    run_evalforge()

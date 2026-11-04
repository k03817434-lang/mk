# eval/run_eval.py — MK Demo D2 评测脚本
import os
import sys

# 保证项目根目录在 sys.path 中
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from eval.eval_cases import EVAL_CASES
from core.bayes import calc_win_prob
from mock_data import CATEGORY_NAMES

def run_evaluation():
    total = len(EVAL_CASES)
    correct = 0
    cat_stats = {
        "clothing": {"total": 0, "correct": 0},
        "food": {"total": 0, "correct": 0},
        "appliance": {"total": 0, "correct": 0},
    }
    wrong_cases = []

    for case in EVAL_CASES:
        cid = case["case_id"]
        cat = case["category"]
        gold = case["gold"]
        
        prob = calc_win_prob(case)
        pred = "win" if prob >= 0.5 else "lose"
        is_correct = (pred == gold)
        
        cat_stats[cat]["total"] += 1
        if is_correct:
            correct += 1
            cat_stats[cat]["correct"] += 1
        else:
            wrong_cases.append({
                "case_id": cid,
                "gold": gold,
                "pred": pred,
                "win_prob": prob,
                "category": cat,
                "evidence_ids": case.get("evidence_ids", []),
            })

    accuracy = (correct / total) * 100 if total > 0 else 0.0

    # 1. 控制台终端输出
    print("=" * 60)
    print("MarginKeeper (MK) Demo D2 — 50 题评测结果")
    print("=" * 60)
    print(f"总题数: {total} 道 | 做对: {correct} 道 | 总体准确率: {accuracy:.1f}%\n")
    print("分品类准确率:")
    for cat_key, c_info in cat_stats.items():
        c_tot = c_info["total"]
        c_cor = c_info["correct"]
        c_acc = (c_cor / c_tot) * 100 if c_tot > 0 else 0.0
        c_name = CATEGORY_NAMES.get(cat_key, cat_key)
        print(f"  - {c_name} ({cat_key}): {c_cor}/{c_tot} ({c_acc:.1f}%)")

    print("\n做错的题目清单:")
    if wrong_cases:
        for idx, w in enumerate(wrong_cases[:10], 1):
            print(f"  {idx}. 题号: {w['case_id']} | 真实(gold): {w['gold']} | 预测: {w['pred']} | 计算胜率: {w['win_prob']:.2f}")
    else:
        print("  （本次无错题）")

    print("\n基线与目标对比说明:")
    print("  - 基线: 商家凭经验 52.0%（模拟假设值）")
    print(f"  - 方案准确率: 本次实跑值为 {accuracy:.1f}%")
    print("  - 目标: 94.0% 为 Demo 验证目标，不是本次保证能达到的数。实测多少即报多少。")
    print("=" * 60)

    # 2. 生成 eval/eval_report.md
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eval_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# MarginKeeper 评测报告（D2）\n\n")
        f.write("> <font color='red'>**本报告全部基于模拟构造题，不是实测结果。**</font>\n\n")
        f.write("## 1. 总体与分品类准确率\n\n")
        f.write(f"- **总评测题数**：{total} 道\n")
        f.write(f"- **做对题数**：{correct} 道\n")
        f.write(f"- **总体准确率**：**{accuracy:.1f}%**\n\n")
        f.write("### 分品类准确率\n\n")
        f.write("| 品类 | 样本数 | 命中数 | 准确率 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for cat_key, c_info in cat_stats.items():
            c_tot = c_info["total"]
            c_cor = c_info["correct"]
            c_acc = (c_cor / c_tot) * 100 if c_tot > 0 else 0.0
            c_name = CATEGORY_NAMES.get(cat_key, cat_key)
            f.write(f"| {c_name} (`{cat_key}`) | {c_tot} | {c_cor} | {c_acc:.1f}% |\n")
        
        f.write("\n## 2. 错题明细清单\n\n")
        if wrong_cases:
            f.write("| 题号 | 品类 | 真实标准 (gold) | 预测结论 | 计算胜率 | 命中证据 |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            for w in wrong_cases[:10]:
                f.write(f"| `{w['case_id']}` | {w['category']} | `{w['gold']}` | `{w['pred']}` | `{w['win_prob']:.2f}` | `{','.join(w['evidence_ids'])}` |\n")
        else:
            f.write("本次模拟评测中 50 道构造题全部命中预期判定，无错题记录。\n\n")

        f.write("\n## 3. 指标对比说明\n\n")
        f.write(f"- **经验基线**：商家凭经验为 **52.0%**（模拟假设值）。\n")
        f.write(f"- **方案准确率**：本次实跑结果为 **{accuracy:.1f}%**（真实运行输出，不凑数、不刷分）。\n")
        f.write(f"- **目标值说明**：**94.0%** 为 Demo 验证目标，不是本次保证能达到的数。\n")

    print(f"\n评测报告已成功写入: {report_path}")

if __name__ == "__main__":
    run_evaluation()

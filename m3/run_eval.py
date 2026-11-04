# -*- coding: utf-8 -*-
"""m3/run_eval.py — M3 AdCompliance 50 条话术评测脚本
模板化生成 50 条直播话术（违规 25 / 合规 15 / 边缘 10），
运行确定性扫描，输出控制台评测统计及 m3/eval_report.md。
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

from m3.scanner import scan_line

def generate_50_eval_lines():
    """生成 50 条模板测试话术"""
    lines = []

    # 1. 违规 25 条 (ABS 7 / EFF 6 / PRICE 6 / MED 6)
    abs_lines = [
        "这款精华是全网最好用的，没有之一",
        "今年最流行的版型，人手一件",
        "同品类全网第一的销量，闭眼入",
        "顶级羊绒面料，触感细腻",
        "国家级配方认证，品质保证",
        "绝无仅有的破盘机制，仅限今晚",
        "遥遥领先其他品牌，放心冲",
    ]
    for text in abs_lines:
        lines.append({"text": text, "gold_type": "ABS", "is_violation": True, "category": "违规"})

    eff_lines = [
        "坚持使用根治黑头，毛孔隐形",
        "三天见效，快速淡纹",
        "专业祛斑成分，深层击退黑色素",
        "包治各种换季起皮干痒",
        "喝完立竿见影，整个人轻松了",
        "连续敷一周，保你白一个度",
    ]
    for text in eff_lines:
        lines.append({"text": text, "gold_type": "EFF", "is_violation": True, "category": "违规"})

    price_lines = [
        "今晚直接全网最低价，买贵必赔",
        "真正的全网最低，不要犹豫",
        "老板今天赔钱卖，就图交个朋友",
        "亏本大促，库存卖完直接关店",
        "工厂直出0利润，只为冲量",
        "史上最低到手价，错过等一年",
    ]
    for text in price_lines:
        lines.append({"text": text, "gold_type": "PRICE", "is_violation": True, "category": "违规"})

    med_lines = [
        "天然降血压，中老年人必备佳品",
        "能有效治疗关节酸痛",
        "具备临床试验级药用价值",
        "专为改善失眠研发，一觉到天亮",
        "强化宝宝免疫力，换季不生病",
        "中草药配方，显著疗效看得到",
    ]
    for text in med_lines:
        lines.append({"text": text, "gold_type": "MED", "is_violation": True, "category": "违规"})

    # 2. 合规 15 条
    compliant_lines = [
        "版型很正，显瘦显气质",
        "日常百搭，通勤休闲都能穿",
        "面料亲肤透气，手感柔软",
        "独立小包装，携带很方便",
        "配料表简单干净，无多余添加",
        "下单赠送运费险，退换无忧",
        "顺丰包邮，现货速发",
        "颜色温和自然，衬肤色",
        "做工精细，走线工整",
        "温和水润，不拔干",
        "早餐来一杯，开启活力一天",
        "轻便耐摔，居家旅行都合适",
        "耐磨耐脏，使用寿命长",
        "多重卡扣设计，密封不漏水",
        "经典条纹设计，不易过时",
    ]
    for text in compliant_lines:
        lines.append({"text": text, "gold_type": None, "is_violation": False, "category": "合规"})

    # 3. 边缘 10 条（主观感受类，不含违规词）
    boundary_lines = [
        "用过的姐妹都说效果很好",
        "这次价格比上次大促便宜多了",
        "老顾客回购率特别高",
        "很多粉丝反馈很满意",
        "这个价格性价比超高，非常划算",
        "主播自己也在用，体验很舒服",
        "回购无数次了，口碑特别棒",
        "味道很香浓，喝起来很享受",
        "包装很有质感，送礼很大气",
        "平时舍不得买的今天可以下手了",
    ]
    for text in boundary_lines:
        lines.append({"text": text, "gold_type": None, "is_violation": False, "category": "边缘"})

    return lines

def run_evaluation():
    lines = generate_50_eval_lines()
    total = len(lines)
    
    # 指标统计
    total_violating = 25  # 违规真值
    total_non_violating = 25  # 合规 15 + 边缘 10
    
    detected_count = 0  # 正确检出的违规行
    missed_count = 0    # 漏判的违规行
    false_alarm_count = 0  # 误报的合规/边缘行
    
    type_stats = {
        "ABS": {"total": 7, "detected": 0},
        "EFF": {"total": 6, "detected": 0},
        "PRICE": {"total": 6, "detected": 0},
        "MED": {"total": 6, "detected": 0},
    }

    wrong_records = []

    for idx, item in enumerate(lines, 1):
        res = scan_line(item["text"])
        is_pred_violation = res["is_violation"]
        gold_is_violation = item["is_violation"]
        gold_type = item["gold_type"]

        if gold_is_violation:
            if is_pred_violation:
                detected_count += 1
                if gold_type in type_stats:
                    type_stats[gold_type]["detected"] += 1
            else:
                missed_count += 1
                wrong_records.append({
                    "id": idx, "text": item["text"], "error": "漏判", "gold": gold_type, "pred": "合规"
                })
        else:
            if is_pred_violation:
                false_alarm_count += 1
                wrong_records.append({
                    "id": idx, "text": item["text"], "error": "误报", "gold": "合规", "pred": res["main_type"]
                })

    detection_rate = (detected_count / total_violating) * 100.0
    miss_rate = (missed_count / total_violating) * 100.0
    false_alarm_rate = (false_alarm_count / total_non_violating) * 100.0

    caveat = "50 条为模板构造集，检出率高不代表真实漏判率，只证明扫描管线跑通；真实验证需要真实直播话术。"

    # 1. 终端打印
    print("=" * 65)
    print("MarginKeeper (MK) M3 AdCompliance — 50 条话术合规评测结果")
    print("=" * 65)
    print(f"评测总数: {total} 条（违规 25 / 合规 15 / 边缘 10）")
    print(f"  - 违规检出率: {detection_rate:.1f}% ({detected_count}/{total_violating})")
    print(f"  - 违规漏判率: {miss_rate:.1f}% ({missed_count}/{total_violating})")
    print(f"  - 合规误报率: {false_alarm_rate:.1f}% ({false_alarm_count}/{total_non_violating})\n")
    print("按违规类型分项检出统计:")
    for t_key, t_stat in type_stats.items():
        t_acc = (t_stat["detected"] / t_stat["total"]) * 100.0
        print(f"  - {t_key}: {t_stat['detected']}/{t_stat['total']} ({t_acc:.1f}%)")
    
    if wrong_records:
        print("\n误判明细:")
        for r in wrong_records:
            print(f"  - [{r['id']}] [{r['error']}] 原文='{r['text']}' (期望={r['gold']}, 预测={r['pred']})")
    else:
        print("\n误判明细: 无漏判与误报记录（全部符合预期判定）")

    print(f"\n【Caveat 声明】: {caveat}")
    print("=" * 65)

    # 2. 写入 m3/eval_report.md
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eval_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# M3 AdCompliance 直播话术合规评测报告\n\n")
        f.write(f"> **核心声明（Caveat）**：{caveat}\n\n")
        f.write("## 1. 核心指标概览\n\n")
        f.write(f"- **总评测样本数**：{total} 条话术（违规用例 25 条 / 正常合规 15 条 / 主观边缘 10 条）\n")
        f.write(f"- **违规检出率（Recall）**：**{detection_rate:.1f}%** ({detected_count}/{total_violating})\n")
        f.write(f"- **违规漏判率（Miss Rate）**：**{miss_rate:.1f}%** ({missed_count}/{total_violating})\n")
        f.write(f"- **合规误报率（False Alarm）**：**{false_alarm_rate:.1f}%** ({false_alarm_count}/{total_non_violating})\n\n")
        f.write("## 2. 违规类型细分检出统计\n\n")
        f.write("| 违规类型 | 类型含义 | 样本数 | 成功检出数 | 检出率 |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        type_names = {"ABS": "绝对化用语", "EFF": "功效承诺", "PRICE": "价格误导", "MED": "医疗用语"}
        for t_key, t_stat in type_stats.items():
            t_acc = (t_stat["detected"] / t_stat["total"]) * 100.0
            f.write(f"| `{t_key}` | {type_names[t_key]} | {t_stat['total']} | {t_stat['detected']} | {t_acc:.1f}% |\n")
        
        f.write("\n## 3. 错题与边界案例明细\n\n")
        if wrong_records:
            f.write("| 序号 | 错误类型 | 话术原句 | 真实标签 | 预测标签 |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for r in wrong_records:
                f.write(f"| {r['id']} | `{r['error']}` | {r['text']} | `{r['gold']}` | `{r['pred']}` |\n")
        else:
            f.write("本次 50 条构造话术中，25 条违规全部准确命中，25 条合规与边缘主观表达（如“效果很好”“便宜很多”）全部精准放行，无误报与漏判。\n\n")

        f.write("## 4. 架构与测试声明\n\n")
        f.write(f"- **真实性说明**：{caveat}\n")
        f.write("- **算法特性**：本扫描全流程由确定性子串图匹配算法驱动，不调用外部大模型 API，保证主播上播前实时秒级熔断检测。\n")

    print(f"评测报告已写入: {report_path}")
    return detection_rate, miss_rate, false_alarm_rate

if __name__ == "__main__":
    run_evaluation()

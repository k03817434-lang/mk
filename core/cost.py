# core/cost.py
from mock_data import FIVE_PATHS, ASSUMPTIONS

def calc_paths(case, win_prob, slider_value):
    """
    计算五条路的期望成本并根据滑块给出推荐
    公式：
    - A (硬刚抗辩到底): 期望成本 = (1 - win_prob) * 金额 + 抗辩工时成本
    - B (直接认赔仅退款): 金额本身
    - C (折价补偿): 退 30%
    - D (送券 / 换货): 送券 ¥10
    - E (走平台仲裁): (1 - win_prob) * 金额 + 仲裁工时 ¥25/小时 * 0.5 小时
    """
    amount = float(case.get("amount_yuan", 0))
    hourly_wage = float(ASSUMPTIONS.get("hourly_wage_yuan", 25))
    manual_hours = float(ASSUMPTIONS.get("manual_minutes", 25)) / 60.0
    
    # 抗辩工时成本
    defense_labor_cost = hourly_wage * manual_hours
    # 仲裁工时成本
    arbitration_labor_cost = hourly_wage * 0.5

    cost_map = {
        "A": (1.0 - win_prob) * amount + defense_labor_cost,
        "B": amount,
        "C": 0.30 * amount,
        "D": 10.0,
        "E": (1.0 - win_prob) * amount + arbitration_labor_cost,
    }

    # 推荐逻辑：
    # slider < 30 偏保利润：能抗辩就抗辩（胜率>=0.5推荐A，胜率较低则选保利润最低成本项）
    # slider > 70 偏保评分：推荐 B 或 D（slider > 85 偏极速认赔推荐 B，70-85 偏安抚送券推荐 D）
    # 中间默认 30-70：推荐全量中期望成本最低的那条
    min_cost_id = min(cost_map, key=cost_map.get)
    
    if slider_value < 30:
        if win_prob >= 0.5:
            rec_id = "A"
        else:
            # 胜率不利时，排除高风险硬刚，在折价/认赔等非送券方案中取最低成本
            profit_candidates = {"A": cost_map["A"], "C": cost_map["C"], "B": cost_map["B"]}
            rec_id = min(profit_candidates, key=profit_candidates.get)
    elif slider_value > 70:
        if slider_value > 85:
            rec_id = "B"
        else:
            rec_id = "D"
    else:
        rec_id = min_cost_id

    result = []
    for p in FIVE_PATHS:
        pid = p["id"]
        c = round(cost_map[pid], 1)
        result.append({
            "id": pid,
            "name": p["name"],
            "desc": p["desc"],
            "expected_cost": c,
            "is_recommended": (pid == rec_id),
        })

    return result

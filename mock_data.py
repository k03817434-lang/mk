# mock_data.py — MK Demo D1 锁死数据文件
# 地位：全项目唯一的事实来源。所有模块只读这个文件，不许自己另起名字。
# 冻结规则：用户同意后冻结，改动必须通过一个具名决定，一句话记录。
# 来源：MarginKeeper-V2-完整版.md §1.5、§2.1、§2.3、§2.4
# 数据声明：全部是模拟数据 / 假设，不是实测结果。面试时必须主动说明。
# 数字声明：所有“基线→目标”数字均为 Demo 验证目标，不是已实测结果。

# ---------- 全局假设（模拟，显示在页面上，用户可改） ----------
ASSUMPTIONS = {
    "label": "模拟假设",
    "daily_orders": 1000,
    "daily_cases": 30,
    "avg_order_yuan": 60,
    "baseline_win_rate": 0.52,
    "target_win_rate": 0.94,
    "monthly_saving_yuan": 8400,
    "cost_per_call_yuan": 0.0006,
    "latency_target_s": 0.85,
    "hourly_wage_yuan": 25,
    "manual_minutes": 25,
    "agent_seconds": 15,
}

# ---------- 贝叶斯先验 ----------
BASE_PRIOR = 0.52
CATEGORY_PRIORS = {
    "clothing": 0.48,
    "food": 0.55,
    "appliance": 0.60,
}
CATEGORY_NAMES = {
    "clothing": "服装",
    "food": "食品",
    "appliance": "小家电",
}

# ---------- 证据规则：每条证据一个加减分（百分点），写死在代码里 ----------
EVIDENCE_RULES = [
    {"id": "signed_7d_late", "text": "买家签收后7天才说质量问题", "delta": +0.12},
    {"id": "buyer_confirmed_defect", "text": "聊天记录里买家售前已确认瑕疵", "delta": +0.18},
    {"id": "desc_matches", "text": "商品描述与实物一致（有图片/视频证据）", "delta": +0.10},
    {"id": "buyer_3_refunds_30d", "text": "买家30天内3次仅退款（仅参考，不作歧视依据）", "delta": +0.15},
    {"id": "desc_mismatch", "text": "商品描述与实物不符（标题写纯棉，属性写涤纶）", "delta": -0.25},
    {"id": "late_shipment", "text": "未按约定时间发货", "delta": -0.20},
]

VERDICT_LABELS = ["merchant_full", "shared", "buyer_full"]
VERDICT_NAMES = {
    "merchant_full": "商家全责",
    "shared": "责任分摊",
    "buyer_full": "买家责任",
}

# ---------- 五条路（字段名锁死） ----------
FIVE_PATHS = [
    {"id": "A", "name": "硬刚抗辩到底", "desc": "提交证据包，拒绝仅退款"},
    {"id": "B", "name": "直接认赔仅退款", "desc": "全额退款，快速了结"},
    {"id": "C", "name": "折价补偿", "desc": "退30% / 50%，协商解决"},
    {"id": "D", "name": "送券 / 换货", "desc": "送券或换货，留住客户"},
    {"id": "E", "name": "走平台仲裁", "desc": "提交证据包，走平台仲裁"},
]

# ---------- 滑块（字段名锁死） ----------
SLIDER = {
    "field": "slider_value",
    "min": 0,
    "max": 100,
    "default": 50,
    "left_label": "保利润",
    "right_label": "保评分",
    "left_tip": "保利润100%：能抗辩就抗辩，折价上限20%，不送券",
    "right_tip": "保评分100%：快速认赔 / 送券安抚，只对明显买家责任抗辩",
    "mid_tip": "默认50/50：按期望成本最低的那条路走",
}

# ---------- 3 个模拟工单（字段名锁死，不许改） ----------
MOCK_CASES = [
    {
        "case_id": "MK-001",
        "category": "clothing",
        "platform": "拼多多",
        "buyer_reason": "质量问题，仅退款",
        "amount_yuan": 60,
        "signed": True,
        "evidence_ids": ["signed_7d_late", "buyer_confirmed_defect"],
        "chat_note": "买家售前已确认衣摆有小线头，仍下单；签收7天后称质量问题要求仅退款。",
        "status": "pending",
    },
    {
        "case_id": "MK-002",
        "category": "food",
        "platform": "淘宝",
        "buyer_reason": "尺寸不符 / 口味不符",
        "amount_yuan": 48,
        "signed": True,
        "evidence_ids": ["desc_matches", "buyer_3_refunds_30d"],
        "chat_note": "商品描述与实物一致，有图片证据；买家30天内已有3次仅退款记录，仅作参考。",
        "status": "pending",
    },
    {
        "case_id": "MK-003",
        "category": "appliance",
        "platform": "京东",
        "buyer_reason": "假货 / 描述不符",
        "amount_yuan": 129,
        "signed": True,
        "evidence_ids": ["desc_mismatch", "late_shipment"],
        "chat_note": "标题写纯棉，属性表写涤纶；且未按约定时间发货。本单先验不利，慎重抗辩。",
        "status": "pending",
    },
]

PAGES = ["m0_receipt"]
APP_STATE = {
    "selected_case_id": "MK-001",
    "slider_value": 50,
    "selected_path": None,
}

GUARDRAILS = [
    "检索不到依据 → 输出'依据不足'，不给确定结论",
    "引用无法定位到原文段落 → 不引用，标'未定位'",
    "输入不完整（缺金额 / 缺签收状态） → 标'缺信息'，不猜",
    "高风险项（金额 >¥500、疑似假货、买家威胁） → 转人工确认，不自动建议硬刚",
    "评分损失只给区间，不给单点承诺；隐性降权无法精确量化",
]

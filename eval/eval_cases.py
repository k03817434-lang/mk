# 全部是模拟构造题，不是真实纠纷，gold 是按构造方法定的，不是实测判责。
# eval/eval_cases.py — MK Demo D2 50 道模拟评测题

from mock_data import CATEGORY_PRIORS, EVIDENCE_RULES

CATEGORIES = ["clothing", "food", "appliance"]
PLATFORMS = ["拼多多", "淘宝", "京东"]
REASONS_WIN = [
    "质量问题，要求仅退款",
    "商品有瑕疵，不想要了",
    "感觉和图片不一样，申请全额退款",
    "已签收多日后称商品损坏",
]
REASONS_LOSE = [
    "材质不符，参数与标题矛盾",
    "发货严重超时，商品未按时送达",
    "收到实物与描述严重不符",
    "虚假宣传，成分表造假",
]
AMOUNTS = [35, 48, 59, 68, 79, 88, 99, 110, 128, 145, 160, 180, 199]

POS_COMBOS = [
    ["signed_7d_late"],
    ["buyer_confirmed_defect"],
    ["desc_matches"],
    ["buyer_3_refunds_30d"],
    ["signed_7d_late", "buyer_confirmed_defect"],
    ["desc_matches", "buyer_3_refunds_30d"],
    ["signed_7d_late", "desc_matches"],
    ["buyer_confirmed_defect", "buyer_3_refunds_30d"],
]

NEG_COMBOS = [
    ["desc_mismatch"],
    ["late_shipment"],
    ["desc_mismatch", "late_shipment"],
]

EVAL_CASES = []

# 前 25 道：EVAL-001 到 EVAL-025，只用正证据组合，gold = "win"
for i in range(1, 26):
    case_id = f"EVAL-{i:03d}"
    cat = CATEGORIES[(i - 1) % len(CATEGORIES)]
    plat = PLATFORMS[(i - 1) % len(PLATFORMS)]
    amt = AMOUNTS[(i - 1) % len(AMOUNTS)]
    ev_ids = POS_COMBOS[(i - 1) % len(POS_COMBOS)]
    reason = REASONS_WIN[(i - 1) % len(REASONS_WIN)]
    chat = f"买家发起了仅退款申请，当前匹配正向抗辩证据：{','.join(ev_ids)}"
    
    EVAL_CASES.append({
        "case_id": case_id,
        "category": cat,
        "platform": plat,
        "buyer_reason": reason,
        "amount_yuan": amt,
        "signed": True,
        "evidence_ids": ev_ids,
        "chat_note": chat,
        "gold": "win",
    })

# 后 25 道：EVAL-026 到 EVAL-050，只用负证据组合，gold = "lose"
for i in range(26, 51):
    case_id = f"EVAL-{i:03d}"
    cat = CATEGORIES[(i - 26) % len(CATEGORIES)]
    plat = PLATFORMS[(i - 26) % len(PLATFORMS)]
    amt = AMOUNTS[(i - 26) % len(AMOUNTS)]
    ev_ids = NEG_COMBOS[(i - 26) % len(NEG_COMBOS)]
    reason = REASONS_LOSE[(i - 26) % len(REASONS_LOSE)]
    chat = f"买家针对商家过错投诉，当前命中负向证据：{','.join(ev_ids)}"
    
    EVAL_CASES.append({
        "case_id": case_id,
        "category": cat,
        "platform": plat,
        "buyer_reason": reason,
        "amount_yuan": amt,
        "signed": True,
        "evidence_ids": ev_ids,
        "chat_note": chat,
        "gold": "lose",
    })

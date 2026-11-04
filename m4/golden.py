# -*- coding: utf-8 -*-
"""M4 EvalForge 20 道金标题。全部模拟数据，不是真实工单。
gold: win=抗辩能赢, lose=抗辩赢不了。posterior = prior + 证据 deltas 之和。
证据 deltas 与 D1 的 mock_data.py 锁死一致：
signed_7d_late +0.12, buyer_confirmed_defect +0.18, desc_matches +0.10,
buyer_3_refunds_30d +0.15, desc_mismatch -0.25, late_shipment -0.20
先验：clothing 0.48, food 0.55, appliance 0.60
判定规则：posterior >= 0.5 -> win，否则 lose（含 0.50 平局算 win）
subset: clear=清晰题, boundary=边界题(后验 0.40-0.58), adversarial=对抗题(正负证据对冲)
"""

GOLDEN = [
    {"id": "G01", "category": "clothing", "prior": 0.48,
     "evidence": ["buyer_confirmed_defect", "signed_7d_late"],
     "gold": "win", "subset": "clear"},
    {"id": "G02", "category": "clothing", "prior": 0.48,
     "evidence": ["desc_matches", "buyer_3_refunds_30d"],
     "gold": "win", "subset": "clear"},
    {"id": "G03", "category": "food", "prior": 0.55,
     "evidence": ["buyer_confirmed_defect", "desc_matches"],
     "gold": "win", "subset": "clear"},
    {"id": "G04", "category": "appliance", "prior": 0.60,
     "evidence": ["signed_7d_late"],
     "gold": "win", "subset": "clear"},
    {"id": "G05", "category": "food", "prior": 0.55,
     "evidence": ["buyer_3_refunds_30d", "signed_7d_late"],
     "gold": "win", "subset": "clear"},
    {"id": "G06", "category": "clothing", "prior": 0.48,
     "evidence": ["desc_mismatch"],
     "gold": "lose", "subset": "clear"},
    {"id": "G07", "category": "food", "prior": 0.55,
     "evidence": ["desc_mismatch", "late_shipment"],
     "gold": "lose", "subset": "clear"},
    {"id": "G08", "category": "appliance", "prior": 0.60,
     "evidence": ["desc_mismatch"],
     "gold": "lose", "subset": "clear"},
    {"id": "G09", "category": "clothing", "prior": 0.48,
     "evidence": ["late_shipment"],
     "gold": "lose", "subset": "clear"},
    {"id": "G10", "category": "appliance", "prior": 0.60,
     "evidence": ["late_shipment", "desc_mismatch"],
     "gold": "lose", "subset": "clear"},
    {"id": "G11", "category": "clothing", "prior": 0.48,
     "evidence": ["desc_matches"],
     "gold": "win", "subset": "boundary"},
    {"id": "G12", "category": "food", "prior": 0.55,
     "evidence": ["desc_matches", "late_shipment"],
     "gold": "lose", "subset": "boundary"},
    {"id": "G13", "category": "clothing", "prior": 0.48,
     "evidence": ["signed_7d_late", "late_shipment"],
     "gold": "lose", "subset": "boundary"},
    {"id": "G14", "category": "appliance", "prior": 0.60,
     "evidence": ["desc_matches", "late_shipment"],
     "gold": "win", "subset": "boundary"},
    {"id": "G15", "category": "clothing", "prior": 0.48,
     "evidence": ["buyer_confirmed_defect", "desc_mismatch"],
     "gold": "lose", "subset": "adversarial"},
    {"id": "G16", "category": "food", "prior": 0.55,
     "evidence": ["buyer_confirmed_defect", "desc_mismatch"],
     "gold": "lose", "subset": "adversarial"},
    {"id": "G17", "category": "appliance", "prior": 0.60,
     "evidence": ["buyer_3_refunds_30d", "desc_mismatch"],
     "gold": "win", "subset": "adversarial"},
    {"id": "G18", "category": "clothing", "prior": 0.48,
     "evidence": ["buyer_3_refunds_30d", "signed_7d_late", "late_shipment"],
     "gold": "win", "subset": "adversarial"},
    {"id": "G19", "category": "food", "prior": 0.55,
     "evidence": ["signed_7d_late", "desc_mismatch", "buyer_confirmed_defect"],
     "gold": "win", "subset": "adversarial"},
    {"id": "G20", "category": "appliance", "prior": 0.60,
     "evidence": ["desc_matches", "desc_mismatch"],
     "gold": "lose", "subset": "adversarial"},
]

# 变体只改金额和举证形式，不改先验和证据，gold 不变。
AMOUNTS = [40, 60, 80, 100, 120, 150, 200, 260, 300, 500]
EVIDENCE_FORMS = ["照片", "视频", "聊天记录", "物流截图", "检测报告",
                  "照片", "视频", "聊天记录", "物流截图", "检测报告"]

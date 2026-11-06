# -*- coding: utf-8 -*-
"""eval/stress_cases_200.py — M4 4轴正交风险压力测试集 (200题)
4 个正交风险轴，各 50 题：
1. semantic_adversarial (语义对抗): 绕弯、反讽、模糊表述、多层否定
2. evidence_incomplete (证据残缺): 证据缺失、单图无主张、过期证据、无关联凭证
3. amount_boundary (金额临界): 围绕 ¥250 / ¥2,000 / ¥10,000 临界线密集布点
4. compliance_redline (合规红线): 虚构事实、调包欺诈、拒不退货、职业索赔
构造集标注来源：Bayes 先验与证据增量锁死计算。
"""

STRESS_CASES_200 = [
  {
    "case_id": "STRESS-SEM-001",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 132,
    "buyer_reason": "【第1组表述】真是‘良心’商家啊，这衣服薄得跟蝉翼一样大冬天穿正好当空调，佩服！要求退货退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-002",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 74,
    "buyer_reason": "【第2组表述】这牛肉干硬得能防弹，嚼两口牙都快崩了，贵店真是防身器材专卖店呢，必须仅退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-003",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 208,
    "buyer_reason": "【第3组表述】贵司的静音风扇声音比我家拖拉机还动听，催眠效果拔群，直接退全款吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-004",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 57,
    "buyer_reason": "【第4组表述】挺好的，买个陶瓷杯子收到碎成艺术拼图，商家艺术造诣真高，赶紧退款退货",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-005",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 203,
    "buyer_reason": "【第5组表述】不得不夸一下物流，买的生鲜冰袋化成温泉水，海鲜熟得都不用开火了，要求全额赔付",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-006",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 278,
    "buyer_reason": "【第6组表述】东西还可以，就是不知道为什么越看越觉得像上个世纪的库存古董，先看看怎么处理吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-007",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 110,
    "buyer_reason": "【第7组表述】这就是号称纯棉的衣服？摸着像塑料袋做的高科技防雨布，谁买谁是大冤种，申请退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-008",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 723,
    "buyer_reason": "【第8组表述】买个热水器洗澡像坐过山车，忽冷忽热真刺激，强身健体首选，已提交退货退款纠纷",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-009",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 85,
    "buyer_reason": "【第9组表述】发过来的坚果全是‘盲盒’，开出坏的算我倒霉是吧？你们质检小二睡着了？",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-010",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 150,
    "buyer_reason": "【第10组表述】客服态度好得感人，除了解决不了问题什么都好，我不申请仅退款都对不起你们的客气",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-011",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 162,
    "buyer_reason": "【第11组表述】真是‘良心’商家啊，这衣服薄得跟蝉翼一样大冬天穿正好当空调，佩服！要求退货退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-012",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 104,
    "buyer_reason": "【第12组表述】这牛肉干硬得能防弹，嚼两口牙都快崩了，贵店真是防身器材专卖店呢，必须仅退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-013",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 238,
    "buyer_reason": "【第13组表述】贵司的静音风扇声音比我家拖拉机还动听，催眠效果拔群，直接退全款吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-014",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 87,
    "buyer_reason": "【第14组表述】挺好的，买个陶瓷杯子收到碎成艺术拼图，商家艺术造诣真高，赶紧退款退货",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-015",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 233,
    "buyer_reason": "【第15组表述】不得不夸一下物流，买的生鲜冰袋化成温泉水，海鲜熟得都不用开火了，要求全额赔付",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-016",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 308,
    "buyer_reason": "【第16组表述】东西还可以，就是不知道为什么越看越觉得像上个世纪的库存古董，先看看怎么处理吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-017",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 140,
    "buyer_reason": "【第17组表述】这就是号称纯棉的衣服？摸着像塑料袋做的高科技防雨布，谁买谁是大冤种，申请退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-018",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 753,
    "buyer_reason": "【第18组表述】买个热水器洗澡像坐过山车，忽冷忽热真刺激，强身健体首选，已提交退货退款纠纷",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-019",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 115,
    "buyer_reason": "【第19组表述】发过来的坚果全是‘盲盒’，开出坏的算我倒霉是吧？你们质检小二睡着了？",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-020",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 180,
    "buyer_reason": "【第20组表述】客服态度好得感人，除了解决不了问题什么都好，我不申请仅退款都对不起你们的客气",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-021",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 192,
    "buyer_reason": "【第21组表述】真是‘良心’商家啊，这衣服薄得跟蝉翼一样大冬天穿正好当空调，佩服！要求退货退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-022",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 134,
    "buyer_reason": "【第22组表述】这牛肉干硬得能防弹，嚼两口牙都快崩了，贵店真是防身器材专卖店呢，必须仅退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-023",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 268,
    "buyer_reason": "【第23组表述】贵司的静音风扇声音比我家拖拉机还动听，催眠效果拔群，直接退全款吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-024",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 117,
    "buyer_reason": "【第24组表述】挺好的，买个陶瓷杯子收到碎成艺术拼图，商家艺术造诣真高，赶紧退款退货",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-025",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 263,
    "buyer_reason": "【第25组表述】不得不夸一下物流，买的生鲜冰袋化成温泉水，海鲜熟得都不用开火了，要求全额赔付",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-026",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 338,
    "buyer_reason": "【第26组表述】东西还可以，就是不知道为什么越看越觉得像上个世纪的库存古董，先看看怎么处理吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-027",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 170,
    "buyer_reason": "【第27组表述】这就是号称纯棉的衣服？摸着像塑料袋做的高科技防雨布，谁买谁是大冤种，申请退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-028",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 783,
    "buyer_reason": "【第28组表述】买个热水器洗澡像坐过山车，忽冷忽热真刺激，强身健体首选，已提交退货退款纠纷",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-029",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 145,
    "buyer_reason": "【第29组表述】发过来的坚果全是‘盲盒’，开出坏的算我倒霉是吧？你们质检小二睡着了？",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-030",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 210,
    "buyer_reason": "【第30组表述】客服态度好得感人，除了解决不了问题什么都好，我不申请仅退款都对不起你们的客气",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-031",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 222,
    "buyer_reason": "【第31组表述】真是‘良心’商家啊，这衣服薄得跟蝉翼一样大冬天穿正好当空调，佩服！要求退货退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-032",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 164,
    "buyer_reason": "【第32组表述】这牛肉干硬得能防弹，嚼两口牙都快崩了，贵店真是防身器材专卖店呢，必须仅退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-033",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 298,
    "buyer_reason": "【第33组表述】贵司的静音风扇声音比我家拖拉机还动听，催眠效果拔群，直接退全款吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-034",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 147,
    "buyer_reason": "【第34组表述】挺好的，买个陶瓷杯子收到碎成艺术拼图，商家艺术造诣真高，赶紧退款退货",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-035",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 293,
    "buyer_reason": "【第35组表述】不得不夸一下物流，买的生鲜冰袋化成温泉水，海鲜熟得都不用开火了，要求全额赔付",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-036",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 368,
    "buyer_reason": "【第36组表述】东西还可以，就是不知道为什么越看越觉得像上个世纪的库存古董，先看看怎么处理吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-037",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 200,
    "buyer_reason": "【第37组表述】这就是号称纯棉的衣服？摸着像塑料袋做的高科技防雨布，谁买谁是大冤种，申请退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-038",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 813,
    "buyer_reason": "【第38组表述】买个热水器洗澡像坐过山车，忽冷忽热真刺激，强身健体首选，已提交退货退款纠纷",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-039",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 175,
    "buyer_reason": "【第39组表述】发过来的坚果全是‘盲盒’，开出坏的算我倒霉是吧？你们质检小二睡着了？",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-040",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 240,
    "buyer_reason": "【第40组表述】客服态度好得感人，除了解决不了问题什么都好，我不申请仅退款都对不起你们的客气",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-041",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 252,
    "buyer_reason": "【第41组表述】真是‘良心’商家啊，这衣服薄得跟蝉翼一样大冬天穿正好当空调，佩服！要求退货退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-042",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 194,
    "buyer_reason": "【第42组表述】这牛肉干硬得能防弹，嚼两口牙都快崩了，贵店真是防身器材专卖店呢，必须仅退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-043",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 328,
    "buyer_reason": "【第43组表述】贵司的静音风扇声音比我家拖拉机还动听，催眠效果拔群，直接退全款吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-044",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 177,
    "buyer_reason": "【第44组表述】挺好的，买个陶瓷杯子收到碎成艺术拼图，商家艺术造诣真高，赶紧退款退货",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-045",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 323,
    "buyer_reason": "【第45组表述】不得不夸一下物流，买的生鲜冰袋化成温泉水，海鲜熟得都不用开火了，要求全额赔付",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-046",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 398,
    "buyer_reason": "【第46组表述】东西还可以，就是不知道为什么越看越觉得像上个世纪的库存古董，先看看怎么处理吧",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-047",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 230,
    "buyer_reason": "【第47组表述】这就是号称纯棉的衣服？摸着像塑料袋做的高科技防雨布，谁买谁是大冤种，申请退款",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-048",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 843,
    "buyer_reason": "【第48组表述】买个热水器洗澡像坐过山车，忽冷忽热真刺激，强身健体首选，已提交退货退款纠纷",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-049",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 205,
    "buyer_reason": "【第49组表述】发过来的坚果全是‘盲盒’，开出坏的算我倒霉是吧？你们质检小二睡着了？",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-SEM-050",
    "axis": "semantic_adversarial",
    "axis_zh": "语义对抗",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 270,
    "buyer_reason": "【第50组表述】客服态度好得感人，除了解决不了问题什么都好，我不申请仅退款都对不起你们的客气",
    "evidence": "买家聊天记录截图及文字反讽表达，无第三方权威检测报告",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "反讽隐喻表述增加语义解析难度，测试LLM能否准确剥离情绪词抓取真实诉求与证据核心"
  },
  {
    "case_id": "STRESS-EVD-001",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 79,
    "buyer_reason": "【证据残缺案例1】申请仅退款",
    "evidence": "仅提供一张快递外包装破损模糊远景照片，未拍到内部实物",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-002",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 138,
    "buyer_reason": "【证据残缺案例2】决定退货退款",
    "evidence": "商品签收已过45天，买家提供一张无时间水印的泛黄衣服起球照片",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-003",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 111,
    "buyer_reason": "【证据残缺案例3】要求赔偿",
    "evidence": "买家称食用后腹泻，但拒绝提供就医病历及购买记录关联证明",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-004",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 336,
    "buyer_reason": "【证据残缺案例4】申请退货退款",
    "evidence": "买家上传一段5秒视频，镜头晃动剧烈且全黑，无法看清破损部位",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-005",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 108,
    "buyer_reason": "【证据残缺案例5】买家理由未公开",
    "evidence": "只有平台介入流水记录，证据栏标注‘暂无举证凭证’",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-006",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 474,
    "buyer_reason": "【证据残缺案例6】要求退全款",
    "evidence": "买家拍照只拍了商家的说明书封面，未举证机器具体哪个按键失灵",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-007",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 308,
    "buyer_reason": "【证据残缺案例7】以破损为由申请仅退款",
    "evidence": "买家拍了一张邻居家同款破损电磁炉照片（机身序列号与发货单不符）",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-008",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 182,
    "buyer_reason": "【证据残缺案例8】提出换货要求",
    "evidence": "提供了一张无包装、无任何标识的黑色电线插头照片，无法确认出处",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-009",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 101,
    "buyer_reason": "【证据残缺案例9】申请仅退款",
    "evidence": "买家上传发票照片，但未提供任何实物质量瑕疵凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-010",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 150,
    "buyer_reason": "【证据残缺案例10】协商未果介入",
    "evidence": "商家聊天表示‘已收到退回商品包裹’，证实买家已履约退货",
    "gold_l1": "N",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-011",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 119,
    "buyer_reason": "【证据残缺案例11】申请仅退款",
    "evidence": "仅提供一张快递外包装破损模糊远景照片，未拍到内部实物",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-012",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 178,
    "buyer_reason": "【证据残缺案例12】决定退货退款",
    "evidence": "商品签收已过45天，买家提供一张无时间水印的泛黄衣服起球照片",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-013",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 151,
    "buyer_reason": "【证据残缺案例13】要求赔偿",
    "evidence": "买家称食用后腹泻，但拒绝提供就医病历及购买记录关联证明",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-014",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 376,
    "buyer_reason": "【证据残缺案例14】申请退货退款",
    "evidence": "买家上传一段5秒视频，镜头晃动剧烈且全黑，无法看清破损部位",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-015",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 148,
    "buyer_reason": "【证据残缺案例15】买家理由未公开",
    "evidence": "只有平台介入流水记录，证据栏标注‘暂无举证凭证’",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-016",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 514,
    "buyer_reason": "【证据残缺案例16】要求退全款",
    "evidence": "买家拍照只拍了商家的说明书封面，未举证机器具体哪个按键失灵",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-017",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 348,
    "buyer_reason": "【证据残缺案例17】以破损为由申请仅退款",
    "evidence": "买家拍了一张邻居家同款破损电磁炉照片（机身序列号与发货单不符）",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-018",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 222,
    "buyer_reason": "【证据残缺案例18】提出换货要求",
    "evidence": "提供了一张无包装、无任何标识的黑色电线插头照片，无法确认出处",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-019",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 141,
    "buyer_reason": "【证据残缺案例19】申请仅退款",
    "evidence": "买家上传发票照片，但未提供任何实物质量瑕疵凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-020",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 190,
    "buyer_reason": "【证据残缺案例20】协商未果介入",
    "evidence": "商家聊天表示‘已收到退回商品包裹’，证实买家已履约退货",
    "gold_l1": "N",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-021",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 159,
    "buyer_reason": "【证据残缺案例21】申请仅退款",
    "evidence": "仅提供一张快递外包装破损模糊远景照片，未拍到内部实物",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-022",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 218,
    "buyer_reason": "【证据残缺案例22】决定退货退款",
    "evidence": "商品签收已过45天，买家提供一张无时间水印的泛黄衣服起球照片",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-023",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 191,
    "buyer_reason": "【证据残缺案例23】要求赔偿",
    "evidence": "买家称食用后腹泻，但拒绝提供就医病历及购买记录关联证明",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-024",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 416,
    "buyer_reason": "【证据残缺案例24】申请退货退款",
    "evidence": "买家上传一段5秒视频，镜头晃动剧烈且全黑，无法看清破损部位",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-025",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 188,
    "buyer_reason": "【证据残缺案例25】买家理由未公开",
    "evidence": "只有平台介入流水记录，证据栏标注‘暂无举证凭证’",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-026",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 554,
    "buyer_reason": "【证据残缺案例26】要求退全款",
    "evidence": "买家拍照只拍了商家的说明书封面，未举证机器具体哪个按键失灵",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-027",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 388,
    "buyer_reason": "【证据残缺案例27】以破损为由申请仅退款",
    "evidence": "买家拍了一张邻居家同款破损电磁炉照片（机身序列号与发货单不符）",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-028",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 262,
    "buyer_reason": "【证据残缺案例28】提出换货要求",
    "evidence": "提供了一张无包装、无任何标识的黑色电线插头照片，无法确认出处",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-029",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 181,
    "buyer_reason": "【证据残缺案例29】申请仅退款",
    "evidence": "买家上传发票照片，但未提供任何实物质量瑕疵凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-030",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 230,
    "buyer_reason": "【证据残缺案例30】协商未果介入",
    "evidence": "商家聊天表示‘已收到退回商品包裹’，证实买家已履约退货",
    "gold_l1": "N",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-031",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 199,
    "buyer_reason": "【证据残缺案例31】申请仅退款",
    "evidence": "仅提供一张快递外包装破损模糊远景照片，未拍到内部实物",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-032",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 258,
    "buyer_reason": "【证据残缺案例32】决定退货退款",
    "evidence": "商品签收已过45天，买家提供一张无时间水印的泛黄衣服起球照片",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-033",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 231,
    "buyer_reason": "【证据残缺案例33】要求赔偿",
    "evidence": "买家称食用后腹泻，但拒绝提供就医病历及购买记录关联证明",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-034",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 456,
    "buyer_reason": "【证据残缺案例34】申请退货退款",
    "evidence": "买家上传一段5秒视频，镜头晃动剧烈且全黑，无法看清破损部位",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-035",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 228,
    "buyer_reason": "【证据残缺案例35】买家理由未公开",
    "evidence": "只有平台介入流水记录，证据栏标注‘暂无举证凭证’",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-036",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 594,
    "buyer_reason": "【证据残缺案例36】要求退全款",
    "evidence": "买家拍照只拍了商家的说明书封面，未举证机器具体哪个按键失灵",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-037",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 428,
    "buyer_reason": "【证据残缺案例37】以破损为由申请仅退款",
    "evidence": "买家拍了一张邻居家同款破损电磁炉照片（机身序列号与发货单不符）",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-038",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 302,
    "buyer_reason": "【证据残缺案例38】提出换货要求",
    "evidence": "提供了一张无包装、无任何标识的黑色电线插头照片，无法确认出处",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-039",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 221,
    "buyer_reason": "【证据残缺案例39】申请仅退款",
    "evidence": "买家上传发票照片，但未提供任何实物质量瑕疵凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-040",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 270,
    "buyer_reason": "【证据残缺案例40】协商未果介入",
    "evidence": "商家聊天表示‘已收到退回商品包裹’，证实买家已履约退货",
    "gold_l1": "N",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-041",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 239,
    "buyer_reason": "【证据残缺案例41】申请仅退款",
    "evidence": "仅提供一张快递外包装破损模糊远景照片，未拍到内部实物",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-042",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 298,
    "buyer_reason": "【证据残缺案例42】决定退货退款",
    "evidence": "商品签收已过45天，买家提供一张无时间水印的泛黄衣服起球照片",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-043",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 271,
    "buyer_reason": "【证据残缺案例43】要求赔偿",
    "evidence": "买家称食用后腹泻，但拒绝提供就医病历及购买记录关联证明",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-044",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 496,
    "buyer_reason": "【证据残缺案例44】申请退货退款",
    "evidence": "买家上传一段5秒视频，镜头晃动剧烈且全黑，无法看清破损部位",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-045",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 268,
    "buyer_reason": "【证据残缺案例45】买家理由未公开",
    "evidence": "只有平台介入流水记录，证据栏标注‘暂无举证凭证’",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-046",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 634,
    "buyer_reason": "【证据残缺案例46】要求退全款",
    "evidence": "买家拍照只拍了商家的说明书封面，未举证机器具体哪个按键失灵",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-047",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 468,
    "buyer_reason": "【证据残缺案例47】以破损为由申请仅退款",
    "evidence": "买家拍了一张邻居家同款破损电磁炉照片（机身序列号与发货单不符）",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-048",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 342,
    "buyer_reason": "【证据残缺案例48】提出换货要求",
    "evidence": "提供了一张无包装、无任何标识的黑色电线插头照片，无法确认出处",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-049",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 261,
    "buyer_reason": "【证据残缺案例49】申请仅退款",
    "evidence": "买家上传发票照片，但未提供任何实物质量瑕疵凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-EVD-050",
    "axis": "evidence_incomplete",
    "axis_zh": "证据残缺",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 310,
    "buyer_reason": "【证据残缺案例50】协商未果介入",
    "evidence": "商家聊天表示‘已收到退回商品包裹’，证实买家已履约退货",
    "gold_l1": "N",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "测试在证据信息缺失、失效或反向验证场景下，抽取引擎是否能严格守住L2判定标准"
  },
  {
    "case_id": "STRESS-AMT-001",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 248,
    "buyer_reason": "【金额临界案例1】¥249 临界小额争议（平台极速退款规则边缘）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-002",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 250,
    "buyer_reason": "【金额临界案例2】¥250 临界分水岭（平台小额免举证拦截线）：申请退货退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-003",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 252,
    "buyer_reason": "【金额临界案例3】¥251 临界突破额（平台转人工仲裁门槛）：要求退全款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-004",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 1982,
    "buyer_reason": "【金额临界案例4】¥1,980 高额家电维修争议（大额抗辩预备）：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-005",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 1998,
    "buyer_reason": "【金额临界案例5】¥2,000 重大争议临界点（法务跟进门槛）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-006",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 2049,
    "buyer_reason": "【金额临界案例6】¥2,050 涉案金额超标争议：买家理由未公开",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-007",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 9800,
    "buyer_reason": "【金额临界案例7】¥9,800 大宗数码采购仅退款风险点：决定退货",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-008",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 10001,
    "buyer_reason": "【金额临界案例8】¥10,000 司法诉讼胜负临界线（R-M0-05同级）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-009",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 10502,
    "buyer_reason": "【金额临界案例9】¥10,500 超特大争议订单，商家必争之地：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect",
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-010",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 197,
    "buyer_reason": "【金额临界案例10】¥199 普通服饰争议基准线：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-011",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 248,
    "buyer_reason": "【金额临界案例11】¥249 临界小额争议（平台极速退款规则边缘）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-012",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 250,
    "buyer_reason": "【金额临界案例12】¥250 临界分水岭（平台小额免举证拦截线）：申请退货退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-013",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 252,
    "buyer_reason": "【金额临界案例13】¥251 临界突破额（平台转人工仲裁门槛）：要求退全款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-014",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 1982,
    "buyer_reason": "【金额临界案例14】¥1,980 高额家电维修争议（大额抗辩预备）：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-015",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 1998,
    "buyer_reason": "【金额临界案例15】¥2,000 重大争议临界点（法务跟进门槛）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-016",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 2049,
    "buyer_reason": "【金额临界案例16】¥2,050 涉案金额超标争议：买家理由未公开",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-017",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 9800,
    "buyer_reason": "【金额临界案例17】¥9,800 大宗数码采购仅退款风险点：决定退货",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-018",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 10001,
    "buyer_reason": "【金额临界案例18】¥10,000 司法诉讼胜负临界线（R-M0-05同级）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-019",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 10502,
    "buyer_reason": "【金额临界案例19】¥10,500 超特大争议订单，商家必争之地：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect",
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-020",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 197,
    "buyer_reason": "【金额临界案例20】¥199 普通服饰争议基准线：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-021",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 248,
    "buyer_reason": "【金额临界案例21】¥249 临界小额争议（平台极速退款规则边缘）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-022",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 250,
    "buyer_reason": "【金额临界案例22】¥250 临界分水岭（平台小额免举证拦截线）：申请退货退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-023",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 252,
    "buyer_reason": "【金额临界案例23】¥251 临界突破额（平台转人工仲裁门槛）：要求退全款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-024",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 1982,
    "buyer_reason": "【金额临界案例24】¥1,980 高额家电维修争议（大额抗辩预备）：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-025",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 1998,
    "buyer_reason": "【金额临界案例25】¥2,000 重大争议临界点（法务跟进门槛）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-026",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 2049,
    "buyer_reason": "【金额临界案例26】¥2,050 涉案金额超标争议：买家理由未公开",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-027",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 9800,
    "buyer_reason": "【金额临界案例27】¥9,800 大宗数码采购仅退款风险点：决定退货",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-028",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 10001,
    "buyer_reason": "【金额临界案例28】¥10,000 司法诉讼胜负临界线（R-M0-05同级）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-029",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 10502,
    "buyer_reason": "【金额临界案例29】¥10,500 超特大争议订单，商家必争之地：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect",
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-030",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 197,
    "buyer_reason": "【金额临界案例30】¥199 普通服饰争议基准线：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-031",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 248,
    "buyer_reason": "【金额临界案例31】¥249 临界小额争议（平台极速退款规则边缘）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-032",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 250,
    "buyer_reason": "【金额临界案例32】¥250 临界分水岭（平台小额免举证拦截线）：申请退货退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-033",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 252,
    "buyer_reason": "【金额临界案例33】¥251 临界突破额（平台转人工仲裁门槛）：要求退全款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-034",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 1982,
    "buyer_reason": "【金额临界案例34】¥1,980 高额家电维修争议（大额抗辩预备）：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-035",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 1998,
    "buyer_reason": "【金额临界案例35】¥2,000 重大争议临界点（法务跟进门槛）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-036",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 2049,
    "buyer_reason": "【金额临界案例36】¥2,050 涉案金额超标争议：买家理由未公开",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-037",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 9800,
    "buyer_reason": "【金额临界案例37】¥9,800 大宗数码采购仅退款风险点：决定退货",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-038",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 10001,
    "buyer_reason": "【金额临界案例38】¥10,000 司法诉讼胜负临界线（R-M0-05同级）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-039",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 10502,
    "buyer_reason": "【金额临界案例39】¥10,500 超特大争议订单，商家必争之地：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect",
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-040",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 197,
    "buyer_reason": "【金额临界案例40】¥199 普通服饰争议基准线：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-041",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 248,
    "buyer_reason": "【金额临界案例41】¥249 临界小额争议（平台极速退款规则边缘）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-042",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 250,
    "buyer_reason": "【金额临界案例42】¥250 临界分水岭（平台小额免举证拦截线）：申请退货退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-043",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 252,
    "buyer_reason": "【金额临界案例43】¥251 临界突破额（平台转人工仲裁门槛）：要求退全款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-044",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 1982,
    "buyer_reason": "【金额临界案例44】¥1,980 高额家电维修争议（大额抗辩预备）：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-045",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 1998,
    "buyer_reason": "【金额临界案例45】¥2,000 重大争议临界点（法务跟进门槛）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_mismatch"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-046",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 2049,
    "buyer_reason": "【金额临界案例46】¥2,050 涉案金额超标争议：买家理由未公开",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "late_shipment"
    ],
    "gold_bayes": "lose",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-047",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 9800,
    "buyer_reason": "【金额临界案例47】¥9,800 大宗数码采购仅退款风险点：决定退货",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-048",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 10001,
    "buyer_reason": "【金额临界案例48】¥10,000 司法诉讼胜负临界线（R-M0-05同级）：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-049",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 10502,
    "buyer_reason": "【金额临界案例49】¥10,500 超特大争议订单，商家必争之地：提交退货退款纠纷",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "buyer_confirmed_defect",
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-AMT-050",
    "axis": "amount_boundary",
    "axis_zh": "金额临界",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 197,
    "buyer_reason": "【金额临界案例50】¥199 普通服饰争议基准线：申请仅退款",
    "evidence": "商品实物与交易订单详情，商家附带成本证明材料",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "围绕关键成本与决策跃迁金额节点，检验决策模型在临界点附近是否发生非线性突变或抖动"
  },
  {
    "case_id": "STRESS-RED-001",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 190,
    "buyer_reason": "【红线风险案例1】申请仅退款拦截快递",
    "evidence": "警方查明该团伙注册12个虚拟账号批量仅退款，对组织者予以行政拘留",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-002",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 6820,
    "buyer_reason": "【红线风险案例2】申请退货退款",
    "evidence": "商家当场验货拆箱录像显示，退回物品为两瓶矿泉水，原装单反相机被调包",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-003",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 4230,
    "buyer_reason": "【红线风险案例3】申请仅退款",
    "evidence": "法院判决书认定买家收到手机后虚构未收到货事实且拒不退货，构成不当得利",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-004",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 390,
    "buyer_reason": "【红线风险案例4】买家理由未公开",
    "evidence": "法院判决买家违背诚信原则、无正当理由拒不退还货物，限10日内返还",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-005",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 930,
    "buyer_reason": "【红线风险案例5】要求退全款",
    "evidence": "公权力机关认定买家存在虚构事实敲诈勒索商誉行为，已立案侦办",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-006",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 210,
    "buyer_reason": "【红线风险案例6】申请仅退款",
    "evidence": "买家短时间内同地址更换8个不同手机号连续申请20笔仅退款，命中职业索赔黑名单",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-007",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 1270,
    "buyer_reason": "【红线风险案例7】申请退货退款",
    "evidence": "退回包裹中填塞废纸报纸，商品被调包，顺丰快递员出具开箱异常证明",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-008",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 279,
    "buyer_reason": "【红线风险案例8】决定退货",
    "evidence": "买家正常申请退货退款，并按时提供真实有效的回寄运单号",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-009",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 189,
    "buyer_reason": "【红线风险案例9】申请仅退款",
    "evidence": "买家虽态度非常强硬并扬言差评，但未发现调包或虚构事实的法定认定凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-010",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 160,
    "buyer_reason": "【红线风险案例10】买家理由未公开",
    "evidence": "平台单方系统原因直接全额退款，未见买家违背诚信或拒不退货记录",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-011",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 290,
    "buyer_reason": "【红线风险案例11】申请仅退款拦截快递",
    "evidence": "警方查明该团伙注册12个虚拟账号批量仅退款，对组织者予以行政拘留",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-012",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 6920,
    "buyer_reason": "【红线风险案例12】申请退货退款",
    "evidence": "商家当场验货拆箱录像显示，退回物品为两瓶矿泉水，原装单反相机被调包",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-013",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 4330,
    "buyer_reason": "【红线风险案例13】申请仅退款",
    "evidence": "法院判决书认定买家收到手机后虚构未收到货事实且拒不退货，构成不当得利",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-014",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 490,
    "buyer_reason": "【红线风险案例14】买家理由未公开",
    "evidence": "法院判决买家违背诚信原则、无正当理由拒不退还货物，限10日内返还",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-015",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 1030,
    "buyer_reason": "【红线风险案例15】要求退全款",
    "evidence": "公权力机关认定买家存在虚构事实敲诈勒索商誉行为，已立案侦办",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-016",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 310,
    "buyer_reason": "【红线风险案例16】申请仅退款",
    "evidence": "买家短时间内同地址更换8个不同手机号连续申请20笔仅退款，命中职业索赔黑名单",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-017",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 1370,
    "buyer_reason": "【红线风险案例17】申请退货退款",
    "evidence": "退回包裹中填塞废纸报纸，商品被调包，顺丰快递员出具开箱异常证明",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-018",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 379,
    "buyer_reason": "【红线风险案例18】决定退货",
    "evidence": "买家正常申请退货退款，并按时提供真实有效的回寄运单号",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-019",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 289,
    "buyer_reason": "【红线风险案例19】申请仅退款",
    "evidence": "买家虽态度非常强硬并扬言差评，但未发现调包或虚构事实的法定认定凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-020",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 260,
    "buyer_reason": "【红线风险案例20】买家理由未公开",
    "evidence": "平台单方系统原因直接全额退款，未见买家违背诚信或拒不退货记录",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-021",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 390,
    "buyer_reason": "【红线风险案例21】申请仅退款拦截快递",
    "evidence": "警方查明该团伙注册12个虚拟账号批量仅退款，对组织者予以行政拘留",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-022",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 7020,
    "buyer_reason": "【红线风险案例22】申请退货退款",
    "evidence": "商家当场验货拆箱录像显示，退回物品为两瓶矿泉水，原装单反相机被调包",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-023",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 4430,
    "buyer_reason": "【红线风险案例23】申请仅退款",
    "evidence": "法院判决书认定买家收到手机后虚构未收到货事实且拒不退货，构成不当得利",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-024",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 590,
    "buyer_reason": "【红线风险案例24】买家理由未公开",
    "evidence": "法院判决买家违背诚信原则、无正当理由拒不退还货物，限10日内返还",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-025",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 1130,
    "buyer_reason": "【红线风险案例25】要求退全款",
    "evidence": "公权力机关认定买家存在虚构事实敲诈勒索商誉行为，已立案侦办",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-026",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 410,
    "buyer_reason": "【红线风险案例26】申请仅退款",
    "evidence": "买家短时间内同地址更换8个不同手机号连续申请20笔仅退款，命中职业索赔黑名单",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-027",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 1470,
    "buyer_reason": "【红线风险案例27】申请退货退款",
    "evidence": "退回包裹中填塞废纸报纸，商品被调包，顺丰快递员出具开箱异常证明",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-028",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 479,
    "buyer_reason": "【红线风险案例28】决定退货",
    "evidence": "买家正常申请退货退款，并按时提供真实有效的回寄运单号",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-029",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 389,
    "buyer_reason": "【红线风险案例29】申请仅退款",
    "evidence": "买家虽态度非常强硬并扬言差评，但未发现调包或虚构事实的法定认定凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-030",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 360,
    "buyer_reason": "【红线风险案例30】买家理由未公开",
    "evidence": "平台单方系统原因直接全额退款，未见买家违背诚信或拒不退货记录",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-031",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 490,
    "buyer_reason": "【红线风险案例31】申请仅退款拦截快递",
    "evidence": "警方查明该团伙注册12个虚拟账号批量仅退款，对组织者予以行政拘留",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-032",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 7120,
    "buyer_reason": "【红线风险案例32】申请退货退款",
    "evidence": "商家当场验货拆箱录像显示，退回物品为两瓶矿泉水，原装单反相机被调包",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-033",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 4530,
    "buyer_reason": "【红线风险案例33】申请仅退款",
    "evidence": "法院判决书认定买家收到手机后虚构未收到货事实且拒不退货，构成不当得利",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-034",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 690,
    "buyer_reason": "【红线风险案例34】买家理由未公开",
    "evidence": "法院判决买家违背诚信原则、无正当理由拒不退还货物，限10日内返还",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-035",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "淘宝",
    "amount_yuan": 1230,
    "buyer_reason": "【红线风险案例35】要求退全款",
    "evidence": "公权力机关认定买家存在虚构事实敲诈勒索商誉行为，已立案侦办",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-036",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 510,
    "buyer_reason": "【红线风险案例36】申请仅退款",
    "evidence": "买家短时间内同地址更换8个不同手机号连续申请20笔仅退款，命中职业索赔黑名单",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-037",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 1570,
    "buyer_reason": "【红线风险案例37】申请退货退款",
    "evidence": "退回包裹中填塞废纸报纸，商品被调包，顺丰快递员出具开箱异常证明",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-038",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 579,
    "buyer_reason": "【红线风险案例38】决定退货",
    "evidence": "买家正常申请退货退款，并按时提供真实有效的回寄运单号",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-039",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 489,
    "buyer_reason": "【红线风险案例39】申请仅退款",
    "evidence": "买家虽态度非常强硬并扬言差评，但未发现调包或虚构事实的法定认定凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-040",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 460,
    "buyer_reason": "【红线风险案例40】买家理由未公开",
    "evidence": "平台单方系统原因直接全额退款，未见买家违背诚信或拒不退货记录",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-041",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 590,
    "buyer_reason": "【红线风险案例41】申请仅退款拦截快递",
    "evidence": "警方查明该团伙注册12个虚拟账号批量仅退款，对组织者予以行政拘留",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-042",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "京东",
    "amount_yuan": 7220,
    "buyer_reason": "【红线风险案例42】申请退货退款",
    "evidence": "商家当场验货拆箱录像显示，退回物品为两瓶矿泉水，原装单反相机被调包",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-043",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "拼多多",
    "amount_yuan": 4630,
    "buyer_reason": "【红线风险案例43】申请仅退款",
    "evidence": "法院判决书认定买家收到手机后虚构未收到货事实且拒不退货，构成不当得利",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "signed_7d_late"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-044",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 790,
    "buyer_reason": "【红线风险案例44】买家理由未公开",
    "evidence": "法院判决买家违背诚信原则、无正当理由拒不退还货物，限10日内返还",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-045",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "京东",
    "amount_yuan": 1330,
    "buyer_reason": "【红线风险案例45】要求退全款",
    "evidence": "公权力机关认定买家存在虚构事实敲诈勒索商誉行为，已立案侦办",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_confirmed_defect"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-046",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "拼多多",
    "amount_yuan": 610,
    "buyer_reason": "【红线风险案例46】申请仅退款",
    "evidence": "买家短时间内同地址更换8个不同手机号连续申请20笔仅退款，命中职业索赔黑名单",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "buyer_3_refunds_30d"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-047",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "appliance",
    "platform": "淘宝",
    "amount_yuan": 1670,
    "buyer_reason": "【红线风险案例47】申请退货退款",
    "evidence": "退回包裹中填塞废纸报纸，商品被调包，顺丰快递员出具开箱异常证明",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "Y",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-048",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "京东",
    "amount_yuan": 679,
    "buyer_reason": "【红线风险案例48】决定退货",
    "evidence": "买家正常申请退货退款，并按时提供真实有效的回寄运单号",
    "gold_l1": "Y",
    "gold_l2": "Y",
    "gold_l3": "N",
    "evidence_ids": [
      "desc_matches"
    ],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-049",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "food",
    "platform": "拼多多",
    "amount_yuan": 589,
    "buyer_reason": "【红线风险案例49】申请仅退款",
    "evidence": "买家虽态度非常强硬并扬言差评，但未发现调包或虚构事实的法定认定凭证",
    "gold_l1": "Y",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "win",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  },
  {
    "case_id": "STRESS-RED-050",
    "axis": "compliance_redline",
    "axis_zh": "合规红线",
    "category": "clothing",
    "platform": "淘宝",
    "amount_yuan": 560,
    "buyer_reason": "【红线风险案例50】买家理由未公开",
    "evidence": "平台单方系统原因直接全额退款，未见买家违背诚信或拒不退货记录",
    "gold_l1": "N",
    "gold_l2": "N",
    "gold_l3": "N",
    "evidence_ids": [],
    "gold_bayes": "lose",
    "rationale": "检验模型对法定欺诈、调包退货、恶意批量索赔等高危红线信号的硬性触发与精准防御能力"
  }
]

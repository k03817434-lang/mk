# m2/mock_menus.py — M2 模拟菜单锁死数据文件
# 全部是模拟数据，不是真实店铺菜单和账单。面试时必须主动说明。
# 4 家店：S1–S3 外卖店 + S4 电商女装店，同一套求解器跑两边，证明穿底逻辑不分渠道。
# 每家店 6 个商品，1 个引流亏本品（毛利为负），1 条满减规则。
# 公式锁死（写在 m2/solver.py 里，不许改），费率按店取：
#   实收 = 总价 - 满减 - 佣金，佣金 = 该店佣金率 × (总价 - 满减)
#   利润 = 实收 - 总成本 - 该店配送/物流成本
#   利润 < 0 就是穿底（负毛利组合）
# 外卖店：佣金 15%，配送成本 ¥2/单；电商店：佣金 5%，物流成本 ¥8/单。

MOCK_STORES = [
    {
        "store_id": "S1",
        "store_name": "咔滋炸鸡（模拟·外卖）",
        "channel": "takeaway",
        "commission_rate": 0.15,
        "delivery_cost_yuan": 2,
        "rule_text": "满30减15，引流烤肠限购1份但暂未设置不与满减同享",
        "rule": {"type": "满减", "threshold": 30, "off": 15},
        "loss_leader_id": "sausage",
        "skus": [
            {"id": "drumstick", "name": "招牌炸鸡腿", "price": 18, "cost": 9},
            {"id": "popcorn", "name": "鸡米花", "price": 12, "cost": 8},
            {"id": "fries", "name": "薯条", "price": 10, "cost": 3},
            {"id": "cola", "name": "可乐", "price": 8, "cost": 2},
            {"id": "sausage", "name": "引流烤肠", "price": 5, "cost": 6},
            {"id": "wings", "name": "鸡翅", "price": 15, "cost": 8},
        ],
    },
    {
        "store_id": "S2",
        "store_name": "川香冒菜（模拟·外卖）",
        "channel": "takeaway",
        "commission_rate": 0.15,
        "delivery_cost_yuan": 2,
        "rule_text": "满25减10，引流素菜限购1份但暂未设置不与满减同享",
        "rule": {"type": "满减", "threshold": 25, "off": 10},
        "loss_leader_id": "veggie",
        "skus": [
            {"id": "beef", "name": "肥牛", "price": 20, "cost": 12},
            {"id": "tripe", "name": "毛肚", "price": 18, "cost": 11},
            {"id": "tofu", "name": "豆皮", "price": 8, "cost": 3},
            {"id": "noodle", "name": "粉条", "price": 7, "cost": 2},
            {"id": "veggie", "name": "引流素菜", "price": 4, "cost": 5},
            {"id": "luncheon", "name": "午餐肉", "price": 14, "cost": 8},
        ],
    },
    {
        "store_id": "S3",
        "store_name": "茶小憩（模拟·外卖）",
        "channel": "takeaway",
        "commission_rate": 0.15,
        "delivery_cost_yuan": 2,
        "rule_text": "满20减5，引流绿茶限购1份但暂未设置不与满减同享",
        "rule": {"type": "满减", "threshold": 20, "off": 5},
        "loss_leader_id": "greentea",
        "skus": [
            {"id": "milktea", "name": "招牌奶茶", "price": 16, "cost": 6},
            {"id": "lemon", "name": "柠檬茶", "price": 12, "cost": 4},
            {"id": "fruit", "name": "水果茶", "price": 18, "cost": 8},
            {"id": "pearl", "name": "珍珠小料", "price": 3, "cost": 1},
            {"id": "greentea", "name": "引流绿茶", "price": 6, "cost": 7},
            {"id": "cake", "name": "蛋糕", "price": 20, "cost": 10},
        ],
    },
    {
        "store_id": "S4",
        "store_name": "衣橱女装（模拟·电商）",
        "channel": "ecommerce",
        "commission_rate": 0.05,
        "delivery_cost_yuan": 8,
        "rule_text": "满150减60，引流袜子限购1份但暂未设置不与满减同享",
        "rule": {"type": "满减", "threshold": 150, "off": 60},
        "loss_leader_id": "socks",
        "skus": [
            {"id": "dress", "name": "连衣裙", "price": 89, "cost": 45},
            {"id": "tee", "name": "T恤", "price": 49, "cost": 22},
            {"id": "jeans", "name": "牛仔裤", "price": 79, "cost": 38},
            {"id": "scarf", "name": "围巾", "price": 29, "cost": 12},
            {"id": "socks", "name": "引流袜子", "price": 9, "cost": 12},
            {"id": "base", "name": "打底衫", "price": 39, "cost": 18},
        ],
    },
]

# 修复建议（锁死，不许自己发明别的修法）：
# 引流菜限购 1 份，且不与满减同享。修复后重跑一遍，报告穿底组合数下降了多少。
FIX_RULE = "引流菜限购1份且不与满减同享"

# -*- coding: utf-8 -*-
"""core/real_views.py — M0–M3 真实数据与案例定档渲染视图
包含 4 个 JSON 真实数据在 Streamlit 页面上的结构化渲染。
"""
import streamlit as st
import pandas as pd
from core.real_data import get_m0_real_data, get_m1_real_data, get_m2_real_data, get_m3_real_data

def render_m0_real():
    """渲染 M0 真实数据与两阶段先验定档"""
    m0 = get_m0_real_data()
    
    st.markdown(
        '<div style="color: #0d47a1; font-weight: bold; font-size: 15px; padding: 10px 14px; background-color: #e3f2fd; border-left: 4px solid #1976d2; margin-bottom: 20px; border-radius: 4px;">'
        '📌 <strong>数据来源</strong>：57 条公开司法裁判文书与平台售后投诉案卷（定档版 v1）。'
        '<br><span style="font-size: 13px; font-weight: normal; color: #1565c0;">注：真实数据作对比与先验参考标注，系统决策沙盘中的先验数值保持原样，两套数据并存展示。</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # 1. Headline 对比看板
    st.subheader("📢 核心定档 Headline：平台 vs 司法 两阶段胜率逆转")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="⚡ 平台抗辩阶段：买家胜率",
            value="89.5%",
            delta="-79.0% 商家赢面极低 (34/38明确裁决)",
            delta_color="inverse"
        )
        st.caption("争议样本统计：38 起明确裁决中，平台判买家 34 起、判商家 1 起、部分和解 3 起，另有 19 起未公开。")
    with col2:
        st.metric(
            label="⚖️ 司法诉讼阶段：商家胜率",
            value="76.2%",
            delta="+76.2% 法院支持商家 (16/21案)",
            delta_color="normal"
        )
        st.caption("终局裁决统计：20 起判决中商家胜诉 16 起、败诉 4 起，另有 1 起起诉后和解。")

    st.markdown(
        """
        > 💡 **核心决策洞察**：**平台裁决与司法判决呈现方向性逆转！**  
        > 平台阶段争议样本多来自买家投诉维权，存在明显样本选择偏误（能上热搜或投诉的多是买家赢的案子），若直接作为先验会严重低估商家抗辩赢面。  
        > **先验数值决策**：系统当前保持模拟先验（服装 0.48 / 食品 0.55 / 家电 0.60），真实统计区间作为标注参考，新数值待 Phase 3 商家后台数据接入后再行调优。
        """
    )
    
    st.markdown("---")

    # 2. 两阶段分类胜率区间表
    st.subheader("📊 两阶段分品类胜率与观测区间对比")
    p_stage = m0.get("platform_stage", {}).get("by_category", {})
    c_stage = m0.get("court_stage", {}).get("by_category", {})
    
    cats = [
        ("appliance", "数码家电"),
        ("clothing", "服装鞋包"),
        ("food", "食品生鲜"),
        ("other", "其他日化品类"),
    ]
    rows = []
    for cat_key, cat_name in cats:
        p_info = p_stage.get(cat_key, {})
        c_info = c_stage.get(cat_key, {})
        rows.append({
            "商品类目": cat_name,
            "平台阶段买家胜数": f"{p_info.get('buyer', 0)} / {p_info.get('n_clear', 0)}",
            "平台商家赢面观测": f"{p_info.get('merchant_win_rate', 0)*100:.1f}%",
            "法院判决商家胜数": f"{c_info.get('merchant_win', 0)} / {c_info.get('n_judgments', 0)}",
            "司法阶段商家胜率": f"{c_info.get('merchant_win_rate', 0)*100:.1f}%",
        })
    rows.append({
        "商品类目": "🔥 全品类总体",
        "平台阶段买家胜数": "34 / 38",
        "平台商家赢面观测": "10.5%",
        "法院判决商家胜数": "16 / 21",
        "司法阶段商家胜率": "76.2%",
    })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.markdown("---")

    # 3. 关键边界案判定（定档依据）
    st.subheader("🔍 关键边界案例定性记录（Ken 授权定档）")
    boundary_flags = m0.get("boundary_flags", [])
    for b in boundary_flags:
        st.markdown(f"- **案例 `{b.get('id')}`**：{b.get('issue')}\n  - 📌 **定性结论**：{b.get('decision')}")

    st.markdown("---")

    # 4. 标杆案与反向案例
    st.subheader("⚖️ 典型标杆案例剖析：期望维权成本 vs 规则自治边界")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("#### 💰 成本-of-winning 案例（赢了官司输了钱）")
        st.error(
            "**案例 R-M0-42**：\n"
            "- **案情**：买家仅退款 ¥60+ 服装商品，商家千里跨省维权并最终获胜诉；\n"
            "- **代价**：追回货款 ¥60+，但耗费差旅与误工成本 **¥4,000+**！\n"
            "- **启示**：证明中小商家售后博弈中，**维权期望成本比胜率更关键**，盲目抗辩往往击穿毛利。"
        )
        st.success(
            "**案例 R-M0-39**（最高法工作报告标杆案例）：\n"
            "- **案情**：平台判定仅退款严重侵犯商家合法财产权益；\n"
            "- **判决**：法院判决平台向商家承担侵权连带赔偿责任，赔偿商家 **¥760,000+**。"
        )
    with col_c2:
        st.markdown("#### 🛡️ 反向案例（平台仅退款自治规则边界）")
        st.warning(
            "**案例 R-M0-57**（平台规则自治获得司法支持）：\n"
            "- **案情**：商家不满平台“仅退款”裁决诉至法院要求赔偿；\n"
            "- **裁判**：法院认定买卖双方入驻前均签署服务协议，平台依据协议争议解决条款做出的售后处理属于**契约自治范畴**，依法驳回商家诉求；\n"
            "- **启示**：明确了司法对平台规则自治的尊重边界，非严重过错下平台仲裁受协议约束。"
        )


def render_m1_real():
    """渲染 M1 真实数据与规则覆盖缺口"""
    m1 = get_m1_real_data()

    st.markdown(
        '<div style="color: #0d47a1; font-weight: bold; font-size: 15px; padding: 10px 14px; background-color: #e3f2fd; border-left: 4px solid #1976d2; margin-bottom: 20px; border-radius: 4px;">'
        '📌 <strong>数据来源</strong>：37 条真实电商商品上架案例（含 27 个 live 样本：淘宝 14 + 拼多多 13，以及 10 个历史样本）。'
        '<br><span style="font-size: 13px; font-weight: normal; color: #1565c0;">注：真实案例用于评估现有规则覆盖度与缺口，现有 12 案例模拟质检器原样保留。</span>'
        '</div>',
        unsafe_allow_html=True
    )

    # 1. 37 条判定总计
    st.subheader("📋 37 条真实商品质检判定分布")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🚨 冲突拦截", "9 条 (24.3%)", "实存虚假信息")
    c2.metric("⚠️ 人工核验", "20 条 (54.1%)", "模糊缺失/占比最高")
    c3.metric("✅ 一致合规", "7 条 (18.9%)", "准予上架")
    c4.metric("❓ 无法判定", "1 条 (2.7%)", "R-M1-25 采集受限")
    st.caption("注：在 27 个现场采集的 live 样本中，分布为：通过 6 条、人工核验 19 条、拦截 1 条、无法判定 1 条。绝大多数线上商品存在模糊缺失表述。")

    st.markdown("---")

    # 2. 规则覆盖与三大缺口
    st.subheader("🎯 8 大平台质检规则真实案例覆盖与缺口分析")
    
    # 缺口警告
    st.error(
        "🚨 **三大关键规则缺口（必须标出）**：\n"
        "1. **R3 件数冲突缺口**：真实冲突案仍为 **0 条**（仅有模糊实例 2 条：R-M1-36/37 买一送一标题自洽但属性缺失件数）；规则过窄只写“买一送一”，对 R-M1-22 这类纯数字不一致（36包/18包/72包）需补通用条款；\n"
        "2. **R4 保质期冲突缺口**：两平台采集未抓到干净的两值冲突，冲突真实例仍为 **0 条**（弱候选 1 条 R-M1-30，模糊实例 10 条）；\n"
        "3. **R5 材质模糊缺口**：**0 条**精确实例（无案件使用“其他/见包装/未注明”等标准模糊词，仅有 R-M1-15、16 近似案例）。"
    )

    rules_data = m1.get("rules", [])
    table_rows = []
    for r in rules_data:
        status = r.get("status", "")
        cases_str = ", ".join(r.get("real_cases", [])) if r.get("real_cases") else "无"
        table_rows.append({
            "规则编号": r.get("id"),
            "规则类型": r.get("type"),
            "依据标准/法条": r.get("source"),
            "真实例覆盖状态": status,
            "对标真实案例": cases_str,
            "真实证据摘要": r.get("evidence", "")
        })
    st.dataframe(pd.DataFrame(table_rows), use_container_width=True, hide_index=True)

    st.markdown("---")

    # 3. 范围外扩展发现
    st.subheader("🔍 模型范围外扩展发现（Phase 3 升级清单）")
    st.markdown(
        "- **R-M1-09 品牌/正品冲突（“里序正品”实发 jolly 劣质包）**：M1 是 4 字段模型（材质/净含量/件数/保质期），品牌不在 4 字段内，属于范围外，记为 Phase 3 候选扩展；\n"
        "- **R-M1-10 平台误判场景**：三处完全一致仍判商家承担运费，检出率不能只算冲突检出，也是 M1 必须对抗覆盖的典型场景。"
    )


def render_m2_real():
    """渲染 M2 真实电商旗舰店活动穿底推演实测"""
    m2 = get_m2_real_data()

    st.markdown(
        '<div style="color: #0d47a1; font-weight: bold; font-size: 15px; padding: 10px 14px; background-color: #e3f2fd; border-left: 4px solid #1976d2; margin-bottom: 20px; border-radius: 4px;">'
        '📌 <strong>数据来源</strong>：天猫/拼多多官方旗舰店真实在售商品价格与满减规则实测（伊芙丽、全棉时代、三只松鼠天猫/拼多多、蓝月亮）。'
        '<br><span style="font-size: 13px; font-weight: normal; color: #1565c0;">注：模拟 4 家外卖沙盘原样保留，本节专门展示真实电商版旗舰店实算结果。</span>'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("🏪 电商旗舰店真实活动穿底求解实测（三家已定档）")

    # 店铺 1：伊芙丽
    with st.container():
        st.markdown("### 1. 👗 伊芙丽官方旗舰（天猫·女装）——【已定档，0 穿底】")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("在售 SKU", "7 款真实服饰", "原价 ¥299 ~ ¥798")
        col_b.metric("店铺券档位", "满799减30 / 满1299减50", "约 3.8% 折扣")
        col_c.metric("穷举 784 组合穿底数", "0 种 (0.0%)", "全部盈利安全")
        st.info(
            "💡 **实测结论**：两档券 × 两种成本率（40%/50%），四种组合全部 **0 穿底**。\n"
            "- 最亏组合（2×保暖绒感休闲裤，原价 ¥798，差 ¥1 未达 799 门槛）仍大幅**盈利 ¥430.9**（40%成本率）/ **¥351.1**（50%成本率）；\n"
            "- **商业本质**：服饰毛利高且券力度仅 3.8% 左右，券太浅，确定性求解器证明无需修改规则。"
        )

    st.markdown("---")

    # 店铺 2：全棉时代
    with st.container():
        st.markdown("### 2. 🧻 全棉时代官方旗舰店（天猫·日用）——【已定档，0 穿底】")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("在售 SKU", "5 款在售日用品", "原价 ¥11.9 ~ ¥108.0")
        col_b.metric("店铺满减档位", "满200减25 / 满480减60", "同为 12.5% 折扣")
        col_c.metric("穷举 246 组合穿底数", "0 种 (0.0%)", "全部盈利安全")
        st.info(
            "💡 **实测结论**：四种成本率与满减组合全部 **0 穿底**。\n"
            "- 最亏组合：2×洗脸巾20抽体验装（原价 ¥23.8），最亏仍**盈利 ¥5.0**（40%成本率）/ **¥2.6**（50%成本率）；\n"
            "- **关键洞察**：单笔原价低的小单，虽然满减未穿底，但 ¥8 物流/履约成本几乎吞噬了小单全部毛利。"
        )

    st.markdown("---")

    # 店铺 3：三只松鼠天猫
    with st.container():
        st.markdown("### 3. 🐿️ 三只松鼠旗舰店（天猫·零食）——【唯一跑出真实穿底的电商店铺】")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("在售 SKU", "6 款休闲零食", "原价 ¥14.9 ~ ¥59.0")
        col_b.metric("活动满减", "满99减30", "高达 30.3% 折扣")
        col_c.metric("限购过滤后有效穿底", "24 种 (7.0%)", "40%成本率下实测", delta_color="inverse")
        
        st.error(
            "🚨 **三只松鼠真实穿底数据与归因剖析**：\n"
            "- **组合穷举**：原始穷举 455 种组合，穿底 54 种（11.9%）@40% / 74 种（16.3%）@50%；\n"
            "- **限购过滤后**（肉片尝鲜装限购 1 件、其余小件 ≤ 3 件）：**有效组合 343 种，穿底 24 种（7.0%）@40% / 35 种（10.2%）@50%**；\n"
            "- **有效最亏组合**：`高蛋白肉片尝鲜装×1 + 益生元坚果山楂棒×1`（实付总价 ¥27.8），**净亏损 −¥8.0**（40%）/ **−¥8.9**（50%）；\n"
            "- **深度归因**：**漏检本质是小额订单 + ¥13 运费，而不是满减**！能触发满 99 减 30 的大单毛利足够抗住折扣，穿底的全是凑不到 ¥99 门槛、被单笔固定履约运费吃穿毛利的小篮子！"
        )

    st.markdown("---")

    # 归档与弃用店铺
    st.subheader("📦 归档与弃用店铺说明")
    st.markdown(
        "- **蓝月亮官方旗舰（拼多多·日用）——【归档】**：规则已采全（满54减15 / 满99减50 等，满99减50为最陡规则），但拼多多网页端原价被遮挡（仅显示券后价），不符合求解器输入标准，记作极端参考归档；\n"
        "- **三只松鼠官方旗舰（拼多多·零食）——【弃用】**：无原价且无店铺满减（仅百亿补贴与首件立减，属平台补贴），不符合店铺决策场景，弃用不展示。"
    )


def render_m3_real():
    """渲染 M3 真实行政执法案例与模式缺口"""
    m3 = get_m3_real_data()

    st.markdown(
        '<div style="color: #0d47a1; font-weight: bold; font-size: 15px; padding: 10px 14px; background-color: #e3f2fd; border-left: 4px solid #1976d2; margin-bottom: 20px; border-radius: 4px;">'
        '📌 <strong>数据来源</strong>：20 条真实市场监管行政处罚案卷与平台合规判罚（覆盖罚金 ¥2,000 ～ ¥1,750,000）。'
        '<br><span style="font-size: 13px; font-weight: normal; color: #1565c0;">注：模拟话术扫描器原样保留，本节展示市场监管执法尺度与真实法条案例映射。</span>'
        '</div>',
        unsafe_allow_html=True
    )

    # 1. 罚金与执法力度看板
    st.subheader("💰 真实市场监管处罚力度看板")
    col1, col2, col3 = st.columns(3)
    col1.metric("真实案例总数", "20 起", "14 起有明确罚金")
    col2.metric("处罚金额区间", "¥2,000 ～ ¥1,750,000", "最高辛选艾草三伏贴")
    col3.metric("平台执法时效", "10秒中断 ~ 5分钟限流", "限流 60%–80%")

    st.markdown("---")

    # 2. 6 条规则对标真实案例映射
    st.subheader("📜 6 大合规规则与真实案件映射总览表")
    rules = m3.get("rules", [])
    rows = []
    for r in rules:
        cases_str = ", ".join(r.get("real_cases", [])) if r.get("real_cases") else "无"
        rows.append({
            "规则编号": r.get("id"),
            "违规类型": r.get("type"),
            "法定依据/规范": r.get("source"),
            "真实案例文号": cases_str,
            "法条核心要求": r.get("text"),
            "真实执法证据摘要": r.get("evidence", "")
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.markdown("---")

    # 3. 4 大模式缺口（升级路线）
    st.subheader("⚠️ 真实案例暴露的 4 大模式缺口（规则升级路线）")
    gaps = m3.get("pattern_gaps", [])
    for idx, g in enumerate(gaps, 1):
        st.warning(
            f"**缺口 {idx}：关键词 `{', '.join(g.get('words', []))}`**\n"
            f"- **案源出处**：{g.get('from')}\n"
            f"- **升级建议**：{g.get('action')}"
        )

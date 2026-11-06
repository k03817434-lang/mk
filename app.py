# app.py — MK Demo Streamlit 页面 (D1+D2+D3)
import os
import json
import pandas as pd
import streamlit as st
from mock_data import MOCK_CASES, CATEGORY_NAMES, SLIDER, EVIDENCE_RULES
from core.bayes import calc_win_prob, get_case_evidence_details
from core.cost import calc_paths
from m2.mock_menus import MOCK_STORES, FIX_RULE
from m2.solver import enumerate_combos, apply_fix, translate_rule
from m1.mock_products import PRODUCTS, RULES
from m1.specdiff import diff_product, llm_adjudicate_stub
from m3.mock_scripts import SCRIPTS
from m3.scanner import scan_script, llm_rewrite_stub
from core.real_views import (
    render_m0_real,
    render_m1_real,
    render_m2_real,
    render_m3_real
)

# 页面基础配置
st.set_page_config(page_title="MarginKeeper (MK)", layout="wide")

# 全站顶栏
st.title("MarginKeeper — 电商售后合规与博弈决策台")
st.markdown("##### 帮中小商家在仅退款、满减穿底、直播违规之前，先算清每一分钱。")
st.markdown(
    '<div style="color: #d32f2f; font-weight: bold; font-size: 15px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
    '全部数据为模拟 / 假设，不是真实店铺数据与实测结果。'
    '</div>',
    unsafe_allow_html=True
)

# 顶层五页签（顺序：M0 售后决策 / M1 上架质检 / M2 活动推演 / M3 直播合规 / M4 评测报告）
tab_m0, tab_m1, tab_m2, tab_m3, tab_m4 = st.tabs(["M0 售后决策", "M1 上架质检", "M2 活动推演", "M3 直播合规", "M4 评测报告"])

# =========================================================================
# 页签 1：M0 售后决策（原样保留 D1、D2 全部逻辑与文案，一行不改）
# =========================================================================
with tab_m0:
    m0_sub_sim, m0_sub_real = st.tabs(["📊 模拟决策沙盘 (Demo)", "📁 真实业务数据与裁判文书 (60 案)"])
    with m0_sub_sim:
        # 顶部必显警示红字
        st.markdown(
            '<div style="color: #d32f2f; font-weight: bold; font-size: 16px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
            '模拟数据 / 假设，不是实测结果。月省 ¥8,400 是情景计算。'
            '</div>',
            unsafe_allow_html=True
        )

        st.title("MarginKeeper (MK) — 售后决策小工具")

        # 三栏布局：左侧工单信息、中间贝叶斯小票、右侧决策滑块与五条路期望成本
        col_left, col_mid, col_right = st.columns([1, 1.1, 1.2], gap="medium")

        # ==================== 左边：工单选择与详情 ====================
        with col_left:
            st.subheader("📋 售后工单选择")
            case_ids = [c["case_id"] for c in MOCK_CASES]
            selected_id = st.selectbox("选择工单编号", case_ids, index=0)
        
            current_case = next(c for c in MOCK_CASES if c["case_id"] == selected_id)
            category_zh = CATEGORY_NAMES.get(current_case["category"], current_case["category"])
        
            st.markdown("---")
            st.markdown(f"**工单编号**: `{current_case['case_id']}`")
            st.markdown(f"**商品类目**: {category_zh}")
            st.markdown(f"**电商平台**: {current_case['platform']}")
            st.markdown(f"**买家理由**: {current_case['buyer_reason']}")
            st.markdown(f"**争议金额**: <span style='font-size: 18px; color: #e65100; font-weight: bold;'>¥{current_case['amount_yuan']}</span>", unsafe_allow_html=True)
            st.markdown(f"**聊天摘要**: {current_case['chat_note']}")

        # ==================== 中间：贝叶斯小票 ====================
        prior, applied_rules = get_case_evidence_details(current_case)
        win_prob = calc_win_prob(current_case)

        with col_mid:
            st.subheader("🧾 贝叶斯小票")
            st.caption("依据先验与客诉证据动态计算抗辩赢面")
        
            # 贝叶斯公式展示
            st.markdown("**计算公式**：")
            st.latex(r"P(\text{商家胜}|\text{证据}) \propto P(\text{证据}|\text{商家胜}) \times P(\text{商家胜})")
        
            st.markdown("---")
            st.markdown(f"**基础先验（{category_zh}类目）**: `{prior * 100:.1f}%`")
        
            st.markdown("**命中证据加减分**：")
            if applied_rules:
                for r in applied_rules:
                    delta_val = r["delta"]
                    delta_str = f"+{delta_val * 100:.0f}%" if delta_val > 0 else f"{delta_val * 100:.0f}%"
                    color = "#2e7d32" if delta_val > 0 else "#c62828"
                    st.markdown(
                        f"- <span style='color: {color}; font-weight: bold;'>[{delta_str}]</span> {r['text']}",
                        unsafe_allow_html=True
                    )
            else:
                st.markdown("- 无匹配证据规则")
            
            st.markdown("---")
            win_pct = int(round(win_prob * 100))
            st.metric(label="最终胜率 (抗辩赢面)", value=f"{win_pct}%")
            st.progress(win_prob)

        # ==================== 右边：滑块与五条路 ====================
        with col_right:
            st.subheader("⚖️ 决策倾向与五条路")
        
            slider_val = st.slider(
                label="老板倾向滑块（0 保利润 ← 50 均衡 → 100 保评分）",
                min_value=SLIDER["min"],
                max_value=SLIDER["max"],
                value=SLIDER["default"],
                step=1
            )
        
            # 滑块提示说明
            if slider_val < 30:
                st.info(f"💡 **倾向**：{SLIDER['left_label']} — {SLIDER['left_tip']}")
            elif slider_val > 70:
                st.info(f"💡 **倾向**：{SLIDER['right_label']} — {SLIDER['right_tip']}")
            else:
                st.info(f"💡 **倾向**：均衡 — {SLIDER['mid_tip']}")
            
            st.markdown("---")
            st.markdown("**五条路期望成本（推荐项高亮）**：")
        
            paths_result = calc_paths(current_case, win_prob, slider_val)
        
            for p in paths_result:
                pid = p["id"]
                name = p["name"]
                desc = p["desc"]
                cost = p["expected_cost"]
                is_rec = p["is_recommended"]
            
                if is_rec:
                    st.markdown(
                        f"""
                        <div style="border: 2px solid #2e7d32; background-color: #e8f5e9; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px;">
                            <span style="background-color: #2e7d32; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold;">⭐ 推荐方案</span>
                            <strong style="font-size: 15px; margin-left: 6px;">路径 {pid}：{name}</strong>
                            <div style="font-size: 13px; color: #555; margin-top: 3px;">{desc}</div>
                            <div style="margin-top: 5px; font-size: 15px; font-weight: bold; color: #1b5e20;">期望成本：¥{cost:.1f}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div style="border: 1px solid #e0e0e0; background-color: #fafafa; border-radius: 8px; padding: 8px 14px; margin-bottom: 8px;">
                            <strong>路径 {pid}：{name}</strong>
                            <span style="font-size: 12px; color: #777; margin-left: 6px;">({desc})</span>
                            <div style="font-size: 14px; color: #333; margin-top: 3px;">期望成本：¥{cost:.1f}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # ==================== 底部：证据包占位 ====================
        st.divider()
        st.subheader("📦 证据包清单（占位）")
        st.caption("注：今日为 D1 阶段，仅展示提取的证据清单文字，不生成正式申诉文书。")

        if applied_rules:
            for idx, rule in enumerate(applied_rules, 1):
                st.markdown(f"**证据 {idx}**：`{rule['id']}` — {rule['text']}（影响度: {rule['delta']:+.2f}）")
        else:
            st.markdown("暂无可用证据清单")

        # ==================== 评测报告（D2 新增折叠栏） ====================
        with st.expander("评测报告（模拟）"):
            report_file = os.path.join(os.path.dirname(__file__), "eval", "eval_report.md")
            if os.path.exists(report_file):
                with open(report_file, "r", encoding="utf-8") as f:
                    st.markdown(f.read(), unsafe_allow_html=True)
            else:
                st.info("还没跑评测，先在终端跑 python eval/run_eval.py")


    # =========================================================================
    # 页签 2：M1 上架质检（D4 新增）
    with m0_sub_real:
        render_m0_real()

# =========================================================================
with tab_m1:
    m1_sub_sim, m1_sub_real = st.tabs(["📊 演示案例质检 (12 商品)", "📁 真实业务规则与黑猫案例 (37 案)"])
    with m1_sub_sim:
        # 顶部一行红字横幅
        st.markdown(
            '<div style="color: #d32f2f; font-weight: bold; font-size: 16px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
            '模拟商品 / 假设，不是真实店铺商品。'
            '</div>',
            unsafe_allow_html=True
        )
        st.title("M1 SpecDiff — 上架多维交叉质检")

        # 1. 商品选择与详情
        col_prod_sel, col_prod_info = st.columns([1, 2], gap="medium")
        with col_prod_sel:
            prod_options = {p["id"]: f"{p['id']} - {p['name']} ({p['category']})" for p in PRODUCTS}
            selected_pid = st.selectbox("选择质检商品", list(prod_options.keys()), format_func=lambda x: prod_options[x], index=0)
            cur_prod = next(p for p in PRODUCTS if p["id"] == selected_pid)
            diff_res = diff_product(cur_prod)

        with col_prod_info:
            st.markdown(f"**商品完整标题**：`{cur_prod['title']}`")
            st.markdown(f"**SKU规格包装**：`{cur_prod['sku_pack']}` ｜ **促销说明**：`{cur_prod['promo']}` ｜ **所属类目**：`{cur_prod['category']}`")

        st.markdown("---")

        # 2. 三列交叉比对表
        st.subheader("🔍 三处信息交叉比对表（标题 / 属性表 / 详情页）")
        rows_html = ""
        for row in diff_res["field_diffs"]:
            status = row["status"]
            if status == "conflict":
                bg = "background-color: #ffebee; color: #c62828; font-weight: bold;"
                status_badge = '<span style="background-color: #c62828; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px;">🚨 冲突拦截</span>'
            elif status == "fuzzy":
                bg = "background-color: #fffde7; color: #b78103; font-weight: bold;"
                status_badge = '<span style="background-color: #f57f17; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px;">⚠️ 模糊缺失</span>'
            else:
                bg = "background-color: #fafafa; color: #333;"
                status_badge = '<span style="background-color: #2e7d32; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px;">✅ 一致合规</span>'

            rows_html += f'<tr style="border-bottom: 1px solid #e0e0e0; {bg}"><td style="padding: 10px;">{row["name"]}</td><td style="padding: 10px;">{row["title_val"]}</td><td style="padding: 10px;">{row["attr_val"]}</td><td style="padding: 10px;">{row["detail_val"]}</td><td style="padding: 10px;">{status_badge}</td></tr>'

        table_html = f'<table style="width: 100%; border-collapse: collapse; font-size: 15px; margin-bottom: 20px;"><thead><tr style="border-bottom: 2px solid #ddd; background-color: #f1f3f4; text-align: left;"><th style="padding: 10px;">比对字段</th><th style="padding: 10px;">标题表述</th><th style="padding: 10px;">属性表填报</th><th style="padding: 10px;">详情页说明</th><th style="padding: 10px;">校验状态</th></tr></thead><tbody>{rows_html}</tbody></table>'
        st.markdown(table_html, unsafe_allow_html=True)

        # 3. 裁决横幅
        st.markdown("---")
        verdict = diff_res["verdict"]
        if verdict == "conflict":
            st.error("🚨 **质检裁决：拦截（禁止上架）** — 存在虚假宣传与信息冲突风险，平台将予以扣分或下架处罚。")
        elif verdict == "fuzzy":
            st.warning("⚠️ **质检裁决：人工核验** — 存在模糊或缺失表述，需人工质检小二复核后再行发布。")
        else:
            st.success("✅ **质检裁决：通过（准予上架）** — 标题、属性表、详情页三处核心字段完全一致，符合平台合规标准。")

        # LLM 参考意见区（仅在判定为人工核验的模糊商品上显示，如 P11）
        if verdict == "fuzzy":
            cache_key_m1 = f"llm_m1_{cur_prod['id']}"
            if cache_key_m1 not in st.session_state:
                try:
                    st.session_state[cache_key_m1] = llm_adjudicate_stub(cur_prod, diff_res.get("suggestion", ""))
                except Exception:
                    st.session_state[cache_key_m1] = None
            llm_adv = st.session_state.get(cache_key_m1)

            st.markdown("#### 🤖 LLM 参考意见（仅供参考）")
            if llm_adv and isinstance(llm_adv, dict) and "verdict" in llm_adv and "reason" in llm_adv:
                llm_box_html = (
                    f'<div style="border-left: 4px solid #1976d2; background-color: #e3f2fd; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px;">'
                    f'<div style="font-size: 15px; color: #0d47a1; margin-bottom: 6px;"><strong>LLM 建议裁决</strong>：<code style="font-size: 14px; background-color: #bbdefb; padding: 2px 6px; border-radius: 3px;">{llm_adv["verdict"]}</code></div>'
                    f'<div style="font-size: 14px; color: #263238; margin-bottom: 6px;"><strong>LLM 理由</strong>：{llm_adv["reason"]}</div>'
                    f'<div style="font-size: 12px; color: #546e7a;">LLM 意见仅供参考，不改变锁定判定。</div>'
                    f'</div>'
                )
                st.markdown(llm_box_html, unsafe_allow_html=True)
            else:
                llm_box_html = (
                    f'<div style="border-left: 4px solid #b0bec5; background-color: #eceff1; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px;">'
                    f'<div style="font-size: 14px; color: #455a64; margin-bottom: 6px;">LLM 参考意见暂不可用（已回退）</div>'
                    f'<div style="font-size: 12px; color: #78909c;">LLM 意见仅供参考，不改变锁定判定。</div>'
                    f'</div>'
                )
                st.markdown(llm_box_html, unsafe_allow_html=True)

        # 4. 命中的规则与修正建议
        if diff_res["hit_rules"]:
            st.markdown("#### 📜 命中平台质检规则库：")
            for r in diff_res["hit_rules"]:
                st.markdown(f"- **[{r['id']}]**（出处：*{r['source']}*）: {r['text']}")

        st.info(f"💡 **一句话修正建议**：{diff_res['suggestion']}")

        # 5. 评测报告折叠栏
        st.markdown("---")
        with st.expander("评测报告（模拟）"):
            m1_report_file = os.path.join(os.path.dirname(__file__), "m1", "eval_report.md")
            if os.path.exists(m1_report_file):
                with open(m1_report_file, "r", encoding="utf-8") as f:
                    st.markdown(f.read(), unsafe_allow_html=True)
            else:
                st.info("还没跑评测，先在终端跑 python m1/run_eval.py")


    # =========================================================================
    # 页签 3：M2 活动推演（D3 新增）
    with m1_sub_real:
        render_m1_real()

# =========================================================================
with tab_m2:
    m2_sub_sim, m2_sub_real = st.tabs(["📊 演示活动沙盘 (3 模拟店)", "📁 真实电商店铺推演 (三只松鼠/全棉时代/伊芙丽)"])
    with m2_sub_sim:
        # 顶部一行红字必显
        st.markdown(
            '<div style="color: #d32f2f; font-weight: bold; font-size: 16px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
            '模拟菜单 / 假设，不是真实店铺账单。'
            '</div>',
            unsafe_allow_html=True
        )
        st.title("M2 活动穿底沙盘 — 跨渠道推演")

        # 1. 店铺选择与信息
        col_store_sel, col_store_info = st.columns([1, 2], gap="medium")
    
        with col_store_sel:
            store_names = [f"{s['store_id']} - {s['store_name']}" for s in MOCK_STORES]
            selected_store_name = st.selectbox("选择推演店铺", store_names, index=0)
            selected_sid = selected_store_name.split(" - ")[0]
            cur_store = next(s for s in MOCK_STORES if s["store_id"] == selected_sid)
            channel_label = "外卖渠道（美团/饿了么）" if cur_store["channel"] == "takeaway" else "电商渠道（淘宝/拼多多）"
        
            st.markdown(f"**所属渠道**：`{channel_label}`")
            st.markdown(f"**平台费率**：佣金 `{cur_store['commission_rate']*100:.0f}%` | 履约成本 `¥{cur_store['delivery_cost_yuan']}/单`")
            st.markdown(f"**人话规则原文**：")
            st.info(f"{cur_store['rule_text']}")

        with col_store_info:
            st.subheader("📖 该店菜单与商品毛利")
            menu_display = []
            for sku in cur_store["skus"]:
                is_loss = (sku["id"] == cur_store["loss_leader_id"])
                margin = sku["price"] - sku["cost"]
                menu_display.append({
                    "商品名称": f"🔥 {sku['name']}（引流亏本品）" if is_loss else sku["name"],
                    "售价 (¥)": f"¥{sku['price']}",
                    "成本 (¥)": f"¥{sku['cost']}",
                    "单品毛利 (¥)": f"¥{margin:+d}",
                })
            st.dataframe(menu_display, use_container_width=True, hide_index=True)

        st.markdown("---")

        # 2. 求解器计算
        all_combos, underwater = enumerate_combos(cur_store)
        fix_res = apply_fix(cur_store)

        st.subheader("📊 暴力穷举与穿底风险概览")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("2-5件穷举总组合数", f"{len(all_combos)} 种")
        m2.metric("穿底组合数 (利润<0)", f"{len(underwater)} 种", f"穿底率 {len(underwater)/len(all_combos)*100:.1f}%", delta_color="inverse")
        m3.metric("修复后穿底组合数", f"{fix_res['after_count']} 种")
        m4.metric("修复后穿底降幅", f"-{fix_res['decrease_pct']}%", "规则生效")

        # 3. 最亏 Top 10 表展示
        st.markdown("### 🚨 穿底最亏 Top 10 组合（客人凑单漏洞）")
        st.caption("提示：以下组合按单笔亏损最大（利润最低）排序，证明即使跨渠道，利用引流品凑满减同样会击穿毛利。")

        top10_list = []
        for rank, c in enumerate(underwater[:10], 1):
            top10_list.append({
                "排名": f"#{rank}",
                "组合内容": c["combo_text"],
                "件数": f"{c['item_count']} 件",
                "总价": f"¥{c['total_price']}",
                "满减": f"¥{c['discount']}",
                "平台实收": f"¥{c['net_receipt']}",
                "总成本": f"¥{c['total_cost']}",
                "净利润": f"¥{c['profit']}",
            })
        st.dataframe(top10_list, use_container_width=True, hide_index=True)

        # 4. 修复建议与对比
        st.markdown("---")
        st.subheader("🛠️ 穿底漏洞修复规则与前后对比")
        st.success(f"**锁死修复建议**：`{FIX_RULE}`")
        st.markdown(
            f"- **修复前穿底**：{fix_res['before_count']} 种组合（占总组合 {fix_res['before_count']/len(all_combos)*100:.1f}%）\n"
            f"- **修复后穿底**：{fix_res['after_count']} 种组合\n"
            f"- **穿底消除比例**：下降 {fix_res['decrease_pct']}%（实跑真实数值，不刷分、不凑数）"
        )

        # 5. Text-to-Solver 分工说明与自定义新规则推演入口
        st.markdown("---")
        st.subheader("🤖 Text-to-Solver：自定义新规则翻译与沙盘推演（DeepSeek-V3）")
        st.caption("ℹ️ **架构分工**：规则翻译占 15%（由 DeepSeek-V3 把人话规则解析为确定性约束），穷举求解占 85%（确定性算法暴力穷举账目），LLM 不直接算账，确保账目 100% 准确与抗幻觉。")

        col_rule_in, col_rule_btn = st.columns([3, 1], gap="small")
        with col_rule_in:
            custom_rule_input = st.text_input("输入新满减规则（如：满50减20）", value="满50减20", label_visibility="visible")
        with col_rule_btn:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            btn_trans = st.button("🚀 翻译并推演", use_container_width=True)

        if btn_trans or "custom_m2_parsed" in st.session_state:
            if btn_trans:
                st.session_state["custom_m2_input"] = custom_rule_input
                st.session_state["custom_m2_parsed"] = translate_rule(custom_rule_input)

            parsed_rule = st.session_state.get("custom_m2_parsed", translate_rule(custom_rule_input))
            st.markdown("**结构化规则 (JSON)**：")
            st.json(parsed_rule)

            # 用确定性求解器跑出穿底结果
            custom_store = dict(cur_store)
            custom_store["rule"] = parsed_rule
            c_all_combos, c_underwater = enumerate_combos(custom_store)
            st.markdown(
                f"**沙盘推演结果（当前店铺：{cur_store['store_name']}）**：\n"
                f"- 2-5件穷举总组合数：**{len(c_all_combos)}** 种\n"
                f"- 新规则穿底组合数 (利润<0)：**{len(c_underwater)}** 种（占 {len(c_underwater)/len(c_all_combos)*100:.1f}%）"
            )


    # =========================================================================
    # 页签 4：M3 直播合规（D6 新增）
    with m2_sub_real:
        render_m2_real()

# =========================================================================
with tab_m3:
    m3_sub_sim, m3_sub_real = st.tabs(["📊 演示话术扫描 (6 场次)", "📁 真实处罚案例与规则映射 (20 案)"])
    with m3_sub_sim:
        # 顶部一行红字横幅
        st.markdown(
            '<div style="color: #d32f2f; font-weight: bold; font-size: 16px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
            '模拟话术 / 假设，不是真实直播话术。'
            '</div>',
            unsafe_allow_html=True
        )
        st.title("M3 AdCompliance — 直播话术合规熔断")

        # 1. 场次选择与概览
        script_options = {s["id"]: f"{s['id']} - {s['name']}" for s in SCRIPTS}
        selected_sid = st.selectbox("选择直播话术场次", list(script_options.keys()), format_func=lambda x: script_options[x], index=0)
        cur_script = next(s for s in SCRIPTS if s["id"] == selected_sid)
        scan_res = scan_script(cur_script)

        # 2. 熔断灯横幅
        lamp = scan_res["lamp"]
        if lamp == "RED":
            st.error(f"🔴 **熔断警告：{scan_res['lamp_zh']}** — {scan_res['lamp_reason']}")
        elif lamp == "YELLOW":
            st.warning(f"🟡 **合规提醒：{scan_res['lamp_zh']}** — {scan_res['lamp_reason']}")
        else:
            st.success(f"🟢 **合规通过：{scan_res['lamp_zh']}** — {scan_res['lamp_reason']}")

        # 指标卡片
        m1, m2, m3 = st.columns(3)
        m1.metric("话术总行数", f"{scan_res['total_lines']} 行")
        m2.metric("检出违规行数", f"{scan_res['violation_count']} 行", delta="需修改后开播" if scan_res['violation_count'] > 0 else "合规准予上播", delta_color="inverse")
        m3.metric("熔断灯状态", scan_res["lamp_zh"])

        st.markdown("---")

        # 3. 逐行展示与改写
        st.subheader("🎙️ 话术逐行合规扫描与改写对比")
        for idx, l in enumerate(scan_res["scanned_lines"], 1):
            if l["is_violation"]:
                # 尝试调用 LLM 改写桩（Qwen3.8-Flash）
                cache_key_m3 = f"llm_m3_{cur_script['id']}_{idx}"
                if cache_key_m3 not in st.session_state:
                    try:
                        st.session_state[cache_key_m3] = llm_rewrite_stub(l["text"], l["main_type"])
                    except Exception:
                        st.session_state[cache_key_m3] = None
                llm_res_m3 = st.session_state.get(cache_key_m3)

                llm_rw_text = None
                if llm_res_m3 and isinstance(llm_res_m3, dict) and "rewrite" in llm_res_m3:
                    cand = llm_res_m3["rewrite"]
                    if "全网最低" in l["text"]:
                        if "平台补贴价" in cand:
                            llm_rw_text = cand
                    else:
                        llm_rw_text = cand

                if llm_rw_text:
                    rewrite_box_html = (
                        f'<div style="font-size: 14px; color: #1b5e20; background-color: #e8f5e9; padding: 8px 12px; border-radius: 4px; margin-bottom: 6px;">'
                        f'<div style="margin-bottom: 4px;"><strong>🤖 LLM 改写（Qwen3.8-Flash）：</strong><span>{llm_rw_text}</span></div>'
                        f'<div style="color: #2e7d32;"><strong>模板改写：</strong><span>{l["rewritten"]}</span></div>'
                        f'</div>'
                    )
                else:
                    rewrite_box_html = (
                        f'<div style="font-size: 14px; color: #1b5e20; background-color: #e8f5e9; padding: 8px 12px; border-radius: 4px; margin-bottom: 6px;">'
                        f'<div><strong>模板改写：</strong><span>{l["rewritten"]}</span></div>'
                        f'</div>'
                    )

                card_html = (
                    f'<div style="border-left: 5px solid #d32f2f; background-color: #ffebee; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px;">'
                    f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">'
                    f'<span style="font-weight: bold; font-size: 15px; color: #b71c1c;">第 {idx} 行话术 ｜ 🚨 违规拦截 [{l["main_type_zh"]} · {l["severity"]}]</span>'
                    f'<span style="background-color: #d32f2f; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">命中词: {", ".join(l["hit_words"])}</span>'
                    f'</div>'
                    f'<div style="font-size: 15px; color: #212121; margin-bottom: 6px;"><strong>原句：</strong><span style="text-decoration: line-through; color: #c62828;">{l["text"]}</span></div>'
                    f'{rewrite_box_html}'
                    f'<div style="font-size: 12px; color: #616161;"><strong>命中法规/规则：</strong>[{l["rule"]["id"]}] 《{l["rule"]["source"]}》— {l["rule"]["text"]}</div>'
                    f'</div>'
                )
                st.markdown(card_html, unsafe_allow_html=True)
            else:
                card_html = (
                    f'<div style="border-left: 5px solid #2e7d32; background-color: #f1f8e9; padding: 10px 16px; border-radius: 6px; margin-bottom: 8px;">'
                    f'<div style="display: flex; justify-content: space-between; align-items: center;">'
                    f'<span style="font-weight: bold; font-size: 14px; color: #1b5e20;">第 {idx} 行话术 ｜ ✅ 合规通过</span>'
                    f'<span style="font-size: 12px; color: #558b2f;">符合《{l["rule"]["source"]}》</span>'
                    f'</div>'
                    f'<div style="font-size: 14px; color: #33691e; margin-top: 4px;"><strong>话术：</strong>{l["text"]}</div>'
                    f'</div>'
                )
                st.markdown(card_html, unsafe_allow_html=True)

        # 4. 评测报告折叠栏
        st.markdown("---")
        with st.expander("评测报告（模拟）"):
            report_m3_file = os.path.join(os.path.dirname(__file__), "m3", "eval_report.md")
            if os.path.exists(report_m3_file):
                with open(report_m3_file, "r", encoding="utf-8") as f:
                    st.markdown(f.read(), unsafe_allow_html=True)
            else:
                st.info("还没跑评测，先在终端跑 python m3/run_eval.py")


    # =========================================================================
    # 页签 5：M4 评测报告（D5 新增）
    with m3_sub_real:
        render_m3_real()

# =========================================================================
with tab_m4:
    # 顶部一行红字横幅
    st.markdown(
        '<div style="color: #d32f2f; font-weight: bold; font-size: 16px; padding: 8px 12px; background-color: #ffebee; border-left: 4px solid #d32f2f; margin-bottom: 20px;">'
        '模拟评测 / 假设，gold 由规则定义，不是真实判责结果。'
        '</div>',
        unsafe_allow_html=True
    )
    st.title("M4 EvalForge — 200 题三模型对比评测")

    results_file = os.path.join(os.path.dirname(__file__), "m4", "results.json")
    if os.path.exists(results_file):
        with open(results_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        models_data = data.get("models", {})

        # 1. 三模型准确率对比柱状图
        st.subheader("📊 三模型总体准确率对比")
        chart_data = {
            "模型": [models_data[k]["name"] for k in ["A", "B", "C"] if k in models_data],
            "总体准确率 (%)": [models_data[k]["accuracy"] for k in ["A", "B", "C"] if k in models_data],
        }
        chart_df = pd.DataFrame(chart_data).set_index("模型")
        st.bar_chart(chart_df)

        st.markdown("---")

        # 2. 三维表
        st.subheader("📋 三模型三维评测对比表（准确率 × 期望成本 × 耗时）")
        dim3_rows = []
        for k in ["A", "B", "C"]:
            if k in models_data:
                m = models_data[k]
                dim3_rows.append({
                    "模型方案": m["name"],
                    "总体准确率": f"{m['accuracy']}%",
                    "平均单笔期望成本": f"¥{m['avg_cost']:.1f}",
                    "平均单题耗时": f"{m['avg_ms']:.3f} ms",
                })
        st.dataframe(dim3_rows, use_container_width=True, hide_index=True)

        st.markdown("---")

        # 3. 分 subset 准确率表
        st.subheader("🎯 细分子集准确率表现（清晰题 / 边界题 / 对抗题）")
        sub_rows = []
        for k in ["A", "B", "C"]:
            if k in models_data:
                m = models_data[k]
                sub_rows.append({
                    "模型方案": m["name"],
                    "清晰题 (100题)": f"{m['accuracy_clear']}%",
                    "边界题 (40题)": f"{m['accuracy_boundary']}%",
                    "对抗题 (60题)": f"{m['accuracy_adversarial']}%",
                    "总体准确率 (200题)": f"{m['accuracy']}%",
                })
        st.dataframe(sub_rows, use_container_width=True, hide_index=True)
        st.caption("*注：100% 为规则引擎自洽性验证（Sanity Check），LLM 端到端实测准确率待双盲标注后更新。")

    else:
        st.warning("暂无评测数据，请先在终端运行 `python m4/evalforge.py` 生成评测报告。")

    # 4. 评测报告折叠栏
    st.markdown("---")
    with st.expander("评测报告（模拟）"):
        report_200_file = os.path.join(os.path.dirname(__file__), "m4", "eval_report_200.md")
        if os.path.exists(report_200_file):
            with open(report_200_file, "r", encoding="utf-8") as f:
                st.markdown(f.read(), unsafe_allow_html=True)
        else:
            st.info("还没跑评测，先在终端跑 python m4/evalforge.py")



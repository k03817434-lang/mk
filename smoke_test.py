# -*- coding: utf-8 -*-
"""smoke_test.py — MarginKeeper (MK) 全站一键冒烟测试
锁死断言，严格校验 M0 / M1 / M2 / M3 / M4 五大模块及工程合规性。
逐项打印 PASS / FAIL，最后汇总退出码（全部 PASS 退出 0，否则 1）。
"""
import json
import os
import re
import sys

# 避免 Windows 终端编码问题
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def run_smoke_test():
    tests = []
    
    # ----------------------------------------------------
    # 1. M0：MK-001 胜率 == 0.78
    # ----------------------------------------------------
    try:
        from mock_data import MOCK_CASES
        from core.bayes import calc_win_prob
        c1 = next(c for c in MOCK_CASES if c["case_id"] == "MK-001")
        wp = calc_win_prob(c1)
        passed = (round(wp, 2) == 0.78)
        msg = f"MK-001 胜率实测 = {wp:.2f} (预期 0.78)"
        tests.append(("1. M0 售后决策胜率", passed, msg))
    except Exception as e:
        tests.append(("1. M0 售后决策胜率", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 2. M2：S3 茶小憩穿底组合修复前 == 37，修复后 == 2
    # ----------------------------------------------------
    try:
        from m2.mock_menus import MOCK_STORES
        from m2.solver import apply_fix
        s3 = next(s for s in MOCK_STORES if s["store_id"] == "S3")
        res_s3 = apply_fix(s3)
        before_cnt = res_s3["before_count"]
        after_cnt = res_s3["after_count"]
        passed = (before_cnt == 37 and after_cnt == 2)
        msg = f"S3 修复前穿底 = {before_cnt} (预期 37), 修复后 = {after_cnt} (预期 2)"
        tests.append(("2. M2 满减穿底与修复", passed, msg))
    except Exception as e:
        tests.append(("2. M2 满减穿底与修复", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 3. M1：P01 判 拦截，P07 判 通过，P11 判 人工核验
    # ----------------------------------------------------
    try:
        from m1.mock_products import PRODUCTS
        from m1.specdiff import diff_product
        p01 = next(p for p in PRODUCTS if p["id"] == "P01")
        p07 = next(p for p in PRODUCTS if p["id"] == "P07")
        p11 = next(p for p in PRODUCTS if p["id"] == "P11")
        
        v01 = diff_product(p01)["verdict_zh"]
        v07 = diff_product(p07)["verdict_zh"]
        v11 = diff_product(p11)["verdict_zh"]
        
        passed = (v01 == "拦截" and v07 == "通过" and v11 == "人工核验")
        msg = f"P01={v01}(预期拦截), P07={v07}(预期通过), P11={v11}(预期人工核验)"
        tests.append(("3. M1 上架参数交叉质检", passed, msg))
    except Exception as e:
        tests.append(("3. M1 上架参数交叉质检", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 4. M3：S01 标出违规 == 3 行，S06 标出违规 == 1 行
    # ----------------------------------------------------
    try:
        from m3.mock_scripts import SCRIPTS
        from m3.scanner import scan_script
        s01 = next(s for s in SCRIPTS if s["id"] == "S01")
        s06 = next(s for s in SCRIPTS if s["id"] == "S06")
        
        cnt_s01 = scan_script(s01)["violation_count"]
        cnt_s06 = scan_script(s06)["violation_count"]
        
        passed = (cnt_s01 == 3 and cnt_s06 == 1)
        msg = f"S01 违规 = {cnt_s01} 行 (预期 3), S06 违规 = {cnt_s06} 行 (预期 1)"
        tests.append(("4. M3 直播话术违规扫描", passed, msg))
    except Exception as e:
        tests.append(("4. M3 直播话术违规扫描", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 5. M4：读 m4/results.json，A 总体准确率 == 50.0 (0.50)，B 总体准确率 == 100.0 (1.00)，C 平均期望成本 == 10.0
    # ----------------------------------------------------
    try:
        results_file = os.path.join(PROJECT_ROOT, "m4", "results.json")
        if not os.path.exists(results_file):
            from m4.evalforge import run_evalforge
            run_evalforge()
            
        with open(results_file, "r", encoding="utf-8") as f:
            rdata = json.load(f)
            
        acc_a = rdata["models"]["A"]["accuracy"]
        acc_b = rdata["models"]["B"]["accuracy"]
        cost_c = rdata["models"]["C"]["avg_cost"]
        
        passed_a = (acc_a == 50.0 or acc_a == 0.5)
        passed_b = (acc_b == 100.0 or acc_b == 1.0)
        passed_c = (cost_c == 10.0)
        
        passed = (passed_a and passed_b and passed_c)
        msg = f"A准度={acc_a} (预期50.0/0.5), B准度={acc_b} (预期100.0/1.0), C均成本=¥{cost_c} (预期10.0)"
        tests.append(("5. M4 200题三模型对比评测", passed, msg))
    except Exception as e:
        tests.append(("5. M4 200题三模型对比评测", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 6. app.py 里五个页签标签都存在且顺序正确
    # ----------------------------------------------------
    try:
        app_file = os.path.join(PROJECT_ROOT, "app.py")
        with open(app_file, "r", encoding="utf-8") as f:
            app_code = f.read()
            
        expected_tabs = ["M0 售后决策", "M1 上架质检", "M2 活动推演", "M3 直播合规", "M4 评测报告"]
        all_present = all(t in app_code for t in expected_tabs)
        
        # 验证 tabs 列表定义中的顺序
        tab_list_match = re.search(r'st\.tabs\(\[(.*?)\]\)', app_code)
        order_ok = False
        if tab_list_match:
            tabs_str = tab_list_match.group(1)
            pos = [tabs_str.find(t) for t in expected_tabs]
            if all(p != -1 for p in pos) and pos == sorted(pos):
                order_ok = True
                
        passed = (all_present and order_ok)
        msg = f"全页签存在: {all_present}, 排序严格符合 M0->M1->M2->M3->M4: {order_ok}"
        tests.append(("6. app.py 五大页签存在与排序", passed, msg))
    except Exception as e:
        tests.append(("6. app.py 五大页签存在与排序", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 7. 全站机密信息扫描（API key / Token / 密码等）
    # ----------------------------------------------------
    try:
        forbidden_str = "".join(["1234567890", "WK", "dsb"])
        secret_patterns = [
            re.compile(r"sk-[a-zA-Z0-9]{20,}"),
            re.compile(r"(?i)api[_-]?key\s*=\s*['\"][a-zA-Z0-9_\-]{16,}['\"]"),
            re.compile(r"(?i)password\s*=\s*['\"][^'\"]{6,}['\"]"),
        ]
        
        found_secrets = []
        for root, dirs, files in os.walk(PROJECT_ROOT):
            # 过滤排除目录
            if any(p in root for p in ["__pycache__", ".git", ".venv", "venv", ".pytest_cache"]):
                continue
            for fname in files:
                if fname == "smoke_test.py":
                    continue
                if fname.endswith((".py", ".md", ".json", ".txt", ".yaml", ".yml")):
                    fpath = os.path.join(root, fname)
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if forbidden_str in content:
                            found_secrets.append(f"{fname}: 命中ECS密码泄漏")
                        for sp in secret_patterns:
                            matches = sp.findall(content)
                            if matches:
                                found_secrets.append(f"{fname}: 命中疑似机密模式")

        passed = (len(found_secrets) == 0)
        msg = "全站代码与文档无硬编码密钥或密码泄漏" if passed else f"发现敏感信息泄漏: {found_secrets}"
        tests.append(("7. 全站安全合规(无密钥机密泄漏)", passed, msg))
    except Exception as e:
        tests.append(("7. 全站安全合规(无密钥机密泄漏)", False, f"异常: {e}"))

    # ----------------------------------------------------
    # 输出结果汇总
    # ----------------------------------------------------
    print("=" * 72)
    print("MarginKeeper (MK) — 全站冒烟集成测试报告 (Smoke Test)")
    print("=" * 72)
    
    all_passed = True
    for name, ok, detail in tests:
        status_str = "PASS" if ok else "FAIL"
        if not ok:
            all_passed = False
        print(f"[{status_str:4s}] {name}")
        print(f"       -> {detail}")

    print("=" * 72)
    pass_cnt = sum(1 for _, ok, _ in tests if ok)
    fail_cnt = sum(1 for _, ok, _ in tests if not ok)
    print(f"冒烟测试汇总: 共 {len(tests)} 项 | 通过: {pass_cnt} 项 | 失败: {fail_cnt} 项")
    
    if all_passed:
        print(">>> 结论: 全部断言 100% 通过 (ALL PASSED)，准予发布上云与交付！")
        print("=" * 72)
        return 0
    else:
        print(">>> 结论: 存在未通过断言 (FAILED)，请修复后再行部署！")
        print("=" * 72)
        return 1

if __name__ == "__main__":
    sys.exit(run_smoke_test())

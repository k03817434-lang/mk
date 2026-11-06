# -*- coding: utf-8 -*-
"""core/real_data.py — M0–M3 真实数据加载模块
读取 data-real/ 目录下的定档真实案例与规则数据 JSON。
"""
import os
import json

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_REAL_DIR = os.path.join(PROJECT_ROOT, "data-real")

def load_real_json(filename):
    path = os.path.join(DATA_REAL_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_m0_real_data():
    return load_real_json("m0_priors_draft.json")

def get_m1_real_data():
    return load_real_json("m1_rules_real_cases.json")

def get_m2_real_data():
    return load_real_json("m2_ecommerce_stores.json")

def get_m3_real_data():
    return load_real_json("m3_rules_real_cases.json")

# core/bayes.py
from mock_data import CATEGORY_PRIORS, EVIDENCE_RULES, MOCK_CASES

def get_case_evidence_details(case):
    category = case.get("category", "")
    prior = CATEGORY_PRIORS.get(category, 0.52)
    rule_map = {r["id"]: r for r in EVIDENCE_RULES}
    applied_rules = []
    for eid in case.get("evidence_ids", []):
        if eid in rule_map:
            applied_rules.append(rule_map[eid])
    return prior, applied_rules

def calc_win_prob(case):
    prior, applied_rules = get_case_evidence_details(case)
    total_delta = sum(r["delta"] for r in applied_rules)
    raw_prob = prior + total_delta
    # 结果裁剪到 0.05–0.95 之间
    clamped_prob = max(0.05, min(0.95, round(raw_prob, 4)))
    return clamped_prob

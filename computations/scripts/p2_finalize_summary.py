"""Fold the recheck results into C10_STRESS_SUMMARY.json (final accounting)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, dump

S = json.load(open(os.path.join(RESULTS, "C10_STRESS_SUMMARY.json")))
R = json.load(open(os.path.join(RESULTS, "P2_HP_RECHECK.json")))
W = json.load(open(os.path.join(RESULTS, "P2_C5_LEMMA2_WITNESSES.json")))
CT = json.load(open(os.path.join(RESULTS, "P2_HP_CONTROLS.json")))
h = S["hp_stage"]
h["control_sample_v2"] = CT["control_sample_v2"]
h["extreme_scaling_audit_v2"] = CT["extreme_scaling_audit_v2"]
h["note_v1_artifacts"] = ("v1 control_sample used a local mp search from D=I (C5 non-P0 controls need extreme D) and "
                          "v1 extreme_scaling_audit used 60 digits for ratios up to 1e60; both superseded by *_v2.")
S.pop("GENUINE_COUNTEREXAMPLES", None)
S.pop("counterexample_candidates", None)
flagged_bad = h["n_hp_cases"] - h["consistent_at_40"]
S["GENUINE_C10_COUNTEREXAMPLES_before_recheck"] = S.pop("GENUINE_C10_COUNTEREXAMPLES", None)
S["recheck"] = {
    "strictP_controls_reported_inconsistent": R["n_strictP"],
    "cause": "unbounded mp pattern search ran away to |w| in [%.1f, %.1f] (diagonal ratios e^|w|) "
             "where 40 digits cannot resolve the smallest eigenvalue" % (R["min_final_|w|_strictP"], R["max_final_|w|"]),
    "negative_at_adequate_precision": len(R["strictP_negative_at_adequate_precision"]),
    "negative_bounded_search_|w|<=16_dps60": len(R["strictP_negative_bounded_search"]),
    "C5_nonP0_controls": {"n": W["n_C5_controls"], "analytic_Lemma2_witness_negative_at_150_digits": W["witness_negative"]},
}
S["GENUINE_C10_COUNTEREXAMPLES"] = flagged_bad + len(R["strictP_negative_at_adequate_precision"]) \
    + len(h["extreme_scaling_audit_v2"]["strictP_negative"])
S["VERDICT"] = "COMPUTE_PASS for C-10: 0 mismatches survive high precision" if S["GENUINE_C10_COUNTEREXAMPLES"] == 0 \
    else "COMPUTE_FAIL"
dump("C10_STRESS_SUMMARY.json", S)
print(S["GENUINE_C10_COUNTEREXAMPLES"], S["VERDICT"])

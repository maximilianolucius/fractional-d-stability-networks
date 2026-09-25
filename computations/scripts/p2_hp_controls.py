"""P2 HP stage, part 2: corrected control sample + extreme-scaling audit.

Why this exists: the first HP pass (p2_hp_verify.py) re-ran control cases
with a *local* mp search started at D = I.  For the C5 controls (-A not P0,
outside the C-10 hypothesis) the instability lives at extreme D, so a local
search from D = I cannot see it -> 95 spurious "inconsistent" controls.  Its
extreme-scaling audit used diagonal ratios up to 1e60 at only 60 digits,
below the precision needed for eigenvalues of relative size 1e-60.

Here: every control starts from the float global direct optimizer
(min_margin, [-16,16]^2) AND from D = I; mp margins at 50 digits.  The
extreme audit uses ratios 1e30 and 1e60 at 250 digits and stores every case.
Results are merged into C10_STRESS_SUMMARY.json (hp_stage.control_sample_v2,
hp_stage.extreme_scaling_audit_v2) and written to P2_HP_CONTROLS.json.
"""
from __future__ import annotations

import json
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, Timer, dump, log, pool  # noqa: E402

import p2_hp_verify as H  # noqa: E402
import p2_stress as S  # noqa: E402
from fdsn.direct_margin import min_margin, mp_margin  # noqa: E402


def controls():
    rng = np.random.default_rng(H.SEED)
    data = H.load()
    for mech, d in data.items():                     # consume rng exactly as p2_hp_verify did
        flag = d["mismatch"] | d["near_zero"] | d["theorem_near"]
        rng.choice(np.nonzero(~flag)[0], size=min(150, (~flag).sum()), replace=False)
    out = []
    for mech in data:
        for j in (0, 7):
            seed = S.MASTER_SEED * 1000 + S.hash_mech(mech) * 100000 + j
            A, al, _ = S.GENERATORS[mech](np.random.default_rng(seed), S.JOB)
            for k in rng.choice(A.shape[0], size=75, replace=False):
                gi = j * S.JOB + int(k)
                out.append({"mech": mech, "i": gi, "A": A[k], "alpha": float(al[k]),
                            "pred": bool(data[mech]["pred"][gi])})
    return out


def verify_control(c):
    r = min_margin(c["A"][None], c["alpha"], half_width=16, step=0.5, n_starts=3)
    res = {}
    for name, w0 in (("float_global_start", r["w"][0]), ("identity_start", [0.0, 0.0])):
        c2 = dict(c, w=w0)
        o = H.verify(c2)
        fin = o.get("dps110", o["dps40"])
        res[name] = {"consistent": bool(fin["consistent"]), "margin": float(fin["margin_min"]),
                     "pred": bool(fin["pred"])}
    return {"mech": c["mech"], "i": c["i"], "alpha": c["alpha"], "float_margin": float(r["margin"][0]),
            **res}


def extreme(c):
    with mp.workdps(260):
        A = mp.matrix([[mp.mpf(float(v)) for v in row] for row in c["A"]])
        p, beta, kappa, strictP = H.mp_inv(A)
        As = mp.matrix([[A[i, j] / p[i] for j in range(3)] for i in range(3)])
        worst, wd = mp.inf, None
        for E in (mp.mpf(10) ** 30, mp.mpf(10) ** 60):
            for d in [(E, 1, 1), (1, E, 1), (1, 1, E), (E, E, 1), (E, 1, E), (1, E, E),
                      (E * E, E, 1), (1, E, E * E), (E, E * E, 1), (E * E, 1, E), (1, E * E, E), (E, 1, E * E)]:
                m = mp_margin(As, [mp.mpf(v) for v in d], c["alpha"], 250)[0]
                if m < worst:
                    worst, wd = m, d
        return {"mech": c["mech"], "i": c["i"], "alpha": c["alpha"], "strictP": bool(strictP),
                "min_margin": float(worst), "worst_d": [mp.nstr(v, 5) for v in wd]}


def main():
    T = Timer()
    cs = controls()
    log("controls", len(cs))
    with pool() as P:
        cres = P.map(verify_control, cs, chunksize=4)
        ex = P.map(extreme, [c for c in cs if c["alpha"] < 1], chunksize=4)
    by = lambda k: sum(r[k]["consistent"] for r in cres)
    strictp_ex = [e for e in ex if e["strictP"]]
    out = {
        "control_sample_v2": {
            "n": len(cres),
            "consistent_float_global_start": by("float_global_start"),
            "consistent_identity_start": by("identity_start"),
            "inconsistent_float_global_start": [r for r in cres if not r["float_global_start"]["consistent"]],
            "inconsistent_identity_start_by_mech": {m: sum((not r["identity_start"]["consistent"]) and r["mech"] == m
                                                           for r in cres) for m in sorted({r["mech"] for r in cres})},
        },
        "extreme_scaling_audit_v2": {
            "dps": 250, "ratios": "1e30, 1e60 (12 corner patterns each)",
            "n": len(ex), "n_strictP": len(strictp_ex),
            "strictP_negative": [e for e in strictp_ex if e["min_margin"] < 0],
            "strictP_min_margin": min(e["min_margin"] for e in strictp_ex),
            "nonP_cases": len(ex) - len(strictp_ex),
        },
        "seconds": T(),
    }
    dump("P2_HP_CONTROLS.json", out)
    sp = os.path.join(RESULTS, "C10_STRESS_SUMMARY.json")
    summ = json.load(open(sp))
    summ["hp_stage"]["control_sample_v2"] = {k: v for k, v in out["control_sample_v2"].items()}
    summ["hp_stage"]["extreme_scaling_audit_v2"] = out["extreme_scaling_audit_v2"]
    summ["hp_stage"]["note_v1_artifacts"] = (
        "v1 control_sample used a local mp search from D=I (C5 non-P0 controls need extreme D) and "
        "v1 extreme_scaling_audit used 60 digits for ratios up to 1e60; both superseded by *_v2.")
    # v1 counted the spurious control failures as "GENUINE_COUNTEREXAMPLES"; recompute:
    flagged_bad = summ["hp_stage"]["n_hp_cases"] - summ["hp_stage"]["consistent_at_40"]
    ctrl_bad = [r for r in cres if not r["float_global_start"]["consistent"]]
    ctrl_bad_strictP = [r for r in ctrl_bad if not r["mech"].startswith("C5")]
    summ["GENUINE_COUNTEREXAMPLES_v1_field_superseded"] = summ.pop("GENUINE_COUNTEREXAMPLES", None)
    summ.pop("counterexample_candidates", None)
    summ["GENUINE_C10_COUNTEREXAMPLES"] = flagged_bad + len(ctrl_bad_strictP) + len(out["extreme_scaling_audit_v2"]["strictP_negative"])
    dump("C10_STRESS_SUMMARY.json", summ)


if __name__ == "__main__":
    main()

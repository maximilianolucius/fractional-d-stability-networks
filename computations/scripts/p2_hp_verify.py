"""P2 high-precision stage + aggregation -> C10_STRESS_SUMMARY.json, C10_WORST_CASES.csv.

Every flagged float case (float mismatch, near-zero direct margin, or theorem
near-boundary |kappa/T-1| < 1e-10) plus a random control sample is re-run with
mpmath:
  * matrix entries are the float64 entries taken as exact binary rationals;
  * theorem side: invariants and T_alpha(beta) at 60 digits;
  * direct side: mpmath.eig margins (40 digits), local pattern search started
    from the float direct optimizer (O1) and, separately, from the theorem's
    x* (labelled `theorem_start`, used only as an extra start);
  * any case whose HP verdict disagrees with C-10 is re-verified at 110 digits.
Extreme-scaling audit: for random strict-P cases, mp margins at diagonal
ratios 10^{+-30} (the region excluded by the float reliability filter).
"""
from __future__ import annotations

import csv
import glob
import json
import os
import sys
import time

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from _common import RAW, RESULTS, Timer, dump, log, peak_rss_mb, pool  # noqa: E402

from fdsn.c10_threshold import threshold_mp  # noqa: E402
from fdsn.direct_margin import mp_margin  # noqa: E402

SEED = 777
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def mp_inv(A):
    a = [[A[i, j] for j in range(3)] for i in range(3)]
    p = [-a[i][i] for i in range(3)]
    m12 = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    m13 = a[0][0] * a[2][2] - a[0][2] * a[2][0]
    m23 = a[1][1] * a[2][2] - a[1][2] * a[2][1]
    det = mp.det(A)
    beta = [m12 / (p[0] * p[1]), m13 / (p[0] * p[2]), m23 / (p[1] * p[2])]
    return p, beta, -det / (p[0] * p[1] * p[2]), all(v > 0 for v in p + [m12, m13, m23, -det])


def search(As, alpha, w0, dps, min_step, max_evals=600):
    """mp pattern search of the margin over w (As prescaled, d = exp([w,0]))."""
    w = [mp.mpf(w0[0]), mp.mpf(w0[1])]
    f = lambda v: mp_margin(As, [mp.exp(v[0]), mp.exp(v[1]), mp.mpf(1)], alpha, dps)[0]
    best = f(w)
    step = mp.mpf("0.01")
    ev = 1
    while step > min_step and ev < max_evals:
        improved = False
        for dx, dy in DIRS:
            t = [w[0] + step * dx, w[1] + step * dy]
            v = f(t)
            ev += 1
            if v < best:
                best, w, improved = v, t, True
                break
        step = step * 2 if improved else step / 2
    return best, w, ev


def verify(case):
    A_f, alpha_f, w_f, pred_f = case["A"], case["alpha"], case["w"], case["pred"]
    out = {"alpha": alpha_f, "pred_float": pred_f}
    t0 = time.time()
    for dps in (40, 110):
        with mp.workdps(dps + 20):
            A = mp.matrix([[mp.mpf(float(v)) for v in r] for r in A_f])
            alpha = mp.mpf(float(alpha_f))
            p, beta, kappa, strictP = mp_inv(A)
            As = mp.matrix([[A[i, j] / p[i] for j in range(3)] for i in range(3)])
            if not strictP:
                pred, T, x_th = False, None, None
            elif alpha <= mp.mpf(2) / 3:
                pred, T, x_th = True, None, None
            elif alpha >= 1:
                T = (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2
                pred, x_th = kappa < T, None
            else:
                r = threshold_mp(beta, alpha, dps=dps + 10)
                T, x_th = r["T"], r["x"]
                pred = kappa < T
            starts = [("float_O1", [float(w_f[0]), float(w_f[1])])]
            if x_th is not None:
                starts.append(("theorem_start", [mp.log(x_th[0] / x_th[2]), mp.log(x_th[1] / x_th[2])]))
            res = {}
            min_step = mp.mpf(10) ** -(dps // 2 - 2)
            for name, w0 in starts:
                v0 = mp_margin(As, [mp.exp(mp.mpf(w0[0])), mp.exp(mp.mpf(w0[1])), mp.mpf(1)], alpha, dps)[0]
                if (not pred) and v0 < 0:
                    res[name] = (v0, 1)                  # explicit witness, no search needed
                else:
                    b, _, ev = search(As, alpha, w0, dps, min_step)
                    res[name] = (b, ev)
            m_direct = min(v for v, _ in res.values())
            m_indep = res["float_O1"][0]
            # HP decision: witness (<0) is conclusive; >0 is "local min positive"
            consistent = (m_direct > 0) == bool(pred)
            consistent_indep = (m_indep > 0) == bool(pred)
            out[f"dps{dps}"] = {
                "pred": bool(pred), "gap": (kappa / T - 1) if T is not None else None,
                "kappa": kappa, "T": T, "margin_min": m_direct, "margin_indep_start": m_indep,
                "evals": sum(e for _, e in res.values()),
                "consistent": consistent, "consistent_independent_start": consistent_indep,
            }
        if dps == 40 and out["dps40"]["consistent"] and out["dps40"]["consistent_independent_start"]:
            break
    out["seconds"] = time.time() - t0
    return out


def extreme_audit(case):
    """mp margins at 10^{+-30} diagonal ratios for one strict-P matrix."""
    A_f, alpha_f = case["A"], case["alpha"]
    with mp.workdps(80):
        A = mp.matrix([[mp.mpf(float(v)) for v in r] for r in A_f])
        alpha = mp.mpf(float(alpha_f))
        p, beta, kappa, strictP = mp_inv(A)
        As = mp.matrix([[A[i, j] / p[i] for j in range(3)] for i in range(3)])
        worst = mp.inf
        E = mp.mpf(10) ** 30
        for d in [(E, 1, 1), (1, E, 1), (1, 1, E), (E, E, 1), (E, 1, E), (1, E, E),
                  (E * E, E, 1), (1, E, E * E), (E, E * E, 1), (E * E, 1, E), (1, E * E, E), (E, 1, E * E)]:
            m = mp_margin(As, [mp.mpf(v) for v in d], alpha, 60)[0]
            worst = min(worst, m)
        return float(worst), bool(strictP)


def load():
    data = {}
    for f in sorted(glob.glob(os.path.join(RAW, "p2_*.npz"))):
        mech = os.path.basename(f)[3:-4]
        data[mech] = dict(np.load(f, allow_pickle=False))
    return data


def main():
    T = Timer()
    rng = np.random.default_rng(SEED)
    data = load()
    summary = {"mechanisms": {}, "labels": "FLOAT stage + HP stage (mpmath 40 digits, 110 digits for any disagreement)"}
    cases, audit = [], []
    tot = 0
    for mech, d in data.items():
        n = d["alpha"].size
        tot += n if not mech.startswith("C") else 0
        flag = d["mismatch"] | d["near_zero"] | d["theorem_near"]
        fl_idx = d["flag_global"]
        assert fl_idx.size == flag.sum(), (mech, fl_idx.size, flag.sum())
        for k, gi in enumerate(fl_idx):
            cases.append({"mech": mech, "i": int(gi), "A": d["A_flag"][k], "alpha": float(d["alpha"][gi]),
                          "w": d["w_flag"][k], "pred": bool(d["pred"][gi]), "kind": "flagged",
                          "float_mismatch": bool(d["mismatch"][gi])})
        a = d["alpha"]
        sp = d["strictP"]
        s = summary["mechanisms"][mech] = {
            "cases": int(n), "strictP": int(sp.sum()),
            "theorem_pred_stable": int(d["pred"].sum()),
            "float_mismatch": int(d["mismatch"].sum()), "float_near_zero": int(d["near_zero"].sum()),
            "theorem_near_boundary_1e-10": int(d["theorem_near"].sum()),
            "optimizer_disagreement_gt_1e-9": int((d["opt_disagree"] > 1e-9).sum()),
            "O2_runs": int(np.isfinite(d["margin_O2"]).sum()), "O3_runs": int(np.isfinite(d["margin_O3"]).sum()),
            "alpha_counts": {f"{v:.6g}": int(c) for v, c in zip(*np.unique(np.round(a, 12), return_counts=True))}
            if np.unique(np.round(a, 12)).size < 30 else "continuous",
            "margin_quantiles_pred_stable": np.quantile(d["margin"][d["pred"]], [0, 0.001, 0.5, 1]).tolist() if d["pred"].any() else None,
            "margin_quantiles_pred_unstable": np.quantile(d["margin"][~d["pred"]], [0, 0.5, 0.999, 1]).tolist() if (~d["pred"]).any() else None,
            "min_abs_gap": float(np.nanmin(np.abs(d["gap"]))) if np.isfinite(d["gap"]).any() else None,
        }
        # theorem x* vs direct worst D orbit coordinates near the fractional boundary
        near = np.isfinite(d["gap"]) & (np.abs(d["gap"]) < 1e-4) & (a > 2 / 3) & (a < 1)
        if near.any():
            dist = np.max(np.abs(d["x_theorem"][near] - d["x_direct"][near]), axis=1)
            s["x_theorem_vs_direct_near_boundary"] = {
                "n": int(near.sum()), "median_maxabs": float(np.median(dist)),
                "p99_maxabs": float(np.quantile(dist, 0.99)), "max_maxabs": float(dist.max())}
    # random control sample: replay two generation jobs per mechanism (generation is
    # deterministic in the recorded seed), take 150 random cases each
    import p2_stress as S
    controls = []
    for mech in data:
        for j in (0, 7):
            seed = S.MASTER_SEED * 1000 + S.hash_mech(mech) * 100000 + j
            A, al, _ = S.GENERATORS[mech](np.random.default_rng(seed), S.JOB)
            for k in rng.choice(A.shape[0], size=75, replace=False):
                gi = j * S.JOB + int(k)
                controls.append({"mech": mech, "i": gi, "A": A[k], "alpha": float(al[k]),
                                 "w": [0.0, 0.0], "pred": bool(data[mech]["pred"][gi]), "kind": "control",
                                 "float_mismatch": bool(data[mech]["mismatch"][gi])})
    log("HP cases", len(cases))
    with pool() as P:
        res = P.map(verify, cases, chunksize=4)
        cres = P.map(verify, controls, chunksize=4)
        ex_cases = controls + [c for c in cases if c["alpha"] < 1][:: max(1, len(cases) // 2000)]
        ex = P.map(extreme_audit, ex_cases, chunksize=8)
    rows = []
    genuine = []
    for c, r in zip(cases + controls, res + cres):
        final = r.get("dps110", r["dps40"])
        rows.append((c, r, final))
        if not (final["consistent"]):
            genuine.append((c, r))
    hp = {
        "n_hp_cases": len(cases),
        "float_mismatches_rechecked": sum(c["float_mismatch"] for c in cases),
        "consistent_at_40": sum(r["dps40"]["consistent"] for r in res),
        "consistent_independent_start_at_40": sum(r["dps40"]["consistent_independent_start"] for r in res),
        "escalated_to_110": sum("dps110" in r for r in res),
        "inconsistent_after_110": len(genuine),
        "hp_seconds_total": sum(r["seconds"] for r in res),
        "control_sample": {"n": len(controls),
                           "consistent_final": sum(r.get("dps110", r["dps40"])["consistent"] for r in cres),
                           "note": "random non-flagged cases (replayed generation) re-run at 40 digits"},
        "extreme_scaling_audit": {"n": len(ex), "min_margin": min(e[0] for e in ex) if ex else None,
                                   "negative": sum(e[0] < 0 and e[1] for e in ex)},
    }
    summary["hp_stage"] = hp
    summary["total_C10_cases"] = int(tot)
    summary["total_control_cases"] = int(sum(v["cases"] for k, v in summary["mechanisms"].items() if k.startswith("C")))
    summary["total_float_mismatch_C10"] = int(sum(v["float_mismatch"] for k, v in summary["mechanisms"].items() if not k.startswith("C")))
    summary["GENUINE_COUNTEREXAMPLES"] = len(genuine)
    # worst cases CSV: every HP case sorted by |final margin| (closest to boundary)
    rows.sort(key=lambda t: abs(float(t[2]["margin_min"])))
    path = os.path.join(RESULTS, "C10_WORST_CASES.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["mech", "index", "alpha", "a11", "a12", "a13", "a21", "a22", "a23", "a31", "a32", "a33",
                    "float_mismatch", "hp_dps", "theorem_pred_member", "gap_kappa_over_T_minus_1",
                    "hp_min_margin", "hp_margin_independent_start", "consistent"])
        for c, r, fin in rows[:5000]:
            dps = 110 if "dps110" in r else 40
            w.writerow([c["mech"], c["i"], repr(c["alpha"]), *[repr(float(v)) for v in np.ravel(c["A"])],
                        c["float_mismatch"], dps, fin["pred"],
                        mp.nstr(fin["gap"], 12) if fin["gap"] is not None else "",
                        mp.nstr(fin["margin_min"], 12), mp.nstr(fin["margin_indep_start"], 12), fin["consistent"]])
    summary["worst_cases_csv"] = "computations/results/C10_WORST_CASES.csv (first 5000 HP cases by |margin|)"
    if genuine:
        summary["counterexample_candidates"] = [{"mech": c["mech"], "i": c["i"], "alpha": c["alpha"],
                                                 "A": np.asarray(c["A"]).tolist(), "hp": r} for c, r in genuine[:50]]
    summary["wall_seconds_hp"] = T()
    summary["memory"] = peak_rss_mb()
    p2idx = json.load(open(os.path.join(RESULTS, "P2_RAW_INDEX.json")))
    summary["float_stage_wall_seconds"] = p2idx["wall_seconds"]
    summary["master_seed"] = p2idx["master_seed"]
    summary["raw_files_sha256"] = {}
    import hashlib
    for mech, f in p2idx["files"].items():
        summary["raw_files_sha256"][os.path.basename(f)] = hashlib.sha256(open(f, "rb").read()).hexdigest()
    dump("C10_STRESS_SUMMARY.json", summary)


if __name__ == "__main__":
    main()

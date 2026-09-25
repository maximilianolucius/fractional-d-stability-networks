"""P3B — quantitative validation of C-14 (HP, mpmath 70 digits).

For diverse beta triples and alpha = 1 - 10^-k, k = 2..10:
  rate_k   = (T_alpha - T1)/(1 - alpha)          -> C(beta)
  err_k    = |rate_k - C| / C                      (should be O(10^-k))
  D_k      = (T_alpha - T1 - C (1-alpha))/(1-alpha)^2   -> second-order coefficient
  order    = log10(err_k / err_{k+1})              (should be ~1)
Monotonicity: T at 40 alpha values in (2/3, 1) strictly decreasing, per beta.
Symmetric check: T_alpha(1,1,1) = 1 + R3^3 and C(1,1,1) = 12 pi sqrt 3; the
second-order coefficient D(1,1,1) from the exact series of 1 + R3(alpha)^3.
Outputs computations/results/C14_LIMIT_RATE.csv and P3B_C14_SUMMARY.json.
"""
from __future__ import annotations

import csv
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, Timer, dump, log, peak_rss_mb, pool  # noqa: E402

from fdsn.c10_threshold import mp_rate_constant, mp_siami_R3, mp_T1, threshold_mp  # noqa: E402

KS = list(range(2, 11))
DPS = 70


def betas():
    rng = np.random.default_rng(401)
    fixed = [(1, 1, 1), (0.5, 0.5, 0.5), (3, 3, 3), (0.3, 2, 5), (100, 0.01, 1), (1e-4, 1, 1),
             (1e4, 1e4, 1e-4), (1, 1, 4), (0.2, 0.2, 1), (1.01, 0.99, 1.0), (10, 10, 0.1)]
    rand = [tuple(float(v) for v in np.exp(rng.normal(scale=2.0, size=3))) for _ in range(89)]
    return [tuple(repr(float(v)) for v in b) for b in fixed + rand]


def job(beta):
    mp.mp.dps = DPS
    bm = [mp.mpf(b) for b in beta]
    t1, C = mp_T1(bm), mp_rate_constant(bm)
    rows = []
    for k in KS:
        eps = mp.mpf(10) ** -k
        r = threshold_mp(beta, 1 - eps, dps=DPS)
        rate = (r["T"] - t1) / eps
        rows.append({"k": k, "T": r["T"], "rate": rate, "rel_err": abs(rate - C) / C,
                     "D_est": (r["T"] - t1 - C * eps) / eps ** 2})
    # monotonicity on a fine alpha grid
    al = [mp.mpf(2) / 3 + (1 - mp.mpf(2) / 3) * mp.mpf(j) / 41 for j in range(1, 41)]
    vals = [threshold_mp(beta, a, dps=40)["T"] for a in al]
    mono = all(v1 > v2 for v1, v2 in zip(vals, vals[1:])) and vals[-1] > t1
    return beta, t1, C, rows, mono


def symmetric_series():
    """Exact series of 1 + R3(1-eps)^3 around eps = 0 (mpmath taylor, 60 digits)."""
    mp.mp.dps = 60
    f = lambda e: 1 + mp_siami_R3(1 - e) ** 3
    c = mp.taylor(f, 0, 3)
    return {"T1": c[0], "C": c[1], "D": c[2], "E3": c[3], "C_expected_12pi_sqrt3": 12 * mp.pi * mp.sqrt(3)}


def main():
    T = Timer()
    B = betas()
    with pool(int(os.environ.get("P3B_WORKERS", "3"))) as P:
        res = P.map(job, B, chunksize=1)
    path = os.path.join(RESULTS, "C14_LIMIT_RATE.csv")
    worst = {}
    orders = []
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["beta12", "beta13", "beta23", "k", "one_minus_alpha", "T1", "C_beta", "T_alpha",
                    "rate_(T-T1)/(1-alpha)", "rel_err_vs_C", "D_estimate"])
        for beta, t1, C, rows, mono in res:
            for r in rows:
                w.writerow([*beta, r["k"], f"1e-{r['k']}", mp.nstr(t1, 30), mp.nstr(C, 30), mp.nstr(r["T"], 40),
                            mp.nstr(r["rate"], 30), mp.nstr(r["rel_err"], 8), mp.nstr(r["D_est"], 20)])
                worst[r["k"]] = max(worst.get(r["k"], 0), float(r["rel_err"]))
            e = [float(r["rel_err"]) for r in rows]
            orders.append([np.log10(e[i] / e[i + 1]) for i in range(len(e) - 1)])
    orders = np.array(orders)
    # D stabilisation: relative change between k=9 and k=10 estimates
    dstab = max(float(abs(rows[-1]["D_est"] / rows[-2]["D_est"] - 1)) for _, _, _, rows, _ in res)
    sym = symmetric_series()
    sym_num = [r for b, _, _, r, _ in res if b == ("1", "1", "1")] or \
        [r for b, _, _, r, _ in res if tuple(float(v) for v in b) == (1.0, 1.0, 1.0)]
    out = {
        "label": f"HP ({DPS} digits)", "n_beta": len(B), "k": KS,
        "worst_rel_err_by_k": {str(k): v for k, v in worst.items()},
        "convergence_order_median_by_step": np.median(orders, 0).tolist(),
        "convergence_order_min_by_step": orders.min(0).tolist(),
        "second_order_D_estimate_rel_change_k9_k10_max": dstab,
        "monotone_all": all(m for *_, m in res),
        "symmetric": {"series": sym,
                      "C_minus_12pi_sqrt3": abs(sym["C"] - sym["C_expected_12pi_sqrt3"]),
                      "numeric_D_estimate_k10": sym_num[0][-1]["D_est"] if sym_num else None},
        "D_over_C_range": [float(min(r[-1]["D_est"] / C for _, _, C, r, _ in res)),
                           float(max(r[-1]["D_est"] / C for _, _, C, r, _ in res))],
        "csv": "computations/results/C14_LIMIT_RATE.csv",
        "wall_seconds": T(), "memory": peak_rss_mb(),
    }
    dump("P3B_C14_SUMMARY.json", out)


if __name__ == "__main__":
    main()

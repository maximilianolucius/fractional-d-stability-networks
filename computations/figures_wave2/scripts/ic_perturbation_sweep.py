"""Round-1 R2-4: random initial-condition perturbations of the full nonlinear W2-A Caputo model at alpha = 0.9.

For each relative radius rho, N initial states u(0) = u* (1 + rho xi) with xi uniform on the unit sphere of R^3
(so d(0) = ||u(0)/u* - 1||_2 = rho exactly) are integrated with the fractional Adams-Bashforth-Moulton PECE
method (h = 0.01, refinement against h = 0.02) on 0 <= t <= T, for the row-scaled configuration R_* (the
case study) and for the unscaled model R = I.  A trajectory "returns" if all three states stay positive on
[0, T] and d(T) <= d(0)/10.  Integration is stopped early if a state falls below 1e-8 u*_i or d(t) > 5.
Numerical evidence only, not a proof.
Output: computations/figures_wave2/data/ic_perturbation_sweep.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from alpha_sweep_nonlinear import EQ, SCALINGS, make_rhs, rel_dist  # noqa: E402
from fdsn.caputo import caputo_pece  # noqa: E402

ALPHA = 0.9


def run(job):
    scaling, rho, k, xi, t_end, steps = job
    u0 = EQ * (1.0 + rho * np.asarray(xi))
    rhs = make_rhs(SCALINGS[scaling])
    stop = lambda _t, u: bool(np.any(u < 1e-8 * EQ) or np.linalg.norm(u / EQ - 1.0) > 5.0)
    res = {}
    for h in steps:
        t, u = caputo_pece(rhs, u0, ALPHA, t_end, h, stop=stop)
        d = rel_dist(u)
        res[h] = (t, u, d)
    hf = min(steps)
    t, u, d = res[hf]
    completed = bool(abs(t[-1] - t_end) < 1e-9)
    positive = bool(completed and np.all(u > 0))
    hc = max(steps)
    tc, uc, dc = res[hc]
    r = int(round(hc / hf)); n = min(len(uc), len(u[::r]))
    ok_c = bool(abs(tc[-1] - t_end) < 1e-9 and np.all(uc > 0) and dc[-1] <= rho / 10)
    return {"scaling": scaling, "rho": rho, "k": k, "xi": list(map(float, xi)), "completed": completed,
            "positive": positive, "d_end": float(d[-1]), "d_max": float(d.max()), "min_state_rel": float((u / EQ).min()),
            "returned": bool(positive and d[-1] <= rho / 10), "returned_coarse": ok_c,
            "refinement_max_rel_diff": float(np.max(np.abs((uc[:n] - u[::r][:n]) / EQ)))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--n", type=int, default=256)
    ap.add_argument("--t-end", type=float, default=300.0)
    ap.add_argument("--rhos", default="0.01,0.02,0.05,0.1,0.15,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.8,0.9")
    ap.add_argument("--seed", type=int, default=20261017)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    rhos = [float(v) for v in args.rhos.split(",")]
    jobs = []
    for rho in rhos:
        xs = rng.standard_normal((args.n, 3))
        xs /= np.linalg.norm(xs, axis=1, keepdims=True)
        for sc in ("worst", "unscaled"):
            for k, xi in enumerate(xs):
                jobs.append((sc, rho, k, xi.tolist(), args.t_end, (0.02, 0.01)))
    t0 = time.time()
    with Pool(args.workers) as pool:
        out = pool.map(run, jobs, chunksize=1)
    summ = []
    for sc in ("worst", "unscaled"):
        for rho in rhos:
            rs = [o for o in out if o["scaling"] == sc and o["rho"] == rho]
            summ.append({"scaling": sc, "rho": rho, "n": len(rs), "returned": sum(o["returned"] for o in rs),
                         "returned_coarse": sum(o["returned_coarse"] for o in rs), "positive": sum(o["positive"] for o in rs),
                         "max_d_end_over_rho": max(o["d_end"] for o in rs) / rho, "max_d_max": max(o["d_max"] for o in rs),
                         "min_state_rel": min(o["min_state_rel"] for o in rs),
                         "max_refinement_diff": max(o["refinement_max_rel_diff"] for o in rs)})
            print(json.dumps(summ[-1]), flush=True)
    radius = {}
    for sc in ("worst", "unscaled"):
        good = [s["rho"] for s in summ if s["scaling"] == sc]
        best = None
        for s in sorted([s for s in summ if s["scaling"] == sc], key=lambda s: s["rho"]):
            if s["returned"] == s["n"] and s["returned_coarse"] == s["n"]:
                best = s["rho"]
            else:
                break
        radius[sc] = best
    json.dump({"method": __doc__.strip().splitlines()[0], "alpha": ALPHA, "t_end": args.t_end, "steps": [0.02, 0.01],
               "n_per_radius": args.n, "seed": args.seed, "summary": summ, "largest_radius_all_returned": radius,
               "seconds": round(time.time() - t0, 1), "runs": out},
              open(os.path.join(HERE, "..", "data", "ic_perturbation_sweep.json"), "w"))
    print("largest radius with 100% return:", radius, "seconds", round(time.time() - t0, 1))


if __name__ == "__main__":
    main()

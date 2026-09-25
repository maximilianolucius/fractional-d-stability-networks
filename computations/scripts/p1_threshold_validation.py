"""P1 — validation of the numerical T_alpha(beta) implementation.

Outputs computations/results/P1_THRESHOLD_VALIDATION.json and
computations/results/P1_CERTIFIED_ANCHORS.csv.

Labels: FLOAT (float64), HP (mpmath), CERTIFIED (interval arithmetic,
fdsn.interval_cert) -- every entry states which.
Seeds: fixed per block (see SEED_* constants).
"""
from __future__ import annotations

import csv
import itertools
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, Timer, dump, log, peak_rss_mb, pool  # noqa: E402

from fdsn.c10_threshold import (  # noqa: E402
    T1, mp_h_alpha, mp_siami_R3, mp_T1, mp_uk, objective_G, threshold_batch, threshold_mp,
)
from fdsn.interval_cert import certify_threshold  # noqa: E402

SEED_FLOATMP, SEED_PERM, SEED_MONO, SEED_UNIQ, SEED_CONVEX = 101, 102, 103, 104, 105


def rand_beta(rng, n, spread=2.0):
    return np.exp(rng.normal(scale=spread, size=(n, 3)))


def _mp_job(args):
    beta, alpha, dps = args
    r = threshold_mp([repr(float(b)) for b in beta], repr(float(alpha)), dps=dps)
    return float(r["T"]), float(r["grad_norm"]), float(r["hess_min_eig"])


def block_float_vs_mp(P, n=4000):
    rng = np.random.default_rng(SEED_FLOATMP)
    beta = rand_beta(rng, n)
    alpha = np.concatenate([rng.uniform(0.6667, 0.7, n // 4), rng.uniform(0.7, 0.99, n // 2),
                            1 - 10 ** rng.uniform(-6, -2, n - n // 4 - n // 2)])
    tb = threshold_batch(beta, alpha, n_starts=2)
    res = P.map(_mp_job, [(beta[i], alpha[i], 40) for i in range(n)], chunksize=20)
    Tmp = np.array([r[0] for r in res])
    rel = np.abs(tb.T / Tmp - 1)
    worst = int(np.argmax(rel))
    return {
        "label": "FLOAT vs HP(40 digits)", "n": n, "seed": SEED_FLOATMP,
        "beta_lognormal_sigma": 2.0,
        "max_rel_err": float(rel.max()), "median_rel_err": float(np.median(rel)),
        "p99_rel_err": float(np.quantile(rel, 0.99)),
        "worst_case": {"beta": beta[worst], "alpha": alpha[worst], "T_float": tb.T[worst],
                       "T_mp": Tmp[worst]},
        "float_grad_norm_max": float(tb.grad_norm.max()),
        "float_hess_min_eig_min": float(tb.hess_min_eig.min()),
        "float_hess_cond_max": float(tb.hess_cond.max()),
        "float_hess_cond_median": float(np.median(tb.hess_cond)),
        "newton_iters_max": int(tb.it.max()),
        "hp_grad_norm_max": max(r[1] for r in res),
        "hp_hess_min_eig_min": min(r[2] for r in res),
    }


def block_permutation(n=20000):
    rng = np.random.default_rng(SEED_PERM)
    beta = rand_beta(rng, n)
    alpha = rng.uniform(0.6667, 0.9999, n)
    base = threshold_batch(beta, alpha).T
    worst = 0.0
    for perm in itertools.permutations(range(3)):
        if perm == (0, 1, 2):
            continue
        Tp = threshold_batch(beta[:, perm], alpha).T
        worst = max(worst, float(np.max(np.abs(Tp / base - 1))))
    return {"label": "FLOAT", "n": n, "seed": SEED_PERM, "permutations": 5,
            "max_rel_diff": worst}


def block_monotone(n=20000):
    rng = np.random.default_rng(SEED_MONO)
    beta = rand_beta(rng, n)
    alpha = rng.uniform(0.6667, 0.9999, n)
    base = threshold_batch(beta, alpha).T
    out = {"label": "FLOAT", "n": n, "seed": SEED_MONO}
    for k in range(3):
        for f in (1.0 + 1e-6, 1.01, 2.0):
            b2 = beta.copy()
            b2[:, k] *= f
            T2 = threshold_batch(b2, alpha).T
            viol = int(np.sum(T2 < base * (1 - 1e-13)))
            out[f"beta{['12', '13', '23'][k]}_x{f}"] = {
                "violations": viol, "min_rel_increase": float(np.min(T2 / base - 1))}
    return out


def _classical_job(args):
    beta, ks = args
    mp.mp.dps = 60
    bm = [mp.mpf(repr(float(b))) for b in beta]
    t1 = mp_T1(bm)
    return [float(threshold_mp([repr(float(b)) for b in beta], 1 - mp.mpf(10) ** -k, dps=60)["T"] / t1 - 1)
            for k in ks]


def block_classical_limit(P, n=300):
    rng = np.random.default_rng(SEED_MONO + 1)
    beta = rand_beta(rng, n)
    ks = list(range(1, 11))
    res = np.array(P.map(_classical_job, [(b, ks) for b in beta]))
    # relative gap (T_alpha/T1 - 1) should be O(1-alpha)
    ratios = res / np.array([10.0 ** -k for k in ks])
    return {"label": "HP(60 digits)", "n": n, "k": ks,
            "max_rel_gap_by_k": res.max(axis=0), "min_rel_gap_by_k": res.min(axis=0),
            "all_positive": bool(np.all(res > 0)),
            "gap_over_eps_max_by_k": ratios.max(axis=0), "gap_over_eps_min_by_k": ratios.min(axis=0)}


def _two_thirds_job(args):
    beta, k = args
    mp.mp.dps = 80
    alpha = mp.mpf(2) / 3 + mp.mpf(10) ** -k
    u, K = mp_uk(alpha)
    T = threshold_mp([repr(float(b)) for b in beta], alpha, dps=80)["T"]
    s = sum(mp.mpf(repr(float(b))) for b in beta)
    lead = T * K ** 3
    second = (lead - 27) / K                   # conjecture: -> 9*sum(beta) - 27
    return float(lead), float(second), float(9 * s - 27), float(K)


def block_two_thirds(P):
    rng = np.random.default_rng(SEED_MONO + 2)
    betas = [np.array([1.0, 1.0, 1.0]), np.array([0.3, 2.0, 5.0]), np.array([100, 0.01, 1.0])]
    betas += list(rand_beta(rng, 17))
    jobs = [(b, k) for b in betas for k in (3, 5, 7, 9, 12, 15)]
    res = P.map(_two_thirds_job, jobs)
    rows = []
    for (b, k), (lead, second, pred, K) in zip(jobs, res):
        rows.append({"beta": b, "k": k, "K": K, "T_K3": lead, "(T_K3-27)/K": second,
                     "9*sum(beta)-27": pred})
    err_lead = max(abs(r["T_K3"] - 27) / 27 for r in rows if r["k"] >= 9)
    err_second = max(abs(r["(T_K3-27)/K"] - r["9*sum(beta)-27"]) / (1 + abs(r["9*sum(beta)-27"]))
                     for r in rows if r["k"] >= 9)
    return {"label": "HP(80 digits)", "alpha": "2/3 + 10^-k",
            "conjecture": "T_alpha(beta) = 27/K^3 + (9*sum(beta) - 27)/K^2 + O(1/K), K = 1-4cos^2(alpha pi/2)",
            "max_rel_err_leading_k>=9": err_lead, "max_rel_err_second_order_k>=9": err_second,
            "rows": rows}


def _siami_job(alpha_str):
    mp.mp.dps = 110
    r = threshold_mp(["1", "1", "1"], alpha_str, dps=105)
    s = 1 + mp_siami_R3(alpha_str) ** 3
    c = 27 * mp_h_alpha(mp.mpf(1) / 3, alpha_str)
    return alpha_str, mp.nstr(r["T"], 50), float(abs(r["T"] / s - 1)), float(abs(r["T"] / c - 1)), \
        float(max(abs(x - mp.mpf(1) / 3) for x in r["x"]))


def block_siami(P):
    alphas = ["0.6667", "0.67", "0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "0.99", "0.999",
              "0.9999", "0.99999999"]
    res = P.map(_siami_job, alphas)
    return {"label": "HP(105 digits)", "rows": [
        {"alpha": a, "T": T, "rel_err_vs_1+R3^3": e1, "rel_err_vs_27h(1/3)": e2,
         "max|x*-1/3|": dx} for a, T, e1, e2, dx in res],
        "max_rel_err_vs_siami": max(r[2] for r in res)}


def _uniq_job(args):
    beta, alpha = args
    tb = threshold_batch(beta[None], alpha, n_starts=6, step=0.25, half_width=14)
    # enumerate ALL grid local minima and Newton-refine each
    from fdsn.c10_threshold import _grid, newton_refine
    grid = _grid(14, 0.25)
    m = int(round(np.sqrt(grid.shape[0])))
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    G = objective_G(grid, np.repeat(beta[None], grid.shape[0], 0), np.full(grid.shape[0], u),
                    np.full(grid.shape[0], K), derivs=False)[0].reshape(m, m)
    P_ = np.pad(G, 1, constant_values=np.inf)
    is_min = np.ones_like(G, dtype=bool)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di or dj:
                is_min &= G <= P_[1 + di:1 + di + m, 1 + dj:1 + dj + m]
    idx = np.nonzero(is_min.ravel())[0]
    ys = grid[idx]
    y, T, x, gn, hmin, hcond, it = newton_refine(ys, np.repeat(beta[None], len(idx), 0),
                                                 np.full(len(idx), u), np.full(len(idx), K))
    distinct = []
    for yy, TT in zip(y, T):
        if not any(np.linalg.norm(yy - d) < 1e-5 for d, _ in distinct):
            distinct.append((yy, TT))
    return len(idx), len(distinct), float(tb.T[0]), float(min(T))


def block_uniqueness(P, n=4000):
    rng = np.random.default_rng(SEED_UNIQ)
    beta = rand_beta(rng, n, spread=2.5)
    alpha = rng.uniform(0.6667, 0.9999, n)
    res = P.map(_uniq_job, [(beta[i], alpha[i]) for i in range(n)], chunksize=10)
    nd = np.array([r[1] for r in res])
    return {"label": "FLOAT", "n": n, "seed": SEED_UNIQ, "grid": "logit [-14,14]^2 step 0.25",
            "cases_with_>1_distinct_local_min": int(np.sum(nd > 1)),
            "max_grid_local_minima": int(max(r[0] for r in res)),
            "max_distinct_refined_minima": int(nd.max())}


def _convex_job(args):
    seed, n_pts = args
    rng = np.random.default_rng(seed)
    beta = np.exp(rng.normal(scale=2.5, size=(n_pts, 3)))
    alpha = rng.uniform(0.6667, 0.99999, n_pts)
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    y = rng.uniform(-12, 12, size=(n_pts, 2))
    G, g, H, x, B = objective_G(y, beta, u, K)
    ev = np.linalg.eigvalsh(H)
    # also Hessian in affine coordinates (x1, x2): H_x = J^-T (H_y - curvature) J^-1 is messy;
    # evaluate directly with finite differences of G in x-coordinates
    def Gx(x1, x2):
        yy = np.stack([np.log(x1 / (1 - x1 - x2)), np.log(x2 / (1 - x1 - x2))], -1)
        return objective_G(yy, beta, u, K, derivs=False)[0]
    x1, x2 = x[:, 0], x[:, 1]
    hstep = 1e-4 * np.minimum(np.minimum(x1, x2), x[:, 2])
    f0 = Gx(x1, x2)
    f11 = (Gx(x1 + hstep, x2) - 2 * f0 + Gx(x1 - hstep, x2)) / hstep ** 2
    f22 = (Gx(x1, x2 + hstep) - 2 * f0 + Gx(x1, x2 - hstep)) / hstep ** 2
    f12 = (Gx(x1 + hstep, x2 + hstep) - Gx(x1 + hstep, x2 - hstep) - Gx(x1 - hstep, x2 + hstep)
           + Gx(x1 - hstep, x2 - hstep)) / (4 * hstep ** 2)
    detx = f11 * f22 - f12 ** 2
    nonconvex_x = (f11 < 0) | (detx < -1e-6 * np.abs(f11 * f22))
    return int(np.sum(ev[:, 0] < 0)), int(np.sum(nonconvex_x)), n_pts


def block_convexity(P, n_jobs=64, n_pts=20000):
    res = P.map(_convex_job, [(SEED_CONVEX * 1000 + j, n_pts) for j in range(n_jobs)])
    tot = sum(r[2] for r in res)
    return {"label": "FLOAT", "points": tot, "seed_base": SEED_CONVEX * 1000,
            "logit_hessian_not_PD": sum(r[0] for r in res),
            "affine_x_hessian_not_PSD_fd": sum(r[1] for r in res),
            "note": "random points y~U[-12,12]^2, beta lognormal(2.5), alpha~U(0.6667,0.99999)"}


ANCHOR_BETAS = [("1", "1", "1"), ("0.5", "0.5", "0.5"), ("2", "2", "2"), ("0.3", "2", "5"),
                ("100", "0.01", "1"), ("1.5", "1.5", "0.2"), ("3", "3", "3"), ("0.1", "1", "10"),
                ("1", "1", "4"), ("0.2", "0.2", "1")]
ANCHOR_ALPHAS = ["0.7", "0.8", "0.9", "0.95", "0.99", "0.999"]


def _cert_job(args):
    beta, alpha = args
    r = certify_threshold(beta, alpha, dps=40, time_limit=900)
    return beta, alpha, r


def block_certified(P):
    jobs = [(b, a) for b in ANCHOR_BETAS for a in ANCHOR_ALPHAS]
    res = P.map(_cert_job, jobs, chunksize=1)
    path = os.path.join(RESULTS, "P1_CERTIFIED_ANCHORS.csv")
    ok = 0
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["beta12", "beta13", "beta23", "alpha", "certified", "L", "U", "rel_width",
                    "T1", "boxes", "seconds"])
        for beta, alpha, r in res:
            ok += bool(r["certified"])
            t1 = mp_T1([mp.mpf(b) for b in beta])
            w.writerow([*beta, alpha, r["certified"], mp.nstr(r.get("L", mp.nan), 35),
                        mp.nstr(r.get("U", mp.nan), 35), mp.nstr(r.get("rel_width", mp.nan), 5),
                        mp.nstr(t1, 35), r.get("boxes"), round(r.get("seconds", 0), 2)])
    return {"label": "CERTIFIED (interval arithmetic of the variational formula)",
            "n": len(jobs), "certified": ok, "csv": "computations/results/P1_CERTIFIED_ANCHORS.csv"}


def main():
    T = Timer()
    out = {}
    with pool() as P:
        for name, fn in [("float_vs_mp", lambda: block_float_vs_mp(P)),
                         ("permutation_symmetry", block_permutation),
                         ("monotonicity_in_beta", block_monotone),
                         ("classical_limit", lambda: block_classical_limit(P)),
                         ("two_thirds_transition", lambda: block_two_thirds(P)),
                         ("symmetric_siami", lambda: block_siami(P)),
                         ("uniqueness_of_minimizer", lambda: block_uniqueness(P)),
                         ("convexity_scan", lambda: block_convexity(P)),
                         ("certified_anchors", lambda: block_certified(P))]:
            log("P1 block", name)
            t = Timer()
            out[name] = fn()
            out[name]["seconds"] = t()
            dump("P1_THRESHOLD_VALIDATION.json", out)
    out["wall_seconds"] = T()
    out["memory"] = peak_rss_mb()
    dump("P1_THRESHOLD_VALIDATION.json", out)


if __name__ == "__main__":
    main()

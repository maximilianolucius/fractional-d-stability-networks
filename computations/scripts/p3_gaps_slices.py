"""P3 — C-11 conservatism, closed-form slices, explicit parametrisation (NUMERICAL + HP).

Outputs
  computations/results/C11_GAP_SUMMARY.csv    per-alpha statistics of the C-11 gap
  computations/results/C11_GAP_GRID.csv       full invariant-space grid (plot-ready)
  computations/results/P3_SLICES.json         slice / optimizer / parametrisation checks

Definitions (kappa-space boundaries, strict-P stratum):
  T1      = (sum sqrt beta)^2                  classical Cain
  T_Phi   = T1 / rho_alpha                     C-11: Phi > rho  <=>  kappa < T1/rho
  T_alpha = exact C-10 threshold
  certified_band_fraction = (T_Phi - T1) / (T_alpha - T1)  in (0, 1]
Explicit parametrisation (derived from the Lagrange conditions; see report):
  for x in the open simplex and r > 2u/K, with B = K r^2 - 2u r and
  E = (K r - 2u)(1 + 3u r)/((K r - u)(1 + 2u r)),
     beta_ij = B [1 + (2E - 3)(1 - 2 x_k)] / (2 E x_i x_j),   T = r^2 (1 + 2u r)/(x1 x2 x3),
  whenever all three beta_ij > 0.
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

from fdsn.c10_threshold import T1, phi_threshold, rho_alpha, siami_R3, threshold, threshold_batch, threshold_mp  # noqa: E402

ALPHAS = [0.6667, 0.68, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99, 0.999, 0.9999]
GRID = np.logspace(-2, 2, 21)


def param_beta(x, r, alpha):
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    B = K * r * r - 2 * u * r
    E = (K * r - 2 * u) * (1 + 3 * u * r) / ((K * r - u) * (1 + 2 * u * r))
    x1, x2, x3 = x[..., 0], x[..., 1], x[..., 2]
    c = lambda xk: 1 + (2 * E - 3) * (1 - 2 * xk)
    b12 = B * c(x3) / (2 * E * x1 * x2)
    b13 = B * c(x2) / (2 * E * x1 * x3)
    b23 = B * c(x1) / (2 * E * x2 * x3)
    T = r * r * (1 + 2 * u * r) / (x1 * x2 * x3)
    return np.stack([b12, b13, b23], -1), T


def block_grid():
    trip = [t for t in itertools.product(GRID, repeat=3) if t[0] <= t[1] <= t[2]]
    beta = np.array(trip)
    rows = []
    summ = []
    for a in ALPHAS:
        tb = threshold_batch(beta, a, n_starts=2)
        t1 = T1(beta)
        tphi = phi_threshold(beta, a)
        frac = (tphi - t1) / (tb.T - t1)
        ratio = tphi / tb.T
        for i in range(len(beta)):
            rows.append([*beta[i], a, t1[i], tphi[i], tb.T[i], frac[i], ratio[i], *tb.x[i]])
        iw, ib = int(np.argmin(frac)), int(np.argmax(frac))
        sym = np.isclose(beta[:, 0], beta[:, 2])
        summ.append({
            "alpha": a, "n_beta": len(beta), "rho_alpha": rho_alpha(a),
            "frac_min": frac.min(), "frac_median": float(np.median(frac)), "frac_max": frac.max(),
            "Tphi_over_Talpha_min": ratio.min(), "Tphi_over_Talpha_median": float(np.median(ratio)),
            "Tphi_over_Talpha_max": ratio.max(),
            "worst_beta": beta[iw].tolist(), "best_beta": beta[ib].tolist(),
            "sym_slice_frac_range": [float(frac[sym].min()), float(frac[sym].max())],
            "violations_Tphi_gt_Talpha": int(np.sum(tphi > tb.T * (1 + 1e-12))),
        })
    with open(os.path.join(RESULTS, "C11_GAP_GRID.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["beta12", "beta13", "beta23", "alpha", "T1", "T_Phi", "T_alpha",
                    "certified_band_fraction", "T_Phi_over_T_alpha", "x1*", "x2*", "x3*"])
        w.writerows([[f"{v:.12g}" for v in r] for r in rows])
    with open(os.path.join(RESULTS, "C11_GAP_SUMMARY.csv"), "w", newline="") as f:
        w = csv.writer(f)
        keys = list(summ[0].keys())
        w.writerow(keys)
        for s in summ:
            w.writerow([s[k] if not isinstance(s[k], float) else f"{s[k]:.10g}" for k in keys])
    return summ


def block_random_gap(n=200000):
    """Random wide beta (lognormal sigma 2.5) incl. ecological regimes."""
    rng = np.random.default_rng(301)
    beta = np.exp(rng.normal(scale=2.5, size=(n, 3)))
    alpha = rng.uniform(0.6667, 0.9999, n)
    tb = threshold_batch(beta, alpha)
    t1, tphi = T1(beta), T1(beta) / ((1 - 2 * np.cos(alpha * np.pi / 2)) ** 2)
    frac = (tphi - t1) / (tb.T - t1)
    i = int(np.argmin(frac))
    j = int(np.argmax(frac))
    # dependence on anisotropy of the Cain minimiser: spread = max/min sqrt(beta)
    spread = np.sqrt(beta).max(1) / np.sqrt(beta).min(1)
    bins = [1, 1.5, 3, 10, 100, 1e4, np.inf]
    by = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (spread >= lo) & (spread < hi)
        if m.any():
            by.append({"sqrt_beta_spread": [lo, hi], "n": int(m.sum()),
                       "frac_median": float(np.median(frac[m])), "frac_min": float(frac[m].min()),
                       "frac_max": float(frac[m].max())})
    return {"label": "FLOAT", "n": n, "seed": 301, "violations_Tphi_gt_Talpha": int(np.sum(tphi > tb.T * (1 + 1e-12))),
            "frac_min": float(frac.min()), "frac_max": float(frac.max()), "frac_median": float(np.median(frac)),
            "worst": {"beta": beta[i], "alpha": alpha[i], "frac": frac[i]},
            "best": {"beta": beta[j], "alpha": alpha[j], "frac": frac[j]},
            "by_anisotropy": by}


def block_symmetric_slice():
    out = []
    for a in ALPHAS[1:]:
        bs = np.logspace(-6, 6, 121)
        tb = threshold_batch(np.stack([bs] * 3, 1), a, n_starts=3)
        closed = 27 * (lambda h: h)(0)  # placeholder to keep linter quiet
        del closed
        from fdsn.c10_threshold import h_alpha
        cf = 27 * h_alpha(bs / 3, a)
        out.append({"alpha": a, "max_rel_err_closed_form": float(np.max(np.abs(tb.T / cf - 1))),
                    "max_|x*-1/3|": float(np.max(np.abs(tb.x - 1 / 3))),
                    "Tphi_over_T_at_b=1": float(9 / rho_alpha(a) / (1 + siami_R3(a) ** 3))})
    return out


def block_two_equal():
    rng = np.random.default_rng(302)
    n = 50000
    a_ = np.exp(rng.normal(scale=2.5, size=n))
    c_ = np.exp(rng.normal(scale=2.5, size=n))
    al = rng.uniform(0.6667, 0.9999, n)
    beta = np.stack([a_, a_, c_], 1)
    tb = threshold_batch(beta, al, n_starts=2)
    return {"label": "FLOAT", "n": n, "seed": 302, "slice": "beta12 = beta13 != beta23",
            "max_|x2*-x3*|": float(np.max(np.abs(tb.x[:, 1] - tb.x[:, 2]))),
            "max_grad_norm": float(tb.grad_norm.max())}


def block_parametrisation(n=200000):
    """Forward map (x, r) -> (beta, T) vs numerical minimisation."""
    rng = np.random.default_rng(303)
    alpha = rng.uniform(0.6667, 0.9999, n)
    t = alpha * np.pi / 2
    u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
    x = rng.dirichlet([1.5, 1.5, 1.5], size=n)
    r = 2 * u / K * (1 + np.exp(rng.normal(scale=3, size=n)))
    beta, T = param_beta(x, r, alpha)
    ok = np.all(beta > 0, 1) & np.all(np.isfinite(beta), 1)
    tb = threshold_batch(beta[ok], alpha[ok], n_starts=2)
    relT = np.abs(tb.T / T[ok] - 1)
    dx = np.max(np.abs(tb.x - x[ok]), 1)
    # HP spot checks
    idx = np.nonzero(ok)[0][:40]
    hp = []
    for i in idx:
        with mp.workdps(50):
            rr = threshold_mp(beta[i], alpha[i], dps=45)
            hp.append(float(abs(rr["T"] / T[i] - 1)))
    return {"label": "FLOAT (+HP spot checks at 45 digits)", "n_sampled": n, "n_admissible": int(ok.sum()),
            "admissible_fraction": float(ok.mean()),
            "max_rel_err_T": float(relT.max()), "median_rel_err_T": float(np.median(relT)),
            "max_abs_err_x": float(dx.max()), "hp_max_rel_err_T": max(hp)}


def block_smooth_dependence():
    """x*(alpha, beta) along paths: max second difference / step^2 (no jumps)."""
    beta0 = np.array([0.3, 2.0, 5.0])
    al = np.linspace(0.6668, 0.9999, 3001)
    tb = threshold_batch(np.repeat(beta0[None], al.size, 0), al)
    d2 = np.abs(np.diff(tb.x, 2, axis=0)).max() / (al[1] - al[0]) ** 2
    d1 = np.abs(np.diff(tb.x, 1, axis=0)).max() / (al[1] - al[0])
    s = np.linspace(-4, 4, 3001)
    bp = np.stack([np.exp(s), np.full_like(s, 1.0), np.exp(-s / 2)], 1)
    tb2 = threshold_batch(bp, 0.9)
    e1 = np.abs(np.diff(tb2.x, 1, axis=0)).max() / (s[1] - s[0])
    e2 = np.abs(np.diff(tb2.x, 2, axis=0)).max() / (s[1] - s[0]) ** 2
    return {"label": "FLOAT", "alpha_path": {"beta": beta0, "max|dx/dalpha|": d1, "max|d2x/dalpha2|": d2},
            "beta_path": {"alpha": 0.9, "max|dx/ds|": e1, "max|d2x/ds2|": e2},
            "x_at_alpha_ends": [tb.x[0].tolist(), tb.x[-1].tolist()],
            "cain_minimiser_at_alpha1": (np.sqrt(beta0[[2, 1, 0]]) / np.sqrt(beta0).sum()).tolist()}


def main():
    T = Timer()
    out = {}
    for name, fn in [("grid", block_grid), ("random_gap", block_random_gap),
                     ("symmetric_slice", block_symmetric_slice), ("two_equal_slice", block_two_equal),
                     ("explicit_parametrisation", block_parametrisation),
                     ("smooth_dependence", block_smooth_dependence)]:
        log("P3", name)
        t = Timer()
        out[name] = fn()
        out[name + "_seconds"] = t()
        dump("P3_SLICES.json", out)
    out["wall_seconds"] = T()
    out["memory"] = peak_rss_mb()
    dump("P3_SLICES.json", out)


if __name__ == "__main__":
    main()

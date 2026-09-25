"""P4 — ecological motif phase-diagram datasets (C-13 coordinates).

Theorem-illustration data (exact boundaries evaluated numerically; a subset of
anchor values is CERTIFIED in P1).  Plot-ready CSVs are written to
computations/results/C13_PHASE_DATA/, figures to .../figures/ (separate).

Coordinates: g_ij = a_ij a_ji/(p_i p_j), beta_ij = 1 - g_ij,
             kappa = sum(beta) - 2 - L3.
Regions on the strict-P stratum (kappa > 0 <=> L3 < sum(beta) - 2):
  CLASSICAL  : kappa < T1              <=> L3 > sum(beta) - 2 - T1
  FRACTIONAL : T1 < kappa < T_alpha    (genuinely fractional band; alpha <= 2/3: T_alpha = inf)
  UNSTABLE   : kappa > T_alpha
Real realizability: L3 = l + G/l with G = g12 g13 g23, hence L3^2 >= 4G if G > 0.

Files
  L3_alpha_<name>.csv   : alpha, T1, T_alpha, W, L3_kappa0, L3_cain, L3_frac, realizability
  pairloop_alpha<a>_g23<g>.csv : g12, g13 grid, T1, T_alpha, W, W/T1, L3 bounds
  width_asymptotics.csv : W vs alpha for the named triples + C(beta)(1-alpha) and 27/K^3
  symmetric_width.csv   : W along beta12=beta13=beta23=b (antagonistic b>1 vs mutualistic b<1)
  direct_validation.json: independent direct-margin classification of sampled points per region
"""
from __future__ import annotations

import csv
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from _common import RESULTS, Timer, dump, log, peak_rss_mb  # noqa: E402

from fdsn.c10_threshold import T1, h_alpha, matrix_from_invariants, rate_constant, threshold_batch  # noqa: E402
from fdsn.direct_margin import min_margin  # noqa: E402

OUT = os.path.join(RESULTS, "C13_PHASE_DATA")
FIG = os.path.join(OUT, "figures")
os.makedirs(FIG, exist_ok=True)

TRIPLES = {
    "no_pair_loops_111": (1.0, 1.0, 1.0),
    "all_antagonistic_333": (3.0, 3.0, 3.0),
    "antagonistic_mixed_1.5_4_2": (1.5, 4.0, 2.0),
    "all_mutualistic_competitive_0.5": (0.5, 0.5, 0.5),
    "mutualistic_mixed_0.2_0.8_0.5": (0.2, 0.8, 0.5),
    "mixed_3_0.5_1": (3.0, 0.5, 1.0),
    "mixed_5_0.2_0.2": (5.0, 0.2, 0.2),
    "weak_pair_loops_1.01_0.99_1.005": (1.01, 0.99, 1.005),
    "strong_antagonism_20_20_20": (20.0, 20.0, 20.0),
}


def alpha_grid():
    a1 = 2 / 3 + np.logspace(-6, np.log10(1 / 3 - 1e-6), 400)
    return np.unique(np.concatenate([a1[a1 < 1], 1 - np.logspace(-6, -1, 100)]))


def write(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow([f"{v:.12g}" if isinstance(v, (float, np.floating)) else v for v in r])


def block_L3_alpha():
    al = alpha_grid()
    info = {}
    for name, b in TRIPLES.items():
        b = np.array(b)
        tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
        t1 = T1(b)
        s = b.sum()
        G = np.prod(1 - b)
        rows = []
        for a, Ta in zip(al, tb.T):
            rows.append([a, t1, Ta, Ta - t1, s - 2, s - 2 - t1, s - 2 - Ta,
                         ("L3^2>=4G" if G > 0 else "all L3"), 2 * np.sqrt(G) if G > 0 else 0.0])
        rows.append(["alpha<=2/3", t1, "inf", "inf", s - 2, s - 2 - t1, "-inf", "", ""])
        write(os.path.join(OUT, f"L3_alpha_{name}.csv"),
              ["alpha", "T1", "T_alpha", "W_alpha", "L3_at_kappa0", "L3_cain_boundary",
               "L3_fractional_boundary", "realizability", "sqrt4G"], rows)
        info[name] = {"beta": b, "T1": t1, "W_at_0.9": float(np.interp(0.9, al, tb.T - t1)),
                      "W_at_0.99": float(np.interp(0.99, al, tb.T - t1)),
                      "G": G, "realizable_band_everywhere": bool(G <= 0 or (s - 2 - t1) ** 2 >= 4 * G)}
    return info


def block_pairloop():
    files = []
    g = np.linspace(-6, 0.95, 140)
    G12, G13 = np.meshgrid(g, g, indexing="ij")
    for a in (0.75, 0.9, 0.99):
        for g23 in (0.0, -2.0, 0.5):
            beta = np.stack([1 - G12.ravel(), 1 - G13.ravel(), np.full(G12.size, 1 - g23)], 1)
            tb = threshold_batch(beta, a)
            t1 = T1(beta)
            s = beta.sum(1)
            rows = [[G12.ravel()[i], G13.ravel()[i], g23, a, t1[i], tb.T[i], tb.T[i] - t1[i],
                     (tb.T[i] - t1[i]) / t1[i], s[i] - 2 - t1[i], s[i] - 2 - tb.T[i]] for i in range(beta.shape[0])]
            fn = f"pairloop_alpha{a}_g23_{g23}.csv"
            write(os.path.join(OUT, fn), ["g12", "g13", "g23", "alpha", "T1", "T_alpha", "W_alpha",
                                          "W_over_T1", "L3_cain", "L3_frac"], rows)
            files.append(fn)
    return {"files": files, "grid": "g12,g13 in linspace(-6,0.95,140); beta=1-g"}


def block_width_asymptotics():
    rows = []
    summary = {}
    for name, b in TRIPLES.items():
        b = np.array(b)
        near1 = 1 - np.logspace(-7, -1, 60)
        near23 = 2 / 3 + np.logspace(-7, -1, 60)
        for al, reg in ((near1, "alpha->1"), (near23, "alpha->2/3")):
            tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
            W = tb.T - T1(b)
            t = al * np.pi / 2
            K = -np.sin(3 * t) / np.sin(t)
            for a, w_, k_ in zip(al, W, K):
                rows.append([name, reg, a, w_, rate_constant(b) * (1 - a), 27 / k_ ** 3 + (9 * b.sum() - 27) / k_ ** 2])
            if reg == "alpha->1":
                summary[name] = {"W/(C(1-alpha)) at 1-1e-7": float(W[0] / (rate_constant(b) * 1e-7)),
                                 "C_beta": float(rate_constant(b))}
            else:
                summary[name]["W*K^3/27 at 2/3+1e-7"] = float(W[0] * K[0] ** 3 / 27)
    write(os.path.join(OUT, "width_asymptotics.csv"),
          ["triple", "regime", "alpha", "W_alpha", "C_beta*(1-alpha)", "27/K^3+(9S-27)/K^2"], rows)
    return summary


def block_symmetric_width():
    bs = np.logspace(-3, 3, 241)
    rows = []
    out = {}
    for a in (0.7, 0.8, 0.9, 0.95, 0.99):
        W = 27 * h_alpha(bs / 3, a) - 9 * bs          # exact closed form on the symmetric slice
        rel = W / (9 * bs)
        for b, w_, r_ in zip(bs, W, rel):
            rows.append([a, b, 1 - b, w_, r_])
        out[str(a)] = {"W_monotone_increasing_in_b": bool(np.all(np.diff(W) > 0)),
                       "W_over_T1_monotone_decreasing_in_b": bool(np.all(np.diff(rel) < 0)),
                       "W_at_b=0.5(mutualistic)": float(np.interp(0.5, bs, W)),
                       "W_at_b=1(no loops)": float(np.interp(1.0, bs, W)),
                       "W_at_b=3(antagonistic)": float(np.interp(3.0, bs, W))}
    write(os.path.join(OUT, "symmetric_width.csv"), ["alpha", "b", "g=1-b", "W_alpha", "W_over_T1"], rows)
    return out


def block_direct_validation(n_per=300):
    """Independent check: sample kappa inside each region, build matrices, direct margin."""
    rng = np.random.default_rng(501)
    res = {}
    for name, b in TRIPLES.items():
        b = np.array(b)
        for a in (0.75, 0.9, 0.99):
            Ta = threshold_batch(b[None], a).T[0]
            t1 = T1(b)
            As, lab = [], []
            for region, lo, hi in (("CLASSICAL", 0.02 * t1, t1), ("FRACTIONAL", t1, Ta), ("UNSTABLE", Ta, 3 * Ta)):
                k = 0
                while k < n_per // 3:
                    kap = lo + (hi - lo) * rng.uniform(0.02, 0.98)
                    A = matrix_from_invariants(b, kap, p=np.exp(rng.normal(size=3)), rng=rng,
                                               branch=int(rng.integers(2)))
                    if A is None:
                        continue
                    As.append(A); lab.append(region); k += 1
            As = np.array(As)
            frac = min_margin(As, a)["margin"]
            hur = min_margin(As, 1.0)["margin"]
            lab = np.array(lab)
            ok_frac = np.where(lab == "UNSTABLE", frac < 0, frac > 0)
            ok_cls = np.where(lab == "CLASSICAL", hur > 0, hur < 0)
            res[f"{name}|alpha={a}"] = {"n": int(lab.size), "fractional_membership_agrees": int(ok_frac.sum()),
                                         "hurwitz_D_stability_agrees": int(ok_cls.sum())}
    tot = sum(v["n"] for v in res.values())
    return {"label": "FLOAT direct eigenvalue optimisation (independent of C-10)", "cases": tot,
            "all_agree": all(v["fractional_membership_agrees"] == v["n"] and v["hurwitz_D_stability_agrees"] == v["n"]
                             for v in res.values()), "detail": res}


def figures():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    for name in ("no_pair_loops_111", "all_antagonistic_333", "all_mutualistic_competitive_0.5", "mixed_3_0.5_1"):
        rows = list(csv.DictReader(open(os.path.join(OUT, f"L3_alpha_{name}.csv"))))[:-1]
        a = np.array([float(r["alpha"]) for r in rows])
        lc = np.array([float(r["L3_cain_boundary"]) for r in rows])
        lf = np.array([float(r["L3_fractional_boundary"]) for r in rows])
        l0 = float(rows[0]["L3_at_kappa0"])
        fig, ax = plt.subplots(figsize=(5, 3.6))
        lo = min(lf[a > 0.72].min(), lc.min()) - 5
        ax.fill_between(a, lc, l0, color="#4C78A8", alpha=0.35, label="classical D-stable")
        ax.fill_between(a, np.maximum(lf, lo), lc, color="#F58518", alpha=0.45, label="genuinely fractional")
        ax.fill_between(a, lo, np.maximum(lf, lo), color="#BBBBBB", alpha=0.4, label="not in F_alpha")
        ax.set_ylim(lo, l0 + 1)
        ax.set_xlabel("alpha"); ax.set_ylabel("L3 (normalized 3-cycle feedback)")
        ax.set_title(name, fontsize=9); ax.legend(fontsize=7, loc="lower right")
        fig.tight_layout(); fig.savefig(os.path.join(FIG, f"L3_alpha_{name}.png"), dpi=130); plt.close(fig)
    rows = list(csv.DictReader(open(os.path.join(OUT, "pairloop_alpha0.9_g23_0.0.csv"))))
    g12 = np.array([float(r["g12"]) for r in rows]); g13 = np.array([float(r["g13"]) for r in rows])
    w = np.array([float(r["W_over_T1"]) for r in rows])
    n = int(round(np.sqrt(len(rows))))
    fig, ax = plt.subplots(figsize=(4.6, 3.8))
    cs = ax.contourf(g12.reshape(n, n), g13.reshape(n, n), w.reshape(n, n), 20, cmap="viridis")
    fig.colorbar(cs, label="W_alpha / T1  (alpha=0.9, g23=0)")
    ax.set_xlabel("g12 (<0 antagonistic, >0 mutualistic/competitive)"); ax.set_ylabel("g13")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "pairloop_relwidth_alpha0.9.png"), dpi=130); plt.close(fig)


def main():
    T = Timer()
    out = {}
    for name, fn in [("L3_alpha", block_L3_alpha), ("pairloop", block_pairloop),
                     ("width_asymptotics", block_width_asymptotics), ("symmetric_width", block_symmetric_width),
                     ("direct_validation", block_direct_validation)]:
        log("P4", name)
        out[name] = fn()
        dump("C13_PHASE_DATA/P4_SUMMARY.json", out)
    figures()
    out["wall_seconds"] = T()
    out["memory"] = peak_rss_mb()
    dump("C13_PHASE_DATA/P4_SUMMARY.json", out)
    with open(os.path.join(OUT, "README.md"), "w") as f:
        f.write(__doc__)


if __name__ == "__main__":
    main()

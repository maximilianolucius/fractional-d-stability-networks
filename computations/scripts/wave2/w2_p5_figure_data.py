"""Wave 2 P5 — publication figure-source datasets (data, not graphics).

Every CSV row carries an `evidence` column: FLOAT (float64 threshold_batch),
HP (mpmath threshold_mp, digits stated) or CERTIFIED (interval bracket copied
from CERTIFIED_THRESHOLD_ATLAS.csv).  Each family Fk has a README.md with the
mathematical purpose, the columns, the generating command and the commit SHA.

F1 T_alpha/T_1 vs alpha            F2 W_alpha = T_alpha - T_1         F3 W_alpha/T_1
F4 C-11 sufficient fraction        F5 ecological (L3, alpha) boundaries
F6 pair-loop sensitivity surfaces  F7 optimizer coordinates x*(alpha, beta)
F8 classical-order asymptotic      F9 low-order blow-up
Preview PNGs (QA only) in FIGURE_DATA/preview/.
"""
from __future__ import annotations

import csv
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import BASELINE_SHA, FIG, RESULTS, Timer, dump, git_sha, log, pool, stamp  # noqa: E402

from fdsn.c10_threshold import (T1, h_derivs, mp_rate_constant, mp_T1, mp_uk, rate_constant, rho_alpha,  # noqa: E402
                                threshold_batch, threshold_mp)

os.makedirs(os.path.join(FIG, "preview"), exist_ok=True)
SCRIPT = "computations/scripts/wave2/w2_p5_figure_data.py"

TRIPLES = {
    "no_pair_loops_(1,1,1)": (1.0, 1.0, 1.0), "all_antagonistic_(3,3,3)": (3.0, 3.0, 3.0),
    "antagonistic_mixed_(1.5,4,2)": (1.5, 4.0, 2.0), "all_mutualistic_(0.5,0.5,0.5)": (0.5, 0.5, 0.5),
    "mutualistic_mixed_(0.2,0.8,0.5)": (0.2, 0.8, 0.5), "mixed_(3,0.5,1)": (3.0, 0.5, 1.0),
    "mixed_(5,0.2,0.2)": (5.0, 0.2, 0.2), "weak_pair_loops_(1.01,0.99,1.005)": (1.01, 0.99, 1.005),
    "strong_antagonism_(20,20,20)": (20.0, 20.0, 20.0), "anisotropic_(0.01,1,100)": (0.01, 1.0, 100.0),
}


def alpha_dense():
    a = np.concatenate([2 / 3 + np.logspace(-8, np.log10(1 / 3 - 1e-8), 300), 1 - np.logspace(-8, -1, 120)])
    return np.unique(a[(a > 2 / 3) & (a < 1)])


def write(name, header, rows, readme):
    d = os.path.join(FIG, name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name + ".csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(header)
        for r in rows:
            w.writerow([f"{v:.15g}" if isinstance(v, (float, np.floating)) else v for v in r])
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(f"# {name}\n\n{readme}\n\nGenerating script: `{SCRIPT}` (function for this family). "
                f"Commit: {git_sha()}; baseline {BASELINE_SHA}.\n")
    return d


def atlas_rows():
    path = os.path.join(RESULTS, "CERTIFIED_THRESHOLD_ATLAS.csv")
    if not os.path.exists(path):
        return []
    return [r for r in csv.DictReader(open(path)) if r["status"] == "CERTIFIED"]


# ----------------------------------------------------------------- F1-F3, F7 (alpha sweeps)

def f1_f2_f3_f7():
    al = alpha_dense()
    rows1, rows2, rows3, rows7 = [], [], [], []
    for name, b in TRIPLES.items():
        b = np.array(b); t1 = T1(b)
        tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
        for a, T, x in zip(al, tb.T, tb.x):
            rows1.append([name, *b, a, t1, T, T / t1, "FLOAT"])
            rows2.append([name, *b, a, t1, T, T - t1, "FLOAT"])
            rows3.append([name, *b, a, t1, T, (T - t1) / t1, "FLOAT"])
            rows7.append([name, *b, a, *x, "FLOAT"])
    # certified anchors (symmetric family A and ecological family E of the atlas)
    cert = []
    for r in atlas_rows():
        if r["family"] in ("A", "E"):
            b = np.array([float(r["beta12"]), float(r["beta13"]), float(r["beta23"])]); t1 = T1(b)
            L, U = float(r["L"]), float(r["U"])
            cert.append([f"atlas_{r['family']}", *b, float(r["alpha"]), t1, r["L"], r["U"], r["mid"], float(r["mid"]) / t1,
                         (float(r["mid"]) - t1), (float(r["mid"]) - t1) / t1, r["x1_hat"], r["x2_hat"], r["x3_hat"],
                         r["x_enclosure_radius"], "CERTIFIED"])
    write("F1_T_ratio_vs_alpha", ["triple", "beta12", "beta13", "beta23", "alpha", "T1", "T_alpha", "T_alpha_over_T1", "evidence"], rows1,
          "Ratio T_alpha(beta)/T_1(beta) versus alpha on (2/3,1) for representative pair-loop triples (C-10, C-14). "
          "Shows the monotone decrease to 1 at alpha -> 1 and the blow-up at alpha -> 2/3+. Rows FLOAT; certified anchors in F1_certified_anchors.csv.")
    with open(os.path.join(FIG, "F1_T_ratio_vs_alpha", "F1_certified_anchors.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["family", "beta12", "beta13", "beta23", "alpha", "T1", "T_alpha_L", "T_alpha_U", "T_alpha_mid", "ratio_mid",
                    "W_mid", "W_over_T1_mid", "x1_hat", "x2_hat", "x3_hat", "x_enclosure_radius", "evidence"])
        w.writerows(cert)
    write("F2_W_alpha", ["triple", "beta12", "beta13", "beta23", "alpha", "T1", "T_alpha", "W_alpha", "evidence"], rows2,
          "Absolute width W_alpha = T_alpha - T_1 of the genuinely fractional band (C-10 §7, C-14). FLOAT rows; CERTIFIED anchors: see F1_certified_anchors.csv (column W_mid with bracket).")
    write("F3_W_over_T1", ["triple", "beta12", "beta13", "beta23", "alpha", "T1", "T_alpha", "W_over_T1", "evidence"], rows3,
          "Relative band width W_alpha/T_1 versus alpha. FLOAT rows; certified anchors in F1_certified_anchors.csv.")
    write("F7_xstar_alpha_beta", ["triple", "beta12", "beta13", "beta23", "alpha", "x1", "x2", "x3", "evidence"], rows7,
          "Unique simplex minimiser x*(alpha, beta) (C-15) along alpha for the triples; tends to the Cain minimiser "
          "(sqrt beta23, sqrt beta13, sqrt beta12)/S at alpha -> 1 and to the centre (1/3,1/3,1/3) at alpha -> 2/3+. "
          "FLOAT rows; rigorous enclosures (x_hat, radius) for atlas anchors in F1_certified_anchors.csv. "
          "A beta-path at fixed alpha is in F7_xstar_beta_path.csv.")
    # beta path at fixed alpha
    s = np.linspace(-4, 4, 801)
    bp = np.stack([np.exp(s), np.ones_like(s), np.exp(-s / 2)], 1)
    rows = []
    for a in (0.75, 0.9, 0.99):
        tb = threshold_batch(bp, a)
        S = np.sqrt(bp).sum(1)
        cain = np.sqrt(bp[:, [2, 1, 0]]) / S[:, None]
        for i in range(s.size):
            rows.append([a, s[i], *bp[i], *tb.x[i], *cain[i], "FLOAT"])
    with open(os.path.join(FIG, "F7_xstar_alpha_beta", "F7_xstar_beta_path.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["alpha", "s", "beta12=e^s", "beta13=1", "beta23=e^-s/2", "x1", "x2", "x3", "cain_x1", "cain_x2", "cain_x3", "evidence"])
        for r in rows:
            w.writerow([f"{v:.12g}" if isinstance(v, (float, np.floating)) else v for v in r])


# ----------------------------------------------------------------- F4 C-11 fraction

def f4():
    al = alpha_dense()
    rows = []
    for name, b in TRIPLES.items():
        b = np.array(b); t1 = T1(b)
        S = np.sqrt(b).sum(); G = np.sqrt(np.prod(b))
        lim = 2 * np.sqrt(S * G) / (S + G)
        tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
        for a, T in zip(al, tb.T):
            tphi = t1 / rho_alpha(a)
            rows.append([name, *b, a, t1, tphi, T, (tphi - t1) / (T - t1), tphi / T, lim, "FLOAT"])
    write("F4_C11_sufficient_fraction", ["triple", "beta12", "beta13", "beta23", "alpha", "T1", "T_Phi=T1/rho_alpha", "T_alpha",
                                         "certified_fraction_(TPhi-T1)/(Talpha-T1)", "TPhi_over_Talpha", "limit_alpha_to_1_2sqrt(SG)/(S+G)", "evidence"], rows,
          "Fraction of the exact genuinely fractional band [T_1, T_alpha) certified by the C-11 scalar condition "
          "Phi > rho_alpha (equivalently kappa < T_1/rho_alpha). The alpha -> 1 limit 2 sqrt(SG)/(S+G) <= 1 "
          "(S = sum sqrt beta, G = sqrt(prod beta)) is the Wave-1 symbolic result. FLOAT rows.")


# ----------------------------------------------------------------- F5 ecological boundaries

def f5():
    al = alpha_dense()
    rows = []
    for name, b in TRIPLES.items():
        b = np.array(b); t1 = T1(b); s = b.sum(); G = np.prod(1 - b)
        tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
        for a, T in zip(al, tb.T):
            rows.append([name, *b, a, s - 2, s - 2 - t1, s - 2 - T, T - t1, (2 * np.sqrt(G) if G > 0 else 0.0), "FLOAT"])
    write("F5_L3_alpha_boundaries", ["triple", "beta12", "beta13", "beta23", "alpha", "L3_at_kappa0", "L3_cain_boundary",
                                     "L3_fractional_boundary", "band_width_in_L3", "realizability_2sqrtG_if_G>0", "evidence"], rows,
          "Exact C-13 phase boundaries in the (L3, alpha) plane at fixed pair-loop triple: kappa = sum(beta) - 2 - L3; "
          "classical D-stable iff L3 > sum(beta)-2-T_1; genuinely fractional iff sum(beta)-2-T_alpha < L3 < sum(beta)-2-T_1; "
          "for alpha <= 2/3 the lower boundary is -infinity. Real matrices require |L3| >= 2 sqrt(G) when G = prod g_ij > 0 "
          "(automatic above the Cain boundary, C-15 Thm 4). FLOAT rows.")


# ----------------------------------------------------------------- F6 pair-loop sensitivity surfaces

def f6():
    g = np.linspace(-6, 0.95, 120)
    G12, G13 = np.meshgrid(g, g, indexing="ij")
    rows = []
    for a in (0.75, 0.9, 0.99):
        for g23 in (0.0, -2.0, 0.5):
            beta = np.stack([1 - G12.ravel(), 1 - G13.ravel(), np.full(G12.size, 1 - g23)], 1)
            tb = threshold_batch(beta, a)
            t = a * np.pi / 2; u, K = np.cos(t), -np.sin(3 * t) / np.sin(t)
            B = beta[:, 0] * tb.x[:, 0] * tb.x[:, 1] + beta[:, 1] * tb.x[:, 0] * tb.x[:, 2] + beta[:, 2] * tb.x[:, 1] * tb.x[:, 2]
            h, h1, _ = h_derivs(B, u, K)
            dT = np.stack([h1 / tb.x[:, 2], h1 / tb.x[:, 1], h1 / tb.x[:, 0]], 1)
            E = B * h1 / h
            for i in range(beta.shape[0]):
                rows.append([a, g23, G12.ravel()[i], G13.ravel()[i], *beta[i], tb.T[i], *dT[i], *(beta[i] * dT[i] / tb.T[i]), E[i], "FLOAT"])
    write("F6_pairloop_sensitivity", ["alpha", "g23", "g12", "g13", "beta12", "beta13", "beta23", "T_alpha", "dT_dbeta12", "dT_dbeta13", "dT_dbeta23",
                                      "logelast_beta12", "logelast_beta13", "logelast_beta23", "E_at_Bstar", "evidence"], rows,
          "C-15 exact sensitivities dT_alpha/dbeta_ij = h'_alpha(B*)/x_k* (> 0: strict pair-loop monotonicity, C-13 §7) "
          "and log-elasticities d log T/d log beta_ij = [1+(2E-3)(1-2x_k*)]/2 (sum = E in (0,3/2)) over the (g12,g13) pair-loop "
          "plane (g = 1 - beta; g<0 antagonistic, 0<g<1 mutualistic/competitive) for fixed alpha and g23. FLOAT rows.")


# ----------------------------------------------------------------- F8 / F9 (HP)

def _f8_job(args):
    name, b = args
    mp.mp.dps = 50
    bm = [mp.mpf(v) for v in b]
    t1, C = mp_T1(bm), mp_rate_constant(bm)
    out = []
    for k in range(1, 11):
        eps = mp.mpf(10) ** -k
        T = threshold_mp([repr(float(v)) for v in b], 1 - eps, dps=45)["T"]
        out.append([name, *b, k, mp.nstr(eps, 5), mp.nstr(t1, 25), mp.nstr(C, 25), mp.nstr(T, 35), mp.nstr((T - t1) / eps, 25),
                    mp.nstr((T - t1) / (C * eps), 20), mp.nstr((T - t1 - C * eps) / eps ** 2, 15), "HP(45 digits)"])
    return out


def _f9_job(args):
    name, b = args
    mp.mp.dps = 60
    bm = [mp.mpf(v) for v in b]
    out = []
    for k in range(1, 11):
        a = mp.mpf(2) / 3 + mp.mpf(10) ** -k
        u, K = mp_uk(a)
        T = threshold_mp([repr(float(v)) for v in b], a, dps=55)["T"]
        out.append([name, *b, k, mp.nstr(a, 25), mp.nstr(K, 15), mp.nstr(T, 35), mp.nstr(T * K ** 3 / 27, 20),
                    mp.nstr((T * K ** 3 - 27) / K, 15), mp.nstr(9 * sum(bm) - 27, 15), "HP(55 digits)"])
    return out


def f8_f9(P):
    jobs = list(TRIPLES.items())
    r8 = [r for rr in P.map(_f8_job, jobs) for r in rr]
    r9 = [r for rr in P.map(_f9_job, jobs) for r in rr]
    write("F8_classical_asymptotic", ["triple", "beta12", "beta13", "beta23", "k", "1-alpha", "T1", "C_beta", "T_alpha",
                                      "(T-T1)/(1-alpha)", "(T-T1)/(C(1-alpha))", "D_estimate=(T-T1-C eps)/eps^2", "evidence"], r8,
          "C-14 classical-order asymptotic T_alpha - T_1 ~ C(beta)(1-alpha), C = pi(S^{5/2}/sqrt G + S^{3/2} sqrt G): the ratio "
          "(T-T1)/(C(1-alpha)) -> 1 linearly in (1-alpha); D is the second-order coefficient estimate. HP rows (45 digits).")
    write("F9_low_order_blowup", ["triple", "beta12", "beta13", "beta23", "k", "alpha=2/3+1e-k", "K=1-4cos^2(alpha pi/2)", "T_alpha",
                                  "T*K^3/27", "(T*K^3-27)/K", "9*sum(beta)-27", "evidence"], r9,
          "C-15 Theorem 3 low-order blow-up T_alpha = 27/K^3 + (9 sum beta - 27)/K^2 + O(1/K) as alpha -> 2/3+: "
          "T K^3/27 -> 1 and (T K^3 - 27)/K -> 9 sum(beta) - 27. HP rows (55 digits).")


def previews():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows = list(csv.DictReader(open(os.path.join(FIG, "F1_T_ratio_vs_alpha", "F1_T_ratio_vs_alpha.csv"))))
    fig, ax = plt.subplots(figsize=(5, 3.5))
    for name in list(TRIPLES)[:6]:
        rr = [r for r in rows if r["triple"] == name]
        ax.semilogy([float(r["alpha"]) for r in rr], [float(r["T_alpha_over_T1"]) for r in rr], label=name[:22], lw=1)
    ax.set_xlabel("alpha"); ax.set_ylabel("T_alpha / T_1"); ax.legend(fontsize=6); fig.tight_layout()
    fig.savefig(os.path.join(FIG, "preview", "F1_preview.png"), dpi=110); plt.close(fig)
    rows = list(csv.DictReader(open(os.path.join(FIG, "F6_pairloop_sensitivity", "F6_pairloop_sensitivity.csv"))))
    rr = [r for r in rows if r["alpha"] == "0.9" and r["g23"] == "0"]
    n = int(round(np.sqrt(len(rr))))
    Z = np.array([float(r["logelast_beta12"]) for r in rr]).reshape(n, n)
    X = np.array([float(r["g12"]) for r in rr]).reshape(n, n); Y = np.array([float(r["g13"]) for r in rr]).reshape(n, n)
    fig, ax = plt.subplots(figsize=(4.5, 3.8))
    cs = ax.contourf(X, Y, Z, 20); fig.colorbar(cs, label="d log T / d log beta12 (alpha=0.9, g23=0)")
    ax.set_xlabel("g12"); ax.set_ylabel("g13"); fig.tight_layout()
    fig.savefig(os.path.join(FIG, "preview", "F6_preview.png"), dpi=110); plt.close(fig)


def main():
    T = Timer()
    with pool(10) as P:
        log("F1-F3, F7"); f1_f2_f3_f7()
        log("F4"); f4()
        log("F5"); f5()
        log("F6"); f6()
        log("F8, F9"); f8_f9(P)
    previews()
    index = stamp({"git_sha": git_sha(), "script": SCRIPT, "families": sorted(d for d in os.listdir(FIG) if d.startswith("F")),
                   "evidence_labels": {"F1-F7": "FLOAT (+CERTIFIED anchors in F1_certified_anchors.csv)", "F8": "HP 45 digits", "F9": "HP 55 digits"},
                   "wall_seconds": T()})
    dump("FIGURE_DATA/INDEX.json", index)
    with open(os.path.join(FIG, "README.md"), "w") as f:
        f.write("# Figure-source datasets (Wave 2, P5)\n\nEach subdirectory Fk contains the CSV source, a README with the mathematical purpose, "
                "the generating script and commit, and an `evidence` column per row (FLOAT / HP / CERTIFIED). "
                "Preview PNGs in `preview/` are QA only.\n\n" + "\n".join(f"- {d}" for d in index["families"]) + "\n")


if __name__ == "__main__":
    main()

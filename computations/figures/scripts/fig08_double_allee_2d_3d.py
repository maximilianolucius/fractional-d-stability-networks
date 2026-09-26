"""FIG-08 — exact 2D/3D Double-Allee contrast.

(a) 2D model (C-07 / DA-12): in the (X, m) plane for fixed a, K the fractional-only mechanism is the single curve
    m = m_c(X) = (X^2+2aX-Ka)/(K+a) (g'_DA(X)=0): codimension one; below classical, above unstable.
(b) 3D IGP model: (m, K) slice of the biological parameter space classified by the exact C-10 criterion
    (coexistence solved exactly, T_alpha = exact C-10 minimum); the certified m-interval [0.2005, 0.45] at K=1.1
    (CERTIFIED INTERVAL, Audit 1) is overlaid.  The fractional-only region is open.
"""
import json, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import figstyle as S
from fdsn.double_allee import Params, chief_witness, coexistence_equilibria, reduced_matrix
from fdsn.c10_threshold import T1, invariants_batch, threshold_batch

S.setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
# (a)
a, K = 0.5, 1.1
X = np.linspace(0.05, K, 300); mc = (X ** 2 + 2 * a * X - K * a) / (K + a)
ax1.fill_between(X, np.maximum(mc, 0), X, where=X > np.maximum(mc, 0), color=S.NOGO, alpha=0.12, lw=0)
ax1.fill_between(X, 0, np.clip(mc, 0, None), color=S.CLAS, alpha=0.18, lw=0)
ok = mc > 0
ax1.plot(X[ok], mc[ok], color=S.FRAC, lw=S.LW_THM, label=r"$m=m_c(X)$: $g_{DA}'(X)=0$")
ax1.plot(X, X, color=S.NDARK, lw=S.LW_AUX, ls=":"); ax1.text(0.52, 0.56, "$m=X$", fontsize=7, color=S.NDARK, rotation=48)
ax1.set_xlim(0, K); ax1.set_ylim(0, 0.9); ax1.set_xlabel(r"prey equilibrium $X=d/p$"); ax1.set_ylabel(r"Allee threshold $m$")
ax1.text(0.85, 0.15, "classical\n$g_{DA}'(X)<0$", color=S.CLAS, fontsize=7.5, ha="center")
ax1.text(0.35, 0.28, "not in $\\mathcal{F}_\\alpha$\n$g_{DA}'(X)>0$", color=S.NOGO, fontsize=7.5, ha="center")
ax1.annotate("fractional-only: codimension one\n$m_c=(X^2+2aX-Ka)/(K+a)$", xy=(0.8, (0.8 ** 2 + 2 * a * 0.8 - K * a) / (K + a)), xytext=(0.30, 0.74), fontsize=7, color=S.FRAC,
             arrowprops=dict(arrowstyle="-", lw=0.7, color=S.FRAC))
ax1.set_title(rf"2D double-Allee model ($a={a}$, $K={K}$)", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax1, "(a)")
# (b) (m, K) slice for the 3D model
P0 = chief_witness(); base = np.array(P0.as_list())
ms = np.linspace(0.02, 0.66, 130); Ks = np.linspace(1.02, 1.30, 120)
cls = np.full((Ks.size, ms.size), 3, dtype=int)     # 0 classical, 1 frac-only, 2 unstable, 3 infeasible
for i, Kv in enumerate(Ks):
    for j, mv in enumerate(ms):
        v = base.copy(); v[1] = Kv; v[3] = mv
        eqs = coexistence_equilibria(Params(*v))
        if not eqs:
            continue
        e = eqs[0]; B = np.array(reduced_matrix(e["X"], e["Y"], e["Z"], Params(*v)))
        p, mm, q, beta, kappa = invariants_batch(B[None])
        if not (mm.min() > 0 and q[0] > 0 and p.min() > 0):
            cls[i, j] = 2; continue
        t1 = T1(beta[0]); Ta = threshold_batch(beta, 0.9).T[0]
        cls[i, j] = 0 if kappa[0] < t1 else (1 if kappa[0] < Ta else 2)
cmap = ListedColormap([S.CLAS, S.FRAC, S.NOGO, S.NLIGHT])
ax2.pcolormesh(ms, Ks, cls, cmap=cmap, vmin=-0.5, vmax=3.5, shading="nearest", alpha=0.55, rasterized=True)
ax2.plot([0.2005, 0.45], [1.1, 1.1], color=S.BIO, lw=3.2, solid_capstyle="butt", label="certified $m$-interval ($K=1.1$)")
ax2.plot([0.2], [1.1], marker="o", ms=5, color=S.CLAS, mec="black", mew=0.5, ls="none", label="$m_0$ (exact crossing)")
ax2.plot([0.35], [1.1], marker="D", ms=5, color=S.BIO, mec="black", mew=0.5, ls="none", label="anchor $m=0.35$")
ax2.set_xlim(ms[0], ms[-1]); ax2.set_ylim(Ks[0], Ks[-1]); ax2.set_xlabel(r"Allee threshold $m$"); ax2.set_ylabel(r"carrying capacity $K$")
ax2.text(0.09, 1.25, "classical", color=S.CLAS, fontsize=7.5, fontweight="bold"); ax2.text(0.30, 1.25, "fractional-only (open)", color=S.FRAC, fontsize=7.5, fontweight="bold")
ax2.text(0.55, 1.05, "infeasible /\nnot strict-P", color=S.NDARK, fontsize=6.5, ha="center")
ax2.legend(loc="lower left", fontsize=6.3)
ax2.set_title(r"3D IGP model, $\alpha=0.9$: $(m,K)$ slice", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
np.savetxt(os.path.join(S.DATA, "fig08_mK_classes.csv"), cls, fmt="%d", delimiter=",", header="rows K in linspace(1.02,1.30,120); cols m in linspace(0.02,0.66,130); 0 classical,1 frac-only,2 unstable/non-strict-P,3 infeasible", comments="")
S.export(fig, "fig08_double_allee_2d_3d", {
    "claims": ["DA-12 (2D codimension one)", "DA-08 (3D open region)", "C-07", "C-10"],
    "formulas": ["m_c=(X^2+2aX-Ka)/(K+a)", "classification: kappa<T1 classical; T1<kappa<T_alpha fractional-only; else not in F_alpha"],
    "parameters": {"panel_a": {"a": a, "K": K}, "panel_b": {"alpha": 0.9, "fixed_parameters": dict(zip(["a", "K", "r", "m", "q1", "q2", "h", "e1", "e2", "e3", "mu1", "mu2", "c1", "c2"], base.tolist())),
                   "grid": "m in [0.02,0.66] x 130, K in [1.02,1.30] x 120", "certified_interval": "[0.2005, 0.45] at K=1.1 (computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json)"}},
    "objects": {"m_c curve": "CLOSED-FORM BOUNDARY", "(m,K) classification": "NUMERICAL EVALUATION OF EXACT FORMULAS (per grid point: exact coexistence, exact C-10 threshold)",
                "green segment": "CERTIFIED INTERVAL", "m0": "CERTIFIED COMPUTATION (HP root)"},
    "data": "computations/figures/data/fig08_mK_classes.csv"})

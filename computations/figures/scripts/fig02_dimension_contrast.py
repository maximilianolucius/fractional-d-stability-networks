"""FIG-02 — dimension two versus dimension three (THEOREM VISUALIZATION: C-07 / C-09 / C-10).

(a) 2x2: with a22 = 0 (the double-Allee 2D reduced matrix has this form) and det > 0, C-07 gives
    F_alpha iff a11 <= 0, classical D-stability iff a11 < 0: the fractional-only set is the line a11 = 0
    (codimension one); (b) 3x3 symmetric slice beta=(b,b,b): open band T_1(b,b,b)=9b < kappa < T_alpha(b,b,b)=27 h_alpha(b/3).
"""
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S
from fdsn.c10_threshold import h_alpha

S.setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
# (a) 2D: axes a11 (= g'_DA(X)) horizontal, det = pq vertical (>0)
ax1.set_xlim(-1, 1); ax1.set_ylim(0, 1)
ax1.fill_betweenx([0, 1], -1, 0, color=S.CLAS, alpha=0.18, lw=0)
ax1.fill_betweenx([0, 1], 0, 1, color=S.NOGO, alpha=0.12, lw=0)
ax1.axvline(0, color=S.FRAC, lw=S.LW_THM)
ax1.set_xlabel(r"$a_{11}=g_{DA}'(X)$"); ax1.set_ylabel(r"$\det B_2=pq>0$")
ax1.set_yticks([]); ax1.set_xticks([-1, 0, 1]); ax1.set_xticklabels([r"$<0$", "0", r"$>0$"])
ax1.text(-0.5, 0.55, "classical\nD-stable", ha="center", color=S.CLAS, fontsize=8)
ax1.text(0.5, 0.55, "not in $\\mathcal{F}_\\alpha$", ha="center", color=S.NOGO, fontsize=8)
ax1.annotate("fractional-only:\n$a_{11}=0$ (codimension one)", xy=(0, 0.25), xytext=(0.35, 0.18), color=S.FRAC, fontsize=7.5,
             arrowprops=dict(arrowstyle="-", color=S.FRAC, lw=0.8))
ax1.set_title(r"$n=2$ (C-07): empty interior", fontsize=8.5, color=S.NDARK, pad=2)
S.panel_label(ax1, "(a)")
# (b) 3D symmetric slice
alpha = 0.9
b = np.logspace(-1, 1, 400)
T1 = 9 * b; Ta = 27 * h_alpha(b / 3, alpha)
ax2.fill_between(b, T1, Ta, color=S.FRAC, alpha=0.35, lw=0)
ax2.fill_between(b, 1e-3, T1, color=S.CLAS, alpha=0.18, lw=0)
ax2.fill_between(b, Ta, 1e4, color=S.NOGO, alpha=0.12, lw=0)
ax2.plot(b, T1, color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$\kappa=T_1(\beta)$")
ax2.plot(b, Ta, color=S.FRAC, lw=S.LW_THM, label=r"$\kappa=T_\alpha(\beta)$")
ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.set_xlim(0.1, 10); ax2.set_ylim(0.5, 2000)
ax2.set_xlabel(r"$b$  ($\beta_{12}=\beta_{13}=\beta_{23}=b$)"); ax2.set_ylabel(r"$\kappa$")
ax2.text(1.0, 100, r"open band $T_1<\kappa<T_\alpha$", color=S.FRAC, fontsize=8, ha="center")
ax2.text(3, 6, "classical D-stable", color=S.CLAS, fontsize=7.5, ha="center")
ax2.text(0.2, 400, "not in $\\mathcal{F}_\\alpha$", color=S.NOGO, fontsize=7.5, ha="center")
ax2.legend(loc="lower right", fontsize=7)
ax2.set_title(rf"$n=3$ (C-09/C-10), $\alpha={alpha}$: nonempty interior", fontsize=8.5, color=S.NDARK, pad=2)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.32)
S.save_data("fig02_symmetric_slice.csv", {"array": np.column_stack([b, T1, Ta]), "header": "b,T1=9b,T_alpha=27h(b/3)"})
S.export(fig, "fig02_dimension_contrast", {
    "claims": ["C-07", "C-09", "C-10 (symmetric slice)", "C-15 Cor. 1"],
    "formulas": ["2x2: F_alpha iff det>0, a11<=0, a22<=0 (C-07); D_H iff additionally a11+a22<0", "T_1(b,b,b)=9b", "T_alpha(b,b,b)=27 h_alpha(b/3)"],
    "parameters": {"alpha": alpha, "b_range": [0.1, 10]},
    "objects": {"a11=0 line": "EXACT THEOREM CURVE", "T_1 curve": "CLOSED-FORM BOUNDARY", "T_alpha curve": "CLOSED-FORM BOUNDARY (27 h_alpha(b/3), C-15)"},
    "data": "computations/figures/data/fig02_symmetric_slice.csv"})

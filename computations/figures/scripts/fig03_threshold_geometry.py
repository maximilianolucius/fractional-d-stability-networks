"""FIG-03 — exact C-10 threshold geometry (THEOREM-GRADE).

(a) symmetric slice beta=(b,b,b): T_1 = 9b (closed form), T_alpha = 27 h_alpha(b/3) (closed form, C-15 Cor. 1)
    for three orders; (b) asymmetric slice beta=(b, 1.5, 3): T_alpha from the exact C-10 variational formula
    (unique minimiser, C-15), T_1 = (sqrt b + sqrt 1.5 + sqrt 3)^2; certified anchor points (interval brackets)
    marked with squares.  No diagonal sampling anywhere.
"""
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import figstyle as S
from fdsn.c10_threshold import T1, h_alpha, threshold_batch
from fdsn.interval_cert import certify_threshold_logit

S.setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
b = np.logspace(-1, 1, 300)
rows = [b, 9 * b]
for alpha, ls in ((0.7, ":"), (0.8, "-."), (0.9, "-")):
    Ta = 27 * h_alpha(b / 3, alpha); rows.append(Ta)
    ax1.plot(b, Ta, color=S.FRAC, lw=S.LW_THM if alpha == 0.9 else S.LW_CMP, ls=ls)
    ax1.text(10.5, Ta[-1], rf"$\alpha={alpha}$", color=S.FRAC, fontsize=7, va="center")
ax1.plot(b, 9 * b, color=S.CLAS, lw=S.LW_THM, ls="--"); ax1.text(10.5, 90, r"$T_1$", color=S.CLAS, fontsize=7.5, va="center")
ax1.fill_between(b, 9 * b, 27 * h_alpha(b / 3, 0.9), color=S.FRAC, alpha=0.25, lw=0)
ax1.set_xscale("log"); ax1.set_yscale("log"); ax1.set_xlim(0.1, 13); ax1.set_ylim(0.5, 3e4)
ax1.set_xlabel(r"$b$  (symmetric slice $\beta=(b,b,b)$)"); ax1.set_ylabel(r"$\kappa$")
ax1.text(0.4, 1.2e3, r"$T_\alpha(b,b,b)=27\,h_\alpha(b/3)$", color=S.FRAC, fontsize=7.5)
ax1.text(0.13, 0.7, r"$T_1=9b$", color=S.CLAS, fontsize=7.5)
S.panel_label(ax1, "(a)")
S.save_data("fig03_symmetric_slice.csv", {"array": np.column_stack(rows), "header": "b,T1,T_0.7,T_0.8,T_0.9"})
# (b) asymmetric slice
alpha = 0.9
beta = np.stack([b, np.full_like(b, 1.5), np.full_like(b, 3.0)], 1)
tb = threshold_batch(beta, alpha)
t1 = T1(beta)
ax2.plot(b, t1, color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$T_1(\beta)$ (closed form)")
ax2.plot(b, tb.T, color=S.FRAC, lw=S.LW_THM, label=r"$T_{0.9}(\beta)$ (exact C-10 minimum)")
ax2.fill_between(b, t1, tb.T, color=S.FRAC, alpha=0.25, lw=0)
# certified anchors
cert = []
for bb in ("0.2", "1", "5"):
    c = certify_threshold_logit([bb, "1.5", "3"], "0.9", dps=40)
    cert.append({"b": float(bb), "L": mp.nstr(c["L"], 30), "U": mp.nstr(c["U"], 30), "rel_width": mp.nstr(c["rel_width"], 4)})
    ax2.plot(float(bb), float(c["L"]), marker="s", ms=4.5, color=S.FRAC, mec="black", mew=0.5, ls="none")
ax2.plot([], [], marker="s", ms=4.5, color=S.FRAC, mec="black", mew=0.5, ls="none", label="certified interval (width $<10^{-30}$)")
ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.set_xlim(0.1, 10); ax2.set_ylim(5, 300)
ax2.set_xlabel(r"$\beta_{12}$  (slice $\beta_{13}=1.5,\ \beta_{23}=3$)"); ax2.set_ylabel(r"$\kappa$")
ax2.legend(loc="lower right", fontsize=6.8)
ax2.text(0.13, 8.5, "classical", color=S.CLAS, fontsize=7.5); ax2.text(0.13, 150, "not in $\\mathcal{F}_{0.9}$", color=S.NOGO, fontsize=7.5)
ax2.text(1.5, 40, "fractional-only", color=S.FRAC, fontsize=7.5)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
S.save_data("fig03_asymmetric_slice.csv", {"array": np.column_stack([b, t1, tb.T, tb.x]), "header": "beta12,T1,T_0.9,x1*,x2*,x3*"})
S.save_data("fig03_certified_anchors.json", cert)
S.export(fig, "fig03_threshold_geometry", {
    "claims": ["C-10 Thm 1", "C-10 §6-7 (T_1, band)", "C-15 Cor. 1 (symmetric closed form)", "C-15 Thm 1 (unique minimiser)"],
    "formulas": ["T_1=(sum sqrt beta_ij)^2", "T_alpha(b,b,b)=27 h_alpha(b/3)", "T_alpha(beta)=min_x h_alpha(B_beta(x))/(x1x2x3)"],
    "parameters": {"panel_a_alphas": [0.7, 0.8, 0.9], "panel_b": {"alpha": 0.9, "beta13": 1.5, "beta23": 3.0}},
    "objects": {"T_1 curves": "CLOSED-FORM BOUNDARY", "panel (a) T_alpha": "CLOSED-FORM BOUNDARY", "panel (b) T_alpha": "EXACT THEOREM CURVE (numerical evaluation of the exact variational formula, unique minimiser)",
                "squares": "CERTIFIED INTERVAL (interval arithmetic, conditional on C-15 Thm 1)"},
    "data": ["computations/figures/data/fig03_symmetric_slice.csv", "computations/figures/data/fig03_asymmetric_slice.csv", "computations/figures/data/fig03_certified_anchors.json"]})

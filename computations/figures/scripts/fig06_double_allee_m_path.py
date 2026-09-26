"""FIG-06 — Double-Allee m-path through exact invariant space (THEOREM-GRADE; data from branch_data.py).

(a) exact Cain gap G_1(m)=kappa-T_1 and fractional margin G_alpha(m)=T_alpha-kappa along the coexistence branch
    (all other parameters fixed; alpha=0.9); m0 (HP root), one classical point, the recommended interior anchor;
(b) the path in the invariant slice (beta12=beta13, beta23=C0 fixed): straight line kappa=C0+(A0+B0+E0)t,
    beta12=1+A0 t, against the exact boundaries T_1 and T_0.9 of that slice.
"""
import json, os
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S
from fdsn.c10_threshold import T1, threshold_batch

S.setup()
D = json.load(open(os.path.join(S.DATA, "branch_alpha0.9.json")))
br = D["branch"]; m = np.array([r["m"] for r in br]); kap = np.array([r["kappa"] for r in br]); t1 = np.array([r["T1"] for r in br]); ta = np.array([r["T_alpha"] for r in br])
beta = np.array([r["beta"] for r in br])
m0 = float(D["m0_hp"]); mA = 0.35; mC = 0.12
cand = D["candidates"]["0.35"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
ax1.axhline(0, color=S.NDARK, lw=S.LW_AUX)
ax1.plot(m, kap - t1, color=S.CLAS, lw=S.LW_THM, ls="--")
ax1.plot(m, ta - kap, color=S.FRAC, lw=S.LW_THM)
ax1.fill_between(m, 0, np.maximum(kap - t1, 0), where=(kap - t1) > 0, color=S.FRAC, alpha=0.2, lw=0)
ax1.axvline(m0, color=S.NDARK, lw=S.LW_AUX, ls=":")
ax1.plot([m0], [0], marker="o", ms=5, color=S.CLAS, mec="black", mew=0.5, zorder=5)
ax1.annotate(r"$m_0=0.2$ (exact crossing)", xy=(m0, 0), xytext=(0.27, -6), fontsize=7, color=S.NDARK, arrowprops=dict(arrowstyle="-", lw=0.7, color=S.NDARK))
iC = int(np.argmin(np.abs(m - mC))); iA = int(np.argmin(np.abs(m - mA)))
ax1.plot([mC], [kap[iC] - t1[iC]], marker="s", ms=5, color=S.CLAS, mec="black", mew=0.5, zorder=5)
ax1.annotate("classical\n$m=0.12$", xy=(mC, kap[iC] - t1[iC]), xytext=(0.03, 6), fontsize=7, color=S.CLAS, arrowprops=dict(arrowstyle="-", lw=0.7, color=S.CLAS))
ax1.plot([mA], [kap[iA] - t1[iA]], marker="D", ms=5, color=S.BIO, mec="black", mew=0.5, zorder=5)
ax1.plot([mA], [ta[iA] - kap[iA]], marker="D", ms=5, color=S.BIO, mec="black", mew=0.5, zorder=5)
ax1.annotate("certified anchor\n$m=0.35$", xy=(mA, kap[iA] - t1[iA]), xytext=(0.20, 8.5), fontsize=7, color=S.BIO, arrowprops=dict(arrowstyle="-", lw=0.7, color=S.BIO))
ax1.set_xlim(0, 0.66); ax1.set_ylim(-10, 26); ax1.set_xlabel(r"Allee threshold $m$ (all other parameters fixed)"); ax1.set_ylabel("gap")
ax1.text(0.03, 23.6, r"$G_\alpha(m)=T_\alpha-\kappa$ (fractional margin)", color=S.FRAC, fontsize=7)
ax1.text(0.47, 13.5, r"$G_1(m)=\kappa-T_1$" + "\n(Cain gap)", color=S.CLAS, fontsize=7, ha="center")
ax1.text(0.60, -9.3, "feasibility\nlost", fontsize=6.5, color=S.NOGO, ha="center")
ax1.text(0.09, -8.5, "classical ($m<m_0$)", color=S.CLAS, fontsize=7, ha="center"); ax1.text(0.40, -8.5, "fractional-only ($m>m_0$)", color=S.FRAC, fontsize=7, ha="center")
S.panel_label(ax1, "(a)")
# (b) invariant slice: beta12 = beta13 = b, beta23 = C0
C0 = D["path_constants"]["C0"]; A0 = D["path_constants"]["A0"]; B0 = D["path_constants"]["B0"]; E0 = D["path_constants"]["E0"]
b = np.linspace(1.3, 3.3, 300)
bb = np.stack([b, b, np.full_like(b, C0)], 1)
T1c = T1(bb); Tac = threshold_batch(bb, 0.9).T
ax2.plot(b, T1c, color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$T_1$"); ax2.plot(b, Tac, color=S.FRAC, lw=S.LW_THM, label=r"$T_{0.9}$")
ax2.fill_between(b, T1c, Tac, color=S.FRAC, alpha=0.2, lw=0)
ax2.plot(beta[:, 0], kap, color=S.BIO, lw=S.LW_CMP, label=r"$m$-path: $\kappa=C_0+(A_0+B_0+E_0)t$")
for mm, mk, col in ((mC, "s", S.CLAS), (m0, "o", S.CLAS), (mA, "D", S.BIO), (0.6, "^", S.BIO)):
    i = int(np.argmin(np.abs(m - mm))); ax2.plot(beta[i, 0], kap[i], marker=mk, ms=5, color=col, mec="black", mew=0.5, ls="none", zorder=5)
    ax2.annotate(f"$m={mm:.2g}$", xy=(beta[i, 0], kap[i]), xytext=(6, -10), textcoords="offset points", fontsize=6.5, color=col)
i1, i2 = int(np.argmin(np.abs(m - 0.45))), int(np.argmin(np.abs(m - 0.5)))
ax2.annotate("", xy=(beta[i2, 0], kap[i2]), xytext=(beta[i1, 0], kap[i1]), arrowprops=dict(arrowstyle="-|>", color=S.BIO, lw=1.2))
ax2.set_xlim(1.4, 3.3); ax2.set_ylim(10, 60); ax2.set_xlabel(r"$\beta_{12}=\beta_{13}=1+A_0t$   ($\beta_{23}=C_0=2$ fixed)"); ax2.set_ylabel(r"$\kappa$")
ax2.legend(loc="upper left", fontsize=6.5)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
S.export(fig, "fig06_double_allee_m_path", {
    "claims": ["DA-09 (ds/dm<0)", "DA-10 (unique transverse crossing)", "DA-11 (prescribed m0)", "C-10", "C-13"],
    "formulas": ["t=1/s(m)", "beta12=1+A0 t, beta13=1+B0 t, beta23=C0", "kappa=C0+(A0+B0+E0)t", "G1=kappa-T1", "G_alpha=T_alpha-kappa"],
    "parameters": {"alpha": 0.9, "biological_parameters": D["params"], "path_constants": D["path_constants"], "m0_hp": D["m0_hp"], "G1(m0=0.2)": D["G1_at_m0=0.2"],
                   "feasible_m_range": D["feasible_range"], "classical_point": mC, "anchor": mA},
    "objects": {"G1, G_alpha, path": "EXACT THEOREM CURVE (numerical evaluation of exact formulas along the branch; T_alpha = exact C-10 minimum)",
                "m0 marker": "CERTIFIED COMPUTATION (HP bisection, 60 digits: G1(0.2) = -5e-60)", "anchor marker": "CERTIFIED INTERVAL (see fig07 metadata)",
                "T_1, T_0.9 in (b)": "CLOSED-FORM BOUNDARY / EXACT THEOREM CURVE"},
    "data": "computations/figures/data/branch_alpha0.9.json"})

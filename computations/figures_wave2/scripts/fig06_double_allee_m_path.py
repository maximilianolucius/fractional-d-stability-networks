"""FIG-06 (Wave 2) — Double-Allee m-path for the selected design (THEOREM-GRADE; data: select_design.py).
Panel (a): G_1(m)=kappa-T_1 and G_alpha(m)=T_alpha-kappa along the coexistence branch; markers: classical point,
exact crossing m0 (60-digit), certified anchor; feasibility endpoint indicated.  Panel (b): path in the invariant
slice (beta12, kappa) with beta13, beta23 evaluated along the path (all exact formulas), against T_1 and T_0.9 of
the slice beta=(beta12, beta13(m), beta23) -- since beta13 also moves, the boundaries are drawn as functions of m
mapped to beta12 (exact pointwise), i.e. the curves are the boundaries seen along the path.
"""
import json, os
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S

S.setup()
D = json.load(open(os.path.join(S.DATA, "design_selected.json")))
BR = json.load(open(os.path.join(S.DATA, "branch_wave2.json")))["branch"]
br = [r for r in BR if r["strictP"]]
m = np.array([r["m"] for r in br]); kap = np.array([r["kappa"] for r in br]); t1 = np.array([r["T1"] for r in br]); ta = np.array([r["T_alpha"] for r in br])
beta = np.array([r["beta"] for r in br])
m0 = float(D["m0_hp"]); mA = D["anchor_m"]; mC = D["classical_m"]; lo, hi = D["feasible_range"]
sel = (m >= lo - 1e-9) & (m <= hi + 1e-9)
m, kap, t1, ta, beta = m[sel], kap[sel], t1[sel], ta[sel], beta[sel]
# the branch ends where s -> 0+ (strict-P lost): kappa - T1 grows without bound there; show the window where the
# Cain gap stays below 4x its anchor value (the divergence is stated in the annotation, not plotted)
iA0 = int(np.argmin(np.abs(m - mA))); cap = 4 * (kap - t1)[iA0]
cut = int(np.argmax((kap - t1) > cap)) if np.any((kap - t1) > cap) else len(m)
m_end = m[cut - 1]
m, kap, t1, ta, beta = m[:cut], kap[:cut], t1[:cut], ta[:cut], beta[:cut]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
ax1.axhline(0, color=S.NDARK, lw=S.LW_AUX)
ax1.plot(m, kap - t1, color=S.CLAS, lw=S.LW_THM, ls="--")
ax1.plot(m, ta - kap, color=S.FRAC, lw=S.LW_THM)
ax1.fill_between(m, 0, np.maximum(kap - t1, 0), where=(kap - t1) > 0, color=S.FRAC, alpha=0.18, lw=0)
ax1.axvline(m0, color=S.NDARK, lw=S.LW_AUX, ls=":")
iC = int(np.argmin(np.abs(m - mC))); iA = int(np.argmin(np.abs(m - mA)))
ax1.plot([mC], [kap[iC] - t1[iC]], marker="s", ms=5, color=S.CLAS, mec="black", mew=0.5, zorder=5)
ax1.plot([m0], [0], marker="o", ms=5, color=S.CLAS, mec="black", mew=0.5, zorder=5)
ax1.plot([mA, mA], [kap[iA] - t1[iA], ta[iA] - kap[iA]], marker="D", ms=5, color=S.BIO, mec="black", mew=0.5, ls="none", zorder=5)
ymax = max((ta - kap).max(), (kap - t1).max()) * 1.12; ymin = (kap - t1).min() * 1.3
ax1.set_xlim(lo - 0.01, m_end + 0.06); ax1.set_ylim(ymin, ymax)
ax1.set_xlabel(r"Allee threshold $m$ (all other parameters fixed)"); ax1.set_ylabel("gap")
ax1.text(m[len(m) // 6], (ta - kap)[len(m) // 6] + 0.04 * ymax, r"$T_\alpha-\kappa$", color=S.FRAC, fontsize=7.5)
iL = int(np.argmin(np.abs(m - 0.5 * (m0 + mA)))); ax1.text(m[iL] + 0.012, (kap - t1)[iL] - 0.02 * ymax, r"$\kappa-T_1$", color=S.CLAS, fontsize=7.5, ha="left", va="top")
ax1.text(m0 + 0.008, ymin + 0.03 * (ymax - ymin), r"$m_0$", color=S.NDARK, fontsize=7.5, ha="left")
ax1.text(mC, kap[iC] - t1[iC] - 0.07 * ymax, "classical", color=S.CLAS, fontsize=7, ha="center")
ax1.text(mA, ta[iA] - kap[iA] + 0.04 * ymax, "anchor", color=S.BIO, fontsize=7, ha="center")
ax1.annotate("", xy=(m_end + 0.05, (kap - t1)[-1]), xytext=(m_end, (kap - t1)[-1]), arrowprops=dict(arrowstyle="-|>", color=S.CLAS, lw=1.0, ls="--"))
ax1.text(m_end + 0.055, (kap - t1)[-1], f"$s\\to0^+$\nat $m={hi:.3f}$", color=S.NOGO, fontsize=6.3, ha="left", va="center")
S.panel_label(ax1, "(a)")
# (b)
ax2.plot(beta[:, 0], t1, color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$T_1(\beta(m))$")
ax2.plot(beta[:, 0], ta, color=S.FRAC, lw=S.LW_THM, label=r"$T_{0.9}(\beta(m))$")
ax2.fill_between(beta[:, 0], t1, ta, color=S.FRAC, alpha=0.18, lw=0)
ax2.plot(beta[:, 0], kap, color=S.BIO, lw=S.LW_CMP, label=r"$\kappa(m)$ along the $m$-path")
for mm_, mk, col, lab in ((mC, "s", S.CLAS, "classical"), (m0, "o", S.CLAS, r"$m_0$"), (mA, "D", S.BIO, "anchor")):
    i = int(np.argmin(np.abs(m - mm_))); ax2.plot(beta[i, 0], kap[i], marker=mk, ms=5, color=col, mec="black", mew=0.5, ls="none", zorder=5)
    ax2.annotate(lab, xy=(beta[i, 0], kap[i]), xytext=(7, -3), textcoords="offset points", fontsize=6.5, color=col, va="top")
j1, j2 = int(0.55 * len(m)), int(0.62 * len(m))
ax2.annotate("", xy=(beta[j2, 0], kap[j2]), xytext=(beta[j1, 0], kap[j1]), arrowprops=dict(arrowstyle="-|>", color=S.BIO, lw=1.2))
ax2.set_xlabel(r"$\beta_{12}(m)=1+A_0/s(m)$"); ax2.set_ylabel(r"$\kappa$"); ax2.legend(loc="upper left", fontsize=6.5)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
S.export(fig, "fig06_double_allee_m_path", {
    "claims": ["DA-09", "DA-10", "DA-11", "C-10", "C-13"],
    "formulas": ["t=1/s(m); beta12=1+A0 t, beta13=1+B0 t, beta23=C0; kappa=C0+(A0+B0+E0)t", "G1=kappa-T1; G_alpha=T_alpha-kappa"],
    "parameters": {"alpha": 0.9, "design": D["design"], "biological_parameters": D["params"], "m0_hp": D["m0_hp"], "G1_at_m0": D["G1_at_m0"], "classical_point": mC, "anchor": mA, "feasible_range": D["feasible_range"]},
    "objects": {"curves": "EXACT THEOREM CURVE (exact formulas along the exactly solved branch; T_alpha = exact C-10 minimum)", "m0": "CERTIFIED COMPUTATION (60-digit root)", "anchor": "CERTIFIED INTERVAL (see fig07 metadata)"},
    "data": ["computations/figures_wave2/data/design_selected.json", "computations/figures_wave2/data/branch_wave2.json"]})

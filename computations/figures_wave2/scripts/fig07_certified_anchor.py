"""FIG-07 (Wave 2) — certified biological anchor, three panels.
(a) coexistence densities along m (log scale) with the anchor; (b) certified margins kappa-T1 and T_0.9-kappa with
interval-certified lower bounds at three m values (squares) and the certified m-interval (thick bar);
(c) spectrum of D*B at the worst positive diagonal (scale-invariant search): |arg| > 0.9 pi/2, Re > 0.
Numerical dynamics are NOT shown: all-D stability is the C-10 theorem, corroborated here only by the spectral angle.
"""
import json, math, os
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S

S.setup()
D = json.load(open(os.path.join(S.DATA, "design_selected.json")))
br = [r for r in json.load(open(os.path.join(S.DATA, "branch_wave2.json")))["branch"] if r["strictP"]]
lo, hi = D["feasible_range"]; mA = D["anchor_m"]; m0 = float(D["m0_hp"])
m = np.array([r["m"] for r in br]); sel = (m >= lo - 1e-9) & (m <= hi + 1e-9)
m = m[sel]; X = np.array([r["X"] for r in br])[sel]; Y = np.array([r["Y"] for r in br])[sel]; Z = np.array([r["Z"] for r in br])[sel]
kap = np.array([r["kappa"] for r in br])[sel]; t1 = np.array([r["T1"] for r in br])[sel]; ta = np.array([r["T_alpha"] for r in br])[sel]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(S.W2, S.W2 * 0.34))
for arr, lab, col in ((X, "$X$", S.BIO), (Y, "$Y$", S.NDARK), (Z, "$Z$", S.FRAC)):
    ax1.plot(m, arr, color=col, lw=S.LW_CMP); ax1.text(m[-1] + 0.01, arr[-1], lab, color=col, fontsize=7.5, va="center")
ax1.axvline(mA, color=S.BIO, lw=S.LW_AUX, ls=":"); ax1.axvline(m0, color=S.NDARK, lw=S.LW_AUX, ls=":")
ax1.set_yscale("log"); ax1.set_xlim(lo, hi + 0.06); ax1.set_xlabel(r"$m$"); ax1.set_ylabel("coexistence densities")
ax1.text(m0 + 0.01, ax1.get_ylim()[0] * 1.3, r"$m_0$", color=S.NDARK, fontsize=7, ha="left")
iA_ = int(np.argmin(np.abs(m - mA))); ax1.text(mA + 0.01, (Y[iA_] * Z[iA_]) ** 0.5, "anchor", color=S.BIO, fontsize=7, ha="left", va="center")
S.panel_label(ax1, "(a)")
ax2.plot(m, kap - t1, color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$\kappa-T_1$")
ax2.plot(m, ta - kap, color=S.FRAC, lw=S.LW_THM, label=r"$T_{0.9}-\kappa$")
ci = D["certified_m_interval"]
if ci["fully_certified"]:
    ax2.plot(ci["attempted"], [0, 0], color=S.BIO, lw=3.5, solid_capstyle="butt", label="certified $m$-range")
for k, c in D["certified_points"].items():
    if c["ok"]:
        mm_ = float(k)
        ax2.plot([mm_], [float(c["kappa_minus_T1_lo"])], marker="s", ms=4.5, color=S.CLAS, mec="black", mew=0.5, ls="none", zorder=5)
        ax2.plot([mm_], [float(c["T_alpha_L_minus_kappa_hi"])], marker="s", ms=4.5, color=S.FRAC, mec="black", mew=0.5, ls="none", zorder=5)
ax2.plot([], [], marker="s", ms=4.5, color="white", mec="black", mew=0.5, ls="none", label="certified bounds")
ax2.axvline(mA, color=S.BIO, lw=S.LW_AUX, ls=":")
ax2.set_xlim(lo, hi + 0.02); ax2.set_ylim(min(0, (kap - t1).min()) * 1.1, (ta - kap).max() * 1.15); ax2.set_xlabel(r"$m$"); ax2.set_ylabel("margin")
ax2.legend(fontsize=6.0, loc="center left", bbox_to_anchor=(0.0, 0.36), handlelength=1.5, frameon=False)
S.panel_label(ax2, "(b)")
ev = np.array(D["direct"]["eig_at_worst_d"]); th = 0.9 * math.pi / 2
R = 1.15 * np.abs(ev[:, 0] + 1j * ev[:, 1]).max()
ax3.set_aspect("equal"); ax3.set_xlim(-R * 1.15, R * 0.5); ax3.set_ylim(-R, R)
ax3.axvline(0, color=S.NDARK, lw=S.LW_AUX); ax3.axhline(0, color=S.NDARK, lw=S.LW_AUX)
for sgn in (1, -1):
    ax3.plot([0, R * np.cos(th)], [0, sgn * R * np.sin(th)], color=S.FRAC, lw=S.LW_THM)
ax3.fill_betweenx([-R, R], -R * 1.15, 0, color=S.CLAS, alpha=0.10, lw=0)
ax3.plot(ev[:, 0], ev[:, 1], marker="o", ms=5, color=S.NOGO, mec="black", mew=0.5, ls="none", zorder=5)
ang = D["direct"]["min_arg"]
ax3.text(-R * 1.1, R * 0.95, f"$\\min_{{D}}\\,\\min_i|\\arg\\lambda_i(DB)|$\n$={ang:.3f}>0.9\\pi/2={th:.3f}$\nand $\\mathrm{{Re}}\\,\\lambda>0$ (all $D$ searched)", fontsize=6.2, color=S.NDARK, va="top", ha="left")
ax3.set_xlabel(r"$\mathrm{Re}\,\lambda(D^*B)$"); ax3.set_ylabel(r"$\mathrm{Im}\,\lambda$")
S.panel_label(ax3, "(c)")
fig.subplots_adjust(wspace=0.42)
S.export(fig, "fig07_certified_anchor", {
    "claims": ["DA-08", "DA-11", "C-10", "C-11"],
    "anchor": {"m": mA, "design": D["design"], "biological_parameters": D["params"], "coexistence": D["anchor"], "margins": D["margins"], "densities": D["densities"],
               "conditioning": D["conditioning"], "direct": D["direct"], "certified_points": D["certified_points"], "certified_m_interval": D["certified_m_interval"]},
    "objects": {"(a),(b) curves": "EXACT THEOREM CURVE (exact formulas along the branch)", "squares / bar": "CERTIFIED INTERVAL (interval Newton, outward rounding, 50 digits; C-11 bound unconditional, C-10 bound conditional on C-15 Thm 1)",
                "(c) eigenvalues": "NUMERICAL CORROBORATION (scale-invariant search min|arg lambda| over positive diagonals)"},
    "data": ["computations/figures_wave2/data/design_selected.json", "computations/figures_wave2/data/branch_wave2.json"]})

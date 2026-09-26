"""FIG-07 — certified biological anchor m=0.35 (CERTIFIED COMPUTATION + NUMERICAL CORROBORATION).

(a) coexistence densities along m in [0.25,0.45] with the anchor; (b) invariant margins kappa-T1 and T_alpha-kappa
along m with certified lower bounds at the three candidate anchors (squares = CERTIFIED INTERVAL);
(c) eigenvalues of D*B at the worst positive diagonal (min |arg| over D, scale-invariant search) with the
Matignon rays at alpha=0.9: the pair has |arg| > 0.9 pi/2 but Re > 0;
(d) linearised Caputo dynamics at the same worst diagonal (predictor-corrector, own implementation):
decay at alpha=0.9, growth at alpha=1.
"""
import json, math, os
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S

S.setup()
D = json.load(open(os.path.join(S.DATA, "branch_alpha0.9.json")))
br = D["branch"]; m = np.array([r["m"] for r in br])
sel = (m >= 0.25) & (m <= 0.46)
X = np.array([r["X"] for r in br]); Y = np.array([r["Y"] for r in br]); Z = np.array([r["Z"] for r in br])
kap = np.array([r["kappa"] for r in br]); t1 = np.array([r["T1"] for r in br]); ta = np.array([r["T_alpha"] for r in br])
A = D["candidates"]["0.35"]; mA = 0.35
fig, axes = plt.subplots(2, 2, figsize=(S.W2, S.W2 * 0.72))
(ax1, ax2), (ax3, ax4) = axes
# (a)
for arr, lab, col in ((X, "$X$", S.BIO), (Y, "$Y$", S.NDARK), (Z, "$Z$", S.FRAC)):
    ax1.plot(m[sel], arr[sel], color=col, lw=S.LW_CMP); ax1.text(0.463, arr[sel][-1], lab, color=col, fontsize=7.5, va="center")
ax1.axvline(mA, color=S.BIO, lw=S.LW_AUX, ls=":")
ax1.set_yscale("log"); ax1.set_xlim(0.25, 0.48); ax1.set_xlabel(r"$m$"); ax1.set_ylabel("coexistence densities")
ax1.set_title("positive coexistence branch", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax1, "(a)")
# (b)
ax2.plot(m[sel], (kap - t1)[sel], color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$\kappa-T_1$")
ax2.plot(m[sel], (ta - kap)[sel], color=S.FRAC, lw=S.LW_THM, label=r"$T_{0.9}-\kappa$")
for k, c in D["candidates"].items():
    mm = float(k); cert = c["certified"]
    ax2.plot([mm], [float(cert["kappa_minus_T1_lo"])], marker="s", ms=4.5, color=S.CLAS, mec="black", mew=0.5, ls="none", zorder=5)
    ax2.plot([mm], [float(cert["T_alpha_L_minus_kappa_hi"])], marker="s", ms=4.5, color=S.FRAC, mec="black", mew=0.5, ls="none", zorder=5)
ax2.plot([], [], marker="s", ms=4.5, color="white", mec="black", mew=0.5, ls="none", label="certified lower bounds")
ax2.axvline(mA, color=S.BIO, lw=S.LW_AUX, ls=":")
ax2.set_xlim(0.25, 0.48); ax2.set_ylim(0, 24); ax2.set_xlabel(r"$m$"); ax2.set_ylabel("margin"); ax2.legend(fontsize=6.5, loc="center right")
ax2.set_title("invariant margins (both strict)", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax2, "(b)")
# (c) eigenvalues at worst D
ev = np.array(A["eig_at_worst_d"]); alpha = 0.9; th = alpha * math.pi / 2
R = 1.15 * np.abs(ev[:, 0] + 1j * ev[:, 1]).max()
ax3.set_aspect("equal"); ax3.set_xlim(-R * 1.15, R * 0.45); ax3.set_ylim(-R, R)
ax3.axvline(0, color=S.NDARK, lw=S.LW_AUX); ax3.axhline(0, color=S.NDARK, lw=S.LW_AUX)
for sgn in (1, -1):
    ax3.plot([0, R * np.cos(th)], [0, sgn * R * np.sin(th)], color=S.FRAC, lw=S.LW_THM)
ax3.fill_betweenx([-R, R], -R, 0, color=S.CLAS, alpha=0.12, lw=0)
ax3.plot(ev[:, 0], ev[:, 1], marker="o", ms=5, color=S.NOGO, mec="black", mew=0.5, ls="none", zorder=5)
ang = np.min(np.abs(np.angle(ev[:, 0] + 1j * ev[:, 1])))
ax3.text(-R * 1.1, -R * 0.95, f"$\\min|\\arg\\lambda|={ang:.4f}$\n$>0.9\\pi/2={th:.4f}$\nand $\\mathrm{{Re}}\\,\\lambda>0$", fontsize=6.8, color=S.NDARK, va="bottom")
ax3.set_xlabel(r"$\mathrm{Re}\,\lambda(D^*B)$"); ax3.set_ylabel(r"$\mathrm{Im}\,\lambda$")
ax3.set_title(r"spectrum of $D^*B$", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax3, "(c)")
# (d) linearised Caputo PECE at the worst D
B = np.array(A["B"]); d = np.array(A["worst_d_geomean1"]); J = np.diag(d) @ B
w, V = np.linalg.eig(J); k = int(np.argmin(np.abs(np.angle(w)))); v0 = np.real(V[:, k]); v0 = v0 / np.linalg.norm(v0) * 1e-3


def pece(fun, x0, alpha, T, h):
    N = int(T / h); x = np.zeros((N + 1, len(x0))); f = np.zeros_like(x); x[0] = x0; f[0] = fun(x0)
    kk = np.arange(N + 2, dtype=float); b = (kk + 1) ** alpha - kk ** alpha
    a = np.zeros(N + 2); a[1:] = (kk[1:] + 1) ** (alpha + 1) - 2 * kk[1:] ** (alpha + 1) + (kk[1:] - 1) ** (alpha + 1)
    g1, g2 = math.gamma(alpha + 1), math.gamma(alpha + 2)
    for j in range(1, N + 1):
        idx = np.arange(j)
        pred = x0 + h ** alpha / g1 * (b[j - 1 - idx][:, None] * f[:j]).sum(0)
        c0 = (j - 1) ** (alpha + 1) - (j - 1 - alpha) * j ** alpha
        ssum = c0 * f[0] + ((a[j - idx[1:]][:, None] * f[1:j]).sum(0) if j > 1 else 0)
        x[j] = x0 + h ** alpha / g2 * (fun(pred) + ssum); f[j] = fun(x[j])
    return x


T, h = 250.0, 0.05
tt = np.arange(0, T + h / 2, h)
sim = {}
for al, col, lab in ((0.9, S.FRAC, r"$\alpha=0.9$"), (1.0, S.CLAS, r"$\alpha=1$")):
    xs = pece(lambda v: J @ v, v0, al, T, h); n = np.linalg.norm(xs, axis=1)
    ax4.plot(tt[:len(n)], n / n[0], color=col, lw=S.LW_CMP, label=lab); sim[str(al)] = {"final_over_initial": float(n[-1] / n[0]), "max_over_initial": float(n.max() / n[0])}
ax4.set_yscale("log"); ax4.set_xlabel(r"$t$ (scaled time)"); ax4.set_ylabel(r"$\|\delta x(t)\|/\|\delta x(0)\|$"); ax4.legend(fontsize=7, loc="lower left")
ax4.set_title(r"linearised Caputo dynamics at $D^*$", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax4, "(d)")
fig.subplots_adjust(wspace=0.32, hspace=0.5)
S.save_data("fig07_anchor_candidates.json", D["candidates"])
S.export(fig, "fig07_certified_anchor", {
    "claims": ["DA-08 (open region)", "DA-11 (interior fractional-only point)", "C-10", "C-11 (certificate also holds)"],
    "anchor": {"m": 0.35, "biological_parameters": {**D["params"], "m": 0.35}, "X_Y_Z": [A["X"], A["Y"], A["Z"]], "s": A["s"], "beta": A["beta"], "kappa": A["kappa"],
               "T1": A["T1"], "T_alpha": A["T_alpha"], "m_Cain": A["m_Cain"], "m_frac": A["m_frac"], "m_Cain_over_T1": A["m_Cain_over_T1"], "m_frac_over_Talpha": A["m_frac_over_Talpha"],
               "direct_min_margin_alpha": A["direct_min_margin_alpha"], "direct_min_margin_1": A["direct_min_margin_1"], "worst_d_geomean1": A["worst_d_geomean1"],
               "certified": A["certified"], "cond_classical": A["cond_classical"], "cond_fractional": A["cond_fractional"], "time_domain": sim},
    "candidates_ranked": ["0.35 (recommended)", "0.40", "0.30"],
    "objects": {"densities, margins": "EXACT THEOREM CURVE (numerical evaluation of exact formulas along the branch)", "squares": "CERTIFIED INTERVAL (interval Newton + outward rounding, 50 digits; C-10 bound conditional on C-15 Thm 1, C-11 bound unconditional)",
                "eigenvalues (c)": "NUMERICAL CORROBORATION (scale-invariant direct search over positive diagonals)", "time series (d)": "NUMERICAL CORROBORATION (Diethelm PECE on the linearised Caputo system)"},
    "data": ["computations/figures/data/branch_alpha0.9.json", "computations/figures/data/fig07_anchor_candidates.json"]})

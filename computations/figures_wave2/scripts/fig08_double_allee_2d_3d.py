"""FIG-08 (Wave 2) — 2D/3D contrast with smooth boundary tracing in panel (b).
(a) as Wave 1 (m_c curve).  (b) (m, K) slice of the selected 3D design: the classical|fractional boundary
(kappa-T1=0), the fractional|unstable boundary (T_alpha-kappa=0, if present) and the feasibility edges are traced
as functions of K by deterministic scan+bisection on the exact functions (design_tools.trace_boundaries); regions
are filled between the traced curves; the certified m-interval and the anchor are overlaid.
"""
import json, os
import numpy as np
import matplotlib.pyplot as plt
import figstyle as S
from design_tools import params_from_design, trace_boundaries
from fdsn.double_allee import PARAM_NAMES

S.setup()
D = json.load(open(os.path.join(S.DATA, "design_selected.json")))
P, _ = params_from_design(D["design"])
K0 = P.K; mA = D["anchor_m"]; m0 = float(D["m0_hp"])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(S.W2, S.W2 * 0.42))
a, K = 0.5, 1.1
Xg = np.linspace(0.05, K, 300); mc = (Xg ** 2 + 2 * a * Xg - K * a) / (K + a)
ax1.fill_between(Xg, np.maximum(mc, 0), Xg, where=Xg > np.maximum(mc, 0), color=S.NOGO, alpha=0.10, lw=0)
ax1.fill_between(Xg, 0, np.clip(mc, 0, None), color=S.CLAS, alpha=0.14, lw=0)
ok = mc > 0; ax1.plot(Xg[ok], mc[ok], color=S.FRAC, lw=S.LW_THM)
ax1.plot(Xg, Xg, color=S.NDARK, lw=S.LW_AUX, ls=":"); ax1.text(0.52, 0.56, "$m=X$", fontsize=7, color=S.NDARK, rotation=48)
ax1.set_xlim(0, K); ax1.set_ylim(0, 0.9); ax1.set_xlabel(r"prey equilibrium $X=d/p$"); ax1.set_ylabel(r"Allee threshold $m$")
ax1.text(0.85, 0.15, "classical\n$g_{DA}'(X)<0$", color=S.CLAS, fontsize=7.5, ha="center")
ax1.text(0.35, 0.28, "not in $\\mathcal{F}_\\alpha$\n$g_{DA}'(X)>0$", color=S.NOGO, fontsize=7.5, ha="center")
ax1.annotate("fractional-only:\n$m_c=(X^2+2aX-Ka)/(K+a)$", xy=(0.8, (0.8 ** 2 + 2 * a * 0.8 - K * a) / (K + a)), xytext=(0.30, 0.74), fontsize=7, color=S.FRAC, arrowprops=dict(arrowstyle="-", lw=0.7, color=S.FRAC))
ax1.set_title(rf"2D double-Allee model ($a={a}$, $K={K}$)", fontsize=8, color=S.NDARK, pad=2)
S.panel_label(ax1, "(a)")
# (b) traced boundaries
Ks = np.linspace(K0 * 0.7, K0 * 1.3, 61)
cur = trace_boundaries(P, Ks)
def arr(name):
    v = np.array(cur[name]) if cur[name] else np.zeros((0, 2)); return v
cf, fu, fl, fh = arr("classical_fractional"), arr("fractional_unstable"), arr("feasibility_low"), arr("feasibility_high")
# fill: classical between feasibility_low and classical_fractional; fractional between classical_fractional and min(feasibility_high, fractional_unstable)
Kc = cf[:, 0]; mcf = np.interp(Kc, fl[:, 0], fl[:, 1]) if len(fl) else np.zeros_like(Kc)
upper = np.interp(Kc, fh[:, 0], fh[:, 1]) if len(fh) else np.full_like(Kc, 0.99)
if len(fu):
    upper = np.minimum(upper, np.interp(Kc, fu[:, 0], fu[:, 1]))
ax2.fill_betweenx(Kc, mcf, cf[:, 1], color=S.CLAS, alpha=0.14, lw=0)
ax2.fill_betweenx(Kc, cf[:, 1], upper, color=S.FRAC, alpha=0.22, lw=0)
if len(fu):
    ax2.fill_betweenx(fu[:, 0], fu[:, 1], np.interp(fu[:, 0], fh[:, 0], fh[:, 1]) if len(fh) else 0.99, color=S.NOGO, alpha=0.10, lw=0)
    ax2.plot(fu[:, 1], fu[:, 0], color=S.NOGO, lw=S.LW_CMP, label=r"$\kappa=T_{0.9}$")
ax2.plot(cf[:, 1], cf[:, 0], color=S.CLAS, lw=S.LW_THM, ls="--", label=r"$\kappa=T_1$")
if len(fh):
    ax2.plot(fh[:, 1], fh[:, 0], color=S.NDARK, lw=S.LW_AUX, ls="-", label="feasibility edge")
if len(fl) and fl[:, 1].max() > 0.006:
    ax2.plot(fl[:, 1], fl[:, 0], color=S.NDARK, lw=S.LW_AUX, ls="-")
ci = D["certified_m_interval"]
if ci["fully_certified"]:
    ax2.plot(ci["attempted"], [K0, K0], color=S.BIO, lw=3.2, solid_capstyle="butt", label="certified $m$-range")
ax2.plot([m0], [K0], marker="o", ms=5, color=S.CLAS, mec="black", mew=0.5, ls="none", label="$m_0$ (exact)")
ax2.plot([mA], [K0], marker="D", ms=5, color=S.BIO, mec="black", mew=0.5, ls="none", label=f"anchor $m={mA}$")
ax2.set_xlim(0, min(0.99, (fh[:, 1].max() if len(fh) else 0.99) + 0.05)); ax2.set_ylim(Ks[0], Ks[-1])
ax2.set_xlabel(r"Allee threshold $m$"); ax2.set_ylabel(r"carrying capacity $K$")
Kmid = Ks[len(Ks) // 2]; i = int(np.argmin(np.abs(Kc - Kmid)))
ax2.text(0.5 * (mcf[i] + cf[i, 1]), Kmid, "classical", color=S.CLAS, fontsize=7.5, ha="center", va="center")
Khi = Ks[int(0.82 * len(Ks))]; j = int(np.argmin(np.abs(Kc - Khi)))
ax2.text(0.5 * (cf[j, 1] + upper[j]), Khi, "fractional-\nonly (open)", color=S.FRAC, fontsize=7, ha="center", va="center")
if len(fu) and len(fh):
    jj = int(np.argmin(np.abs(fu[:, 0] - Khi)))
    ax2.text(0.5 * (fu[jj, 1] + np.interp(Khi, fh[:, 0], fh[:, 1])) + 0.01, Khi, "not\nstable", color=S.NOGO, fontsize=6.5, ha="center", va="center")
ax2.legend(loc="lower left", fontsize=6.0, handlelength=1.4, borderaxespad=0.3, labelspacing=0.35)
ax2.set_title(r"3D IGP model, $\alpha=0.9$: $(m,K)$ slice" + "\n" + r"(traced boundaries: exact formulas pointwise, not certified)", fontsize=7.5, color=S.NDARK, pad=2)
S.panel_label(ax2, "(b)")
fig.subplots_adjust(wspace=0.3)
json.dump({k: [list(map(float, p)) for p in v] for k, v in cur.items()}, open(os.path.join(S.DATA, "fig08_traced_boundaries.json"), "w"), indent=1)
S.export(fig, "fig08_double_allee_2d_3d", {
    "claims": ["DA-12", "DA-08", "C-07", "C-10"],
    "formulas": ["m_c=(X^2+2aX-Ka)/(K+a)", "boundaries: kappa-T1=0 (classical|fractional), T_alpha-kappa=0 (fractional|unstable), feasibility edges"],
    "parameters": {"panel_a": {"a": a, "K": K}, "panel_b": {"alpha": 0.9, "design": D["design"], "fixed_parameters": D["params"], "K_range": [float(Ks[0]), float(Ks[-1])], "n_K": len(Ks),
                   "tracing": "scan of 400 m-values per K + 80 bisection steps on the exact defining function"}},
    "objects": {"m_c curve": "CLOSED-FORM BOUNDARY", "traced boundaries and fills": "NUMERICAL EVALUATION OF EXACT FORMULAS (root tracing; not interval-certified)",
                "green segment": "CERTIFIED INTERVAL", "m0": "CERTIFIED COMPUTATION (60-digit root)"},
    "data": ["computations/figures_wave2/data/fig08_traced_boundaries.json", "computations/figures_wave2/data/design_selected.json"]})

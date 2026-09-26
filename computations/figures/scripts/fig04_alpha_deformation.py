"""FIG-04 — deformation of T_alpha with alpha (THEOREM-GRADE + numerical evaluation of exact formulas; HP near limits).

(a) T_alpha/T_1 vs alpha on (2/3,1) for selected beta; (b) zoom alpha -> 1: (T_alpha - T_1) vs (1-alpha) with the
C-14 linear asymptotic C(beta)(1-alpha) (dashed); (c) alpha -> 2/3+: T_alpha K^3/27 vs K with the C-15 Thm 3
first-order asymptotic 1 + K(9 sum beta - 27)/27 (dashed).
"""
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import figstyle as S
from fdsn.c10_threshold import T1, mp_T1, mp_rate_constant, mp_uk, rate_constant, threshold_batch, threshold_mp

S.setup()
BETAS = {r"$(1,1,1)$": (1.0, 1.0, 1.0), r"$(3,3,3)$": (3.0, 3.0, 3.0), r"$(0.5,2,1.5)$": (0.5, 2.0, 1.5)}
LS = {r"$(1,1,1)$": "-", r"$(3,3,3)$": "-.", r"$(0.5,2,1.5)$": ":"}
fig, axes = plt.subplots(1, 3, figsize=(S.W2, S.W2 * 0.36))
ax1, ax2, ax3 = axes
al = np.unique(np.concatenate([2 / 3 + np.logspace(-4, np.log10(1 / 3 - 1e-4), 300), 1 - np.logspace(-4, -1, 80)]))
al = al[(al > 2 / 3) & (al < 1)]
data = {"alpha": al.tolist()}
for lab, b in BETAS.items():
    b = np.array(b); tb = threshold_batch(np.repeat(b[None], al.size, 0), al)
    ax1.plot(al, tb.T / T1(b), color=S.FRAC, lw=S.LW_CMP, ls=LS[lab], label=lab)
    data["ratio_" + lab] = (tb.T / T1(b)).tolist()
ax1.axhline(1, color=S.CLAS, lw=S.LW_AUX, ls="--"); ax1.text(0.98, 1.15, r"$T_1$", color=S.CLAS, fontsize=7.5, ha="right")
ax1.set_yscale("log"); ax1.set_xlim(2 / 3, 1); ax1.set_ylim(0.9, 1e4)
ax1.set_xlabel(r"$\alpha$"); ax1.set_ylabel(r"$T_\alpha(\beta)/T_1(\beta)$")
ax1.axvline(2 / 3, color=S.NDARK, lw=S.LW_AUX, ls=":"); ax1.text(0.78, 400, r"$\alpha\downarrow2/3$: $T_\alpha\sim27/K^3$", color=S.NDARK, fontsize=6.8)
ax1.legend(title=r"$\beta$", fontsize=6.8, title_fontsize=7, loc="upper right")
S.panel_label(ax1, "(a)")
# (b) alpha -> 1 (HP)
eps = np.logspace(-6, -1, 26)
hp = {}
for lab, b in BETAS.items():
    bs = [repr(float(v)) for v in b]
    with mp.workdps(40):
        W = [float(threshold_mp(bs, 1 - mp.mpf(e), dps=35)["T"] - mp_T1([mp.mpf(v) for v in bs])) for e in eps]
    C = float(rate_constant(np.array(b)))
    ax2.plot(eps, W, color=S.FRAC, lw=S.LW_CMP, ls=LS[lab])
    ax2.plot(eps, C * eps, color=S.CLAS, lw=S.LW_AUX, ls="--")
    hp[lab] = {"eps": eps.tolist(), "W": W, "C_beta": C}
ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.set_xlabel(r"$1-\alpha$"); ax2.set_ylabel(r"$T_\alpha-T_1$")
ax2.text(3e-4, 1.2e-4, r"dashed: C-14 $C(\beta)(1-\alpha)$", color=S.CLAS, fontsize=7)
S.panel_label(ax2, "(b)")
# (c) alpha -> 2/3+ (HP)
Ks = []; lo = {}
for lab, b in BETAS.items():
    bs = [repr(float(v)) for v in b]; vals = []; Kv = []
    with mp.workdps(60):
        for k in np.linspace(1, 7, 25):
            a = mp.mpf(2) / 3 + mp.mpf(10) ** (-k)
            u, K = mp_uk(a); T = threshold_mp(bs, a, dps=55)["T"]
            vals.append(float(T * K ** 3 / 27)); Kv.append(float(K))
    Kv = np.array(Kv); vals = np.array(vals)
    ax3.plot(Kv, vals, color=S.FRAC, lw=S.LW_CMP, ls=LS[lab])
    ax3.plot(Kv, 1 + Kv * (9 * sum(b) - 27) / 27, color=S.CLAS, lw=S.LW_AUX, ls="--")
    lo[lab] = {"K": Kv.tolist(), "T_K3_over_27": vals.tolist()}
ax3.set_xscale("log"); ax3.set_ylim(0.97, 1.5); ax3.set_xlabel(r"$K=1-4\cos^2(\alpha\pi/2)\to0^+$"); ax3.set_ylabel(r"$T_\alpha K^3/27$")
ax3.text(1.5e-7, 1.42, r"dashed: C-15 $1+K\,(9\sum\beta-27)/27$", color=S.CLAS, fontsize=7)
S.panel_label(ax3, "(c)")
fig.subplots_adjust(wspace=0.42)
S.save_data("fig04_alpha_curves.json", {"panel_a": data, "panel_b_hp": hp, "panel_c_hp": lo})
S.export(fig, "fig04_alpha_deformation", {
    "claims": ["C-14 Thm 1-2", "C-15 Thm 3", "C-10 §6-7"],
    "formulas": ["T_alpha(beta)=T_1+C(beta)(1-alpha)+O((1-alpha)^2), C=pi(S^{5/2}/sqrt G+S^{3/2}sqrt G)", "T_alpha=27/K^3+(9 sum beta-27)/K^2+O(1/K)"],
    "parameters": {"betas": {k: v for k, v in BETAS.items()}, "panel_b_eps": [1e-6, 1e-1], "panel_c_k": [1, 7], "hp_digits": {"b": 35, "c": 55}},
    "objects": {"solid/dashdot/dotted blue": "EXACT THEOREM CURVE (numerical evaluation; HP in (b),(c))", "dashed orange": "CLOSED-FORM asymptotics (C-14, C-15)"},
    "data": "computations/figures/data/fig04_alpha_curves.json"})

#!/usr/bin/env python3
from pathlib import Path
import math
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from matplotlib.patches import Wedge

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
DATA = ROOT / "computations" / "results" / "wave2" / "FIGURE_DATA"
ROBUST = ROOT / "computations" / "results" / "wave2" / "ROBUSTNESS_SUMMARY.csv"

TRIPLES = [
    "no_pair_loops_(1,1,1)",
    "all_antagonistic_(3,3,3)",
    "mixed_(3,0.5,1)",
    "anisotropic_(0.01,1,100)",
]
LABELS = {
    "no_pair_loops_(1,1,1)": r"$(1,1,1)$",
    "all_antagonistic_(3,3,3)": r"$(3,3,3)$",
    "mixed_(3,0.5,1)": r"$(3,0.5,1)$",
    "anisotropic_(0.01,1,100)": r"$(0.01,1,100)$",
}
STYLES = ["-", "--", "-.", ":"]

def save(fig, name):
    fig.tight_layout(pad=0.5)
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

def h_alpha(b, alpha):
    theta = alpha * math.pi / 2
    u = math.cos(theta)
    K = 1 - 4 * u * u
    r = (u + np.sqrt(u*u + K*b)) / K
    return r*r*(1 + 2*u*r)

def panel_spectral():
    alpha = 0.8
    theta = alpha * math.pi / 2
    fig, ax = plt.subplots(figsize=(3.1, 2.55))
    R = 1.0
    ax.add_patch(Wedge((0,0), R, math.degrees(theta), 360-math.degrees(theta),
                       fill=False, hatch="///", linewidth=1.0))
    ax.add_patch(Wedge((0,0), R, 90, 270,
                       fill=False, hatch="\\\\", linewidth=1.0))
    ax.axhline(0, linewidth=0.6)
    ax.axvline(0, linewidth=0.6)
    for sgn in [1,-1]:
        ax.plot([0, R*math.cos(theta)], [0, sgn*R*math.sin(theta)],
                linestyle="--", linewidth=0.9)
    ax.text(-0.98, 0.88, "Hurwitz", fontsize=7)
    ax.text(0.08, -0.92, "fractional RHP sliver", fontsize=7)
    ax.set_aspect("equal")
    ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
    ax.set_xlabel(r"$\Re z$", fontsize=8); ax.set_ylabel(r"$\Im z$", fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title(r"(a) Matignon vs. Hurwitz, $\alpha=0.8$", fontsize=8)
    save(fig, "panel01_spectral_geometry")

def panel_dimension():
    fig, ax = plt.subplots(figsize=(3.1, 2.55))
    ax.set_xlim(0.5, 3.5); ax.set_ylim(-0.08, 1.1)
    ax.scatter([1,2,3],[0,0,1], s=[35,35,55], marker="o")
    ax.plot([1,2],[0,0], linestyle="--", linewidth=0.8)
    ax.axhline(0, linewidth=0.6)
    ax.text(1,0.11,"coincide",ha="center",fontsize=7)
    ax.text(2,0.11,"fractional-only\nlower-dimensional",ha="center",fontsize=7)
    ax.text(3,0.80,"nonempty\nfull-dimensional\ninterior",ha="center",fontsize=7)
    ax.set_xticks([1,2,3],["1","2","3"])
    ax.set_yticks([0,1],["no","yes"])
    ax.set_xlabel("matrix dimension",fontsize=8)
    ax.set_ylabel("robust fractional-only class",fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title("(b) Minimum robust dimension",fontsize=8)
    save(fig, "panel02_dimension_threshold")

def panel_simplex():
    alpha=0.9
    b12,b13,b23=3.0,0.5,1.0
    xs=[]; ys=[]; zs=[]
    for x1 in np.linspace(0.025,0.95,65):
        for x2 in np.linspace(0.025,0.95-x1,65):
            x3=1-x1-x2
            if x3<=0.025:
                continue
            B=b12*x1*x2+b13*x1*x3+b23*x2*x3
            F=h_alpha(B,alpha)/(x1*x2*x3)
            xs.append(x1); ys.append(x2); zs.append(math.log10(F))
    tri=mtri.Triangulation(xs,ys)
    fig, ax=plt.subplots(figsize=(3.1,2.55))
    cs=ax.tricontour(tri,zs,levels=9,linewidths=0.8)
    ax.clabel(cs,inline=True,fontsize=6,fmt="%.1f")
    ax.plot([0,1,0,0],[0,0,1,0],linewidth=0.8)
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.set_xlabel(r"$x_1$",fontsize=8); ax.set_ylabel(r"$x_2$",fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title(r"(c) $\log_{10}F_{\alpha,\beta}$ on the simplex",fontsize=8)
    save(fig,"panel03_simplex_objective")

def panel_cyclic():
    a=np.linspace(2/3+1e-3,0.999,350)
    th=a*np.pi/2
    R=np.sin(th)/np.sin(th-np.pi/3)
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    ax.plot(a,R,linewidth=1.2,label=r"$R_3(\alpha)$")
    ax.axhline(2,linestyle="--",linewidth=0.9,label=r"classical $\gamma=2$")
    ax.set_xlim(2/3,1); ax.set_ylim(1.7,min(15,np.nanmax(R)))
    ax.set_xlabel(r"$\alpha$",fontsize=8); ax.set_ylabel(r"$\gamma$",fontsize=8)
    ax.tick_params(labelsize=7); ax.legend(fontsize=6,loc="upper right")
    ax.set_title("(d) Exact cyclic fractional band",fontsize=8)
    save(fig,"panel04_cyclic_band")

def panel_threshold_ratio():
    df=pd.read_csv(DATA/"F1_T_ratio_vs_alpha"/"F1_T_ratio_vs_alpha.csv")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    for name,ls in zip(TRIPLES,STYLES):
        d=df[df["triple"]==name].sort_values("alpha")
        ax.plot(d["alpha"],d["T_alpha_over_T1"],linestyle=ls,linewidth=1.0,label=LABELS[name])
    ax.set_yscale("log"); ax.set_xlim(2/3,1)
    ax.set_xlabel(r"$\alpha$",fontsize=8); ax.set_ylabel(r"$T_\alpha/T_1$",fontsize=8)
    ax.tick_params(labelsize=7); ax.legend(fontsize=5.5)
    ax.set_title("(a) Fractional enlargement",fontsize=8)
    save(fig,"panel05_threshold_ratio")

def panel_relative_width():
    df=pd.read_csv(DATA/"F3_W_over_T1"/"F3_W_over_T1.csv")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    for name,ls in zip(TRIPLES,STYLES):
        d=df[df["triple"]==name].sort_values("alpha")
        ax.plot(d["alpha"],d["W_over_T1"],linestyle=ls,linewidth=1.0,label=LABELS[name])
    ax.set_yscale("log"); ax.set_xlim(2/3,1)
    ax.set_xlabel(r"$\alpha$",fontsize=8); ax.set_ylabel(r"$(T_\alpha-T_1)/T_1$",fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title("(b) Relative fractional-band width",fontsize=8)
    save(fig,"panel06_relative_width")

def panel_classical_asymptotic():
    df=pd.read_csv(DATA/"F8_classical_asymptotic"/"F8_classical_asymptotic.csv")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    for name,ls in zip(TRIPLES,STYLES):
        d=df[df["triple"]==name].copy()
        ax.plot(d["1-alpha"],d["(T-T1)/(C(1-alpha))"],linestyle=ls,marker="o",markersize=2.5,linewidth=0.9,label=LABELS[name])
    ax.axhline(1,linestyle="--",linewidth=0.7)
    ax.set_xscale("log"); ax.set_xlabel(r"$1-\alpha$",fontsize=8)
    ax.set_ylabel(r"$(T_\alpha-T_1)/(C(1-\alpha))$",fontsize=7)
    ax.tick_params(labelsize=7)
    ax.set_title("(c) Classical-order asymptotic",fontsize=8)
    save(fig,"panel07_classical_asymptotic")

def panel_low_order():
    df=pd.read_csv(DATA/"F9_low_order_blowup"/"F9_low_order_blowup.csv")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    for name,ls in zip(TRIPLES,STYLES):
        d=df[df["triple"]==name].copy()
        ax.plot(d["K=1-4cos^2(alpha pi/2)"],d["T*K^3/27"],linestyle=ls,marker="o",markersize=2.5,linewidth=0.9,label=LABELS[name])
    ax.axhline(1,linestyle="--",linewidth=0.7)
    ax.set_xscale("log"); ax.invert_xaxis()
    ax.set_xlabel(r"$K\downarrow0$",fontsize=8); ax.set_ylabel(r"$T_\alpha K^3/27$",fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title(r"(d) Low-order $K^{-3}$ blow-up",fontsize=8)
    save(fig,"panel08_low_order")

def panel_ecological_band():
    df=pd.read_csv(DATA/"F5_L3_alpha_boundaries"/"F5_L3_alpha_boundaries.csv")
    d=df[df["triple"]=="mixed_(3,0.5,1)"].sort_values("alpha")
    d=d[d["alpha"]>=0.82]
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    ax.plot(d["alpha"],-d["L3_cain_boundary"],linestyle="--",linewidth=1.0,label="Cain")
    ax.plot(d["alpha"],-d["L3_fractional_boundary"],linestyle="-",linewidth=1.0,label="fractional")
    ax.set_yscale("log"); ax.set_xlim(0.82,1)
    ax.set_xlabel(r"$\alpha$",fontsize=8); ax.set_ylabel(r"$-L_3$",fontsize=8)
    ax.tick_params(labelsize=7); ax.legend(fontsize=6)
    ax.set_title(r"(a) Loop-space band, $\beta=(3,.5,1)$",fontsize=8)
    save(fig,"panel09_ecological_band")

def panel_pairloop_sensitivity():
    df=pd.read_csv(DATA/"F6_pairloop_sensitivity"/"F6_pairloop_sensitivity.csv")
    d=df[(df["alpha"]==0.9)&(df["g23"]==0.0)].copy()
    pivot=d.pivot(index="g13",columns="g12",values="logelast_beta12")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    cs=ax.contour(pivot.columns.values,pivot.index.values,pivot.values,levels=10,linewidths=0.8)
    ax.clabel(cs,inline=True,fontsize=5.5,fmt="%.2f")
    ax.set_xlabel(r"$g_{12}$",fontsize=8); ax.set_ylabel(r"$g_{13}$",fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title(r"(b) Pair-loop elasticity, $\alpha=.9$",fontsize=8)
    save(fig,"panel10_pairloop_sensitivity")

def panel_optimizer():
    df=pd.read_csv(DATA/"F7_xstar_alpha_beta"/"F7_xstar_alpha_beta.csv")
    d=df[df["triple"]=="mixed_(3,0.5,1)"].sort_values("alpha")
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    for col,ls in zip(["x1","x2","x3"],["-","--","-."]):
        ax.plot(d["alpha"],d[col],linestyle=ls,linewidth=1.0,label="$"+col+"$")
    ax.set_xlim(2/3,1); ax.set_ylim(0,0.65)
    ax.set_xlabel(r"$\alpha$",fontsize=8); ax.set_ylabel(r"$x_i^*$",fontsize=8)
    ax.tick_params(labelsize=7); ax.legend(fontsize=6)
    ax.set_title(r"(c) Unique worst-orbit coordinate $x^*$",fontsize=8)
    save(fig,"panel11_optimizer")

def panel_robustness():
    df=pd.read_csv(ROBUST)
    d=df[(df["norm"]=="max") & (df["id"].isin(["W01","W03","W18","W22","W28"]))].copy()
    d["dist"]=pd.to_numeric(d["best_upper_bound_hp"],errors="coerce")
    ids=["W01","W03","W18","W22","W28"]
    boundaries=["frac","cain","p"]
    fig,ax=plt.subplots(figsize=(3.1,2.55))
    xpos=np.arange(len(ids))
    width=0.23
    for j,b in enumerate(boundaries):
        vals=[]
        for wid in ids:
            q=d[(d["id"]==wid)&(d["boundary"]==b)]["dist"]
            vals.append(float(q.iloc[0]) if len(q) and np.isfinite(q.iloc[0]) else np.nan)
        ax.bar(xpos+(j-1)*width,vals,width=width,label=b)
    ax.set_yscale("log"); ax.set_xticks(xpos,ids)
    ax.set_ylabel("max-norm upper bound",fontsize=7)
    ax.tick_params(labelsize=7); ax.legend(fontsize=5.5,ncol=3)
    ax.set_title("(d) Boundary robustness of witnesses",fontsize=8)
    save(fig,"panel12_robustness")


def legacy_c11_coverage():
    df=pd.read_csv(DATA/"F4_C11_sufficient_fraction"/"F4_C11_sufficient_fraction.csv")
    fig,ax=plt.subplots(figsize=(5.2,4.0))
    for name,ls in zip(TRIPLES,STYLES):
        d=df[df["triple"]==name].sort_values("alpha")
        d=d[d["alpha"]>=0.70]
        ax.plot(d["alpha"],d["certified_fraction_(TPhi-T1)/(Talpha-T1)"],
                linestyle=ls,linewidth=1.0,label=LABELS[name])
    ax.set_xlim(0.70,1.0); ax.set_ylim(0,1.03)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel("fraction of exact band certified by C-11")
    ax.legend(title=r"$\beta$",fontsize=8,title_fontsize=8)
    ax.set_title("Conservatism of the closed-form certificate")
    save(fig,"fig_c11_coverage")

def legacy_aliases():
    for src,dst in [
        ("panel01_spectral_geometry","fig_spectral_geometry"),
        ("panel05_threshold_ratio","fig_threshold_ratio"),
        ("panel09_ecological_band","fig_ecological_band"),
    ]:
        for ext in ("pdf","png"):
            shutil.copyfile(OUT/f"{src}.{ext}",OUT/f"{dst}.{ext}")

if __name__=="__main__":
    panel_spectral()
    panel_dimension()
    panel_simplex()
    panel_cyclic()
    panel_threshold_ratio()
    panel_relative_width()
    panel_classical_asymptotic()
    panel_low_order()
    panel_ecological_band()
    panel_pairloop_sensitivity()
    panel_optimizer()
    panel_robustness()
    legacy_c11_coverage()
    legacy_aliases()

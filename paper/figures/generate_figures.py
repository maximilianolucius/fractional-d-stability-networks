#!/usr/bin/env python3
from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
DATA = ROOT / "computations" / "results" / "wave2" / "FIGURE_DATA"

def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

def spectral_geometry():
    alpha = 0.8
    theta = alpha * math.pi / 2
    fig, ax = plt.subplots(figsize=(5.0, 4.3))
    R = 1.0
    # Full Matignon stable reflex sector.
    frac = Wedge((0,0), R, math.degrees(theta), 360-math.degrees(theta),
                 fill=False, hatch="///", linewidth=1.3, label=r"$\Sigma_\alpha$")
    hur = Wedge((0,0), R, 90, 270,
                fill=False, hatch="\\\\", linewidth=1.3, label="Hurwitz half-plane")
    ax.add_patch(frac)
    ax.add_patch(hur)
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    for sgn in [1,-1]:
        ax.plot([0, R*math.cos(theta)], [0, sgn*R*math.sin(theta)],
                linestyle="--", linewidth=1.2)
    ax.text(0.23, 0.83, r"$|\arg z|=\alpha\pi/2$", fontsize=9)
    ax.text(0.16, -0.84, r"RHP fractional sliver", fontsize=9)
    ax.set_aspect("equal")
    ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
    ax.set_xlabel(r"$\Re z$"); ax.set_ylabel(r"$\Im z$")
    ax.legend(loc="lower left", fontsize=8)
    ax.set_title(r"Matignon versus Hurwitz stability ($\alpha=0.8$)")
    save(fig, "fig_spectral_geometry")

def threshold_ratio():
    df = pd.read_csv(DATA/"F1_T_ratio_vs_alpha"/"F1_T_ratio_vs_alpha.csv")
    chosen = [
        "no_pair_loops_(1,1,1)",
        "all_antagonistic_(3,3,3)",
        "mutualistic_mixed_(0.2,0.8,0.5)",
        "anisotropic_(0.01,1,100)",
    ]
    labels = {
        chosen[0]: r"$(1,1,1)$",
        chosen[1]: r"$(3,3,3)$",
        chosen[2]: r"$(0.2,0.8,0.5)$",
        chosen[3]: r"$(0.01,1,100)$",
    }
    styles=["-","--","-.",":"]
    fig, ax = plt.subplots(figsize=(5.2,4.0))
    for name,ls in zip(chosen,styles):
        d=df[df["triple"]==name].sort_values("alpha")
        ax.plot(d["alpha"], d["T_alpha_over_T1"], linestyle=ls, label=labels[name])
    ax.set_yscale("log")
    ax.set_xlim(2/3,1.0)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel(r"$T_\alpha(\beta)/T_1(\beta)$")
    ax.legend(title=r"$\beta$", fontsize=8, title_fontsize=8)
    ax.set_title("Exact fractional enlargement of Cain's threshold")
    save(fig, "fig_threshold_ratio")

def c11_coverage():
    df = pd.read_csv(DATA/"F4_C11_sufficient_fraction"/"F4_C11_sufficient_fraction.csv")
    chosen = [
        "no_pair_loops_(1,1,1)",
        "all_antagonistic_(3,3,3)",
        "mixed_(3,0.5,1)",
        "anisotropic_(0.01,1,100)",
    ]
    labels = {
        chosen[0]: r"$(1,1,1)$",
        chosen[1]: r"$(3,3,3)$",
        chosen[2]: r"$(3,0.5,1)$",
        chosen[3]: r"$(0.01,1,100)$",
    }
    styles=["-","--","-.",":"]
    fig, ax = plt.subplots(figsize=(5.2,4.0))
    for name,ls in zip(chosen,styles):
        d=df[df["triple"]==name].sort_values("alpha")
        d=d[d["alpha"]>=0.70]
        ax.plot(d["alpha"], d["certified_fraction_(TPhi-T1)/(Talpha-T1)"],
                linestyle=ls, label=labels[name])
    ax.set_xlim(0.70,1.0); ax.set_ylim(0,1.03)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel("fraction of exact band certified by C-11")
    ax.legend(title=r"$\beta$", fontsize=8, title_fontsize=8)
    ax.set_title("Conservatism of the closed-form certificate")
    save(fig, "fig_c11_coverage")

def ecological_band():
    df = pd.read_csv(DATA/"F5_L3_alpha_boundaries"/"F5_L3_alpha_boundaries.csv")
    name="mixed_(3,0.5,1)"
    d=df[df["triple"]==name].sort_values("alpha")
    d=d[d["alpha"]>=0.82]
    fig, ax = plt.subplots(figsize=(5.2,4.0))
    ax.plot(d["alpha"], -d["L3_cain_boundary"], linestyle="--",
            label=r"$-L_3$ at Cain boundary")
    ax.plot(d["alpha"], -d["L3_fractional_boundary"], linestyle="-",
            label=r"$-L_3$ at fractional boundary")
    ax.set_yscale("log")
    ax.set_xlim(0.82,1.0)
    ax.set_xlabel(r"fractional order $\alpha$")
    ax.set_ylabel(r"$-L_3$")
    ax.legend(fontsize=8)
    ax.set_title(r"Exact loop-space band for $\beta=(3,0.5,1)$")
    save(fig, "fig_ecological_band")

if __name__ == "__main__":
    spectral_geometry()
    threshold_ratio()
    c11_coverage()
    ecological_band()

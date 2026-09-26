# Chief Final Visual Gate — Wave 2

**Date:** 2026-09-26  
**Canonical branch:** `chief/manuscript-prep-20260926`  
**Figure Wave 2:** `agent/compute-figures-wave2-20260926` @ `3b596577e24d57dda6edd94b85649909e9b849de`

## Final decision

`VISUAL_GATE_PASS`

Wave 2 resolves the two outstanding visual issues from Wave 1:

1. the biological witness is now well-balanced in coexistence scale;
2. the dense figures have been simplified into a journal-ready six-environment program.

The visual system is now frozen for manuscript drafting, subject only to ordinary typesetting adjustments.

## Canonical biological witness

Adopt **W2-A** as the manuscript's primary ecological realization.

At the anchor:

~~~text
alpha = 0.9
m = 0.511
X = 1
Y = 0.785633
Z = 0.192182
~~~

so

~~~text
Y/X = 0.786
Z/X = 0.192
max/min density ratio = 5.20
~~~

The exact invariant data are:

~~~text
beta = (4.79, 4.506, 5.607)
kappa = 62.735
T1 = 44.6124
T_0.9 = 94.5719
~~~

with certified margins

~~~text
kappa - T1 >= 18.1226
T_0.9 - kappa >= 31.8369.
~~~

The exact classical crossing occurs at

~~~text
m0 =
0.37445128124251493523908034461904384927176466921467...
~~~

and the interval

~~~text
m in [0.394, 0.578]
~~~

is fully certified fractional-only for the fixed W2-A biological design.

The older Wave-1 witness at m=0.35 remains a documented backup and must not be deleted.

## Why W2-A becomes canonical

Compared with the Wave-1 anchor:

- density ratio improves from about 780 to 5.2;
- relative classical margin improves from about 14% to 41%;
- fractional margin remains large (about 34%);
- classical conditioning is essentially unchanged;
- the crossing remains unique/transverse;
- a nontrivial m-interval is interval-certified.

The tradeoff is accepted:
- the certified m-interval is shorter;
- the anchor is closer to the branch end;
- fractional conditioning is somewhat worse but still comfortable.

These are presentation-level tradeoffs, not theorem weaknesses.

## Final visual set

The paper should use **six figure environments** by default.

### Figure 1 — conceptual opening
Merge:
- FIG-01(b): Matignon sector at alpha=0.9;
- FIG-02(a): 2D codimension-one fractional-only locus;
- FIG-02(b): 3D open fractional-only band.

Three panels.

### Figure 2 — exact C-10 threshold geometry
Use FIG-03 unchanged except for final typesetting-scale adjustments.

Two panels.

### Figure 3 — threshold deformation with alpha
Use Wave-2 FIG-04:
- global T_alpha/T1 curve;
- classical-limit C-14 asymptotic.

Two panels.

The low-order C-15 panel remains an optional main-text asset only if the final page budget allows it.

### Figure 4 — ecological mechanism
Use Wave-2 FIG-05:
- competitive two-consumer no-go;
- IGP signed-cycle mechanism.

Two panels.

### Figure 5 — Double-Allee crossing
Use Wave-2 FIG-06.

Two panels.

This is the flagship ecological figure.

### Figure 6 — certified realization + exact 2D/3D contrast
Merge:
- FIG-08(a): exact 2D codimension-one curve;
- FIG-08(b): traced 3D (m,K) classification;
- FIG-07(b): certified margins;
- FIG-07(c): scale-invariant spectral corroboration.

Four panels in a 2x2 layout.

## Dropped from default main-text set

The following remain archived/reproducible but are not in the default manuscript layout:

- FIG-01(a): representative alpha=0.75 sector;
- FIG-07(a): coexistence-density path;
- FIG-07 time-domain panel from Wave 1;
- FIG-04c low-order asymptotic unless page budget permits.

Their mathematical content must be stated in the main text when relevant. Nothing is moved to supplementary material.

## Visual hierarchy

Non-negotiable:
- Figure 2 (C-10 geometry);
- Figure 5 (Double-Allee crossing).

High priority:
- Figure 4 (ecological sign mechanism);
- Figure 6 (certified realization / 2D-3D contrast).

Page-pressure reductions, in order:
1. omit optional FIG-04c;
2. reduce Figure 3 to its global alpha panel;
3. simplify Figure 1 before cutting theorem/ecological flagship figures.

## Evidence labeling lock

The manuscript must preserve the distinction:

- exact theorem curve;
- closed-form boundary;
- certified computation/interval;
- numerical corroboration;
- schematic.

In particular:
- direct diagonal spectral searches are corroboration only;
- FIG-08(b) traced regions are pointwise evaluations of exact formulas, not interval certification;
- certified green segments/points must be explicitly labeled as certified.

## Visual style lock

Keep the semantic palette:

~~~text
fractional / Matignon:  #1F4E79
classical / Cain:       #D97A00
biological / certified: #2A7F62
excluded / unstable:    #B14E3A
neutral dark:           #5C6770
neutral light:          #D9DDE3
~~~

White background, vector-first, no decorative 3D, no rainbow maps, no rasterized equations.

## Final visual status

~~~text
FIGURE WAVE 1:       PASS
FIGURE WAVE 2:       PASS
CANONICAL WITNESS:   W2-A
FINAL ENVIRONMENTS:  6
VISUAL GATE:         PASS
VISUAL SYSTEM:       FROZEN FOR DRAFTING
~~~

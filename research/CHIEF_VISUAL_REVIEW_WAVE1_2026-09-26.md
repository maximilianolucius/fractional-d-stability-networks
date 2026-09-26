# Chief Visual Review — Figure Wave 1

**Date:** 2026-09-26  
**Reviewed branch:** `agent/compute-figures-wave1-20260926`  
**Reviewed SHA:** `46c9eeffc55754ab6c2f010be68be6b95f8661d0`  
**Chief integration branch:** `chief/visual-integration-20260926`

## Overall verdict

`FIGURE_WAVE1_ACCEPTED_WITH_DESIGN_REFINEMENT`

The figure package is scientifically strong, reproducible, internally consistent, and visually coherent. The exact/certified/numerical evidence hierarchy is respected, the semantic palette is consistently applied, and the central theorem geometry is already visible at publication quality.

The figures are not yet frozen for final manuscript use. A short Wave 2 is justified to improve biological presentation and reduce visual density in selected panels.

## Non-negotiable strengths

1. **FIG-03** is publication-grade and should remain a central main-paper figure.
2. **FIG-06** is the strongest ecological figure and should remain a central main-paper figure.
3. The palette is coherent and should remain fixed.
4. The vector-first export and metadata sidecars are appropriate.
5. The evidence taxonomy is correctly separated:
   - exact theorem curves;
   - certified intervals;
   - numerical corroboration;
   - schematics.
6. No finite diagonal sampling is being used as theorem evidence.
7. The (m=0.35) point is a substantially better mathematical anchor than (m=0.21).

## Figure-by-figure Chief decisions

### FIG-01 — Matignon versus Hurwitz

**Verdict:** ACCEPT WITH MINOR VISUAL FIX.

Strengths:
- immediate geometric message;
- correct semantic colors;
- strong introductory value.

Required fix:
- panel (a) must not be titled merely “generic (0<\alpha<1)” while being drawn at a specific angle. Use either:
  - “representative order, (\alpha=0.75)”, or
  - remove the numerical geometry and make the rays intentionally symbolic.

Preferred: label it explicitly as representative (alpha=0.75).

Optional refinement:
- reduce the saturation/opacity of the large background regions slightly so the Matignon wedge remains the dominant object.

### FIG-02 — dimension two versus dimension three

**Verdict:** ACCEPT.

Strengths:
- very clear C-07/C-09 message;
- good visual contrast between codimension-one and open band;
- works as a theorem figure.

Page-economy option:
- FIG-01 and FIG-02 may later be combined into one compact conceptual figure if needed.

### FIG-03 — exact C-10 threshold geometry

**Verdict:** FREEZE SCIENTIFIC CONTENT; MINOR TYPOGRAPHIC POLISH ONLY.

This is one of the flagship figures.

Strengths:
- exact theorem geometry is obvious;
- log scaling is effective;
- symmetric and asymmetric slices complement one another;
- certified anchors reinforce rather than replace the theorem.

Keep in final paper.

Possible micro-fix:
- slightly reduce legend footprint in panel (b), if manuscript typesetting makes it crowded.

### FIG-04 — alpha deformation

**Verdict:** SCIENTIFICALLY ACCEPTED; REDESIGN FOR DENSITY.

The mathematics is valuable but the current three-panel layout is visually dense.

Required Wave-2 objective:
- create a cleaner two-panel main-paper candidate:
  1. global (T_\alpha/T_1) deformation;
  2. classical-limit zoom with C-14 asymptotic.
- the low-order C-15 asymptotic should remain available as a third candidate panel, but the paper should include it only if page space permits.

Important:
- there will be **no supplementary material**. If a panel is omitted from the paper, its mathematical statement must remain adequately covered in the main text.

Also fix the long orange annotation in current panel (c), which visually competes with the curves.

### FIG-05 — ecological no-go versus IGP mechanism

**Verdict:** ACCEPT WITH DESIGN POLISH.

Conceptually excellent.

Required refinements:
- reduce the amount of algebra in the lower boxes;
- keep only the decisive cycle-sign identities and final implication;
- align node/arrow geometry more symmetrically;
- reduce headline size slightly;
- maintain red for no-go and green for successful realization;
- keep the graph-theoretic message readable before the equations.

This should look like a mathematical network diagram, not a slide infographic.

### FIG-06 — Double-Allee (m)-path

**Verdict:** FREEZE AS FLAGSHIP FIGURE, WITH SMALL ANNOTATION CLEANUP.

This is the strongest narrative figure produced in Wave 1.

Strengths:
- one-control-parameter mechanism is immediately visible;
- exact Cain crossing and fractional margin are simultaneously visible;
- panel (b) makes the invariant-space geometry intuitive.

Required micro-fixes:
- simplify panel (a) annotations to reduce label competition;
- keep the exact crossing (m_0), classical point, anchor, and feasibility-loss indication;
- avoid adding further labels.

Keep in final paper.

### FIG-07 — certified biological anchor

**Verdict:** DO NOT FREEZE. REBUILD IN WAVE 2.

The current figure is scientifically correct but too dense for a main-paper figure and visually exposes a weakness of the current constructive witness:

[
Z/X \approx 1.3\times 10^{-3}.
]

This is mathematically harmless, but the four-panel presentation invites the reader to interpret the parameter choice biologically.

Wave-2 objectives:
1. search for a re-embedded biological witness with less extreme coexistence-density separation;
2. retain comfortable certified C-10/Cain margins;
3. retain an (m)-driven crossing with all non-(m) parameters fixed;
4. redesign the final anchor figure to at most 3 panels.

Preferred final composition:
- coexistence/parameter summary;
- certified margins;
- spectral-angle corroboration.

The time-domain linearized Caputo panel is optional and should be dropped if it weakens page economy.

### FIG-08 — exact 2D/3D contrast

**Verdict:** ACCEPT CONCEPT; REDESIGN PANEL (b).

Panel (a) is strong and should stay.

Panel (b) currently looks like a pixel classification map. Although it uses exact formulas pointwise, its visual language resembles a simulation heatmap rather than a theorem figure.

Wave-2 objective:
- replace the coarse grid appearance with smooth boundary continuation/root tracing where possible;
- use light filled regions bounded by smooth curves;
- preserve the certified (K=1.1) segment and the selected anchor;
- clearly label the full region as formula-evaluated, not interval-certified.

## Main-paper figure hierarchy after Wave 1

### Tier 1 — non-negotiable
- FIG-03 exact C-10 geometry
- FIG-06 Double-Allee crossing

### Tier 2 — very likely main paper
- FIG-01 Matignon/Hurwitz
- FIG-02 dimension contrast
- FIG-05 ecological mechanism
- FIG-08 2D/3D ecological contrast

### Tier 3 — include after Wave-2 redesign / page test
- FIG-04 alpha deformation
- FIG-07 certified anchor

## Page-budget policy

The manuscript has a hard 25-page total ceiling and no supplementary material.

Therefore:
- do not automatically include all eight Wave-1 figures unchanged;
- target approximately 6–7 figure environments;
- combine conceptual figures if needed;
- prefer multi-panel figures that directly serve theorem narrative;
- omit redundant visualization before compressing theorem proofs beyond readability.

Potential final compression:
- combine FIG-01 + FIG-02;
- redesign FIG-07 as a compact 2–3 panel figure;
- keep FIG-04 to two panels if retained.

## Biological anchor policy

The (m=0.35) Wave-1 anchor is accepted as a mathematically robust backup.

However, Wave 2 should search for a **less scale-separated coexistence witness**.

This is not a realism/calibration claim. The goal is to avoid an unnecessarily extreme illustrative realization when the theorem provides substantial re-embedding freedom.

Internal target:
- ideally both (Y/X) and (Z/X) at least (10^{-2});
- preferably max/min coexistence density ratio <100;
- all biological parameters positive;
- efficiencies in ((0,1));
- comfortable strict-P and fractional-only margins;
- certified or interval-verifiable;
- (m)-crossing retained with all non-(m) parameters fixed.

If no such point is found without materially worsening robustness, keep the Wave-1 (m=0.35) anchor and state clearly that it is a constructive witness, not a calibrated ecosystem.

## Wave-2 scope

Wave 2 is authorized for:
- visual polish;
- compact re-layout;
- improved ecological re-embedding;
- smooth boundary continuation for FIG-08;
- regenerated captions/metadata;
- no theorem changes.

No new theorem discovery is required.

## Current visual status

```text
FIGURE WAVE 1:          ACCEPTED
SCIENTIFIC CONTENT:     PASS
VISUAL SYSTEM:          PASS
FLAGSHIP FIG-03:        FREEZE
FLAGSHIP FIG-06:        FREEZE
ANCHOR FIG-07:          REDESIGN
FIG-08 PANEL (b):       REDESIGN
FIG-04:                 SIMPLIFY
FIG-05:                 POLISH
FINAL FIGURE SET:       NOT YET FROZEN
```

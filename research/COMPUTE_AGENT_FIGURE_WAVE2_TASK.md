# Compute Agent Figure Wave 2 — Final visual refinement and biological re-embedding

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P1 — final manuscript visual gate  
**Repository:** \`maximilianolucius/fractional-d-stability-networks\`  
**Work branch:** \`agent/compute-figures-wave2-20260926\`  
**Base Chief visual-review SHA:** \`289b81a61d0a2528f1a30708b5f5102ccaaf0081\`

## Mission

Wave 1 passed. Wave 2 is a **targeted refinement**.

Do not regenerate the entire program blindly.

Your objectives are:

1. find a less scale-separated biological re-embedding if possible;
2. redesign the figures that the Chief marked as visually dense;
3. preserve the fixed semantic palette and theorem/evidence hierarchy;
4. leave a near-final main-paper figure set.

Read first:

1. \`research/CHIEF_VISUAL_REVIEW_WAVE1_2026-09-26.md\`
2. \`research/FIGURE_MASTERPLAN.md\`
3. \`research/FIGURE_STYLE_GUIDE.md\`
4. \`research/PAPER_BAGGAGE_CAPUTO_DOUBLE_ALLEE_3D.md\`
5. \`research/FIGURE_WAVE1_FINAL_REPORT.md\`
6. \`research/FIGURE_DATA_REGISTRY.md\`
7. \`research/FIGURE_CAPTIONS_DRAFT.md\`
8. \`research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md\`
9. \`research/THEOREM_C10_EXACT_3X3.md\`
10. \`research/THEOREM_C15_THRESHOLD_GEOMETRY.md\`

Do not modify theorem or claim files.

---

# Part A — biological re-embedding search

The current Wave-1 anchor is mathematically strong but has

\[
Z/X \approx 1.3\times10^{-3}.
\]

This is not a mathematical flaw, but it makes the illustrative community look unnecessarily scale-separated.

Search for an alternative constructive biological embedding that preserves the theorem mechanism while giving a less extreme coexistence profile.

## Required mathematical properties

For a candidate design, require:

- commensurate Caputo order \(\alpha=0.9\);
- positive biological parameters;
- \(0<e_1,e_2,e_3<1\);
- positive coexistence \(X,Y,Z\);
- \(0<m<X<K\);
- strict-P reduced matrix;
- exact or certified fractional-only classification;
- comfortable classical margin:
  \[
  \kappa-T_1(\beta)>0;
  \]
- comfortable fractional margin:
  \[
  T_{0.9}(\beta)-\kappa>0;
  \]
- all non-\(m\) parameters fixed along the \(m\)-branch;
- existence of a unique/transverse classical crossing along that local branch;
- biological feasibility on both sides of the crossing locally.

## Internal visual targets

These are **selection criteria only**, not biological realism claims.

Prefer:
- \(Y/X\ge10^{-2}\);
- \(Z/X\ge10^{-2}\);
- \(\max(X,Y,Z)/\min(X,Y,Z)<100\);
- preferably <30 if achievable without sacrificing robustness.

Do not force these if they create pathological parameters or very poor margins.

## Robustness targets

Prefer:
- relative classical margin \((\kappa-T_1)/T_1\ge0.10\);
- relative fractional margin \((T_{0.9}-\kappa)/T_{0.9}\ge0.20\);
- parameter-log sensitivity / conditioning not materially worse than the Wave-1 \(m=0.35\) anchor;
- coexistence away from feasibility boundaries.

## Search freedom

You may vary:
- the invariant target;
- \(s,c_1,c_2\);
- efficiencies;
- attacks;
- split parameter \(\xi\);
- \(a,K,X,m\);
- mortalities;
- the prescribed crossing point \(m_0\).

The theorem does not require preserving the exact Wave-1 parameterization.

However, the final design must retain the same theorem-level mechanism:
- fixed model except for \(m\);
- classical D-stable on one side;
- fractional-only on the other.

## Deliverable

Create:

\`computations/figures_wave2/data/reembedding_candidates.json\`

with at least:
- top 10 feasible candidates;
- metrics;
- reasons for rejection/selection.

Create:

\`research/FIGURE_WAVE2_REEMBEDDING_REPORT.md\`

with:
- whether a materially better witness exists;
- selected candidate;
- proof/certification status;
- comparison with Wave-1 \(m=0.35\).

If no candidate clearly improves the presentation, say so and retain Wave 1.

No cosmetic “improvement” is worth weakening theorem robustness.

---

# Part B — figure-specific final redesign

Keep FIG-03 and FIG-06 scientifically frozen except for small typography/annotation improvements.

## FIG-01

Required:
- replace “generic \(0<\alpha<1\)” with “representative order, \(\alpha=0.75\)” or equivalent;
- slightly lighten broad background fills if needed;
- keep exact wedge geometry.

## FIG-03

Do not alter theorem content.

Allowed:
- reduce legend footprint;
- small typography alignment.

## FIG-04

Produce a cleaner **two-panel main-paper candidate**:

Panel A:
- global \(T_\alpha/T_1\) versus \(\alpha\).

Panel B:
- classical-limit zoom showing C-14 linear asymptotic.

Also export the low-order C-15 panel separately as:

\`fig04c_low_order_asymptotic.*\`

Do not call it supplementary. It is simply an available optional main-text panel.

Remove long inline annotations that compete visually with curves.

## FIG-05

Redesign for journal elegance:
- retain two network panels;
- align node positions exactly;
- standardize arrow curvature;
- reduce lower algebra boxes to decisive identities only;
- emphasize:
  - \(L_3>0\Rightarrow\) no-go;
  - \(L_3<0\Rightarrow\) open-band access possible;
- smaller panel headings;
- no slide-like large prose blocks.

## FIG-06

Keep as flagship.

Required:
- reduce annotation density in panel (a);
- retain:
  - classical point;
  - exact crossing \(m_0\);
  - selected anchor;
  - feasibility endpoint;
- keep panel (b) geometry essentially intact.

If Wave-2 re-embedding changes the canonical biological design, regenerate FIG-06 consistently for the new design.

## FIG-07

Rebuild to at most **3 panels**.

If a better re-embedding is found, use it.

Preferred panels:
1. coexistence summary or compact density plot;
2. certified classical/fractional margins;
3. scale-invariant spectral-angle corroboration.

Drop the time-domain panel unless it materially improves the paper.

The figure must not imply that numerical dynamics prove all-D stability.

## FIG-08

Keep panel (a).

Redesign panel (b) so it no longer looks like a coarse pixel map.

Preferred method:
- trace classification boundaries as smooth curves using deterministic continuation/root solving in \(m\) or \(K\);
- fill regions lightly between traced boundaries;
- overlay the interval-certified segment;
- mark the selected anchor.

Evidence wording must remain precise:
- boundaries/regions may be numerical evaluations of exact formulas;
- only certified intervals should be called certified.

Do not use visual smoothing that changes the mathematical classification.

---

# Part C — final figure-set recommendation

Create:

\`research/FIGURE_FINAL_SET_RECOMMENDATION.md\`

The paper has:
- hard 25-page ceiling;
- no supplementary material.

Recommend:
- 6 or 7 figure environments maximum;
- any proposed merges;
- exact panel count.

The recommendation must prioritize:
1. theorem communication;
2. visual clarity;
3. ecological mechanism;
4. page economy.

Do not recommend “move to supplement”.

---

# Part D — final visual QA

For final candidates:

- inspect at 100% and 50%;
- grayscale;
- colorblind-safe semantics;
- one-column / two-column suitability;
- embedded/vector text;
- consistent font sizing;
- no clipped labels;
- no legend/data collisions;
- no rasterized equations in vector outputs.

Record results in:

\`research/FIGURE_WAVE2_FINAL_REPORT.md\`

---

# Output structure

Create:

\`computations/figures_wave2/\`

with:
- \`scripts/\`
- \`data/\`
- \`exports/pdf/\`
- \`exports/svg/\`
- \`exports/png/\`
- \`metadata/\`

Do not overwrite Wave-1 outputs. Wave 2 must be directly comparable.

---

# Tests

Add namespaced tests:

\`tests/test_figures_wave2.py\`

Minimum:
- selected re-embedding is feasible;
- strict-P;
- exact/C-10 margins positive;
- local m crossing exists and signs are correct;
- if new design adopted, FIG-06 exact crossing test;
- FIG-08 traced boundary classification checks on both sides;
- all required exports exist.

Run entire repository suite.

---

# Repository restrictions

Work only on:

\`agent/compute-figures-wave2-20260926\`

Do NOT modify:
- \`paper/\`
- theorem files
- \`research/CLAIMS.md\`
- novelty audit conclusions
- main

No merge.

---

# Final status

Return exactly one:

- \`FIGURE_WAVE2_PASS\`
- \`FIGURE_WAVE2_PASS_WITH_FIXES\`
- \`FIGURE_WAVE2_FAIL\`
- \`PARTIAL/BLOCKED\`

At completion report:
- branch;
- final SHA;
- tests;
- whether a better re-embedding was found;
- old vs new anchor comparison;
- figure-by-figure changes;
- final recommended 6–7 figure environments;
- remaining visual caveats.

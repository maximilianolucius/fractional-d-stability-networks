# Compute Agent Figure Wave 1 — Certified visual program

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P1 — manuscript construction  
**Repository:** \`maximilianolucius/fractional-d-stability-networks\`  
**Work branch:** \`agent/compute-figures-wave1-20260926\`  
**Base Chief SHA:** \`b5a6ebce3fd0ccf33b2245822dbd414a56a4bf61\`

## Mission

Build the reproducible computational and visual asset package for the manuscript.

This is a **figure-production and certification task**, not a theorem-discovery task.

Do not change theorem claims.

Do not rewrite the paper.

Do not weaken or strengthen mathematical statements silently.

Your job is to:
- generate theorem-faithful data;
- render publication-quality figures;
- certify the key ecological visual anchors;
- keep exact, certified, and numerical objects clearly separated.

Read first:

1. \`research/FIGURE_MASTERPLAN.md\`
2. \`research/FIGURE_STYLE_GUIDE.md\`
3. \`research/PAPER_BAGGAGE_CAPUTO_DOUBLE_ALLEE_3D.md\`
4. \`research/Q1_PAPER_ARCHITECTURE.md\`
5. \`research/THEOREM_C10_EXACT_3X3.md\`
6. \`research/THEOREM_C15_THRESHOLD_GEOMETRY.md\`
7. \`research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md\`
8. \`research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md\`
9. \`research/CLAIMS.md\`

Do not modify \`paper/\`.

---

# Required directory structure

Create:

\`computations/figures/\`

with:

- \`scripts/\`
- \`data/\`
- \`exports/pdf/\`
- \`exports/svg/\`
- \`exports/png/\`
- \`metadata/\`

Create also:

- \`research/FIGURE_DATA_REGISTRY.md\`
- \`research/FIGURE_CAPTIONS_DRAFT.md\`
- \`research/FIGURE_WAVE1_FINAL_REPORT.md\`

---

# Required figure set

Produce at least FIG-01 through FIG-08 as specified in \`research/FIGURE_MASTERPLAN.md\`.

## FIG-01 — Matignon versus Hurwitz geometry
Exact theorem visualization.

## FIG-02 — 2D versus 3D contrast
Exact theorem visualization.

## FIG-03 — C-10 exact threshold geometry
Use exact formulas only.

At minimum:
- symmetric slice;
- one asymmetric slice.

Do not derive the threshold by finite diagonal sampling.

## FIG-04 — alpha deformation of T_alpha
Use exact C-10/C-15 threshold evaluation.

Required:
- full alpha curve;
- near-alpha=1 zoom;
- compare with C-14 linear asymptotic;
- if practical, low-order C-15 asymptotic check.

## FIG-05 — ecological no-go versus IGP mechanism
Produce a clean network diagram programmatically or as vector output.

Must distinguish:
- failed competitive architecture;
- successful IGP architecture;
- signed 3-cycle mechanism.

## FIG-06 — Double-Allee m path through invariant space
This is a flagship figure.

Required:
- compute the coexistence branch;
- compute s(m), beta_ij(m), kappa(m);
- plot exact Cain gap:
  \[
  G_1(m)=\kappa(m)-T_1(\beta(m));
  \]
- plot fractional margin:
  \[
  G_\alpha(m)=T_\alpha(\beta(m))-\kappa(m);
  \]
- mark m0;
- mark one classical point;
- mark one robust fractional-only interior point.

Use exact formulas / high precision / certification where available.

## FIG-07 — robust certified biological anchor

Search within the already certified region for a manuscript-friendly point, preferably m in [0.30,0.40].

Selection criteria:
- positive coexistence with comfortable margins;
- not close to the classical boundary;
- not close to biological feasibility boundaries;
- visually reasonable state magnitudes;
- preferably better conditioning than m=0.21.

For the selected anchor:
- record all biological parameters;
- coexistence values;
- s;
- beta coordinates;
- kappa;
- T1;
- T_alpha;
- classical margin;
- fractional margin;
- direct scale-invariant spectral corroboration;
- interval/certified status if available.

Do not optimize for aesthetics at the expense of robustness.

## FIG-08 — exact 2D/3D Double-Allee contrast

Required:
- 2D codimension-one critical condition;
- 3D open-region slice / certified band.

Make the contrast mathematically explicit, not merely illustrative.

---

# Optional figures

If resources permit:
- C-11 sufficient versus C-10 exact;
- simplex optimizer geometry;
- band width versus alpha.

Do not let optional figures delay FIG-01…FIG-08.

---

# Visual quality requirements

Use the exact palette in \`research/FIGURE_STYLE_GUIDE.md\`.

No custom/random colors.

All figures:
- white background;
- consistent typography;
- vector-first;
- readable at journal scale;
- no rasterized labels;
- no decorative 3D;
- no rainbow colormap.

Perform:
- grayscale check;
- 50% scale readability check;
- colorblind-friendly review where practical.

---

# Export requirements

For every figure:
- PDF;
- SVG;
- PNG preview.

Use deterministic names:
- \`fig01_matignon_hurwitz\`
- \`fig02_dimension_contrast\`
- ...
- \`fig08_double_allee_2d_3d\`

If multi-panel, export both:
- complete figure;
- panel data separately where useful.

---

# Data provenance

For every figure create metadata recording:
- claim IDs supported;
- equations/formulas used;
- parameter values;
- whether each plotted object is:
  - EXACT THEOREM CURVE
  - CLOSED-FORM BOUNDARY
  - CERTIFIED COMPUTATION
  - CERTIFIED INTERVAL
  - NUMERICAL CORROBORATION
  - SCHEMATIC
- script path;
- data path;
- output paths.

A JSON sidecar per figure is preferred.

---

# Numerical standards

Use high precision for:
- near-boundary threshold evaluation;
- m-crossing location;
- comparison of T1 and T_alpha;
- certified anchor margins.

For direct spectral checks:
- never maximize raw spectral abscissa over an unnormalized positive diagonal cone;
- use eigenvalue angle or Re(lambda)/|lambda|;
- normalize diagonal scale explicitly.

Finite diagonal optimization is corroboration only.

---

# Certified anchor search

The paper should not use the fragile m=0.21 point as its primary biological example.

Search the certified interval and propose a point approximately m=0.30–0.40.

Return a ranked shortlist of 3 candidate anchors based on:
1. classical margin;
2. fractional margin;
3. positivity margin;
4. conditioning;
5. visual interpretability.

Do not create a formal “score” in the paper; ranking is internal only.

---

# Caption task

Draft one technical caption per figure in:

\`research/FIGURE_CAPTIONS_DRAFT.md\`

Each caption must state:
- what is plotted;
- what theorem/claim it supports;
- which curves are exact;
- which data are certified;
- which elements are numerical corroboration;
- the main takeaway.

---

# Tests

Add deterministic tests for figure-generating formulas where useful.

Minimum checks:
- FIG-03 threshold values agree with theorem formulas;
- FIG-04 monotonicity in alpha;
- FIG-06 m0 crossing equality;
- FIG-06 sign change on each side of m0;
- FIG-07 selected anchor satisfies both strict margins;
- FIG-08 2D equality formula.

Run the entire test suite before finalizing.

---

# Repository discipline

Work only on:

\`agent/compute-figures-wave1-20260926\`

Allowed modifications:
- \`computations/figures/\`
- \`research/FIGURE_*.md\`
- new namespaced figure tests
- reusable plotting utilities under \`src/fdsn/\` if needed

Forbidden:
- \`paper/\`
- theorem files
- claim wording
- novelty audit conclusions
- main branch

Commit by phase.

Suggested commits:
1. figure infrastructure + style;
2. FIG-01…FIG-04;
3. FIG-05…FIG-08;
4. certified anchor + captions;
5. final QA/report.

---

# Final status

Return exactly one:

- \`FIGURE_WAVE1_PASS\`
- \`FIGURE_WAVE1_PASS_WITH_FIXES\`
- \`FIGURE_WAVE1_FAIL\`
- \`PARTIAL/BLOCKED\`

A PASS requires:
- FIG-01…FIG-08 exported in PDF/SVG/PNG;
- metadata/data registry complete;
- captions drafted;
- full tests green;
- no theorem claim modified.

At completion push the branch and report:
- branch;
- final SHA;
- tests passed/failed;
- figure inventory;
- selected robust anchor;
- any unresolved visual or numerical issue;
- recommended final-paper subset.

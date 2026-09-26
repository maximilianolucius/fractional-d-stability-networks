# Manuscript Storyboard — Post Visual Wave 1

**Date:** 2026-09-26  
**Owner:** Chief Researcher  
**Branch:** \`chief/manuscript-prep-20260926\`  
**Purpose:** freeze the theorem-first narrative, figure placement, and page budget before final LaTeX drafting.

## Global constraints

- hard ceiling: 25 journal-formatted pages total;
- target: 22–23 pages;
- no supplementary material;
- published references only;
- theorem-first structure;
- ecological model is an exact realization theorem, not a model-first paper;
- target 6 figure environments, with one optional seventh panel only if the final page budget permits.

## Scientific arc

The paper should read as one continuous argument:

\[
\text{classical D-stability}
\to
\text{positive-diagonal Matignon stability}
\to
\text{2D obstruction}
\to
\text{exact 3D threshold}
\to
\text{threshold geometry}
\to
\text{non-GLV ecological realization}
\to
\text{Double-Allee crossing mechanism}.
\]

The ecological block must feel inevitable after the matrix theory, not appended.

---

# Proposed page budget

## Front matter — 0.8 page

- title;
- abstract;
- keywords;
- MSC.

No figure.

## 1. Introduction and closest literature — 2.3 pages

### Goals
- classical D-stability;
- fractional Matignon sector;
- why positive-diagonal robustness is different from fixed-Jacobian stability;
- exact closest prior art;
- contribution list.

### Figure
**FINAL FIGURE ENVIRONMENT F1:** combine Wave-1 FIG-01 and FIG-02 into one compact conceptual figure.

Suggested panels:
- (a) Hurwitz versus Matignon sector;
- (b) 2D codimension-one obstruction;
- (c) 3D open fractional-only band.

Do not use four panels if three suffice.

### End-of-section contribution paragraph
State the theorem spine explicitly.

---

## 2. Positive-diagonal fractional stability framework — 1.6 pages

### Content
- definitions of \(\Sigma_\alpha\), \(\mathcal F_\alpha^{(n)}\), \(\mathcal D_H^{(n)}\), \(\mathcal P_\alpha^{(n)}\);
- positive diagonal action;
- C-16 simplex reduction;
- normalized principal-minor invariants.

No new figure unless absolutely needed.

The C-16 general \(n\) statement should be concise.

---

## 3. Dimension two: exact obstruction — 1.0 page

### Content
- C-07 exact classification;
- fractional-only equality set;
- empty full-dimensional interior.

Reuse F1 panel (b); do not create another figure.

Conclude with the question:
> does dimension three create a genuinely open difference class?

---

## 4. Dimension three: exact characterization — 3.5 pages

### Content
- strict-P robust stratum;
- normalized cubic;
- simplex reduction;
- C-10 exact threshold;
- classical Cain boundary;
- exact fractional-only band.

### Figure
**F2:** Wave-1 FIG-03, essentially frozen.

This is a flagship theorem figure.

### Proof economy
Keep one full proof spine in the main article.
Avoid repeating fixed-cubic algebra in multiple forms.

---

## 5. Geometry and order dependence of the threshold — 3.0 pages

### Content
- C-15 strict logit convexity;
- unique/nondegenerate optimizer;
- smooth threshold surface;
- C-14 \(\alpha\to1^-\) collapse;
- C-15 \(\alpha\downarrow2/3^+\) behavior;
- C-09 minimum dimension as consequence.

### Figure
**F3:** redesigned Wave-2 FIG-04, preferably two panels:
- global \(T_\alpha/T_1\);
- classical-limit asymptotic.

If the low-order asymptotic panel is not included, state the expansion clearly in text.

No supplement.

---

## 6. Exact Caputo Double-Allee ecological realization — 4.5 pages

This is the main application/theorem-realization section.

### 6.1 Kolmogorov orbit bridge
- positive equilibrium;
- \(J=\operatorname{diag}(x^*)B\);
- exact orbit equivalence.

Keep short; not novelty.

### 6.2 Why the naive ecological architecture fails
- two competing consumers;
- cycle sign;
- no-go theorem.

### 6.3 Intraguild-predation realization
- canonical Caputo model;
- coexistence equations;
- exact reduced matrix;
- \(\beta_{ij},\kappa,L_3\);
- invariant realization.

### Figure
**F4:** redesigned FIG-05.

Place immediately after no-go + IGP theorem.

### 6.4 Open biological fractional-only theorem
- quantified Double-Allee embedding;
- full-dimensional IFT openness;
- high-order and low-order cases.

### 6.5 Allee-threshold mechanism
- \(q=\Delta(s+\chi)\);
- \(dX/dm<0\);
- \(ds/dm<0\);
- invariant path;
- unique/transverse Cain crossing.

### Figure
**F5:** FIG-06, flagship.

Place immediately after the crossing theorem.

### 6.6 Exact 2D/3D ecological contrast
- codimension-one 2D;
- open 3D.

### Figure
**F6:** merged final environment combining FIG-08(a,b) with FIG-07(b,c): exact 2D/3D contrast, certified margins, and spectral corroboration.

This closes the ecological/numerical narrative.

---

## 7. Certified realization and numerical corroboration — 1.4 pages

### Purpose
Record the W2-A certified witness without creating an extra figure environment.

### Content
- W2-A parameter table;
- certified margins;
- interval-certified (m)-range;
- explanation of what the spectral panel corroborates and what it does not prove.

The visual material is already contained in **F6**.

No separate Figure 7 is required by default.

---

## 8. Discussion and conclusion — 1.3 pages

### Discussion
- what the fractional order changes;
- why dimension 3 is the first robust dimension;
- why signed three-cycles matter;
- model limitations;
- no global nonlinear-stability claim;
- no empirical calibration claim;
- \(n\ge4\) frontier.

### Conclusion
One compact paragraph summarizing:
- exact matrix classification;
- dimension threshold;
- ecological realization;
- Allee-driven crossing.

No new figure.

---

## References and declarations — 2.5 pages target

Published references only.

Forbidden:
- arXiv/preprints;
- working papers;
- unpublished/submitted manuscripts;
- technical drafts;
- personal communications.

All DOI/publisher metadata verified.

---

# Final figure hierarchy

## F1 — conceptual foundation
Merged FIG-01(b) + FIG-02(a,b).

## F2 — exact C-10 threshold geometry
FIG-03.

## F3 — threshold deformation in alpha
Wave-2 FIG-04 two-panel redesign.

## F4 — ecological no-go versus IGP mechanism
Wave-2 FIG-05.

## F5 — Double-Allee crossing
Wave-2 FIG-06 with W2-A.

## F6 — certified realization and exact 2D/3D contrast
Merged FIG-08(a,b) + FIG-07(b,c).

Total: **6 figure environments / 14 panels**.

Optional only if the final page budget permits: standalone FIG-04c low-order asymptotic panel.

If final typesetting exceeds 23 pages:
1. compress F1;
2. reduce F3 to one panel + textual asymptotic;
3. reduce F7 to two panels;
4. omit redundant visual information before compressing theorem prose.

Do not move anything to supplementary material.

---

# Figure narrative rule

Every figure must be introduced in the preceding paragraph with a mathematical reason for its existence.

Avoid:
> “Figure 3 shows…”

Prefer:
> “The variational threshold admits a direct geometric interpretation: on both symmetric and asymmetric slices, the Matignon boundary remains strictly above Cain's surface, exposing the open difference band (Figure 3).”

Figures must be cited after the theorem/result they visualize, never before the mathematics that justifies them.

---

# Abstract narrative target

The abstract should eventually contain four conceptual beats:

1. define positive-diagonal Matignon stability;
2. give exact dimension-three characterization and dimension threshold;
3. state exact nonlinear Caputo Double-Allee ecological realization;
4. state that varying the Allee threshold alone can cross the classical Cain boundary into an open fractional-only robust region.

Do not mention computational stress tests in the abstract.

---

# Title direction

Current strongest title family:

**From Cain to Matignon: Exact Three-Dimensional D-Stability Thresholds and a Nonlinear Caputo Ecological Realization**

Alternative:

**Fractional D-Stability Beyond Hurwitz Stability: Exact Three-Dimensional Theory and a Double-Allee Kolmogorov Realization**

Do not freeze title until final frozen-claim novelty/bibliography audit.

---

# Current Chief manuscript state

\`\`\`text
THEOREM PACKAGE:         FROZEN
EXTERNAL PROOF GATE:     PASS
VISUAL WAVE 1:           PASS
VISUAL WAVE 2:           PASS
MANUSCRIPT STORYBOARD:   FROZEN
FINAL FIGURE SET:        FROZEN (6 ENVIRONMENTS)
CANONICAL WITNESS:       W2-A
BIBLIOGRAPHY GATE:       NEXT
LATEX FULL DRAFT:        NOT YET STARTED
\`\`\`

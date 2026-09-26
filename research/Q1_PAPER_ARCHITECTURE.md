# Provisional Q1 paper architecture — Chief Researcher

**Date:** 2026-09-26  
**Status:** architecture approved for drafting; Double-Allee external proof gate passed. Submission readiness still depends on final novelty/bibliography/editorial gates.

## Scientific center

The paper should **not** be framed as "fractional stability of an ecological model".

Its mathematical center is:

> Exact positive-diagonal Matignon stability in dimensions two and three, the first full-dimensional genuinely fractional class at dimension three, the exact fractional deformation of Cain's 3x3 D-stability boundary, and an exact non-GLV Caputo ecological realization in which a double-Allee threshold drives a transverse transition from classical D-stability into the fractional-only band.

## Flagship theorem package

### Proposition 0 — general positive-diagonal orbit reduction (C-16)

For strict-P(-A) in dimension n, positive diagonal scaling modulo common scalar is exactly the open simplex

\[
\Delta_{n-1}^\circ.
\]

The normalized characteristic polynomial depends only on the normalized principal-minor invariants \(\beta_I\), with exactly

\[
2^n-n-1
\]

nontrivial orbit invariants.

This is structural machinery, not the main novelty. It makes explicit that the difficult part of the project is dimension-specific root geometry, not the diagonal multiplier itself.

### Theorem A — exact 2x2 obstruction (C-07)

For every \(0<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(2)}
\iff
\det A>0,\quad a_{11}\le0,\quad a_{22}\le0.
\]

The genuinely fractional difference class has empty full-dimensional interior.

### Theorem B — exact robust 3x3 characterization (C-10)

On the full-dimensional strict-P(-A) stratum, the positive diagonal orbit is represented exactly by four invariants

\[
(\beta_{12},\beta_{13},\beta_{23},\kappa)
\]

and a two-dimensional simplex.

For \(2/3<\alpha<1\),

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
}
\]

For \(0<\alpha\le2/3\), strict-P(-A) is sufficient and, for interior points, necessary.

### Theorem C — geometry of the exact threshold (C-15)

For \(2/3<\alpha<1\), the logarithm of the C-10 threshold objective is globally **strictly convex in logit simplex coordinates**.

Consequences:

- the optimizer \(x^*(\alpha,\beta)\) is unique and nondegenerate;
- \(T_\alpha(\beta)\) is smooth;
- symmetric and two-equal slices reduce exactly;
- the whole threshold surface admits an explicit global \((x,r)\)-parametrization;
- every invariant point above the classical Cain surface is realizable by a real matrix;
- as \(\alpha\downarrow2/3\),
  \[
  T_\alpha(\beta)
  =
  \frac{27}{K^3}
  +
  \frac{9\sum\beta_{ij}-27}{K^2}
  +
  O(K^{-1}),
  \qquad
  K=1-4\cos^2(\alpha\pi/2).
  \]

### Corollary D — exact fractional deformation of Cain

At \(\alpha=1\),

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+\sqrt{\beta_{13}}
+\sqrt{\beta_{23}}
\right)^2,
\]

which recovers Cain's exact strict-P 3x3 threshold.

For \(2/3<\alpha<1\),

\[
T_\alpha(\beta)>T_1(\beta),
\]

so the exact genuinely fractional band is

\[
T_1(\beta)<\kappa<T_\alpha(\beta).
\]

### Corollary E — minimum robust dimension (C-09)

For every \(0<\alpha<1\),

\[
\boxed{
\min\{n:
\operatorname{int}(
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)}
)\ne\varnothing\}
=3.
}
\]

This should be presented as a major consequence of Theorems A and B.

### Corollary F — ecological loop coordinates and sensitivity (C-12/C-13)

For three-species GLV systems,

\[
J=\operatorname{diag}(x^*)A
\]

has the same orbit invariants as \(A\).

Moreover,

\[
\beta_{ij}
=
1-\frac{a_{ij}a_{ji}}{p_ip_j},
\]

and

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3,
\]

where \(L_3\) is the total normalized directed three-cycle feedback.

Thus the exact genuinely fractional band has an exact feedback-motif representation.

Using C-15 uniqueness, the pair-loop sensitivity is explicit:

\[
\frac{\partial T_\alpha}{\partial\beta_{ij}}
=
\frac{h_\alpha'(B^*)}{x_k^*}
>0,
\qquad
\{i,j,k\}=\{1,2,3\},
\]

at fixed \(\kappa\).

### Corollary G — quantitative memory width (C-14)

For \(2/3<\alpha<1\), \(T_\alpha(\beta)\) is strictly decreasing in \(\alpha\), and

\[
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2)
\]

as \(\alpha\to1^-\).

This quantifies the collapse of the memory-only band toward classical D-stability.

## Suggested section order

1. **Introduction**
   - classical D-stability and abundance scaling;
   - Matignon stability region;
   - exact prior-art boundary: Matignon / Cain / Kushel / Siami;
   - theorem-first contribution summary.

2. **General orbit geometry**
   - \(\mathcal F_\alpha\), \(\mathcal D_H\), \(\mathcal P_\alpha\);
   - positive left-diagonal action;
   - C-16 simplex reduction in arbitrary dimension;
   - normalized principal-minor invariants;
   - GLV Jacobian orbit equivalence.

3. **Dimension two**
   - exact classification;
   - obstruction to robust genuinely fractional separation.

4. **Dimension three: orbit reduction**
   - P0 necessity;
   - strict-P robust stratum;
   - four invariants;
   - simplex representation.

5. **Exact fractional 3x3 criterion and threshold geometry**
   - fixed-cubic boundary;
   - variational threshold \(T_\alpha\);
   - necessary-and-sufficient theorem;
   - C-15 strict logit convexity and unique optimizer;
   - symmetry reductions and explicit threshold-surface parametrization;
   - realizability of the full invariant band.

6. **Classical and low-order limits; dimension threshold**
   - recovery of Cain;
   - \(T_\alpha>T_1\);
   - minimum dimension theorem;
   - C-14 \(\alpha\to1^-\) asymptotic rate;
   - C-15 \(\alpha\downarrow2/3\) blow-up;
   - \(\Phi\) certificate only as a simple sufficient corollary.

7. **Ecological network interpretation**
   - pair loops \(\beta_{ij}\);
   - directed 3-cycle coordinate \(L_3\);
   - GLV abundance invariance;
   - exact motif phase diagram;
   - exact pair-loop sensitivities.

8. **Computational validation and illustrations**
   - independent stress testing;
   - exact-threshold numerical implementation;
   - interval-certified anchor points;
   - adversarial high-precision audit of near-boundary cases;
   - no Monte Carlo as theorem evidence.

9. **Discussion**
   - what memory changes mathematically;
   - why dimension three is first;
   - relation to classical D-stability;
   - ecological meaning;
   - limitations and \(n\ge4\) frontier.

## Figures to produce after validation

1. Matignon region showing the Hurwitz half-plane and genuinely fractional sliver.
2. Dimension-two versus dimension-three threshold schematic.
3. Normalized cubic coefficient boundary.
4. General C-16 orbit-simplex reduction, specialized to the four C-10 invariants.
5. Convex C-10 threshold surface / unique optimizer geometry.
6. \(T_\alpha(\beta)\) versus \(\alpha\), showing both C-14 and C-15 asymptotic regimes.
7. Exact ecological motif phase diagram in \((L_3,\alpha)\) and selected pair-loop slices.
8. C-11 sufficient boundary versus exact C-10 boundary.

## Provisional title candidates

1. **From Cain to Matignon: Exact Three-Dimensional D-Stability Thresholds and a Nonlinear Ecological Realization**
2. **Fractional D-Stability Beyond Hurwitz Stability: Exact Dimension-Three Theory and a Double-Allee Kolmogorov Realization**
3. **Exact Positive-Diagonal Matignon Stability in Dimension Three with a Caputo Double-Allee Realization**

Titles remain provisional until the final frozen-claim novelty and bibliography audits are complete.

## Q1 quality gate

The Double-Allee proof gate and genuinely external audit are now passed. Before final submission require:

- frozen-claim specialist novelty audit of C-10/C-15 and the exact ecological realization/crossing claims;
- published-source-only bibliography: no arXiv/preprint/working-paper/unpublished references;
- exact DOI, theorem-number and sign-convention verification for every imported result;
- reproducible tests green;
- no central statement dependent on finite diagonal sampling;
- final referee-style rigor, novelty, bibliography, page-budget and visual audits.

If these gates pass, the theorem package is strong enough to justify targeting a serious Q1 venue rather than an application-first paper.

# Provisional Q1 paper architecture — Chief Researcher

**Date:** 2026-09-25  
**Status:** architecture only; final drafting locked pending independent validation.

## Scientific center

The paper should **not** be framed as "fractional stability of an ecological model".

Its mathematical center is:

> Exact positive-diagonal Matignon stability in dimensions two and three, the first full-dimensional genuinely fractional class at dimension three, the exact fractional deformation of Cain's 3x3 D-stability boundary, and its interpretation through ecological feedback loops.

## Flagship theorem package

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

### Corollary C — exact fractional deformation of Cain

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

### Corollary D — minimum robust dimension (C-09)

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

### Corollary E — ecological loop coordinates (C-12/C-13)

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

### Corollary F — quantitative memory width (C-14)

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

2. **Definitions and invariances**
   - \(\mathcal F_\alpha\), \(\mathcal D_H\), \(\mathcal P_\alpha\);
   - positive left-diagonal action;
   - GLV Jacobian orbit equivalence.

3. **Dimension two**
   - exact classification;
   - obstruction to robust genuinely fractional separation.

4. **Dimension three: orbit reduction**
   - P0 necessity;
   - strict-P robust stratum;
   - four invariants;
   - simplex representation.

5. **Exact fractional 3x3 criterion**
   - fixed-cubic boundary;
   - variational threshold \(T_\alpha\);
   - necessary-and-sufficient theorem.

6. **Classical limit and dimension threshold**
   - recovery of Cain;
   - \(T_\alpha>T_1\);
   - minimum dimension theorem;
   - C-14 asymptotic rate;
   - \(\Phi\) certificate only as a simple sufficient corollary.

7. **Ecological network interpretation**
   - pair loops \(\beta_{ij}\);
   - directed 3-cycle coordinate \(L_3\);
   - GLV abundance invariance;
   - exact motif phase diagram.

8. **Computational validation and illustrations**
   - independent stress testing;
   - exact-threshold numerical implementation;
   - certified anchor points if interval computation succeeds;
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
4. Simplex representation of the positive diagonal orbit.
5. \(T_\alpha(\beta)\) versus \(\alpha\), including C-14 linear asymptotic.
6. Exact ecological motif phase diagram in \((L_3,\alpha)\) and selected pair-loop slices.
7. C-11 sufficient boundary versus exact C-10 boundary.

## Provisional title candidates

1. **From Cain to Matignon: Exact Three-Dimensional D-Stability Thresholds for Fractional Dynamics**
2. **Exact Fractional D-Stability in Dimension Three and Its Ecological Feedback Structure**
3. **Fractional D-Stability Beyond Hurwitz Stability: Exact Dimension-Three Characterization**

Titles remain provisional until independent proof and novelty audits pass.

## Q1 quality gate

Before final prose drafting require:

- adversarial proof audit: PASS or PASS WITH MINOR FIX for C-07/C-09/C-10/C-11/C-14;
- high-compute wave: no persistent counterexample;
- final specialist novelty audit of C-10;
- exact citation and sign-convention verification for Cain, Matignon, Kushel/Kushel-Pavani, Siami, Cermak-Nechvatal, Bourafa et al.;
- reproducible tests green;
- no central statement dependent on finite diagonal sampling.

If these gates pass, the theorem package is strong enough to justify targeting a serious Q1 venue rather than an application-first paper.

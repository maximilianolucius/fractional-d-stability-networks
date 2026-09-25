# Provisional Q1 paper architecture — Chief Researcher

**Date:** 2026-09-24
**Status:** architecture only; final manuscript drafting locked pending independent proof audit

## Working scientific center

The paper should not be framed as "fractional stability of an ecological model".

Its mathematical center is:

> **Exact positive-diagonal Matignon stability in dimensions two and three, the emergence of a genuinely fractional full-dimensional class at dimension three, and the interpretation of the exact 3x3 orbit invariants as ecological feedback loops.**

## Provisional flagship theorem package

### Theorem A — exact 2x2 obstruction (C-07)

For every 0<alpha<1,

[
Ain F_alpha^{(2)}
iff
det A>0,quad a_{11}le0,quad a_{22}le0.
]

The genuinely fractional difference class has empty full-dimensional interior.

### Theorem B — exact robust 3x3 characterization (C-10)

On the full-dimensional strict-P(-A) stratum, the positive diagonal orbit is represented exactly by four invariants

[
(eta_{12},eta_{13},eta_{23},kappa)
]

and a two-dimensional simplex.

For 2/3<alpha<1,

[
Ain F_alpha^{(3)}
iff
kappa<T_alpha(eta).
]

For alpha<=2/3, strict-P(-A) is sufficient and, for interior points, necessary.

### Corollary C — exact fractional Cain deformation

At alpha=1,

[
T_1(eta)
=
(sqrt{eta_{12}}+sqrt{eta_{13}}+sqrt{eta_{23}})^2,
]

which is Cain's complete strict-P 3x3 threshold.

For every alpha<1,

[
T_alpha(eta)>T_1(eta)
]

in the high-order regime, and the gap collapses continuously as alpha->1.

### Theorem/Corollary D — minimal dimension (C-09)

For every 0<alpha<1,

[
min{n:operatorname{int}(F_alpha^{(n)}setminus D_H^{(n)})
eqarnothing}=3.
]

This should appear as a major consequence of Theorems A and B, not as an isolated construction.

### Corollary E — ecological loop coordinates (C-12/C-13)

For three-species GLV systems,

[
J=operatorname{diag}(x^*)A
]

has the same orbit invariants as A.

Moreover,

[
eta_{ij}=1-rac{a_{ij}a_{ji}}{p_ip_j},
]

and

[
kappa
=
eta_{12}+eta_{13}+eta_{23}-2-L_3,
]

where L_3 is the sum of the two normalized directed 3-cycle products.

Thus the exact genuinely fractional band becomes an exact motif inequality.

## Suggested section order

1. **Introduction**
   - D-stability and abundance scaling in ecology.
   - Fractional Matignon region.
   - Precise prior-art boundary: Matignon / Cain / Kushel / Siami.
   - Contributions stated theorem-first.

2. **Definitions and invariances**
   - F_alpha, D_H, P_alpha.
   - positive left diagonal action.
   - GLV Jacobian orbit equivalence.

3. **Dimension two**
   - exact classification.
   - obstruction to robust genuinely fractional separation.

4. **Dimension three: orbit reduction**
   - P0 necessity.
   - strict-P robust stratum.
   - four invariants.
   - simplex representation.

5. **Exact fractional 3x3 criterion**
   - fixed-cubic boundary.
   - variational threshold T_alpha.
   - necessary-and-sufficient theorem.

6. **Classical limit and dimension threshold**
   - recovery of Cain.
   - T_alpha>T_1.
   - minimal dimension theorem.
   - simple Phi certificate as an interpretable sufficient corollary, not central theorem.

7. **Ecological network interpretation**
   - pair loops beta.
   - directed 3-cycle coordinate L_3.
   - GLV abundance invariance.
   - motif phase diagram.

8. **Numerical illustrations**
   - only theorem illustrations / boundary validation.
   - no Monte Carlo promoted as proof.
   - compare exact T_alpha against Phi sufficient certificate and Siami cyclic slice.

9. **Discussion**
   - what memory changes mathematically.
   - why n=3 is first robust dimension.
   - relation to classical D-stability.
   - limitations: n>=4 remains open.

## Figures worth producing later

1. Complex-plane Matignon region showing Hurwitz half-plane plus genuinely fractional sliver.
2. 2x2 vs 3x3 dimension-threshold schematic.
3. Normalized coefficient plane for the exact cubic boundary.
4. Simplex representation of the 3x3 diagonal orbit with stable/unstable boundary.
5. T_alpha(beta) versus alpha, showing convergence to Cain.
6. Ecological motif diagram mapping beta pair-loops and L_3 to the fractional-only band.

## Provisional title candidates

1. **Fractional D-Stability Beyond Hurwitz Stability: An Exact Three-Dimensional Characterization**
2. **Exact Fractional D-Stability in Dimension Three and Its Ecological Loop Structure**
3. **From Cain to Matignon: Exact 3x3 D-Stability Thresholds for Fractional Dynamics**

The title should remain provisional until proof audit and final novelty audit pass.

## Q1 quality gate

Before prose drafting, require:

- independent proof audit: PASS or PASS WITH MINOR FIX for C-07/C-09/C-10/C-11;
- final specialist novelty audit of C-10;
- exact citations/theorem numbers for Cain, Bahl-Cain, Matignon, Kushel/Kushel-Pavani, Siami, Cermak-Nechvatal, Bourafa et al.;
- reproducible tests green;
- no central statement dependent on finite diagonal sampling.

If these gates pass, the mathematical content is strong enough to justify targeting a serious Q1 venue rather than writing an application-first paper.

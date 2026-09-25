# C-10 targeted novelty audit — exact 3x3 variational characterization

**Date:** 2026-09-24
**Role:** Chief Researcher
**Target:** `research/THEOREM_C10_EXACT_3X3.md`
**Verdict:** **NOVELTY SURVIVES TARGETED SEARCH — PROVISIONAL, INCLUDING LOW-DIMENSIONAL INERTIA/SECTOR PREDECESSORS**

## Exact object audited

For real 3x3 matrices on the full-dimensional strict-P(-A) stratum, the project eliminates the entire positive left-diagonal orbit modulo common scale and represents it by the open simplex

[
x_i=rac{p_i d_i}{a_D},qquad x_i>0,quad sum_i x_i=1.
]

The orbit is determined by four positive invariants

[
eta_{12}=rac{m_{12}}{p_1p_2},quad
eta_{13}=rac{m_{13}}{p_1p_3},quad
eta_{23}=rac{m_{23}}{p_2p_3},quad
kappa=rac{-det A}{p_1p_2p_3}.
]

For 2/3<alpha<1 the exact theorem is

[
Ain F_alpha^{(3)}
iff
kappa<T_alpha(eta),
]

where

[
T_alpha(eta)
=
min_{xinDelta_2^circ}
rac{h_alpha(B_eta(x))}{x_1x_2x_3}
]

and (h_alpha) is the exact normalized cubic Matignon boundary.

The same theorem gives

[
operatorname{int}P_alpha^{(3)}
=
{A:-A	ext{ strict P}, T_1(eta)<kappa<T_alpha(eta)}.
]

At alpha=1,

[
T_1(eta)=
(sqrt{eta_{12}}+sqrt{eta_{13}}+sqrt{eta_{23}})^2,
]

recovering Cain's exact 3x3 D-stability threshold.

## Closest prior art

### Cain 1976

Cain gives a complete characterization of real 3x3 classical D-stable matrices. The project must credit this result as the alpha=1 endpoint.

The current result is not a rediscovery of Cain: it constructs the alpha-dependent Matignon threshold (T_alpha) and proves exact positive-diagonal-orbit equivalence for all 2/3<alpha<1.

### Cain 1984 / Hartfiel / robust D-stability

These works study interiors and robust classical D-stability. They occupy the topology/robustness concepts, but not the fractional Matignon threshold.

### Kushel 2019; Kushel-Pavani 2020/2021

The generalized-D-stability framework permits arbitrary spectral regions and multiplier classes. The forbidden-boundary theorem says, abstractly, that region D-stability is equivalent to stability plus avoidance of the region boundary under all positive diagonal multipliers.

This is the closest conceptual framework.

What was not located there is the present low-dimensional elimination:

- no normalization of the complete 3x3 positive diagonal orbit to a simplex;
- no four-invariant reduction ((eta_{12},eta_{13},eta_{23},kappa));
- no exact scalar threshold (T_alpha(eta));
- no exact fractional-only band between (T_1) and (T_alpha).

Thus C-10 can be viewed as an explicit solution of the generalized forbidden-boundary problem for the 3x3 Matignon region on its robust stratum.

### Fractional Routh-Hurwitz literature

Cermak-Nechvatal and Bourafa-Abdelouahab-Moussaoui provide exact fixed-polynomial fractional root-location criteria. Joya-Furuta and related coefficient-domain work also characterize polynomial sector stability.

These results occupy the fixed-cubic component (h_alpha).

They do not quantify over (D), do not eliminate (D), and do not produce a matrix-orbit invariant necessary-and-sufficient criterion.

### Bahl-Cain 1977 — inertia of diagonal multiples

C. A. Bahl and B. E. Cain, *The inertia of diagonal multiples of 3x3 real matrices*, Linear Algebra and its Applications 18(3) (1977), 267-280, DOI 10.1016/0024-3795(77)90056-8.

This is a particularly close low-dimensional predecessor: it characterizes classes of 3x3 real matrices whose inertia is preserved under every positive diagonal multiplier, using algebraic conditions on principal minors.

**Overlap:** exact low-dimensional positive-diagonal-orbit classification.

**Non-overlap:** inertia records the counts of eigenvalues in left/right half-planes and on the imaginary axis. C-10 requires angular localization relative to the Matignon rays inside a non-half-plane region, produces an alpha-dependent threshold, and isolates spectra that may lie in the right-half-plane sliver while remaining fractionally stable.

Thus Bahl-Cain is mandatory positioning but does not imply C-10.

### Joya-Furuta 1991 — sector-stable polynomial coefficient domains

K. Joya and K. Furuta, *A Necessary and Sufficient Condition for the D-Stability of Convex Combinations of D-Stable Polynomials*, Trans. SICE 27(3) (1991), 298-305, DOI 10.9746/sicetr1965.27.298.

They derive explicit coefficient-space descriptions for monic polynomials whose roots lie in prescribed convex domains including sectors.

**Overlap:** exact sector root-location in polynomial coefficient space.

**Non-overlap:** no positive-diagonal matrix orbit, no principal-minor orbit invariants, no GLV row-scaling interpretation, and no deformation of the 3x3 Cain matrix criterion.

### Siami 2020/2021

Siami gives an exact/sufficient fractional secant condition for the single-cycle family. This is recovered as a structured slice of C-10, not the source of novelty.

Indeed, for the symmetric cyclic family (A_gamma), C-10 reproduces the exact Siami threshold while also applying to unrestricted perturbations and arbitrary strict-P 3x3 matrices.

## Searches performed

Targeted searches included combinations of:

- 3x3 fractional D-stability necessary sufficient;
- sector D-stability 3x3 principal minors;
- generalized D-stability three-dimensional sector;
- inertia of diagonal multiples of 3x3 matrices;
- D-stable polynomials in sector coefficient domains;
- Matignon positive diagonal scaling principal minors;
- forbidden boundary 3x3 cubic;
- fractional D-stability Routh-Hurwitz diagonal scaling.

No equivalent theorem was found.

## Novelty boundary

Do not claim novelty for:

- fixed-cubic Matignon/Routh-Hurwitz boundary (h_alpha);
- Cain's alpha=1 criterion;
- generalized D-stability;
- the forbidden-boundary principle;
- the simplex as a generic normalization trick.

The candidate novelty is the **combined exact elimination theorem**:

> on the full-dimensional 3x3 stratum, the complete positive-diagonal Matignon-stability problem reduces exactly to four orbit invariants and one explicit two-dimensional variational threshold, continuously deforming Cain's criterion and giving an exact genuinely fractional band.

## Residual risk

The residual risk is an older low-dimensional generalized-region D-stability paper that contains an equivalent coefficient/orbit elimination under different terminology. No such result was located in the targeted search.

A final independent specialist literature audit is still required before submission.

## Verdict

**NOVELTY SURVIVES TARGETED SEARCH — PROVISIONAL**

Mathematical status: internally proved.
Research value: potentially stronger than C-09 because it explains and generalizes the dimension-threshold theorem.
Publication strategy: elevate C-10 beside C-09 as a flagship theorem package, pending adversarial proof audit and final independent novelty verification.

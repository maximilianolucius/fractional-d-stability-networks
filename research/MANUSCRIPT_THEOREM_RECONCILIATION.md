# Manuscript theorem reconciliation

Branch: q1-manuscript-20260925  
Purpose: map every load-bearing manuscript statement to the independently audited canonical theorem package.

## Reconciliation table

| Manuscript statement | Canonical source | Manuscript location | Reconciliation |
|---|---|---|---|
| Exact 2x2 classification | C-07 | Sec. 3, thm:2x2 | MATCH |
| Empty interior in n=2 | C-07 | Sec. 3, cor:2x2-empty-interior | MATCH |
| General simplex/orbit reduction | C-16 | Sec. 2, lem:simplex-reduction | MATCH; explicitly structural/non-novel |
| Exact fixed-cubic ray boundary | C-10 fixed-cubic lemma | Sec. 4, lem:cubic-boundary | MATCH |
| Exact strict-P 3x3 criterion kappa<T_alpha | C-10 | Sec. 4, thm:C10 | MATCH |
| P0 necessity | C-10/P0 | Sec. 4, lem:P0 | MATCH |
| Strict-P necessity for interior | C-10 | Sec. 4, cor:strictP-interior | MATCH |
| Complete interior classification | C-10 | Sec. 4, thm:interior-F | MATCH |
| Cain endpoint T1=(sum sqrt beta)^2 | Cain + C-10 | Sec. 4 | MATCH |
| Exact genuinely fractional band | C-10 | Sec. 4, cor:exact-band | MATCH |
| Strict logit convexity / unique optimizer | C-15 | Sec. 5, thm:strict-convexity | MATCH |
| Symmetric slice and Siami identity | C-15 | Sec. 5, cor:symmetric-slice | MATCH |
| Canonical cyclic family | C-10/C-15 + Siami | Sec. 5, cor:cyclic-family | MATCH |
| Two-equal symmetry reduction | C-15 | Sec. 5 | MATCH |
| Global threshold-surface parametrization | C-15 | Sec. 5, thm:parametrization | MATCH; inverse identities included after proof audit |
| Exact dT/dbeta sensitivity | C-13 strengthened by C-15 | Sec. 5, cor:sensitivity | MATCH |
| Strict monotonicity in alpha | C-14 | Sec. 5, thm:alpha-monotonicity | MATCH |
| Sharp alpha->1 rate | C-14 | Sec. 5, thm:C14 | MATCH |
| Alpha->2/3+ blow-up | C-15 | Sec. 5, thm:loworder | MATCH |
| Exact Phi orbit minimum | C-11 | Sec. 5, prop:Phi | MATCH |
| Fractional Phi>rho_alpha certificate | C-11 | Sec. 5, cor:Phi-certificate | MATCH |
| C-11 asymptotic coverage fraction | Wave 1 consequence + C-14 | Sec. 5, cor:C11-coverage | DERIVED IN MANUSCRIPT; proof supplied |
| Realizability for all kappa>=T1 | C-15 | Sec. 5, thm:realizability | MATCH; explicit construction included |
| Minimum robust dimension =3 | C-09 | Sec. 5, thm:C09 | MATCH |
| GLV abundance invariance | C-12 | Sec. 6, prop:GLV-invariance | MATCH |
| Pair-loop identity beta=1-g | C-13 | Sec. 6 | MATCH |
| Determinant/three-cycle identity | C-13 | Sec. 6, prop:loop-identity | MATCH |
| Exact loop-space fractional band | C-13 + C-10 | Sec. 6, cor:loop-band | MATCH |
| Fixed-kappa reciprocal-loop sensitivity | C-13 + C-15 | Sec. 6 | MATCH |
| Computational corroboration | Compute Wave 1 final report | Sec. 7 | MATCH; explicitly non-proof |

## Equality/boundary checks

- Matignon stability is always strict: |arg lambda| > alpha*pi/2.
- Zero eigenvalues are excluded.
- Cain/D-stability boundary is strict: kappa<T1, not <=.
- Fractional C-10 boundary is strict: kappa<T_alpha, not <=.
- The fractional-only interior uses T1<kappa<T_alpha.
- For 0<alpha<=2/3, the fractional-only interior uses kappa>T1; equality is not interior.
- C-11 sufficient band correctly includes Phi=1 as non-classically-D-stable because the orbit minimum is attained.
- C-16 is not presented as a novelty claim.

## Novelty wording lock

The manuscript currently uses the permitted formulation:

"explicit exact real-3x3 elimination/solution of the positive-diagonal generalized-D-stability problem for the Matignon reflex sector on the strict-P(-A) stratum."

It does not claim:

- first fractional D-stability concept;
- first abstract generalized-D-stability N&S criterion;
- novelty of principal-minor/simplex normalization;
- novelty of generic network loop decompositions.

## Status

THEOREM RECONCILIATION: PASS

Re-run this check after any substantive theorem/proof edit.

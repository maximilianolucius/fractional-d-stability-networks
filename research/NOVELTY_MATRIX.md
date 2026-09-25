# Closest-work novelty matrix — canonical Chief state

**Date:** 2026-09-24  
**Rule:** compare hypotheses, quantifiers, spectral region, matrix dimension, and conclusion. Keyword mismatch is not novelty.

| Reference | Exact occupied territory | Positive diagonal orbit? | Fractional / sector? | Relation to current theorem package |
|---|---|---:|---:|---|
| Matignon 1996; Brandibur-Garrappa-Kaslik 2021 | exact commensurate fractional sector criterion; alpha monotonicity | no | yes | C-01 imported; C-02 not novel |
| Ahmed-El-Sayed-El-Saka 2007 | explicit fractional-stable / integer-unstable low-dimensional equilibria | no | yes | kills novelty of the basic stabilization phenomenon |
| Cermak-Nechvatal 2017 | optimal fractional Routh-Hurwitz root-location conditions | no | yes | fixed-polynomial component of C-10 is prior art |
| Bourafa-Abdelouahab-Moussaoui 2020 | explicit n=2/n=3 fractional coefficient criteria; exact cubic angular cases | no | yes | fixed-cubic component prior art; no all-D orbit elimination |
| Joya-Furuta 1991 | explicit coefficient-space descriptions for polynomial stability in prescribed domains including sectors | no matrix orbit | sector | coefficient-domain predecessor; does not solve DA orbit |
| Kushel 2019 | general (region, multiplier class, operation)-stability framework | yes | arbitrary region | F_alpha as a concept is not new |
| Kushel-Pavani 2020 | generalized D-stability; forbidden-boundary principle | yes | LMI/conic and complement machinery | closest abstract framework to C-10; no explicit 3x3 Matignon elimination found |
| Kushel-Pavani 2021 | diagonal region-dominance; fractional-order applications | yes for specified classes | yes | sufficient-condition prior art |
| Kushel 2023 | relative D-stability in left-half-plane conic sectors; determinant and sector-gap bounds | yes | sector | sector gap is not novelty; does not include genuinely non-Hurwitz Matignon band |
| Cain 1976 | complete real 3x3 classical D-stability characterization | yes | half-plane | exact alpha=1 endpoint recovered by C-10 |
| Bahl-Cain 1977 | complete inertia classifications for diagonal multiples of real 3x3 matrices | yes | half-plane inertia | very close low-dimensional orbit predecessor; does not control eigenvalue angles |
| Cain 1984; Hartfiel 1980 | topology/interior of classical D-stable matrices | yes | half-plane | interior/robustness concept is classical |
| Abed 1986; Lee-Edgar 2001 | strong/robust D-stability | yes | half-plane | "strong D-stability" terminology/concept occupied |
| Kellogg P-matrix wedge theorem | angular spectral bound for P-matrices | preserved by positive row scaling | angular | imported low-order bridge C-08 |
| Siami 2020/2021 | generalized fractional secant condition for single-circuit networks; necessary in equal-diagonal special case | cycle ratio invariant under row scaling | yes | single-cycle novelty rejected; structured slice of C-10 |
| Arcak-Sontag 2006; Arcak 2011 | cyclic/cactus diagonal stability via secant-type structure | related | alpha=1 | structural graph precedent |
| Jeffries-Klee-van den Driessche; Berman-Hershkowitz | sign/graph characterizations of classical stability classes | related | alpha=1 | graph/topology claims require exact fractional distinction |
| Allesina-Tang; Grilli-Rogers-Allesina | ecological topology/community-matrix spectral stability | no full D orbit | alpha=1 | ecology/topology prior art |
| classical ecological loop analysis / community-matrix literature | signed feedback loops, principal minors, species-deletion stability | no fractional D theorem | alpha=1 | C-13 must be presented as interpretation of C-10, not generic loop novelty |

## Current project theorem versus nearest precedents

### C-09 — minimum robust genuinely fractional dimension

Project theorem:

[
min{n:operatorname{int}(F_alpha^{(n)}setminus D_H^{(n)})
eqarnothing}=3
quad
orall,0<alpha<1.
]

No located prior result combines:
- all positive diagonal multipliers;
- the full Matignon region including its right-half-plane sliver;
- exclusion from classical Hurwitz D-stability;
- full-dimensional interior;
- exact lower-dimensional obstruction;
- minimum dimension 3;
- every fractional order below one.

**Targeted audit verdict:** NOVELTY SURVIVES.

### C-10 — exact 3x3 variational characterization

On the strict-P(-A) full-dimensional stratum, the project reduces the complete positive diagonal orbit to four invariants

[
(eta_{12},eta_{13},eta_{23},kappa)
]

and the simplex threshold

[
T_alpha(eta).
]

For 2/3<alpha<1,

[
Ain F_alpha^{(3)}
iff
kappa<T_alpha(eta).
]

The alpha=1 limit is exactly Cain's threshold.

Closest ingredients are:
- fixed-cubic fractional Routh-Hurwitz;
- general forbidden-boundary D-stability;
- Cain's exact half-plane solution;
- Bahl-Cain's exact inertia solution.

No located source performs the same Matignon-angle diagonal-orbit elimination.

**Targeted search verdict:** NOVELTY SURVIVES PROVISIONALLY; final independent specialist audit required.

### C-13 — ecological motif layer

C-13 rewrites the C-10 invariants as normalized two-cycle and directed three-cycle feedback coordinates and proves GLV abundance-scaling invariance.

Generic loop analysis is classical. The value is that the exact new matrix threshold acquires a motif-coordinate form.

## Claims explicitly withdrawn

Do not state any of the following:

1. "purely fractional stabilization is new";
2. "fractional D-stability is a new concept";
3. "the literature only treats convex regions";
4. "a fractional secant criterion for one cycle is new";
5. "uniform angular gap is new";
6. "strong D-stability is new";
7. "loops determine stability" as a generic novelty claim.

## Final audit rule

Before submission, the independent novelty verifier must try specifically to recover C-10 from:
- Bahl-Cain 1977;
- old inertia-preservation literature;
- generalized-region D-stability papers;
- sector-stable polynomial coefficient-domain papers;
- unpublished/less-visible low-dimensional multiplier-stability results.

Until then, C-10 is a provisional flagship theorem, not a bibliographically final claim.

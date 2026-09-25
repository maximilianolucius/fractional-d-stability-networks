# Scope matrix — canonical Chief state

**Date:** 2026-09-24

Use this file to prevent a prior-art corollary, benchmark, or numerical observation from being promoted into a theorem.

| Claim | Exact current scope | Proof/evidence status | Forbidden overstatement |
|---|---|---|---|
| C-01 Matignon | all commensurate linear systems under imported hypotheses | IMPORTED THEOREM | never claim as project novelty |
| C-02 purely fractional stabilization | matrix/Jacobian phenomenon | KNOWN / DERIVABLE | motivation only |
| C-03 S_alpha(G) | definition | DEFINITION ONLY | no contribution without theorem |
| C-04 generalized fractional D-stability | general framework | PRIOR ART | do not rename as novelty |
| C-05 single cycle/secant | structured cyclic family | SUBSTANTIALLY PRIOR ART (Siami) | not a flagship theorem |
| C-06 robustness/interior concept | general D-stability topology | CLASSICAL PRIOR ART | "strong" / "open" alone not novel |
| C-07 exact 2x2 F_alpha | **all real 2x2 matrices, all 0<alpha<1** | INTERNAL THEOREM | none beyond stated matrix class |
| C-08 low-order dimension-3 separation | real 3x3, 0<alpha<=2/3 | INTERNAL THEOREM modulo Kellogg | ingredient only |
| C-09 minimum robust dimension | **all 0<alpha<1; dimension threshold 3** | INTERNAL THEOREM; targeted novelty survived | not submission-certified until proof audit |
| C-10 exact 3x3 characterization | **full-dimensional strict-P(-A) stratum; exact interior classification** | INTERNAL THEOREM; targeted novelty search survived provisionally | do not silently claim boundary-stratum classification |
| C-11 Phi certificate | strict-P(-A), 2/3<alpha<1 | INTERNAL THEOREM; sufficient only | Phi condition is NOT necessary |
| C-12 GLV abundance invariance | positive equilibria x*>0 | INTERNAL COROLLARY | does not establish feasibility/existence of x* |
| C-13 motif coordinates | three-species strict-P robust stratum | INTERNAL COROLLARY | loop analysis itself is classical |

## Exact hard boundaries

### Dimension 2

For every 0<alpha<1,

[
Ain F_alpha^{(2)}
iff
det A>0,quad a_{11}le0,quad a_{22}le0.
]

The genuinely fractional difference class has empty full-dimensional interior.

### Dimension 3, robust/full-dimensional stratum

Any interior point of (F_alpha^{(3)}) must have (-A) strict P.

For 0<alpha<=2/3,

[
operatorname{int}F_alpha^{(3)}
=
{A:-A	ext{ strict P}}.
]

For 2/3<alpha<1,

[
operatorname{int}F_alpha^{(3)}
=
{A:-A	ext{ strict P}, kappa<T_alpha(eta)}.
]

The exact genuinely fractional interior is

[
operatorname{int}P_alpha^{(3)}
=
{A:-A	ext{ strict P}, T_1(eta)<kappa<T_alpha(eta)}
]

for 2/3<alpha<1.

For 0<alpha<=2/3,

[
operatorname{int}P_alpha^{(3)}
=
{A:-A	ext{ strict P}, kappa>T_1(eta)}.
]

### Boundary strata

Matrices with zero order-one or order-two signed principal minors may belong to (F_alpha), but C-10 does **not** claim a complete classification of all such lower-dimensional boundary strata.

This is not needed for the full-dimensional Q1 theorem package.

## Evidence discipline

- C-07/C-09/C-10/C-11: analytic proofs exist but await adversarial independent audit.
- Numerical diagonal sampling is falsification/corroboration only.
- The numerical optimizer for (T_alpha) evaluates an analytically defined exact variational threshold; numerical minimization is not itself the theorem proof.
- The cyclic (A_gamma) family is a witness/special slice, not the general theorem.

## Prior-art locks

The following are occupied:
- fixed fractional cubic root location;
- single-cycle fractional secant;
- generalized D-stability and forbidden-boundary principles;
- relative D-stability / sector gaps;
- classical D-stability interior/robustness;
- classical loop analysis.

## Manuscript lock

Final manuscript prose remains locked until the adversarial proof audit passes.

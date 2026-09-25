# Research status — Chief Researcher update 2026-09-24

## Current scientific thesis

The project is no longer centered on generic "fractional stabilization on ecological networks".

For fixed 0<alpha<1 define

[
Sigma_alpha={z!=0: |arg z|>alpha*pi/2},
]

[
F_alpha^(n)
=
{A in R^(n x n): sigma(DA) subset Sigma_alpha for every positive diagonal D},
]

and

[
P_alpha^(n)=F_alpha^(n) \ D_H^(n),
]

where D_H is the classical Hurwitz D-stable class.

The central question is the structure of the genuinely fractional difference class P_alpha.

## Flagship theorem — C-09

**Proof status:** internal analytic theorem complete.
**Novelty status:** targeted audit verdict = **NOVELTY SURVIVES**.

For every 0<alpha<1,

[
\boxed{
min { n : int(P_alpha^(n)) != empty } = 3.
}
]

Dimension 2 has only a lower-dimensional boundary separation class; dimension 3 contains a full-dimensional open genuinely fractional class.

Primary proof file:
`research/THEOREM_C09_DIMENSION_THRESHOLD.md`.

Novelty audit:
`research/novelty/C09_TARGETED_AUDIT.md`.

## Structural theorem — C-11

For strict-P(-A) real 3x3 matrices,

[
Phi(A)
=
\frac{
(\sqrt{p_1m_{23}}+\sqrt{p_2m_{13}}+\sqrt{p_3m_{12}})^2
}{-det A}
=
\inf_{D>0}\frac{a_Db_D}{c_D}.
]

Cain's classical strict-P 3x3 D-stability threshold is

[
Phi(A)>1.
]

For 2/3<alpha<1 the project proves the fractional sufficient certificate

[
Phi(A)>
(1-2cos(alpha*pi/2))^2
\Longrightarrow
A in F_alpha^(3).
]

The threshold tends to 1 as alpha->1-, recovering the classical Cain boundary.

Primary file:
`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`.

## Ecological bridge — C-12

For a positive GLV equilibrium,

[
J=diag(x^*)A.
]

Because positive left-diagonal multiplication only reparametrizes the orbit,

[
J in F_alpha iff A in F_alpha,
]

[
J in D_H iff A in D_H,
]

and

[
J in P_alpha iff A in P_alpha.
]

Also Phi(J)=Phi(A).

Thus the new matrix classification is invariant to positive equilibrium abundance scaling; the ecological interpretation is structural rather than parameter-fitted.

## Prior-art boundaries

Do not claim novelty for:
- Matignon stabilization;
- fractional Routh-Hurwitz criteria;
- generalized D-stability;
- relative D-stability / sector gaps;
- strong D-stability;
- single-cycle fractional secant conditions;
- P-matrix spectral wedges;
- Cain's classical 3x3 D-stability theorem.

## Current gates

### P0 — independent proof audit
Run `research/PROOF_AUDIT_TASK_C07_C09_C11.md`.

### P1 — exact 3x3 characterization
Run `research/C10_EXACT_3X3_TASK.md`.

### P2 — manuscript architecture
Allowed only after P0 passes. Full prose drafting should wait until the C-10 outcome is known, because an exact characterization would materially change the title and abstract.

### P3 — topology / ecology
Only after C-10. Graph motifs should be derived from the matrix theorem, not used as the primary source of novelty.

## Evidence discipline

- THEOREM: analytic proof.
- IMPORTED THEOREM: published result used as a lemma.
- CERTIFIED COMPUTATION: rigorous certificate.
- NUMERICAL CORROBORATION: floating-point evidence only.
- OPEN: unresolved.

Finite diagonal sampling is never proof.

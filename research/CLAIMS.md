# Claim registry

**Chief status 2026-09-24: NOVELTY AUDIT REOPENED.**

The audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` is a baseline, not a frozen verdict. See `research/CHIEF_RESEARCH_DIRECTION_2026-09-24.md`.

| ID | Statement / object | Novelty status | Proof status | Mandatory dependency |
|---|---|---|---|---|
| C-01 | Matignon sector criterion | KNOWN/STANDARD | IMPORTED | Matignon; Brandibur–Garrappa–Kaslik |
| C-02 | Fractionally stable while integer-order unstable | DERIVABLE BUT NOT NOVEL | elementary | motivation only |
| C-03 | graph-indexed `S_alpha(G)` | DEFINITION ONLY / NEEDS THEOREM | OPEN | fractional consensus + integer-order topology/spectrum |
| C-04 | `F_alpha={A: sigma(DA) subset Sigma_alpha for all D>0}` | CLOSE PRIOR ART — REOPENED | OPEN | Kushel 2019/2020/2021 + **Kushel 2023 relative D-stability/sector gap** |
| C-05 | topology/motifs characterize genuinely non-Hurwitz fractional D-stability | REOPENED — SINGLE-CYCLE NOVELTY NOT APPROVED | OPEN | **Siami 2020/2021 fractional cyclic secant condition** + Arcak/Sontag |
| C-06 | perturbational robustness / uniform angular margin over all D | REOPENED — NOT APPROVED | OPEN | **Abed 1986 strong D-stability** + Kushel 2023 sector gap |
| C-07 | exact 2x2 classification of `F_alpha`; no open purely-fractional separation in n=2 | NEW AUDIT TARGET — NOT YET NOVEL | OPEN | independent derivation + prior-art search |
| C-08 | dimension threshold for nonempty interior of `P_alpha=F_alpha\\D_H`, candidate first at n=3 | NEW THEOREM CANDIDATE ONLY IF PROVED/AUDITED | OPEN | no inference from finite sampling; identify minimal motif |

## Current objects

\[
\Sigma_\alpha=\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

\[
\mathcal F_\alpha=\{A:\sigma(DA)\subset\Sigma_\alpha\ \forall D\succ0\},
\]

\[
\mathcal P_\alpha=\mathcal F_\alpha\setminus\mathcal D_H.
\]

The main scientific target is structural mathematics for `\mathcal P_\alpha`, especially whether it has nonempty interior and what dimension/motif first permits it.

## Working 2x2 target

Audit and prove/refute:

\[
A\in\mathcal F_\alpha
\iff
\det A>0,\quad a_{11}\le0,\quad a_{22}\le0
\qquad(0<\alpha<1,\ n=2).
\]

If true, determine the exact classical D-stable subset and whether the purely-fractional difference has empty interior.

## Q1 gate

No central-paper drafting until there is:

1. one exact characterization theorem;
2. one genuine separation/obstruction theorem versus classical D-stability or prior fractional-sector results;
3. one nontrivial structural extension (dimension threshold, graph/motif theorem, or ecological consequence).

## Evidence labels

- `THEOREM` — analytic proof.
- `CERTIFIED COMPUTATION` — rigorous certificate.
- `NUMERICAL CORROBORATION` — floating-point evidence only.
- `OPEN` — unresolved.

Finite diagonal sampling is never proof.

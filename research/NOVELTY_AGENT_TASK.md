# Novelty audit task — REOPENED by Chief Researcher

**Status:** ACTIVE  
**Reopened:** 2026-09-24  
**Controlling file:** `research/CHIEF_RESEARCH_DIRECTION_2026-09-24.md`

## Objective

Perform a theorem-level novelty re-audit before any manuscript drafting or proof campaign. The audit at commit `0b3b4df394eceec0dc9951a33fda01560de2f731` is a baseline, not a final verdict.

Read the Chief direction file first.

## Mandatory close prior art

Retrieve and compare exact theorems/equations from:

1. Siami, "Stability and Robustness Analysis of Commensurate Fractional-order Networks", arXiv:2011.04204 / IEEE TCNS — generalized fractional secant condition for a single-circuit digraph.
2. Kushel, "Some bounds for determinants of relatively D-stable matrices", LAA 656 (2023), DOI 10.1016/j.laa.2022.09.018 / arXiv:2205.10823 — relative D-stability and sector-gap results.
3. Abed, "Strong D-stability", Systems & Control Letters 7(3) (1986), DOI 10.1016/0167-6911(86)90116-7 — perturbational robustness/interior.
4. Revisit Kushel 2019 and Kushel–Pavani 2020/2021 in light of these references.

No claim involving "fractional secant criterion", "single cycle", "cactus", "sector gap", "uniform angular margin", "openness", or "strong fractional D-stability" may be promoted before these comparisons.

## Central objects

\[
\Sigma_\alpha=\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

\[
\mathcal F_\alpha
=
\{A:\sigma(DA)\subset\Sigma_\alpha\ \forall D\succ0\},
\]

\[
\mathcal P_\alpha
=
\mathcal F_\alpha\setminus\mathcal D_H.
\]

The novelty question is exact mathematics for the genuinely non-Hurwitz part, not the definition.

## Required low-dimensional audit

Independently derive/prove or refute and search prior art for:

> For real `A in R^{2x2}` and every `0<alpha<1`, `A in F_alpha` iff `det(A)>0` and `a_11<=0, a_22<=0`. If true, determine precisely when A is classically D-stable and whether `P_alpha` has empty interior in dimension two.

## Required questions

1. Does Siami quantify over the same positive diagonal orbit `DA`?
2. Can a proposed single-cycle theorem be obtained from Siami by specialization or transformation?
3. Does Siami allow the right-half-plane Matignon sliver?
4. What exact conic sector does Kushel call relatively D-stable, and how does it compare with `Sigma_alpha`?
5. Does Kushel 2023 already give the proposed uniform sector/angular gap?
6. Does Abed's strong D-stability settle the open-set idea after region substitution, or is non-convexity genuinely new?
7. Is `int(P_alpha)=empty` for n=2, and is that known?
8. Is `int(P_alpha)!=empty` for n=3? Do not infer from finite sampling.
9. Which motif/topology theorem remains genuinely unoccupied?
10. What minimum theorem package is Q1-level?

## Deliverables

Update:

- `research/NOVELTY_REPORT.md`
- `research/NOVELTY_MATRIX.md`
- `research/CLAIMS.md`
- `research/SCOPE_MATRIX.md`
- `research/novelty/novelty-audit.md`

Create:

- `research/novelty/REOPENED_AUDIT_2026-09-24.md` with theorem-by-theorem Siami/Kushel/Abed comparison.

End `NOVELTY_REPORT.md` with:

1. strongest novelty surviving the reopened audit (<=3 sentences);
2. exact theorem target;
3. prior-art result most likely to kill it;
4. verdict: `GO`, `GO-NARROWED`, or `NO-GO/REFRAME`.

Do not draft the manuscript. Numerical sampling is falsification only.

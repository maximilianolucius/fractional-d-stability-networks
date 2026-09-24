# Chief Research Direction — Novelty Audit Reopened

**Date:** 2026-09-24  
**Authority:** Chief Researcher  
**Status:** `NOVELTY_AUDIT = REOPENED`

## Why the audit is reopened

The audit committed at `0b3b4df394eceec0dc9951a33fda01560de2f731` is a strong baseline, but it is not yet sufficient to freeze the novelty claim.

The reopened audit MUST incorporate:

1. **Milad Siami**, "Stability and Robustness Analysis of Commensurate Fractional-order Networks" (arXiv:2011.04204; IEEE TCNS): generalized fractional secant condition for cyclic interconnected commensurate fractional-order systems; a sufficient condition for a single-circuit digraph, necessary in a special uniform-coupling case.
2. **Olga Y. Kushel**, "Some bounds for determinants of relatively D-stable matrices", *Linear Algebra and its Applications* 656 (2023), 9–26, DOI 10.1016/j.laa.2022.09.018 / arXiv:2205.10823: relative D-stability, conic sectors, sector-gap results under positive diagonal scaling.
3. **Eyad H. Abed**, "Strong D-stability", *Systems & Control Letters* 7(3) (1986), 207–212, DOI 10.1016/0167-6911(86)90116-7: persistence of D-stability under sufficiently small perturbations.

Therefore no novelty claim based only on "fractional secant criterion", "single cycle", "sector gap", "uniform angular margin", or "openness/robustness" is approved until theorem-level comparison is complete.

## Revised central objects

For fixed `0<alpha<1` define

\[
\Sigma_\alpha=\{z\ne0:|\arg z|>\alpha\pi/2\}.
\]

Define

\[
\mathcal F_\alpha
=
\{A\in\mathbb R^{n\times n}:
\sigma(DA)\subset\Sigma_\alpha
\text{ for every positive diagonal }D\}.
\]

Let `\mathcal D_H` denote classical Hurwitz D-stability, and define the genuinely fractional separation class

\[
\mathcal P_\alpha
=
\mathcal F_\alpha\setminus\mathcal D_H.
\]

The paper is not allowed to claim novelty from these definitions alone. The target is exact structural mathematics in `\mathcal P_\alpha`, especially where spectra can occupy the right-half-plane Matignon sliver.

## Mandatory dimension-first audit

Before graph-family generalization, resolve low dimension exactly.

For

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
D=\operatorname{diag}(x,y)>0,
\]

we have

\[
\operatorname{tr}(DA)=xa+yd,
\qquad
\det(DA)=xy\det A.
\]

Working proposition to prove/refute and audit:

> For every `0<alpha<1`, a real `2x2` matrix belongs to `\mathcal F_\alpha` iff `det A>0` and `a_11<=0, a_22<=0`. Consequently its non-Hurwitz part is confined to `a_11=a_22=0`, so there is no open robust purely-fractional D-stable set in dimension two.

This is a target, NOT yet an accepted theorem or novelty claim.

If correct, the next question is whether `n=3` is the first dimension for which `int(\mathcal P_\alpha)` is nonempty.

## Revised theorem programme

1. Classify `\mathcal F_\alpha` and `\mathcal P_\alpha` in the smallest dimensions where feasible.
2. Determine whether open/robust purely-fractional D-stability first appears at `n=3`.
3. Identify the minimal signed motif or graph mechanism permitting it.
4. Only then generalize to a graph class, and only if the theorem is strictly different from Siami's cyclic-network result and Kushel's sector theory.
5. Keep distinct:
   - fractional D-stability;
   - strong fractional D-stability (perturbational interior; compare Abed);
   - possible total fractional D-stability (all principal submatrices), if useful for ecological extinction robustness.

## Q1 gate

No manuscript drafting around the central theorem is authorized until the project has, at minimum:

- one exact characterization theorem;
- one genuine separation/obstruction theorem versus classical Hurwitz D-stability or existing fractional-sector results;
- one nontrivial structural extension: dimension threshold, motif/graph theorem, or ecological consequence.

Numerical diagonal sampling is counterexample hunting only.

## Required reopened-audit questions

1. Does Siami's theorem quantify over the same orbit `DA`?
2. Can our single-cycle target be recovered by specialization, sign convention, state scaling, or change of variables?
3. Does Siami reach the right-half-plane Matignon sliver?
4. What is the exact set-theoretic relationship between Kushel's relative D-stability sector and `\Sigma_\alpha`?
5. Does Kushel's sector-gap theory already imply the proposed uniform angular margin?
6. Which topology claims survive after Siami?
7. Is the candidate `2x2` classification already known or immediate from existing generalized D-stability results?
8. Is `int(\mathcal P_\alpha)\ne\varnothing` possible in dimension three?
9. How must strong fractional D-stability differ mathematically from Abed 1986?
10. What is the smallest exact theorem package that remains title-worthy and defensibly new?

## Decision rule

If the strongest surviving result is a reparameterization of Siami/Kushel/Abed, return `NO-GO/REFRAME`. If an exact dimension/topology characterization remains unoccupied, state its full quantifiers before launching a proof agent or manuscript writer.

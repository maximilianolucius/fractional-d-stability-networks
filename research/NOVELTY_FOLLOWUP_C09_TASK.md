# Targeted novelty follow-up — C-09 dimension theorem

**Priority:** P0  
**Do not draft the manuscript.**

Audit the internally proved theorem in `research/THEOREM_C09_DIMENSION_THRESHOLD.md`.

## Exact claim to kill or validate

For every `0<alpha<1`,

\[
\min\{n:\operatorname{int}(\mathcal F_\alpha^{(n)}\setminus\mathcal D_H^{(n)})\neq\varnothing\}=3.
\]

The proof uses:

1. exact 2x2 classification;
2. Kellogg P-matrix wedge for `alpha<=2/3`;
3. a high-order cubic certificate
   \[
   ab/c>(1-2\cos(\alpha\pi/2))^2;
   \]
4. AM-GM to make that coefficient certificate uniform over every positive diagonal scaling;
5. an explicit `A_gamma` family with `gamma>2`;
6. strict inequalities to obtain a full-dimensional open set.

## Mandatory literature audit

Search theorem-level prior art for:

- exact/optimal fractional Routh-Hurwitz criteria for cubic polynomials, especially Cermák–Nechvátal and subsequent "optimal Routh-Hurwitz" papers;
- any published coefficient inequality algebraically equivalent to the cubic certificate above;
- sector/relative/generalized D-stability criteria specialized to 3x3 matrices;
- any theorem combining P-matrices, positive diagonal scaling and Matignon sectors;
- any minimal-dimension/interior theorem separating fractional region D-stability from Hurwitz D-stability.

## Required distinctions

Even if the cubic coefficient lemma is known, determine whether the **uniform diagonal-orbit AM-GM theorem** is known.

Even if that is known, determine whether the **minimal robust dimension = 3 for every 0<alpha<1** theorem is known.

Do not kill the title-level theorem merely because one proof ingredient is classical.

## Deliverable

Create `research/novelty/C09_TARGETED_AUDIT.md` and update `NOVELTY_REPORT.md` / `NOVELTY_MATRIX.md` / `CLAIMS.md` as appropriate.

Final verdict for C-09 must be exactly one of:

- `NOVELTY SURVIVES`
- `PARTIALLY OCCUPIED — REFRAME`
- `NOT NOVEL`
- `UNCERTAIN — SOURCE ACCESS LIMITATION`

Include exact theorem/equation correspondences.

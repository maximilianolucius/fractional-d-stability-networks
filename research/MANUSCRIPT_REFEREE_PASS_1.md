# Internal referee pass 1 — Q1 manuscript

**Date:** 2026-09-25  
**Branch:** q1-manuscript-20260925  
**Role:** adversarial internal referee  
**Target standard:** SIMAX-level matrix-analysis paper.

## Provisional recommendation

**MAJOR REVISION BEFORE EXTERNAL SUBMISSION, BUT SCIENTIFIC CORE IS ACCEPTABLE.**

This is not a verdict on theorem correctness: novelty, proof and compute gates have already passed. The remaining issues are manuscript quality, compression and positioning.

## Major strengths

1. The main theorem is exact, not sufficient:
   \[
   A\in\mathcal F_\alpha^{(3)}
   \iff
   \kappa<T_\alpha(\beta).
   \]
2. The universal positive-diagonal quantifier is genuinely eliminated to four orbit invariants and a two-variable problem.
3. Cain is recovered exactly at alpha=1; this provides a strong classical anchor.
4. C-15 changes the threshold from an opaque global minimization into a unique, smooth, strictly convex optimization problem.
5. C-09 gives a clean conceptual consequence: the first full-dimensional genuinely fractional separation occurs in dimension three.
6. The cyclic Siami theorem is recovered as an exact symmetric slice, rather than merely compared numerically.
7. The GLV layer follows from the orbit structure and is not an unrelated numerical application.
8. Independent proof and compute audits materially strengthen credibility.

## Major manuscript risks

### R1 — Length

The proof-complete article-class draft reached approximately 35 pages before bibliography in an early build.

SIMAX has a nominal 20-page policy.

**Required action after Wave 2:** compress aggressively and split supplementary material. Do not delete the core proofs needed for self-containment.

Recommended main-text priorities:
- definitions/orbit reduction;
- C-07;
- C-10;
- P0/interior theorem;
- Cain recovery;
- C-15 convexity;
- C-09;
- concise ecological interpretation;
- one compact validation section.

Likely supplement/appendix candidates:
- full stress-test mechanism table and pathologies;
- interval-certification implementation details;
- extended numerical derivative checks;
- additional canonical witnesses;
- some secondary asymptotic algebra if necessary.

### R2 — Closest-prior-art statement must stay exact

Kushel–Pavani already give an abstract all-positive-diagonal forbidden-boundary N&S theorem for conic regions/complements.

Any sentence implying “first N&S fractional D-stability criterion” would be incorrect.

Current draft passes this check.

### R3 — C-16 must remain structural

The general simplex normalization is useful but elementary/standard.

Current draft explicitly says it is not a novelty claim.

### R4 — Shao et al. 2017 primary PDF remains uninspected

This does not block the current novelty gate because stronger multiplicative-D prior art has already been inspected, but the PDF should still be obtained before submission if feasible.

### R5 — Figures not yet integrated

A matrix-analysis paper of this length should not rely on equations alone for the geometric message.

Wave 2 should supply data for approximately 5–8 final figures. The final SIMAX version should likely use fewer, around 4–6 high-value figures, with additional plots moved to supplement.

### R6 — Need canonical witness table

The analytic A_gamma family is excellent but insufficient as the only visible example because it is exactly Siami's symmetric slice.

Wave 2 should supply a small table of generic nonsymmetric matrices, ideally including:
- one A already non-Hurwitz at D=I;
- one A Hurwitz at D=I but not Hurwitz D-stable;
- one ecological mixed-sign example;
- one anisotropic example.

Each must have certified/HP T_alpha and explicit margins.

### R7 — Low-order asymptotic proof should show one more Taylor line

The current proof of
\[
K^3 h_\alpha(b)=1+K(3b-1)+O(K^2)
\]
says “a Taylor expansion” after an explicit root formula. This is correct and was proof-audited, but for a top matrix-analysis journal one additional displayed expansion of R(K,b) would improve self-containment.

### R8 — Ecology language must distinguish positive product mechanisms

A positive reciprocal product g_ij can come from mutualism (+,+) or competition (-,-); a negative product corresponds to opposite-sign predator-prey/antagonistic coupling.

Do not call every positive product “mutually reinforcing.”

### R9 — Nonlinear fractional GLV scope

The theorem is a local Jacobian/linearized stability result at a positive equilibrium. It must not be phrased as a global nonlinear stability theorem.

Current Discussion states this limitation; Section 6 opening should also say “local Jacobian stability problem.”

## Minor issues

1. Define the principal argument convention explicitly.
2. Define strict P-matrix and P0-matrix in words on first use.
3. Reduce underfull/overfull boxes in prior-art and notation tables.
4. Use SIAM abbreviations for journal names after converting to SIAM macros.
5. Freeze submission SHA in code/data statement.
6. Add final author affiliation/contact only when supplied/confirmed.
7. Abstract should be rechecked against SIMAX 250-word cap after final revision.
8. Convert to official SIAM class only after main/supplement split is chosen.

## Referee questions the final draft must answer immediately

1. What is new relative to Kushel–Pavani?
2. What is new relative to Cain?
3. Why is n=3 not an arbitrary small example?
4. Why is Siami not already the same theorem?
5. Does computation prove anything?
6. Why is the ecological layer mathematically consequential?
7. Which assumptions are essential and which are presentation choices?

The current draft has defensible answers to all seven; final editing should make them impossible to miss.

## Current internal verdict

- correctness: PASS;
- novelty positioning: PASS;
- conceptual contribution: PASS;
- manuscript structure: PASS WITH REVISION;
- journal-length discipline: NOT YET;
- figures/examples: NOT YET;
- reproducibility: STRONG;
- submission readiness: WAIT FOR WAVE 2 + COMPRESSION.

No new central theorem is requested.

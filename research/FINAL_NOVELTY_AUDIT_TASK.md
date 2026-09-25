# Final specialist novelty audit — C-10 / C-15 / C-16

**Date:** 2026-09-25  
**Assigned by:** Chief Researcher  
**Role:** adversarial literature referee / web-searcher  
**Priority:** P0 before manuscript drafting  
**Target branch:** \`agent/final-novelty-c10-c15-20260925\`

## Objective

Try to **kill** the project's central novelty claim.

Do not confirm the project by default. Search for any prior theorem that is mathematically equivalent, stronger, or close enough that C-10/C-15 would become only a reformulation.

The central project claim to audit is:

For real \(3\times3\) matrices on the strict-P(-A) stratum and \(2/3<\alpha<1\), positive-diagonal multiplicative Matignon stability under **every** \(D\succ0\) is characterized exactly by four positive-left-diagonal orbit invariants

\[
(\beta_{12},\beta_{13},\beta_{23},\kappa)
\]

and a scalar threshold

\[
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta),
\]

where \(T_\alpha\) is the exact simplex minimization of the fixed-cubic Matignon boundary.

C-15 further proves:
- strict convexity in logit coordinates;
- unique/nondegenerate optimizer;
- explicit global parametrization of the threshold surface;
- symmetric slice recovering Siami exactly;
- exact low-order asymptotics;
- realizability of the whole fractional band.

C-16 gives the general \(n\)-dimensional simplex/orbit reduction through normalized principal minors.

## Read first

1. \`research/THEOREM_C10_EXACT_3X3.md\`
2. \`research/THEOREM_C15_THRESHOLD_GEOMETRY.md\`
3. \`research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md\`
4. \`research/THEOREM_C09_DIMENSION_THRESHOLD.md\`
5. \`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md\`
6. \`research/novelty/C10_TARGETED_AUDIT.md\`
7. \`research/NOVELTY_MATRIX.md\`
8. \`research/novelty/D_STABILITY_TERMINOLOGY_COLLISION.md\`
9. \`research/CLAIMS.md\`

## Mandatory threat families

Search theorem-by-theorem, not by title similarity alone.

### T1 — classical 3x3 multiplicative D-stability

Inspect:
- Cain 1976, *Real, 3 x 3, D-stable matrices*;
- Bahl & Cain 1977, *The inertia of diagonal multiples of 3x3 real matrices*;
- Cain 1984, *Inside the D-stable matrices*;
- Hartfiel / Cross / Johnson / classical P-matrix D-stability literature;
- any explicit 3x3 inertia-preservation theorem.

Determine whether their homogeneous-polynomial/minor machinery already yields sector-angle information equivalent to C-10 after a change of variables.

### T2 — generalized-region multiplicative D-stability

Inspect:
- Kushel 2019 generalized D-stability;
- Kushel & Pavani generalized D-stability in LMI regions;
- Kushel 2023 relative D-stability / sector gap;
- older "relative stability", "relative D-stability", "sector D-stability", "D-stability angle", "D-stability degree", "multiplicative D-stability in a sector", "conic D-stability";
- Soviet/Russian/Eastern European literature under alternative terminology.

Critical distinction:
the project uses **positive diagonal multiplier \(D\)** and the Matignon region
\[
|\arg\lambda|>\alpha\pi/2,
\]
which for \(\alpha<1\) contains a right-half-plane sliver.

Do not count ordinary pole-region \(\mathcal D\)-stability as the same concept.

### T3 — fractional-order matrix D-stability

Search all combinations/synonyms:
- fractional D-stability;
- fractional-order D-stability;
- positive diagonal scaling fractional systems;
- diagonal multiplier fractional stability;
- robust fractional stability under positive diagonal uncertainty;
- diagonal perturbation / multiplicative uncertainty + Matignon;
- P-matrix + fractional sector.

Explicitly inspect:
- Shao et al. 2017;
- Mohsenipour & Liu 2020;
- any papers citing them;
- papers after 2020 using "necessary and sufficient D-stability" language.

Resolve whether their \(D\) means a pole domain or a diagonal multiplier.

### T4 — fixed cubic sector / fractional Routh-Hurwitz

Inspect:
- Cermák–Nechvátal;
- Bourafa–Abdelouahab–Moussaoui;
- sector-stable polynomial coefficient-domain papers;
- robust polynomial / zero-exclusion sector tests;
- exact cubic root-angle conditions.

Question:
does any source combine those fixed-polynomial conditions with the **entire positive diagonal orbit** to eliminate \(D\) exactly?

### T5 — cyclic / secant theory

Inspect:
- Siami 2020/2021;
- Arcak/Sontag cyclic systems;
- secant criteria and diagonal stability of cyclic feedback systems;
- multi-cycle extensions.

Determine whether C-10 is merely an unstructured rewriting of a known cyclic result or whether Siami is only a lower-dimensional slice.

### T6 — normalized principal-minor orbit parametrizations

Search for:
- principal-minor normalized coordinates under positive diagonal scaling;
- homogeneous characteristic coefficients under row scaling;
- simplex normalization of D-stability;
- projective/geometric formulations of diagonal multiplier orbits;
- hyperbolic polynomial / log-convex / geometric programming formulations.

This is the main threat to C-15/C-16.

### T7 — newest literature through 2026-09-25

Search current 2025–2026 papers/preprints, including:
- Kushel's 2026 recursive determinantal D-stability framework;
- recent diagonal-stability/D-stability papers;
- any new fractional matrix stability work.

Do not stop at the historical literature.

## Search strategy

Use:
- Google Scholar / publisher pages / Crossref / arXiv / Semantic Scholar / MathSciNet-like metadata when accessible;
- citation chaining backward and forward;
- references of Bahl–Cain, Cain, Kushel, Siami and recent D-stability surveys;
- exact theorem text whenever obtainable.

Search in English and, where useful, alternate transliterations/terminology.

## Required comparison matrix

For each serious prior work, record:

1. exact citation;
2. object (matrix / polynomial / network);
3. multiplier class;
4. spectral region;
5. dimension;
6. necessary or sufficient;
7. exact characterization or bound;
8. quantifies over all positive diagonal multipliers?;
9. allows right-half-plane Matignon-stable eigenvalues?;
10. uses principal minors?;
11. eliminates the diagonal multiplier?;
12. relation to C-10;
13. relation to C-15;
14. relation to C-16;
15. verdict:
   - SUBSUMES;
   - PARTIAL OVERLAP;
   - SPECIAL CASE;
   - ADJACENT;
   - TERMINOLOGY COLLISION;
   - NO MATERIAL OVERLAP.

## Mandatory falsification questions

Answer explicitly:

1. Is C-10 already contained in Bahl–Cain 1977 after replacing inertia by an angular condition?
2. Is \(T_\alpha(\beta)\) equivalent to a known "relative D-stability" determinant bound?
3. Is the strict convexity/logit formulation known in D-stability or geometric-programming literature?
4. Is the general simplex reduction C-16 already standard enough that it should be only a lemma with no novelty language?
5. Does any source give an exact necessary-and-sufficient 3x3 positive-diagonal **sector** stability theorem?
6. Does any source cover a nonconvex Matignon region including RHP points?
7. Does any fractional paper quantify over every \(D\succ0\) rather than over uncertain polynomial coefficients?
8. Is the dimension-threshold C-09 derivable immediately from a published theorem?
9. Does the symmetric Siami slice exhaust the C-10 family under hidden similarity/scaling?
10. Is the ecological loop form C-13 already an exact known three-species D-stability criterion under different notation?

## Deliverables

Create:

- \`research/novelty/FINAL_C10_C15_SPECIALIST_AUDIT.md\`
- update \`research/NOVELTY_MATRIX.md\` with every materially relevant source;
- update \`research/novelty/C10_TARGETED_AUDIT.md\` only if new evidence changes or sharpens it;
- create \`research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md\` with verified DOI/title/year/theorem/page details for all load-bearing citations.

## Final verdict

Return exactly one for each:

- C-09
- C-10
- C-15
- C-16

using:

- **NOVEL**
- **NOVEL WITH NARROWED CLAIM**
- **NOT NOVEL**
- **UNRESOLVED**

Then give one overall manuscript recommendation:

- **NOVELTY GATE PASS**
- **NOVELTY GATE PASS WITH REPOSITIONING**
- **NOVELTY GATE FAIL**
- **BLOCKED BY MISSING PRIMARY SOURCE**

Any NOT NOVEL / FAIL verdict must identify the exact prior theorem and show the implication or equivalence.

Do not draft the manuscript.
Do not soften a collision because the project already invested work in the theorem.

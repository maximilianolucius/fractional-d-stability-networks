# Submission directive compliance audit

**Date:** 2026-09-25  
**Canonical directive:** \`agent_directives_publishable_first_submission.md\`  
**Submission target:** SIAM Journal on Matrix Analysis and Applications (SIMAX)  
**Audited entry point:** \`paper/submission-siam.tex\`

## Executive verdict

The mathematical/research requirements are satisfied. The editor-facing submission is being finalized to satisfy the hard page and visual-density constraints.

One internal directive is intentionally superseded by mandatory journal policy:

> "No reference to AI ... in the manuscript."

Current SIAM policy requires disclosure of substantial AI use beyond routine language polishing. The submission therefore retains a factual generative-AI declaration and full author-responsibility statement. Hiding that use would violate the target journal's policy.

## Hard constraints

| Directive | Status | Evidence / action |
|---|---|---|
| Maximum 25 pages total; target 22--23 | PASS at hard ceiling in last successful SIAM build (25); latest compact build aims for margin | \`paper/submission-siam.tex\`; CI page-count audit |
| No AI reference | JOURNAL-POLICY EXCEPTION | SIAM requires disclosure; \`sections/10-declarations.tex\` |
| No supplementary-material dependency | PASS | all load-bearing proofs remain in main article; editor package contains no supplementary PDF |
| Visually rich: 8--12 figures or 12--20 informative panels | PASS by design; final CI pending | 3 compact figure environments × 4 panels = 12 theorem-driven panels |
| Publication-grade figures | PASS by design; visual PDF inspection still required | vector PDFs generated from final Wave 2 data; PNG copies included for portability |
| Every figure earns its space | PASS | all panels correspond to C-10/C-14/C-15/C-09, GLV interpretation, or robustness/certification questions |

## Research and theorem discipline

- Strong theorem identified before final prose: **PASS**.
- Central result is a family theorem, not a benchmark: **PASS**.
- Claim registry exists and has been audited: **PASS**.
- Imported theorem hypotheses/sign conventions audited: **PASS**.
- Equality/boundary cases treated explicitly: **PASS**.
- Fractional-specific stability condition stated precisely: **PASS**.
- Orbit problem reduced before examples: **PASS**.
- Numerical sampling never used as proof: **PASS**.
- Exact/certified/HP/numerical evidence separated: **PASS**.
- Closest-prior-work comparison and conservative novelty language: **PASS**.
- Title foregrounds the strongest theorem: **PASS**.
- Abstract theorem-first rather than benchmark-first: **PASS**.
- Independent proof/novelty/compute referee gates: **PASS**.
- Compute Wave 1: \`COMPUTE_PASS\`; Wave 2: \`COMPUTE2_PASS\`.
- Final tests: 135/135.
- Persistent C-10/C-15 discrepancies: 0.

## Visual program

Final submission panel plan:

1. spectral Matignon/Hurwitz geometry;
2. dimension-1/2/3 robust-separation schematic;
3. normalized simplex objective;
4. exact cyclic fractional band;
5. \(T_\alpha/T_1\);
6. relative fractional-band width;
7. classical-order asymptotic;
8. low-order \(K^{-3}\) normalization;
9. ecological \(L_3\) band;
10. pair-loop sensitivity;
11. unique optimizer coordinates;
12. witness robustness distances.

All panels are generated from analytic formulas or final Wave 2 datasets and discussed in the main text.

## Packaging rule

The final editor ZIP must contain only the compile-ready submission:

- one root SIAM LaTeX file with a title-derived filename;
- every included section \`.tex\`;
- bibliography;
- current SIAM class and bibliography style;
- all 12 vector PDF panels and PNG copies;
- final title-derived PDF;
- a short source manifest/build README.

It must not contain:
- the long technical manuscript;
- exploratory n=4 material;
- proof/novelty/agent reports;
- a supplementary PDF;
- internal task files.

## Remaining gates

1. final CI build with the 12-panel compact layout;
2. verify page count <=25, preferably 22--23;
3. zero undefined citations/references and zero material overfull boxes;
4. render final PDF and visually inspect figure/text pages;
5. generate title-derived PDF filename and final submission ZIP;
6. verify ZIP compiles from its own contents.

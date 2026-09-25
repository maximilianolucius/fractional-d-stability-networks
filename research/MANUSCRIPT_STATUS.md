# Q1 Manuscript Status

**Branch:** \`q1-manuscript-20260925\`  
**Phase:** proof-complete technical v2 + compact submission draft; Compute Wave 2 integrated
**Scientific gates:** novelty PASS WITH REPOSITIONING; proof PASS; compute PASS.

## Current manuscript state

The obsolete ecological-network scaffold has been replaced by a theorem-first manuscript.

### Complete in v1

- title and abstract aligned with the final novelty boundary;
- Introduction with explicit relation to Cain, Bahl--Cain, Kushel/Kushel--Pavani, fixed-polynomial fractional criteria, and Siami;
- general positive-diagonal orbit/simplex reduction with proof;
- exact 2x2 classification with proof;
- exact cubic Matignon boundary with proof;
- exact real-3x3 threshold theorem C-10 with proof;
- P0 necessity and strict-P interior characterization;
- exact recovery of Cain;
- exact genuinely fractional band;
- C-15 global strict logit convexity with proof;
- symmetry reductions and canonical cyclic family;
- global threshold-surface parametrization with proof;
- exact sensitivity formula;
- monotonicity in alpha;
- C-14 alpha->1 asymptotic with proof;
- alpha->2/3 asymptotic with proof;
- C-11 exact orbit minimum and sufficient certificate;
- asymptotic quantification of C-11 conservatism;
- realizability theorem;
- C-09 minimum-dimension theorem;
- GLV abundance invariance and loop-coordinate interpretation;
- adversarial/high-precision computational validation section;
- prior-art comparison table;
- limitations and future n=4 boundary;
- conclusion;
- verified core bibliography;
- automated LaTeX build workflow;
- static reference/citation audit with zero missing citations/refs.

## Current readiness

- theorem correctness: PASS;
- novelty positioning: PASS;
- theorem reconciliation: PASS;
- clean LaTeX build: PASS;
- static citation/reference audit: PASS;
- abstract length: ~189 words;
- current technical length: ~37 pages including bibliography;
- internal referee pass 2: scientific content ready, editorial revision required.

See `research/MANUSCRIPT_REFEREE_PASS_2.md`.

## Still required before submission

1. inspect the primary Shao et al. 2017 PDF only if it becomes accessible; current final search found metadata but no public full text, and it is not load-bearing;
2. incorporate Wave 2 certified atlas/canonical witnesses/robustness outputs;
3. choose 5--8 publication figures and final captions;
4. integrate Wave 2 outputs and then perform the final post-figure referee pass;
5. preserve the current warning-free LaTeX build after figure integration;
6. add repository/data-availability statement and final commit identifier;
7. select target journal and adapt formatting;
8. title/abstract final compression after figures and journal target are fixed.

## Manuscript principle

No new central theorem is required for submission. New discoveries from Wave 2 or n=4 are excluded unless the Chief explicitly reopens the theorem package.


## Build and audit record

The manuscript branch includes a dedicated `.github/workflows/paper.yml` workflow. A clean completed build produced a 37-page PDF with no LaTeX/BibTeX warnings, no undefined citations and no undefined references. The workflow now also uploads the compiled PDF as a versioned CI artifact.

The manuscript theorem reconciliation is recorded in:

`research/MANUSCRIPT_THEOREM_RECONCILIATION.md`.

The second internal referee pass is recorded in:

`research/MANUSCRIPT_REFEREE_PASS_2.md`.


## Wave 2 closure

Compute Wave 2 returned \`COMPUTE2_PASS\` and has been Chief-reviewed and merged to \`main\`.

- tests: 135/135;
- certified atlas: 938/938, with 903 unconditional x-space certificates and 35 additional C-15-assisted logit certificates;
- canonical witnesses: 35;
- C-15 checks: 128,000 float + 2,500 HP;
- unresolved C-10/C-15 discrepancies: 0;
- P6 n=4 shared-edge result remains exploratory and is excluded from current manuscript claims.

## Current manuscript variants

- \`paper/main.tex\`: proof-complete technical manuscript, 39 pages in the neutral article layout;
- \`paper/submission.tex\`: compact submission draft, 24 pages in the same neutral layout;
- \`paper/submission-siam.tex\`: current-SIAM-class draft using \`siamart251216\`; page-count gate pending CI.

The compact version retains the full load-bearing proofs of C-10, the strict-P interior classification, C-15 strict convexity, C-14, and C-09. Secondary threshold geometry remains preserved in the technical manuscript.

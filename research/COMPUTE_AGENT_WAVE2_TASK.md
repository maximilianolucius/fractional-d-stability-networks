# Compute Agent Wave 2 — execution task

**Date:** 2026-09-25  
**Assigned by:** Chief Researcher  
**Execution branch:** \`agent/compute-wave2-20260925\`  
**Baseline main SHA:** \`36b2432d717be7f24ba589b58d6ad7efaabaebd9\`  
**Status:** **READY TO START**  
**Wave 1 prerequisite:** satisfied — \`COMPUTE_PASS\`, zero genuine C-10 counterexamples.

## Mission

Wave 2 is a **publication-grade certification and robustness campaign**.

Wave 1 established computational soundness. Wave 2 must now turn the validated theorem package into a compact numerical layer suitable for a Q1 paper and supplement.

Do **not** search broadly for new central theorems. Do **not** alter the mathematical claims already locked by the Chief. Do **not** edit \`paper/\`.

Your job is to produce:

1. a certified atlas of \(T_\alpha(\beta)\);
2. a compact canonical witness library;
3. quantitative robustness margins;
4. independent high-precision checks of C-15 differential structure;
5. publication-ready source datasets for final figures;
6. optionally, one sharply focused \(n=4\) conjecture family only after P0–P5 are complete.

The theorem package is already proof-audited and novelty-audited. Computation is corroboration/certification, never proof unless a rigorous interval bound is explicitly produced.

---

# Required reading before execution

Read in this order:

1. \`research/COMPUTE_WAVE1_FINAL_REPORT.md\`
2. \`computations/results/C10_STRESS_SUMMARY.json\`
3. \`research/CHIEF_PROOF_AUDIT_CLOSURE.md\`
4. \`research/novelty/FINAL_C10_C15_SPECIALIST_AUDIT.md\`
5. \`research/THEOREM_C10_EXACT_3X3.md\`
6. \`research/THEOREM_C15_THRESHOLD_GEOMETRY.md\`
7. \`research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md\`
8. \`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md\`
9. \`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md\`
10. \`research/MANUSCRIPT_PRODUCTION_PLAN.md\` if present on your branch; otherwise do not fetch or modify the manuscript branch.

Core numerical implementation:

- \`src/fdsn/c10_threshold.py\`
- \`src/fdsn/interval_cert.py\`
- \`src/fdsn/direct_margin.py\`

Existing Wave 1 scripts/results should be reused where mathematically appropriate rather than duplicated.

---

# P0 — frozen baseline and reproducibility

Mandatory.

1. Verify current branch:
   \`\`\`bash
   git status
   git branch --show-current
   git rev-parse HEAD
   \`\`\`
2. Confirm branch is \`agent/compute-wave2-20260925\`.
3. Record baseline SHA.
4. Confirm Wave 1 final status is \`COMPUTE_PASS\`.
5. Confirm:
   - \`GENUINE_C10_COUNTEREXAMPLES = 0\`;
   - 121 tests passed in Wave 1;
   - decisive Wave 1 artifacts are readable.
6. Run full current test suite before any edits.
7. Create:
   \`computations/results/wave2/ENVIRONMENT.json\`.
8. Record Python, numpy, scipy, mpmath, sympy, CPU, RAM, worker count, BLAS threading, git SHA and exact commands.

**STOP LINE:** if the baseline does not reproduce cleanly, stop and return \`COMPUTE2_FAIL\` or \`PARTIAL/BLOCKED\`. Do not build Wave 2 on a broken baseline.

---

# P1 — certified threshold atlas

Construct an adaptive interval-certified atlas of

\[
T_\alpha(\beta_{12},\beta_{13},\beta_{23})
\]

using the existing exact threshold implementation and interval machinery.

## Mandatory families

### A. Fully symmetric
\[
\beta=(b,b,b),
\qquad
b\in[10^{-3},10^3].
\]

Use the exact closed form
\[
T_\alpha(b,b,b)=27h_\alpha(b/3)
\]
as an independent cross-check.

### B. Two-equal
\[
\beta=(b,b,c)
\]
over at least 6 logarithmic \(b/c\) ratios per decade in a broad range.

### C. All antagonistic
\[
\beta_{ij}>1.
\]

### D. All below one
\[
0<\beta_{ij}<1.
\]

### E. Mixed-sign ecological loop regime
Use the C-13 slices already present in Wave 1.

### F. Highly anisotropic
At least representative triples spanning
\[
10^{-4}\le\beta_{ij}\le10^4.
\]

## Alpha grid

Must be especially dense near both transitions.

Include at minimum:

\[
\alpha=
2/3+10^{-k},
\quad
k=1,\ldots,8,
\]

selected ordinary values in \((2/3,1)\), and

\[
\alpha=1-10^{-k},
\quad
k=1,\ldots,10.
\]

## Certification target

Return at least **500 rigorously interval-certified anchor points**.

Target relative enclosure width:

- ordinary region: \(\le10^{-12}\);
- near singular limits: \(\le10^{-9}\), unless a tighter result is affordable.

For every certified point record:

- beta triple;
- alpha;
- lower and upper bound;
- midpoint;
- relative width;
- optimizer enclosure if available;
- arithmetic precision;
- runtime;
- certification method/status.

Required file:

\`computations/results/wave2/CERTIFIED_THRESHOLD_ATLAS.csv\`

Also write:

\`computations/results/wave2/CERTIFIED_THRESHOLD_ATLAS_SUMMARY.json\`

with count, worst width, median width and failures.

No silent certification failures. Any point not certified must be labelled explicitly.

---

# P2 — canonical genuinely fractional witness library

Construct **24–40 canonical real \(3\times3\) matrices**, selected for interpretability rather than randomness.

Mandatory categories:

1. symmetric cyclic / Siami slice;
2. generic nonsymmetric strict-P examples;
3. strong antagonistic pair loops;
4. mixed ecological signs;
5. close to Cain boundary;
6. close to exact fractional boundary;
7. close to \(\alpha=2/3\);
8. close to \(\alpha=1\);
9. cases where \(A\) itself is Hurwitz but fails classical D-stability elsewhere in the orbit;
10. cases where \(A\) itself is already non-Hurwitz.

Prefer:
- integers;
- rationals;
- short decimals;
over opaque random matrices.

For each witness record:

- full \(A\);
- alpha;
- strict-P principal minors;
- \(\beta_{12},\beta_{13},\beta_{23},\kappa\);
- \(T_1\);
- certified or HP \(T_\alpha\);
- \(m_{\rm Cain}=\kappa-T_1\);
- \(m_{\rm frac}=T_\alpha-\kappa\);
- normalized versions of both margins;
- optimizer \(x^*\);
- corresponding worst diagonal ratio \(D^*\) up to common scale;
- direct spectral Matignon margin at \(D^*\);
- whether \(A\) is Hurwitz at \(D=I\);
- explicit positive diagonal \(D_H\), where applicable, witnessing failure of classical Hurwitz D-stability;
- \(g_{ij}\);
- \(L_3\).

At least 8 witnesses should have a rigorously certified \(T_\alpha\).

Required files:

- \`computations/results/wave2/CANONICAL_WITNESSES.csv\`
- \`computations/results/wave2/CANONICAL_WITNESSES.json\`
- \`computations/results/wave2/CANONICAL_WITNESSES_README.md\`

---

# P3 — quantitative robustness

Goal: demonstrate numerically that selected genuinely fractional matrices are not knife-edge examples.

Use a curated subset of at least 12 canonical witnesses.

## P3A invariant-space robustness

Compute:

\[
m_{\rm frac}=T_\alpha(\beta)-\kappa,
\]

\[
m_{\rm Cain}=\kappa-T_1(\beta).
\]

Return absolute and dimensionless normalized margins.

Also compute local first-order sensitivities using C-15.

## P3B entry-space robustness

Estimate the minimum real full-matrix perturbation needed to reach:

1. the exact fractional boundary;
2. the Cain boundary;
3. any strict-P boundary.

Use several independent methods:

- local differential approximation;
- constrained local nonlinear optimization;
- global/adversarial optimization;
- high-precision refinement of best candidates.

For each witness and target boundary return:

- best upper bound found;
- any rigorous lower bound if available;
- perturbation matrix;
- norm used;
- verification residual;
- whether result is NUMERICAL, HP, or CERTIFIED.

Use at least:

- Frobenius norm;
- max-entry norm.

Do **not** state an exact robustness radius unless you have a proof/certificate.

Required:

- \`computations/results/wave2/ROBUSTNESS_SUMMARY.csv\`
- \`computations/results/wave2/ROBUSTNESS_DETAILS.json\`

---

# P4 — C-15 differential structure

Independently verify the theorem-specific differential identities of C-15.

Primary identity:

\[
\frac{\partial T_\alpha}{\partial\beta_{ij}}
=
\frac{h_\alpha'(B^*)}{x_k^*},
\qquad
\{i,j,k\}=\{1,2,3\}.
\]

Mandatory checks:

1. HP central finite differences;
2. complex-step or equivalent high-accuracy differentiation where valid;
3. Hessian positive-definiteness in logit coordinates;
4. condition number of the optimizer Hessian;
5. derivatives with respect to alpha;
6. sensitivity of \(x^*\);
7. permutation equivariance.

Cover:

- symmetric beta;
- two-equal beta;
- ordinary generic beta;
- strong anisotropy;
- alpha near \(2/3\);
- alpha near 1.

Target:
at least **50,000 independent differential checks**, with high-precision recheck of the worst 500.

Search for simple identities, but label them only as:

- NUMERICAL OBSERVATION;
- SYMBOLIC IDENTITY;
- CONJECTURE;

unless a complete proof is supplied separately for Chief review.

Required:

- \`computations/results/wave2/C15_SENSITIVITY_VALIDATION.json\`
- \`computations/results/wave2/C15_SENSITIVITY_WORST.csv\`

---

# P5 — publication datasets and figure source layer

Generate **data**, not ornamental graphics.

Every dataset must state whether rows are:

- FLOAT;
- HP;
- CERTIFIED.

Required figure-source families:

1. \(T_\alpha/T_1\) versus alpha;
2. \(W_\alpha=T_\alpha-T_1\);
3. \(W_\alpha/T_1\);
4. C-11 sufficient fraction versus exact band;
5. ecological \((L_3,\alpha)\) boundaries;
6. pair-loop sensitivity surfaces;
7. optimizer coordinates \(x^*(\alpha,\beta)\);
8. classical-order asymptotic:
   \[
   T_\alpha-T_1\sim C(\beta)(1-\alpha);
   \]
9. low-order blow-up:
   \[
   T_\alpha\sim27/K^3.
   \]

Create:

\`computations/results/wave2/FIGURE_DATA/\`

Each figure dataset must have:

- CSV/Parquet source;
- a short README explaining mathematical purpose;
- exact generating script;
- baseline/commit SHA;
- evidence label.

You may generate preview PNGs for QA, but final paper styling is not your responsibility.

---

# P6 — optional focused \(n=4\) reconnaissance

**Only after P0–P5 are complete.**

Do not run another broad random scan.

Study only:

> two directed 3-cycles sharing an edge.

Objectives:

1. find a low-dimensional invariant parametrization;
2. exploit any exact symmetry;
3. resolve the fractional/classical boundary numerically at high precision;
4. test whether it reduces to a known secant/cycle theorem;
5. return one or more precise conjectures.

If no simple structure emerges, report the negative result and stop.

Required only if P6 is run:

\`computations/results/wave2/N4_SHARED_EDGE_CONJECTURE.md\`

This material is **future-paper only** and must remain separate from the current Q1 manuscript claims.

---

# Independent-validation rule

For every important quantitative conclusion, use two computational routes whenever possible.

Examples:

- exact threshold implementation vs direct spectral optimization;
- analytic derivative vs HP finite difference;
- interval enclosure vs HP optimizer;
- constructed orbit worst point vs direct eigenspectrum.

A result generated by one code path only should be labelled accordingly.

---

# Numerical pathology rule

Wave 1 discovered that extreme diagonal ratios can invalidate eigenvalue angles if arithmetic precision is too low.

Therefore:

- never trust tiny eigenvalues whose magnitude is far below the spectral radius without a posteriori precision analysis;
- either bound log-diagonal ratios or increase precision with scaling magnitude;
- log every escalation rule;
- never convert a numerical failure into a mathematical counterexample before independent HP confirmation.

---

# Stop-line rules

Immediately stop the normal campaign and report to the Chief if any of the following occurs:

1. a certified interval contradicts C-10;
2. a direct spectral calculation and C-10 disagree after independent HP confirmation;
3. a C-15 derivative identity fails after HP recheck;
4. the current test suite regresses;
5. Wave 1 final artifacts cannot be reproduced or validated.

In such a case:

- minimize the counterexample;
- reproduce independently;
- use at least 100 digits where relevant;
- commit the smallest reproduction script/data;
- mark final status \`COMPUTE2_FAIL\`.

Do not average away or silently discard discrepancies.

---

# Scope restrictions

You may modify:

- \`computations/scripts/\`
- \`computations/results/wave2/\`
- \`src/fdsn/\` only when needed for reusable numerical infrastructure;
- \`tests/\`;
- \`research/COMPUTE_WAVE2_FINAL_REPORT.md\`.

Do **not** modify:

- \`paper/\`;
- theorem files C-07...C-16;
- novelty audits;
- proof-audit reports;
- \`research/CLAIMS.md\`;
- \`research/research-status.md\`;
- manuscript-production files.

If you discover a mathematical result, report it in the Wave 2 final report; the Chief decides whether it becomes a theorem.

---

# Commit discipline

Use separate commits:

1. \`wave2: P0 baseline\`
2. \`wave2: P1 certified atlas\`
3. \`wave2: P2 canonical witnesses\`
4. \`wave2: P3 robustness\`
5. \`wave2: P4 C15 sensitivity\`
6. \`wave2: P5 publication datasets\`
7. optional \`wave2: P6 n4 shared-edge reconnaissance\`
8. \`wave2: final report\`

Push every commit to:

\`agent/compute-wave2-20260925\`

Do not merge to \`main\`.

---

# Final report

Create:

\`research/COMPUTE_WAVE2_FINAL_REPORT.md\`

It must begin with one of:

- \`COMPUTE2_PASS\`
- \`COMPUTE2_FAIL\`
- \`PARTIAL/BLOCKED\`

Required executive summary:

- branch;
- final SHA;
- baseline SHA;
- tests passed/failed;
- number of certified atlas points;
- worst certified relative width;
- number of canonical witnesses;
- number of robustness optimizations;
- number of C-15 differential checks;
- any discrepancies;
- any precision pathologies;
- P6 status;
- exact paths of decisive artifacts.

Then report the 5–10 most important numerical/certification findings.

## PASS criterion

\`COMPUTE2_PASS\` requires:

- P0–P5 complete;
- full test suite green;
- no unresolved contradiction with C-10/C-15;
- at least 500 certified atlas points;
- at least 24 canonical witnesses;
- robustness study completed on at least 12 witnesses;
- at least 50,000 C-15 differential checks;
- figure-source datasets complete and reproducible.

P6 is optional and cannot block PASS.

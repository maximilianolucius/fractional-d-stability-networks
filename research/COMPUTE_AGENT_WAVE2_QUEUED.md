# Compute Agent Wave 2 — certified atlas, robustness and publication-grade numerical layer

**Date prepared:** 2026-09-25  
**Assigned by:** Chief Researcher  
**Status:** **UNLOCKED — COMPUTE WAVE 1 PASSED**  
**Start condition:** Compute Wave 1 must finish with \`COMPUTE_PASS\` and zero genuine C-10 counterexamples.

This wave is intentionally large. It must not be started if Wave 1 returns COMPUTE_FAIL or unresolved HP discrepancies.

## Scientific purpose

Wave 1 attacks correctness. Wave 2, if unlocked, should create a compact **certified computational layer** suitable for a Q1 paper and supplement:

1. rigorous/certified values of the exact threshold \(T_\alpha(\beta)\);
2. quantitative robustness of genuinely fractional examples;
3. publication-grade reproducible phase datasets;
4. high-precision validation of C-15 sensitivities and asymptotics;
5. a small library of canonical examples chosen for mathematical interpretability, not random spectacle.

No central theorem may rely on this wave.

---

# P0 — freeze a validated baseline

After the Chief merges Wave 1:

1. clone/fetch current \`main\`;
2. record exact SHA;
3. run full test suite;
4. verify that Wave 1 final artifacts are present and status is COMPUTE_PASS;
5. refuse to proceed if any Wave 1 counterexample flag is nonzero.

---

# P1 — certified threshold atlas

Build an adaptive interval-certified atlas for

\[
T_\alpha(\beta_{12},\beta_{13},\beta_{23})
\]

over structured slices.

Mandatory families:

1. symmetric:
   \[
   (b,b,b),\quad b\in[10^{-3},10^3];
   \]
2. two-equal:
   \[
   (b,b,c);
   \]
3. antagonistic:
   \[
   \beta_{ij}>1;
   \]
4. mutualistic/competitive:
   \[
   0<\beta_{ij}<1;
   \]
5. highly anisotropic triples spanning at least \(10^{-4}\) to \(10^4\);
6. ecological pair-loop slices used in C-13.

Alpha grid must be dense near both singular limits:

\[
\alpha\downarrow2/3,
\qquad
\alpha\uparrow1.
\]

For a curated set of at least 500 anchor points, return rigorous interval enclosures for \(T_\alpha\) with documented outward rounding.

Target relative certified width:
- ordinary region: <= \(10^{-12}\);
- near singular limits: <= \(10^{-9}\), or document why harder.

Deliver:
- compact CSV/Parquet;
- interval width statistics;
- exact reproduction commands.

---

# P2 — canonical genuinely fractional witness library

Construct 20–40 canonical real \(3\times3\) matrices spanning:

- symmetric cyclic family;
- non-symmetric generic strict-P examples;
- antagonistic pair-loop examples;
- mixed-sign ecological examples;
- examples near Cain boundary;
- examples near fractional boundary;
- examples near \(\alpha=2/3\);
- examples near \(\alpha=1\).

Prefer simple rational or low-complexity decimal entries whenever possible.

For each witness record:

1. \(A\);
2. \(\alpha\);
3. \(\beta\);
4. \(\kappa\);
5. \(T_1\);
6. certified/HP \(T_\alpha\);
7. exact fractional band position;
8. direct spectral worst diagonal \(D^*\);
9. direct margin at \(D^*\);
10. whether \(A\) itself is Hurwitz;
11. whether the failure of classical D-stability occurs already at \(D=I\) or only elsewhere;
12. ecological loop coordinates \(g_{ij},L_3\).

For several examples, provide an explicit diagonal \(D\) witnessing failure of Hurwitz D-stability while the full orbit remains Matignon-stable.

---

# P3 — robustness in invariant and entry space

The paper needs to demonstrate that the genuinely fractional class is not a numerical knife-edge.

For representative witnesses compute:

## Invariant-space margins

\[
m_{\rm frac}=T_\alpha(\beta)-\kappa,
\]

\[
m_{\rm Cain}=\kappa-T_1(\beta).
\]

Normalize them in several dimensionless ways.

## Entry-space robustness

Estimate the smallest full-matrix perturbation (Frobenius and max-entry norms) that reaches:

1. the fractional boundary;
2. the classical Cain boundary;
3. a strict-P boundary.

Use multiple methods:
- local sensitivity/Jacobian from C-15;
- nonlinear constrained optimization;
- adversarial global search;
- high precision near the optimum.

Where possible produce rigorous lower/upper brackets, not only one optimizer result.

This phase is exploratory/certificatory: do not call the computed radius a theorem unless a rigorous bound is produced.

---

# P4 — verify C-15 differential structure

For broad beta/alpha grids independently verify:

\[
\frac{\partial T_\alpha}{\partial\beta_{ij}}
=
\frac{h_\alpha'(B^*)}{x_k^*}.
\]

Compute:
- finite-difference checks at high precision;
- Hessian eigenvalues;
- condition numbers;
- derivatives with respect to alpha;
- sensitivity of \(x^*\);
- permutation identities.

Search for analytically simple derivative identities that the Chief may prove.

Particularly study:
- symmetric slice;
- two-equal slice;
- extreme anisotropy;
- both alpha limits.

---

# P5 — publication phase diagrams

Generate plot-ready data, with no embedded styling assumptions, for:

1. \(T_\alpha/T_1\) vs alpha;
2. absolute width \(W_\alpha=T_\alpha-T_1\);
3. normalized width \(W_\alpha/T_1\);
4. C-11 sufficient fraction versus exact band;
5. ecological \((L_3,\alpha)\) boundaries;
6. pair-loop sensitivity surfaces;
7. optimizer coordinates \(x^*(\alpha,\beta)\);
8. asymptotic collapse near alpha=1;
9. blow-up near alpha=2/3.

For every plotted curve include:
- generation script;
- source CSV;
- commit SHA;
- whether values are FLOAT, HP or CERTIFIED.

No decorative figures. Every figure must support a theorem, corollary, comparison or interpretation.

---

# P6 — optional future-paper reconnaissance

Only if P0-P5 are complete and server time remains.

Focus **only** on the most promising Wave 1 n=4 family:

> two 3-cycles sharing an edge.

Do not re-run broad random n=4 searches.

Tasks:
- resolve the fractional/classical boundary numerically at high precision;
- search for a low-dimensional invariant reduction;
- identify symmetry reductions;
- derive candidate exact boundary equations;
- test whether the family reduces to an existing secant/network theorem.

Return a precise conjecture, not a generic heatmap.

This material is for a possible later paper and must remain separate from the current manuscript.

---

# Deliverables

If unlocked, create:

- \`research/COMPUTE_WAVE2_FINAL_REPORT.md\`
- \`computations/results/wave2/CERTIFIED_THRESHOLD_ATLAS.*\`
- \`computations/results/wave2/CANONICAL_WITNESSES.*\`
- \`computations/results/wave2/ROBUSTNESS_SUMMARY.*\`
- \`computations/results/wave2/C15_SENSITIVITY_VALIDATION.*\`
- \`computations/results/wave2/FIGURE_DATA/\`
- optional \`computations/results/wave2/N4_SHARED_EDGE_CONJECTURE.md\`

Final status:
- \`COMPUTE2_PASS\`
- \`COMPUTE2_FAIL\`
- \`PARTIAL/BLOCKED\`

## Resource rule

This is a server-scale bundled task. Do not return after a few plots or a small sample.

## Branch rule

Execution branch: `agent/compute-wave2-20260925`.

Do not start this task from the current compute-wave branch.

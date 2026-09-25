# fractional-d-stability-networks

Public research repository for the development of an exact theory of **fractional D-stability under positive diagonal scaling**, with a three-species ecological-network / generalized Lotka–Volterra interpretation.

> **Current research state — 2026-09-25:** the exploratory novelty phase has produced a concrete internal theorem package (C-07 through C-16). The mathematical center is now the exact low-dimensional structure of genuinely fractional D-stability, especially the exact \(3\times3\) threshold C-10. The package is **not yet submission-certified**: an independent adversarial proof audit, a high-compute validation wave, and a final specialist novelty audit are still required.

The repository is public:

**https://github.com/maximilianolucius/fractional-d-stability-networks**

---

## 1. Scientific center

For fixed \(0<\alpha<1\), define the Matignon stability region

\[
\Sigma_\alpha
=
\{z\neq0:|\arg z|>\alpha\pi/2\}.
\]

For real \(n\times n\) matrices define

\[
\mathcal F_\alpha^{(n)}
=
\left\{
A\in\mathbb R^{n\times n}:
\sigma(DA)\subset\Sigma_\alpha
\text{ for every positive diagonal }D
\right\}.
\]

Let \(\mathcal D_H^{(n)}\) be the classical Hurwitz D-stable class and define the genuinely fractional difference class

\[
\mathcal P_\alpha^{(n)}
=
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)}.
\]

The project is therefore **not** centered on the already-known fact that fractional order can stabilize an integer-order unstable equilibrium. The current mathematical question is:

> How does positive diagonal D-stability change when the Hurwitz half-plane is replaced by the Matignon angular region, and what exact new structure appears in the genuinely fractional class \(\mathcal P_\alpha^{(n)}\)?

The present theorem program answers this exactly in dimensions two and, on the full-dimensional robust stratum, three.

---

## 2. Current flagship theorem package

All statements below have analytic derivations in the repository. Until the independent proof audit is complete, they must be described as **internal theorems/corollaries**, not submission-certified results.

### C-07 — exact \(2\times2\) classification

For every \(0<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(2)}
\iff
\det A>0,
\qquad
a_{11}\le0,
\qquad
a_{22}\le0.
\]

Moreover,

\[
\mathcal P_\alpha^{(2)}
=
\left\{
\begin{pmatrix}
0&b\\
c&0
\end{pmatrix}:bc<0
\right\},
\]

so

\[
\operatorname{int}\mathcal P_\alpha^{(2)}=\varnothing.
\]

Canonical derivation: [`research/novelty/REOPENED_AUDIT_2026-09-24.md`](research/novelty/REOPENED_AUDIT_2026-09-24.md).

### C-09 — minimum robust dimension

For every \(0<\alpha<1\),

\[
\boxed{
\min\left\{
n:
\operatorname{int}\mathcal P_\alpha^{(n)}\neq\varnothing
\right\}=3.
}
\]

Dimension two permits only a lower-dimensional genuinely fractional separation, whereas dimension three admits a full-dimensional open class.

Canonical proof: [`research/THEOREM_C09_DIMENSION_THRESHOLD.md`](research/THEOREM_C09_DIMENSION_THRESHOLD.md).

**Novelty status:** `NOVELTY SURVIVES` in the targeted theorem-level audit, subject to a final independent pre-submission check.

### C-10 — exact \(3\times3\) variational characterization

On the full-dimensional stratum where \(-A\) is a strict P-matrix, define

\[
p_i=-a_{ii},\qquad
m_{ij}=\det A[\{i,j\}],\qquad
q=-\det A,
\]

and the positive-left-diagonal orbit invariants

\[
\beta_{12}=\frac{m_{12}}{p_1p_2},
\qquad
\beta_{13}=\frac{m_{13}}{p_1p_3},
\qquad
\beta_{23}=\frac{m_{23}}{p_2p_3},
\]

\[
\kappa=\frac{q}{p_1p_2p_3}.
\]

For \(2/3<\alpha<1\), C-10 reduces the complete positive diagonal orbit, modulo common scale, to the open simplex and defines an exact threshold \(T_\alpha(\beta)\) such that

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
}
\]

At the classical endpoint,

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+
\sqrt{\beta_{13}}
+
\sqrt{\beta_{23}}
\right)^2,
\]

recovering Cain's exact strict-P \(3\times3\) D-stability boundary.

The exact genuinely fractional full-dimensional band is therefore

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta)
}
\qquad
(2/3<\alpha<1).
\]

For \(0<\alpha\le2/3\), every strict-P\((-A)\) interior point is fractionally D-stable, and the classical Cain threshold separates the genuinely fractional part.

Canonical proof: [`research/THEOREM_C10_EXACT_3X3.md`](research/THEOREM_C10_EXACT_3X3.md).

**Novelty status:** `NOVELTY SURVIVES TARGETED SEARCH — PROVISIONAL`. This is presently the strongest candidate for the paper's central theorem.

### C-11 — fractional Cain sufficient certificate

The exact diagonal-orbit minimum

\[
\Phi(A)
=
\inf_{D\succ0}\frac{a_Db_D}{c_D}
=
\frac{
\left(
\sqrt{p_1m_{23}}
+
\sqrt{p_2m_{13}}
+
\sqrt{p_3m_{12}}
\right)^2
}{q}
\]

gives, for \(2/3<\alpha<1\), the simple sufficient condition

\[
\Phi(A)>
\left(1-2\cos(\alpha\pi/2)\right)^2
\Longrightarrow
A\in\mathcal F_\alpha^{(3)}.
\]

C-10 proves that this scalar condition is **sufficient but not necessary**.

Canonical proof: [`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`](research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md).

### C-12 / C-13 — GLV abundance invariance and ecological loop coordinates

For a positive generalized Lotka–Volterra equilibrium,

\[
J=\operatorname{diag}(x^*)A,
\qquad x_i^*>0,
\]

positive abundance scaling merely reparametrizes the full positive left-diagonal orbit. Hence membership in \(\mathcal F_\alpha\), \(\mathcal D_H\), and \(\mathcal P_\alpha\) is unchanged.

The exact \(3\times3\) invariants have the ecological feedback interpretation

\[
\beta_{ij}
=
1-
\frac{a_{ij}a_{ji}}{p_ip_j},
\]

and

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3,
\]

where \(L_3\) is the total normalized directed three-cycle feedback.

Thus C-10 has an exact pair-loop / three-cycle representation that is independent of the positive equilibrium abundance vector.

Canonical source: [`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`](research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md).

### C-14 — monotonicity and classical-limit rate

For \(2/3<\alpha<1\), the exact threshold is strictly decreasing in \(\alpha\):

\[
\alpha_1<\alpha_2
\quad\Longrightarrow\quad
T_{\alpha_1}(\beta)>T_{\alpha_2}(\beta).
\]

As \(\alpha\to1^-\),

\[
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2),
\]

with an explicit \(C(\beta)>0\). Thus the memory-only band collapses linearly toward the classical Cain boundary.

Canonical source: [`research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md`](research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md).

### C-15 — exact threshold geometry

For (2/3<alpha<1), the logarithm of the C-10 simplex objective is globally **strictly convex in logit coordinates**. Therefore the optimizer (x^*(alpha,eta)) is unique, nondegenerate and smooth.

C-15 also proves:

[
T_alpha(b,b,b)=27h_alpha(b/3),
]

so the Siami cyclic threshold is exactly the symmetric slice (eta=(1,1,1)); an explicit global ((x,r))-parametrization of the full threshold surface; the low-order asymptotic

[
T_alpha(eta)
=
rac{27}{K^3}
+
rac{9sumeta_{ij}-27}{K^2}
+
O(K^{-1}),
qquad
K=1-4cos^2(alphapi/2),
]

as (alphadownarrow2/3); and realizability of every invariant point with (kappage T_1(eta)) by an actual real matrix.

Canonical source: [`research/THEOREM_C15_THRESHOLD_GEOMETRY.md`](research/THEOREM_C15_THRESHOLD_GEOMETRY.md).

### C-16 — general positive-diagonal orbit reduction

For strict-P((-A)) in arbitrary dimension (n), positive diagonal scaling modulo a common scalar is exactly the open simplex (Delta_{n-1}^circ).

Using normalized signed principal minors (eta_I), the entire orbit is represented by

[
z^n+z^{n-1}+B_2(x)z^{n-2}+cdots+B_n(x),
]

with

[
B_k(x)=sum_{|I|=k}eta_Iprod_{iin I}x_i.
]

There are exactly

[
2^n-n-1
]

nontrivial orbit invariants: four in dimension three and eleven in dimension four.

C-16 is structural machinery rather than a standalone novelty claim. It shows that the unresolved (n=4) difficulty is quartic root geometry, not positive-diagonal orbit geometry.

Canonical source: [`research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md`](research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md).

---

## 3. What is known prior art and must **not** be claimed as novelty

The research audit has already removed several tempting but incorrect novelty claims.

The project does **not** claim novelty for:

- Matignon's fractional stability criterion;
- fractional stabilization of an integer-order unstable equilibrium;
- fixed-polynomial fractional Routh–Hurwitz criteria;
- generalized D-stability as a framework;
- relative D-stability or generic sector-gap results;
- classical robustness/interior/strong D-stability;
- single-cycle fractional secant conditions;
- P-matrix spectral wedges;
- Cain's classical \(3\times3\) D-stability theorem;
- generic ecological loop analysis.

In particular, the earlier single-cycle/cactus-centered direction was narrowed after comparison with Siami, Kushel/Kushel–Pavani, Abed, Cain, Kellogg, Cermák–Nechvátal and related literature.

The potentially new contribution is the **combined low-dimensional exact structure**, especially C-09 and C-10.

---

## 4. Novelty status

Two targeted audits are currently the most relevant:

- [`research/novelty/C09_TARGETED_AUDIT.md`](research/novelty/C09_TARGETED_AUDIT.md): **NOVELTY SURVIVES**.
- [`research/novelty/C10_TARGETED_AUDIT.md`](research/novelty/C10_TARGETED_AUDIT.md): **NOVELTY SURVIVES TARGETED SEARCH — PROVISIONAL**.

The C-10 audit explicitly compares against Cain, Bahl–Cain, Kushel, Kushel–Pavani, fractional Routh–Hurwitz literature, sector-stable polynomial work and Siami.

A final independent specialist novelty audit is still mandatory before submission.

### Historical-audit warning

Some chronological research files preserve earlier states of the project. In particular, [`research/NOVELTY_REPORT.md`](research/NOVELTY_REPORT.md) and [`research/novelty/novelty-audit.md`](research/novelty/novelty-audit.md) contain sections written **before C-09/C-10 closed the previously open high-order \(3\times3\) problem**.

For the current state, use the canonical-source order in Section 6 below rather than treating every historical audit paragraph as equally current.

---

## 5. Independent validation currently required

The project is deliberately locked against premature manuscript claims.

### Lane A — adversarial proof audit

Task:

[`research/PROOF_AUDIT_TASK_C07_C09_C11.md`](research/PROOF_AUDIT_TASK_C07_C09_C11.md)

Dedicated branch:

`agent/proof-audit-c07-c10-20260925`

The verifier must independently attempt to break C-07, C-09, C-10, C-11, C-14, C-15 and C-16 and return, for each theorem:

- `PASS`
- `PASS WITH MINOR FIX`
- `FAIL`

A failure must identify the exact broken implication or a smallest explicit counterexample.

Required final artifact:

`research/PROOF_AUDIT_C07_C09_C10_C11.md`

At the time of this README update, that final audit report is **not yet present on `main`**.

### Lane B — high-compute validation / discovery

Task:

[`research/COMPUTE_AGENT_WAVE1_TASK.md`](research/COMPUTE_AGENT_WAVE1_TASK.md)

Dedicated branch:

`agent/compute-c10-wave1-20260925`

The campaign includes:

- high-precision regression tests;
- robust numerical evaluation of the C-10 simplex threshold;
- million-scale adversarial comparison against direct spectral optimization;
- quantitative study of C-11 conservatism;
- C-14 asymptotic-rate checks;
- ecological motif phase datasets;
- \(n=4\) reconnaissance after validation phases.

Required final artifact:

`research/COMPUTE_WAVE1_FINAL_REPORT.md`

with status `COMPUTE_PASS`, `COMPUTE_FAIL`, or `PARTIAL/BLOCKED`.

The compute branch has completed P0, P1, P3/P3B, P4, P5 and the full float stage of P2. Current committed evidence includes:

- **121 tests passed** on aureus;
- **60/60 interval-certified** C-10 threshold anchors, with relative bracket widths near (10^{-39});
- C-10 threshold float/high-precision agreement at worst (7.1	imes10^{-12}) over 4000 random cases;
- exact symmetric-slice agreement with Siami at approximately (10^{-107}) relative scale;
- **2,060,000 C-10 adversarial cases + 120,000 controls** in the float P2 stage with zero persistent mismatches;
- **8100/8100** independent ecological-region classifications agreeing with C-10/C-13;
- C-14 high-precision rate validation down to (1-alpha=10^{-10});
- exploratory (n=4) reconnaissance.

The remaining compute gate is the high-precision recheck of 56,234 deliberately flagged near-boundary/numerically delicate P2 cases. Until `C10_STRESS_SUMMARY.json` and `C10_WORST_CASES.csv` are committed, Compute Wave 1 is a **strong interim pass**, not final `COMPUTE_PASS`.

Chief review: [`research/CHIEF_COMPUTE_WAVE1_INTERIM_REVIEW.md`](research/CHIEF_COMPUTE_WAVE1_INTERIM_REVIEW.md).

### Current CI state

The latest GitHub Actions run on `main` completes successfully, including package installation and `pytest`.

This is a software/regression gate only. Passing tests do **not** promote an internal theorem to a proof-certified result.

---

## 6. Canonical source-of-truth order

Because the repository contains the history of the research process, later canonical files override earlier exploratory status statements.

For the current mathematical state, read in this order:

1. [`research/research-status.md`](research/research-status.md)
2. [`research/CLAIMS.md`](research/CLAIMS.md)
3. [`research/SCOPE_MATRIX.md`](research/SCOPE_MATRIX.md)
4. [`research/THEOREM_C10_EXACT_3X3.md`](research/THEOREM_C10_EXACT_3X3.md)
5. [`research/THEOREM_C09_DIMENSION_THRESHOLD.md`](research/THEOREM_C09_DIMENSION_THRESHOLD.md)
6. [`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`](research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md)
7. [`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`](research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md)
8. [`research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md`](research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md)
9. [`research/THEOREM_C15_THRESHOLD_GEOMETRY.md`](research/THEOREM_C15_THRESHOLD_GEOMETRY.md)
10. [`research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md`](research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md)
11. [`research/novelty/C09_TARGETED_AUDIT.md`](research/novelty/C09_TARGETED_AUDIT.md)
12. [`research/novelty/C10_TARGETED_AUDIT.md`](research/novelty/C10_TARGETED_AUDIT.md)
13. [`research/Q1_PAPER_ARCHITECTURE.md`](research/Q1_PAPER_ARCHITECTURE.md)
14. [`AGENT_ACCESS.md`](AGENT_ACCESS.md)

The broad/reopened novelty reports remain useful for provenance and prior-art reasoning, but are not the final authority on theorem status.

---

## 7. Repository structure

```text
fractional-d-stability-networks/
├── README.md
├── AGENT_ACCESS.md
├── agent_directives_publishable_first_submission.md
├── research/
│   ├── research-status.md
│   ├── CLAIMS.md
│   ├── SCOPE_MATRIX.md
│   ├── THEOREM_C09_DIMENSION_THRESHOLD.md
│   ├── THEOREM_C10_EXACT_3X3.md
│   ├── THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md
│   ├── THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md
│   ├── THEOREM_C14_CLASSICAL_LIMIT_RATE.md
│   ├── THEOREM_C15_THRESHOLD_GEOMETRY.md
│   ├── THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md
│   ├── Q1_PAPER_ARCHITECTURE.md
│   ├── PROOF_AUDIT_TASK_C07_C09_C11.md
│   ├── COMPUTE_AGENT_WAVE1_TASK.md
│   └── novelty/
├── src/fdsn/
│   ├── spectral.py
│   ├── d_stability.py
│   ├── ecology.py
│   └── cubic_certificate.py
├── tests/
│   ├── test_spectral.py
│   ├── test_d_stability.py
│   └── test_cubic_certificate.py
├── computations/
├── experiments/
├── data/
├── paper/
├── reference-paper/
├── docs/
└── supplement/
```

### Important directory roles

- **`research/`** — theorem development, claim registry, scope control, literature/novelty audits, proof/computation assignments.
- **`src/fdsn/`** — executable implementations of spectral criteria, diagonal-scaling diagnostics and C-09/C-10/C-11 quantities.
- **`tests/`** — regression and theorem-formula corroboration tests.
- **`computations/`** — workspace for the large validation campaign; not theorem evidence unless a rigorous certificate is explicitly produced.
- **`paper/`** — current manuscript scaffold only. Final prose is intentionally locked.
- **`reference-paper/`** — immutable accepted-paper source package used as the MDPI *Mathematics* formatting and presentation reference.
- **`supplement/`** — internal research support only; the final paper must remain self-contained.

---

## 8. Computational implementation

The principal computational module is

[`src/fdsn/cubic_certificate.py`](src/fdsn/cubic_certificate.py).

It currently implements, among other quantities:

- strict-P\((-A)\) principal-minor checks;
- the C-11 exact orbit functional \(\Phi(A)\);
- an orbit-minimizing diagonal scaling;
- the fractional Cain sufficient threshold;
- the C-10 orbit invariants \((\beta,\kappa)\);
- the normalized fixed-cubic Matignon boundary \(h_\alpha\);
- numerical evaluation of the exact C-10 variational threshold \(T_\alpha(\beta)\);
- the classical Cain threshold \(T_1(\beta)\).

The numerical optimizer evaluates the analytically defined threshold; it is **not** itself a proof of C-10.

Finite sampling over positive diagonal matrices remains a falsification/corroboration tool only.

---

## 9. Reproducibility

Clone and test:

```bash
git clone https://github.com/maximilianolucius/fractional-d-stability-networks.git
cd fractional-d-stability-networks

python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python scripts/demo_fractional_stability.py
```

Minimal test invocation:

```bash
PYTHONPATH=src pytest -q
```

Every computational result intended for the paper should record:

- repository commit SHA;
- Python/package versions;
- matrix/model definition;
- parameter values and fractional order;
- diagonal-scaling normalization;
- random seed where applicable;
- optimizer/solver and tolerances;
- high-precision or interval backend when used.

---

## 10. Previous accepted paper — format reference

The complete accepted paper

> **Exact Stability Atlases and a Memoryless-Surrogate Failure Theorem for a Caputo Allee Predator-Prey Model**

is stored under [`reference-paper/`](reference-paper/), including:

- [`mathematics-4528508.tex`](reference-paper/mathematics-4528508.tex);
- [`mathematics-4528508.pdf`](reference-paper/mathematics-4528508.pdf);
- MDPI *Mathematics* class and bibliography files;
- all publication figure assets.

It is the formatting/editorial reference for the new manuscript.

Its mathematics does **not** establish novelty for this project.

---

## 11. Manuscript status

[`paper/`](paper/) is still a scaffold. The final manuscript is deliberately **locked** until the following gates are satisfied:

1. adversarial proof audit passes C-07/C-09/C-10/C-11/C-14/C-15/C-16;
2. high-compute wave finds no persistent counterexample;
3. final specialist novelty audit of C-10 is completed;
4. exact bibliographic theorem numbers and sign conventions are verified;
5. all central claims remain independent of finite numerical sampling.

A provisional Q1 architecture is already available in

[`research/Q1_PAPER_ARCHITECTURE.md`](research/Q1_PAPER_ARCHITECTURE.md).

The intended scientific center is not “fractional stability of an ecological model”, but:

> exact positive-diagonal Matignon stability in dimensions two and three, the first full-dimensional genuinely fractional class in dimension three, the exact fractional deformation of Cain's \(3\times3\) D-stability boundary, and its ecological feedback-loop interpretation.

---

## 12. Publication constraints

The controlling workflow is

[`agent_directives_publishable_first_submission.md`](agent_directives_publishable_first_submission.md).

Among its hard constraints:

- final journal-formatted article: **maximum 25 pages**;
- theorem first, prose second;
- no load-bearing result may depend on supplementary material;
- numerical experiments are corroboration, not proof;
- equality/boundary cases must be explicit;
- exact arithmetic should be used whenever it decides the claim;
- final figures must be publication-grade and mathematically informative;
- claims in title/abstract/conclusion must be traceable to theorem, certified computation, numerical object, citation or clearly labeled interpretation.

---

## 13. Current next actions

The immediate project order is:

1. complete the adversarial proof audit;
2. complete the high-compute C-10/C-14 validation wave;
3. reconcile any counterexample or proof issue before manuscript drafting;
4. run one final independent specialist novelty audit focused on C-10;
5. freeze the theorem package and bibliography;
6. only then rebuild the final paper from the accepted MDPI formatting reference.

No cactus-graph or \(n\ge4\) generalization should displace these validation gates. The \(n=4\) work currently belongs only to exploratory reconnaissance after C-10 validation.

---

## 14. Agent handoff

For an agent with GitHub access:

```text
Repository: maximilianolucius/fractional-d-stability-networks
Branch: main
```

Start with:

[`AGENT_ACCESS.md`](AGENT_ACCESS.md)

and then follow the role-specific task file.

Do not infer current theorem status from an older audit file when a later canonical theorem/status file exists.

---

## 15. Evidence labels used in this repository

- **INTERNAL THEOREM** — analytic proof exists in the repository; independent audit pending.
- **IMPORTED THEOREM** — published external result used under stated hypotheses.
- **CERTIFIED COMPUTATION** — rigorous inclusion/certificate with documented semantics.
- **NUMERICAL CORROBORATION** — floating-point experiment or stress test.
- **OPEN** — unresolved.
- **SUBMISSION-CERTIFIED** — reserved for results that have passed the project's proof, novelty and citation gates.

At present, the flagship C-09/C-10 package is **internal + novelty-surviving**, but not yet `SUBMISSION-CERTIFIED`.
# Research status — Chief Researcher canonical update

**Date:** 2026-09-25  
**State:** theorem package developed and triply validated; **novelty gate passed with repositioning**, **proof gate passed**, **compute gate passed**. Project phase: **Q1 MANUSCRIPT PRODUCTION**.

## Central objects

For fixed \(0<\alpha<1\),

\[
\Sigma_\alpha
=
\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

\[
\mathcal F_\alpha^{(n)}
=
\{A\in\mathbb R^{n\times n}:
\sigma(DA)\subset\Sigma_\alpha
\text{ for every positive diagonal }D\},
\]

and

\[
\mathcal P_\alpha^{(n)}
=
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)},
\]

where \(\mathcal D_H^{(n)}\) is the classical Hurwitz D-stable class.

The scientific center is the structure of the genuinely fractional difference class \(\mathcal P_\alpha\).

## Flagship theorem package

### C-07 — exact 2x2 classification

For every \(0<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(2)}
\iff
\det A>0,\quad a_{11}\le0,\quad a_{22}\le0.
\]

Hence \(\operatorname{int}\mathcal P_\alpha^{(2)}=\varnothing\).

### C-10 — exact robust 3x3 characterization

On the full-dimensional strict-P(-A) stratum define

\[
\beta_{12}=\frac{m_{12}}{p_1p_2},
\quad
\beta_{13}=\frac{m_{13}}{p_1p_3},
\quad
\beta_{23}=\frac{m_{23}}{p_2p_3},
\quad
\kappa=\frac{-\det A}{p_1p_2p_3}.
\]

For \(2/3<\alpha<1\), the entire positive diagonal orbit reduces exactly to a two-dimensional simplex and

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
}
\]

At \(\alpha=1\),

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+\sqrt{\beta_{13}}
+\sqrt{\beta_{23}}
\right)^2,
\]

recovering Cain's exact 3x3 D-stability boundary.

The exact genuinely fractional full-dimensional band is

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta).
}
\]

For \(0<\alpha\le2/3\), every strict-P(-A) matrix is fractionally D-stable.

### C-09 — minimum robust dimension

As a consequence of C-07/C-10,

\[
\boxed{
\min\left\{
n:
\operatorname{int}\mathcal P_\alpha^{(n)}
\ne\varnothing
\right\}=3
\quad
\forall\,0<\alpha<1.
}
\]

### C-11 — simple sufficient certificate

C-11 gives the exact orbit minimum

\[
\Phi(A)
=
\inf_{D\succ0}\frac{a_Db_D}{c_D}
\]

and a simple sufficient high-order certificate. C-10 and the Siami slice show that this scalar certificate is not necessary.

### C-12/C-13 — GLV and ecological loops

For a positive GLV equilibrium,

\[
J=\operatorname{diag}(x^*)A,
\]

membership in \(\mathcal F_\alpha\), \(\mathcal D_H\), and \(\mathcal P_\alpha\) is unchanged.

The exact 3x3 orbit coordinates have the motif form

\[
\beta_{ij}
=
1-\frac{a_{ij}a_{ji}}{p_ip_j},
\]

and

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3,
\]

where \(L_3\) is total normalized directed three-cycle feedback.

### C-14 — quantitative classical limit

For \(2/3<\alpha<1\), \(T_\alpha(\beta)\) is strictly decreasing in \(\alpha\), and

\[
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2)
\]

as \(\alpha\to1^-\), with explicit \(C(\beta)>0\).

## Novelty state

The final specialist literature audit is complete.

Final verdicts:

- C-09: **NOVEL WITH NARROWED CLAIM**;
- C-10: **NOVEL WITH NARROWED CLAIM**;
- C-15: **NOVEL WITH NARROWED CLAIM**;
- C-16: **NOT NOVEL** as a standalone result.

Overall:

```text
NOVELTY GATE PASSED WITH REPOSITIONING
```

The strongest surviving paper claim is the explicit exact real-3x3 elimination of the known generalized positive-diagonal Matignon forbidden-boundary problem, together with the full-dimensional dimension threshold and the theorem-specific convex threshold geometry.

Submission remains blocked by proof/computation validation, not by novelty.

Do not claim novelty for Matignon stabilization, fixed-polynomial fractional Routh-Hurwitz, generalized D-stability, relative D-stability, strong D-stability, single-cycle fractional secant conditions, P-matrix wedges, or Cain's classical theorem.

## Active independent validation lanes

### Lane A — adversarial proof verifier

Branch:

\`agent/proof-audit-c07-c10-20260925\`

Task:

\`research/PROOF_AUDIT_TASK_C07_C09_C11.md\`

The verifier must attempt to break C-07/C-09/C-10/C-11/C-14/C-15/C-16 before improving anything.

### Lane B — high-compute validation/discovery

Branch:

\`agent/compute-c10-wave1-20260925\`

Task:

\`research/COMPUTE_AGENT_WAVE1_TASK.md\`

This is a large campaign: high precision, million-scale adversarial tests, exact-threshold implementation, C-11 gap analysis, C-14 rate checks, ecological phase data, and n=4 reconnaissance.

## Manuscript state

All three scientific gates are now closed:

```text
NOVELTY GATE: PASS WITH REPOSITIONING
PROOF GATE: PASS
COMPUTE GATE: PASS
```

The project is now in **Q1 MANUSCRIPT PRODUCTION**.

Remaining work is editorial/scientific packaging rather than discovery validation:

1. final citation/theorem-number/sign-convention reconciliation;
2. manuscript rewrite around C-10/C-15, with C-09 as a major corollary;
3. publication-grade figures/tables and compact certified examples;
4. full LaTeX build and internal referee-style consistency pass.

Architecture planning is allowed. Final prose drafting is not.


## C-15/C-16 — threshold and orbit geometry

C-15 proves that the exact C-10 variational problem is globally strictly convex in logit coordinates, so its optimizer is unique, nondegenerate and smooth. It also gives a global threshold-surface parametrization, the alpha->2/3+ asymptotic, and realizability of the whole fractional band.

C-16 gives the general dimension-n positive-diagonal orbit reduction to the open simplex through normalized principal-minor invariants. The final novelty audit classifies this as **standard structural machinery, not a novel contribution**. It remains useful because it explains why n=3 has 4 nontrivial invariants and n=4 has 11.

These results strengthen the theorem package but do not change the current validation lock: final integration of Compute Wave 1 still waits for P2 high-precision completion.


## Proof gate closure

Independent report:

`research/PROOF_AUDIT_C07_C09_C10_C11.md`

Chief closure after applying all requested fixes:

`research/CHIEF_PROOF_AUDIT_CLOSURE.md`

Final proof-gate status:

```text
PROOF GATE PASSED
```


## Compute gate closure

Compute Wave 1 final branch:

`agent/compute-c10-wave1-20260925`

Final SHA:

`03165c107162e7099da29c13d40669474055bb22`

Integrated into `main`.

Key evidence:

- 121/121 tests passed;
- 2,180,000 adversarial/control cases in P2;
- 56,234/56,234 flagged cases high-precision consistent;
- zero genuine C-10 counterexamples;
- 1,350 strict-P extreme-scaling audits at 250 digits with zero negatives;
- 60 interval-certified (T_\alpha) anchors with relative width about (10^{-39});
- 8,100/8,100 ecological phase-region classifications consistent.

Final status:

```text
COMPUTE GATE PASSED
```

The computation corroborates the proofs; it does not replace them.

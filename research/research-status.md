# Research status — Chief Researcher canonical update

**Date:** 2026-09-25  
**State:** theorem package developed; independent adversarial proof audit and heavy compute validation pending.

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

Targeted searches found no theorem equivalent to C-09 or C-10. Their current status is:

- mathematically: INTERNAL THEOREM;
- novelty: SURVIVES TARGETED SEARCH / PROVISIONAL;
- submission: NOT YET CERTIFIED.

Do not claim novelty for Matignon stabilization, fixed-polynomial fractional Routh-Hurwitz, generalized D-stability, relative D-stability, strong D-stability, single-cycle fractional secant conditions, P-matrix wedges, or Cain's classical theorem.

## Active independent validation lanes

### Lane A — adversarial proof verifier

Branch:

`agent/proof-audit-c07-c10-20260925`

Task:

`research/PROOF_AUDIT_TASK_C07_C09_C11.md`

The verifier must attempt to break C-07/C-09/C-10/C-11/C-14 before improving anything.

### Lane B — high-compute validation/discovery

Branch:

`agent/compute-c10-wave1-20260925`

Task:

`research/COMPUTE_AGENT_WAVE1_TASK.md`

This is a large campaign: high precision, million-scale adversarial tests, exact-threshold implementation, C-11 gap analysis, C-14 rate checks, ecological phase data, and n=4 reconnaissance.

## Manuscript lock

Final title/abstract/conclusions remain locked until:

1. proof audit passes;
2. compute wave returns without a persistent counterexample;
3. final independent specialist novelty audit of C-10;
4. exact citations/theorem numbers and sign conventions are verified.

Architecture planning is allowed. Final prose drafting is not.


## C-15/C-16 — threshold and orbit geometry

C-15 proves that the exact C-10 variational problem is globally strictly convex in logit coordinates, so its optimizer is unique, nondegenerate and smooth. It also gives a global threshold-surface parametrization, the alpha->2/3+ asymptotic, and realizability of the whole fractional band.

C-16 gives the general dimension-n positive-diagonal orbit reduction to the open simplex through normalized principal-minor invariants. It explains structurally why n=3 has 4 nontrivial invariants and n=4 has 11.

These results strengthen the theorem package but do not change the current validation lock: final integration of Compute Wave 1 still waits for P2 high-precision completion.


---

# Chief extension state — 2026-09-26

## Double-Allee Kolmogorov extension

The user-requested extension has been investigated at theorem level.

### Original architecture

The shared-prey / two-competing-consumer extension is **KILLED** as the paper model: on the strict-P stratum its signed-cycle structure forces

```text
kappa < T1(beta),
```

so it cannot realize an open genuinely fractional-only D-stable band.

### Redesigned architecture

The active ecological model is a standard three-species intraguild-predation / omnivory Kolmogorov system with a double-Allee basal prey.

Chief theorem development currently provides:

1. exact positive coexistence geometry;
2. exact Kolmogorov positive-diagonal orbit equivalence;
3. exact beta_ij / kappa / L3 formulas;
4. constructive four-invariant realization on beta_ij>1;
5. biological embedding of any required positive self-slope s using the double-Allee law;
6. a nonempty open biologically feasible fractional-only parameter region for every 0<alpha<1;
7. a monotone m-path with ds/dm<0;
8. a tunable classical-to-fractional-only crossing with all non-m parameters fixed;
9. exact 2D codimension-one contrast;
10. one interval-certified alpha=0.9 interior witness.

Primary Chief files:

- `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
- `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
- `research/novelty/DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT.md`
- `research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md`

## Active STOP-THE-LINE validation lane

A dedicated compute-agent branch has been created:

`agent/compute-double-allee-proof-audit-20260926`

Task:

`research/COMPUTE_AGENT_DOUBLE_ALLEE_PROOF_AUDIT_TASK.md`

The agent must independently rederive and attempt to falsify DA-01 through DA-12 using symbolic algebra, high precision, interval arithmetic and direct spectral optimization.

Required final report:

`research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`

Overall acceptable statuses:

- `COMPUTE_AUDIT_PASS`
- `COMPUTE_AUDIT_PASS_WITH_FIXES`

Unacceptable / stop states:

- `COMPUTE_AUDIT_FAIL`
- unresolved `PARTIAL/BLOCKED` on any load-bearing theorem.

## Integration gate

The Chief will **not** integrate the Double-Allee extension into manuscript claims unless all load-bearing items pass:

- DA-02 no-go theorem;
- DA-03 invariant identities;
- DA-06 invariant realization;
- DA-07 biological embedding;
- DA-08 full-dimensional open-region theorem;
- DA-09/10/11 Allee-threshold crossing;
- DA-12 2D contrast.

A minor algebraic correction is acceptable only if it leaves the theorem statements unchanged or narrows them transparently without destroying the open-region/crossing conclusions.

A counterexample to DA-06, DA-07 or DA-08 returns the project to **MODIFY/KILL** immediately.

## Work allowed in parallel

Until the compute audit returns, the Chief may:
- continue literature/novelty verification;
- refine theorem dependencies and proof architecture;
- prepare a decision tree for standalone paper vs major extension.

The Chief may **not**:
- write final manuscript claims;
- change title/abstract/conclusion;
- merge the extension into main;
- call the new ecology theorem submission-certified.

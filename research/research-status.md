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

\`agent/proof-audit-c07-c10-20260925\`

Task:

\`research/PROOF_AUDIT_TASK_C07_C09_C11.md\`

The verifier must attempt to break C-07/C-09/C-10/C-11/C-14 before improving anything.

### Lane B — high-compute validation/discovery

Branch:

\`agent/compute-c10-wave1-20260925\`

Task:

\`research/COMPUTE_AGENT_WAVE1_TASK.md\`

This is a large campaign: high precision, million-scale adversarial tests, exact-threshold implementation, C-11 gap analysis, C-14 rate checks, ecological phase data, and n=4 reconnaissance.

## Manuscript lock

Final title/abstract/conclusions remain locked until:

1. proof audit passes;
2. compute wave returns without a persistent counterexample;
3. final independent specialist novelty audit of C-10;
4. exact citations/theorem numbers and sign conventions are verified.

Architecture planning is allowed. Final prose drafting is not.

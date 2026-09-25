# Claim registry — Chief canonical state

**Date:** 2026-09-24  
**Status:** theorem package developed; independent adversarial proof audit pending.

No theorem is submission-certified until the independent proof audit passes. "Novelty survives" means no theorem-equivalent prior art was found in the targeted audit; it is not a substitute for the final pre-submission literature check.

| ID | Statement / object | Novelty status | Proof status | Canonical source |
|---|---|---|---|---|
| C-01 | Matignon sector criterion for commensurate Caputo systems | KNOWN / STANDARD | IMPORTED THEOREM | Matignon; Brandibur-Garrappa-Kaslik |
| C-02 | fractionally stable while integer-order unstable | KNOWN / DERIVABLE | elementary | motivation only |
| C-03 | graph-indexed stability set S_alpha(G) | DEFINITION ONLY | no standalone theorem | subordinate to exact structural results |
| C-04 | F_alpha = {A: sigma(DA) subset Sigma_alpha for every D>0} | generalized-D-stability FRAMEWORK KNOWN | definition/framework | Kushel 2019; Kushel-Pavani |
| C-05 | single-cycle fractional D-stability/secant condition | CENTRAL NOVELTY REJECTED | substantially prior art | Siami 2020/2021 |
| C-06 | robustness/interior/strong D-stability as a generic concept | CLASSICAL PRIOR ART | framework known | Hartfiel; Abed; Lee-Edgar |
| C-07 | exact real 2x2 classification of F_alpha; int(P_alpha^(2)) empty | structural result; novelty secondary | **INTERNAL THEOREM** | reopened audit |
| C-08 | dimension-3 open separation for alpha<=2/3 via P-matrix wedge | ingredient of C-09 | **INTERNAL THEOREM** modulo Kellogg | Kellogg + C-07 |
| C-09 | minimum dimension with nonempty interior of P_alpha is 3 for every 0<alpha<1 | **NOVELTY SURVIVES TARGETED AUDIT — FLAGSHIP** | **INTERNAL THEOREM** | `research/THEOREM_C09_DIMENSION_THRESHOLD.md` |
| C-10 | exact variational 3x3 characterization on the full-dimensional strict-P(-A) stratum | **NOVELTY SURVIVES TARGETED SEARCH — FLAGSHIP PACKAGE** | **INTERNAL THEOREM** | `research/THEOREM_C10_EXACT_3X3.md` |
| C-11 | exact orbit minimum Phi(A) and simple fractional Cain sufficient certificate | structural/supporting result; standalone novelty unnecessary | **INTERNAL THEOREM** | `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md` |
| C-12 | GLV abundance-scaling invariance of F_alpha, D_H, P_alpha and orbit invariants | application bridge | **INTERNAL COROLLARY** | positive-diagonal orbit action |
| C-13 | exact ecological loop-coordinate form of C-10 | structural/ecological corollary; loop analysis itself classical | **INTERNAL COROLLARY** | `research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md` |

## Central definitions

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

where \(\mathcal D_H^{(n)}\) is classical Hurwitz D-stability.

## C-07 — exact 2x2 result

For every real

\[
A=
\begin{pmatrix}
a&b\\c&d
\end{pmatrix}
\]

and every \(0<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(2)}
\iff
\det A>0,\quad a\le0,\quad d\le0.
\]

Moreover,

\[
\mathcal P_\alpha^{(2)}
=
\left\{
\begin{pmatrix}
0&b\\c&0
\end{pmatrix}:bc<0
\right\},
\]

so

\[
\operatorname{int}\mathcal P_\alpha^{(2)}=\varnothing.
\]

## C-09 — provisional flagship dimension theorem

For every \(0<\alpha<1\),

\[
\boxed{
\min\left\{
n:
\operatorname{int}\mathcal P_\alpha^{(n)}
\ne\varnothing
\right\}
=3.
}
\]

Targeted novelty verdict: **NOVELTY SURVIVES**.

## C-10 — exact 3x3 robust-stratum characterization

Let \(-A\) be a strict P-matrix and define

\[
p_i=-a_{ii},
\qquad
m_{ij}=\det A[\{i,j\}],
\qquad
q=-\det A.
\]

Define the positive-left-diagonal orbit invariants

\[
\beta_{12}=\frac{m_{12}}{p_1p_2},
\quad
\beta_{13}=\frac{m_{13}}{p_1p_3},
\quad
\beta_{23}=\frac{m_{23}}{p_2p_3},
\]

and

\[
\kappa=\frac{q}{p_1p_2p_3}.
\]

For \(2/3<\alpha<1\), C-10 defines an explicit simplex threshold \(T_\alpha(\beta)\) and proves

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
}
\]

The classical limit is

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+\sqrt{\beta_{13}}
+\sqrt{\beta_{23}}
\right)^2,
\]

which recovers Cain's exact strict-P/type-2 \(3\times3\) D-stability threshold.

Furthermore,

\[
T_\alpha(\beta)>T_1(\beta)
\qquad(2/3<\alpha<1),
\]

so the exact full-dimensional genuinely fractional band is

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta).
}
\]

For \(0<\alpha\le2/3\),

\[
\operatorname{int}\mathcal F_\alpha^{(3)}
=
\{A:-A\text{ strict P}\},
\]

and

\[
\operatorname{int}\mathcal P_\alpha^{(3)}
=
\{A:-A\text{ strict P},\ \kappa>T_1(\beta)\}.
\]

## C-11 — simple sufficient certificate

Define

\[
\Phi(A)
=
\frac{
\left(
\sqrt{p_1m_{23}}
+\sqrt{p_2m_{13}}
+\sqrt{p_3m_{12}}
\right)^2
}{q}.
\]

Then

\[
\inf_{D\succ0}\frac{a_Db_D}{c_D}
=
\Phi(A).
\]

For \(2/3<\alpha<1\),

\[
\Phi(A)>
\left(1-2\cos(\alpha\pi/2)\right)^2
\Longrightarrow
A\in\mathcal F_\alpha^{(3)}.
\]

C-10 and the Siami cyclic family show this scalar condition is sufficient but **not necessary**.

## C-12/C-13 — GLV and motif interpretation

For a positive GLV equilibrium,

\[
J=\operatorname{diag}(x^*)A,
\]

positive diagonal orbit reparametrization gives

\[
J\in\mathcal F_\alpha
\iff
A\in\mathcal F_\alpha,
\]

\[
J\in\mathcal D_H
\iff
A\in\mathcal D_H,
\]

and

\[
J\in\mathcal P_\alpha
\iff
A\in\mathcal P_\alpha.
\]

The pair-loop coordinates are

\[
\beta_{ij}
=
1-\frac{a_{ij}a_{ji}}{p_ip_j},
\]

and, with

\[
L_3
=
\frac{
a_{12}a_{23}a_{31}
+
a_{13}a_{32}a_{21}
}{
p_1p_2p_3
},
\]

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3.
\]

Thus C-10 admits an exact feedback-motif interpretation.

## Prior-art locks

Do not claim as new:

- Matignon stabilization;
- critical-order monotonicity;
- fixed-polynomial fractional Routh-Hurwitz;
- generalized D-stability;
- relative D-stability / sector gaps;
- strong D-stability / interior as a concept;
- single-cycle fractional secant conditions;
- P-matrix spectral wedges;
- Cain's classical 3x3 D-stability theorem;
- generic ecological loop analysis.

## Q1 gate

Before final manuscript drafting:

1. adversarial proof audit of C-07/C-09/C-10/C-11 must PASS or PASS WITH MINOR FIX;
2. final independent specialist novelty audit of C-10;
3. exact bibliographic theorem numbers and sign conventions checked;
4. test suite green;
5. no numerical sampling used as theorem evidence.

## Evidence labels

- **INTERNAL THEOREM** — analytic proof present in repository; independent audit pending.
- **IMPORTED THEOREM** — published result used as lemma.
- **CERTIFIED COMPUTATION** — rigorous computational certificate.
- **NUMERICAL CORROBORATION** — floating-point evidence only.
- **OPEN** — unresolved.

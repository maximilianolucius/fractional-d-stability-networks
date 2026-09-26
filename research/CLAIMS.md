# Claim registry — Chief canonical state

**Date:** 2026-09-26  
**Status:** core 2D/3D theorem package developed; Caputo Double-Allee ecological realization externally audited and approved for manuscript integration.

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
| C-14 | strict monotonicity of T_alpha and sharp alpha->1 collapse rate | supporting structural corollary; standalone novelty not required | **INTERNAL COROLLARY** | `research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md` |
| C-15 | strict logit convexity, unique optimizer, explicit threshold-surface parametrization, alpha->2/3 asymptotic, and realizability of the full band | structural strengthening of C-10; standalone novelty pending | **INTERNAL THEOREM** | `research/THEOREM_C15_THRESHOLD_GEOMETRY.md` |
| C-16 | general positive-diagonal orbit reduction to a simplex using normalized principal-minor invariants | structural proposition; standalone novelty not claimed | **INTERNAL PROPOSITION** | `research/THEOREM_C16_GENERAL_SIMPLEX_REDUCTION.md` |
| C-17 | positive-equilibrium Kolmogorov orbit equivalence (J=operatorname{diag}(x^*)DF(x^*)) preserves the full positive-diagonal orbit | FOUNDATION / NOT NOVEL | **EXTERNALLY AUDITED LEMMA** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |
| C-18 | naive double-Allee prey + two competing consumers cannot realize the open fractional-only band on the strict-P stratum | theorem-level ecological no-go; novelty survives targeted search | **EXTERNALLY AUDITED THEOREM** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |
| C-19 | adopted 3D Caputo double-Allee IGP architecture has exact (eta_{ij},kappa,L_3) coordinates and a constructive four-invariant realization | theorem-level ecological realization | **EXTERNALLY AUDITED THEOREM** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |
| C-20 | for every (0<alpha<1), a nonempty open set in the full biological parameter space is in (mathcal F_alpha^{(3)}\setminusmathcal D_H^{(3)}) at a positive coexistence equilibrium | **FLAGSHIP ECOLOGICAL REALIZATION** | **EXTERNALLY AUDITED THEOREM** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |
| C-21 | along the positive strict-P coexistence branch, (dX/dm<0), (ds/dm<0), and (m) can drive a unique/transverse crossing from classical D-stability into the fractional-only band | theorem-level Double-Allee mechanism | **EXTERNALLY AUDITED THEOREM** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |
| C-22 | corresponding 2D double-Allee system has fractional-only D-stability only on a codimension-one condition, versus an open 3D IGP region | structural 2D/3D contrast | **EXTERNALLY AUDITED COROLLARY** | `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` |

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


## C-14 — monotone memory widening and classical-limit rate

For positive beta coordinates and 2/3<alpha<1, the exact C-10 threshold is strictly decreasing in alpha:

```text
alpha1 < alpha2  =>  T_alpha1(beta) > T_alpha2(beta).
```

As alpha->1 from below,

```text
T_alpha(beta)
=
T_1(beta)
+
C(beta) (1-alpha)
+
O((1-alpha)^2),
```

with explicit positive C(beta) given in `research/THEOREM_C14_CLASSICAL_LIMIT_RATE.md`.

Thus the genuinely fractional band closes linearly, with a motif-dependent coefficient.


## C-15 — exact geometry of the C-10 threshold

For every positive beta triple and 2/3<alpha<1, the log-threshold objective in logit simplex coordinates is globally strictly convex. Hence the C-10 minimizer is unique and nondegenerate.

Consequences proved in `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`:

- fully symmetric slice:
  ```text
  T_alpha(b,b,b) = 27 h_alpha(b/3);
  ```
- the Siami cyclic boundary is exactly the beta=(1,1,1) slice;
- two-equal beta slices reduce to one dimension;
- the entire threshold surface has an explicit global (x,r) parametrization;
- as alpha->2/3+,
  ```text
  T_alpha(beta)
  =
  27/K^3
  + [9 sum(beta)-27]/K^2
  + O(K^-1),
  K=1-4 cos^2(alpha*pi/2);
  ```
- every invariant point with kappa>=T1(beta) is realizable by a real matrix, so every exact fractional band
  ```text
  T1(beta)<kappa<T_alpha(beta)
  ```
  is nonempty in actual matrix space for every beta>0.


## C-16 — universal simplex reduction

For strict-P(-A) in dimension n, define signed principal minors
```text
m_I=(-1)^|I| det A[I]
```
and normalized invariants
```text
beta_I = m_I / product_{i in I} p_i.
```

After normalizing
```text
x_i = p_i d_i / sum_j p_j d_j,
```
the full positive diagonal orbit modulo common scale is exactly the open simplex.

The normalized characteristic polynomial is
```text
z^n + z^(n-1) + B_2(x) z^(n-2) + ... + B_n(x),
```
with
```text
B_k(x)=sum_{|I|=k} beta_I product_{i in I} x_i.
```

There are exactly `2^n-n-1` nontrivial orbit invariants: 4 in n=3 and 11 in n=4.


## C-17 — general Kolmogorov positive-equilibrium orbit bridge

For a commensurate Caputo Kolmogorov system

\[
{}^C D_t^\alpha x_i=x_iF_i(x),
\]

at a positive equilibrium \(x^*\),

\[
J(x^*)
=
\operatorname{diag}(x^*)DF(x^*).
\]

Hence

\[
\{DJ(x^*):D\succ0\}
=
\{EDF(x^*):E\succ0\}.
\]

This is a foundational bridge and is not claimed as novel.

## C-18 — competitive two-consumer no-go

For the natural double-Allee prey + two competing consumers extension, the exact cycle decomposition forces

\[
\kappa<T_1(\beta)
\]

throughout the relevant strict-\(P\) domain.

Therefore this architecture cannot realize an open genuinely fractional-only positive-diagonal stable region.

## C-19 — canonical Caputo Double-Allee IGP realization

The paper's canonical ecological model is

\[
{}^C D_t^\alpha x
=
x[g_{DA}(x)-q_1y-q_2z],
\]

\[
{}^C D_t^\alpha y
=
y[e_1q_1x-\mu_1-c_1y-hz],
\]

\[
{}^C D_t^\alpha z
=
z[e_2q_2x+e_3hy-\mu_2-c_2z],
\]

with

\[
g_{DA}(x)
=
\frac{r}{x+a}
\left(1-\frac{x}{K}\right)(x-m).
\]

At positive coexistence, its C-10 invariants have exact closed forms and the biological parameterization admits a constructive right inverse onto an open four-dimensional invariant region.

## C-20 — open biological fractional-only theorem

For every fixed \(0<\alpha<1\), there exists a nonempty open set in the full biological parameter space such that a positive coexistence equilibrium satisfies

\[
J
\in
\mathcal F_\alpha^{(3)}
\setminus
\mathcal D_H^{(3)}.
\]

The openness is in the full biological coordinate space, not merely in an engineered lower-dimensional construction family.

## C-21 — Allee-threshold monotonicity and Cain crossing

On the positive strict-\(P\) coexistence branch,

\[
q=-\det B
=
\Delta(s+\chi)>0
\]

and the external audit proves

\[
\frac{dX}{dm}<0,
\qquad
\frac{ds}{dm}<0.
\]

Thus

\[
t=\frac1s
\]

is strictly increasing in \(m\). The induced invariant path has a unique/transverse Cain crossing under the explicit crossing condition, and parameters can be chosen so that varying only \(m\) moves the fixed model locally from classical D-stability into the fractional-only Matignon region.

## C-22 — exact 2D/3D Double-Allee contrast

For the corresponding two-species Double-Allee system, the genuinely fractional difference occurs only on the codimension-one condition

\[
g_{DA}'(X)=0.
\]

The adopted three-species Caputo IGP architecture instead realizes a nonempty open fractional-only region.

## Ecological-model novelty lock

Do not claim novelty for:
- Caputo fractional ecological modeling;
- fractional intraguild predation;
- the double-Allee functional form;
- generic 3D predator-prey/IGP dynamics;
- local Matignon analysis at one fixed Jacobian.

The ecological novelty is restricted to C-18 through C-22.

## Ecological terminology lock

Use:
- **3D Caputo Double-Allee ecological realization**;
- **three-species Caputo Kolmogorov system**;
- **intraguild-predation/omnivory realization**.

Do not call the model **experimental** unless actual experimental calibration/data are introduced.

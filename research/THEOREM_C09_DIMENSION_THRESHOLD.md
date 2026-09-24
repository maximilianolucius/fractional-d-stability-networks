# C-09 — Dimension threshold for robust genuinely fractional D-stability

**Status:** INTERNAL ANALYTIC THEOREM; NOVELTY AUDIT REQUIRED  
**Date:** 2026-09-24  
**Scope:** real matrices, positive left-diagonal scaling, commensurate Matignon region

For `0<alpha<1` let

\[
\theta=\frac{\alpha\pi}{2},
\qquad
\Sigma_\alpha=\{z\neq0:|\arg z|>\theta\},
\]

\[
\mathcal F_\alpha^{(n)}
=
\{A\in\mathbb R^{n\times n}:\sigma(DA)\subset\Sigma_\alpha
\ \forall D\succ0\},
\]

and let `\mathcal D_H^{(n)}` denote classical Hurwitz D-stability. Define

\[
\mathcal P_\alpha^{(n)}
=
\mathcal F_\alpha^{(n)}\setminus\mathcal D_H^{(n)}.
\]

## Theorem

For every `0<alpha<1`,

\[
\boxed{
\min\{n:\operatorname{int}\mathcal P_\alpha^{(n)}\neq\varnothing\}=3.
}
\]

The n=1 case is trivial. The n=2 obstruction is C-07. The only new step below is to prove nonempty interior in n=3 for `2/3<alpha<1`; the range `0<alpha<=2/3` already follows from the Kellogg P-matrix wedge argument in the reopened audit.

---

## Lemma 1 — cubic angular certificate

Let

\[
p(z)=z^3+a z^2+b z+c,
\qquad a,b,c>0,
\]

and let

\[
\frac{\pi}{3}<\theta<\frac{\pi}{2}.
\]

If

\[
\boxed{
\frac{ab}{c}>\rho(\theta)
:=
\left(1-2\cos\theta\right)^2,
}
\]

then every zero `lambda` of `p` satisfies

\[
|\arg\lambda|>\theta.
\]

### Proof

A positive real zero is impossible because all coefficients are positive. Real zeros, if present, are therefore negative and already satisfy the angular condition.

Assume a nonreal conjugate pair violates the desired sector condition. Write it as

\[
r e^{\pm i\phi},
\qquad
0<\phi\le\theta,
\]

and write the third real root as `-s` with `s>0`. Put `t=s/r>0` and `u=\cos\phi`.

Matching coefficients from

\[
(z-r e^{i\phi})(z-r e^{-i\phi})(z+s)
\]

gives

\[
a=r(t-2u),
\]

\[
b=r^2(1-2tu),
\]

\[
c=t r^3.
\]

Since `a,b>0`,

\[
2u<t<\frac{1}{2u}.
\]

Hence `u<1/2`, equivalently `\phi>\pi/3`. Moreover,

\[
\frac{ab}{c}
=
\frac{(t-2u)(1-2tu)}{t}
=
1+4u^2-2u\left(t+\frac1t\right).
\]

Using `t+1/t\ge2`,

\[
\frac{ab}{c}
\le
(1-2u)^2.
\]

Because `\phi\le\theta<\pi/2`, we have `u=\cos\phi\ge\cos\theta`, and on `0<u<1/2` the function `(1-2u)^2` decreases with `u`. Therefore

\[
\frac{ab}{c}
\le
(1-2\cos\theta)^2
=
\rho(\theta),
\]

contradicting the hypothesis. Thus every zero lies outside the forbidden wedge. QED.

---

## Lemma 2 — uniform diagonal-orbit certificate for 3x3 matrices

Let `A in R^{3x3}` and suppose `-A` is a P-matrix. Define

\[
p_i=-a_{ii}>0,
\]

\[
m_{ij}=\det A[\{i,j\}]>0
\qquad(i<j),
\]

and

\[
q=-\det A>0.
\]

For `D=diag(d_1,d_2,d_3)\succ0`,

\[
\det(\lambda I-DA)
=
\lambda^3+a_D\lambda^2+b_D\lambda+c_D,
\]

where

\[
a_D=\sum_i p_i d_i,
\]

\[
b_D=
m_{12}d_1d_2+m_{13}d_1d_3+m_{23}d_2d_3,
\]

\[
c_D=q\,d_1d_2d_3.
\]

By AM-GM,

\[
a_D
\ge
3(p_1p_2p_3d_1d_2d_3)^{1/3},
\]

and

\[
b_D
\ge
3(m_{12}m_{13}m_{23})^{1/3}
(d_1d_2d_3)^{2/3}.
\]

Therefore

\[
\boxed{
\frac{a_D b_D}{c_D}
\ge
L(A)
:=
\frac{
9\left(
p_1p_2p_3m_{12}m_{13}m_{23}
\right)^{1/3}
}{q}
}
\]

for every `D\succ0`.

Consequently, for `2/3<alpha<1`, if

\[
L(A)>
\rho\!\left(\frac{\alpha\pi}{2}\right),
\]

then Lemma 1 gives

\[
A\in\mathcal F_\alpha^{(3)}.
\]

---

## Lemma 3 — explicit non-Hurwitz open centre for every alpha<1

Consider

\[
A_\gamma=
\begin{pmatrix}
-1&0&-\gamma\\
\gamma&-1&0\\
0&\gamma&-1
\end{pmatrix},
\qquad
\gamma>2.
\]

For this family,

\[
p_1=p_2=p_3=1,
\qquad
m_{12}=m_{13}=m_{23}=1,
\]

and

\[
q=-\det A_\gamma=1+\gamma^3.
\]

Hence

\[
L(A_\gamma)=\frac{9}{1+\gamma^3}.
\]

For `2/3<alpha<1`, let `theta=alpha pi/2`. Since `theta<pi/2`,

\[
0<\rho(\theta)<1.
\]

At `gamma=2`,

\[
L(A_2)=1>\rho(\theta).
\]

By continuity there exists a nonempty interval

\[
2<\gamma<
\left(\frac{9}{\rho(\theta)}-1\right)^{1/3}
\]

on which

\[
L(A_\gamma)>\rho(\theta).
\]

Therefore every such `A_gamma` lies in `F_alpha^(3)`.

On the other hand,

\[
\sigma(A_\gamma)
=
\left\{
-1-\gamma,\,
-1+\frac{\gamma}{2}
\pm i\frac{\sqrt3\,\gamma}{2}
\right\}.
\]

For `gamma>2` the conjugate pair has positive real part. Thus `A_gamma` is not Hurwitz at `D=I` and hence

\[
A_\gamma\notin\mathcal D_H^{(3)}.
\]

So

\[
A_\gamma\in\mathcal P_\alpha^{(3)}.
\]

---

## Lemma 4 — full-dimensional interior

All conditions used above are strict:

1. `-A_gamma` is a strict P-matrix;
2. `L(A_gamma)>rho(theta)`;
3. the spectral abscissa of `A_gamma` at `D=I` is positive.

Each condition persists under sufficiently small full-matrix perturbations. Hence there exists `epsilon>0` such that

\[
B_\epsilon(A_\gamma)
\subset
\mathcal F_\alpha^{(3)}
\setminus
\mathcal D_H^{(3)}
=
\mathcal P_\alpha^{(3)}.
\]

Therefore

\[
\operatorname{int}\mathcal P_\alpha^{(3)}\neq\varnothing
\qquad
\forall\,2/3<\alpha<1.
\]

Combining with the existing P-matrix/Kellogg proof for `0<alpha<=2/3` gives

\[
\operatorname{int}\mathcal P_\alpha^{(3)}\neq\varnothing
\qquad
\forall\,0<\alpha<1.
\]

C-07 gives

\[
\operatorname{int}\mathcal P_\alpha^{(2)}=\varnothing
\qquad
\forall\,0<\alpha<1.
\]

Thus the theorem follows.

---

## Interpretation

The threshold `alpha=2/3` is a threshold for the **universal P-matrix wedge certificate**, not for the existence of robust genuinely fractional D-stability in dimension three.

The new cubic inequality bridges the high-order region `2/3<alpha<1`.

As `alpha->1^-`,

\[
\rho(\alpha\pi/2)\to1,
\]

and the admissible interval for `gamma>2` collapses to the classical boundary `gamma=2`. This is exactly consistent with the disappearance of genuinely fractional separation at integer order.

---

## Novelty lock

This proof establishes mathematical validity internally. It does **not** establish bibliographic novelty.

Before promotion to a paper theorem, the novelty agent must compare it against:

- optimal fractional Routh-Hurwitz criteria for cubics;
- Cermák–Nechvátal and related exact coefficient-space descriptions;
- Ahmed–El-Sayed–El-Saka fractional Routh-Hurwitz conditions;
- Kushel/Kushel–Pavani generalized D-stability and forbidden-boundary results;
- classical 3x3 D-stability criteria (Cain and successors).

The exact object to audit is not Lemma 1 alone. The title-level candidate is the quantified dimension theorem

\[
\min\{n:\operatorname{int}(\mathcal F_\alpha^{(n)}\setminus\mathcal D_H^{(n)})\neq\varnothing\}=3
\quad
\forall\,0<\alpha<1.
\]

# C-15 — Convex geometry and explicit parametrization of the exact 3x3 threshold

**Date:** 2026-09-25  
**Status:** INTERNAL ANALYTIC THEOREM  
**Origin:** discovered during Compute Wave 1; independently re-derived by the Chief  
**Role:** strengthens C-10 by replacing a generic variational minimum with a strictly convex two-variable problem having a unique optimizer and an explicit global surface parametrization.

## 1. Setup

Fix

\[
\frac23<\alpha<1,
\qquad
\theta=\frac{\alpha\pi}{2},
\]

and put

\[
u=\cos\theta\in(0,1/2),
\qquad
K=1-4u^2>0.
\]

For \(b>0\), let \(r=r_\alpha(b)\) be the unique positive solution of

\[
b=Kr^2-2ur,
\qquad
r>\frac{2u}{K},
\]

and define

\[
h_\alpha(b)=r^2(1+2ur).
\]

For

\[
\beta=(\beta_{12},\beta_{13},\beta_{23})\in\mathbb R_{>0}^3
\]

and

\[
x=(x_1,x_2,x_3)\in\Delta_2^\circ,
\]

define

\[
B_\beta(x)
=
\beta_{12}x_1x_2
+
\beta_{13}x_1x_3
+
\beta_{23}x_2x_3,
\]

and the C-10 threshold objective

\[
F_{\alpha,\beta}(x)
=
\frac{h_\alpha(B_\beta(x))}{x_1x_2x_3}.
\]

Then

\[
T_\alpha(\beta)
=
\min_{x\in\Delta_2^\circ}F_{\alpha,\beta}(x).
\]

---

# 2. Strict convexity in logit coordinates

Parameterize the open simplex by

\[
x_1=\frac{e^{y_1}}{e^{y_1}+e^{y_2}+1},
\qquad
x_2=\frac{e^{y_2}}{e^{y_1}+e^{y_2}+1},
\qquad
x_3=\frac{1}{e^{y_1}+e^{y_2}+1}.
\]

Let

\[
L(y)
=
\log(e^{y_1}+e^{y_2}+1),
\]

and

\[
Q_\beta(y)
=
\log\!\left(
\beta_{12}e^{y_1+y_2}
+
\beta_{13}e^{y_1}
+
\beta_{23}e^{y_2}
\right).
\]

Then

\[
\log B_\beta(x(y))
=
Q_\beta(y)-2L(y).
\]

Define

\[
\phi_\alpha(s)
=
\log h_\alpha(e^s).
\]

The logarithm of the threshold objective is

\[
G_{\alpha,\beta}(y)
=
\log F_{\alpha,\beta}(x(y))
=
\phi_\alpha(Q_\beta-2L)
+
3L-y_1-y_2.
\]

## Lemma 1 — elasticity bounds

Let

\[
E_\alpha(b)
=
\frac{b\,h_\alpha'(b)}{h_\alpha(b)}
=
\phi_\alpha'(\log b).
\]

Then

\[
\boxed{
0<E_\alpha(b)<\frac32
}
\qquad
\forall b>0,
\]

and

\[
\boxed{
\frac{dE_\alpha}{db}>0.
}
\]

Hence

\[
\boxed{
\phi_\alpha'(s)\in(0,3/2),
\qquad
\phi_\alpha''(s)>0.
}
\]

### Proof

Using the boundary parameter \(r\),

\[
b=r(Kr-2u),
\]

\[
h=r^2(1+2ur),
\]

\[
\frac{db}{dr}=2(Kr-u)>0,
\]

and

\[
\frac{dh}{dr}=2r(1+3ur).
\]

Therefore

\[
E
=
\frac{b}{h}\frac{dh/dr}{db/dr}
=
\frac{(Kr-2u)(1+3ur)}
     {(Kr-u)(1+2ur)}.
\]

Factor

\[
E=A(r)B(r)
\]

with

\[
A(r)=\frac{Kr-2u}{Kr-u},
\qquad
B(r)=\frac{1+3ur}{1+2ur}.
\]

On \(r>2u/K\),

\[
A'(r)=\frac{Ku}{(Kr-u)^2}>0,
\]

and

\[
B'(r)=\frac{u}{(1+2ur)^2}>0.
\]

Moreover,

\[
E\to0
\quad\text{as}\quad
r\downarrow2u/K,
\]

and

\[
E\to\frac32
\quad\text{as}\quad
r\to\infty.
\]

Thus \(E\) is strictly increasing and takes values in \((0,3/2)\). Since \(b(r)\) is strictly increasing, \(E\) is strictly increasing in \(b\). Finally,

\[
\phi''(s)
=
\frac{dE}{ds}
=
b\frac{dE}{db}>0.
\]

QED.

---

## Theorem 1 — global strict convexity

For every

\[
\beta\in\mathbb R_{>0}^3
\]

and every

\[
2/3<\alpha<1,
\]

the function

\[
G_{\alpha,\beta}:\mathbb R^2\to\mathbb R
\]

is strictly convex.

Consequently:

1. \(F_{\alpha,\beta}\) has exactly one minimizer \(x^*(\alpha,\beta)\) in the open simplex;
2. the minimizer is nondegenerate;
3. \(T_\alpha(\beta)\) is smooth in \((\alpha,\beta)\) on the high-order domain.

### Proof

Set

\[
s=Q_\beta-2L.
\]

Differentiation gives

\[
\nabla^2G
=
\phi''(s)\nabla s\nabla s^\top
+
\phi'(s)\nabla^2Q_\beta
+
(3-2\phi'(s))\nabla^2L.
\]

Now:

- \(Q_\beta\) is a log-sum-exp of affine functions, so
  \[
  \nabla^2Q_\beta\succeq0;
  \]
- \(L\) is the log-sum-exp of the three affine functions \(y_1,y_2,0\), all with strictly positive softmax weights, hence
  \[
  \nabla^2L\succ0
  \]
  for every finite \(y\);
- by Lemma 1,
  \[
  \phi''(s)>0,\qquad
  \phi'(s)>0,\qquad
  3-2\phi'(s)>0.
  \]

Therefore

\[
\boxed{
\nabla^2G(y)\succ0
\quad
\forall y\in\mathbb R^2.
}
\]

It remains only to show existence of a minimizer. As \(y\to\infty\) in any direction, \(x(y)\) approaches the simplex boundary. Since \(h_\alpha(b)\) has a strictly positive finite limit as \(b\downarrow0\), while \(x_1x_2x_3\to0\),

\[
F_{\alpha,\beta}(x(y))\to\infty.
\]

Thus \(G\) is coercive. A unique global minimizer exists.

Nondegeneracy follows from the positive-definite Hessian. Smooth dependence then follows from the implicit-function theorem applied to

\[
\nabla_yG_{\alpha,\beta}(y^*)=0.
\]

QED.

---

# 3. Exact symmetry reductions

## Corollary 1 — fully symmetric slice

If

\[
\beta_{12}=\beta_{13}=\beta_{23}=b>0,
\]

then permutation symmetry plus uniqueness gives

\[
\boxed{
x^*=(1/3,1/3,1/3).
}
\]

Hence

\[
\boxed{
T_\alpha(b,b,b)
=
27\,h_\alpha(b/3).
}
\]

For \(b=1\),

\[
\boxed{
T_\alpha(1,1,1)
=
1+R_3(\alpha)^3,
}
\]

where

\[
R_3(\alpha)
=
\frac{\sin(\alpha\pi/2)}
     {\sin(\alpha\pi/2-\pi/3)}.
\]

Thus the exact C-10 surface contains the Siami cyclic boundary as its symmetric one-dimensional slice.

## Corollary 2 — two-equal slice

If

\[
\beta_{12}=\beta_{13},
\]

then invariance under \(2\leftrightarrow3\) and uniqueness imply

\[
\boxed{x_2^*=x_3^*.}
\]

Therefore this family reduces exactly to a one-dimensional minimization problem.

The analogous statements hold under permutations.

---

# 4. Explicit global parametrization of the threshold surface

At the unique minimizer define

\[
B=B_\beta(x),
\]

\[
\mu=\frac{h_\alpha'(B)}{h_\alpha(B)},
\]

and the elasticity

\[
E=\mu B.
\]

The constrained stationarity equations for

\[
\log h_\alpha(B)-\sum_i\log x_i
\]

under \(\sum_i x_i=1\) are

\[
\mu x_i\partial_iB
=
1+(2E-3)x_i.
\]

Write

\[
z_{ij}
=
\frac{\beta_{ij}x_ix_j}{B},
\qquad
z_{12}+z_{13}+z_{23}=1.
\]

Then

\[
E(z_{ij}+z_{ik})
=
1+(2E-3)x_i.
\]

Put (c_E=2E-3). Solving the resulting linear system yields

\[
z_{ij}
=
\frac{1+c_E(1-2x_k)}{2E}.
\]

Two identities are immediate and will be used in the inverse construction:

\[
z_{12}+z_{13}+z_{23}
=
\frac{3+c_E}{2E}
=
1,
\]

and

\[
E(z_{ij}+z_{ik})
=
1+c_E x_i.
\]

Therefore

\[
\boxed{
\beta_{ij}
=
\frac{
B\left[
1+(2E-3)(1-2x_k)
\right]
}{
2E\,x_ix_j
},
}
\]

where

\[
\{i,j,k\}=\{1,2,3\}.
\]

Since

\[
B=Kr^2-2ur,
\]

\[
E
=
\frac{(Kr-2u)(1+3ur)}
     {(Kr-u)(1+2ur)},
\]

and

\[
T_\alpha
=
\frac{r^2(1+2ur)}{x_1x_2x_3},
\]

the entire threshold surface admits an explicit three-parameter representation.

## Theorem 2 — global threshold-surface parametrization

Define the admissible domain

\[
\mathcal A_\alpha
=
\left\{
(x,r):
x\in\Delta_2^\circ,\;
r>2u/K,\;
1+(2E(r)-3)(1-2x_k)>0
\;\forall k
\right\}.
\]

The map

\[
\Psi_\alpha:\mathcal A_\alpha\to\mathbb R_{>0}^3
\]

defined by the formula above for \(\beta_{ij}\) is bijective.

For each \((x,r)\in\mathcal A_\alpha\),

\[
x=x^*(\alpha,\beta),
\]

and

\[
T_\alpha(\beta)
=
\frac{r^2(1+2ur)}{x_1x_2x_3}.
\]

### Proof

**Surjectivity.** Given any \(\beta>0\), Theorem 1 gives a unique optimizer \(x^*\). Set

\[
B=B_\beta(x^*)>0.
\]

Since

\[
r\mapsto Kr^2-2ur
\]

is strictly increasing on \(r>2u/K\), there is a unique \(r\) with

\[
B=Kr^2-2ur.
\]

The stationarity equations then recover the displayed formula for each \(\beta_{ij}\). Positivity of the original \(\beta_{ij}\) implies admissibility.

**Injectivity.** Suppose two admissible pairs \((x,r)\) and \((\tilde x,\tilde r)\) generate the same \(\beta\). By construction, each \(x\) is a stationary point of the same strictly convex objective. Hence

\[
x=\tilde x=x^*(\beta).
\]

Then \(B_\beta(x)\) is fixed, and strict monotonicity of \(Kr^2-2ur\) gives

\[
r=\tilde r.
\]

QED.

---

# 5. Universal transition as alpha approaches 2/3 from above

Let

\[
K=1-4\cos^2(\alpha\pi/2).
\]

Then

\[
K\downarrow0
\qquad
\text{as}
\qquad
\alpha\downarrow2/3.
\]

For fixed \(b\ge0\),

\[
\boxed{
K^3h_\alpha(b)
=
1+K(3b-1)+O(K^2).
}
\]

The expansion is uniform for \(b\) in compact intervals.

## Theorem 3 — low-order asymptotic of the exact threshold

For every fixed

\[
\beta\in\mathbb R_{>0}^3,
\]

as

\[
\alpha\downarrow2/3,
\]

\[
\boxed{
T_\alpha(\beta)
=
\frac{27}{K^3}
+
\frac{
9(\beta_{12}+\beta_{13}+\beta_{23})-27
}{K^2}
+
O(K^{-1}).
}
\]

Moreover,

\[
\boxed{
x^*(\alpha,\beta)
=
(1/3,1/3,1/3)+O(K).
}
\]

### Proof

Let

\[
P(x)=x_1x_2x_3.
\]

Multiplying the threshold objective by \(K^3\),

\[
K^3F_{\alpha,\beta}(x)
=
\frac1{P(x)}
+
K\frac{3B_\beta(x)-1}{P(x)}
+
O(K^2)
\]

uniformly on compact subsets of the open simplex.

The leading functional

\[
P(x)^{-1}
\]

has the unique nondegenerate minimum \(27\) at the simplex center

\[
x_c=(1/3,1/3,1/3).
\]

Boundary coercivity implies the exact minimizer remains in a fixed compact subset for sufficiently small \(K\). Standard smooth perturbation of a nondegenerate minimizer then gives

\[
x^*=x_c+O(K).
\]

Evaluating the first perturbation term at \(x_c\),

\[
P(x_c)=\frac1{27},
\]

and

\[
B_\beta(x_c)
=
\frac{\beta_{12}+\beta_{13}+\beta_{23}}9.
\]

Hence

\[
K^3T_\alpha
=
27
+
K\left[
9(\beta_{12}+\beta_{13}+\beta_{23})-27
\right]
+
O(K^2),
\]

which is equivalent to the stated expansion.

QED.

### Interpretation

The blow-up is universal at leading order:

\[
T_\alpha(\beta)\sim\frac{27}{K^3}.
\]

The first motif dependence enters only through

\[
\beta_{12}+\beta_{13}+\beta_{23}
\]

at order \(K^{-2}\).

---

# 6. Realizability of the full genuinely fractional band

The C-13 loop coordinates satisfy

\[
g_{ij}=1-\beta_{ij},
\]

and

\[
G=g_{12}g_{13}g_{23}.
\]

For the two oriented normalized three-cycle products,

\[
\ell_{123}\ell_{132}=G.
\]

Writing one of them as \(\ell\),

\[
L_3
=
\ell+\frac{G}{\ell}.
\]

The determinant coordinate is

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3.
\]

## Theorem 4 — every point above the Cain threshold is realizable

For every

\[
\beta\in\mathbb R_{>0}^3
\]

and every

\[
\boxed{
\kappa\ge T_1(\beta),
}
\]

there exists a real \(3\times3\) interaction matrix \(A\) with negative diagonal and exactly those orbit invariants \((\beta,\kappa)\).

Consequently, for every \(\beta>0\) and every \(2/3<\alpha<1\), the exact genuinely fractional interval

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta)
}
\]

is nonempty **in actual real matrix space**, not only in formal invariant coordinates.

### Proof

For prescribed \((\beta,\kappa)\), the required total three-cycle feedback is

\[
L_3
=
\sum_{i<j}\beta_{ij}-2-\kappa.
\]

At

\[
\kappa=T_1(\beta)
=
\left(
\sqrt{\beta_{12}}+
\sqrt{\beta_{13}}+
\sqrt{\beta_{23}}
\right)^2,
\]

we have

\[
L_3
=
-2
-
2\left(
\sqrt{\beta_{12}\beta_{13}}
+
\sqrt{\beta_{12}\beta_{23}}
+
\sqrt{\beta_{13}\beta_{23}}
\right).
\]

Thus \(L_3<0\), and increasing \(\kappa\) makes \(L_3\) still more negative.

If \(G\le0\), the quadratic

\[
\ell^2-L_3\ell+G=0
\]

has a real nonzero solution for every real \(L_3\).

If \(G>0\), real solutions require

\[
|L_3|\ge2\sqrt G.
\]

There are only two sign patterns:

1. all \(g_{ij}>0\), equivalently all \(\beta_{ij}<1\). Then
   \[
   \sqrt G<1<1+\sum\sqrt{\beta_i\beta_j};
   \]

2. exactly two \(g_{ij}<0\), equivalently exactly two \(\beta_{ij}>1\). Then
   \[
   \sqrt G
   <
   \sqrt{\beta_j\beta_k}
   <
   1+\sum\sqrt{\beta_i\beta_j}.
   \]

Therefore already at \(\kappa=T_1\),

\[
|L_3|
>
2\sqrt G.
\]

The inequality remains true for every larger \(\kappa\).

Choose a real root \(\ell\) of

\[
\ell^2-L_3\ell+G=0.
\]

Set \(p_1=p_2=p_3=1\). Choose six off-diagonal entries with pair products

\[
a_{ij}a_{ji}=g_{ij}
\]

and oriented loop product

\[
a_{12}a_{23}a_{31}=\ell.
\]

The opposite loop product is then automatically

\[
a_{13}a_{32}a_{21}=G/\ell.
\]

This constructs a real matrix with the desired \(\beta\), \(L_3\), and hence \(\kappa\).

The degenerate case \(G=0\) follows by taking one oriented loop product zero and tuning the other to \(L_3\).

QED.

---

# 7. Consequences for the paper

C-15 strengthens the C-10 package in four ways:

1. the exact threshold is a **strictly convex optimization problem**, not an arbitrary global minimization;
2. the optimizer is unique and smooth, rigorously validating the envelope argument used in C-14;
3. the entire threshold surface admits an explicit global \((x,r)\)-parametrization;
4. every point of the genuinely fractional invariant band is realized by an actual real matrix.

The \(\alpha\downarrow2/3\) asymptotic also explains analytically why the low-order Kellogg regime appears as an infinite-threshold limit.

None of these statements should be promoted as separately novel until literature audit; their current role is to sharpen and simplify the flagship C-10 theorem package.

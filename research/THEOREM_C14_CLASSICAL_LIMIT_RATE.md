# C-14 — Monotonicity and sharp classical-limit rate of the fractional Cain threshold

**Date:** 2026-09-25  
**Status:** INTERNAL ANALYTIC COROLLARY OF C-10  
**Role:** quantitative structural support for the Q1 theorem package; not required as standalone novelty

## Setup

For

\[
\frac23<\alpha<1
\]

let

\[
T_\alpha(\beta)
=
\min_{x\in\Delta_2^\circ}
\frac{h_\alpha(B_\beta(x))}{x_1x_2x_3}
\]

be the exact C-10 threshold, with

\[
B_\beta(x)
=
\beta_{12}x_1x_2+
\beta_{13}x_1x_3+
\beta_{23}x_2x_3.
\]

At the classical endpoint,

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+\sqrt{\beta_{13}}
+\sqrt{\beta_{23}}
\right)^2.
\]

Assume throughout

\[
\beta_{12},\beta_{13},\beta_{23}>0.
\]

---

## Theorem 1 — strict monotonicity in fractional order

If

\[
\frac23<\alpha_1<\alpha_2\le1,
\]

then

\[
\boxed{
T_{\alpha_1}(\beta)
>
T_{\alpha_2}(\beta).
}
\]

### Proof

For a fixed positive cubic

\[
p(\lambda)=\lambda^3+a\lambda^2+b\lambda+c,
\qquad a,b,c>0,
\]

the Matignon stability region strictly enlarges as alpha decreases.

For fixed \(a,b>0\), C-10 defines \(H_\theta(a,b)\) as the unique value of \(c\) placing a conjugate pair on the rays

\[
|\arg\lambda|=\theta,
\qquad
\theta=\alpha\pi/2.
\]

If \(\theta_1<\theta_2\), the cubic with

\[
c=H_{\theta_2}(a,b)
\]

has a conjugate pair at angle \(\theta_2\), hence lies strictly inside the wider sector condition associated with \(\theta_1\). Therefore

\[
H_{\theta_1}(a,b)
>
H_{\theta_2}(a,b).
\]

After normalization,

\[
h_{\alpha_1}(b)>h_{\alpha_2}(b)
\qquad
\forall b>0.
\]

Thus for every simplex point \(x\),

\[
\frac{h_{\alpha_1}(B_\beta(x))}{x_1x_2x_3}
>
\frac{h_{\alpha_2}(B_\beta(x))}{x_1x_2x_3}.
\]

Both minima are attained in the simplex interior. Evaluating the first objective at its own minimizer gives the strict inequality between minima. QED.

### Consequence

The exact memory-only width

\[
W_\alpha(\beta)
=
T_\alpha(\beta)-T_1(\beta)
\]

is strictly positive for every \(\alpha<1\) in the high-order regime and strictly increases as memory strengthens (alpha decreases).

---

## Theorem 2 — exact first-order collapse toward Cain

Define

\[
S
=
\sqrt{\beta_{12}}
+
\sqrt{\beta_{13}}
+
\sqrt{\beta_{23}},
\]

and

\[
G
=
\sqrt{\beta_{12}\beta_{13}\beta_{23}}.
\]

Then, as

\[
\alpha\to1^-,
\]

\[
\boxed{
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2),
}
\]

where

\[
\boxed{
C(\beta)
=
\pi
\left(
\frac{S^{5/2}}{\sqrt G}
+
S^{3/2}\sqrt G
\right)
=
\pi S^{3/2}
\left(
\frac{S}{\sqrt G}
+
\sqrt G
\right).
}
\]

Equivalently,

\[
\boxed{
W_\alpha(\beta)
\sim
C(\beta)(1-\alpha).
}
\]

### Step 1 — fixed-cubic boundary expansion

Put

\[
\theta=\frac{\alpha\pi}{2},
\qquad
u=\cos\theta.
\]

As \(\alpha\to1^-\),

\[
u
=
\frac{\pi}{2}(1-\alpha)
+
O((1-\alpha)^3).
\]

For normalized \(a=1\), C-10 writes the boundary through the positive solution \(r=r(u,b)\) of

\[
(1-4u^2)r^2-2ur-b=0,
\]

with

\[
h_\alpha(b)
=
r^2(1+2ur).
\]

At \(u=0\),

\[
r(0,b)=\sqrt b.
\]

Implicit differentiation of the quadratic gives

\[
\left.\frac{\partial r}{\partial u}\right|_{u=0}=1.
\]

Therefore

\[
\left.
\frac{\partial h}{\partial u}
\right|_{u=0}
=
2\sqrt b(1+b).
\]

Hence

\[
\boxed{
h_\alpha(b)
=
b
+
\pi(1-\alpha)\sqrt b(1+b)
+
O((1-\alpha)^2).
}
\]

---

## Step 2 — unique classical simplex minimizer

At alpha=1,

\[
\frac{B_\beta(x)}{x_1x_2x_3}
=
\frac{\beta_{23}}{x_1}
+
\frac{\beta_{13}}{x_2}
+
\frac{\beta_{12}}{x_3}.
\]

This strictly convex objective has the unique minimizer

\[
\boxed{
x_1^*
=
\frac{\sqrt{\beta_{23}}}{S},
\qquad
x_2^*
=
\frac{\sqrt{\beta_{13}}}{S},
\qquad
x_3^*
=
\frac{\sqrt{\beta_{12}}}{S}.
}
\]

At this point,

\[
x_1^*x_2^*x_3^*
=
\frac{G}{S^3},
\]

and

\[
B_\beta(x^*)
=
\frac{G}{S}.
\]

Because the minimizer is unique, interior, and nondegenerate, the envelope theorem applies to the smooth perturbation from alpha=1.

Thus the first-order change in \(T_\alpha\) is obtained by evaluating the first-order change in \(h_\alpha\) at \(x^*\):

\[
C(\beta)
=
\pi
\frac{
\sqrt{G/S}(1+G/S)
}{
G/S^3
}.
\]

Simplifying yields the stated formula. QED.

---

## Corollary — symmetric pair-loop slice

For

\[
\beta_{12}=\beta_{13}=\beta_{23}=1,
\]

we have

\[
S=3,
\qquad
G=1,
\]

so

\[
T_1=9
\]

and

\[
\boxed{
T_\alpha(1,1,1)
=
9
+
12\pi\sqrt3\,(1-\alpha)
+
O((1-\alpha)^2).
}
\]

Since the symmetric cyclic slice also satisfies

\[
T_\alpha(1,1,1)
=
1+R_3(\alpha)^3
\]

through the Siami boundary, this gives a direct asymptotic cross-check against the cyclic prior-art slice.

---

## Interpretation

C-10 showed that memory opens an exact band

\[
T_1(\beta)<\kappa<T_\alpha(\beta).
\]

C-14 quantifies how that band disappears:

- it narrows monotonically as alpha increases;
- near the integer-order limit its width is linear in \(1-\alpha\);
- the coefficient \(C(\beta)\) depends explicitly on the three normalized pair-loop invariants.

Thus the classical Cain surface is approached at a motif-dependent but analytically computable rate.

---

## Compute-agent validation request

The high-compute Wave 1 should independently verify:

1. monotonicity of \(T_\alpha\) over broad beta grids;
2. the first-order coefficient \(C(\beta)\);
3. the symmetric formula against the Siami slice;
4. the \(O((1-\alpha)^2)\) residual numerically at high precision.

Any disagreement should be surfaced as COMPUTE-FAIL for C-14, without modifying C-09/C-10 conclusions until reviewed by the Chief.

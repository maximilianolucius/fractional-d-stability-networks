# C-10 — Exact variational characterization of robust 3x3 fractional D-stability

**Date:** 2026-09-24  
**Status:** INTERNAL ANALYTIC THEOREM — exact on the strict-P(-A) stratum  
**Novelty status:** FINAL SPECIALIST VERDICT — NOVEL WITH NARROWED CLAIM  
**Scope:** real 3x3 matrices; positive left-diagonal scaling; commensurate order \(0<\alpha<1\)

This result closes the mathematical target posed in \`research/C10_EXACT_3X3_TASK.md\` on the full-dimensional stratum relevant to robust/interior fractional D-stability.

---

## 1. Notation

For \(0<\alpha<1\), set

\[
\theta=\frac{\alpha\pi}{2},
\qquad
\Sigma_\alpha=\{z\ne0:|\arg z|>\theta\}.
\]

For \(A\in\mathbb R^{3\times3}\),

\[
\mathcal F_\alpha^{(3)}
=
\{A:\sigma(DA)\subset\Sigma_\alpha\ \forall D\succ0\}.
\]

Let

\[
\mathcal D_H^{(3)}
=
\{A:DA\text{ is Hurwitz for every }D\succ0\}.
\]

Write

\[
\mathcal P_\alpha^{(3)}
=
\mathcal F_\alpha^{(3)}\setminus\mathcal D_H^{(3)}.
\]

Assume first that \(-A\) is a strict P-matrix. Define

\[
p_i=-a_{ii}>0,
\]

\[
m_{12}=\det A[\{1,2\}],
\quad
m_{13}=\det A[\{1,3\}],
\quad
m_{23}=\det A[\{2,3\}]>0,
\]

and

\[
q=-\det A>0.
\]

The four positive positive-left-diagonal orbit invariants are

\[
\beta_{12}=\frac{m_{12}}{p_1p_2},
\qquad
\beta_{13}=\frac{m_{13}}{p_1p_3},
\qquad
\beta_{23}=\frac{m_{23}}{p_2p_3},
\]

and

\[
\kappa=\frac{q}{p_1p_2p_3}.
\]

Indeed all four quantities are unchanged by \(A\mapsto EA\) with \(E\succ0\) diagonal.

---

## 2. Exact fixed-cubic Matignon boundary

The following lemma is the fixed-polynomial component. Its subject matter lies inside known optimal fractional Routh-Hurwitz theory; it is included here because it makes the diagonal-orbit elimination transparent.

### Lemma 1

Let

\[
p(\lambda)=\lambda^3+a\lambda^2+b\lambda+c,
\qquad
a,b,c>0,
\]

and assume

\[
\frac{\pi}{3}<\theta<\frac{\pi}{2}.
\]

Set

\[
u=\cos\theta\in(0,1/2),
\qquad
K=1-4u^2>0.
\]

Define

\[
r_\theta(a,b)
=
\frac{
ua+\sqrt{u^2a^2+Kb}
}{K},
\]

and

\[
H_\theta(a,b)
=
r_\theta(a,b)^2
\left(
a+2u\,r_\theta(a,b)
\right).
\]

Then

\[
\boxed{
|\arg\lambda_j|>\theta\ \forall j
\iff
c<H_\theta(a,b).
}
\]

Equality \(c=H_\theta(a,b)\) gives a conjugate pair exactly on the rays \(|\arg\lambda|=\theta\).

### Proof

A polynomial with positive coefficients has no positive real zero. A zero can leave the Matignon region only through one of the two boundary rays.

Put \(\lambda=re^{i\theta}\), \(r>0\). Separating imaginary parts in

\[
p(re^{i\theta})=0
\]

and dividing by \(r\sin\theta\) gives

\[
r^2\frac{\sin3\theta}{\sin\theta}
+
ar\frac{\sin2\theta}{\sin\theta}
+b=0.
\]

Using

\[
\frac{\sin3\theta}{\sin\theta}=4u^2-1=-K,
\qquad
\frac{\sin2\theta}{\sin\theta}=2u,
\]

we obtain

\[
Kr^2-2uar-b=0.
\]

This quadratic has exactly one positive solution, namely \(r=r_\theta(a,b)\).

The real part equation then reduces to

\[
c=r^2(a+2ur)=H_\theta(a,b).
\]

Thus for fixed \(a,b>0\) there is exactly one positive value of \(c\) at which a root lies on either Matignon boundary ray.

For \(c>0\) sufficiently small, one root is a small negative real root and the other two are roots of a Hurwitz quadratic perturbed from \(\lambda^2+a\lambda+b\), so all root arguments exceed \(\theta<\pi/2\). For \(c\to\infty\), the roots approach the cube-root directions of \(-c\), including the directions \(\pm\pi/3\), which violate \(\theta>\pi/3\). By continuity and uniqueness of the boundary value, stability holds exactly for \(c<H_\theta(a,b)\). QED.

### Homogeneity

For every \(s>0\),

\[
r_\theta(sa,s^2b)=s\,r_\theta(a,b),
\]

hence

\[
\boxed{
H_\theta(sa,s^2b)=s^3H_\theta(a,b).
}
\]

---

## 3. Exact simplex representation of the positive diagonal orbit

For

\[
D=\operatorname{diag}(d_1,d_2,d_3)\succ0,
\]

write

\[
\det(\lambda I-DA)
=
\lambda^3+a_D\lambda^2+b_D\lambda+c_D.
\]

Then

\[
a_D=p_1d_1+p_2d_2+p_3d_3,
\]

\[
b_D
=
m_{12}d_1d_2
+
m_{13}d_1d_3
+
m_{23}d_2d_3,
\]

and

\[
c_D=q\,d_1d_2d_3.
\]

Define normalized orbit coordinates

\[
x_i
=
\frac{p_id_i}{a_D},
\qquad i=1,2,3.
\]

Then

\[
x_i>0,
\qquad
x_1+x_2+x_3=1.
\]

Conversely, every point \(x\) of the open simplex

\[
\Delta_2^\circ
=
\{x_i>0:\ x_1+x_2+x_3=1\}
\]

is realized by some positive diagonal \(D\), unique modulo a common positive scalar.

Define

\[
B_\beta(x)
=
\beta_{12}x_1x_2
+
\beta_{13}x_1x_3
+
\beta_{23}x_2x_3.
\]

Then the normalized characteristic coefficients are exactly

\[
\frac{b_D}{a_D^2}=B_\beta(x),
\]

and

\[
\frac{c_D}{a_D^3}
=
\kappa x_1x_2x_3.
\]

Thus the entire positive diagonal orbit, modulo common scaling, has been eliminated in favor of the open two-dimensional simplex. Its closure is compact, while the threshold objective is coercive at the boundary.

---

## 4. Exact fractional Cain threshold

For \(2/3<\alpha<1\), write \(\theta=\alpha\pi/2\) and define the normalized fixed-cubic boundary function

\[
h_\alpha(b)
=
H_\theta(1,b).
\]

Equivalently, with

\[
u=\cos(\alpha\pi/2),
\qquad
K=1-4u^2,
\]

\[
r_\alpha(b)
=
\frac{u+\sqrt{u^2+Kb}}{K},
\]

and

\[
h_\alpha(b)
=
r_\alpha(b)^2
\left(1+2u\,r_\alpha(b)\right).
\]

Define the exact orbit threshold

\[
\boxed{
T_\alpha(\beta_{12},\beta_{13},\beta_{23})
=
\min_{x\in\Delta_2^\circ}
\frac{
h_\alpha(B_\beta(x))
}{
x_1x_2x_3
}.
}
\]

The minimum is attained in the interior. Indeed the numerator stays strictly positive on the closed simplex, while \(x_1x_2x_3\to0\) on its boundary.

### Theorem 1 — exact strict-P characterization

Let \(-A\) be a strict P-matrix and let \(2/3<\alpha<1\). Then

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta_{12},\beta_{13},\beta_{23}).
}
\]

### Proof

For any positive diagonal \(D\), let \(s=a_D\) and let \(x\in\Delta_2^\circ\) be its normalized orbit coordinate. Then

\[
a_D=s,
\qquad
b_D=s^2B_\beta(x),
\qquad
c_D=s^3\kappa x_1x_2x_3.
\]

By Lemma 1 and homogeneity,

\[
\sigma(DA)\subset\Sigma_\alpha
\]

if and only if

\[
s^3\kappa x_1x_2x_3
<
s^3h_\alpha(B_\beta(x)).
\]

Equivalently,

\[
\kappa
<
\frac{h_\alpha(B_\beta(x))}{x_1x_2x_3}.
\]

This must hold for every \(D\succ0\), equivalently for every \(x\in\Delta_2^\circ\). Taking the minimum over the simplex gives exactly the stated criterion. QED.

---

## 5. Exact characterization of the interior

### Lemma 2 — P0 necessity

If \(A\in\mathcal F_\alpha^{(3)}\) for any \(0<\alpha<1\), then

\[
-a_{ii}\ge0
\quad(i=1,2,3),
\]

all order-two principal minors of \(A\) are nonnegative, and

\[
-\det A>0.
\]

Hence \(-A\) is a \(P_0\)-matrix with strictly positive determinant.

#### Proof sketch

If \(a_{ii}>0\), let all row scalings except the \(i\)-th tend to zero. The limiting matrix has a positive real eigenvalue \(a_{ii}\), and nearby positive diagonal scalings violate Matignon stability.

If an order-two principal minor is negative, let the remaining row scaling tend to zero. The limiting \(2\times2\) principal block has negative determinant and therefore a positive real eigenvalue, again contradicting stability for nearby positive scalings.

Finally, a real \(3\times3\) Matignon-stable matrix has one negative real eigenvalue and either two additional negative real eigenvalues or a conjugate pair; in either case its determinant is strictly negative. QED.

### Corollary

If

\[
A\in\operatorname{int}\mathcal F_\alpha^{(3)},
\]

then \(-A\) is a **strict** P-matrix. Any vanishing order-one or order-two principal minor can be perturbed arbitrarily slightly to the forbidden sign, so it cannot occur at an interior point.

Conversely, the strict-P conditions are open.

### Theorem 2 — complete interior classification

For \(0<\alpha\le2/3\),

\[
\boxed{
\operatorname{int}\mathcal F_\alpha^{(3)}
=
\{A:-A\text{ is a strict P-matrix}\}.
}
\]

For \(2/3<\alpha<1\),

\[
\boxed{
\operatorname{int}\mathcal F_\alpha^{(3)}
=
\left\{
A:
-A\text{ strict P},
\quad
\kappa<T_\alpha(\beta)
\right\}.
}
\]

For the high-order case, the open simplex itself is not compact. Instead, the threshold objective extends continuously to (+infty) at the closed-simplex boundary. In a sufficiently small parameter neighborhood of any fixed strict-P matrix, (h_\alpha(B_\beta(x))) has a uniform positive lower bound, so all minimizers lie in one compact sublevel subset of the open simplex. The minimum therefore varies continuously, and the strict inequality (\kappa<T_\alpha(\beta)) persists under sufficiently small full-matrix perturbations.

For the low-order case, the Kellogg P-matrix wedge theorem gives \(\mathcal F_\alpha\) for every strict-P(-A) matrix, while Lemma 2 gives necessity for interior points.

---

## 6. Classical limit: exact recovery of Cain

As \(\alpha\to1^-\),

\[
u\to0,
\qquad
K\to1,
\qquad
r_\alpha(b)\to\sqrt b,
\qquad
h_\alpha(b)\to b.
\]

Hence

\[
T_\alpha(\beta)
\longrightarrow
T_1(\beta),
\]

where

\[
T_1(\beta)
=
\min_{x\in\Delta_2^\circ}
\frac{
\beta_{12}x_1x_2+
\beta_{13}x_1x_3+
\beta_{23}x_2x_3
}{
x_1x_2x_3
}.
\]

But

\[
\frac{B_\beta(x)}{x_1x_2x_3}
=
\frac{\beta_{12}}{x_3}
+
\frac{\beta_{13}}{x_2}
+
\frac{\beta_{23}}{x_1}.
\]

By Cauchy-Schwarz,

\[
\boxed{
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+
\sqrt{\beta_{13}}
+
\sqrt{\beta_{23}}
\right)^2.
}
\]

Thus

\[
\kappa<T_1(\beta)
\]

is exactly Cain's strict-P/type-2 \(3\times3\) D-stability condition.

The fractional theorem is therefore a genuine deformation of Cain's exact criterion, not merely an unrelated sufficient test.

---

## 7. Exact genuinely fractional band

For every \(2/3<\alpha<1\) and every \(b>0\),

\[
h_\alpha(b)>b.
\]

Indeed, if \(r=r_\alpha(b)\), then

\[
b=Kr^2-2ur
\]

and therefore

\[
h_\alpha(b)-b
=
(1-K)r^2+2ur^3+2ur
=
4u^2r^2+2ur(r^2+1)>0.
\]

Consequently

\[
\boxed{
T_\alpha(\beta)>T_1(\beta)
\qquad
(2/3<\alpha<1).
}
\]

Therefore, on the strict-P stratum,

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta)
}
\]

is an exact full-dimensional genuinely fractional band:

- \(A\in\mathcal F_\alpha^{(3)}\);
- \(A\notin\mathcal D_H^{(3)}\);
- the inequalities are strict, so \(A\) lies in the interior of the difference class.

Thus for \(2/3<\alpha<1\),

\[
\boxed{
\operatorname{int}\mathcal P_\alpha^{(3)}
=
\left\{
A:
-A\text{ strict P},
\quad
T_1(\beta)<\kappa<T_\alpha(\beta)
\right\}.
}
\]

For \(0<\alpha\le2/3\),

\[
\boxed{
\operatorname{int}\mathcal P_\alpha^{(3)}
=
\left\{
A:
-A\text{ strict P},
\quad
\kappa>T_1(\beta)
\right\}.
}
\]

The equality surface \(\kappa=T_1(\beta)\) is not interior to the genuinely fractional difference class.

---

## 8. Why the scalar Phi certificate is not necessary

C-11 defined

\[
\Phi(A)
=
\frac{
(\sqrt{p_1m_{23}}+
 \sqrt{p_2m_{13}}+
 \sqrt{p_3m_{12}})^2
}{q}.
\]

It yields the sufficient high-order condition

\[
\Phi(A)>
\rho_\alpha
=
(1-2\cos(\alpha\pi/2))^2.
\]

This is not necessary.

Consider

\[
A_\gamma=
\begin{pmatrix}
-1&0&-\gamma\\
\gamma&-1&0\\
0&\gamma&-1
\end{pmatrix}.
\]

Siami's Theorem 2, specialized to \(n=3\), gives the exact positive-diagonal-orbit condition

\[
A_\gamma\in\mathcal F_\alpha^{(3)}
\iff
\gamma<R_3(\alpha),
\]

where

\[
R_3(\alpha)
=
\frac{
\sin(\alpha\pi/2)
}{
\sin(\alpha\pi/2-\pi/3)
}
\qquad
(2/3<\alpha<1).
\]

The sufficiency applies after every positive row scaling because the geometric cycle ratio is invariant; necessity follows already at \(D=I\), where the diagonal coefficients are identical.

For this family,

\[
\Phi(A_\gamma)
=
\frac{9}{1+\gamma^3}.
\]

Define

\[
\gamma_\Phi(\alpha)
=
\left(
\frac{9}{\rho_\alpha}-1
\right)^{1/3}.
\]

Then

\[
\Phi(A_\gamma)>\rho_\alpha
\iff
\gamma<\gamma_\Phi(\alpha).
\]

### Strict gap theorem

For every \(2/3<\alpha<1\),

\[
\boxed{
2<\gamma_\Phi(\alpha)<R_3(\alpha).
}
\]

Hence every

\[
\gamma_\Phi(\alpha)<\gamma<R_3(\alpha)
\]

is an analytic counterexample to necessity of the C-11 scalar certificate.

#### Proof of \(\gamma_\Phi<R_3\)

Put

\[
\delta=\theta-\frac{\pi}{3}\in(0,\pi/6),
\qquad
t=\tan(\delta/2)\in(0,2-\sqrt3).
\]

Then

\[
R_3
=
\frac{2t+\sqrt3(1-t^2)}{4t},
\]

and

\[
\rho_\alpha
=
\frac{
4t^2(t+\sqrt3)^2
}{
(1+t^2)^2
}.
\]

Direct simplification gives

\[
R_3^3\rho_\alpha-(9-\rho_\alpha)
=
-\frac{3}{16t}
\left[
\sqrt3\,
(t-\sqrt3)^2
(t-2+\sqrt3)
(t+\sqrt3+2)
\right].
\]

All factors except \(t-2+\sqrt3\) are positive, while

\[
t<2-\sqrt3.
\]

Hence the right-hand side is positive, so

\[
R_3^3
>
\frac{9}{\rho_\alpha}-1
=
\gamma_\Phi^3.
\]

Also \(\rho_\alpha<1\) for \(\alpha<1\), so \(\gamma_\Phi>2\). QED.

---

## 9. Relation to C-09

C-09 follows immediately from the exact band characterization:

- dimension 2 has empty full-dimensional genuinely fractional interior;
- dimension 3 has a nonempty strict band between \(T_1\) and \(T_\alpha\) for every \(2/3<\alpha<1\);
- for \(0<\alpha\le2/3\), every strict-P(-A) matrix is fractionally D-stable, while the classical Cain threshold still cuts out a proper subset.

Thus C-10 explains **why** the dimension-threshold theorem is true.

---

## 10. Ecological interpretation

For a positive generalized Lotka-Volterra equilibrium,

\[
J=\operatorname{diag}(x^*)A.
\]

The invariants

\[
\beta_{12},\beta_{13},\beta_{23},\kappa
\]

are unchanged by positive left-diagonal scaling. Hence the exact threshold \(T_\alpha(\beta)\) and the classical threshold \(T_1(\beta)\) are abundance invariant.

Therefore the location of a three-species GLV interaction matrix inside the classical, genuinely fractional, or unstable region is a structural property of the interaction matrix rather than of the particular positive equilibrium abundance vector.

---

## 11. Research conclusion

**Outcome requested by C10 task:** EXACT CHARACTERIZATION PROVED, on the strict-P stratum; combined with the P0 necessity lemma, this gives a complete characterization of the full-dimensional interior.

The remaining mathematical work is no longer to find a 3x3 criterion. It is to:

1. independently audit the proof;
2. audit the novelty of the simplex-threshold representation \(T_\alpha(\beta)\);
3. characterize lower-dimensional boundary strata if desired;
4. derive interpretable motif/ecological corollaries from the four orbit invariants.

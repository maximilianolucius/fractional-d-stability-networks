# C-11 — Exact diagonal-orbit minimum and fractional Cain certificate

**Date:** 2026-09-24  
**Status:** INTERNAL ANALYTIC THEOREM — proof-audited with minor fixes applied  
**Novelty status:** structural support for C-10; standalone priority claim not required  
**Scope:** real \(3\times3\) matrices on the strict-\(P(-A)\) stratum

## 1. Setup

Let

\[
A\in\mathbb R^{3\times3}
\]

and assume \(-A\) is a strict P-matrix. Define

\[
p_i=-a_{ii}>0,
\]

\[
m_{12}=\det A[\{1,2\}],
\qquad
m_{13}=\det A[\{1,3\}],
\qquad
m_{23}=\det A[\{2,3\}]>0,
\]

and

\[
q=-\det A>0.
\]

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

---

## 2. Exact orbit minimum

Define

\[
\boxed{
\Phi(A)
=
\frac{
\left(
\sqrt{p_1m_{23}}
+
\sqrt{p_2m_{13}}
+
\sqrt{p_3m_{12}}
\right)^2
}{q}.
}
\]

### Theorem 1

\[
\boxed{
\inf_{D\succ0}\frac{a_Db_D}{c_D}
=
\Phi(A).
}
\]

The infimum is attained. Up to multiplication of \(D\) by a common positive scalar, an optimizer is

\[
\boxed{
d_1\propto\sqrt{\frac{m_{23}}{p_1}},
\qquad
d_2\propto\sqrt{\frac{m_{13}}{p_2}},
\qquad
d_3\propto\sqrt{\frac{m_{12}}{p_3}}.
}
\]

### Proof

Since

\[
\frac{b_D}{d_1d_2d_3}
=
\frac{m_{23}}{d_1}
+
\frac{m_{13}}{d_2}
+
\frac{m_{12}}{d_3},
\]

we have

\[
\frac{a_Db_D}{c_D}
=
\frac1q
\left(
p_1d_1+p_2d_2+p_3d_3
\right)
\left(
\frac{m_{23}}{d_1}
+
\frac{m_{13}}{d_2}
+
\frac{m_{12}}{d_3}
\right).
\]

Put

\[
x_i=p_id_i,
\]

and

\[
r_1=p_1m_{23},
\qquad
r_2=p_2m_{13},
\qquad
r_3=p_3m_{12}.
\]

Then

\[
\frac{a_Db_D}{c_D}
=
\frac1q
\left(\sum_i x_i\right)
\left(\sum_i\frac{r_i}{x_i}\right).
\]

Cauchy–Schwarz gives

\[
\left(\sum_i x_i\right)
\left(\sum_i\frac{r_i}{x_i}\right)
\ge
\left(\sum_i\sqrt{r_i}\right)^2.
\]

Equality holds if and only if

\[
x_i\propto\sqrt{r_i},
\]

which is exactly the stated diagonal optimizer. QED.

---

## 3. Classical Cain threshold

Let \(M=-A\), so \(M\) is a strict P-matrix in the positive-stability sign convention.

Cain's complete real \(3\times3\) D-stability theorem gives, on this strict-P/type-2 stratum,

\[
q
<
\left(
\sqrt{p_1m_{23}}
+
\sqrt{p_2m_{13}}
+
\sqrt{p_3m_{12}}
\right)^2.
\]

Therefore

\[
\boxed{
A\in\mathcal D_H^{(3)}
\iff
\Phi(A)>1.
}
\]

Because the orbit minimum in Theorem 1 is attained, equality

\[
\Phi(A)=1
\]

lies on the classical D-stability boundary and is not classically D-stable.

---

## 4. Fractional Cain-type sufficient certificate

Let

\[
\theta=\frac{\alpha\pi}{2},
\qquad
\frac23<\alpha<1,
\]

and define

\[
\boxed{
\rho_\alpha
=
\left(
1-2\cos\theta
\right)^2.
}
\]

### Theorem 2

If

\[
\boxed{
\Phi(A)>\rho_\alpha,
}
\]

then

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}.
}
\]

### Proof

For every \(D\succ0\), Theorem 1 gives

\[
\frac{a_Db_D}{c_D}
\ge
\Phi(A)
>
\rho_\alpha.
\]

The cubic angular certificate proved in C-09 then implies

\[
\sigma(DA)\subset\Sigma_\alpha
\]

for every positive diagonal \(D\). Hence

\[
A\in\mathcal F_\alpha^{(3)}.
\]

QED.

---

## 5. Explicit purely fractional band certified by \(\Phi\)

Since

\[
0<\rho_\alpha<1
\qquad
\left(\frac23<\alpha<1\right),
\]

the interval

\[
\boxed{
\rho_\alpha<\Phi(A)\le1
}
\]

is an explicit sufficient band for genuinely fractional multiplicative D-stability on the strict-P stratum.

Indeed:

- \(\Phi(A)>\rho_\alpha\) implies
  \[
  A\in\mathcal F_\alpha^{(3)};
  \]
- \(\Phi(A)\le1\) implies
  \[
  A\notin\mathcal D_H^{(3)}.
  \]

Therefore

\[
\boxed{
\rho_\alpha<\Phi(A)\le1
\Longrightarrow
A\in\mathcal P_\alpha^{(3)}.
}
\]

These matrices are not merely candidates: membership follows analytically from the two inequalities above.

C-10 and the Siami cyclic slice show that this \(\Phi\)-certificate is sufficient but not necessary.

---

## 6. Classical limit

As

\[
\alpha\to1^-,
\]

we have

\[
\rho_\alpha\to1.
\]

Thus the sufficient fractional threshold

\[
\Phi(A)>\rho_\alpha
\]

converges exactly to Cain's classical strict-P threshold

\[
\Phi(A)>1.
\]

---

## 7. Positive left-diagonal invariance

### Theorem 3

For every positive diagonal matrix

\[
E=\operatorname{diag}(e_1,e_2,e_3)\succ0,
\]

\[
\boxed{
\Phi(EA)=\Phi(A).
}
\]

### Proof

Under \(A\mapsto EA\),

\[
p_i(EA)=e_i p_i(A),
\]

\[
m_{jk}(EA)=e_je_k\,m_{jk}(A),
\]

and

\[
q(EA)=e_1e_2e_3\,q(A).
\]

Therefore each product \(p_i m_{jk}\), with \(\{i,j,k\}=\{1,2,3\}\), acquires the common factor

\[
e_1e_2e_3.
\]

The squared sum of square roots in the numerator of \(\Phi\) and the denominator \(q\) acquire the same factor, so their ratio is unchanged. QED.

The same quantity is invariant under simultaneous row/column permutation and under positive diagonal similarity.

---

## 8. GLV consequence

For a generalized Lotka–Volterra equilibrium with positive abundance vector \(x^*\),

\[
J
=
\operatorname{diag}(x^*)A.
\]

Hence

\[
\boxed{
\Phi(J)=\Phi(A).
}
\]

More fundamentally, multiplication by \(\operatorname{diag}(x^*)\) simply reparametrizes the full positive left-diagonal orbit. Therefore

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
\boxed{
J\in\mathcal P_\alpha
\iff
A\in\mathcal P_\alpha.
}
\]

Thus the genuinely fractional D-stability classification is independent of the particular positive equilibrium abundance vector.

---

## 9. Research role

C-11 is not the flagship novelty result.

Its role is to:

1. expose the exact classical Cain orbit functional;
2. provide a simple closed-form sufficient fractional certificate;
3. connect the high-order fractional regime continuously to \(\alpha=1\);
4. furnish an analytically explicit sub-band of \(\mathcal P_\alpha^{(3)}\);
5. support the more general exact characterization C-10.

The exact C-10 threshold \(T_\alpha(\beta)\) is strictly stronger than this scalar certificate.

# C-16 — General simplex reduction of the positive-diagonal orbit

**Date:** 2026-09-25  
**Status:** INTERNAL ANALYTIC PROPOSITION  
**Role:** general structural reduction underlying C-10 and the n=4 reconnaissance  
**Novelty status:** elementary/structural; do not claim standalone novelty.

## 1. Setup

Let

\[
A\in\mathbb R^{n\times n}
\]

and assume

\[
-A
\]

is a strict P-matrix.

For every nonempty index set

\[
I\subseteq\{1,\dots,n\},
\]

define the signed principal minor

\[
m_I
=
(-1)^{|I|}\det A[I].
\]

Because \(-A\) is a strict P-matrix,

\[
m_I>0.
\]

For singleton sets define

\[
p_i=m_{\{i\}}=-a_{ii}>0.
\]

For every \(|I|\ge2\), define the normalized principal-minor invariant

\[
\boxed{
\beta_I
=
\frac{m_I}{\prod_{i\in I}p_i}.
}
\]

These quantities are invariant under positive left-diagonal scaling.

---

# 2. Characteristic coefficients under positive diagonal scaling

Let

\[
D=\operatorname{diag}(d_1,\dots,d_n)\succ0.
\]

Write

\[
\det(\lambda I-DA)
=
\lambda^n
+
c_1(D)\lambda^{n-1}
+
\cdots
+
c_n(D).
\]

For every \(k=1,\dots,n\),

\[
\boxed{
c_k(D)
=
\sum_{\substack{I\subseteq[n]\\|I|=k}}
m_I
\prod_{i\in I}d_i.
}
\]

### Proof

The coefficient of \(\lambda^{n-k}\) in the characteristic polynomial is

\[
(-1)^k
\sum_{|I|=k}
\det(DA[I]).
\]

Since

\[
\det(DA[I])
=
\left(\prod_{i\in I}d_i\right)
\det A[I],
\]

we obtain

\[
c_k(D)
=
\sum_{|I|=k}
(-1)^k\det A[I]
\prod_{i\in I}d_i
=
\sum_{|I|=k}
m_I
\prod_{i\in I}d_i.
\]

QED.

In particular,

\[
c_1(D)
=
\sum_{i=1}^n p_i d_i>0.
\]

---

# 3. Orbit normalization to the simplex

Set

\[
s=c_1(D)
=
\sum_i p_i d_i.
\]

Define

\[
\boxed{
x_i
=
\frac{p_i d_i}{s}.
}
\]

Then

\[
x_i>0,
\qquad
\sum_i x_i=1.
\]

Thus

\[
x\in\Delta_{n-1}^\circ.
\]

Conversely, every

\[
x\in\Delta_{n-1}^\circ
\]

is realized by

\[
d_i
=
s\frac{x_i}{p_i}
\]

for any arbitrary common scalar \(s>0\).

Therefore:

\[
\boxed{
\{D\succ0\}/\{\text{common positive scalar}\}
\cong
\Delta_{n-1}^\circ.
}
\]

The normalized orbit is exactly the open simplex.

---

# 4. Normalized characteristic polynomial

Substituting

\[
d_i=sx_i/p_i
\]

into the coefficient formula gives

\[
c_k(D)
=
s^k
\sum_{|I|=k}
\beta_I
\prod_{i\in I}x_i.
\]

Define

\[
\boxed{
B_k(x)
=
\sum_{\substack{I\subseteq[n]\\|I|=k}}
\beta_I
\prod_{i\in I}x_i.
}
\]

Then

\[
\boxed{
\frac{c_k(D)}{s^k}
=
B_k(x).
}
\]

Now put

\[
\lambda=sz.
\]

Because \(s>0\),

\[
\arg\lambda=\arg z.
\]

Dividing the characteristic equation by \(s^n\) gives the normalized polynomial

\[
\boxed{
z^n
+
z^{n-1}
+
B_2(x)z^{n-2}
+
\cdots
+
B_n(x)
=0.
}
\]

Hence the entire positive diagonal orbit, for every spectral property invariant under multiplication of all eigenvalues by a common positive scalar, reduces exactly to the family of normalized polynomials indexed by

\[
x\in\Delta_{n-1}^\circ.
\]

---

# 5. General fractional D-stability reduction

For the Matignon region

\[
\Sigma_\alpha
=
\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

positive radial scaling leaves membership unchanged.

Therefore:

## Theorem

If \(-A\) is a strict P-matrix, then

\[
\boxed{
A\in\mathcal F_\alpha^{(n)}
}
\]

if and only if, for every

\[
x\in\Delta_{n-1}^\circ,
\]

all zeros of

\[
\boxed{
q_x(z)
=
z^n
+
z^{n-1}
+
B_2(x)z^{n-2}
+
\cdots
+
B_n(x)
}
\]

belong to \(\Sigma_\alpha\).

This eliminates the positive diagonal multiplier \(D\) exactly.

---

# 6. Number of orbit invariants

The singleton normalized minors are identically one:

\[
\beta_{\{i\}}=1.
\]

The nontrivial orbit data are therefore all principal-minor ratios with cardinality at least two.

Their number is

\[
\sum_{k=2}^n\binom nk
=
2^n-n-1.
\]

Thus:

- \(n=2\): \(1\) nontrivial invariant;
- \(n=3\): \(4\) nontrivial invariants;
- \(n=4\): \(11\) nontrivial invariants.

This explains exactly the coordinate counts observed in C-10 and Compute Wave 1.

---

# 7. Recovery of C-10

For \(n=3\),

\[
B_2(x)
=
\beta_{12}x_1x_2
+
\beta_{13}x_1x_3
+
\beta_{23}x_2x_3,
\]

and

\[
B_3(x)
=
\kappa x_1x_2x_3.
\]

Hence

\[
q_x(z)
=
z^3+z^2+B_2(x)z+\kappa x_1x_2x_3.
\]

The exact fixed-cubic Matignon boundary then reduces the all-\(x\) condition to the scalar threshold

\[
\kappa<T_\alpha(\beta),
\]

which is precisely C-10.

Thus C-10 is the complete \(n=3\) solution of the general simplex-reduced orbit problem.

---

# 8. The n=4 frontier

For \(n=4\),

\[
q_x(z)
=
z^4
+
z^3
+
B_2(x)z^2
+
B_3(x)z
+
B_4(x),
\]

where:

- \(B_2\) depends on the six normalized order-two principal minors;
- \(B_3\) depends on the four normalized order-three principal minors;
- \(B_4\) depends on the normalized determinant;

for a total of

\[
6+4+1=11
\]

nontrivial orbit invariants.

Compute Wave 1 independently verified the equality of spectral margins between this normalized quartic representation and direct matrices \(DA\) to numerical error of order \(10^{-13}\).

The unresolved n=4 problem is therefore no longer the diagonal orbit itself. It is the exact root-location geometry of this normalized quartic family over the three-simplex.

---

# 9. Research interpretation

C-16 separates the project into two layers:

1. **universal orbit geometry:** positive diagonal scaling modulo common scale is always a simplex and is governed by normalized principal-minor invariants;
2. **dimension-specific root geometry:** solving the exact Matignon condition for the normalized polynomial.

Dimension three is special because the fixed cubic boundary can be eliminated to a scalar threshold \(T_\alpha\).

Dimension four introduces a quartic boundary depending on two independent normalized coefficient coordinates, explaining why the next exact theorem is structurally harder.

C-16 should be used as a conceptual proposition in the manuscript, not as a standalone novelty claim.

# Theorem package — Double-Allee intraguild-predation realization of positive-diagonal Matignon stability

**Date:** 2026-09-26  
**Branch:** chief/double-allee-kolmogorov-20260926  
**Status:** internal analytic development; first independent compute/symbolic audit PASSED WITH MINOR FIXES at agent SHA 9235d75e8d407af8b726bb3bbfbf42c47d792151; second independent audit still pending

## 1. General Kolmogorov orbit lemma

Consider a commensurate fractional Kolmogorov system

~~~text
^C D_t^alpha x_i = x_i F_i(x),    i=1,...,n,
~~~

and let x* >> 0 be an equilibrium, so F(x*)=0.

Let

~~~text
B := DF(x*).
~~~

Then

~~~text
J(x*) = diag(x*) B.
~~~

### Proof

For G_i(x)=x_i F_i(x),

~~~text
partial_j G_i
=
delta_ij F_i(x)
+
x_i partial_j F_i(x).
~~~

At x*, F_i(x*)=0, hence

~~~text
J_ij(x*) = x_i* partial_j F_i(x*).
~~~

Therefore J(x*)=diag(x*)B.

### Positive-diagonal orbit equivalence

For any positive diagonal D,

~~~text
D J(x*) = [D diag(x*)] B.
~~~

The map

~~~text
D -> D diag(x*)
~~~

is a bijection of the positive diagonal cone onto itself. Therefore

~~~text
{ sigma(D J(x*)) : D>0 }
=
{ sigma(D B) : D>0 }.
~~~

Consequently

~~~text
J(x*) in F_alpha^(n)  iff  B in F_alpha^(n),

J(x*) in D_H^(n)      iff  B in D_H^(n).
~~~

Every normalized principal-minor invariant used by C-10 is also identical for J and B.

**Status:** elementary / foundation, not novelty.

---

# 2. No-go theorem for the naive two-consumer competition extension

Consider

~~~text
^C D^alpha x
 = x[g_DA(x)-q1 y-q2 z],

^C D^alpha y
 = y[e1 q1 x-mu1-c11 y-c12 z],

^C D^alpha z
 = z[e2 q2 x-mu2-c21 y-c22 z],
~~~

with all displayed parameters positive.

At a positive equilibrium let

~~~text
s := -g_DA'(x*) > 0.
~~~

Then

~~~text
B =
[ -s      -q1       -q2
  e1 q1   -c11      -c12
  e2 q2   -c21      -c22 ].
~~~

Assume -B is strict P, so in particular

~~~text
c11 c22 - c12 c21 > 0.
~~~

The C-10 invariants are

~~~text
beta12 = 1 + e1 q1^2/(s c11),

beta13 = 1 + e2 q2^2/(s c22),

beta23 = 1 - c12 c21/(c11 c22) > 0.
~~~

The normalized directed three-cycle coordinate is

~~~text
L3
=
q1 q2 (c12 e2 + c21 e1)/(s c11 c22)
> 0.
~~~

Hence

~~~text
kappa
=
beta12+beta13+beta23-2-L3.
~~~

Therefore

~~~text
kappa
<
beta12+beta13+beta23-2
<
beta12+beta13+beta23
<
T1(beta),
~~~

because

~~~text
T1(beta)
=
(sqrt(beta12)+sqrt(beta13)+sqrt(beta23))^2.
~~~

## No-go theorem

Every strict-P point of this architecture is already classically Hurwitz D-stable. In particular, this architecture has no full-dimensional parameter region satisfying

~~~text
T1(beta) < kappa < T_alpha(beta).
~~~

Thus the initial model proposed in the research vector cannot support the desired robust genuinely fractional effect.

---

# 3. Redesigned ecological architecture: double-Allee intraguild predation

Consider

~~~text
^C D^alpha x
=
x[
    g_DA(x)
    - q1 y
    - q2 z
  ],

^C D^alpha y
=
y[
    e1 q1 x
    - mu1
    - c1 y
    - h z
  ],

^C D^alpha z
=
z[
    e2 q2 x
    + e3 h y
    - mu2
    - c2 z
  ],
~~~

where

~~~text
g_DA(x)
=
r/(x+a) (1-x/K)(x-m),
~~~

and all displayed biological parameters are positive.

Interpretation:
- x: basal prey/resource with double Allee effect;
- y: intermediate consumer / intraguild prey;
- z: omnivorous top predator / intraguild predator;
- q1,q2: attacks on basal prey;
- h: predation of z on y;
- e1,e2,e3: conversion efficiencies;
- c1,c2: intraspecific self-limitation.

This is non-GLV because g_DA is nonlinear.

---

# 4. Exact positive coexistence geometry

Let a positive coexistence equilibrium be

~~~text
(X,Y,Z),    X,Y,Z>0.
~~~

The equilibrium equations are

~~~text
g_DA(X) = q1 Y + q2 Z,

c1 Y + h Z
=
e1 q1 X - mu1,

-e3 h Y + c2 Z
=
e2 q2 X - mu2.
~~~

Define

~~~text
Delta = c1 c2 + e3 h^2 > 0,

A1(X) = e1 q1 X - mu1,

A2(X) = e2 q2 X - mu2.
~~~

Then

~~~text
Y(X)
=
[c2 A1(X) - h A2(X)]/Delta,

Z(X)
=
[e3 h A1(X) + c1 A2(X)]/Delta.
~~~

Thus positive coexistence requires

~~~text
X>0,
Y(X)>0,
Z(X)>0,
g_DA(X)=q1Y(X)+q2Z(X).
~~~

The total predation term is affine in X:

~~~text
q1Y(X)+q2Z(X)
=
chi X - nu,
~~~

with

~~~text
chi
=
[
 e1 c2 q1^2
 + e2 c1 q2^2
 + h q1 q2 (e1 e3-e2)
]/Delta,
~~~

and

~~~text
nu
=
[
 mu1(q1 c2 + q2 e3 h)
 + mu2(q2 c1 - q1 h)
]/Delta.
~~~

Therefore X is determined by

~~~text
r/(X+a) (1-X/K)(X-m)
=
chi X - nu.
~~~

Multiplying out gives the explicit quadratic

~~~text
(r+K chi) X^2
-
[r(K+m)-K chi a+K nu] X
+
r K m - K nu a
=
0.
~~~

Hence the positive equilibrium is analytically tractable: candidate X values are given by the quadratic formula, followed by explicit Y(X),Z(X).

---

# 5. Exact reduced matrix and invariant coordinates

At coexistence define

~~~text
s := -g_DA'(X).
~~~

Then

~~~text
B = DF(X,Y,Z)
=
[ -s       -q1      -q2
  e1 q1    -c1      -h
  e2 q2     e3 h    -c2 ].
~~~

The order-one signed principal minors are

~~~text
p1=s,
p2=c1,
p3=c2.
~~~

The order-two principal minors are

~~~text
m12
=
s c1 + e1 q1^2,

m13
=
s c2 + e2 q2^2,

m23
=
c1 c2 + e3 h^2.
~~~

Thus whenever s>0 all order-one and order-two strict-P conditions hold automatically. Full strict-P additionally requires q=-det B>0. The condition e1 e3>e2 is a simple sufficient condition for q>0, but it is not necessary.

The determinant coordinate is

~~~text
q := -det B
=
s(c1 c2+e3 h^2)
+
c1 e2 q2^2
+
c2 e1 q1^2
+
h q1 q2(e1 e3-e2).
~~~

Hence

~~~text
beta12
=
1 + e1 q1^2/(s c1),

beta13
=
1 + e2 q2^2/(s c2),

beta23
=
1 + e3 h^2/(c1 c2),
~~~

and

~~~text
kappa
=
beta12+beta13+beta23-2
+
h q1 q2(e1 e3-e2)/(s c1 c2).
~~~

The signed directed-three-cycle coordinate is

~~~text
L3
=
h q1 q2(e2-e1 e3)/(s c1 c2).
~~~

Therefore

~~~text
kappa
=
beta12+beta13+beta23-2-L3.
~~~

When

~~~text
e1 e3 > e2,
~~~

one has

~~~text
L3<0,
~~~

so the omnivory/intraguild-predation loop raises kappa above the pair-loop baseline.

This sign reversal is the exact structural mechanism that the failed two-consumer model lacks.

---

# 6. Invariant realization theorem

## Theorem — IGP realization of the strict fractional band

Fix any invariant target

~~~text
beta12>1,
beta13>1,
beta23>1,
~~~

and any

~~~text
kappa
>
beta12+beta13+beta23-2.
~~~

Then there exist positive IGP parameters

~~~text
s,c1,c2,q1,q2,h,e1,e2,e3
~~~

such that the reduced matrix B above has exactly those four C-10 invariants.

Moreover, for every such target the construction can be chosen with

~~~text
0<e1,e2,e3<1
~~~

and

~~~text
e1 e3 > e2.
~~~

This does not require the additional assumption kappa>T1(beta); it follows already from the realization hypothesis R>0.

### Constructive proof

Set

~~~text
A = beta12-1 > 0,
B0 = beta13-1 > 0,
C = beta23-1 > 0,

R
=
kappa-(beta12+beta13+beta23-2).
~~~

Then R>0.

Define

~~~text
rho = R/sqrt(A B0 C).
~~~

Let

~~~text
tau
=
[rho + sqrt(rho^2+4)]/2
>1.
~~~

Then

~~~text
tau - 1/tau = rho.
~~~

Choose any

~~~text
eta in (0,1)
~~~

and set

~~~text
e1=e3=eta,

e2=eta^2/tau^2.
~~~

Hence

~~~text
e1 e3/e2=tau^2>1,
~~~

so e1 e3>e2.

Choose arbitrary s,c1,c2>0 and define

~~~text
q1
=
sqrt(A s c1/e1),

q2
=
sqrt(B0 s c2/e2),

h
=
sqrt(C c1 c2/e3).
~~~

Then the three beta coordinates are exactly the prescribed values.

Moreover,

~~~text
h q1 q2(e1 e3-e2)/(s c1 c2)
=
sqrt(A B0 C)
[
 sqrt(e1 e3/e2)
 -
 sqrt(e2/(e1 e3))
]
=
sqrt(A B0 C)(tau-1/tau)
=
R.
~~~

Therefore the determinant invariant is exactly the prescribed kappa.

QED.

### Consequence

The ecological IGP architecture is not trapped in a codimension-one or degenerate invariant subset.

It realizes a four-dimensional open invariant family containing

~~~text
{ beta_ij>1, kappa>T1(beta) }.
~~~

Thus it passes the main invariant-accessibility kill test.

---

# 7. Double-Allee realization at a positive equilibrium

The invariant realization above specifies the desired reduced matrix slope

~~~text
s>0.
~~~

It remains to realize that s using the double-Allee prey law at a biologically feasible equilibrium.

Fix

~~~text
a>0,
0<m<X<K,
~~~

and define

~~~text
H_A(X;m,a,K)
=
1/(K-X)
-
1/(X-m)
+
1/(X+a).
~~~

Choose K sufficiently close to X that

~~~text
H_A>0.
~~~

Set

~~~text
Q = s/H_A >0.
~~~

Choose any split parameter xi in (0,1) and set

~~~text
Y = xi Q/q1,

Z = (1-xi) Q/q2.
~~~

Then

~~~text
q1Y+q2Z=Q.
~~~

For K sufficiently close to X, H_A is arbitrarily large and therefore Q,Y,Z are arbitrarily small.

Define

~~~text
mu1
=
e1 q1 X
-
c1 Y
-
h Z,

mu2
=
e2 q2 X
+
e3 h Y
-
c2 Z.
~~~

For sufficiently small Q both are positive.

Finally set

~~~text
r
=
Q(X+a)
/
[
 (1-X/K)(X-m)
].
~~~

Then

~~~text
g_DA(X)=Q=q1Y+q2Z.
~~~

Also

~~~text
g_DA'(X)
=
g_DA(X)
[
 -1/(K-X)
 +1/(X-m)
 -1/(X+a)
]
=
-Q H_A
=
-s.
~~~

Thus the positive equilibrium (X,Y,Z) has precisely the reduced matrix B specified in the invariant realization theorem.

---

# 8. Main open-region theorem

## Theorem — robust genuinely fractional double-Allee coexistence

Fix any

~~~text
0 < alpha < 1.
~~~

Then there exists a nonempty open set of biologically feasible parameters of the double-Allee IGP system such that a positive coexistence equilibrium on the constructed smooth branch is

~~~text
positive-diagonal Matignon stable
~~~

under every positive diagonal left scaling, but is simultaneously

~~~text
not Hurwitz D-stable.
~~~

### Proof

### Case 1: 2/3 < alpha < 1

Choose any

~~~text
beta in (1,infinity)^3.
~~~

By C-10/C-15,

~~~text
T_alpha(beta)>T1(beta).
~~~

Choose

~~~text
T1(beta)
<
kappa
<
T_alpha(beta).
~~~

The invariant realization theorem constructs a positive IGP reduced matrix with exactly those invariants and with e1 e3>e2.

The double-Allee realization theorem then constructs positive biological parameters and a positive coexistence equilibrium having that reduced matrix.

By C-10,

~~~text
B in F_alpha^(3),
B notin D_H^(3).
~~~

By the Kolmogorov orbit lemma, the same is true for the actual equilibrium Jacobian J=diag(x*)B.

### Case 2: 0 < alpha <= 2/3

Choose beta in (1,infinity)^3 and any

~~~text
kappa>T1(beta).
~~~

The construction again gives strict-P(-B). By the Kellogg/low-order C-10 result, every strict-P(-B) matrix belongs to F_alpha^(3) in this range, while kappa>T1 excludes classical Hurwitz D-stability.

### Openness

All biological feasibility inequalities are strict.

Also

~~~text
-det B
=
kappa s c1 c2
>0,
~~~

so B is nonsingular.

Therefore the equilibrium equations have nonsingular Jacobian with respect to state variables. By the implicit-function theorem the positive equilibrium persists smoothly under sufficiently small parameter perturbations.

The strict-P inequalities and the strict fractional-only invariant inequalities also persist by continuity.

Hence the admissible set contains a nonempty open neighborhood in biological parameter space.

QED.

---

# 9. Double-Allee threshold parameter m as a genuine control of invariant space

The prey equation after eliminating Y,Z is

~~~text
g_DA(X;m)
=
chi X - nu
=: Q(X),
~~~

with chi,nu independent of m.

In the fractional-only construction

~~~text
e1 e3 > e2,
~~~

hence

~~~text
chi>0.
~~~

Assume

~~~text
Q>0,
s=-g_DA'(X)>0,
chi>0,
m>-a,
0<m<X<K.
~~~

The sign conclusions below use Q>0, s>0, chi>0 and m>-a; the additional ecological inequalities 0<m<X<K specify the coexistence branch under study.

The implicit equilibrium equation is

~~~text
F(X,m)
=
g_DA(X;m)-chi X+nu
=
0.
~~~

Since

~~~text
partial_X F
=
g_DA'(X)-chi
=
-(s+chi)
<0,
~~~

the coexistence branch is locally a smooth function X=X(m).

Moreover

~~~text
partial_m g_DA(X;m)
=
-g_DA(X;m)/(X-m)
=
-Q/(X-m).
~~~

Therefore

~~~text
dX/dm
=
-
Q
/
[
 (X-m)(s+chi)
]
<0.
~~~

So increasing the Allee threshold strictly lowers the coexistence prey density.

Now write

~~~text
s
=
Q H_A,
~~~

where

~~~text
H_A
=
1/(K-X)
-
1/(X-m)
+
1/(X+a)
>0.
~~~

Because m>-a and X>m,

~~~text
partial_X H_A
=
1/(K-X)^2
+
1/(X-m)^2
-
1/(X+a)^2
>0,
~~~

and

~~~text
partial_m H_A
=
-1/(X-m)^2
<0.
~~~

Thus

~~~text
ds/dm
=
chi (dX/dm) H_A
+
Q[
   (partial_X H_A)(dX/dm)
   -
   1/(X-m)^2
 ]
<0.
~~~

## Monotone invariant motion

Define

~~~text
A0 = e1 q1^2/c1 > 0,

B0 = e2 q2^2/c2 > 0,

C0 = 1 + e3 h^2/(c1 c2) > 1,

E0 = h q1 q2(e1 e3-e2)/(c1 c2) > 0,

t = 1/s.
~~~

Then

~~~text
beta12 = 1 + A0 t,

beta13 = 1 + B0 t,

beta23 = C0,

kappa
=
C0
+
(A0+B0+E0)t.
~~~

Since ds/dm<0,

~~~text
dt/dm>0.
~~~

Therefore increasing m strictly increases beta12, beta13 and kappa, while beta23 stays fixed.

This proves that the double-Allee threshold is not merely a passive parameter in an equilibrium formula: it moves the system monotonically along an explicit one-dimensional path in C-10 invariant space.

---

# 10. Exact classical crossing along the Allee path

Along the t-path above,

~~~text
G1(t)
:=
kappa(t)-T1(beta(t))
~~~

equals

~~~text
G1(t)
=
E0 t
-2
-2 sqrt[(1+A0 t)(1+B0 t)]
-2 sqrt(C0)
   [
    sqrt(1+A0 t)
    +
    sqrt(1+B0 t)
   ].
~~~

If

~~~text
E0 > 2 sqrt(A0 B0),
~~~

then

~~~text
G1(0)<0,
~~~

while

~~~text
G1(t) -> +infinity
~~~

as t->infinity.

Furthermore:

- sqrt(1+A0 t) is strictly concave;
- sqrt(1+B0 t) is strictly concave;
- sqrt[(1+A0t)(1+B0t)] is concave, with second derivative proportional to -(A0-B0)^2.

Therefore G1 is strictly convex.

Hence there exists a unique

~~~text
t_H>0
~~~

such that

~~~text
G1(t_H)=0.
~~~

The crossing is automatically transverse. Indeed convexity together with G1(0)=-4-4 sqrt(C0) gives

~~~text
G1'(t_H)
>=
[G1(t_H)-G1(0)]/t_H
=
(4+4 sqrt(C0))/t_H
>
0.
~~~

Thus:

~~~text
t<t_H   =>   classical Hurwitz D-stable,

t>t_H   =>   not Hurwitz D-stable.
~~~

Because t increases strictly with m, the Allee threshold crosses the classical D-stability boundary transversally whenever the coexistence branch reaches t_H.

---

# 11. Constructive m-induced transition theorem

For any prescribed

~~~text
t0>0
~~~

and positive A0,B0,C0, set

~~~text
E0
=
{
  2
  +2 sqrt[(1+A0 t0)(1+B0 t0)]
  +2 sqrt(C0)
     [
      sqrt(1+A0 t0)
      +
      sqrt(1+B0 t0)
     ]
}
/t0.
~~~

Then

~~~text
G1(t0)=0.
~~~

This E0 satisfies

~~~text
E0>2 sqrt(A0 B0).
~~~

The IGP realization theorem can realize this exact E0 by choosing the conversion-efficiency ratio e1e3/e2.

The double-Allee realization can independently set

~~~text
s0=1/t0
~~~

at any selected positive Allee threshold m0.

Therefore the model can be tuned so that

~~~text
m=m0
~~~

lies exactly on the classical Cain boundary.

Since

~~~text
dt/dm>0
~~~

and the root t0 is unique/transverse, for all sufficiently small epsilon>0,

~~~text
m0-epsilon < m < m0
    => Hurwitz D-stable,

m0 < m < m0+epsilon
    => not Hurwitz D-stable.
~~~

But at m=m0 and every alpha<1, the fractional threshold lies strictly beyond the classical threshold:
- for alpha>2/3, T_alpha(beta)>T1(beta);
- for alpha<=2/3, strict-P already implies fractional D-stability.

By continuity, after possibly shrinking epsilon,

~~~text
m0 < m < m0+epsilon
~~~

is **genuinely fractional D-stable**.

## Interpretation

Increasing the double-Allee threshold alone can move a biologically feasible coexistence equilibrium from

~~~text
classical robust stability
~~~

into

~~~text
fractional-only robust stability,
~~~

with all other model parameters fixed.

This is the strongest direct double-Allee mechanism currently established in the extension.

---

# 12. Two-dimensional consistency check

Return to the published two-species continuous fractional model

~~~text
^C D^alpha x
=
x[g_DA(x)-q y],

^C D^alpha y
=
y[p x-d].
~~~

At coexistence

~~~text
X=d/p,

Y=g_DA(X)/q.
~~~

The reduced matrix is

~~~text
B2 =
[ g_DA'(X)   -q
  p            0 ].
~~~

Its determinant is

~~~text
det B2=pq>0.
~~~

By the exact 2x2 theorem,

~~~text
B2 in F_alpha^(2)
iff
g_DA'(X)<=0.
~~~

Classical Hurwitz D-stability requires

~~~text
g_DA'(X)<0.
~~~

Therefore the genuinely fractional difference occurs only on

~~~text
g_DA'(X)=0.
~~~

This is a codimension-one condition. The critical threshold m_c below is biologically admissible only when it lies in the allowed positive range; in particular m_c>0 is equivalent to

~~~text
X^2+2aX>Ka.
~~~

For

~~~text
X=d/p,
~~~

the critical double-Allee threshold is obtained from

~~~text
1/(K-X)
-
1/(X-m)
+
1/(X+a)
=
0,
~~~

namely

~~~text
m_c
=
X
-
[(K-X)(X+a)]/(K+a)
=
[X^2+2aX-Ka]/(K+a).
~~~

Thus the two-dimensional double-Allee model supports only the exceptional lower-dimensional fractional-only mechanism, whereas the three-dimensional IGP extension supports a nonempty open fractional-only region.

---

# 13. Theorem-level research conclusion

The natural two-consumer extension is killed.

The intraguild-predation redesign passes all main early kill tests:

1. **tractable equilibrium:** yes; X satisfies an explicit quadratic and Y,Z are affine-rational in X;
2. **strict P on an open feasible set:** yes;
3. **full-dimensional invariant access:** yes; a constructive four-invariant realization theorem is available on beta_ij>1;
4. **fractional-only point:** yes for every 0<alpha<1;
5. **open parameter region:** yes by strict inequalities + IFT;
6. **double-Allee structural role:** yes; m strictly decreases the effective prey self-slope s and can be tuned to cross the classical D-stability boundary into the fractional-only band;
7. **novelty:** targeted search found no theorem-equivalent ecological result.

**Current recommendation: GO.**

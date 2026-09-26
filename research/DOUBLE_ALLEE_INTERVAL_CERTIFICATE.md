# Certified numerical example — double-Allee IGP extension

**Date:** 2026-09-26  
**Purpose:** independent certified check of one interior genuinely fractional point.  
**Script:** `computations/double_allee_igp_interval_certificate.py`

The theorem is analytic; this certificate is corroboration.

## Parameters

Fractional order:

~~~text
alpha = 0.9
~~~

Fixed biological parameters:

~~~text
a = 0.5
K = 1.1

c1 = c2 = 0.05

e1 = e3 = 0.5

tau = (14 + sqrt(200))/2
e2 = 0.25/tau^2

q1 = 0.05 sqrt(2)
h  = 0.05 sqrt(2)
q2 = 0.05/sqrt(e2)
~~~

The mortalities and r are constructed so that m0=0.2 gives X0=1 and

~~~text
s0=-g_DA'(X0)=0.05.
~~~

Numerically:

~~~text
q1 ≈ 0.0707106781186548
q2 ≈ 1.40710678118655
h  ≈ 0.0707106781186548

e2 ≈ 0.00126265847083665

mu1 ≈ 0.0333446506180512
mu2 ≈ 0.00300979112159422

r ≈ 0.109513274336283.
~~~

At m=0.2 the invariants are exactly

~~~text
(beta12,beta13,beta23,kappa)
=
(2,2,2,18),
~~~

so the point lies exactly on the classical Cain boundary

~~~text
T1=18.
~~~

For alpha=0.9,

~~~text
T_0.9(2,2,2)
≈39.5785720431,
~~~

so the classical boundary is strictly inside the fractional region.

## Interval-certified point at m=0.21

Using 50-decimal interval arithmetic:

~~~text
X
in
[0.9998522733376955410536215941332115912961665697003373562,
 0.9998522733376955410536215941332115912961665697004923765]

Y
in
[0.03749697536341635044122222412495900167165172239626621588,
 0.03749697536341635044122222412495900167165172239633370318]

Z
in
[0.001847199748987849771014925598613483520500200505023367087,
 0.001847199748987849771014925598613483520500200505070793]
~~~

Hence coexistence is rigorously positive.

The effective prey slope satisfies

~~~text
s
in
[0.04928213319865775301750159404257522401069524352054699681,
 0.04928213319865775301750159404257522401069524352073024824].
~~~

The invariant intervals are

~~~text
beta12,beta13
≈ 2.01456647175658,

beta23 = 2,

kappa
in
[18.2330635481052752108577388660944541759541510679473131,
 18.23306354810527521085773886609445417595415106800825214].
~~~

The classical threshold is

~~~text
T1
in
[18.08734597731129181770115333281022028269579114598773187,
 18.08734597731129181770115333281022028269579114601069626].
~~~

Therefore

~~~text
kappa-T1
>
0.14571757079398.
~~~

So the matrix is rigorously **not Hurwitz D-stable**.

## Independent all-D fractional certificate

C-11 gives the sufficient certificate

~~~text
Phi > rho_alpha,

Phi = T1/kappa,

rho_alpha
=
(1-2 cos(alpha*pi/2))^2.
~~~

Interval evaluation gives

~~~text
Phi
in
[0.9920080588536573206777460594605139051879635123097065075,
 0.992008058853657320677746059460513905187963512314283617]

rho_0.9
in
[0.4721491072487693797267000553725681439330031634058376372,
 0.4721491072487693797267000553725681439330031634058623602].
~~~

Hence

~~~text
Phi-rho_0.9
>
0.51985895160488.
~~~

Thus the point is interval-certified as **positive-diagonal Matignon stable for every positive diagonal multiplier**.

Combining the two strict certified inequalities:

~~~text
B in F_0.9^(3)
and
B notin D_H^(3).
~~~

By the Kolmogorov orbit lemma, the same classification holds for the actual ecological equilibrium Jacobian.

## Direct spectral corroboration

A separate floating-point optimization of the spectra of DB over diagonal ratios gives at m=0.21:

~~~text
max Re lambda(DB)
≈ +2.42137e-4,
~~~

providing a concrete classical-instability diagonal witness, while

~~~text
min |arg lambda(DB)|
≈ 1.5688343 rad

alpha*pi/2
≈ 1.4137167 rad,
~~~

leaving an angular margin of about

~~~text
0.15512 rad.
~~~

This direct spectral check is not used as proof.

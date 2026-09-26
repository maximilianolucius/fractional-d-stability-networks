# Chief Researcher report — Double-Allee 3D Kolmogorov extension

**Date:** 2026-09-26  
**Branch:** chief/double-allee-kolmogorov-20260926  
**Decision:** **GO, WITH MODEL REDESIGN**  
**Scientific center:** exact ecological realization of the positive-diagonal Matignon threshold, not another stability/bifurcation study.

This report answers the requested investigation in the prescribed order.

---

# 1. Novelty audit

Detailed audit:
- research/novelty/DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT.md

Main findings:

1. The positive-equilibrium factorization of a Kolmogorov system is standard:
   J(x*)=diag(x*) DF(x*).
2. Double-Allee predator–prey systems are already well studied, including 2026 fractional/discrete work.
3. Intraguild predation / omnivory is a standard three-species ecological module.
4. No located paper combines:
   - a non-GLV double-Allee Kolmogorov system;
   - exact positive-diagonal Matignon orbit invariants;
   - the C-10 necessary-and-sufficient all-D threshold;
   - an analytic open biological fractional-only region;
   - an Allee-threshold parameter crossing that boundary.
5. The initially proposed two-consumer competition architecture is mathematically incapable of realizing the required open fractional-only band.
6. The redesigned IGP/omnivory architecture can realize a full four-dimensional invariant family and, in particular, every target point needed for the C-10 fractional-only band with beta_ij>1.

The novelty should therefore be claimed only for the **exact ecological realization/open-region/transversality theorem chain**.

---

# 2. Candidate model and biological justification

The initial shared-prey/two-competing-consumer model is rejected by an analytic no-go theorem.

Use instead the standard intraguild-predation architecture:

~~~text
^C D^alpha x
=
x[
  r/(x+a)(1-x/K)(x-m)
  -q1 y
  -q2 z
],

^C D^alpha y
=
y[
  e1 q1 x
  -mu1
  -c1 y
  -h z
],

^C D^alpha z
=
z[
  e2 q2 x
  +e3 h y
  -mu2
  -c2 z
].
~~~

Biological interpretation:
- x is the basal prey/resource;
- y is the intermediate consumer / IG prey;
- z is the omnivorous top predator / IG predator;
- z consumes both x and y;
- the prey experiences the same double-Allee law used in the published 2026 fractional model;
- c1,c2 are self-limitation terms and are ecologically standard stabilizing density dependence.

This sign pattern is established IGP ecology. The mathematical reason for choosing it is not convenience alone: it is the simplest standard food-web motif that creates two opposing directed three-cycles.

The normalized total three-cycle coordinate is

~~~text
L3
=
h q1 q2(e2-e1 e3)/(s c1 c2).
~~~

Thus e1e3>e2 produces L3<0, which is precisely what can lift kappa above the classical Cain surface.

---

# 3. Exact coexistence equilibrium and feasibility domain

Let the positive equilibrium be (X,Y,Z).

Define

~~~text
Delta = c1 c2 + e3 h^2 >0,

A1(X)=e1 q1 X-mu1,

A2(X)=e2 q2 X-mu2.
~~~

Then

~~~text
Y(X)
=
[c2 A1(X)-h A2(X)]/Delta,

Z(X)
=
[e3 h A1(X)+c1 A2(X)]/Delta.
~~~

Hence necessary and sufficient coexistence feasibility for a candidate X is

~~~text
X>0,
Y(X)>0,
Z(X)>0,
g_DA(X)=q1Y(X)+q2Z(X)>0.
~~~

The combined predation term is affine:

~~~text
q1Y+q2Z
=
chi X-nu,
~~~

where

~~~text
chi
=
[
 e1 c2 q1^2
 +e2 c1 q2^2
 +h q1 q2(e1e3-e2)
]/Delta,
~~~

and

~~~text
nu
=
[
 mu1(q1c2+q2e3h)
 +mu2(q2c1-q1h)
]/Delta.
~~~

Therefore X solves the explicit quadratic

~~~text
(r+K chi) X^2
-
[r(K+m)-K chi a+K nu] X
+
rKm-Knu a
=
0.
~~~

This is substantially better than expected: the non-GLV coexistence geometry remains exactly tractable.

---

# 4. Exact Jacobian factorization

For a general Kolmogorov system

~~~text
^C D^alpha x_i=x_i F_i(x),
~~~

at a positive equilibrium x*:

~~~text
J(x*)=diag(x*) DF(x*).
~~~

For the selected IGP model define

~~~text
B:=DF(X,Y,Z).
~~~

Then

~~~text
J=diag(X,Y,Z) B.
~~~

For every positive diagonal D,

~~~text
D J
=
[D diag(X,Y,Z)] B.
~~~

Since D diag(X,Y,Z) ranges over all positive diagonal matrices as D does,

~~~text
J in F_alpha^(3)
iff
B in F_alpha^(3),
~~~

and

~~~text
J in D_H^(3)
iff
B in D_H^(3).
~~~

This is an exact orbit equivalence.

---

# 5. Novelty status of orbit equivalence

Do not claim it as new.

The factorization itself is standard in Kolmogorov linearization, and classical diagonal-stability work already extends GLV stability reasoning to general Kolmogorov systems.

Its role here is to justify importing the exact C-10 invariant theorem from the reduced matrix B to the actual ecological Jacobian J.

---

# 6. Closed-form beta_ij and kappa

Let

~~~text
s=-g_DA'(X)>0.
~~~

Then

~~~text
B =
[ -s      -q1      -q2
  e1q1    -c1      -h
  e2q2     e3h     -c2 ].
~~~

The invariants are

~~~text
beta12
=
1+e1q1^2/(s c1),

beta13
=
1+e2q2^2/(s c2),

beta23
=
1+e3h^2/(c1c2),
~~~

and

~~~text
kappa
=
beta12+beta13+beta23-2
+
h q1 q2(e1e3-e2)/(s c1c2).
~~~

Equivalently,

~~~text
L3
=
h q1 q2(e2-e1e3)/(s c1c2),

kappa
=
beta12+beta13+beta23-2-L3.
~~~

This is a clean biological interpretation:
- beta12 and beta13 are the two basal-prey/consumer reciprocal loops;
- beta23 is the intraguild predator–IG prey reciprocal loop;
- L3 measures competition between the two oriented three-step energy-feedback routes.

---

# 7. Strict-P conditions

The signed order-one minors are

~~~text
p1=s,
p2=c1,
p3=c2.
~~~

The order-two minors are automatically positive once s>0:

~~~text
m12=s c1+e1q1^2>0,

m13=s c2+e2q2^2>0,

m23=c1c2+e3h^2>0.
~~~

Also

~~~text
-det B
=
s(c1c2+e3h^2)
+c1e2q2^2
+c2e1q1^2
+hq1q2(e1e3-e2).
~~~

Hence a sufficient transparent strict-P regime is

~~~text
s>0,
e1e3>e2.
~~~

In the constructed fractional-only band, -det B is in fact automatically positive because

~~~text
-det B
=
kappa s c1c2
>0.
~~~

---

# 8. Search for a fractional-only point

The search succeeds analytically, not merely numerically.

## Invariant realization theorem

For any target

~~~text
beta12>1,
beta13>1,
beta23>1,
~~~

and any

~~~text
kappa
>
beta12+beta13+beta23-2,
~~~

the IGP matrix architecture realizes those four invariants exactly.

For a genuinely fractional point choose:

### If 2/3<alpha<1

~~~text
T1(beta)
<
kappa
<
T_alpha(beta).
~~~

### If 0<alpha<=2/3

choose

~~~text
kappa>T1(beta).
~~~

The constructive formulas are given in
research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md.

Therefore a fractional-only invariant point exists for **every** 0<alpha<1.

---

# 9. Analytic proof of a nonempty open biological region

This also succeeds.

After realizing the desired matrix invariants, choose

~~~text
a>0,
0<m<X<K
~~~

with

~~~text
H_A
=
1/(K-X)-1/(X-m)+1/(X+a)
>0.
~~~

Set

~~~text
Q=s/H_A.
~~~

Choose positive Y,Z satisfying

~~~text
q1Y+q2Z=Q.
~~~

For K sufficiently close to X, Q can be made arbitrarily small. Therefore the mortalities

~~~text
mu1=e1q1X-c1Y-hZ,

mu2=e2q2X+e3hY-c2Z
~~~

are positive.

Then set

~~~text
r
=
Q(X+a)/[(1-X/K)(X-m)].
~~~

This gives exactly

~~~text
g_DA(X)=Q,
g_DA'(X)=-s.
~~~

Hence the biologically feasible equilibrium realizes the target invariant point.

All inequalities are strict and

~~~text
det B !=0.
~~~

The implicit-function theorem therefore continues the coexistence equilibrium under small parameter perturbations, while positivity, strict-P and the C-10 strict threshold inequalities persist.

## Result

For every 0<alpha<1 there is a **nonempty open set** of positive double-Allee IGP parameters whose coexistence equilibrium is fractionally D-stable under every positive diagonal multiplier but not Hurwitz D-stable.

This is the main GO theorem.

---

# 10. Sensitivity / threshold result for the double-Allee parameter m

This also succeeds in a rigorous local form.

Along a positive equilibrium branch,

~~~text
g_DA(X;m)=chi X-nu=:Q>0.
~~~

In the target architecture e1e3>e2, hence chi>0.

With

~~~text
s=-g_DA'(X)>0,
~~~

implicit differentiation gives

~~~text
dX/dm
=
-
Q/[(X-m)(s+chi)]
<0.
~~~

Thus increasing the Allee threshold decreases the coexistence prey density.

Moreover

~~~text
s
=
Q[
  1/(K-X)
  -1/(X-m)
  +1/(X+a)
].
~~~

For m>-a and X>m,

~~~text
ds/dm<0.
~~~

Therefore

~~~text
t:=1/s
~~~

is strictly increasing with m.

The invariant path is explicitly

~~~text
beta12=1+A0 t,

beta13=1+B0 t,

beta23=C0,

kappa=C0+(A0+B0+E0)t,
~~~

with positive constants A0,B0,C0 and, when e1e3>e2, E0>0.

The classical gap is

~~~text
G1(t)
=
kappa-T1(beta)
=
E0 t
-2
-2 sqrt[(1+A0t)(1+B0t)]
-2 sqrt(C0)
  [
    sqrt(1+A0t)
    +
    sqrt(1+B0t)
  ].
~~~

If

~~~text
E0>2 sqrt(A0B0),
~~~

then G1 is strictly convex, begins negative, tends to +infinity, and therefore has exactly one positive zero t_H.

Thus increasing m drives the system through the classical D-stability boundary exactly once whenever the coexistence branch spans t_H.

Even more strongly, the parameter construction can force any chosen m0 to satisfy t(m0)=t_H. Since T_alpha>T1 for alpha<1, continuity gives

~~~text
m<m0  : classically D-stable  (locally),

m>m0  : genuinely fractional D-stable (locally),
~~~

with every other model parameter held fixed.

This is the requested structural role for the double-Allee threshold.

I do **not** currently claim a universal second threshold m2 leading to fractional instability; that depends on the global continuation range and trophic parameter strengths. The local classical-to-fractional-only crossing is rigorous and sufficient for the new theorem.

---

# 11. Certified / independent numerical checks

A reproducible script is committed at

~~~text
computations/double_allee_igp_validation.py
~~~

The validation deliberately constructs a case where

~~~text
alpha=0.9,
m0=0.2
~~~

is exactly the classical Cain boundary.

Biological parameters:

~~~text
a = 0.5
K = 1.1
r = 0.109513274336283

c1=c2=0.05

q1 = 0.0707106781186548
q2 = 1.40710678118655
h  = 0.0707106781186548

e1=e3=0.5
e2=0.00126265847083665

mu1 = 0.0333446506180512
mu2 = 0.00300979112159422
~~~

At m=0.20:

~~~text
(X,Y,Z)
=
(1,
 0.0375454928063654,
 0.0018867560672250)

s=0.05

(beta12,beta13,beta23,kappa)
=
(2,2,2,18)

T1=18

T_0.9
≈39.5785720433.
~~~

The reduced matrix at this exact boundary has an imaginary conjugate pair at D=I, so it is on the classical D-stability boundary while remaining comfortably inside the alpha=0.9 Matignon sector.

With **all parameters fixed except m**:

### m=0.19

~~~text
s ≈ 0.0507175545969
kappa ≈ 17.7736311689
T1 ≈ 17.9150614687
T_0.9 ≈ 39.4102432080
~~~

so it is classically D-stable.

### m=0.21

~~~text
(X,Y,Z)
≈
(0.999852273338,
 0.0374969753634,
 0.00184719974899)

s ≈ 0.0492821331987

kappa ≈ 18.2330635481
T1 ≈ 18.0873459773
T_0.9 ≈ 39.7517450794
~~~

so

~~~text
T1 < kappa < T_0.9.
~~~

An independent direct optimization over positive diagonal multipliers finds:
- a positive classical spectral-abscissa witness approximately +2.42e-4;
- minimum eigenvalue angle approximately 1.56883 rad;
- Matignon boundary theta=0.9*pi/2≈1.41372 rad;
- angular margin ≈0.15512 rad.

Thus the all-D threshold formulas and the direct spectral calculation agree.

The numerical check is corroboration only; the open-region theorem is analytic.

---

# 12. Two-dimensional reduction

For the published continuous two-species model

~~~text
^C D^alpha x=x[g_DA(x)-q y],

^C D^alpha y=y[p x-d],
~~~

the coexistence prey density is

~~~text
X=d/p.
~~~

The reduced matrix is

~~~text
B2=
[ g_DA'(X)  -q
  p            0 ].
~~~

Because det B2=pq>0, the exact 2x2 theorem gives

~~~text
B2 in F_alpha^(2)
iff
g_DA'(X)<=0,
~~~

whereas classical D-stability requires

~~~text
g_DA'(X)<0.
~~~

Therefore genuinely fractional D-stability occurs only on

~~~text
g_DA'(X)=0,
~~~

a codimension-one surface.

The corresponding exact Allee threshold is

~~~text
m_c
=
X
-
[(K-X)(X+a)]/(K+a)

=
[X^2+2aX-Ka]/(K+a).
~~~

This provides the intended conceptual contrast:

~~~text
2D double Allee:
fractional-only D-stability is exceptional / codimension one.

3D double-Allee IGP:
fractional-only D-stability occupies a nonempty open parameter set.
~~~

---

# 13. GO / MODIFY / KILL assessment

## Original model

**KILL.**

The shared-prey / two-competing-consumer architecture cannot reach the fractional-only band on the strict-P stratum.

## Research direction after redesign

**GO.**

The IGP/omnivory redesign passes all seven early kill tests.

### Why GO

1. Exact coexistence geometry is tractable.
2. Strict-P conditions are transparent.
3. The invariant map is genuinely four-dimensional.
4. A fractional-only point exists analytically for every alpha<1.
5. The biological parameter set is open, not isolated.
6. The double-Allee threshold m has a provable monotone effect on the effective self-slope and can cross the classical boundary into the fractional-only band.
7. The theorem combination survived the current novelty search.

---

# 14. Proposed theorem structure for a new paper

### Lemma 1 — Kolmogorov orbit equivalence
Standard foundation; no novelty claim.

### Proposition 2 — competitive two-consumer no-go
Shows why the naive 3D extension cannot realize robust fractional-only D-stability.

### Theorem 3 — exact IGP invariant coordinates
Closed-form beta_ij, kappa and signed-cycle decomposition.

### Theorem 4 — ecological invariant realization
Every target beta_ij>1 and sufficiently large kappa is realizable by positive IGP parameters; fractional-band points admit efficiencies in (0,1).

### Theorem 5 — double-Allee coexistence realization
Any such reduced matrix can be embedded at a feasible positive equilibrium with the published double-Allee prey law.

### Theorem 6 — open genuinely fractional region
For every 0<alpha<1 there is a nonempty open biological parameter set satisfying positive-diagonal Matignon stability but not Hurwitz D-stability.

### Theorem 7 — Allee-threshold transversality
Increasing m decreases s=-g'(X), increases t=1/s, and can be tuned to cross the classical D-stability boundary into the fractional-only region with all other parameters fixed.

### Corollary 8 — 2D/3D contrast
The published two-species double-Allee model has only a codimension-one fractional-only D-stability surface.

---

# 15. Proposed title

Primary recommendation:

**From Fragile to Robust Fractional Stability: Double-Allee Intraguild Predation Across the Positive-Diagonal Matignon Boundary**

More matrix-theoretic:

**Exact Positive-Diagonal Matignon Stability in a Double-Allee Kolmogorov Food Web**

More ecological:

**Double Allee Effects and Robust Fractional-Only Stability in a Three-Species Intraguild-Predation System**

The first is the strongest narrative title if the proof audit confirms the theorem chain.

---

# 16. Abstract skeleton

1. Positive equilibria of general Kolmogorov systems inherit a positive-diagonal orbit from their per-capita derivative matrix.
2. A natural two-consumer double-Allee extension is proved incapable of robust fractional-only D-stability.
3. Replacing consumer competition by a standard intraguild-predation/omnivory motif changes the signed three-cycle coordinate.
4. Exact invariant formulas are derived and a realization theorem maps an open biological parameter family into the C-10 invariant space.
5. For every fractional order 0<alpha<1, a nonempty open set of feasible coexistence equilibria is positive-diagonal Matignon stable but not Hurwitz D-stable.
6. The double-Allee threshold m is shown to decrease the effective prey self-slope and can transversally move the system from classical robust stability into the fractional-only band.
7. The corresponding two-species model exhibits only a codimension-one fractional-only mechanism.

---

# 17. Candidate journals

Final venue should be selected only after independent proof audit and after checking current journal metrics at submission.

Current candidate ordering by scientific fit:

1. **Mathematical Biosciences** — best biological/mathematical fit if ecological realization is emphasized.
2. **Nonlinear Analysis: Real World Applications** — attractive if the paper is theorem-first and the analysis is the dominant contribution.
3. **Chaos, Solitons & Fractals** — strong fractional/nonlinear-dynamics audience; current sources list it as Q1 in multiple mathematics/physics categories.
4. **Journal of Mathematical Biology** — potentially appropriate if the ecological interpretation and theorem depth are both strengthened.

The paper should not be sent as a routine fractional predator–prey dynamics paper.

---

# 18. Remaining gates before manuscript drafting

1. independent proof audit of the new theorem package;
2. symbolic algebra verification of every invariant identity;
3. reproduce the m-crossing example from a clean clone;
4. interval/high-precision certification of at least one interior fractional-only parameter box;
5. a second independent novelty audit focused on:
   - IGP D-stability,
   - Kolmogorov D-stability,
   - exact ecological realization theorems,
   - Allee-threshold robust-stability crossings;
6. decide whether the extension should be:
   - a new standalone paper, or
   - a major second half of the existing C-10 manuscript.

## Chief recommendation

**Do not merge this into manuscript prose yet.**

The mathematics is sufficiently promising to justify the next proof-audit/computation wave, and materially stronger than simply appending another ecological example to the existing paper.

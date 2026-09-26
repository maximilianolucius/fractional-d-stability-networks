# Novelty audit — Double-Allee 3D Kolmogorov / intraguild-predation extension

**Date:** 2026-09-26  
**Branch:** chief/double-allee-kolmogorov-20260926  
**Role:** Chief Researcher — theorem discovery / adversarial novelty audit  
**Status:** GO, but with a redesigned ecological architecture

## 1. Novelty question

The target is not a new Allee predator–prey model. The target is an exact ecological realization of the already-developed positive-diagonal Matignon theory:

~~~text
T_1(beta) < kappa < T_alpha(beta)
~~~

at a biologically feasible positive equilibrium of a genuinely non-GLV three-dimensional Kolmogorov system, together with an open-parameter theorem and a rigorous mechanism by which a double-Allee parameter moves the system across the classical/fractional robust-stability boundary.

## 2. General Kolmogorov factorization is NOT novel

For

~~~text
D^alpha x_i = x_i F_i(x)
~~~

and a positive equilibrium x* with F(x*)=0, direct differentiation gives

~~~text
J(x*) = diag(x*) DF(x*).
~~~

This factorization is standard in Kolmogorov-system linearization. It appears explicitly, for example, in work on tridiagonal predator–prey Kolmogorov systems, where the linearized matrix is written as D(x*) J_f(x*).

Hou & Baigent (2015) extend diagonal-stability/Lyapunov ideas from Lotka–Volterra to general autonomous Kolmogorov systems. The 2024 Physics Reports review likewise states that diagonal-stability methods extend beyond GLV to Kolmogorov systems.

**Decision:** the factorization and the positive-equilibrium local linearization are foundations/lemmas, not novelty.

Relevant sources:
- Z. Hou and S. Baigent, *Global stability and repulsion in autonomous Kolmogorov systems*, Commun. Pure Appl. Anal. 14 (2015), 1205–1238, DOI 10.3934/cpaa.2015.14.1205.
- C. Chen, X.-W. Wang, Y.-Y. Liu, *Stability of ecological systems: A theoretical review*, Physics Reports 1088 (2024), 1–41, DOI 10.1016/j.physrep.2024.08.001.

What does appear useful, but is elementary, is the exact orbit corollary:

~~~text
J(x*) in F_alpha  iff  DF(x*) in F_alpha,
J(x*) in D_H      iff  DF(x*) in D_H,
~~~

because D diag(x*) ranges bijectively over all positive diagonal matrices.

## 3. Double-Allee models are heavily occupied

The double-Allee law

~~~text
g_DA(x) = r/(x+a) * (1-x/K) * (x-m)
~~~

and equivalent forms are established in the ecological literature.

A 2026 Fractal and Fractional paper studies the Caputo system

~~~text
D^alpha x = x[g_DA(x)-q y],
D^alpha y = y[p x-d],
~~~

and then a discrete fractional approximation, local stability, bifurcations, chaos and feedback control.

A 2026 AIMS Mathematics article and earlier papers study closely related double-Allee predator–prey forms, including the two low-density mechanisms x-m and x/(x+l) or 1/(x+a).

**Decision:** no novelty claim for the double-Allee functional form, fractional predator–prey modeling, equilibrium calculation, Matignon local stability, bifurcation, chaos or control.

Relevant sources:
- *Bifurcation Structure and Chaos Control in a Discrete-Time Fractional Predator–Prey Model with Double Allee Effect*, Fractal Fract. 10 (2026), 304, DOI 10.3390/fractalfract10050304.
- A. Tassaddiq et al., *Impact of double Allee effect on the dynamics and stability of a predator-prey model*, AIMS Mathematics 11 (2026), 1117–1144, DOI 10.3934/math.2026048.
- Earlier double-Allee predator–prey analyses include Chaos, Solitons & Fractals 73 (2015), 36–63, DOI 10.1016/j.chaos.2014.12.007.

## 4. Three-species IGP/omnivory is established ecology

Intraguild predation (IGP) / omnivory is a standard three-species module:
- a basal resource/prey x;
- an intermediate consumer y feeding on x;
- a top predator z feeding on both x and y.

The sign architecture used in the proposed extension is therefore biologically standard, not invented for algebraic convenience.

Representative sources:
- Holt–Polis IGP tradition, summarized in later IGP work.
- R. Liu and G. Liu, *Dynamics of a stochastic three species prey-predator model with intraguild predation*, J. Appl. Anal. Comput. 10 (2020), 81–103, DOI 10.11948/jaac20190002.
- D. Bai, Y. Kang, S. Ruan, L. Wang, *Dynamics of an intraguild predation food web model with strong Allee effect in the basal prey*, Nonlinear Analysis: Real World Applications 58 (2021), 103206, DOI 10.1016/j.nonrwa.2020.103206.

**Decision:** no novelty claim for the IGP module itself, IGP + Allee effect, or three-species local-stability analysis.

## 5. Critical negative result: the initially proposed two-consumer competition model is structurally incapable of the target

For the natural candidate

~~~text
x' = x[g_DA(x)-q1 y-q2 z]
y' = y[e1 q1 x-mu1-c11 y-c12 z]
z' = z[e2 q2 x-mu2-c21 y-c22 z],
~~~

with all competition coefficients positive, the reduced equilibrium matrix on the strict-P stratum is

~~~text
B =
[ -s      -q1       -q2
  e1 q1   -c11      -c12
  e2 q2   -c21      -c22 ],
s=-g_DA'(x*)>0.
~~~

Its exact orbit invariants satisfy

~~~text
beta12 = 1 + e1 q1^2/(s c11),
beta13 = 1 + e2 q2^2/(s c22),
beta23 = 1 - c12 c21/(c11 c22),
~~~

and the normalized directed three-cycle sum is strictly positive:

~~~text
L3 = q1 q2 (c12 e2 + c21 e1)/(s c11 c22) > 0.
~~~

Hence

~~~text
kappa
 = beta12+beta13+beta23-2-L3
 < beta12+beta13+beta23-2
 < T1(beta),
~~~

because

~~~text
T1(beta)
 = (sqrt(beta12)+sqrt(beta13)+sqrt(beta23))^2
 > beta12+beta13+beta23.
~~~

Therefore every full-dimensional strict-P point of this architecture is already classically Hurwitz D-stable.

**Conclusion:** the initial two-consumer competitive architecture FAILS the core early kill test. It cannot realize an open genuinely fractional-only D-stable region.

This negative theorem is useful because it identifies the missing ecological mechanism: a signed three-cycle capable of making the normalized cycle coordinate sufficiently negative.

## 6. Redesigned architecture: double-Allee intraguild predation

Use

~~~text
D^alpha x = x[ g_DA(x) - q1 y - q2 z ]

D^alpha y = y[ e1 q1 x - mu1 - c1 y - h z ]

D^alpha z = z[ e2 q2 x + e3 h y - mu2 - c2 z ],
~~~

with every displayed biological parameter positive and

~~~text
g_DA(x)
 = r/(x+a) (1-x/K)(x-m).
~~~

Interpretation:
- x = basal prey/resource with double Allee effect;
- y = intermediate consumer / IG prey;
- z = omnivorous top predator / IG predator;
- z consumes both x and y;
- c1,c2 provide intraspecific density dependence.

At a positive equilibrium, with s=-g_DA'(x*)>0,

~~~text
B = DF(x*) =
[ -s      -q1      -q2
  e1 q1   -c1      -h
  e2 q2    e3 h    -c2 ].
~~~

The two directed three-cycle products have opposite signs:

~~~text
a12 a23 a31 = + e2 q1 q2 h,
a13 a32 a21 = - e1 e3 q1 q2 h.
~~~

Thus

~~~text
L3 = h q1 q2 (e2-e1 e3)/(s c1 c2).
~~~

When

~~~text
e1 e3 > e2,
~~~

the total normalized three-cycle coordinate is negative. This is exactly the sign mechanism missing from the failed two-consumer architecture.

## 7. Prior-art search for the actual target theorem

Targeted searches were performed for combinations of:
- Kolmogorov + D-stability;
- fractional/Matignon + Kolmogorov;
- positive diagonal scaling + predator–prey;
- D-stability + intraguild predation;
- D-stability + omnivory;
- double Allee + D-stability;
- fractional D-stability + ecology.

Located literature separates into:
1. classical D-/diagonal-stability in ecology;
2. general Kolmogorov Lyapunov/diagonal-stability theory;
3. fractional ecological models using ordinary Matignon stability at one Jacobian;
4. IGP/omnivory and Allee-effect dynamics;
5. the matrix-theory generalized-D-stability literature already audited in C-10.

No located paper gives the theorem combination proposed here:

~~~text
double-Allee non-GLV Kolmogorov equilibrium
+ exact positive-diagonal Matignon orbit invariants
+ exact C-10 all-D threshold
+ analytic realization of a nonempty open biologically feasible
  fractional-only D-stable parameter region
+ a double-Allee parameter transversally crossing the classical boundary.
~~~

## 8. Defensible novelty boundary

Do NOT claim novelty for:
- Kolmogorov factorization;
- IGP/omnivory;
- double Allee effects;
- fractional ecological systems;
- ordinary Matignon stability;
- D-stability or diagonal stability;
- equilibrium/bifurcation calculations.

The strongest candidate novelty is:

> an exact ecological realization theorem showing that a biologically standard double-Allee intraguild-predation Kolmogorov system can realize an open subset of the genuinely fractional positive-diagonal Matignon-stable invariant band, together with an explicit signed-cycle mechanism and a rigorous Allee-threshold transversality result.

A second, useful structural result is the no-go theorem proving that the superficially simpler two-consumer competitive extension cannot realize the target open band.

## 9. Novelty verdict

**GO — NEW THEOREM VECTOR SURVIVES THE CURRENT SEARCH.**

The novelty is conditional on keeping the paper theorem-first:
- exact no-go for the naive architecture;
- exact invariant realization for the IGP architecture;
- open biological fractional-only region;
- rigorous m-induced crossing.

A simulation-first “3D double-Allee fractional food web” paper would NOT be novel enough.

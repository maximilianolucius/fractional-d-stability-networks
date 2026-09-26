# Final novelty addendum — Double-Allee IGP theorem after Audit 1

**Date:** 2026-09-26  
**Chief branch:** `chief/double-allee-kolmogorov-20260926`  
**Purpose:** update novelty boundary after the first independent proof/compute audit sharpened the exact theorem statement.

## 1. New direct prior art that must be cited

### Panja 2019 — fractional intraguild predation already exists

Prabir Panja, *Dynamics of a fractional order predator-prey model with intraguild predation*, International Journal of Modelling and Simulation 39(4) (2019), 256–268, DOI 10.1080/02286203.2019.1611311.

The paper explicitly uses a three-species intraguild-predation architecture in which:
- the intermediate predator consumes the basal prey;
- the intraguild predator consumes both the basal prey and the intermediate predator;
- intraspecific competition is included;
- fractional-order dynamics, equilibria, stability and simulations are studied.

Therefore the project must **not** claim novelty for:
- a fractional-order IGP food web;
- a three-species Caputo IGP system;
- local stability of IGP equilibria;
- the qualitative idea that memory/fractional order can stabilize an IGP system.

### 2026 fractional IGP work

A 2026 paper, *Periodic structures and memory–fear interactions in a fractional order intraguild predation model* (International Journal of Modelling and Simulation, DOI 10.1080/02286203.2026.2703016), studies a Caputo fractional IGP model with a basal prey and an IG predator consuming both prey levels, with local stability, Hopf bifurcation and extensive nonlinear-dynamics simulations.

Thus fractional IGP is not only historical prior art; it remains an active current literature area.

### Double-Allee fractional ecology is also occupied

The 2026 Fractal and Fractional paper *Bifurcation Structure and Chaos Control in a Discrete-Time Fractional Predator–Prey Model with Double Allee Effect* directly uses

~~~text
g_DA(x)
=
r/(x+a) (1-x/K)(x-m)
~~~

inside a fractional predator–prey model and studies equilibrium stability, bifurcations, chaos and control.

Additional 2021–2026 fractional double-Allee predator–prey papers further confirm that neither the double-Allee law nor fractional-memory ecology is new.

## 2. Exact surviving novelty claim after the stronger search

The project novelty is **not**:

~~~text
fractional IGP
+ double Allee effect
+ coexistence stability.
~~~

The surviving candidate theorem is much narrower:

> For a biologically standard non-GLV double-Allee IGP Kolmogorov system, derive the exact positive-diagonal Matignon orbit invariants at coexistence; prove a structural no-go theorem for the natural competitive two-consumer alternative; prove a constructive four-invariant realization theorem; embed an open subset of the genuinely fractional C-10 band in the full biological parameter space; and prove that varying the Allee threshold alone can cross the exact classical Cain boundary into the fractional-only robust region.

No located IGP/Allee/fractional ecology paper imposes the quantifier

~~~text
sigma(DJ(x*)) subset Sigma_alpha
for every positive diagonal D,
~~~

nor derives an exact threshold equivalent to C-10, nor proves a full-dimensional open biological realization of the fractional-only positive-diagonal class.

## 3. Why ordinary local-stability literature does not subsume the theorem

Panja 2019 and the 2026 fractional IGP paper analyze a fixed Jacobian / fixed parameter set at an equilibrium. Their local stability condition asks whether the eigenvalues of that single Jacobian satisfy the fractional stability condition.

The present theorem asks whether **every positive diagonal row scaling** of the equilibrium Jacobian satisfies Matignon stability:

~~~text
for all D>0 diagonal.
~~~

This is a strictly different robustness quantifier.

Moreover, the project proves the separation

~~~text
J in F_alpha
but
J not in D_H,
~~~

and certifies an open parameter set realizing that difference.

The located ecological papers do not formulate that matrix-orbit problem.

## 4. Updated priority wording

Approved:

> “We give an exact ecological realization of the genuinely fractional positive-diagonal Matignon-stable class in a non-GLV double-Allee intraguild-predation Kolmogorov system.”

Approved:

> “The double-Allee threshold can be tuned to move a fixed ecological model transversally across the exact classical D-stability boundary into a fractional-only positive-diagonal stable region.”

Avoid:

> “We introduce a fractional intraguild-predation model.”

Avoid:

> “We introduce a double-Allee fractional predator–prey model.”

Avoid:

> “We are the first to show memory-induced stabilization in intraguild predation.”

All three are contradicted or strongly occupied by prior literature.

## 5. Novelty status

After this additional targeted search:

~~~text
MODEL NOVELTY:        NO
FRACTIONAL IGP:       KNOWN
DOUBLE-ALLEE FDE:     KNOWN
LOCAL STABILITY:      KNOWN
ALL-D ORBIT THEOREM:  SURVIVES SEARCH
OPEN BIOLOGICAL BAND: SURVIVES SEARCH
m-CROSSING THEOREM:   SURVIVES SEARCH
~~~

**Chief novelty verdict:** `GO-NARROWED`.

The strongest claim remains theorem-level, not model-level.

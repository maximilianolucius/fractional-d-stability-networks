# Chief review — Audit 2 / Double-Allee theorem package

**Date:** 2026-09-26  
**Chief integration branch:** `chief/double-allee-final-integration-20260926`  
**Audit 2 branch:** `agent/independent-proof-double-allee-20260926`  
**Audit 2 final SHA:** `fb970648ff8dcb586fe5733c52717bf2c4d9d20f`  
**Audit 2 status:** `PROOF_AUDIT2_PASS_WITH_FIXES`

## Chief verdict

**MATHEMATICAL PACKAGE SURVIVES AUDIT 2, BUT AUDIT 2 DOES NOT SATISFY THE EPISTEMIC-INDEPENDENCE GATE.**

Reason: the auditor explicitly disclosed that it was the same agent/session that produced Audit 1. The Phase A protocol was procedurally blind, and the second audit used new code, a new witness, a different verification route and did not read Audit 1 artifacts before freezing its blind verdicts. That makes it a strong replication and a useful adversarial rerun, but not a genuinely independent external proof audit.

Accordingly:

~~~text
Audit 1: strong independent-compute lane relative to Chief derivation
Audit 2: procedurally blind replication, same-session
True external proof audit: still required
~~~

No theorem is downgraded because Audit 2 found no counterexample and added several exact identities; however the manuscript remains locked from "submission-certified" language.

---

## Verdict reconciliation

Audit 2 returned the same item-level decisions as Audit 1:

| Item | Audit 2 | Chief disposition |
|---|---|---|
| DA-01 | PASS | ACCEPT |
| DA-02 | PASS | ACCEPT |
| DA-03 | PASS | ACCEPT |
| DA-04 | PASS, sharpened | ACCEPT |
| DA-05 | PASS | ACCEPT |
| DA-06 | PASS | ACCEPT |
| DA-07 | PASS, quantified | ACCEPT |
| DA-08 | PASS WITH MINOR FIX | ACCEPT; wording already corrected |
| DA-09 | PASS, sharpened | ACCEPT |
| DA-10 | PASS | ACCEPT |
| DA-11 | PASS | ACCEPT |
| DA-12 | PASS | ACCEPT |

There are no verdict disagreements between Audit 1 and Audit 2.

---

## New exact result accepted: Schur identity

Audit 2 found the identity

~~~text
q = -det B = Delta (s+chi),

Delta = c1 c2 + e3 h^2.
~~~

This is exact.

Consequences:

1. once s>0, the order-one and order-two strict-P conditions are automatic;
2. full strict-P is exactly

~~~text
s+chi>0;
~~~

3. the scalar coexistence equation has derivative

~~~text
Phi_X
=
g_DA'(X)-chi
=
-(s+chi)
=
-q/Delta;
~~~

4. therefore the nondegeneracy condition used by the reduced scalar IFT and by the full coexistence IFT is the same determinant condition;
5. a fold of the scalar coexistence branch corresponds to q=0, i.e. the strict-P determinant boundary.

This is an important conceptual simplification and has been incorporated into the Chief theorem file in commit `47a1043e463f39646781656da850321ea5f12908`.

---

## DA-09 sharpening accepted

The exact derivative is

~~~text
dX/dm
=
-Q/[(X-m)(s+chi)].
~~~

Hence on the positive strict-P coexistence stratum:

~~~text
Q>0,
X>m,
s+chi>0
~~~

already imply

~~~text
dX/dm<0.
~~~

No separate assumption chi>0 is needed.

For

~~~text
ds/dm<0,
~~~

a transparent sufficient condition remains

~~~text
chi>=0,
~~~

and the constructive fractional-only regime actually has chi>0 because e1e3>e2.

Thus the Allee-threshold mechanism is stronger than initially stated: prey coexistence density decreases with m throughout the strict-P branch, while monotone decrease of the effective self-slope s is guaranteed on the constructive chi>0 branch.

---

## DA-07 quantification accepted

The phrase "K sufficiently close to X" is not uniform across all realizations.

Define

~~~text
C_A
=
(m+a)/[(X-m)(X+a)].
~~~

Then

~~~text
H_A
=
1/(K-X)-C_A
~~~

and

~~~text
H_A>0
iff
X<K<
X+(X-m)(X+a)/(m+a).
~~~

For a chosen split xi in (0,1),

~~~text
mu1
=
e1 q1 X
-
Q[
 xi c1/q1
 +(1-xi)h/q2
],
~~~

so mu1>0 if Q<Q1 with the explicit Q1 bound recorded in the Chief theorem.

The analogous Q2 condition is needed only when the coefficient of Q in mu2 is negative.

This quantifies the embedding theorem and removes a possible referee objection that "sufficiently close" hides an uncontrolled feasibility issue.

---

## DA-05 degree caveat accepted

The eliminated coexistence equation is

~~~text
(r+K chi)X^2
-
[r(K+m)-K chi a+K nu]X
+
rKm-Knu a
=
0.
~~~

It is a genuine quadratic only when

~~~text
r+K chi != 0.
~~~

The constructive regime has e1e3>=e2, hence chi>0 and therefore r+Kchi>0 automatically.

Outside that regime the leading term may vanish; the equation must then be described as a polynomial equation of degree at most two rather than unconditionally "quadratic".

---

## DA-11 wording correction accepted

The prescribed E0 crossing is realized through the joint DA-06 parameter construction.

In particular, e2 and q2 are coupled through

~~~text
B0=e2 q2^2/c2.
~~~

Therefore manuscript wording must not suggest that one can vary the conversion-efficiency ratio alone while all other invariant-building parameters remain fixed.

The Chief theorem now reflects this.

---

## Computational evidence from Audit 2

Audit 2 adds corroboration through a genuinely different computational path:

- 8,000 exact rational evaluations of 20 identities: 0 failures;
- new alpha=0.8 witness with beta=(1.5,2.5,2);
- independent T_alpha minimizer;
- 25,000 joint perturbations;
- 600 theorem-vs-direct spectral comparisons: 0 discrepancies;
- 20,000 wide degeneracy draws;
- 200 local-rank checks;
- quantified DA-07 feasibility checks;
- time-domain corroboration at the worst diagonal orbit point.

This evidence is useful but remains corroboration rather than proof.

---

## Important methodological note

The worst diagonal orbit point for the angular objective

~~~text
min_D min_i |arg lambda_i(DB)|
~~~

is a property of B and does not depend on alpha.

Therefore a single worst-orbit diagonal can be used to compare multiple fractional orders against different angular boundaries.

For validation plots/searches, use scale-invariant objectives:
- eigenvalue angle;
- Re(lambda)/|lambda|.

Do not maximize raw spectral abscissa over an unnormalized positive diagonal cone.

---

## Current Chief status

~~~text
THEOREM CHAIN:                SURVIVES TWO PROCEDURAL AUDITS
AUDIT 1:                      PASS WITH MINOR FIXES
AUDIT 2:                      PASS WITH FIXES
EPISTEMIC INDEPENDENCE:       NOT SATISFIED
NOVELTY:                      GO-NARROWED
MANUSCRIPT INTEGRATION:       CONDITIONALLY PREFERRED
SUBMISSION-CERTIFIED STATUS:  NO
NEXT HARD GATE:               DIFFERENT AGENT / SESSION PROOF AUDIT
~~~

The next external audit should be smaller than Audit 1/2: the algebra is now heavily replicated. It should concentrate on the logical core DA-06, DA-07, DA-08, DA-09/10/11 and on the dependency on C-10/C-15.

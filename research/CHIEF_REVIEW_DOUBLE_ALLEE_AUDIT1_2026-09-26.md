# Chief review — first independent Double-Allee proof audit

**Date:** 2026-09-26  
**Chief branch:** `chief/double-allee-kolmogorov-20260926`  
**Audited agent branch:** `agent/compute-double-allee-proof-audit-20260926`  
**Agent final SHA:** `9235d75e8d407af8b726bb3bbfbf42c47d792151`  
**Agent status:** `COMPUTE_AUDIT_PASS_WITH_FIXES`

## 1. Chief decision

**PROVISIONAL ACCEPT — theorem package survives the first independent adversarial audit.**

This is a materially strong validation result:

- 39 tests pass, 0 fail;
- 71 independent symbolic identities, 0 mismatches;
- DA-01…DA-12 contain no mathematical FAIL;
- 160,000 joint biological-parameter perturbations were explored;
- 4,500 adversarial feasible cases were cross-checked against direct positive-diagonal spectral optimization with zero theorem/direct discrepancies;
- the chief witness was reconstructed independently at 100-digit precision;
- a one-parameter m interval and a full 14-parameter box were certified as genuinely fractional.

The result is not yet the final manuscript gate because a second independent agent is still running.

## 2. Verdicts accepted by the Chief

| Item | Agent verdict | Chief disposition |
|---|---|---|
| DA-01 orbit equivalence | PASS | ACCEPT |
| DA-02 two-consumer no-go | PASS | ACCEPT |
| DA-03 IGP matrix/invariants | PASS | ACCEPT |
| DA-04 strict-P | PASS | ACCEPT WITH SHARPENING |
| DA-05 coexistence geometry | PASS | ACCEPT |
| DA-06 invariant realization | PASS | ACCEPT |
| DA-07 double-Allee embedding | PASS | ACCEPT |
| DA-08 open biological region | PASS WITH MINOR FIX | ACCEPT FIX |
| DA-09 m sensitivity | PASS | ACCEPT WITH EXPLICIT HYPOTHESES |
| DA-10 unique classical crossing | PASS | ACCEPT WITH STRONGER TRANSVERSALITY ARGUMENT |
| DA-11 prescribed-m0 crossing | PASS | ACCEPT |
| DA-12 2D consistency | PASS | ACCEPT WITH ADMISSIBILITY CONDITION |

## 3. Integrated fixes

The Chief theorem file has been updated in commit `1560210c746507ca164bdf5a60e1229a19053528`.

### DA-08 wording

Changed from an implication of uniqueness:

> “its positive coexistence equilibrium”

to:

> “a positive coexistence equilibrium on the constructed smooth branch”.

The theorem proves existence and openness of a branch. It does not prove global uniqueness of coexistence equilibria for all parameters in the open set.

### DA-06 efficiency clause

The extra assumption `kappa>T1(beta)` was removed from the statement that the constructive realization can have

~~~text
0<e1,e2,e3<1,
e1e3>e2.
~~~

The construction already gives this for every target with

~~~text
R = kappa-(beta12+beta13+beta23-2) > 0.
~~~

### DA-04 strict-P status

The theorem now says explicitly:

- s>0 makes all order-one and order-two principal minors strict;
- full strict-P also requires q=-det B>0;
- e1e3>e2 is a simple sufficient condition for q>0;
- it is not necessary.

The exact determinant condition verified by the agent is

~~~text
h q1 q2 (e2-e1e3)
<
s(c1c2+e3h^2)
+c1 e2 q2^2
+c2 e1 q1^2.
~~~

This sharper inequality should be considered for the final theorem statement after the second audit. The current Chief theorem keeps the cleaner sufficient condition because it is enough for the realization result.

### DA-09 minimal assumptions

The sign proof now explicitly records the load-bearing assumptions:

~~~text
Q>0,
s>0,
chi>0,
m>-a.
~~~

The ecological branch additionally uses

~~~text
0<m<X<K.
~~~

### DA-10 transversality

The previous proof said the unique crossing was transverse after proving strict convexity. The compute agent correctly demanded an explicit check.

The Chief file now includes:

~~~text
G1'(t_H)
>=
[G1(t_H)-G1(0)]/t_H
=
(4+4 sqrt(C0))/t_H
>
0.
~~~

Thus transversality is not an inference from convexity alone; it has an explicit positive lower bound.

### DA-12 admissibility

The critical 2D Allee threshold is biologically positive iff

~~~text
X^2+2aX > K a.
~~~

This condition is now recorded.

## 4. Strongest new evidence

### 4.1 The no-go theorem is stronger than originally stated

The compute audit found

~~~text
T1(beta)-kappa
=
2+L3
+2[
 sqrt(beta12 beta13)
 +sqrt(beta12 beta23)
 +sqrt(beta13 beta23)
].
~~~

For the naive competitive architecture, L3>=0 for every positive parameter choice.

Therefore the inequality

~~~text
kappa<T1(beta)
~~~

holds throughout the positive-beta domain; strict-P is needed only to invoke the classical Cain classification, not for the algebraic inequality itself.

This strengthens the interpretation that the model failure is structural, not a narrow parameter accident.

### 4.2 The invariant realization is genuinely four-dimensional

The agent independently computed the Jacobian determinant of

~~~text
(beta12,beta13,beta23,kappa)
~~~

with respect to a four-parameter subfamily and obtained

~~~text
-4 e1 e3 h^2 q1^2 q2^2 (e1e3+e2)/(c1 c2 s)^3,
~~~

which is nonzero throughout the positive domain.

This provides an independent local-rank proof that the ecological architecture is not trapped in a lower-dimensional invariant variety.

### 4.3 The open biological region is now explicitly certified

The compute agent certified a full 14-parameter relative box of half-width

~~~text
5e-4
~~~

around the m=0.21 witness.

Within that box:
- the constructed coexistence branch exists and is positive;
- strict-P holds;
- kappa-T1 remains positive;
- the fractional all-D certificate remains positive.

This does not replace the IFT proof, but it independently confirms that the theorem is genuinely full-dimensional in the biological parameter space.

## 5. Witness quality assessment

The original m=0.21 witness is mathematically valid but not ideal for publication:

- it is only about 0.8% beyond the classical boundary;
- Q is generated by a near cancellation chi X ≈ nu;
- the top-predator abundance is small;
- the construction is relatively sensitive to simultaneous parameter perturbation.

The compute agent reports that the same fixed model remains certified fractional-only for

~~~text
m in [0.2005,0.45].
~~~

### Chief recommendation

For a future manuscript figure/table, use an interior point approximately

~~~text
m = 0.30 to 0.45,
~~~

rather than m=0.21, unless the purpose of the figure is specifically to illustrate transversality at the classical boundary.

The boundary witness m0=0.2 should remain as the exact analytic crossing anchor.

## 6. Numerical-method correction accepted

For positive-diagonal spectral searches, the raw spectral abscissa is not a valid scale-invariant optimization objective because multiplying all diagonal entries by a common scalar multiplies all eigenvalues.

Use instead one of:

~~~text
min_i |arg lambda_i(DB)|
~~~

or

~~~text
max_i Re(lambda_i(DB))/|lambda_i(DB)|.
~~~

This note should be propagated to all future validation code and eventually to the numerical-methods section.

## 7. Remaining lock

The first compute audit substantially raises confidence, but the Double-Allee theorem package remains:

~~~text
INTERNAL THEOREM — FIRST INDEPENDENT AUDIT PASSED
~~~

not yet:

~~~text
SUBMISSION-CERTIFIED.
~~~

The Chief waits for the second independent agent.

When it arrives:

### If the second agent also PASSes

1. reconcile any minor fixes;
2. merge/copy the validated compute artifacts into the Chief integration branch;
3. freeze the theorem statements;
4. run a final targeted novelty search against the exact final theorem wording;
5. decide standalone paper vs major extension;
6. then unlock manuscript architecture/prose.

### If the second agent finds a genuine mathematical FAIL

The second-agent failure takes precedence. The Chief will reproduce the counterexample independently before deciding MODIFY/KILL.

### If the second agent is PARTIAL/BLOCKED

Only the unresolved load-bearing item remains locked; passed items may be integrated provisionally, but manuscript claims remain locked.

## 8. Current Chief verdict

```text
MATHEMATICS:     PROVISIONAL PASS
COMPUTE AUDIT 1: PASS WITH MINOR FIXES
NOVELTY:         PROVISIONAL GO
MANUSCRIPT:      STILL LOCKED
NEXT GATE:       SECOND INDEPENDENT AGENT
```

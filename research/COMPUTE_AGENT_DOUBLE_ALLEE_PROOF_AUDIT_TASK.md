# Compute Agent — Independent adversarial proof audit + symbolic verification
## Double-Allee 3D Kolmogorov / IGP extension

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P0 / STOP-THE-LINE  
**Execution class:** symbolic + high-precision + adversarial computation  
**Dedicated branch:** `agent/compute-double-allee-proof-audit-20260926`  
**Base Chief branch:** `chief/double-allee-kolmogorov-20260926`  
**Base Chief SHA:** `ba67d678f54e3b906a85ac4c4e0c69e412c827dd`

## Mission

Independently try to **break** the new Double-Allee Kolmogorov theorem package before any manuscript integration.

Do not assume the Chief derivations are correct. Re-derive every symbolic identity from the model equations, search for sign mistakes and hidden hypotheses, attack boundary cases, and independently reproduce/certify the numerical witness.

This is not a request for prettier proofs. It is a falsification assignment.

If a theorem is false, stop promotion immediately and return the smallest counterexample / exact broken implication.

---

# 0. Read first

Read in this order:

1. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
2. `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
3. `research/novelty/DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT.md`
4. `research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md`
5. `research/THEOREM_C10_EXACT_3X3.md`
6. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
7. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`
8. `research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`
9. `computations/double_allee_igp_validation.py`
10. `computations/double_allee_igp_interval_certificate.py`
11. existing tests under `tests/`

Do **not** modify `paper/`.

Do **not** edit the Chief theorem/report files during the audit. Put corrections in your audit report. Only after a FAIL is confirmed may you add a separate proposed-correction file.

---

# 1. Required theorem-level verdicts

Return exactly one status for each item:

- `PASS`
- `PASS WITH MINOR FIX`
- `FAIL`

Audit these separately:

### DA-01 — Kolmogorov positive-equilibrium orbit equivalence

For

```text
^C D^alpha x_i = x_i F_i(x),
x* >> 0,
F(x*)=0,
B=DF(x*),
```

verify

```text
J(x*) = diag(x*) B,
```

and rigorously verify the set equality

```text
{D J(x*): D>0 diagonal}
=
{E B: E>0 diagonal}.
```

Check both fractional Matignon D-stability and classical Hurwitz D-stability equivalence.

Also verify invariance of all normalized C-10 principal-minor coordinates between J and B.

### DA-02 — No-go theorem for the naive two-consumer architecture

Starting from the original candidate

```text
x' = x[g_DA(x)-q1 y-q2 z]
y' = y[e1 q1 x-mu1-c11 y-c12 z]
z' = z[e2 q2 x-mu2-c21 y-c22 z],
```

recompute from scratch:

- B;
- p_i;
- m_12,m_13,m_23;
- q=-det B;
- beta_12,beta_13,beta_23;
- the signed directed-cycle coordinate L3;
- kappa.

Verify or falsify the claimed identity

```text
kappa
=
beta12+beta13+beta23-2-L3
```

with

```text
L3>0.
```

Then verify the decisive implication

```text
strict-P(-B)
=>
kappa<T1(beta).
```

Attack all edge cases:
- c12 or c21 -> 0;
- beta23 -> 0+;
- weak q1/q2;
- equality limits;
- any sign convention mismatch with C-13/Cain.

If the no-go statement needs extra hypotheses, identify the minimum exact hypotheses.

### DA-03 — IGP reduced matrix and exact invariants

For

```text
x' = x[g_DA(x)-q1 y-q2 z]

y' = y[e1 q1 x-mu1-c1 y-h z]

z' = z[e2 q2 x+e3 h y-mu2-c2 z],
```

derive symbolically, independently:

```text
B =
[ -s     -q1     -q2
  e1q1   -c1     -h
  e2q2    e3h    -c2 ],
s=-g_DA'(X).
```

Verify exactly:

```text
m12 = s c1 + e1 q1^2

m13 = s c2 + e2 q2^2

m23 = c1 c2 + e3 h^2
```

and

```text
q=-det B
=
s(c1c2+e3h^2)
+c1 e2 q2^2
+c2 e1 q1^2
+h q1 q2(e1e3-e2).
```

Then verify:

```text
beta12 = 1+e1q1^2/(s c1)

beta13 = 1+e2q2^2/(s c2)

beta23 = 1+e3h^2/(c1c2)

kappa
=
beta12+beta13+beta23-2
+
h q1 q2(e1e3-e2)/(s c1c2)

L3
=
h q1 q2(e2-e1e3)/(s c1c2)

kappa
=
beta12+beta13+beta23-2-L3.
```

Check exact sign convention against `THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`.

### DA-04 — strict-P conditions

Verify the claim that, for the IGP architecture,

```text
s>0
and
e1e3>e2
```

with all biological parameters positive imply -B is strict P.

Do not infer this only from the beta formulas. Check every principal minor and determinant directly.

Also determine whether e1e3>e2 is:
- necessary;
- merely sufficient;
- or unnecessarily strong.

Return the sharpest transparent strict-P condition you can prove, but do not rewrite the Chief theorem yet.

### DA-05 — exact coexistence geometry

Starting from the three equilibrium equations, independently eliminate Y,Z.

Verify:

```text
Delta = c1c2+e3h^2,

Y(X)
=
[c2(e1q1X-mu1)-h(e2q2X-mu2)]/Delta,

Z(X)
=
[e3h(e1q1X-mu1)+c1(e2q2X-mu2)]/Delta.
```

Verify the affine identity

```text
q1Y+q2Z = chi X - nu
```

and rederive chi,nu.

Then multiply the double-Allee equilibrium equation

```text
r/(X+a)(1-X/K)(X-m)=chi X-nu
```

to a polynomial and verify every coefficient of the claimed quadratic:

```text
(r+K chi) X^2
-
[r(K+m)-K chi a+K nu] X
+
rKm-Knu a
=
0.
```

Attack degeneracies:
- discriminant zero;
- roots at m, K, 0;
- both positive roots;
- feasibility of Y,Z;
- any extra root introduced by multiplication.

### DA-06 — invariant realization theorem

Audit the constructive statement:

For any

```text
beta12,beta13,beta23>1
```

and

```text
kappa>beta12+beta13+beta23-2,
```

there exist positive IGP parameters producing exactly those invariants.

Re-derive from scratch the construction:

```text
A=beta12-1
B=beta13-1
C=beta23-1

R=kappa-(beta12+beta13+beta23-2)

rho=R/sqrt(A B C)

tau=(rho+sqrt(rho^2+4))/2

e1=e3=eta
e2=eta^2/tau^2

q1=sqrt(A s c1/e1)
q2=sqrt(B s c2/e2)
h =sqrt(C c1c2/e3).
```

Verify exactly that the determinant residual equals R.

Check:
- every parameter is positive;
- e1,e2,e3 can all be chosen in (0,1);
- e1e3>e2;
- no hidden constraint from q=-det B>0;
- the construction remains valid arbitrarily near R=0+;
- whether the image really contains a four-dimensional open invariant set.

As an independent local-rank corroboration, compute the Jacobian rank of the invariant map with respect to a sensible four-parameter subfamily at exact rational/algebraic sample points.

### DA-07 — double-Allee embedding theorem

Fix a target reduced-matrix slope s>0 and verify the construction:

Choose

```text
a>0,
0<m<X<K,
H_A
=
1/(K-X)-1/(X-m)+1/(X+a)
>0.
```

Set

```text
Q=s/H_A.
```

Choose positive Y,Z with q1Y+q2Z=Q, define

```text
mu1=e1q1X-c1Y-hZ

mu2=e2q2X+e3hY-c2Z,
```

and

```text
r
=
Q(X+a)/[(1-X/K)(X-m)].
```

Verify exactly:

```text
g_DA(X)=Q,
g_DA'(X)=-s,
```

and all three equilibrium equations.

Critically audit the limiting argument “choose K sufficiently close to X”:

- prove H_A>0 is achievable;
- prove Q->0 as K->X+;
- prove r stays positive and finite or identify its exact limit;
- prove mu1>0 and mu2>0 for sufficiently small Q;
- verify X<K and X>m remain strict;
- check whether any biological parameter blows up unexpectedly.

Return a fully quantified epsilon/delta-style feasibility statement if possible.

### DA-08 — nonempty open biological region theorem

Audit the main claim:

For every

```text
0<alpha<1
```

there exists a nonempty open set in biological parameter space whose positive coexistence equilibrium is

```text
in F_alpha^(3)
but not in D_H^(3).
```

This proof combines:
- DA-06 invariant realization;
- DA-07 biological embedding;
- C-10/C-15 for 2/3<alpha<1;
- Kellogg/C-10 low-order result for alpha<=2/3;
- IFT/open inequalities.

Check carefully:

1. strict-P(-B);
2. nonsingularity of B;
3. whether IFT is applied to the correct equilibrium equations;
4. whether positivity of X,Y,Z persists;
5. whether the fractional classification is open uniformly over the entire positive diagonal orbit;
6. whether non-Hurwitz D-stability persists;
7. whether the open set is genuinely open in the **full biological parameter space**, not only an engineered lower-dimensional parameterization.

If the construction only yields an immersed/open subset of a constrained submanifold, mark FAIL.

### DA-09 — Allee-threshold sensitivity

With all parameters except m fixed, audit:

```text
g_DA(X;m)=chi X-nu=:Q(X)
```

and

```text
dX/dm
=
-
Q/
[(X-m)(s+chi)]
<0.
```

Then, with

```text
s=-g_DA'(X)
=
Q H_A,
```

verify or falsify

```text
ds/dm<0
```

under the stated assumptions.

Check every partial derivative sign, especially:

```text
H_A
=
1/(K-X)-1/(X-m)+1/(X+a).
```

Identify the exact minimal assumptions needed for ds/dm<0.

### DA-10 — invariant path and unique classical crossing

Verify the path

```text
t=1/s,

beta12=1+A0 t,

beta13=1+B0 t,

beta23=C0,

kappa=C0+(A0+B0+E0)t.
```

Re-derive

```text
G1(t)=kappa-T1(beta)
```

exactly.

Then rigorously audit:

- G1(0)<0;
- asymptotic slope;
- condition E0>2 sqrt(A0B0);
- convexity / strict convexity;
- existence and uniqueness of a positive root t_H;
- transversality at the root.

Important: do not accept “strictly convex therefore transverse” without checking whether G1'(t_H) can vanish.

If transversality needs a stronger condition, state it.

### DA-11 — prescribed-m0 crossing construction

Audit the formula that chooses E0 so a prescribed t0 is exactly on the classical Cain boundary.

Verify:
- E0>2 sqrt(A0B0);
- exact equality G1(t0)=0;
- root uniqueness;
- m0 can be embedded with t(m0)=t0 while preserving positive mortalities;
- with all other parameters fixed, there is a one-sided interval m>m0 that is fractional-only.

For alpha>2/3, explicitly use the positive gap

```text
T_alpha(beta(m0))-T1(beta(m0))>0.
```

For alpha<=2/3, check the low-order strict-P argument.

### DA-12 — 2D consistency theorem

For

```text
x' = x[g_DA(x)-q y]
y' = y[p x-d],
```

verify:

```text
X=d/p,

B2 =
[ g_DA'(X)  -q
  p           0 ].
```

Using C-07, verify:
- F_alpha^(2) iff g_DA'(X)<=0;
- classical Hurwitz D-stability iff g_DA'(X)<0;
- genuinely fractional difference is exactly g_DA'(X)=0.

Re-derive the critical Allee threshold

```text
m_c
=
X - (K-X)(X+a)/(K+a)
=
[X^2+2aX-Ka]/(K+a).
```

Check biological admissibility conditions for m_c.

---

# 2. Symbolic verification requirements

Use an independent CAS path, preferably SymPy, not hand-copied formulas.

Create:

`computations/scripts/double_allee_symbolic_audit.py`

It must symbolically derive/simplify at minimum:

1. both reduced matrices;
2. all principal minors;
3. both determinants;
4. beta/kappa/L3 identities;
5. Y(X),Z(X), chi,nu;
6. quadratic equilibrium polynomial;
7. invariant realization residual;
8. g_DA'(X) embedding identity;
9. dX/dm and ds/dm formulas;
10. G1(t), G1'(t), G1''(t);
11. 2D critical m_c.

Do not merely assert `simplify(expr)==0`; save the exact residual expressions and whether each simplifies identically to zero.

Required machine-readable output:

`computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json`

with one entry per identity:
- name;
- status;
- residual;
- assumptions used.

---

# 3. Adversarial numerical / high-precision requirements

## 3.1 Reproduce existing witness from scratch

Do not import numerical constants from the Chief report except the declared high-level design:
- alpha=0.9;
- m0=0.2;
- target invariant center beta=(2,2,2), kappa=18 at the classical boundary.

Reconstruct all biological parameters from the symbolic construction.

Then verify at:
- m=0.19;
- m=0.20;
- m=0.21.

Use:
- ordinary double precision;
- >=100-digit mpmath;
- interval arithmetic where possible.

## 3.2 Direct all-D spectral attack

For the m=0.21 point:

1. optimize diagonal ratios over at least log d_i in [-20,20];
2. use multiple global optimizers / seeds;
3. independently minimize the Matignon angular margin;
4. independently maximize classical spectral abscissa;
5. compare with C-10 and C-11 classifications;
6. repeat with high precision around the worst diagonal scalings.

## 3.3 Random falsification around the theorem point

Perturb all biological parameters jointly around the witness.

Generate at least:
- 100,000 ordinary random perturbations;
- boundary-heavy samples around m0;
- samples near positivity/strict-P boundaries.

For each:
- solve coexistence;
- reject infeasible points explicitly;
- compute B and invariants;
- classify by theorem;
- compare against direct spectral optimization on a representative adversarial subset.

No finite sampling is proof. Its purpose is to find counterexamples or hidden constraints.

## 3.4 Parameter-box certification

Attempt to certify a nontrivial parameter box around the m=0.21 witness where:
- X,Y,Z remain positive;
- strict-P holds;
- kappa-T1>0;
- fractional certificate remains positive.

If a full biological box is too expensive, certify at least a one-dimensional m interval with all other parameters fixed.

---

# 4. Independent logic checks beyond algebra

The compute agent must explicitly answer:

1. Is the no-go theorem genuinely structural or an artifact of C-13 sign convention?
2. Is the IGP realization map four-dimensional in invariant space?
3. Does the biological embedding use more free parameters than constraints in a way that genuinely gives an open full-dimensional parameter set?
4. Does K->X+ accidentally force r, mu_i, or another parameter to a pathological value?
5. Is e1e3>e2 biologically plausible when all efficiencies are constrained to (0,1)?
6. Does m really move the **same model** with all other parameters fixed, or does any hidden construction re-tune another parameter?
7. Can the m-branch hit feasibility loss before the claimed local crossing?
8. Is the classical crossing genuinely transverse?
9. Is the 2D/3D contrast exact under the same D-stability definitions?
10. Is any theorem accidentally using the sufficient C-11 certificate where exact C-10 is required?

---

# 5. Required deliverables

Create at minimum:

- `research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`
- `computations/scripts/double_allee_symbolic_audit.py`
- `computations/scripts/double_allee_adversarial_validation.py`
- `computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json`
- `computations/results/DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json`
- `computations/results/DOUBLE_ALLEE_WORST_CASES.csv`
- `computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json` if certification succeeds
- new tests under `tests/`

The final report must contain a verdict table for **DA-01 through DA-12**.

If any item FAILS, the report must place the failure at the top and include:
- smallest explicit counterexample if possible;
- exact failed identity/implication;
- whether downstream DA claims collapse.

---

# 6. Test requirements

Run:
- all pre-existing tests;
- all new Double-Allee tests.

Add deterministic tests for:
- symbolic identities at random positive substitutions;
- exact invariant reconstruction;
- equilibrium reconstruction;
- m0 classical-boundary equality;
- one point on each side of the m crossing;
- interval witness;
- direct C-10 versus direct spectral optimization for representative cases.

Final message must report exact test count and failures.

---

# 7. Repository discipline

Work **only** on:

`agent/compute-double-allee-proof-audit-20260926`

Allowed modifications:
- `computations/`
- `tests/`
- `src/fdsn/` only if new reusable audit utilities are needed
- `research/` for audit reports/results

Forbidden:
- `paper/`
- rewriting Chief theorem files
- changing novelty conclusions
- merging to main

Commit by phase.

Suggested commits:
1. baseline + symbolic audit;
2. theorem adversarial tests;
3. interval/high-precision certification;
4. final proof-audit report.

---

# 8. Final status

Return exactly one overall compute status:

- `COMPUTE_AUDIT_PASS`
- `COMPUTE_AUDIT_PASS_WITH_FIXES`
- `COMPUTE_AUDIT_FAIL`
- `PARTIAL/BLOCKED`

At completion push the branch and report:
- branch;
- final SHA;
- total tests passed/failed;
- DA-01...DA-12 verdicts;
- overall status;
- decisive artifact paths.

## Chief lock

Until this audit returns PASS/PASS WITH FIXES and the Chief integrates it:

- do not merge the Double-Allee extension into manuscript claims;
- do not alter the paper title/abstract;
- do not call the new open-region theorem submission-certified.

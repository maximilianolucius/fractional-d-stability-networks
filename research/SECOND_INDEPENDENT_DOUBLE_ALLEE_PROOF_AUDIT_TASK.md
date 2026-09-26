# Second independent proof audit — Double-Allee theorem package

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P0 / final theorem gate  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/independent-proof-double-allee-20260926`  
**Base integration SHA:** `36bf80f2fdaa0c1baa806d064b02b8f26771f8ac`

## Mission

Perform a genuinely **independent proof audit** of the Double-Allee Kolmogorov / intraguild-predation theorem package.

This is **not** a rerun of the first compute audit.

Your primary job is to re-prove or falsify the Chief theorem chain from first principles, with special attention to:

- quantifiers;
- hidden hypotheses;
- openness in the full biological parameter space;
- boundary and degeneracy cases;
- theorem dependency correctness;
- transversality;
- biological feasibility;
- whether any claim silently relies on numerical evidence.

A correct counterexample outranks every other deliverable.

---

# 1. Independence protocol

## Phase A — blind proof audit

Before you form your own theorem verdicts, **do not read**:

- `research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`
- `research/CHIEF_REVIEW_DOUBLE_ALLEE_AUDIT1_2026-09-26.md`
- `computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json`
- `computations/results/DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json`
- `computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json`
- `computations/results/DOUBLE_ALLEE_WORST_CASES.csv`
- `tests/test_double_allee.py`
- `src/fdsn/double_allee.py`
- any Double-Allee audit scripts produced by the first compute agent.

Do not import those modules or reuse their formulas.

### Files you SHOULD read in Phase A

1. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
2. `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
3. `research/THEOREM_C10_EXACT_3X3.md`
4. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
5. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`
6. `research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`

You may use standard CAS or numerical software of your own choosing, but write your own derivations/scripts.

## Phase B — adversarial cross-check

Only after you have written a timestamped blind verdict for DA-01…DA-12 may you read the first agent's audit and compare:

- agreements;
- disagreements;
- missed assumptions;
- stronger/weaker claims;
- any unexplained discrepancy.

The final report must clearly separate:

1. **Blind findings**;
2. **Post-unblinding reconciliation**.

---

# 2. Required theorem verdicts

Return exactly one of:

- `PASS`
- `PASS WITH MINOR FIX`
- `FAIL`

for each item.

## DA-01 — Kolmogorov orbit equivalence

Verify from first principles that for

~~~text
^C D^alpha x_i = x_i F_i(x),
x* >> 0,
F(x*)=0,
B=DF(x*),
~~~

one has

~~~text
J(x*) = diag(x*) B,
~~~

and

~~~text
{D J(x*): D>0 diagonal}
=
{E B: E>0 diagonal}.
~~~

Check both:
- Matignon positive-diagonal stability;
- classical Hurwitz D-stability.

Also verify normalized C-10 invariants are identical for J and B.

## DA-02 — no-go theorem for the naive two-consumer architecture

Re-derive from the model equations:

~~~text
x' = x[g_DA(x)-q1 y-q2 z]
y' = y[e1 q1 x-mu1-c11 y-c12 z]
z' = z[e2 q2 x-mu2-c21 y-c22 z].
~~~

Independently compute:
- reduced B;
- principal minors;
- determinant;
- beta_ij;
- kappa;
- L3.

Then prove or falsify:

~~~text
strict-P(-B)
=> kappa < T1(beta).
~~~

Test edge cases and all sign conventions.

## DA-03 — IGP matrix and invariant identities

For

~~~text
x' = x[g_DA(x)-q1 y-q2 z]
y' = y[e1 q1 x-mu1-c1 y-h z]
z' = z[e2 q2 x+e3 h y-mu2-c2 z],
~~~

derive from scratch:

~~~text
B =
[ -s      -q1      -q2
  e1 q1   -c1      -h
  e2 q2    e3 h    -c2 ],
s=-g_DA'(X).
~~~

Verify exact formulas for:
- m12,m13,m23;
- q=-det B;
- beta12,beta13,beta23;
- kappa;
- L3;
- kappa = beta12+beta13+beta23-2-L3.

## DA-04 — strict-P conditions

Determine the exact condition for -B to be strict P.

Check whether

~~~text
s>0,
e1e3>e2
~~~

is:
- necessary;
- sufficient;
- neither.

Give the sharpest transparent condition you can prove.

## DA-05 — coexistence geometry

Starting only from the equilibrium equations, derive:
- Y(X);
- Z(X);
- Delta;
- chi;
- nu;
- q1Y+q2Z = chi X - nu.

Then verify the claimed quadratic in X exactly.

Audit:
- spurious roots;
- double roots;
- roots at 0,m,K;
- two-positive-root cases;
- Y,Z positivity.

## DA-06 — invariant realization theorem

Audit the constructive claim:

For any

~~~text
beta12,beta13,beta23>1
~~~

and

~~~text
kappa >
beta12+beta13+beta23-2,
~~~

there exist positive IGP parameters realizing exactly those invariants.

Re-derive the tau construction independently.

Check:
- residual exactly zero;
- e1,e2,e3 can lie in (0,1);
- e1e3>e2;
- determinant positivity;
- behavior as R->0+;
- local rank 4 of the invariant map.

A rank-deficient image means FAIL.

## DA-07 — biological embedding into the double-Allee law

Audit the construction with

~~~text
H_A
=
1/(K-X)-1/(X-m)+1/(X+a),
Q=s/H_A.
~~~

Verify:
- H_A>0 can be achieved;
- Q>0;
- Q->0 as K->X+;
- r remains positive and finite;
- mu1,mu2 can both remain positive;
- g_DA(X)=Q;
- g_DA'(X)=-s;
- all three equilibrium equations hold.

Give a quantified feasibility statement, not just a limit heuristic.

## DA-08 — full-dimensional open biological region

This is load-bearing.

Audit the claim:

For every

~~~text
0<alpha<1
~~~

there exists a nonempty **open set in the full biological parameter space** such that a positive coexistence equilibrium satisfies

~~~text
J in F_alpha^(3) \ D_H^(3).
~~~

Check:
- correct use of IFT;
- correct state-space Jacobian;
- persistence of coexistence positivity;
- strict-P persistence;
- all-D fractional stability openness;
- non-Hurwitz persistence;
- whether construction is genuinely full-dimensional, not merely a constrained submanifold.

If only a lower-dimensional family is proved, DA-08 = FAIL.

## DA-09 — sensitivity to the Allee threshold m

With all other parameters fixed, verify:

~~~text
dX/dm
=
-Q/[(X-m)(s+chi)].
~~~

Audit the sign claim dX/dm<0 and then the stronger claim

~~~text
ds/dm<0.
~~~

Identify the minimal exact assumptions.

## DA-10 — invariant path and unique classical crossing

Verify:

~~~text
t=1/s,

beta12=1+A0 t,
beta13=1+B0 t,
beta23=C0,

kappa=C0+(A0+B0+E0)t.
~~~

Derive G1(t)=kappa-T1(beta) independently.

Prove or falsify:
- G1(0)<0;
- asymptotic positive growth under the stated condition;
- strict convexity;
- existence of exactly one positive root;
- transversality at that root.

Do not infer transversality merely from convexity.

## DA-11 — prescribed-m0 crossing

Audit the construction selecting E0 so a chosen t0 lies exactly on the classical Cain boundary.

Then verify that one can embed t(m0)=t0 while:
- keeping all other biological parameters fixed;
- retaining positive coexistence;
- getting a one-sided interval m>m0 that is genuinely fractional-only.

Separate alpha>2/3 and alpha<=2/3 cases.

## DA-12 — exact 2D consistency theorem

For

~~~text
x' = x[g_DA(x)-q y]
y' = y[p x-d],
~~~

verify:
- X=d/p;
- the 2x2 reduced matrix;
- fractional D-stability iff g_DA'(X)<=0;
- classical D-stability iff g_DA'(X)<0;
- fractional-only iff g_DA'(X)=0.

Re-derive

~~~text
m_c
=
X-(K-X)(X+a)/(K+a)
=
[X^2+2aX-Ka]/(K+a)
~~~

and state exact biological admissibility conditions.

---

# 3. Mandatory dependency audit

For every proof, identify whether it uses:

- C-07;
- C-10;
- C-11;
- C-15;
- Cain's theorem;
- Kellogg/P-matrix wedge;
- IFT;
- only elementary algebra.

Flag any circularity.

In particular:

- DA-08 must not use numerical certification as proof.
- DA-11 must not use C-11 where exact C-10 is required.
- The low-order alpha<=2/3 case must be logically separated from the high-order case.

---

# 4. Required independent artifacts

Create your own files, distinct from Audit 1:

- `research/DOUBLE_ALLEE_PROOF_AUDIT2_FINAL.md`
- `research/DOUBLE_ALLEE_PROOF_AUDIT2_BLIND_VERDICTS.md`
- `computations/audit2/double_allee_proof_checks.py`
- `computations/audit2/DOUBLE_ALLEE_AUDIT2_RESULTS.json`

Optional:
- additional symbolic notebook/script;
- exact counterexample files if any;
- a short dependency graph.

Do not overwrite Audit 1 artifacts.

---

# 5. Minimum computational corroboration

This is a proof audit, not a compute campaign, but independent checks are required.

At minimum:

1. independently reconstruct one fractional-only biological point;
2. verify one point on each side of the m-crossing;
3. perform direct spectral checks using scale-invariant objectives;
4. run at least 20,000 independent randomized perturbations or an equivalent adversarial test;
5. compare theorem classification versus direct spectral checks on a nontrivial subset.

Use new code, not Audit 1 code.

If your proof fails, numerical evidence cannot rescue it.

---

# 6. Post-unblinding comparison

Only after freezing the blind verdict file:

Read Audit 1 and Chief Review 1.

Then add a section to your final report:

## Independent comparison with Audit 1

For each DA item:
- same verdict / different verdict;
- same proof idea / independent proof;
- assumptions Audit 1 found that you missed;
- assumptions you found that Audit 1 missed.

If the two audits disagree on any load-bearing item, overall status cannot be PASS until the disagreement is resolved.

---

# 7. Overall final status

Return exactly one:

- `PROOF_AUDIT2_PASS`
- `PROOF_AUDIT2_PASS_WITH_FIXES`
- `PROOF_AUDIT2_FAIL`
- `PARTIAL/BLOCKED`

A PASS requires DA-06, DA-07, DA-08, DA-09, DA-10 and DA-11 to be fully proved.

---

# 8. Repository discipline

Work only on:

`agent/independent-proof-double-allee-20260926`

Do not modify:
- `paper/`;
- the Chief theorem file;
- the Chief report;
- novelty audit files;
- Audit 1 files.

Allowed:
- new audit2 files;
- new audit2 scripts/results;
- new audit2 tests if clearly namespaced.

Commit by logical phase and push the branch.

At completion report:
- branch;
- final SHA;
- DA-01…DA-12 verdict table;
- overall status;
- tests/checks run;
- decisive artifact paths;
- any disagreement with Audit 1.

## Chief lock

Until Audit 2 is complete and reconciled:

- no merge to main;
- no final manuscript claims;
- no title/abstract rewrite;
- no “submission-certified” language.

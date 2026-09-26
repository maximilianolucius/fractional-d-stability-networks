# External independent proof audit — Double-Allee theorem core

**Date:** 2026-09-26  
**Assigned by:** Chief Researcher  
**Priority:** P0 / final manuscript gate  
**Repository:** \`maximilianolucius/fractional-d-stability-networks\`  
**Work branch:** \`agent/external-proof-double-allee-20260926\`  
**Base Chief integration SHA:** \`87e1e6bf2c3a9707896917320d43aeb5610ba5dd\`

## Eligibility rule — mandatory

This task must be executed by an auditor that is **not the same agent/session that produced Audit 1 or Audit 2**.

If you know that you are the same agent/session that produced either:

- \`research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md\`
- \`research/DOUBLE_ALLEE_PROOF_AUDIT2_FINAL.md\`

then STOP and report:

\`INELIGIBLE_SAME_AUDITOR\`

Do not continue the audit.

The Chief needs epistemic independence, not another replication.

---

# Mission

Perform a fresh theorem-level proof audit of the final integrated Double-Allee package.

The algebraic identities have already been heavily replicated. Your main job is to attack the logical core:

1. invariant realization;
2. biological embedding;
3. full-dimensional openness;
4. Allee-threshold monotonicity;
5. unique/transverse classical crossing;
6. one-sided fractional-only transition;
7. exact dependence on C-10/C-15/Cain/Kellogg.

A correct counterexample or missing hypothesis has priority over everything else.

---

# Read first

1. \`research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md\`
2. \`research/THEOREM_C10_EXACT_3X3.md\`
3. \`research/THEOREM_C15_THRESHOLD_GEOMETRY.md\`
4. \`research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md\`
5. \`research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md\`
6. \`research/CHIEF_REVIEW_DOUBLE_ALLEE_AUDIT2_2026-09-26.md\`

Do not modify Chief theorem files or \`paper/\`.

---

# Core claims to audit

Return PASS / PASS WITH FIX / FAIL for each.

## EXT-01 — invariant realization

Audit Section 6.

For every

~~~text
beta12,beta13,beta23>1
~~~

and

~~~text
kappa>beta12+beta13+beta23-2,
~~~

does the constructive IGP parameter choice realize exactly those four invariants?

Check:
- positivity;
- efficiencies in (0,1);
- e1e3>e2;
- q>0;
- no hidden algebraic constraint;
- image genuinely contains an open 4D invariant set.

## EXT-02 — quantified biological embedding

Audit Section 7.

Given an arbitrary realized reduced matrix slope s>0, verify that there exist positive biological parameters and a positive equilibrium with 0<m<X<K such that:
- g_DA(X)=q1Y+q2Z;
- g_DA'(X)=-s;
- all three coexistence equations hold;
- mu1,mu2>0.

Audit the explicit quantities:
- C_A;
- K_max;
- Q1;
- Q2;
- the bound on K-X;
- the finite limit of r as K->X+.

This theorem must be quantified, not heuristic.

## EXT-03 — full-dimensional open biological region

Audit Section 8.

This is the main load-bearing theorem.

For every 0<alpha<1, is there a nonempty OPEN SET in the **full biological parameter space** such that a positive coexistence equilibrium satisfies

~~~text
J in F_alpha^(3) \ D_H^(3)?
~~~

Check:
- one constructed base point really exists;
- full state Jacobian / per-capita Jacobian distinction;
- IFT matrix is correct;
- determinant/nondegeneracy condition;
- positivity persists;
- invariant inequalities persist;
- openness is in all biological coordinates, not only a constrained parameterization.

A lower-dimensional family is FAIL.

## EXT-04 — exact strict-P / nondegeneracy identity

Audit the identity

~~~text
q=-det B=Delta(s+chi),
Delta=c1c2+e3h^2.
~~~

Check the consequences:
- strict-P iff s>0 and s+chi>0;
- scalar coexistence derivative Phi_X=-(s+chi);
- fold boundary corresponds to q=0.

## EXT-05 — Allee sensitivity

Audit Section 9.

Prove or falsify:

~~~text
dX/dm
=
-Q/[(X-m)(s+chi)]<0
~~~

throughout the positive strict-P coexistence stratum.

Then determine the exact hypothesis under which

~~~text
ds/dm<0.
~~~

The Chief theorem currently uses chi>=0 as a transparent sufficient condition and the constructive regime has chi>0.

## EXT-06 — unique/transverse Cain crossing

Audit Section 10.

For

~~~text
G1(t)=kappa(t)-T1(beta(t)),
~~~

check:
- exact formula;
- strict convexity;
- crossing iff E0>2 sqrt(A0B0);
- exactly one positive root;
- explicit transversality lower bound.

## EXT-07 — prescribed-m0 fractional-only transition

Audit Section 11.

Check the construction that prescribes t0 (hence m0) on the exact Cain boundary.

Then verify:
- all other model parameters remain fixed when m varies;
- t(m) crosses t0 in the correct direction;
- for alpha>2/3, exact C-10 gives a one-sided interval with kappa<T_alpha;
- for alpha<=2/3, strict-P + Kellogg gives fractional stability;
- classical D-stability is lost immediately on the m>m0 side.

Check carefully that C-11 is not substituted where C-10 exactness is needed.

## EXT-08 — dependency / circularity audit

Produce a dependency graph showing exactly which results rely on:
- C-07;
- C-10;
- C-15;
- Cain;
- Kellogg;
- IFT;
- elementary algebra/calculus.

Flag any circular dependence.

---

# Required adversarial work

At minimum:

1. search analytically for a counterexample to EXT-03 openness;
2. search analytically for a counterexample to EXT-05 sign claims when chi<0;
3. test whether the embedding can fail because Q1/Q2 bounds are incompatible with H_A>0;
4. check whether e1e3>e2 imposes a biologically impossible efficiency requirement under 0<e_i<1;
5. check whether two positive coexistence equilibria can invalidate any theorem statement;
6. inspect alpha->1- and alpha->2/3+ for hidden discontinuity in EXT-03/07.

Computational experiments are allowed as falsification tools but are not proof.

---

# Required deliverable

Create:

\`research/DOUBLE_ALLEE_EXTERNAL_PROOF_AUDIT_FINAL.md\`

Optional:
- \`computations/external_audit/\`
- additional tests.

Final status must be exactly one of:

- \`EXTERNAL_AUDIT_PASS\`
- \`EXTERNAL_AUDIT_PASS_WITH_FIXES\`
- \`EXTERNAL_AUDIT_FAIL\`
- \`INELIGIBLE_SAME_AUDITOR\`
- \`PARTIAL/BLOCKED\`

At completion push the branch and report:
- branch;
- final SHA;
- EXT-01…EXT-08 verdicts;
- overall status;
- any counterexample/missing hypothesis;
- artifact paths.

## Repository lock

Do not:
- merge to main;
- edit paper;
- rewrite Chief theorem files;
- silently fix a failed theorem.

If a load-bearing claim fails, report the smallest exact failure first.

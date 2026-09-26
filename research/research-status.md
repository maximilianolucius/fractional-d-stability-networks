# Research status — Chief Researcher canonical update

**Date:** 2026-09-25  
**State:** theorem package developed; independent adversarial proof audit and heavy compute validation pending.

## Central objects

For fixed \(0<\alpha<1\),

\[
\Sigma_\alpha
=
\{z\ne0:|\arg z|>\alpha\pi/2\},
\]

\[
\mathcal F_\alpha^{(n)}
=
\{A\in\mathbb R^{n\times n}:
\sigma(DA)\subset\Sigma_\alpha
\text{ for every positive diagonal }D\},
\]

and

\[
\mathcal P_\alpha^{(n)}
=
\mathcal F_\alpha^{(n)}
\setminus
\mathcal D_H^{(n)},
\]

where \(\mathcal D_H^{(n)}\) is the classical Hurwitz D-stable class.

The scientific center is the structure of the genuinely fractional difference class \(\mathcal P_\alpha\).

## Flagship theorem package

### C-07 — exact 2x2 classification

For every \(0<\alpha<1\),

\[
A\in\mathcal F_\alpha^{(2)}
\iff
\det A>0,\quad a_{11}\le0,\quad a_{22}\le0.
\]

Hence \(\operatorname{int}\mathcal P_\alpha^{(2)}=\varnothing\).

### C-10 — exact robust 3x3 characterization

On the full-dimensional strict-P(-A) stratum define

\[
\beta_{12}=\frac{m_{12}}{p_1p_2},
\quad
\beta_{13}=\frac{m_{13}}{p_1p_3},
\quad
\beta_{23}=\frac{m_{23}}{p_2p_3},
\quad
\kappa=\frac{-\det A}{p_1p_2p_3}.
\]

For \(2/3<\alpha<1\), the entire positive diagonal orbit reduces exactly to a two-dimensional simplex and

\[
\boxed{
A\in\mathcal F_\alpha^{(3)}
\iff
\kappa<T_\alpha(\beta).
}
\]

At \(\alpha=1\),

\[
T_1(\beta)
=
\left(
\sqrt{\beta_{12}}
+\sqrt{\beta_{13}}
+\sqrt{\beta_{23}}
\right)^2,
\]

recovering Cain's exact 3x3 D-stability boundary.

The exact genuinely fractional full-dimensional band is

\[
\boxed{
T_1(\beta)<\kappa<T_\alpha(\beta).
}
\]

For \(0<\alpha\le2/3\), every strict-P(-A) matrix is fractionally D-stable.

### C-09 — minimum robust dimension

As a consequence of C-07/C-10,

\[
\boxed{
\min\left\{
n:
\operatorname{int}\mathcal P_\alpha^{(n)}
\ne\varnothing
\right\}=3
\quad
\forall\,0<\alpha<1.
}
\]

### C-11 — simple sufficient certificate

C-11 gives the exact orbit minimum

\[
\Phi(A)
=
\inf_{D\succ0}\frac{a_Db_D}{c_D}
\]

and a simple sufficient high-order certificate. C-10 and the Siami slice show that this scalar certificate is not necessary.

### C-12/C-13 — GLV and ecological loops

For a positive GLV equilibrium,

\[
J=\operatorname{diag}(x^*)A,
\]

membership in \(\mathcal F_\alpha\), \(\mathcal D_H\), and \(\mathcal P_\alpha\) is unchanged.

The exact 3x3 orbit coordinates have the motif form

\[
\beta_{ij}
=
1-\frac{a_{ij}a_{ji}}{p_ip_j},
\]

and

\[
\kappa
=
\beta_{12}+\beta_{13}+\beta_{23}-2-L_3,
\]

where \(L_3\) is total normalized directed three-cycle feedback.

### C-14 — quantitative classical limit

For \(2/3<\alpha<1\), \(T_\alpha(\beta)\) is strictly decreasing in \(\alpha\), and

\[
T_\alpha(\beta)
=
T_1(\beta)
+
C(\beta)(1-\alpha)
+
O((1-\alpha)^2)
\]

as \(\alpha\to1^-\), with explicit \(C(\beta)>0\).

## Novelty state

Targeted searches found no theorem equivalent to C-09 or C-10. Their current status is:

- mathematically: INTERNAL THEOREM;
- novelty: SURVIVES TARGETED SEARCH / PROVISIONAL;
- submission: NOT YET CERTIFIED.

Do not claim novelty for Matignon stabilization, fixed-polynomial fractional Routh-Hurwitz, generalized D-stability, relative D-stability, strong D-stability, single-cycle fractional secant conditions, P-matrix wedges, or Cain's classical theorem.

## Active independent validation lanes

### Lane A — adversarial proof verifier

Branch:

`agent/proof-audit-c07-c10-20260925`

Task:

`research/PROOF_AUDIT_TASK_C07_C09_C11.md`

The verifier must attempt to break C-07/C-09/C-10/C-11/C-14 before improving anything.

### Lane B — high-compute validation/discovery

Branch:

`agent/compute-c10-wave1-20260925`

Task:

`research/COMPUTE_AGENT_WAVE1_TASK.md`

This is a large campaign: high precision, million-scale adversarial tests, exact-threshold implementation, C-11 gap analysis, C-14 rate checks, ecological phase data, and n=4 reconnaissance.

## Manuscript lock

Final title/abstract/conclusions remain locked until:

1. proof audit passes;
2. compute wave returns without a persistent counterexample;
3. final independent specialist novelty audit of C-10;
4. exact citations/theorem numbers and sign conventions are verified.

Architecture planning is allowed. Final prose drafting is not.


## C-15/C-16 — threshold and orbit geometry

C-15 proves that the exact C-10 variational problem is globally strictly convex in logit coordinates, so its optimizer is unique, nondegenerate and smooth. It also gives a global threshold-surface parametrization, the alpha->2/3+ asymptotic, and realizability of the whole fractional band.

C-16 gives the general dimension-n positive-diagonal orbit reduction to the open simplex through normalized principal-minor invariants. It explains structurally why n=3 has 4 nontrivial invariants and n=4 has 11.

These results strengthen the theorem package but do not change the current validation lock: final integration of Compute Wave 1 still waits for P2 high-precision completion.


---

# Chief extension state — 2026-09-26

## Double-Allee Kolmogorov extension

The user-requested extension has been investigated at theorem level.

### Original architecture

The shared-prey / two-competing-consumer extension is **KILLED** as the paper model: on the strict-P stratum its signed-cycle structure forces

```text
kappa < T1(beta),
```

so it cannot realize an open genuinely fractional-only D-stable band.

### Redesigned architecture

The active ecological model is a standard three-species intraguild-predation / omnivory Kolmogorov system with a double-Allee basal prey.

Chief theorem development currently provides:

1. exact positive coexistence geometry;
2. exact Kolmogorov positive-diagonal orbit equivalence;
3. exact beta_ij / kappa / L3 formulas;
4. constructive four-invariant realization on beta_ij>1;
5. biological embedding of any required positive self-slope s using the double-Allee law;
6. a nonempty open biologically feasible fractional-only parameter region for every 0<alpha<1;
7. a monotone m-path with ds/dm<0;
8. a tunable classical-to-fractional-only crossing with all non-m parameters fixed;
9. exact 2D codimension-one contrast;
10. one interval-certified alpha=0.9 interior witness.

Primary Chief files:

- `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
- `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
- `research/novelty/DOUBLE_ALLEE_KOLMOGOROV_NOVELTY_AUDIT.md`
- `research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md`

## Active STOP-THE-LINE validation lane

A dedicated compute-agent branch has been created:

`agent/compute-double-allee-proof-audit-20260926`

Task:

`research/COMPUTE_AGENT_DOUBLE_ALLEE_PROOF_AUDIT_TASK.md`

The agent must independently rederive and attempt to falsify DA-01 through DA-12 using symbolic algebra, high precision, interval arithmetic and direct spectral optimization.

Required final report:

`research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`

Overall acceptable statuses:

- `COMPUTE_AUDIT_PASS`
- `COMPUTE_AUDIT_PASS_WITH_FIXES`

Unacceptable / stop states:

- `COMPUTE_AUDIT_FAIL`
- unresolved `PARTIAL/BLOCKED` on any load-bearing theorem.

## Integration gate

The Chief will **not** integrate the Double-Allee extension into manuscript claims unless all load-bearing items pass:

- DA-02 no-go theorem;
- DA-03 invariant identities;
- DA-06 invariant realization;
- DA-07 biological embedding;
- DA-08 full-dimensional open-region theorem;
- DA-09/10/11 Allee-threshold crossing;
- DA-12 2D contrast.

A minor algebraic correction is acceptable only if it leaves the theorem statements unchanged or narrows them transparently without destroying the open-region/crossing conclusions.

A counterexample to DA-06, DA-07 or DA-08 returns the project to **MODIFY/KILL** immediately.

## Work allowed in parallel

Until the compute audit returns, the Chief may:
- continue literature/novelty verification;
- refine theorem dependencies and proof architecture;
- prepare a decision tree for standalone paper vs major extension.

The Chief may **not**:
- write final manuscript claims;
- change title/abstract/conclusion;
- merge the extension into main;
- call the new ecology theorem submission-certified.


---

# Chief extension state — audit resolution (2026-09-26, later)

The STOP-THE-LINE compute audit returned and has been merged into this branch
(`agent/compute-double-allee-proof-audit-20260926` @ `9235d75`, report `research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`).

**Overall: `COMPUTE_AUDIT_PASS_WITH_FIXES`.** DA-01..DA-07 and DA-09..DA-12 PASS; DA-08 PASS WITH MINOR FIX (wording only).
No identity failed (71 SymPy re-derivations), no counterexample, no C-10 mismatch in 4,500 direct spectral cross-checks of
160,000 joint parameter perturbations; the alpha=0.9 witness is reproduced from the design at 100 digits; m in [0.2005, 0.45]
(all other parameters fixed) and a full 14-parameter box of relative half-width 5e-4 around m=0.21 are interval-CERTIFIED
genuinely fractional. Tests: 39 passed.

Integration gate: all load-bearing items (DA-02, DA-03, DA-06, DA-07, DA-08, DA-09/10/11, DA-12) passed. The audit fixes were
integrated by the Chief in `THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md` (commit `1560210`, "integrate first Double-Allee audit fixes"):

1. §8: "its positive coexistence equilibrium" -> "a positive coexistence equilibrium (the constructed branch)"; uniqueness is not claimed;
2. §6: the redundant hypothesis "if in addition kappa > T1" for the efficiency bounds removed (every R > 0 target admits 0 < e_i < 1, e1 e3 > e2);
3. §5: e1 e3 > e2 recorded as sufficient, not necessary (full strict-P additionally requires q = -det B > 0);
4. §9: minimal sign assumptions (Q > 0, s > 0, chi > 0, m > -a) stated explicitly;
5. §10: automatic transversality bound G1'(t_H) >= (4 + 4 sqrt(C0))/t_H added;
6. §12: admissibility m_c > 0 <=> X^2 + 2aX > Ka added.

Audit recommendations kept for the manuscript stage: choose a less fragile witness (m ~ 0.3-0.45 of the certified interval; the
m=0.21 point is 0.8% beyond the Cain boundary with log-parameter condition ~10^3); in numerical validation maximise Re(lambda)/|lambda|
(never the raw spectral abscissa) over positive diagonals; use interval Newton / mean-value forms for parameter-box certificates.

Still locked: no manuscript claims, no title/abstract change, no merge to main, not submission-certified.


---

## Audit 2 resolution — 2026-09-26

Audit 2 branch:

`agent/independent-proof-double-allee-20260926`

Final SHA:

`fb970648ff8dcb586fe5733c52717bf2c4d9d20f`

Status:

`PROOF_AUDIT2_PASS_WITH_FIXES`

Important independence disclosure:

The auditor was the **same agent/session** that produced Audit 1. It respected the blind-file protocol and froze its blind verdicts before unblinding, but it is not epistemically independent.

Therefore Audit 2 is counted as:

~~~text
strong blind replication / adversarial rerun
~~~

and **not** as satisfying the final different-agent proof gate.

New exact refinements integrated into the Chief theorem:

1. `q = Delta (s+chi)`;
2. strict-P iff `s>0` and `s+chi>0`;
3. `dX/dm<0` follows on the positive strict-P coexistence branch without a separate `chi>0` assumption;
4. `ds/dm<0` is guaranteed under `chi>=0` and in particular on the constructive `chi>0` branch;
5. explicit `K_max`, `Q1`, `Q2` feasibility bounds replace an unquantified "K sufficiently close";
6. the eliminated coexistence equation is genuinely quadratic only when `r+Kchi!=0`, automatic in the constructive regime;
7. the prescribed crossing uses a joint DA-06 parameter realization, not variation of an efficiency ratio alone.

Chief review:

`research/CHIEF_REVIEW_DOUBLE_ALLEE_AUDIT2_2026-09-26.md`

Integrated theorem sharpening commit:

`47a1043e463f39646781656da850321ea5f12908`

Current status:

~~~text
DOUBLE-ALLEE THEOREM CHAIN:  SURVIVES TWO PROCEDURAL AUDITS
AUDIT 1:                     PASS WITH MINOR FIXES
AUDIT 2:                     PASS WITH FIXES
TRUE INDEPENDENT AUDIT:      STILL REQUIRED
NOVELTY:                     GO-NARROWED
MANUSCRIPT:                  LOCKED FOR FINAL CLAIMS
~~~


---

## True external proof audit — final gate resolution (2026-09-26)

External audit branch:

`agent/external-proof-double-allee-20260926`

Final SHA:

`5066fa067dbff1c9b79c053195dbc992b28dc5a4`

Artifact:

`research/DOUBLE_ALLEE_EXTERNAL_PROOF_AUDIT_FINAL.md`

Status:

`EXTERNAL_AUDIT_PASS_WITH_FIXES`

Eligibility gate:

~~~text
SATISFIED — different session from Audit 1 and Audit 2.
~~~

Verdicts:

~~~text
EXT-01 PASS
EXT-02 PASS
EXT-03 PASS
EXT-04 PASS
EXT-05 PASS WITH FIX
EXT-06 PASS
EXT-07 PASS
EXT-08 PASS
~~~

No load-bearing structural implication failed.

### External strengthening integrated

The external auditor proved that the previous sufficient condition `chi>=0` for

~~~text
ds/dm<0
~~~

is unnecessary.

On the positive strict-P coexistence stratum:

~~~text
Q>0,
s>0,
s+chi>0,
m>-a,
0<m<X<K
~~~

already imply

~~~text
dX/dm<0
and
ds/dm<0.
~~~

The exact proof uses

~~~text
H_X-H_A^2
=
2(X+a-X+m)(K-X+X+a) /
[(X-m)(K-X)(X+a)^2]
>0,
~~~

equivalently the simplified positive form recorded in the theorem file.

This strengthening is integrated in commit:

`e7404639dced1b674233847f84f128a825a66069`

### Additional external conclusions

- two positive coexistence equilibria can exist, but all theorems are branch-local and make no global uniqueness claim;
- the full 14-dimensional openness argument is valid;
- the quantified embedding bounds are mutually compatible;
- the prescribed m0 crossing uses exact C-10 in the high-order range and Kellogg in the low-order range;
- C-11 is not load-bearing;
- no circular dependence was found.

### Gate decision

~~~text
DOUBLE-ALLEE PROOF GATE:          CLOSED / PASS
TRUE EXTERNAL INDEPENDENCE:       SATISFIED
THEOREM PACKAGE:                  EXTERNALLY AUDITED
NOVELTY:                          GO-NARROWED
MANUSCRIPT ARCHITECTURE:          UNLOCKED
MANUSCRIPT SUBMISSION-READY:      NO — drafting/reference/editorial gates remain
MERGE TO MAIN:                    NOT YET
~~~

The research theorem package may now be used in manuscript architecture and theorem prose.

Before final submission, remaining non-proof gates are:

1. final bibliography sanitation using only published/non-arXiv references;
2. exact DOI/publisher verification for every cited source;
3. final novelty wording check against the frozen theorem statements;
4. journal-format page/figure budget;
5. final referee-style manuscript audit.

# Agent access and handoff

## Canonical repository

**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Branch:** `main`

```bash
git clone https://github.com/maximilianolucius/fractional-d-stability-networks.git
cd fractional-d-stability-networks
git checkout main
git pull --ff-only
git rev-parse HEAD
```

## CURRENT CHIEF STATUS — 2026-09-24

The broad novelty phase is complete enough to stop exploratory reframing.

The project now has a provisional theorem package:

- **C-07:** exact 2x2 classification; analytic proof.
- **C-09:** minimum dimension for nonempty full-dimensional genuinely fractional D-stability is 3 for every 0<alpha<1; analytic proof; targeted novelty audit survived.
- **C-10:** exact variational 3x3 characterization on the full-dimensional strict-P(-A) stratum; analytic proof; targeted novelty search survived provisionally.
- **C-11:** exact orbit minimum Phi and a simple fractional Cain sufficient certificate; analytic proof; C-10 proves Phi is not necessary.
- **C-12/C-13:** GLV abundance invariance and exact ecological loop-coordinate interpretation.

## NEXT AGENT ROLE: ADVERSARIAL PROOF VERIFIER

Do **not** run another broad novelty search first.
Do **not** draft the manuscript.
Do **not** improve the proof before attempting to break it.

Read, in order:

1. `research/PROOF_AUDIT_TASK_C07_C09_C11.md` — despite the filename, it now covers C-07/C-09/C-10/C-11.
2. `research/THEOREM_C10_EXACT_3X3.md`
3. `research/THEOREM_C09_DIMENSION_THRESHOLD.md`
4. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
5. `research/novelty/REOPENED_AUDIT_2026-09-24.md` — C-07.
6. `research/novelty/C09_TARGETED_AUDIT.md`
7. `research/novelty/C10_TARGETED_AUDIT.md`
8. `research/CLAIMS.md`
9. `research/SCOPE_MATRIX.md`
10. `research/research-status.md`

Then inspect:
- `src/fdsn/cubic_certificate.py`
- `tests/test_cubic_certificate.py`

## Proof-audit deliverable

Create:

`research/PROOF_AUDIT_C07_C09_C10_C11.md`

For each C-07, C-09, C-10, C-11 return exactly one:

- `PASS`
- `PASS WITH MINOR FIX`
- `FAIL`

A FAIL must contain a smallest explicit counterexample or identify the exact broken implication.

The proof verifier must independently check:
- all sign conventions;
- boundary/equality cases;
- the all-positive-diagonal quantifier;
- noncompact diagonal-ratio limits;
- the fixed-cubic boundary derivation in C-10;
- the simplex-orbit bijection;
- P0 necessity and strict-P interior necessity;
- recovery of Cain as alpha->1;
- Siami counterfamily showing Phi is not necessary;
- GLV row-scaling invariance.

## Research lock

Until this proof audit passes:

- C-09 and C-10 are **internal theorems**, not submission-certified theorems;
- do not draft final title/abstract/conclusions;
- do not generalize to cactus graphs;
- do not convert numerical sampling into proof.

If the proof audit passes, the next stage is manuscript architecture + one final independent specialist novelty audit.


---

## PARALLEL AGENT ROLE: HIGH-COMPUTE VALIDATION / DISCOVERY

A compute-intensive campaign is now prepared in:

`research/COMPUTE_AGENT_WAVE1_TASK.md`

Dedicated branch:

`agent/compute-c10-wave1-20260925`

This is intentionally a **large bundled assignment**, not a small utility task. The compute agent should execute P0-P4 completely and P5 if resources permit:

- high-precision regression suite;
- robust implementation of the exact C-10 simplex threshold;
- million-scale adversarial validation against direct spectral optimization over the full positive diagonal orbit;
- quantitative gap analysis for the C-11 sufficient certificate;
- ecological motif phase datasets;
- n=4 reconnaissance after the theorem-validation phases.

The compute agent must not edit `paper/`, must not treat finite sampling as proof, and must stop immediately on any persistent counterexample to C-10.

Its required final artifact is:

`research/COMPUTE_WAVE1_FINAL_REPORT.md`

with final status `COMPUTE_PASS`, `COMPUTE_FAIL`, or `PARTIAL/BLOCKED`.

The adversarial proof-verifier lane and compute lane are complementary and may proceed independently. Neither agent should overwrite the other's report.


---

## PARALLEL AGENT ROLE: FINAL SPECIALIST NOVELTY AUDIT

Dedicated branch:

`agent/final-novelty-c10-c15-20260925`

Task:

`research/FINAL_NOVELTY_AUDIT_TASK.md`

Purpose: adversarial theorem-level search for prior art that could subsume or materially narrow C-09/C-10/C-15/C-16. This agent must attempt to kill the novelty claim, not confirm it.

Required final output:

`research/novelty/FINAL_C10_C15_SPECIALIST_AUDIT.md`

with one explicit novelty verdict per claim and one manuscript-level novelty gate verdict.

This lane is independent of both the proof verifier and compute agent.

---

## QUEUED ONLY: COMPUTE WAVE 2

A second server-scale task is prepared in:

`research/COMPUTE_AGENT_WAVE2_QUEUED.md`

**Do not start it yet.**

Start condition: Compute Wave 1 must return `COMPUTE_PASS` with zero genuine C-10 counterexamples and be integrated by the Chief.

Wave 2 is intended for certified atlas generation, robustness analysis, canonical witnesses, C-15 sensitivity validation and publication-grade numerical data. It is not another broad Monte Carlo campaign.


---

## FINAL NOVELTY GATE: PASSED WITH REPOSITIONING

The final specialist novelty branch has been Chief-reviewed and merged.

Canonical final audit:

`research/novelty/FINAL_C10_C15_SPECIALIST_AUDIT.md`

Bibliographic verification:

`research/novelty/FINAL_BIBLIOGRAPHY_VERIFICATION.md`

Final claim status:

- C-09: **NOVEL WITH NARROWED CLAIM**
- C-10: **NOVEL WITH NARROWED CLAIM**
- C-15: **NOVEL WITH NARROWED CLAIM**
- C-16: **NOT NOVEL** as a standalone contribution

The manuscript must position C-10 as an **explicit exact real-3x3 elimination/solution** of the already-known generalized positive-diagonal forbidden-boundary problem for the Matignon reflex sector. It must not claim the first abstract necessary-and-sufficient generalized-D-stability criterion.

Kushel–Pavani are a load-bearing conceptual predecessor; Cain and Bahl–Cain are load-bearing low-dimensional structural predecessors.

Remaining submission gates:

1. Compute Wave 1 final P2 high-precision verdict.
2. Independent adversarial proof audit.
3. Final theorem/citation/sign-convention reconciliation after those gates.

The novelty lane is closed unless a new prior-art collision is discovered.


---

## COMPUTE WAVE 2 — ACTIVE EXECUTION LANE

Branch:

\`agent/compute-wave2-20260925\`

Canonical execution task:

\`research/COMPUTE_AGENT_WAVE2_TASK.md\`

Status:

\`READY TO START\`

Baseline:

\`36b2432d717be7f24ba589b58d6ad7efaabaebd9\`

Wave 1 prerequisite:

\`COMPUTE_PASS\` with zero genuine C-10 counterexamples.

Mission:

- certified threshold atlas;
- canonical genuinely fractional witnesses;
- robustness quantification;
- C-15 differential validation;
- publication-grade figure-source datasets;
- optional focused n=4 shared-edge reconnaissance after P0-P5.

Do not edit \`paper/\` or canonical theorem/novelty/proof files.

P0-P5 are mandatory. P6 is optional.

Final deliverable:

\`research/COMPUTE_WAVE2_FINAL_REPORT.md\`

Final status must be one of:

- \`COMPUTE2_PASS\`
- \`COMPUTE2_FAIL\`
- \`PARTIAL/BLOCKED\`

# Agent access and handoff

## ACTIVE TASK — SECOND INDEPENDENT DOUBLE-ALLEE PROOF AUDIT

**Date:** 2026-09-26  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/independent-proof-double-allee-20260926`  
**Base integration SHA:** `36bf80f2fdaa0c1baa806d064b02b8f26771f8ac`

### Your only active assignment

Read and execute:

`research/SECOND_INDEPENDENT_DOUBLE_ALLEE_PROOF_AUDIT_TASK.md`

This is the **second independent proof audit** of the Double-Allee Kolmogorov / intraguild-predation theorem package.

It is intentionally different from the first compute audit.

### Independence requirement

During the BLIND phase, do **not** read or reuse:

- `research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`
- `research/CHIEF_REVIEW_DOUBLE_ALLEE_AUDIT1_2026-09-26.md`
- `computations/results/DOUBLE_ALLEE_SYMBOLIC_AUDIT.json`
- `computations/results/DOUBLE_ALLEE_ADVERSARIAL_SUMMARY.json`
- `computations/results/DOUBLE_ALLEE_INTERVAL_BOX.json`
- `computations/results/DOUBLE_ALLEE_WORST_CASES.csv`
- `tests/test_double_allee.py`
- `src/fdsn/double_allee.py`
- first-audit Double-Allee scripts.

First produce and commit:

`research/DOUBLE_ALLEE_PROOF_AUDIT2_BLIND_VERDICTS.md`

Only after that may you unblind and compare against Audit 1.

### Primary theorem sources

Read:

1. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
2. `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
3. `research/THEOREM_C10_EXACT_3X3.md`
4. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
5. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`
6. `research/THEOREM_C13_ECOLOGICAL_LOOP_COORDINATES.md`

### Required final deliverables

At minimum:

- `research/DOUBLE_ALLEE_PROOF_AUDIT2_BLIND_VERDICTS.md`
- `research/DOUBLE_ALLEE_PROOF_AUDIT2_FINAL.md`
- `computations/audit2/double_allee_proof_checks.py`
- `computations/audit2/DOUBLE_ALLEE_AUDIT2_RESULTS.json`

Final overall status must be exactly one of:

- `PROOF_AUDIT2_PASS`
- `PROOF_AUDIT2_PASS_WITH_FIXES`
- `PROOF_AUDIT2_FAIL`
- `PARTIAL/BLOCKED`

### Stop-the-line rule

A genuine counterexample to DA-06, DA-07, DA-08, DA-09, DA-10 or DA-11 has priority over all remaining work and must be reported immediately.

Do not repair the Chief theorem silently.

### Repository restrictions

Do not modify:
- `paper/`;
- Chief theorem/report files;
- novelty audit files;
- Audit 1 artifacts.

Do not merge to main.

At completion push this branch and report:
- branch;
- final SHA;
- DA-01…DA-12 verdicts;
- overall status;
- checks/tests run;
- artifact paths;
- any disagreement with Audit 1.

---

## Historical tasks — NOT ACTIVE HERE

The following are prior project lanes and must not be executed on this branch:

- `research/COMPUTE_AGENT_DOUBLE_ALLEE_PROOF_AUDIT_TASK.md`
- `research/PROOF_AUDIT_TASK_C07_C09_C11.md`
- `research/COMPUTE_AGENT_WAVE1_TASK.md`
- `research/COMPUTE_AGENT_WAVE2_QUEUED.md`
- `research/FINAL_NOVELTY_AUDIT_TASK.md`

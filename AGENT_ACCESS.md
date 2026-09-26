# Agent access and handoff

## ACTIVE TASK — 2026-09-26

**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/compute-double-allee-proof-audit-20260926`  
**Base Chief branch:** `chief/double-allee-kolmogorov-20260926`  
**Base Chief SHA:** `ba67d678f54e3b906a85ac4c4e0c69e412c827dd`

### Your only active assignment

Read and execute:

`research/COMPUTE_AGENT_DOUBLE_ALLEE_PROOF_AUDIT_TASK.md`

This is an **independent adversarial proof audit + symbolic verification** of the new Double-Allee 3D Kolmogorov / intraguild-predation theorem package.

Do not run the older C-10 Compute Wave 1 or Wave 2 tasks on this branch.

Do not modify `paper/`.

Do not improve the Chief proof before attempting to break it.

A genuine counterexample has priority over all remaining work.

### Primary sources to audit

1. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
2. `research/DOUBLE_ALLEE_KOLMOGOROV_CHIEF_REPORT.md`
3. `research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md`
4. `research/THEOREM_C10_EXACT_3X3.md`
5. `research/THEOREM_C11_FRACTIONAL_CAIN_CERTIFICATE.md`
6. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`

### Required final deliverable

`research/DOUBLE_ALLEE_PROOF_AUDIT_FINAL.md`

with verdicts for DA-01 through DA-12 and one overall status:

- `COMPUTE_AUDIT_PASS`
- `COMPUTE_AUDIT_PASS_WITH_FIXES`
- `COMPUTE_AUDIT_FAIL`
- `PARTIAL/BLOCKED`

At completion push this branch and report:
- branch name;
- final SHA;
- exact test count;
- DA-01…DA-12 verdict table;
- decisive artifact paths.

---

## Historical context — previous agent lanes

The following tasks remain part of project history but are **not active on this branch**:

- `research/PROOF_AUDIT_TASK_C07_C09_C11.md`
- `research/COMPUTE_AGENT_WAVE1_TASK.md`
- `research/COMPUTE_AGENT_WAVE2_QUEUED.md`
- `research/FINAL_NOVELTY_AUDIT_TASK.md`

Their branches and outputs should be treated as prior evidence only. Do not overwrite them.

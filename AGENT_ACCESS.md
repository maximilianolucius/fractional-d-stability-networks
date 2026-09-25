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

# Agent access and handoff

## Canonical repository

**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Public URL:** `https://github.com/maximilianolucius/fractional-d-stability-networks`

\`\`\`bash
git clone https://github.com/maximilianolucius/fractional-d-stability-networks.git
cd fractional-d-stability-networks
git checkout main
git pull --ff-only
git rev-parse HEAD
\`\`\`

## CURRENT CHIEF STATUS

**NOVELTY AUDIT IS REOPENED as of 2026-09-24.**

The audit in commit `0b3b4df394eceec0dc9951a33fda01560de2f731` is baseline evidence, not the final novelty verdict.

The next novelty agent must read, in this order:

1. `research/CHIEF_RESEARCH_DIRECTION_2026-09-24.md`
2. `research/NOVELTY_AGENT_TASK.md`
3. `research/NOVELTY_REPORT.md`
4. `research/NOVELTY_MATRIX.md`
5. `research/CLAIMS.md`
6. `research/SCOPE_MATRIX.md`
7. `research/novelty/novelty-audit.md`
8. `agent_directives_publishable_first_submission.md`
9. `README.md`

## Mandatory reopened-audit references

- Siami, arXiv:2011.04204 / IEEE TCNS — fractional cyclic-network secant condition.
- Kushel, LAA 656 (2023), DOI 10.1016/j.laa.2022.09.018 / arXiv:2205.10823 — relative D-stability and sector gap.
- Abed, Systems & Control Letters 7(3) (1986), DOI 10.1016/0167-6911(86)90116-7 — strong D-stability.
- Kushel 2019 and Kushel–Pavani 2020/2021.

## Research lock

Until the reopened audit is complete:

- single-cycle/cactus novelty is NOT approved;
- uniform angular-margin novelty is NOT approved;
- openness/robustness novelty is NOT approved;
- C-02 remains motivation only;
- no title or abstract may claim C-04/C-05/C-06 as proved or novel.

The sampler in `src/fdsn/d_stability.py` is counterexample hunting only.

## Required final verdict

The next agent must update the research files, create `research/novelty/REOPENED_AUDIT_2026-09-24.md`, and return exactly one research verdict:

- `GO`
- `GO-NARROWED`
- `NO-GO/REFRAME`

The criterion is theorem-level novelty.

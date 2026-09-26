# Agent access and handoff

## ACTIVE TASK — COMPUTE FIGURE WAVE 2

**Date:** 2026-09-26  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/compute-figures-wave2-20260926`  
**Base Chief visual-review SHA:** `289b81a61d0a2528f1a30708b5f5102ccaaf0081`

### Your only active assignment

Read and execute:

`research/COMPUTE_AGENT_FIGURE_WAVE2_TASK.md`

Read first:

1. `research/CHIEF_VISUAL_REVIEW_WAVE1_2026-09-26.md`
2. `research/FIGURE_MASTERPLAN.md`
3. `research/FIGURE_STYLE_GUIDE.md`
4. `research/PAPER_BAGGAGE_CAPUTO_DOUBLE_ALLEE_3D.md`
5. `research/FIGURE_WAVE1_FINAL_REPORT.md`
6. `research/FIGURE_DATA_REGISTRY.md`
7. `research/FIGURE_CAPTIONS_DRAFT.md`
8. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`

### Mission

Wave 1 passed.

Wave 2 is only for:
- biological re-embedding search;
- figure refinement;
- page-economy redesign;
- final visual QA.

Do not discover or modify theorem claims.

### Highest priorities

1. Find a less scale-separated biological witness if this can be done without weakening robustness.
2. Keep FIG-03 and FIG-06 as flagship theorem figures.
3. Redesign FIG-07 to at most 3 panels.
4. Replace the blocky FIG-08(b) grid aesthetic with mathematically faithful smooth boundary tracing.
5. Simplify FIG-04 and FIG-05.

### Biological witness selection

The current m=0.35 witness is a valid fallback.

A new witness is preferred only if:
- strict-P and C-10 classification remain strong;
- the m-driven crossing remains exact/local with all other parameters fixed;
- certification is possible;
- coexistence density separation is materially reduced.

Internal visualization targets:
- Y/X >= 1e-2;
- Z/X >= 1e-2;
- max/min density ratio <100 if possible.

These are not empirical realism claims.

### Fixed visual palette

- Fractional / Matignon: `#1F4E79`
- Classical / Cain / Hurwitz: `#D97A00`
- Biological admissible / realized: `#2A7F62`
- No-go / excluded / unstable: `#B14E3A`
- Neutral dark: `#5C6770`
- Neutral light: `#D9DDE3`

Do not change semantic assignments.

### No supplementary material

The paper has a hard 25-page limit and no supplementary material.

Do not recommend moving figures to a supplement.

If a panel is not worth main-text space, recommend omitting it.

### Required final artifacts

At minimum:

- `research/FIGURE_WAVE2_REEMBEDDING_REPORT.md`
- `research/FIGURE_FINAL_SET_RECOMMENDATION.md`
- `research/FIGURE_WAVE2_FINAL_REPORT.md`
- `computations/figures_wave2/`
- `tests/test_figures_wave2.py`

### Repository restrictions

Do NOT modify:
- `paper/`
- theorem files
- `research/CLAIMS.md`
- novelty conclusions
- main

Do not merge.

### Final status

Return exactly one:

- `FIGURE_WAVE2_PASS`
- `FIGURE_WAVE2_PASS_WITH_FIXES`
- `FIGURE_WAVE2_FAIL`
- `PARTIAL/BLOCKED`

At completion push the branch and report:
- branch;
- final SHA;
- tests;
- old vs new anchor;
- final figure inventory;
- recommended 6–7 figure environments;
- remaining visual caveats.

---

## Historical tasks — NOT ACTIVE

Figure Wave 1 and all previous proof/compute audits are historical context only. Do not re-run them except as required for comparison.

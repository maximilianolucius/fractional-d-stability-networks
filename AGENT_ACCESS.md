# Agent access and handoff

## ACTIVE TASK — COMPUTE FIGURE WAVE 1

**Date:** 2026-09-26  
**Repository:** `maximilianolucius/fractional-d-stability-networks`  
**Work branch:** `agent/compute-figures-wave1-20260926`  
**Base Chief SHA:** `b5a6ebce3fd0ccf33b2245822dbd414a56a4bf61`

### Your only active assignment

Read and execute:

`research/COMPUTE_AGENT_FIGURE_WAVE1_TASK.md`

Before coding, read:

1. `research/FIGURE_MASTERPLAN.md`
2. `research/FIGURE_STYLE_GUIDE.md`
3. `research/PAPER_BAGGAGE_CAPUTO_DOUBLE_ALLEE_3D.md`
4. `research/Q1_PAPER_ARCHITECTURE.md`
5. `research/THEOREM_C10_EXACT_3X3.md`
6. `research/THEOREM_C15_THRESHOLD_GEOMETRY.md`
7. `research/THEOREM_DOUBLE_ALLEE_KOLMOGOROV_EXTENSION.md`
8. `research/DOUBLE_ALLEE_INTERVAL_CERTIFICATE.md`
9. `research/CLAIMS.md`

### Mission

Produce the reproducible computational and publication-quality visual assets for the manuscript.

This is a figure-production/certification lane, not theorem discovery.

You must produce FIG-01 through FIG-08 in:
- PDF;
- SVG;
- PNG preview;

with:
- source scripts;
- source data;
- metadata;
- caption drafts;
- evidence labels.

### Fixed visual semantics

Use exactly:

- Fractional / Matignon: `#1F4E79`
- Classical / Cain / Hurwitz: `#D97A00`
- Biological admissible / realized: `#2A7F62`
- No-go / excluded / unstable: `#B14E3A`
- Neutral dark: `#5C6770`
- Neutral light: `#D9DDE3`

Do not invent alternative semantic colors.

### Key scientific priorities

Highest-priority figures:

1. FIG-03 exact C-10 threshold geometry;
2. FIG-06 Double-Allee m-path / Cain-to-Matignon crossing;
3. FIG-07 robust certified biological anchor;
4. FIG-05 ecological no-go vs IGP signed-cycle mechanism.

### Certified anchor

Do not use m=0.21 as the principal manuscript anchor unless the purpose is specifically the boundary crossing.

Search within the already certified region, preferably around:

`m in [0.30,0.40]`

and return three candidate anchors plus one recommended manuscript point.

### Evidence discipline

Never use finite diagonal sampling as proof.

Classify every plotted object as:
- EXACT THEOREM CURVE
- CLOSED-FORM BOUNDARY
- CERTIFIED INTERVAL
- CERTIFIED COMPUTATION
- NUMERICAL CORROBORATION
- SCHEMATIC

### Required final artifacts

At minimum:

- `research/FIGURE_DATA_REGISTRY.md`
- `research/FIGURE_CAPTIONS_DRAFT.md`
- `research/FIGURE_WAVE1_FINAL_REPORT.md`
- `computations/figures/scripts/`
- `computations/figures/data/`
- `computations/figures/exports/pdf/`
- `computations/figures/exports/svg/`
- `computations/figures/exports/png/`
- `computations/figures/metadata/`

### Repository restrictions

Do NOT modify:
- `paper/`
- theorem files
- `research/CLAIMS.md`
- novelty conclusions
- main

Do not merge.

You may add namespaced plotting utilities/tests if needed.

### Final status

Return exactly one:

- `FIGURE_WAVE1_PASS`
- `FIGURE_WAVE1_PASS_WITH_FIXES`
- `FIGURE_WAVE1_FAIL`
- `PARTIAL/BLOCKED`

At completion push the branch and report:
- branch;
- final SHA;
- tests passed/failed;
- figure inventory;
- selected robust anchor;
- theorem-grade vs illustration-grade classification;
- unresolved numerical/visual issues;
- recommended main-paper subset.

---

## Historical tasks — NOT ACTIVE

All previous Double-Allee proof audits and C-10 compute/proof waves are historical context only. Do not execute them on this branch.

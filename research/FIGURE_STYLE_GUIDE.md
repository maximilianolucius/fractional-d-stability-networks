# Figure Style Guide — Fractional D-Stability Networks

**Date:** 2026-09-26  
**Applies to:** all manuscript-bound figures

## Canonical palette

| Semantic role | Hex |
|---|---|
| Fractional / Matignon | \`#1F4E79\` |
| Classical / Cain / Hurwitz | \`#D97A00\` |
| Biological admissible / realized | \`#2A7F62\` |
| No-go / excluded / unstable | \`#B14E3A\` |
| Neutral dark | \`#5C6770\` |
| Neutral light | \`#D9DDE3\` |

Do not change semantic color assignments between figures.

## Background

White only for final exports.

## Fonts

Use a publication-safe serif/sans-serif combination consistent with LaTeX rendering.

Preferred:
- math: LaTeX/STIX-like;
- plot labels: DejaVu Sans / STIX / Liberation Sans depending availability.

Do not embed proprietary fonts.

## Figure widths

Prepare at minimum:
- single-column target: ~85–90 mm;
- double-column target: ~175–180 mm.

Every figure should be tested at both widths where plausible.

## Vector-first rule

Preferred export order:
1. PDF
2. SVG
3. PNG preview

Never use screenshots as final figures.

## Mathematical notation

Use the same notation as the theorem files:
- \(\alpha\);
- \(\beta_{12},\beta_{13},\beta_{23}\);
- \(\kappa\);
- \(T_\alpha\);
- \(T_1\);
- \(L_3\);
- \(m\);
- \(s=-g'_{DA}(X)\).

No alternative symbols in figure code.

## Gridlines

Default: none.

If needed:
- very light;
- sparse;
- never dominate the data.

## Spines

Reduce visual weight.
Avoid boxed axes unless structurally useful.

## Legends

Prefer direct labels.
When a legend is needed:
- compact;
- no opaque heavy frame;
- outside data region if possible.

## Colormaps

Do not use rainbow/jet.

For continuous scalar fields:
- use a perceptually uniform sequential map;
- but theorem/class boundaries must still use the canonical semantic palette.

## 3D surfaces

Avoid 3D perspective when a contour/slice/heatmap conveys the theorem more clearly.

If a 3D surface is unavoidable:
- add a 2D contour companion;
- use shallow perspective;
- no glossy lighting;
- no decorative mesh clutter.

## Network diagrams

Use:
- simple circular nodes;
- arrows with clear direction;
- interaction signs or labels;
- canonical colors only when they encode theorem semantics.

Do not imitate infographic styles.

## Captions

Each caption should answer:
1. what is plotted?
2. what theorem does it support?
3. which elements are exact/certified/numerical?
4. what should the reader notice?

Avoid captions that merely restate axis labels.

## File hygiene

Each script must:
- run headlessly;
- save deterministic outputs;
- use fixed random seeds if randomness is present;
- avoid absolute local paths;
- record parameters in a JSON/YAML companion where useful.

## Reproducibility

Every figure must be regenerable from a clean clone with one documented command.

If a figure requires expensive computation:
- cache source data in \`computations/figures/data/\`;
- keep a verification hash or metadata record;
- separate data generation from rendering.

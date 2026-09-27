# Computation workspace

This directory is reserved for reproducible numerical/certified computation supporting the theorem programme.

## Rules

- Computation is corroboration unless an explicit rigorous certificate is produced.
- Finite diagonal sampling never proves D-stability.
- Large raw datasets should not be committed; commit compact summaries, worst cases, scripts, seeds, and checksums.
- Every result used in a figure must be reproducible from a committed script and recorded parameter file.

## Full nonlinear Caputo case study

The applied manuscript comparison is reproduced in two stages:

```bash
PYTHONPATH=src python3 computations/figures_wave2/scripts/nonlinear_caputo_simulation.py
PYTHONPATH=src python3 computations/figures_wave2/scripts/fig09_nonlinear_caputo_dynamics.py
```

The first command integrates the complete row-scaled W2-A ecological model at
`alpha=0.9`, performs a nested-step PECE refinement study, and integrates the
same model at `alpha=1` with DOP853 until the declared local-neighborhood exit.
The committed canonical run was executed on Aureus (`aur007`); software
versions and all quantitative diagnostics are recorded in
`figures_wave2/data/nonlinear_caputo_summary.json`.

The exact theorems and interval certificates do not depend on this trajectory
calculation. It is an applied numerical illustration of the local spectral
classification.

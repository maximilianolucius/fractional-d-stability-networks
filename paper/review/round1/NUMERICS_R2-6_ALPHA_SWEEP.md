# R2-6 — additional fractional orders near the stability boundary (agent numerics, 2026-10-16)

**Branch** `agent/review-round1-numerics-20261016` (on top of the Chief's `chief/revision-round1-20261016`, `889588e`). Computations on **orion** (344 cores): base sweep 23 runs (16 workers), dense sweep 340 runs (320 workers, 233 s wall).

## What was run

Full nonlinear W2-A Caputo model, same parameters, same initial perturbation u(0) = u* ⊙ (1 + 10⁻³(1,−1,1)), two positive row scalings:
- **R\_\*** = D\_\* diag(u\*)⁻¹ (the diagonal of the spectral search; R\_\*J = D\_\*B), orders α = 0.700 … 1.000 every 0.001 plus the base grid (308 runs);
- **R = I** (unscaled Jacobian J = diag(u\*)B, Hurwitz stable), α = 0.70 … 1.00 every 0.01 (32 runs).

Fractional Adams–Bashforth–Moulton PECE (`src/fdsn/caputo.py`, now with an optional early stop at the declared radius 0.2), steps h = 0.02 and 0.01 (refinement recorded per run), horizon t = 600, extended to t = 2000 for |α − α\*| < 0.02. At α = 1 an independent DOP853 run is also recorded. Script: `computations/figures_wave2/scripts/alpha_sweep_nonlinear.py`; data: `computations/figures_wave2/data/alpha_sweep{,_dense}_summary.json`, `alpha_sweep_timeseries.csv`; figure: `fig10_alpha_sweep`.

## Results (evidenced)

- Theorem boundary order for this realization: **α\* = 0.9505501071** (root of T\_α(β) = κ). It equals (2/π)·min|arg λ(D\_\*B)| to 10 digits, i.e. the searched diagonal is exactly the extremal one.
- Late growth rate of ‖u/u\* − 1‖₂ changes sign **between α = 0.9500 (−0.51·10⁻³) and α = 0.9506 (+0.05·10⁻³)**, the 0.001-grid cell containing α\*. Every run with α ≥ 0.953 leaves the radius 0.2 (exit time 1955 at 0.953 down to 101.6 at α = 1; DOP853 at α = 1: 101.586). Every unscaled run decays.
- Linear prediction (sign of the angular margin) vs observation: 339/340 agree on the "final distance below initial distance" criterion. The single disagreement is α = 0.9506 (margin −8·10⁻⁵ rad): its late rate is already positive (+4.6·10⁻⁵) but the transient has not yet regained the initial distance by t = 2000. This is a finite-horizon effect, not a contradiction.

| α | angular margin (rad) | t\_end | final distance | exit time | late rate (×10⁻³) |
|---|---|---|---|---|---|


## The Chief's t = 180 table (reproduced, but misleading as written)

`order_sweep_round1.py` was rerun on orion: all 12 values agree to the printed digits (e.g. α = 0.950: 8.3838·10⁻⁴; α = 0.955: 2.1087·10⁻³). However d(180) **increases with α already below α\*** (0.930 → 6.5·10⁻⁵, 0.945 → 4.7·10⁻⁴, 0.950 → 8.4·10⁻⁴) only because decay is slower near the boundary; at t = 180 every listed order, including 0.955 and 0.965 (above α\*), still has a distance of order 10⁻³–10⁻² and none has left a neighbourhood. The table therefore does not show the transition; it shows slowing. **Recommendation:** replace it by the long-horizon quantities above (sign of the late rate / exit time), or by Fig. 10, and keep the sentence that finite-time runs corroborate but do not prove.

## Other fixes on this branch

1. **Compilation blocker fixed.** The submitted and revised `main.tex` had `\Author{{Ibrahim Alraddadi^*}` (superscript outside math). With `-halt-on-error` the build stopped with "Missing $ inserted" at `\begin{document}`; the submitted PDF shows the artefact ("Alraddadi∗ 1 \*"). Replaced by `\Author{Ibrahim Alraddadi $^{1,*}$}`. Revised PDF now builds: **28 pages, 0 overfull boxes, 0 undefined references/citations.**
2. **Internal claim labels removed from figure artwork (R1-7).** The only labels left in the compiled PDF came from fig02 ("n = 2 (C-07)", "n = 3 (C-09/C-10)") and fig03 ("exact C-10"). Both figures were regenerated with neutral wording; `pdftotext` of the rebuilt PDF finds **0** occurrences of C-xx. The build script now overlays `revised-source/figures/*.pdf` on the original zip.
3. **Fig. 10 added** to `revised-source/figures/` (not yet referenced in the text; the Chief decides placement/caption).

P4 — ecological motif phase-diagram datasets (C-13 coordinates).

Theorem-illustration data (exact boundaries evaluated numerically; a subset of
anchor values is CERTIFIED in P1).  Plot-ready CSVs are written to
computations/results/C13_PHASE_DATA/, figures to .../figures/ (separate).

Coordinates: g_ij = a_ij a_ji/(p_i p_j), beta_ij = 1 - g_ij,
             kappa = sum(beta) - 2 - L3.
Regions on the strict-P stratum (kappa > 0 <=> L3 < sum(beta) - 2):
  CLASSICAL  : kappa < T1              <=> L3 > sum(beta) - 2 - T1
  FRACTIONAL : T1 < kappa < T_alpha    (genuinely fractional band; alpha <= 2/3: T_alpha = inf)
  UNSTABLE   : kappa > T_alpha
Real realizability: L3 = l + G/l with G = g12 g13 g23, hence L3^2 >= 4G if G > 0.

Files
  L3_alpha_<name>.csv   : alpha, T1, T_alpha, W, L3_kappa0, L3_cain, L3_frac, realizability
  pairloop_alpha<a>_g23<g>.csv : g12, g13 grid, T1, T_alpha, W, W/T1, L3 bounds
  width_asymptotics.csv : W vs alpha for the named triples + C(beta)(1-alpha) and 27/K^3
  symmetric_width.csv   : W along beta12=beta13=beta23=b (antagonistic b>1 vs mutualistic b<1)
  direct_validation.json: independent direct-margin classification of sampled points per region

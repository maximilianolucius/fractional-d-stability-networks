# Compute Wave 1 — live status / handoff

Branch `agent/compute-c10-wave1-20260925`. Updated at every commit. Anyone can resume from here.

## Where things run
- Server: aureus (`~/fdsn_wave1/repo` = rsync of this working tree, venv `~/fdsn_wave1/venv`,
  logs `~/fdsn_wave1/logs/`). Raw arrays in `computations/raw/` (NOT committed; checksums go in results).
- Good-neighbour settings: `FDSN_WORKERS=16`, `OMP_NUM_THREADS=1`, `nice -n 5`.
- Env: `python3 -m venv venv && venv/bin/pip install -e .[dev] numba sympy`.

## Phase status
| Phase | Status | Command | Outputs |
|---|---|---|---|
| P0 | DONE | `pytest -n 8` | tests/test_high_precision.py, tests/test_c10_numerics.py, results/ENVIRONMENT.json |
| P1 | DONE | `python computations/scripts/p1_threshold_validation.py` then `symbolic_checks.py` | results/P1_THRESHOLD_VALIDATION.json, P1_CERTIFIED_ANCHORS.csv, SYMBOLIC_CHECKS.json |
| P2 float | RUNNING (started 12:12 aureus time, ~1 h) | `python computations/scripts/p2_stress.py` | raw/p2_*.npz, results/P2_RAW_INDEX.json |
| P2 HP | NEXT | `python computations/scripts/p2_hp_verify.py` | results/C10_STRESS_SUMMARY.json, C10_WORST_CASES.csv |
| P3/P3B | TODO | (scripts to be added) | C11_GAP_SUMMARY.csv, C14_LIMIT_RATE.csv |
| P4 | TODO | | C13_PHASE_DATA/ |
| P5 | TODO | | N4_RECON_REPORT.md |
| Final report | TODO | | research/COMPUTE_WAVE1_FINAL_REPORT.md |

## Findings so far (labels: NUMERICAL / CERTIFIED / PROOF SKETCH)
1. No genuine C-10 mismatch in pilot runs (3.3k cases) nor so far in P2. Float "mismatches" seen in a pilot were
   rounding artefacts: eigenvalues with |lambda| ~ 1e-14 ||DA|| at diagonal ratios ~e^32 got a spurious sign.
   Fixed by a reliability filter (exclude |lambda| < 1e-10 max|lambda|) + mp audit of extreme scalings.
2. PROOF SKETCH (+ sympy + 1.28M-point numerics): in logit coordinates y (x = softmax(y1,y2,0)) the objective
   G = log h_alpha(B(x)) - sum log x_i is STRICTLY CONVEX. Proof: G = phi(Q-2L) + 3L - sum y with
   Q = log sum beta_ij e^{y_i+y_j}, L = logsumexp(y), phi(s) = log h(e^s); phi' = elasticity
   E = (Kr-2u)(1+3ur)/((Kr-u)(1+2ur)) is increasing in r with range (0, 3/2), so
   Hess G >= phi'' grad s grad s^T + phi' Hess Q + (3-2phi') Hess L > 0. => unique minimizer, T_alpha is a
   convex program; nondegeneracy needed in C-14 is automatic.
3. Consequences: fully symmetric beta => x* = centre, closed form T_alpha(b,b,b) = 27 h_alpha(b/3);
   b = 1 reproduces 1 + R3^3 (sympy identity in theta). beta12 = beta13 => x2* = x3*.
4. alpha -> 2/3+: T_alpha = 27/K^3 + (9 sum beta - 27)/K^2 + O(1/K), K = 1-4cos^2(alpha pi/2) (HP to 6e-8).
5. 60/60 anchor values of T_alpha CERTIFIED by interval branch-and-bound (rel. width ~1e-39).
6. Realizability: every (beta, kappa) with kappa >= T1(beta) is realized by a real matrix (ell123 ell132 = G).

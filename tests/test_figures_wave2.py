"""Deterministic checks behind the Figure-Wave-2 figures (NUMERICAL CORROBORATION of exact formulas; the certified
statements are those recorded in computations/figures_wave2/data/design_selected.json)."""
import json
import os
import sys

import mpmath as mp
import numpy as np

ROOT = os.path.join(os.path.dirname(__file__), "..")
W2 = os.path.join(ROOT, "computations", "figures_wave2")
sys.path.insert(0, os.path.join(W2, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "computations", "scripts"))
from design_tools import ALPHA, classify_pt, crossing_hp, params_from_design, point  # noqa: E402
from fdsn.double_allee import PARAM_NAMES, Params, invariants_of_matrix, prey_roots, reduced_matrix, with_m, yz_of_x  # noqa: E402

SEL = json.load(open(os.path.join(W2, "data", "design_selected.json")))


def test_selected_reembedding_is_feasible_positive_strictP_with_positive_margins():
    P, (X, Y, Z) = params_from_design(SEL["design"])
    pars = dict(zip(PARAM_NAMES, P.as_list()))
    assert all(v > 0 for v in pars.values())
    assert all(0 < pars[e] < 1 for e in ("e1", "e2", "e3"))
    assert X > 0 and Y > 0 and Z > 0 and Y / X >= 1e-2 and Z / X >= 1e-2 and max(X, Y, Z) / min(X, Y, Z) < 30
    r = point(P, SEL["anchor_m"])
    assert r["strictP"] and r["n_eq"] == 1
    assert r["kappa"] - r["T1"] > 0.10 * r["T1"] and r["T_alpha"] - r["kappa"] > 0.20 * r["T_alpha"]
    assert abs(r["kappa"] - SEL["anchor"]["kappa"]) < 1e-9 and abs(r["T_alpha"] - SEL["anchor"]["T_alpha"]) < 1e-7


def test_local_m_crossing_exists_with_correct_signs():
    P, _ = params_from_design(SEL["design"])
    m0 = float(SEL["m0_hp"]); mC = SEL["classical_m"]; mA = SEL["anchor_m"]
    assert mC < m0 < mA
    for m, sign in ((mC, -1), (m0 - 0.01, -1), (m0 + 0.01, 1), (mA, 1)):
        r = point(P, m)
        assert r["strictP"] and sign * (r["kappa"] - r["T1"]) > 0 and r["kappa"] < r["T_alpha"]
    # unique sign change of G1 on the strict-P part of the branch (all non-m parameters fixed)
    G = []
    for m in np.arange(0.01, SEL["feasible_range"][1] - 1e-9, 0.005):
        r = point(P, float(m))
        if r and r["strictP"]:
            G.append(r["kappa"] - r["T1"])
    assert np.count_nonzero(np.diff(np.sign(G))) == 1


def test_fig06_exact_crossing_m0_to_fifty_digits():
    with mp.workdps(60):
        P, _ = params_from_design(SEL["design"], mp.mpf)
        Pq = with_m(P, mp.mpf(SEL["m0_hp"]))
        X = max(prey_roots(Pq)); Y, Z = yz_of_x(X, Pq)
        I = invariants_of_matrix(reduced_matrix(X, Y, Z, Pq)); b = I["beta"]
        assert abs(I["kappa"] - (mp.sqrt(b[0]) + mp.sqrt(b[1]) + mp.sqrt(b[2])) ** 2) < mp.mpf(10) ** -48
    m0_re, _ = crossing_hp(SEL["design"], float(SEL["m0_hp"]) - 1e-3, float(SEL["m0_hp"]) + 1e-3)
    assert abs(mp.mpf(m0_re) - mp.mpf(SEL["m0_hp"])) < mp.mpf(10) ** -40


def test_certified_records_are_consistent_with_exact_evaluation():
    ci = SEL["certified_m_interval"]
    assert ci["fully_certified"] and ci["attempted"][0] < SEL["anchor_m"] < ci["attempted"][1]
    assert ci["min_kappa_minus_T1_lo"] > 0 and ci["min_T_alpha_L_minus_kappa_hi"] > 0
    P, _ = params_from_design(SEL["design"])
    for k, c in SEL["certified_points"].items():
        assert c["ok"] is True
        r = point(P, float(k))
        assert r["kappa"] - r["T1"] >= float(c["kappa_minus_T1_lo"]) - 1e-9
        assert r["T_alpha"] - r["kappa"] >= float(c["T_alpha_L_minus_kappa_hi"]) - 1e-9


def test_fig08_traced_boundaries_separate_the_classes_on_both_sides():
    cur = json.load(open(os.path.join(W2, "data", "fig08_traced_boundaries.json")))
    P, _ = params_from_design(SEL["design"])
    d = 2e-3
    for K, m in cur["classical_fractional"][::10]:
        assert classify_pt(P, m - d, K) == 0 and classify_pt(P, m + d, K) == 1
    for K, m in cur["fractional_unstable"][::10]:
        assert classify_pt(P, m - d, K) == 1 and classify_pt(P, m + d, K) == 2
    for K, m in cur["feasibility_high"][::10]:
        assert classify_pt(P, m - d, K) < 3 and classify_pt(P, m + d, K) == 3
    K0 = params_from_design(SEL["design"])[0].K
    mb = np.interp(K0, [p[0] for p in cur["classical_fractional"]], [p[1] for p in cur["classical_fractional"]])
    assert abs(mb - float(SEL["m0_hp"])) < 1e-3


def test_all_wave2_exports_exist():
    for name in ("fig01_matignon_hurwitz", "fig03_threshold_geometry", "fig04_alpha_deformation", "fig04c_low_order_asymptotic",
                 "fig05_ecological_mechanism", "fig06_double_allee_m_path", "fig07_certified_anchor", "fig08_double_allee_2d_3d"):
        for ext in ("pdf", "svg", "png"):
            assert os.path.exists(os.path.join(W2, "exports", ext, f"{name}.{ext}"))
        meta = json.load(open(os.path.join(W2, "metadata", f"{name}.json")))
        assert "claims" in meta and "objects" in meta

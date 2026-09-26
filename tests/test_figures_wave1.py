"""Deterministic checks of the formulas behind the Figure-Wave-1 figures (NUMERICAL CORROBORATION)."""
import json
import os

import mpmath as mp
import numpy as np
import pytest

from fdsn.c10_threshold import T1, h_alpha, mp_T1, rate_constant, siami_R3, threshold, threshold_batch, threshold_mp
from fdsn.double_allee import chief_witness, coexistence_equilibria, invariants_of_matrix, reduced_matrix, with_m

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA = os.path.join(ROOT, "computations", "figures", "data")


def test_fig03_symmetric_slice_matches_theorem_formulas():
    for alpha in (0.7, 0.8, 0.9):
        for b in (0.2, 1.0, 5.0):
            assert abs(threshold([b, b, b], alpha).T[0] / (27 * h_alpha(b / 3, alpha)) - 1) < 1e-11
        assert abs(27 * h_alpha(1 / 3, alpha) / (1 + siami_R3(alpha) ** 3) - 1) < 1e-12
    beta = np.array([2.0, 1.5, 3.0])
    assert abs(T1(beta) - (np.sqrt(2) + np.sqrt(1.5) + np.sqrt(3)) ** 2) < 1e-13
    assert threshold(beta, 0.9).T[0] > T1(beta)


def test_fig03_certified_anchor_brackets_contain_exact_evaluation():
    cert = json.load(open(os.path.join(DATA, "fig03_certified_anchors.json")))
    for c in cert:
        with mp.workdps(40):
            v = threshold_mp([repr(float(c["b"])), "1.5", "3"], "0.9", dps=35)["T"]
            # L, U are stored to 30 digits (bracket width ~1e-39): compare up to the storage rounding
            assert abs(v / mp.mpf(c["L"]) - 1) < mp.mpf(10) ** -28 and abs(v / mp.mpf(c["U"]) - 1) < mp.mpf(10) ** -28


def test_fig04_monotone_in_alpha_and_asymptotics():
    beta = np.array([0.5, 2.0, 1.5])
    al = np.linspace(0.68, 0.999, 60)
    T = threshold_batch(np.repeat(beta[None], al.size, 0), al).T
    assert np.all(np.diff(T) < 0) and T[-1] > T1(beta)
    eps = 1e-5
    with mp.workdps(40):
        W = threshold_mp([repr(float(v)) for v in beta], 1 - mp.mpf(eps), dps=35)["T"] - mp_T1([mp.mpf(repr(float(v))) for v in beta])
    assert abs(float(W) / (rate_constant(beta) * eps) - 1) < 1e-3


def branch_point(m):
    P = with_m(chief_witness(), m)
    e = coexistence_equilibria(P)[0]
    B = reduced_matrix(e["X"], e["Y"], e["Z"], P)
    I = invariants_of_matrix(B)
    beta = np.array(I["beta"], float)
    return float(I["kappa"]), float(T1(beta)), float(threshold(beta, 0.9).T[0]), e


def test_fig06_m0_is_exact_cain_crossing_and_sign_change():
    with mp.workdps(60):
        from fdsn.double_allee import prey_roots, yz_of_x
        P = chief_witness(lambda v: mp.mpf(v))
        X = max(prey_roots(P)); Y, Z = yz_of_x(X, P)
        I = invariants_of_matrix(reduced_matrix(X, Y, Z, P)); b = I["beta"]
        assert abs(I["kappa"] - (mp.sqrt(b[0]) + mp.sqrt(b[1]) + mp.sqrt(b[2])) ** 2) < mp.mpf(10) ** -50
    k1, t1, _, _ = branch_point(0.12); k2, t2, ta2, _ = branch_point(0.35)
    assert k1 < t1 and t2 < k2 < ta2


def test_fig07_anchor_has_both_strict_margins_and_certification():
    k, t1, ta, e = branch_point(0.35)
    assert k - t1 > 2.5 and ta - k > 20 and e["X"] > 0 and e["Y"] > 0 and e["Z"] > 0
    D = json.load(open(os.path.join(DATA, "branch_alpha0.9.json")))
    c = D["candidates"]["0.35"]["certified"]
    assert c["ok"] is True and float(c["kappa_minus_T1_lo"]) > 2.5 and float(c["T_alpha_L_minus_kappa_hi"]) > 20


def test_fig08_2d_critical_threshold_formula():
    rng = np.random.default_rng(1)
    for _ in range(20):
        X = rng.uniform(0.3, 2); a = np.exp(rng.normal()); K = X + np.exp(rng.normal())
        mc = (X ** 2 + 2 * a * X - K * a) / (K + a)
        assert abs(1 / (K - X) - 1 / (X - mc) + 1 / (X + a)) < 1e-10
        assert abs(mc - (X - (K - X) * (X + a) / (K + a))) < 1e-12


def test_all_figure_exports_exist():
    root = os.path.join(ROOT, "computations", "figures", "exports")
    for i, name in enumerate(["matignon_hurwitz", "dimension_contrast", "threshold_geometry", "alpha_deformation", "ecological_mechanism",
                              "double_allee_m_path", "certified_anchor", "double_allee_2d_3d"], 1):
        for ext in ("pdf", "svg", "png"):
            assert os.path.exists(os.path.join(root, ext, f"fig{i:02d}_{name}.{ext}"))
        assert os.path.exists(os.path.join(ROOT, "computations", "figures", "metadata", f"fig{i:02d}_{name}.json"))

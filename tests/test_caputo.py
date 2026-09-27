import numpy as np

from fdsn.caputo import caputo_pece


def test_caputo_pece_preserves_an_equilibrium():
    initial = np.array([1.0, 2.0, 3.0])
    times, states = caputo_pece(lambda _t, y: np.zeros_like(y), initial, 0.9, 1.0, 0.05)
    assert len(times) == 21
    assert np.all(states == initial)


def test_caputo_pece_converges_for_integer_order_exponential():
    exact = np.exp(-1.0)
    _, coarse = caputo_pece(lambda _t, y: -y, np.array([1.0]), 1.0, 1.0, 0.05)
    _, fine = caputo_pece(lambda _t, y: -y, np.array([1.0]), 1.0, 1.0, 0.025)
    coarse_error = abs(coarse[-1, 0] - exact)
    fine_error = abs(fine[-1, 0] - exact)
    assert fine_error < coarse_error / 3.0

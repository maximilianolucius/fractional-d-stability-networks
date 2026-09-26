#!/usr/bin/env python3
"""Independent numerical checks for the double-Allee IGP extension.

This script is validation only.  The theorems are analytic and do not rely on
finite sampling/optimization.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar


ALPHA = 0.9
THETA = ALPHA * math.pi / 2.0

# Construction chosen so m0=0.2 lies exactly on the classical Cain boundary.
RATE_SCALE = 0.05
ETA = 0.5
A0_NORM = 1.0
B0_NORM = 1.0
C0_NORM = 1.0
E0_NORM = 14.0

tau = (E0_NORM + math.sqrt(E0_NORM**2 + 4.0)) / 2.0

e1 = ETA
e3 = ETA
e2 = ETA**2 / tau**2

s0 = RATE_SCALE
c1 = RATE_SCALE
c2 = RATE_SCALE
q1 = RATE_SCALE * math.sqrt(A0_NORM / e1)
q2 = RATE_SCALE * math.sqrt(B0_NORM / e2)
h = RATE_SCALE * math.sqrt(C0_NORM / e3)

# Double-Allee construction.
X0 = 1.0
m0 = 0.2
a = 0.5
K = 1.1

H0 = 1.0 / (K - X0) - 1.0 / (X0 - m0) + 1.0 / (X0 + a)
Q0 = s0 / H0

Y0 = Q0 / (2.0 * q1)
Z0 = Q0 / (2.0 * q2)

mu1 = e1 * q1 * X0 - c1 * Y0 - h * Z0
mu2 = e2 * q2 * X0 + e3 * h * Y0 - c2 * Z0

r = Q0 * (X0 + a) / ((1.0 - X0 / K) * (X0 - m0))

Delta = c1 * c2 + e3 * h**2

chi = (
    e1 * c2 * q1**2
    + e2 * c1 * q2**2
    + h * q1 * q2 * (e1 * e3 - e2)
) / Delta

nu = (
    mu1 * (q1 * c2 + q2 * e3 * h)
    + mu2 * (q2 * c1 - q1 * h)
) / Delta


def g_da(x: float, m: float) -> float:
    return r / (x + a) * (1.0 - x / K) * (x - m)


def g_da_prime(x: float, m: float) -> float:
    g = g_da(x, m)
    return g * (-1.0 / (K - x) + 1.0 / (x - m) - 1.0 / (x + a))


def coexistence_roots(m: float) -> list[float]:
    # (r+K chi) X^2 - [r(K+m)-K chi a+K nu] X + rKm-Knu a = 0.
    A = r + K * chi
    B = r * (K + m) - K * chi * a + K * nu
    C = r * K * m - K * nu * a
    disc = B * B - 4.0 * A * C
    if disc < 0.0:
        return []
    sd = math.sqrt(disc)
    return [(B + sd) / (2.0 * A), (B - sd) / (2.0 * A)]


def yz_from_x(x: float) -> tuple[float, float]:
    A1 = e1 * q1 * x - mu1
    A2 = e2 * q2 * x - mu2
    y = (c2 * A1 - h * A2) / Delta
    z = (e3 * h * A1 + c1 * A2) / Delta
    return y, z


def reduced_matrix(x: float, m: float) -> np.ndarray:
    s = -g_da_prime(x, m)
    return np.array(
        [
            [-s, -q1, -q2],
            [e1 * q1, -c1, -h],
            [e2 * q2, e3 * h, -c2],
        ],
        dtype=float,
    )


def invariants(B: np.ndarray) -> tuple[float, float, float, float]:
    p1, p2, p3 = -B[0, 0], -B[1, 1], -B[2, 2]
    m12 = np.linalg.det(B[np.ix_([0, 1], [0, 1])])
    m13 = np.linalg.det(B[np.ix_([0, 2], [0, 2])])
    m23 = np.linalg.det(B[np.ix_([1, 2], [1, 2])])
    q = -np.linalg.det(B)
    return (
        m12 / (p1 * p2),
        m13 / (p1 * p3),
        m23 / (p2 * p3),
        q / (p1 * p2 * p3),
    )


def h_alpha(b: float) -> float:
    u = math.cos(THETA)
    Ktheta = 1.0 - 4.0 * u * u
    rr = (u + math.sqrt(u * u + Ktheta * b)) / Ktheta
    return rr * rr * (1.0 + 2.0 * u * rr)


def T1(beta: tuple[float, float, float]) -> float:
    return sum(math.sqrt(v) for v in beta) ** 2


def Talpha_two_equal(beta12: float, beta23: float) -> tuple[float, float]:
    # beta12=beta13.  C-15 uniqueness forces x2=x3=t.
    def objective(t: float) -> float:
        x1 = 1.0 - 2.0 * t
        Bcoef = 2.0 * beta12 * x1 * t + beta23 * t * t
        return h_alpha(Bcoef) / (x1 * t * t)

    res = minimize_scalar(
        objective,
        bounds=(1e-12, 0.5 - 1e-12),
        method="bounded",
        options={"xatol": 1e-14},
    )
    return float(res.fun), float(res.x)


def direct_spectral_checks(B: np.ndarray) -> tuple[float, float, np.ndarray, np.ndarray]:
    # Fix d3=1; common positive scaling does not change eigenvalue arguments
    # and cannot change the sign of real parts.
    def min_angle(logd: np.ndarray) -> float:
        d = np.exp([logd[0], logd[1], 0.0])
        ev = np.linalg.eigvals(np.diag(d) @ B)
        return min(abs(np.angle(v)) for v in ev)

    def spectral_abscissa(logd: np.ndarray) -> float:
        d = np.exp([logd[0], logd[1], 0.0])
        ev = np.linalg.eigvals(np.diag(d) @ B)
        return max(v.real for v in ev)

    angle_res = differential_evolution(
        min_angle,
        [(-6.0, 6.0), (-6.0, 6.0)],
        seed=20260926,
        tol=1e-10,
        polish=True,
    )

    real_res = differential_evolution(
        lambda v: -spectral_abscissa(v),
        [(-6.0, 6.0), (-6.0, 6.0)],
        seed=20260927,
        tol=1e-10,
        polish=True,
    )

    return (
        float(angle_res.fun),
        float(-real_res.fun),
        np.exp([angle_res.x[0], angle_res.x[1], 0.0]),
        np.exp([real_res.x[0], real_res.x[1], 0.0]),
    )


def report(m: float) -> None:
    roots = coexistence_roots(m)
    if not roots:
        raise RuntimeError(f"No real coexistence root at m={m}")

    x = max(roots)
    y, z = yz_from_x(x)
    B = reduced_matrix(x, m)

    beta12, beta13, beta23, kappa = invariants(B)
    t1 = T1((beta12, beta13, beta23))
    ta, optimizer = Talpha_two_equal(beta12, beta23)

    min_angle, max_real, d_angle, d_real = direct_spectral_checks(B)

    print(f"m={m:.6f}")
    print(f"  equilibrium = ({x:.15g}, {y:.15g}, {z:.15g})")
    print(f"  s=-g'(X)   = {-g_da_prime(x,m):.15g}")
    print(
        "  invariants   = "
        f"({beta12:.15g}, {beta13:.15g}, {beta23:.15g}, {kappa:.15g})"
    )
    print(f"  T1           = {t1:.15g}")
    print(f"  Talpha       = {ta:.15g}")
    print(f"  Talpha optimizer x2=x3 = {optimizer:.15g}")
    print(f"  direct min |arg lambda(DB)| = {min_angle:.15g}")
    print(f"  Matignon theta             = {THETA:.15g}")
    print(f"  direct angular margin      = {min_angle-THETA:.15g}")
    print(f"  max spectral abscissa(DB)  = {max_real:.15g}")
    print(f"  D for min angle            = {d_angle}")
    print(f"  D for max real part        = {d_real}")


if __name__ == "__main__":
    print("Constructed biological parameters")
    print(f"alpha={ALPHA}")
    print(f"q1={q1:.15g}, q2={q2:.15g}, h={h:.15g}")
    print(f"e1={e1:.15g}, e2={e2:.15g}, e3={e3:.15g}")
    print(f"c1={c1:.15g}, c2={c2:.15g}")
    print(f"mu1={mu1:.15g}, mu2={mu2:.15g}")
    print(f"r={r:.15g}, a={a}, K={K}")
    print()

    # m0 is the exact classical threshold by construction.
    for m in (0.19, 0.20, 0.21):
        report(m)
        print()

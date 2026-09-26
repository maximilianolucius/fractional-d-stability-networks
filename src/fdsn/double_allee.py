"""Double-Allee intraguild-predation (IGP) model: equilibria, reduced matrix, invariants.

Model (Caputo order alpha, per-capita form x_i' = x_i F_i):
    x: r/(x+a) (1-x/K)(x-m) - q1 y - q2 z
    y: e1 q1 x - mu1 - c1 y - h z
    z: e2 q2 x + e3 h y - mu2 - c2 z
All functions work with floats, mpmath mpf or mpmath.iv intervals (generic
arithmetic; sqrt is taken from the object's module).  Nothing here assumes
the Chief's formulas beyond the model definition: the reduced matrix is the
per-capita Jacobian evaluated from the equations, and the invariants are
computed from the matrix entries (see fdsn.c10_threshold.invariants).

Parameter order (14): a, K, r, m, q1, q2, h, e1, e2, e3, mu1, mu2, c1, c2.
"""
from __future__ import annotations

from dataclasses import dataclass, fields

import mpmath as mp
import numpy as np

PARAM_NAMES = ["a", "K", "r", "m", "q1", "q2", "h", "e1", "e2", "e3", "mu1", "mu2", "c1", "c2"]


def _sqrt(x):
    if isinstance(x, mp.iv.mpf):
        return mp.iv.sqrt(x)
    if isinstance(x, mp.mpf):
        return mp.sqrt(x)
    return np.sqrt(x)


@dataclass
class Params:
    a: object; K: object; r: object; m: object
    q1: object; q2: object; h: object
    e1: object; e2: object; e3: object
    mu1: object; mu2: object; c1: object; c2: object

    def as_list(self):
        return [getattr(self, f.name) for f in fields(self)]

    def cast(self, conv):
        return Params(*[conv(v) for v in self.as_list()])


# ----------------------------------------------------------------- prey law

def g_da(x, P: Params):
    return P.r / (x + P.a) * (1 - x / P.K) * (x - P.m)


def g_da_prime(x, P: Params):
    """Derivative computed from the product rule (not from the H_A identity)."""
    r, a, K, m = P.r, P.a, P.K, P.m
    u = (1 - x / K) * (x - m)
    du = -(x - m) / K + (1 - x / K)
    return r * (du * (x + a) - u) / (x + a) ** 2


def H_A(x, P: Params):
    return 1 / (P.K - x) - 1 / (x - P.m) + 1 / (x + P.a)


# ----------------------------------------------------------------- equilibrium

def yz_of_x(x, P: Params):
    """Solve the (linear) consumer equations for Y, Z at prey level x (Cramer)."""
    A1 = P.e1 * P.q1 * x - P.mu1
    A2 = P.e2 * P.q2 * x - P.mu2
    Delta = P.c1 * P.c2 + P.e3 * P.h ** 2
    Y = (P.c2 * A1 - P.h * A2) / Delta
    Z = (P.e3 * P.h * A1 + P.c1 * A2) / Delta
    return Y, Z


def chi_nu(P: Params):
    Delta = P.c1 * P.c2 + P.e3 * P.h ** 2
    chi = (P.e1 * P.c2 * P.q1 ** 2 + P.e2 * P.c1 * P.q2 ** 2 + P.h * P.q1 * P.q2 * (P.e1 * P.e3 - P.e2)) / Delta
    nu = (P.mu1 * (P.q1 * P.c2 + P.q2 * P.e3 * P.h) + P.mu2 * (P.q2 * P.c1 - P.q1 * P.h)) / Delta
    return chi, nu


def quadratic_coeffs(P: Params):
    """(r + K chi) X^2 - [r(K+m) - K chi a + K nu] X + rKm - K nu a."""
    chi, nu = chi_nu(P)
    return P.r + P.K * chi, P.r * (P.K + P.m) - P.K * chi * P.a + P.K * nu, P.r * P.K * P.m - P.K * nu * P.a


def prey_roots(P: Params):
    A, B, C = quadratic_coeffs(P)
    disc = B * B - 4 * A * C
    if isinstance(disc, (float, np.floating)) and disc < 0:
        return []
    sd = _sqrt(disc)
    return [(B + sd) / (2 * A), (B - sd) / (2 * A)]


def residuals(x, y, z, P: Params):
    """The three per-capita equilibrium equations F_i(x,y,z)."""
    return (g_da(x, P) - P.q1 * y - P.q2 * z,
            P.e1 * P.q1 * x - P.mu1 - P.c1 * y - P.h * z,
            P.e2 * P.q2 * x + P.e3 * P.h * y - P.mu2 - P.c2 * z)


def coexistence_equilibria(P: Params, tol=1e-12):
    """All feasible positive coexistence equilibria (float): m < X < K, Y > 0, Z > 0."""
    out = []
    for X in prey_roots(P):
        if not (P.m < X < P.K):
            continue
        Y, Z = yz_of_x(X, P)
        if Y > 0 and Z > 0:
            res = residuals(X, Y, Z, P)
            out.append({"X": float(X), "Y": float(Y), "Z": float(Z), "max_residual": float(max(abs(v) for v in res))})
    return out


# ----------------------------------------------------------------- reduced matrix and invariants

def reduced_matrix(X, Y, Z, P: Params):
    """DF at (X,Y,Z): per-capita Jacobian, entries differentiated from the model."""
    s = -g_da_prime(X, P)
    return [[-s, -P.q1, -P.q2],
            [P.e1 * P.q1, -P.c1, -P.h],
            [P.e2 * P.q2, P.e3 * P.h, -P.c2]]


def full_jacobian(X, Y, Z, P: Params):
    """Jacobian of G_i = x_i F_i at the equilibrium: diag(x*) DF (computed directly)."""
    B = reduced_matrix(X, Y, Z, P)
    xs = [X, Y, Z]
    return [[xs[i] * B[i][j] for j in range(3)] for i in range(3)]


def invariants_of_matrix(B):
    """(p, m, q, beta, kappa, L3, l123, l132) from the entries (generic arithmetic)."""
    a = B
    p = [-a[i][i] for i in range(3)]
    m12 = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    m13 = a[0][0] * a[2][2] - a[0][2] * a[2][0]
    m23 = a[1][1] * a[2][2] - a[1][2] * a[2][1]
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    P3 = p[0] * p[1] * p[2]
    beta = (m12 / (p[0] * p[1]), m13 / (p[0] * p[2]), m23 / (p[1] * p[2]))
    kappa = -det / P3
    l123 = a[0][1] * a[1][2] * a[2][0] / P3
    l132 = a[0][2] * a[2][1] * a[1][0] / P3
    return {"p": p, "m": (m12, m13, m23), "q": -det, "beta": beta, "kappa": kappa, "L3": l123 + l132,
            "l123": l123, "l132": l132}


def T1_of(beta):
    return (_sqrt(beta[0]) + _sqrt(beta[1]) + _sqrt(beta[2])) ** 2


# ----------------------------------------------------------------- constructions (DA-06 / DA-07)

def realize_invariants(beta12, beta13, beta23, kappa, *, s, c1, c2, eta):
    """DA-06 construction: returns (q1, q2, h, e1, e2, e3) with the prescribed invariants."""
    A = beta12 - 1; B0 = beta13 - 1; C = beta23 - 1
    R = kappa - (beta12 + beta13 + beta23 - 2)
    rho = R / _sqrt(A * B0 * C)
    tau = (rho + _sqrt(rho * rho + 4)) / 2
    e1 = eta; e3 = eta; e2 = eta * eta / (tau * tau)
    q1 = _sqrt(A * s * c1 / e1)
    q2 = _sqrt(B0 * s * c2 / e2)
    h = _sqrt(C * c1 * c2 / e3)
    return q1, q2, h, e1, e2, e3


def embed_double_allee(s, X, m, a, K, q1, q2, h, e1, e2, e3, c1, c2, xi):
    """DA-07 construction: returns Params with a positive equilibrium (X, Y, Z) whose slope is s.

    Requires H_A(X) > 0.  Returns (Params, Y, Z, Q, H).
    """
    H = 1 / (K - X) - 1 / (X - m) + 1 / (X + a)
    Q = s / H
    Y = xi * Q / q1
    Z = (1 - xi) * Q / q2
    mu1 = e1 * q1 * X - c1 * Y - h * Z
    mu2 = e2 * q2 * X + e3 * h * Y - c2 * Z
    r = Q * (X + a) / ((1 - X / K) * (X - m))
    return Params(a, K, r, m, q1, q2, h, e1, e2, e3, mu1, mu2, c1, c2), Y, Z, Q, H


def chief_witness(conv=float):
    """The declared high-level design only: alpha=0.9, m0=0.2, target beta=(2,2,2), kappa=18=T1.

    Free scale choices (not target-dependent): s0=c1=c2=1/20, eta=1/2, X0=1, a=1/2, K=11/10, xi=1/2.
    `conv` maps rational strings to the arithmetic type (float, mp.mpf, mp.iv.mpf).
    """
    one = conv("1")
    s0 = conv("0.05"); c1 = conv("0.05"); c2 = conv("0.05"); eta = conv("0.5")
    q1, q2, h, e1, e2, e3 = realize_invariants(2 * one, 2 * one, 2 * one, 18 * one, s=s0, c1=c1, c2=c2, eta=eta)
    P, Y, Z, Q, H = embed_double_allee(s0, one, conv("0.2"), conv("0.5"), conv("1.1"), q1, q2, h, e1, e2, e3, c1, c2, conv("0.5"))
    return P


def with_m(P: Params, m):
    return Params(*[m if n == "m" else getattr(P, n) for n in PARAM_NAMES])

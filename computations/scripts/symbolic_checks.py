"""Symbolic (sympy) checks supporting the Wave-1 structural findings.

S1  elasticity of the fixed-cubic boundary:
      E(r) = b h'(b)/h(b) = (K r - 2u)(1 + 3u r) / ((K r - u)(1 + 2u r)),
    along the parametrisation b = K r^2 - 2u r, h = r^2 + 2u r^3, r > 2u/K.
    Both factors are increasing in r and E -> 3/2 as r -> oo, so 0 < E < 3/2
    and s -> log h(e^s) is convex.  (Used for the logit-convexity proposition.)
S2  symmetric slice: 27 h_alpha(1/3) == 1 + R3(alpha)^3  (Siami), as an identity
    in theta on (pi/3, pi/2).
S3  expansion at alpha -> 2/3+: T K^3 = 27 + (9 sum beta - 27) K + O(K^2) for the
    centre evaluation (leading two orders do not depend on the minimiser).
S4  C-14 constant: pi sqrt(G/S)(1+G/S) S^3/G == pi(S^{5/2}/sqrt G + S^{3/2} sqrt G).
Output: computations/results/SYMBOLIC_CHECKS.json
"""
import json
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _common import dump  # noqa: E402


def s1():
    r, u, K = sp.symbols("r u K", positive=True)
    b = K * r**2 - 2 * u * r
    h = r**2 + 2 * u * r**3
    E = sp.simplify(b * sp.diff(h, r) / sp.diff(b, r) / h)
    target = (K * r - 2 * u) * (1 + 3 * u * r) / ((K * r - u) * (1 + 2 * u * r))
    f1 = (K * r - 2 * u) / (K * r - u)
    f2 = (1 + 3 * u * r) / (1 + 2 * u * r)
    return {
        "E_equals_factorised_form": sp.simplify(E - target) == 0,
        "d_factor1_dr": str(sp.factor(sp.diff(f1, r))),
        "d_factor2_dr": str(sp.factor(sp.diff(f2, r))),
        "limit_E_r_to_inf": str(sp.limit(target, r, sp.oo)),
        "E_at_b0_(r=2u/K)": str(sp.simplify(target.subs(r, 2 * u / K))),
    }


def s2():
    t = sp.symbols("theta", positive=True)
    u = sp.cos(t)
    K = 1 - 4 * u**2
    b = sp.Rational(1, 3)
    r = (u + sp.sqrt(u**2 + K * b)) / K
    lhs = 27 * r**2 * (1 + 2 * u * r)
    R3 = sp.sin(t) / sp.sin(t - sp.pi / 3)
    rhs = 1 + R3**3
    # u^2 + K/3 = (1 - u^2)/3 = sin^2/3  => sqrt = sin t / sqrt 3 on (pi/3, pi/2)
    r_simpl = (u + sp.sin(t) / sp.sqrt(3)) / K
    lhs2 = 27 * r_simpl**2 * (1 + 2 * u * r_simpl)
    diff = sp.simplify(sp.expand_trig(sp.simplify(lhs2 - rhs)))
    num = [float((lhs - rhs).subs(t, v).evalf(50)) for v in (1.1, 1.3, 1.5, 1.57)]
    return {"sqrt_simplification": "sqrt(u^2+K/3) = sin(theta)/sqrt(3)",
            "symbolic_difference": str(diff), "numeric_differences": num}


def s3():
    K = sp.symbols("K", positive=True)
    B = sp.symbols("Bc", positive=True)            # B at the centre = sum(beta)/9
    u = sp.sqrt(1 - K) / 2
    r = (u + sp.sqrt(u**2 + K * B)) / K
    h = r**2 * (1 + 2 * u * r)
    ser = sp.series(27 * h * K**3, K, 0, 2).removeO()
    return {"27 h(Bc) K^3 series": str(sp.expand(sp.simplify(ser))),
            "with Bc = sum(beta)/9": "27 + (81 Bc - 27) K = 27 + (9 sum(beta) - 27) K"}


def s4():
    S, G = sp.symbols("S G", positive=True)
    lhs = sp.pi * sp.sqrt(G / S) * (1 + G / S) * S**3 / G
    rhs = sp.pi * (S**sp.Rational(5, 2) / sp.sqrt(G) + S**sp.Rational(3, 2) * sp.sqrt(G))
    return {"identity_holds": sp.simplify(lhs - rhs) == 0}


def s5():
    """Exact series of T_alpha(1,1,1) = 1 + R3^3 at alpha = 1 - eps (second-order coefficient)."""
    e = sp.symbols("epsilon", positive=True)
    th = sp.pi / 2 - sp.pi * e / 2
    R3 = sp.cos(sp.pi * e / 2) / sp.sin(sp.pi / 6 - sp.pi * e / 2)
    ser = sp.series(1 + R3**3, e, 0, 4).removeO()
    coeffs = [sp.nsimplify(sp.simplify(ser.coeff(e, k))) for k in range(4)]
    del th
    return {"coefficients": [str(sp.simplify(c)) for c in coeffs],
            "numeric": [float(c) for c in coeffs]}


def s6():
    """C-11 certified fraction of the band as alpha -> 1:
    (T1/rho - T1)/(T_alpha - T1) -> 2 pi T1 / C = 2 sqrt(S G)/(S + G) <= 1 (AM-GM)."""
    S, G, e = sp.symbols("S G epsilon", positive=True)
    rho = (1 - 2 * sp.sin(sp.pi * e / 2)) ** 2
    lead = sp.limit((1 / rho - 1) / e, e, 0)
    C = sp.pi * (S ** sp.Rational(5, 2) / sp.sqrt(G) + S ** sp.Rational(3, 2) * sp.sqrt(G))
    frac = sp.simplify(lead * S**2 / C)
    return {"(1/rho-1)/eps -> ": str(lead), "limit_fraction": str(frac),
            "equals_2sqrt(SG)/(S+G)": sp.simplify(frac - 2 * sp.sqrt(S * G) / (S + G)) == 0}


if __name__ == "__main__":
    out = {"S1_elasticity": s1(), "S2_symmetric_siami": s2(), "S3_two_thirds": s3(), "S4_C14_constant": s4(),
           "S5_symmetric_series": s5(), "S6_C11_limit_fraction": s6()}
    print(json.dumps(out, indent=2, default=str))
    dump("SYMBOLIC_CHECKS.json", out)

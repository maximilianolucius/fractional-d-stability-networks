"""Interval-arithmetic bracket for the C-10 threshold T_alpha(beta).

CERTIFIED COMPUTATION of the *variational formula*: for exact decimal inputs
(beta given as decimal strings, alpha as a decimal string, all enclosed by
mpmath.iv intervals with outward rounding) we return [L, U] with

    L <= T_alpha(beta) = min_{x in open simplex} h_alpha(B_beta(x))/(x1 x2 x3) <= U.

It certifies the value of the minimization problem defined in C-10.  It does
not certify the C-10 theorem itself (which is analytic).

Method (coordinates (x1, x2), x3 = 1 - x1 - x2):
1. Upper bound U: interval evaluation of F at a high-precision minimizer xh.
2. Boundary strip: if some x_i < eps then x1x2x3 < eps/4 and h(B) >= h(0),
   so F > 4 h(0)/eps; eps is chosen so that this exceeds 2U.
3. Convex core: on the box X0 = xh + [-rho, rho]^2 the interval Hessian of
   G = log F is certified positive definite (diagonal lower bounds positive,
   det lower bound positive).  Hence on X0 (convex), G(x) >= G(xh) - |grad
   G(xh)|_1 rho, giving L0.
4. Branch and bound on the rest of {x_i >= eps}: boxes are discarded when
   the monotone interval lower bound h(B_lo)/P_hi exceeds exp(L0-bound).
   B is increasing in each x_i (all beta > 0), so B_lo/P_hi use endpoints.
If every box is discarded, T >= exp(G(xh)_lo - |grad|_1 rho) =: L.
"""
from __future__ import annotations

import time

import mpmath as mp
from mpmath import iv


def lo(x):
    return mp.mpf(x.a)


def hi(x):
    return mp.mpf(x.b)


def _iv(v):
    return iv.mpf(v) if not isinstance(v, iv.mpf) else v


def _h_parts(b, u, K):
    s = iv.sqrt(u * u + K * b)
    r = (u + s) / K
    r1 = 1 / (2 * s)
    r2 = -K / (4 * s * s * s)
    h = r * r * (1 + 2 * u * r)
    dh = 2 * r + 6 * u * r * r
    return h, dh * r1, (2 + 12 * u * r) * r1 * r1 + dh * r2


def _uk(alpha):
    t = _iv(alpha) * iv.pi / 2
    u = iv.cos(t)
    K = 1 - 4 * u * u
    return u, K


def _hess_G(x1, x2, beta, u, K):
    b12, b13, b23 = beta
    x3 = 1 - x1 - x2
    B = b12 * x1 * x2 + b13 * x1 * x3 + b23 * x2 * x3
    h, h1, h2 = _h_parts(B, u, K)
    mu = h1 / h
    nu = h2 / h - mu * mu
    d3 = b13 * x1 + b23 * x2
    g1 = b12 * x2 + b13 * x3 - d3
    g2 = b12 * x1 + b23 * x3 - d3
    H11 = nu * g1 * g1 + mu * (-2 * b13) + 1 / (x1 * x1) + 1 / (x3 * x3)
    H22 = nu * g2 * g2 + mu * (-2 * b23) + 1 / (x2 * x2) + 1 / (x3 * x3)
    H12 = nu * g1 * g2 + mu * (b12 - b13 - b23) + 1 / (x3 * x3)
    G1 = mu * g1 - 1 / x1 + 1 / x3
    G2 = mu * g2 - 1 / x2 + 1 / x3
    return H11, H22, H12, G1, G2, h, x3


def certify_threshold(beta_str, alpha_str, *, dps: int = 40, xh=None,
                      max_boxes: int = 400_000, time_limit: float = 1800.0) -> dict:
    """Return a certified bracket [L, U] for T_alpha(beta) (see module doc)."""
    from .c10_threshold import threshold_mp

    t0 = time.time()
    iv.dps = dps
    mp.mp.dps = dps
    beta = [iv.mpf(b) for b in beta_str]
    u, K = _uk(alpha_str)
    if not (lo(K) > 0 and lo(u) > 0):
        raise ValueError("need 2/3 < alpha < 1 (K > 0, u > 0)")
    if xh is None:
        r = threshold_mp(beta_str, alpha_str, dps=dps + 10)
        xh = (r["x"][0], r["x"][1])
    # point values at xh (exact binary numbers, enclosed)
    x1h, x2h = iv.mpf(mp.mpf(xh[0])), iv.mpf(mp.mpf(xh[1]))
    H11, H22, H12, G1, G2, hh, x3h = _hess_G(x1h, x2h, beta, u, K)
    Fh = hh / (x1h * x2h * x3h)
    U = hi(Fh)
    # boundary strip
    h0 = _h_parts(iv.mpf(0), u, K)[0]
    eps = lo(h0) * 2 / U * mp.mpf("0.999")      # 4 h0/eps > 2U
    # convex core: largest rho (halving) with certified PD interval Hessian
    rho = min(xh[0], xh[1], 1 - xh[0] - xh[1]) * mp.mpf('0.9')
    ok = False
    for _ in range(60):
        X1 = iv.mpf([lo(x1h) - rho, hi(x1h) + rho])
        X2 = iv.mpf([lo(x2h) - rho, hi(x2h) + rho])
        if (lo(X1) > 0 and lo(X2) > 0 and lo(1 - X1 - X2) > 0):
            A11, A22, A12, *_ = _hess_G(X1, X2, beta, u, K)
            m12 = max(abs(lo(A12)), abs(hi(A12)))
            if lo(A11) > 0 and lo(A22) > 0 and lo(iv.mpf(lo(A11)) * lo(A22) - iv.mpf(m12) ** 2) > 0:
                ok = True
                break
        rho = rho / 2
    if not ok:
        return {"certified": False, "reason": "no PD box", "U": U}
    Gh = iv.log(Fh)
    gl1 = max(abs(lo(G1)), abs(hi(G1))) + max(abs(lo(G2)), abs(hi(G2)))
    L_log = lo(Gh - iv.mpf(gl1) * rho)
    L = lo(iv.exp(iv.mpf(L_log)))
    target = L                                   # prove F >= target outside the core
    target_log = L_log
    # branch and bound over [eps, 1]^2 with x3 >= eps, excluding core box
    core = (lo(x1h) - rho, hi(x1h) + rho, lo(x2h) - rho, hi(x2h) + rho)
    stack = [(mp.mpf(eps), mp.mpf(1) - 2 * eps, mp.mpf(eps), mp.mpf(1) - 2 * eps)]
    processed = 0
    min_lb = mp.inf
    while stack:
        a1, b1, a2, b2 = stack.pop()
        processed += 1
        if processed > max_boxes or time.time() - t0 > time_limit:
            return {"certified": False, "reason": "box/time budget", "boxes": processed,
                    "U": U, "L_core": L}
        # outside simplex strip (x3 < eps everywhere on box)
        if a1 + a2 > 1 - eps:
            continue
        # inside the core box entirely
        if a1 >= core[0] and b1 <= core[1] and a2 >= core[2] and b2 <= core[3]:
            continue
        x3lo = max(mp.mpf(eps), 1 - b1 - b2)
        x3hi = 1 - a1 - a2
        X1lo, X1hi, X2lo, X2hi = iv.mpf(a1), iv.mpf(b1), iv.mpf(a2), iv.mpf(b2)
        X3lo = 1 - X1hi - X2hi if 1 - b1 - b2 > eps else iv.mpf(eps)
        X3hi = 1 - X1lo - X2lo
        Blo = beta[0] * X1lo * X2lo + beta[1] * X1lo * X3lo + beta[2] * X2lo * X3lo
        Phi = X1hi * X2hi * X3hi
        lb = lo(_h_parts(iv.mpf(lo(Blo)), u, K)[0] / Phi)
        del x3lo, x3hi
        if lb > target:
            min_lb = min(min_lb, lb)
            continue
        # mean-value (centred) form of G = log F on boxes strictly inside the simplex
        if max(b1 - a1, b2 - a2) < mp.mpf("0.1") and 1 - b1 - b2 > 0:
            BX1, BX2 = iv.mpf([a1, b1]), iv.mpf([a2, b2])
            *_, G1b, G2b, _hb, _x3b = _hess_G(BX1, BX2, beta, u, K)
            c1, c2 = (a1 + b1) / 2, (a2 + b2) / 2
            C1, C2 = iv.mpf(c1), iv.mpf(c2)
            _, _, _, _, _, hc, x3c = _hess_G(C1, C2, beta, u, K)
            Gc = iv.log(hc / (C1 * C2 * x3c))
            mv = Gc + G1b * (BX1 - C1) + G2b * (BX2 - C2)
            if lo(mv) > target_log:
                min_lb = min(min_lb, lo(iv.exp(iv.mpf(lo(mv)))))
                continue
        # split the longer side
        if (b1 - a1) >= (b2 - a2):
            m = (a1 + b1) / 2
            stack += [(a1, m, a2, b2), (m, b1, a2, b2)]
        else:
            m = (a2 + b2) / 2
            stack += [(a1, b1, a2, m), (a1, b1, m, b2)]
        if max(b1 - a1, b2 - a2) < mp.mpf(10) ** -12:
            return {"certified": False, "reason": "box too small", "U": U, "L_core": L,
                    "box": (a1, b1, a2, b2)}
    return {
        "certified": True, "L": L, "U": U, "rel_width": (U - L) / L,
        "eps_strip": eps, "rho_core": rho, "boxes": processed,
        "grad_l1_at_xh": gl1, "seconds": time.time() - t0, "dps": dps,
        "beta": list(beta_str), "alpha": alpha_str,
    }

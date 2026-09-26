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


def _iv_rational(b):
    """Interval from a decimal string or an exact rational string 'p/q'."""
    if isinstance(b, str) and "/" in b:
        n, d = b.split("/")
        return iv.mpf(n.strip()) / iv.mpf(d.strip())
    return iv.mpf(b) if not isinstance(b, iv.mpf) else b


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
    beta = [_iv_rational(b) for b in beta_str]
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
    target = U                                   # prove F > U outside the core -> x* in core
    target_log = lo(iv.log(iv.mpf(U)))
    # Gershgorin lower bound of the Hessian of G over the core box (convex there)
    lam = min(lo(A11) - m12, lo(A22) - m12)
    # PD 2x2: lam_min = det/lam_max >= det_lb/trace_ub (det_lb > 0 was certified above)
    det_lb = lo(iv.mpf(lo(A11)) * lo(A22) - iv.mpf(m12) ** 2)
    lam = max(lam, det_lb / (hi(A11) + hi(A22)))
    gnorm2 = mp.sqrt(max(abs(lo(G1)), abs(hi(G1))) ** 2 + max(abs(lo(G2)), abs(hi(G2))) ** 2)
    x_rad = (2 * gnorm2 / lam) if lam > 0 else rho * mp.sqrt(2)
    x_rad = min(x_rad, rho * mp.sqrt(2))
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
        # straddling the core: cut along a core edge instead of the midpoint
        if b1 > core[0] and a1 < core[1] and b2 > core[2] and a2 < core[3]:
            cut = None
            for c in (core[0], core[1]):
                if a1 < c < b1:
                    cut = ("x1", c); break
            if cut is None:
                for c in (core[2], core[3]):
                    if a2 < c < b2:
                        cut = ("x2", c); break
            if cut is not None:
                if cut[0] == "x1":
                    stack += [(a1, cut[1], a2, b2), (cut[1], b1, a2, b2)]
                else:
                    stack += [(a1, b1, a2, cut[1]), (a1, b1, cut[1], b2)]
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
        "x_hat": (mp.mpf(xh[0]), mp.mpf(xh[1]), 1 - mp.mpf(xh[0]) - mp.mpf(xh[1])),
        "x_enclosure_radius": x_rad, "core_box": core, "hess_gershgorin_lb": lam,
        "eps_strip": eps, "rho_core": rho, "boxes": processed,
        "grad_l1_at_xh": gl1, "seconds": time.time() - t0, "dps": dps,
        "beta": list(beta_str), "alpha": alpha_str,
    }


# ---------------------------------------------------------------------------
# Logit-coordinate certificate (conditional on C-15 Theorem 1: G strictly convex)
# ---------------------------------------------------------------------------

def _logit_parts(y1, y2, beta, u, K):
    """Interval evaluation of G, grad_y G and Hess_y G at logit intervals (y1, y2).

    Formulas (from src/fdsn/c10_threshold.objective_G):
      x = softmax(y1, y2, 0); gx_i = mu dB_i - 1/x_i; s = sum_i x_i gx_i = 2 mu B - 3
      dG/dy_k = x_k gx_k - x_k s
      Hess = J^T Hx J + sum_i gx_i d2x_i,  J_ik = x_i (d_ik - x_k)
    """
    e1, e2 = iv.exp(y1), iv.exp(y2)
    S = e1 + e2 + 1
    x = [e1 / S, e2 / S, 1 / S]
    b12, b13, b23 = beta
    Bm = [[0, b12, b13], [b12, 0, b23], [b13, b23, 0]]
    dB = [sum(Bm[i][j] * x[j] for j in range(3)) for i in range(3)]
    B = (dB[0] * x[0] + dB[1] * x[1] + dB[2] * x[2]) / 2
    h, h1, h2 = _h_parts(B, u, K)
    mu = h1 / h
    nu = h2 / h - mu * mu
    G = iv.log(h) - iv.log(x[0]) - iv.log(x[1]) - iv.log(x[2])
    gx = [mu * dB[i] - 1 / x[i] for i in range(3)]
    s = 2 * mu * B - 3
    g = [x[k] * gx[k] - x[k] * s for k in range(2)]
    Hx = [[nu * dB[i] * dB[j] + mu * Bm[i][j] + (1 / (x[i] * x[i]) if i == j else 0) for j in range(3)] for i in range(3)]
    J = [[x[i] * ((1 if i == k else 0) - x[k]) for k in range(2)] for i in range(3)]
    H = [[sum(J[i][k] * Hx[i][j] * J[j][l] for i in range(3) for j in range(3)) for l in range(2)] for k in range(2)]
    for k in range(2):
        for l in range(2):
            acc = 0
            for i in range(3):
                t1 = x[i] * ((1 if i == k else 0) - x[k]) * ((1 if i == l else 0) - x[l])
                t2 = x[i] * x[k] * ((1 if k == l else 0) - x[l])
                acc += gx[i] * (t1 - t2)
            H[k][l] += acc
    return G, g, H, x


def certify_threshold_logit(beta_str, alpha_str, *, dps: int = 40, R0: float = 0.5, n_sub: int = 8) -> dict:
    """Certified bracket for T_alpha(beta) in logit coordinates.

    CONDITIONAL on C-15 Theorem 1 (G strictly convex on R^2, proof-audited):
    1. y_hat from HP Newton; interval G(y_hat), grad G(y_hat).
    2. Box Y = y_hat + [-R, R]^2 with interval Hessian certified >= lam > 0 on Y
       (n_sub x n_sub pieces; Gershgorin / det-over-trace bound valid for every
       symmetric matrix inside the interval matrix, hence for segment averages).
    3. If |grad G(y_hat)| < lam R then y* in Y: otherwise, at the exit point y_b
       of the segment y_hat -> y*, convexity along the segment gives
       grad G(y_b).(y_b - y_hat) <= 0, while the mean-value form gives
       grad G(y_b).(y_b - y_hat) >= -|grad G(y_hat)| R + lam R^2 > 0.
       Then |y* - y_hat| <= |grad G(y_hat)| / lam (strong convexity on Y) and
       G(y*) >= G(y_hat) - |grad G(y_hat)| |y* - y_hat|.
    4. |x* - x_hat|_2 <= |y* - y_hat|_2 / 2 (softmax Jacobian norm <= 1/2).
    Cost is independent of the anisotropy of beta.
    """
    from .c10_threshold import threshold_mp

    t0 = time.time()
    iv.dps = dps
    mp.mp.dps = dps
    beta = [_iv_rational(b) for b in beta_str]
    u, K = _uk(alpha_str)
    if not (lo(K) > 0 and lo(u) > 0):
        raise ValueError("need 2/3 < alpha < 1")
    r = threshold_mp([b if "/" not in b else mp.nstr(mp.mpf(b.split("/")[0]) / mp.mpf(b.split("/")[1]), dps + 5)
                      for b in beta_str], alpha_str, dps=dps + 10)
    yh = [mp.mpf(r["y"][0]), mp.mpf(r["y"][1])]
    Y1h, Y2h = iv.mpf(yh[0]), iv.mpf(yh[1])
    Gh, gh, _, xh = _logit_parts(Y1h, Y2h, beta, u, K)
    gnorm = mp.sqrt(max(abs(lo(gh[0])), abs(hi(gh[0]))) ** 2 + max(abs(lo(gh[1])), abs(hi(gh[1]))) ** 2)
    U = hi(iv.exp(Gh))
    R = mp.mpf(R0)
    ok = False
    lam = -mp.inf
    for _ in range(80):
        # strong-convexity constant on the box Y = y_hat + [-R,R]^2 (interval Hessian, n_sub^2 pieces)
        lam = mp.inf
        for i in range(n_sub):
            for j in range(n_sub):
                Y1 = iv.mpf([yh[0] - R + 2 * R * i / n_sub, yh[0] - R + 2 * R * (i + 1) / n_sub])
                Y2 = iv.mpf([yh[1] - R + 2 * R * j / n_sub, yh[1] - R + 2 * R * (j + 1) / n_sub])
                _, _, H, _ = _logit_parts(Y1, Y2, beta, u, K)
                m12 = max(abs(lo(H[0][1])), abs(hi(H[0][1])))
                a, d = lo(H[0][0]), lo(H[1][1])
                l1 = min(a - m12, d - m12)
                det_lb = lo(iv.mpf(a) * d - iv.mpf(m12) ** 2)
                l2 = det_lb / (hi(H[0][0]) + hi(H[1][1])) if (a > 0 and d > 0 and det_lb > 0) else -mp.inf
                lam = min(lam, max(l1, l2))
                if not (lam > 0):
                    break
            if not (lam > 0):
                break
        # localisation: y* in Y iff R > |grad G(y_hat)| / lam (mean-value argument, see docstring)
        ok = (lam > 0) and (gnorm < lam * R)
        if ok:
            break
        R = R / 2
    if not ok:
        return {"certified": False, "reason": "Hessian PD / localisation failed down to R=%s" % mp.nstr(R, 5), "U": U}
    rho_y = min(gnorm / lam, R * mp.sqrt(2))
    L = lo(iv.exp(iv.mpf(lo(Gh)) - iv.mpf(gnorm) * iv.mpf(rho_y)))
    return {
        "certified": True, "conditional_on": "C-15 Theorem 1 (strict convexity of G in logit coordinates)",
        "L": L, "U": U, "rel_width": (U - L) / L,
        "x_hat": tuple(mp.mpf(lo(v)) for v in xh), "x_enclosure_radius": rho_y / 2, "y_box_R": R,
        "hess_lb_on_box": lam, "grad_norm_at_yhat": gnorm, "seconds": time.time() - t0, "dps": dps,
        "beta": list(beta_str), "alpha": alpha_str,
    }

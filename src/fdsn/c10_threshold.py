"""Numerical evaluation of the exact C-10 threshold T_alpha(beta).

    T_alpha(beta) = min_{x in open 2-simplex} h_alpha(B_beta(x)) / (x1 x2 x3)

with B_beta(x) = beta12 x1 x2 + beta13 x1 x3 + beta23 x2 x3 and h_alpha the
normalized fixed-cubic Matignon boundary of research/THEOREM_C10_EXACT_3X3.md.

Everything in this module is NUMERICAL CORROBORATION unless explicitly stated
otherwise.  The theorem is analytic; these routines evaluate its variational
formula (float64, vectorized) and refine it at arbitrary precision (mpmath).
Certified brackets live in :mod:`fdsn.interval_cert`.

Parameterization
----------------
The open simplex is parameterized by logits y = (y1, y2):

    x = softmax(y1, y2, 0),

which is a diffeomorphism R^2 -> interior of the simplex.  We minimize

    G(y) = log h(B(x(y))) - log x1 - log x2 - log x3,

whose value is log T at the minimizer.  Gradient and Hessian are analytic.

Beta ordering convention throughout: beta = (beta12, beta13, beta23).
"""
from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp
import numpy as np
from numpy.typing import ArrayLike

TWO_THIRDS = 2.0 / 3.0


# ---------------------------------------------------------------------------
# fixed-cubic boundary h_alpha(b) and derivatives (float64, vectorized)
# ---------------------------------------------------------------------------

def uk(alpha: float) -> tuple[float, float]:
    """Return (u, K) = (cos(alpha pi/2), 1-4u^2)."""
    if not (TWO_THIRDS < alpha < 1.0):
        raise ValueError("C-10 threshold requires 2/3 < alpha < 1")
    u = float(np.cos(alpha * np.pi / 2.0))
    # 1-4cos^2(t) = -sin(3t)/sin(t): the product form is exact near alpha=2/3
    t = alpha * np.pi / 2.0
    K = float(-np.sin(3.0 * t) / np.sin(t))
    return u, K


def h_derivs(b: ArrayLike, u: float, K: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """h, h', h'' of the normalized boundary as functions of b > 0."""
    b = np.asarray(b, dtype=float)
    s = np.sqrt(u * u + K * b)
    r = (u + s) / K
    r1 = 0.5 / s
    r2 = -0.25 * K / (s * s * s)
    h = r * r * (1.0 + 2.0 * u * r)
    dh_dr = 2.0 * r + 6.0 * u * r * r
    d2h_dr2 = 2.0 + 12.0 * u * r
    h1 = dh_dr * r1
    h2 = d2h_dr2 * r1 * r1 + dh_dr * r2
    return h, h1, h2


def h_alpha(b: ArrayLike, alpha: float) -> np.ndarray:
    u, K = uk(alpha)
    return h_derivs(b, u, K)[0]


def T1(beta: ArrayLike) -> np.ndarray:
    """Classical Cain threshold (sqrt b12 + sqrt b13 + sqrt b23)^2 (vectorized)."""
    beta = np.asarray(beta, dtype=float)
    return np.sum(np.sqrt(beta), axis=-1) ** 2


def rate_constant(beta: ArrayLike) -> np.ndarray:
    """C-14 constant C(beta) = pi (S^{5/2}/sqrt G + S^{3/2} sqrt G)."""
    beta = np.asarray(beta, dtype=float)
    S = np.sum(np.sqrt(beta), axis=-1)
    G = np.sqrt(np.prod(beta, axis=-1))
    return np.pi * (S ** 2.5 / np.sqrt(G) + S ** 1.5 * np.sqrt(G))


def siami_R3(alpha: float) -> float:
    t = alpha * np.pi / 2.0
    return float(np.sin(t) / np.sin(t - np.pi / 3.0))


def rho_alpha(alpha: float) -> float:
    return float((1.0 - 2.0 * np.cos(alpha * np.pi / 2.0)) ** 2)


def phi_threshold(beta: ArrayLike, alpha: float) -> np.ndarray:
    """Effective kappa-boundary of the C-11 certificate: Phi>rho <=> kappa<T1/rho.

    Phi(A) = (sum sqrt(p_i m_jk))^2 / q = T1(beta)/kappa.
    """
    return T1(beta) / rho_alpha(alpha)


# ---------------------------------------------------------------------------
# objective in logit coordinates (float64, vectorized over leading axis)
# ---------------------------------------------------------------------------

def _softmax2(y: np.ndarray) -> np.ndarray:
    z = np.concatenate([y, np.zeros(y.shape[:-1] + (1,))], axis=-1)
    z = z - np.max(z, axis=-1, keepdims=True)
    e = np.exp(z)
    return e / np.sum(e, axis=-1, keepdims=True)


def _beta_matrix(beta: np.ndarray) -> np.ndarray:
    """Symmetric zero-diagonal matrix Bm with B(x) = x^T Bm x / 2 * 2 / 2.

    B(x) = sum_{i<j} beta_ij x_i x_j = 0.5 x^T Bm x.
    """
    n = beta.shape[0]
    Bm = np.zeros((n, 3, 3))
    Bm[:, 0, 1] = Bm[:, 1, 0] = beta[:, 0]
    Bm[:, 0, 2] = Bm[:, 2, 0] = beta[:, 1]
    Bm[:, 1, 2] = Bm[:, 2, 1] = beta[:, 2]
    return Bm


def objective_G(y: np.ndarray, beta: np.ndarray, u: np.ndarray, K: np.ndarray,
                derivs: bool = True):
    """G = log h(B) - sum log x and its logit gradient/Hessian.

    Shapes: y (n,2), beta (n,3), u,K (n,).  Returns G (n,), g (n,2), H (n,2,2).
    """
    x = _softmax2(y)
    Bm = _beta_matrix(beta)
    np.seterr(divide="ignore", invalid="ignore", over="ignore")
    Bi = np.einsum("nij,nj->ni", Bm, x)          # dB/dx_i
    B = 0.5 * np.sum(Bi * x, axis=-1)
    h, h1, h2 = h_derivs(B, u, K)
    G = np.log(h) - np.sum(np.log(x), axis=-1)
    if not derivs:
        return G, x, B
    mu = h1 / h
    nu = h2 / h - mu * mu
    gx = mu[:, None] * Bi - 1.0 / x                                # (n,3)
    Hx = (nu[:, None, None] * Bi[:, :, None] * Bi[:, None, :]
          + mu[:, None, None] * Bm
          + np.einsum("ni,ij->nij", 1.0 / (x * x), np.eye(3)))
    # softmax chain rule; k,l in {0,1}
    J = np.zeros((x.shape[0], 3, 2))
    for k in range(2):
        J[:, :, k] = -x * x[:, k:k + 1]
        J[:, k, k] += x[:, k]
    s = np.sum(gx * x, axis=-1)                                    # sum g_i x_i
    g = gx[:, :2] * x[:, :2] - x[:, :2] * s[:, None]
    H = np.einsum("nik,nij,njl->nkl", J, Hx, J)
    # second-derivative term sum_i g_i d2x_i/dy_k dy_l
    # d2x_i = x_i (d_ik - x_k)(d_il - x_l) - x_i x_k (d_kl - x_l)
    for k in range(2):
        for l in range(2):
            dk = np.zeros(3); dk[k] = 1.0
            dl = np.zeros(3); dl[l] = 1.0
            term = x * (dk - x[:, k:k + 1]) * (dl - x[:, l:l + 1])
            term -= x * x[:, k:k + 1] * ((1.0 if k == l else 0.0) - x[:, l:l + 1])
            H[:, k, l] += np.sum(gx * term, axis=-1)
    return G, g, H, x, B


# ---------------------------------------------------------------------------
# robust batch minimizer
# ---------------------------------------------------------------------------

@dataclass
class ThresholdBatch:
    T: np.ndarray            # threshold values
    x: np.ndarray            # simplex minimizers (n,3)
    y: np.ndarray            # logit minimizers (n,2)
    grad_norm: np.ndarray    # |grad_y G| at the returned point
    hess_min_eig: np.ndarray  # smallest eigenvalue of Hess_y G
    hess_cond: np.ndarray    # condition number of Hess_y G
    it: np.ndarray


def _grid(half_width: float, step: float) -> np.ndarray:
    g = np.arange(-half_width, half_width + 1e-12, step)
    Y1, Y2 = np.meshgrid(g, g, indexing="ij")
    return np.stack([Y1.ravel(), Y2.ravel()], axis=-1)


def newton_refine(y0: np.ndarray, beta: np.ndarray, u: np.ndarray, K: np.ndarray,
                  max_iter: int = 100, tol: float = 1e-13):
    """Damped Newton in logit space with backtracking; vectorized."""
    y = y0.copy()
    n = y.shape[0]
    it = np.zeros(n, dtype=int)
    active = np.ones(n, dtype=bool)
    for _ in range(max_iter):
        if not active.any():
            break
        idx = np.nonzero(active)[0]
        G, g, H, x, B = objective_G(y[idx], beta[idx], u[idx], K[idx])
        gn = np.linalg.norm(g, axis=-1)
        done = gn < tol
        active[idx[done]] = False
        idx, G, g, H = idx[~done], G[~done], g[~done], H[~done]
        if idx.size == 0:
            break
        it[idx] += 1
        # Newton direction if PD else steepest descent (with LM shift)
        w, V = np.linalg.eigh(H)
        w = np.maximum(w, 1e-8 * np.maximum(1.0, np.abs(w).max(axis=-1, keepdims=True)))
        step = -np.einsum("nij,nj,nkj,nk->ni", V, 1.0 / w, V, g)
        t = np.ones(idx.size)
        accepted = np.zeros(idx.size, dtype=bool)
        ycur = y[idx]
        for _ls in range(40):
            trial = ycur + t[:, None] * step
            Gt = objective_G(trial, beta[idx], u[idx], K[idx], derivs=False)[0]
            ok = np.isfinite(Gt) & (Gt <= G + 1e-4 * t * np.sum(g * step, axis=-1) + 1e-15 * np.abs(G))
            newly = ok & ~accepted
            y[idx[newly]] = trial[newly]
            accepted |= ok
            if accepted.all():
                break
            t = np.where(accepted, t, 0.5 * t)
        stuck = ~accepted
        active[idx[stuck]] = False   # cannot decrease further: at float floor
    G, g, H, x, B = objective_G(y, beta, u, K)
    w = np.linalg.eigvalsh(H)
    return y, np.exp(G), x, np.linalg.norm(g, axis=-1), w[:, 0], w[:, 1] / np.abs(w[:, 0]), it


def threshold_batch(beta: ArrayLike, alpha: ArrayLike, *, half_width: float = 12.0,
                    step: float = 0.5, n_starts: int = 1, chunk: int = 2000) -> ThresholdBatch:
    """T_alpha(beta) for many (beta, alpha) pairs.

    Global phase: log-objective on a logit grid [-hw,hw]^2 (covers x_i >~ e^-hw).
    Local phase: Newton from the best `n_starts` grid local minima; best kept.
    """
    beta = np.atleast_2d(np.asarray(beta, dtype=float))
    alpha = np.broadcast_to(np.asarray(alpha, dtype=float), (beta.shape[0],)).copy()
    if np.any(alpha <= TWO_THIRDS) or np.any(alpha >= 1.0):
        raise ValueError("2/3 < alpha < 1 required")
    t = alpha * np.pi / 2.0
    u = np.cos(t)
    K = -np.sin(3.0 * t) / np.sin(t)
    grid = _grid(half_width, step)
    m = int(round(np.sqrt(grid.shape[0])))
    out = {k: np.empty(beta.shape[0]) for k in ("T", "gn", "hmin", "hcond", "it")}
    X = np.empty((beta.shape[0], 3))
    Y = np.empty((beta.shape[0], 2))
    for s0 in range(0, beta.shape[0], chunk):
        sl = slice(s0, min(s0 + chunk, beta.shape[0]))
        nb = sl.stop - sl.start
        yy = np.broadcast_to(grid, (nb,) + grid.shape).reshape(-1, 2)
        bb = np.repeat(beta[sl], grid.shape[0], axis=0)
        GG = objective_G(yy, bb, np.repeat(u[sl], grid.shape[0]),
                         np.repeat(K[sl], grid.shape[0]), derivs=False)[0]
        GG = GG.reshape(nb, m, m)
        # grid local minima (8-neighbourhood, edges padded with +inf)
        P = np.pad(GG, ((0, 0), (1, 1), (1, 1)), constant_values=np.inf)
        is_min = np.ones_like(GG, dtype=bool)
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                is_min &= GG <= P[:, 1 + di:1 + di + m, 1 + dj:1 + dj + m]
        cand = np.where(is_min, GG, np.inf).reshape(nb, -1)
        order = np.argsort(cand, axis=1)[:, :n_starts]
        bestT = np.full(nb, np.inf)
        for k in range(n_starts):
            valid = np.isfinite(np.take_along_axis(cand, order[:, k:k + 1], 1)[:, 0])
            if k == 0:
                valid[:] = True
            y0 = grid[order[:, k]]
            y, T, x, gn, hmin, hcond, it = newton_refine(y0, beta[sl], u[sl], K[sl])
            better = valid & (T < bestT)
            idx = np.arange(sl.start, sl.stop)[better]
            bestT[better] = T[better]
            out["T"][idx] = T[better]; out["gn"][idx] = gn[better]
            out["hmin"][idx] = hmin[better]; out["hcond"][idx] = hcond[better]
            out["it"][idx] = it[better]; X[idx] = x[better]; Y[idx] = y[better]
    return ThresholdBatch(out["T"], X, Y, out["gn"], out["hmin"], out["hcond"], out["it"].astype(int))


def threshold(beta: ArrayLike, alpha: float, n_starts: int = 4) -> ThresholdBatch:
    """Single (beta, alpha) convenience wrapper with 4 Newton starts."""
    return threshold_batch(np.asarray(beta, dtype=float)[None, :], alpha, n_starts=n_starts)


# ---------------------------------------------------------------------------
# arbitrary precision (mpmath)
# ---------------------------------------------------------------------------

def mp_uk(alpha) -> tuple:
    a = mp.mpf(alpha)
    t = a * mp.pi / 2
    return mp.cos(t), -mp.sin(3 * t) / mp.sin(t)


def mp_h_derivs(b, u, K):
    s = mp.sqrt(u * u + K * b)
    r = (u + s) / K
    r1 = 1 / (2 * s)
    r2 = -K / (4 * s ** 3)
    h = r * r * (1 + 2 * u * r)
    dh = 2 * r + 6 * u * r * r
    return h, dh * r1, (2 + 12 * u * r) * r1 * r1 + dh * r2


def mp_T1(beta):
    return (mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])) ** 2


def mp_rate_constant(beta):
    S = mp.sqrt(beta[0]) + mp.sqrt(beta[1]) + mp.sqrt(beta[2])
    G = mp.sqrt(beta[0] * beta[1] * beta[2])
    return mp.pi * (S ** mp.mpf(2.5) / mp.sqrt(G) + S ** mp.mpf(1.5) * mp.sqrt(G))


def mp_siami_R3(alpha):
    t = mp.mpf(alpha) * mp.pi / 2
    return mp.sin(t) / mp.sin(t - mp.pi / 3)


def _mp_obj(y, beta, u, K):
    """Return (G, grad_y, Hess_y, x, B) at arbitrary precision."""
    z = [y[0], y[1], mp.mpf(0)]
    zm = max(z)
    e = [mp.exp(zi - zm) for zi in z]
    se = sum(e)
    x = [ei / se for ei in e]
    Bm = [[0, beta[0], beta[1]], [beta[0], 0, beta[2]], [beta[1], beta[2], 0]]
    Bi = [sum(Bm[i][j] * x[j] for j in range(3)) for i in range(3)]
    B = sum(Bi[i] * x[i] for i in range(3)) / 2
    h, h1, h2 = mp_h_derivs(B, u, K)
    G = mp.log(h) - sum(mp.log(xi) for xi in x)
    mu = h1 / h
    nu = h2 / h - mu * mu
    gx = [mu * Bi[i] - 1 / x[i] for i in range(3)]
    Hx = [[nu * Bi[i] * Bi[j] + mu * Bm[i][j] + (1 / x[i] ** 2 if i == j else 0)
           for j in range(3)] for i in range(3)]
    J = [[(x[i] if i == k else 0) - x[i] * x[k] for k in range(2)] for i in range(3)]
    s = sum(gx[i] * x[i] for i in range(3))
    g = [gx[k] * x[k] - x[k] * s for k in range(2)]
    H = [[sum(J[i][k] * Hx[i][j] * J[j][l] for i in range(3) for j in range(3))
          for l in range(2)] for k in range(2)]
    for k in range(2):
        for l in range(2):
            acc = 0
            for i in range(3):
                t1 = x[i] * ((1 if i == k else 0) - x[k]) * ((1 if i == l else 0) - x[l])
                t2 = x[i] * x[k] * ((1 if k == l else 0) - x[l])
                acc += gx[i] * (t1 - t2)
            H[k][l] += acc
    return G, g, H, x, B


def threshold_mp(beta, alpha, dps: int = 60, y0=None, max_iter: int = 200):
    """High-precision T_alpha(beta) by Newton on grad_y G = 0.

    Returns dict(T, x, y, grad_norm, hess_min_eig, iterations).  The float
    solution is used as the start unless `y0` is given.
    """
    with mp.workdps(dps + 10):
        if y0 is None:
            fb = threshold(np.asarray([float(b) for b in beta]), float(alpha))
            y0 = fb.y[0]
        beta_m = [mp.mpf(b) for b in beta]
        u, K = mp_uk(alpha)
        y = [mp.mpf(float(y0[0])), mp.mpf(float(y0[1]))]
        tol = mp.mpf(10) ** (-(dps + 3))
        it = 0
        for it in range(1, max_iter + 1):
            G, g, H, x, B = _mp_obj(y, beta_m, u, K)
            gn = mp.sqrt(g[0] ** 2 + g[1] ** 2)
            if gn < tol:
                break
            det = H[0][0] * H[1][1] - H[0][1] * H[1][0]
            if det > 0 and H[0][0] > 0:
                d0 = -(H[1][1] * g[0] - H[0][1] * g[1]) / det
                d1 = -(-H[1][0] * g[0] + H[0][0] * g[1]) / det
            else:
                d0, d1 = -g[0], -g[1]
            t = mp.mpf(1)
            for _ in range(60):
                Gt = _mp_obj([y[0] + t * d0, y[1] + t * d1], beta_m, u, K)[0]
                if Gt <= G:
                    break
                t /= 2
            y = [y[0] + t * d0, y[1] + t * d1]
        G, g, H, x, B = _mp_obj(y, beta_m, u, K)
        tr = H[0][0] + H[1][1]
        det = H[0][0] * H[1][1] - H[0][1] * H[1][0]
        lam_min = tr / 2 - mp.sqrt((tr / 2) ** 2 - det)
        return {
            "T": +mp.exp(G), "x": [+xi for xi in x], "y": y, "B": B,
            "grad_norm": mp.sqrt(g[0] ** 2 + g[1] ** 2), "hess_min_eig": lam_min,
            "iterations": it,
        }


def mp_h_alpha(b, alpha):
    u, K = mp_uk(alpha)
    return mp_h_derivs(mp.mpf(b), u, K)[0]


# ---------------------------------------------------------------------------
# matrices from invariants (C-13 loop coordinates)
# ---------------------------------------------------------------------------

def matrix_from_invariants(beta, kappa, *, p=(1.0, 1.0, 1.0), cw=None, branch: int = 0,
                           rng: np.random.Generator | None = None, dtype=float):
    """Construct a real 3x3 A with a_ii=-p_i and prescribed (beta, kappa).

    Uses kappa = sum(beta) - 2 - L3, g_ij = 1 - beta_ij = a_ij a_ji/(p_i p_j).
    Normalized matrix N = diag(1/p) A has unit negative diagonal; its clockwise
    3-cycle product ell = n12 n23 n31 must solve ell + G/ell = L3 with
    G = g12 g13 g23.  `cw` gives the relative magnitudes of (n12, n23, n31)
    (defaults to random); `branch` picks the root.  Returns None if infeasible
    (a real ell requires L3^2 >= 4G).
    Works with float or mpmath scalars (pass dtype=mp.mpf).
    """
    one = dtype(1)
    b12, b13, b23 = (dtype(b) for b in beta)
    kap = dtype(kappa)
    g12, g13, g23 = one - b12, one - b13, one - b23
    L3 = b12 + b13 + b23 - 2 - kap
    Gp = g12 * g13 * g23
    disc = L3 * L3 - 4 * Gp
    if disc < 0:
        return None
    sq = mp.sqrt(disc) if dtype is not float else np.sqrt(disc)
    roots = [(L3 + sq) / 2, (L3 - sq) / 2]
    if roots[0] == 0 or roots[1] == 0:          # G = 0: only the nonzero root works
        roots = [r for r in roots if r != 0] or [None]
    ell = roots[min(branch, len(roots) - 1)]
    if ell is None:
        return None
    if rng is None:
        rng = np.random.default_rng(0)
    if cw is None:
        cw = np.exp(rng.normal(size=3))
    c = [dtype(float(v)) for v in cw]
    # choose n12, n23, n31 with product ell and relative magnitudes c;
    # partners then fixed by the pair gains: n21 n12 = g12 etc.
    scale = (abs(ell) / (c[0] * c[1] * c[2])) ** (one / 3)
    sgn = 1 if ell > 0 else -1
    n12, n23, n31 = c[0] * scale * sgn, c[1] * scale, c[2] * scale
    n21 = g12 / n12
    n32 = g23 / n23
    n13 = g13 / n31
    N = [[-one, n12, n13], [n21, -one, n23], [n31, n32, -one]]
    P = [dtype(float(v)) if dtype is not float else float(v) for v in p]
    A = [[P[i] * N[i][j] for j in range(3)] for i in range(3)]
    if dtype is float:
        return np.array(A, dtype=float)
    return mp.matrix(A)


def invariants(A):
    """(beta, kappa) of a strict-P(-A) matrix; float numpy or mpmath matrix."""
    if isinstance(A, mp.matrix):
        a = [[A[i, j] for j in range(3)] for i in range(3)]
    else:
        a = np.asarray(A, dtype=float).tolist()
    p = [-a[i][i] for i in range(3)]
    m12 = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    m13 = a[0][0] * a[2][2] - a[0][2] * a[2][0]
    m23 = a[1][1] * a[2][2] - a[1][2] * a[2][1]
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
           - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    beta = (m12 / (p[0] * p[1]), m13 / (p[0] * p[2]), m23 / (p[1] * p[2]))
    kappa = -det / (p[0] * p[1] * p[2])
    return p, (m12, m13, m23), -det, beta, kappa


def invariants_batch(A: np.ndarray):
    """Vectorized (p, m, q, beta, kappa) for A of shape (n,3,3)."""
    p = -np.diagonal(A, axis1=1, axis2=2)
    m12 = A[:, 0, 0] * A[:, 1, 1] - A[:, 0, 1] * A[:, 1, 0]
    m13 = A[:, 0, 0] * A[:, 2, 2] - A[:, 0, 2] * A[:, 2, 0]
    m23 = A[:, 1, 1] * A[:, 2, 2] - A[:, 1, 2] * A[:, 2, 1]
    q = -np.linalg.det(A)
    m = np.stack([m12, m13, m23], axis=-1)
    beta = np.stack([m12 / (p[:, 0] * p[:, 1]), m13 / (p[:, 0] * p[:, 2]),
                     m23 / (p[:, 1] * p[:, 2])], axis=-1)
    kappa = q / np.prod(p, axis=-1)
    return p, m, q, beta, kappa

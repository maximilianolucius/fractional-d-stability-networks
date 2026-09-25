"""Direct spectral margin over the positive diagonal orbit (independent of C-10).

For a real n x n matrix A and 0 < alpha <= 1 the Matignon margin of D A is

    m(D) = min_i |arg lambda_i(D A)| - alpha pi / 2,

and A is fractionally D-stable iff inf_{D > 0} m(D) > 0 (strictly; the
infimum may be approached at infinity).  This module minimizes m over
log-ratios w = log(d_i/d_n), i = 1..n-1, **using only eigenvalues of the full
matrix** (LAPACK in float64, mpmath.eig at high precision).  It never uses the
principal-minor invariants, the simplex reduction or h_alpha, so its verdict is
independent of the C-10 proof.

A negative margin at some explicit D is a witness of non-membership (subject
to eigenvalue accuracy, controlled by the mpmath re-evaluation).  A positive
minimum is numerical evidence only.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np


def margins_batch(A: np.ndarray, W: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """Margins for matrices A (N,n,n) at log-diagonals W (N,M,n-1).

    Returns array (N, M).  d = exp([w, 0]).
    """
    N, M, k = W.shape
    n = k + 1
    d = np.exp(np.concatenate([W, np.zeros((N, M, 1))], axis=-1))   # (N,M,n)
    DA = d[:, :, :, None] * A[:, None, :, :]
    lam = np.linalg.eigvals(DA.reshape(-1, n, n)).reshape(N, M, n)
    ang = np.abs(np.angle(lam))
    ang = np.where(np.abs(lam) == 0.0, 0.0, ang)
    return ang.min(axis=-1) - (alpha * np.pi / 2.0)[:, None]


def _grid(n_free: int, half_width: float, step: float) -> np.ndarray:
    g = np.arange(-half_width, half_width + 1e-12, step)
    mesh = np.meshgrid(*([g] * n_free), indexing="ij")
    return np.stack([m.ravel() for m in mesh], axis=-1)


def _directions(n_free: int) -> np.ndarray:
    # all nonzero {-1,0,1}^k directions (pattern search stencil)
    mesh = np.meshgrid(*([np.array([-1.0, 0.0, 1.0])] * n_free), indexing="ij")
    D = np.stack([m.ravel() for m in mesh], axis=-1)
    D = D[np.any(D != 0, axis=1)]
    return D / np.linalg.norm(D, axis=1, keepdims=True)


def pattern_search(A: np.ndarray, alpha: np.ndarray, w0: np.ndarray, step0: float = 0.5,
                   min_step: float = 1e-11, max_iter: int = 400,
                   chunk: int = 4096) -> tuple[np.ndarray, np.ndarray]:
    """Batched compass/pattern search minimizing the margin from starts w0 (N,k)."""
    N, k = w0.shape
    dirs = _directions(k)
    w = w0.copy()
    best = np.empty(N)
    for s in range(0, N, chunk):
        sl = slice(s, min(s + chunk, N))
        best[sl] = margins_batch(A[sl], w[sl][:, None, :], alpha[sl])[:, 0]
    step = np.full(N, step0)
    active = np.ones(N, dtype=bool)
    for _ in range(max_iter):
        idx = np.nonzero(active)[0]
        if idx.size == 0:
            break
        for s in range(0, idx.size, chunk):
            ii = idx[s:s + chunk]
            trial = w[ii][:, None, :] + step[ii][:, None, None] * dirs[None, :, :]
            m = margins_batch(A[ii], trial, alpha[ii])
            j = np.argmin(m, axis=1)
            mj = m[np.arange(ii.size), j]
            imp = mj < best[ii]
            w[ii[imp]] = trial[np.arange(ii.size), j][imp]
            best[ii[imp]] = mj[imp]
            step[ii[~imp]] *= 0.5
            # mild expansion after success keeps long valleys cheap
            step[ii[imp]] = np.minimum(step[ii[imp]] * 1.5, 4.0)
        active &= step > min_step
    return w, best


def min_margin(A: np.ndarray, alpha, *, half_width: float = 10.0, step: float = 0.5,
               n_starts: int = 3, chunk: int = 64, prescale: bool = True) -> dict:
    """Global minimum of the margin over positive diagonal D for each A.

    Phase 1: log-grid [-hw, hw]^{n-1} (after row-normalizing by |a_ii| when
    `prescale`, which is itself a positive-diagonal move and changes nothing).
    Phase 2: pattern search from the `n_starts` best distinct grid local minima.
    Returns dict(margin, w, d) with d the full minimizing diagonal for the
    ORIGINAL matrix (i.e. including the prescaling).
    """
    A = np.asarray(A, dtype=float)
    N, n, _ = A.shape
    alpha = np.broadcast_to(np.asarray(alpha, dtype=float), (N,)).copy()
    scale = np.ones((N, n))
    if prescale:
        dg = np.abs(np.diagonal(A, axis1=1, axis2=2))
        ok = np.all(dg > 0, axis=1)
        scale[ok] = 1.0 / dg[ok]
    As = scale[:, :, None] * A
    grid = _grid(n - 1, half_width, step)
    G = grid.shape[0]
    starts = np.empty((N, n_starts, n - 1))
    for s in range(0, N, chunk):
        sl = slice(s, min(s + chunk, N))
        m = margins_batch(As[sl], np.broadcast_to(grid, (sl.stop - sl.start, G, n - 1)).copy(),
                          alpha[sl])
        order = np.argsort(m, axis=1)
        # pick n_starts starts that are mutually separated by > 2 grid steps
        for r in range(sl.stop - sl.start):
            chosen = []
            for j in order[r]:
                p = grid[j]
                if all(np.max(np.abs(p - q)) > 2.01 * step for q in chosen):
                    chosen.append(p)
                    if len(chosen) == n_starts:
                        break
            while len(chosen) < n_starts:
                chosen.append(chosen[0])
            starts[s + r] = np.array(chosen)
    Wall = starts.reshape(-1, n - 1)
    Aall = np.repeat(As, n_starts, axis=0)
    aall = np.repeat(alpha, n_starts)
    w, m = pattern_search(Aall, aall, Wall, step0=step / 2)
    m = m.reshape(N, n_starts)
    w = w.reshape(N, n_starts, n - 1)
    j = np.argmin(m, axis=1)
    wbest = w[np.arange(N), j]
    d = np.exp(np.concatenate([wbest, np.zeros((N, 1))], axis=1)) * scale
    return {"margin": m[np.arange(N), j], "w": wbest, "d": d,
            "margin_all_starts": m}


# ---------------------------------------------------------------------------
# arbitrary precision
# ---------------------------------------------------------------------------

def mp_margin(A, d, alpha, dps: int = 50):
    """Matignon margin of diag(d) A computed with mpmath.eig at `dps` digits.

    `A` may be an mp.matrix or nested list / numpy array of exact decimals;
    `d` a sequence of mp numbers or floats (taken as exact binary values).
    Returns (margin, eigenvalues).
    """
    with mp.workdps(dps):
        n = len(d)
        M = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                M[i, j] = mp.mpf(d[i]) * (A[i, j] if isinstance(A, mp.matrix) else mp.mpf(A[i][j]))
        ev = mp.eig(M, left=False, right=False)
        ang = min(abs(mp.arg(e)) for e in ev)
        return ang - mp.mpf(alpha) * mp.pi / 2, ev


def mp_pattern_search(A, alpha, w0, dps: int = 50, step0: float = 1e-3,
                      min_step: float | None = None, max_iter: int = 2000):
    """Independent high-precision refinement of the direct margin minimum."""
    with mp.workdps(dps):
        k = len(w0)
        n = k + 1
        dirs = _directions(k)
        w = [mp.mpf(float(v)) for v in w0]

        def f(wv):
            d = [mp.exp(v) for v in wv] + [mp.mpf(1)]
            return mp_margin(A, d, alpha, dps)[0]

        best = f(w)
        step = mp.mpf(step0)
        stop = mp.mpf(10) ** (-(dps // 2)) if min_step is None else mp.mpf(min_step)
        it = 0
        while step > stop and it < max_iter:
            it += 1
            improved = False
            for dv in dirs:
                trial = [w[i] + step * mp.mpf(float(dv[i])) for i in range(k)]
                v = f(trial)
                if v < best:
                    best, w, improved = v, trial, True
                    break
            step = step * 2 if improved else step / 2
        d = [mp.exp(v) for v in w] + [mp.mpf(1)]
        del n
        return best, w, d

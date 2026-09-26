"""Shared helpers for the Wave-1 compute scripts (pool, timing, JSON output)."""
from __future__ import annotations

import json
import os
import resource
import sys
import time
from multiprocessing import get_context

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RESULTS = os.path.join(ROOT, "computations", "results")
RAW = os.path.join(ROOT, "computations", "raw")        # never committed
os.makedirs(RESULTS, exist_ok=True)
os.makedirs(RAW, exist_ok=True)

# Good-neighbour default on the shared server; override with FDSN_WORKERS.
WORKERS = int(os.environ.get("FDSN_WORKERS", "16"))


def pool(n=None):
    return get_context("fork").Pool(n or WORKERS, initializer=_init_worker)


def _init_worker():
    os.environ["OMP_NUM_THREADS"] = "1"
    try:
        os.nice(5)
    except OSError:
        pass


def peak_rss_mb():
    self_ = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    child = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024
    return {"self_peak_rss_mb": round(self_, 1), "max_child_peak_rss_mb": round(child, 1)}


class Timer:
    def __init__(self):
        self.t0 = time.time()

    def __call__(self):
        return round(time.time() - self.t0, 2)


def to_jsonable(o):
    import mpmath as mp
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, np.ndarray):
        return to_jsonable(o.tolist())
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, mp.mpf):
        return mp.nstr(o, 40)
    if isinstance(o, float) and not np.isfinite(o):
        return str(o)
    return o


def dump(name, obj):
    path = os.path.join(RESULTS, name)
    with open(path, "w") as f:
        json.dump(to_jsonable(obj), f, indent=2)
    print("wrote", path, file=sys.stderr)
    return path


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)

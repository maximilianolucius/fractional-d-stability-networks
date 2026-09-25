"""Shared helpers for Wave-2 scripts (results dir, pool, JSON dump, env record)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RESULTS = os.path.join(ROOT, "computations", "results", "wave2")
FIG = os.path.join(RESULTS, "FIGURE_DATA")
os.makedirs(RESULTS, exist_ok=True)
sys.path.insert(0, os.path.join(ROOT, "computations", "scripts"))
from _common import Timer, log, peak_rss_mb, pool, to_jsonable  # noqa: E402,F401

BASELINE_SHA = "a8f73dca967e20e90c4dbb7e4aa77d2d6b170497"


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "n/a (synced working tree; see BASELINE_SHA)"


def dump(name, obj):
    path = os.path.join(RESULTS, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(to_jsonable(obj), f, indent=2)
    print("wrote", path, file=sys.stderr)
    return path


def stamp(extra=None):
    d = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "baseline_sha": BASELINE_SHA,
         "workers": int(os.environ.get("FDSN_WORKERS", "16"))}
    if extra:
        d.update(extra)
    return d

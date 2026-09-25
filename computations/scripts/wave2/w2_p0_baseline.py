"""Wave 2 P0 — frozen baseline record and environment."""
import json, os, platform, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w2_common import BASELINE_SHA, RESULTS, ROOT, dump, stamp

import mpmath, numpy, scipy, sympy
try:
    import hypothesis, numba
except Exception:
    hypothesis = numba = None

blas = {}
try:
    import threadpoolctl
    blas = threadpoolctl.threadpool_info()
except Exception:
    blas = {"note": "threadpoolctl unavailable", "OMP_NUM_THREADS": os.environ.get("OMP_NUM_THREADS")}

wave1 = json.load(open(os.path.join(ROOT, "computations", "results", "C10_STRESS_SUMMARY.json")))
report = open(os.path.join(ROOT, "research", "COMPUTE_WAVE1_FINAL_REPORT.md")).read()
env = stamp({
    "host": platform.node(), "platform": platform.platform(), "python": sys.version.split()[0],
    "cpu_count": os.cpu_count(),
    "cpu_model": next((l.split(":", 1)[1].strip() for l in open("/proc/cpuinfo") if l.startswith("model name")), None),
    "mem_total_gb": round(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2**30, 1),
    "numpy": numpy.__version__, "scipy": scipy.__version__, "mpmath": mpmath.__version__, "sympy": sympy.__version__,
    "hypothesis": getattr(hypothesis, "__version__", None), "numba": getattr(numba, "__version__", None),
    "blas_threading": blas, "OMP_NUM_THREADS": os.environ.get("OMP_NUM_THREADS"),
    "nice": os.nice(0),
    "commands": ["git checkout agent/compute-wave2-20260925", "pip install -e .[dev] sympy",
                 "OMP_NUM_THREADS=1 pytest -n 8", "python computations/scripts/wave2/w2_p0_baseline.py"],
    "wave1_check": {
        "GENUINE_C10_COUNTEREXAMPLES": wave1["GENUINE_C10_COUNTEREXAMPLES"], "VERDICT": wave1["VERDICT"],
        "final_report_status_line": [l for l in report.splitlines() if "Final status" in l][0],
        "total_C10_cases": wave1["total_C10_cases"],
        "note": "computations/results/P0_TEST_RESULT.txt on the Wave-1 branch reads '100 passed' (stale copy "
                "overwritten by a later rsync); the Wave-1 final report and the present run both give 121 passed.",
    },
})
dump("ENVIRONMENT.json", env)
print(json.dumps(env, indent=1, default=str)[:1500])

"""Record the compute environment (CPU, RAM, package versions) as JSON."""
import json, os, platform, subprocess, sys, datetime

def main(out):
    import numpy, scipy, mpmath
    info = {
        "utc": datetime.datetime.utcnow().isoformat(timespec="seconds"),
        "host": platform.node(), "platform": platform.platform(),
        "python": sys.version.split()[0],
        "cpu_count": os.cpu_count(),
        "cpu_model": next((l.split(":", 1)[1].strip() for l in open("/proc/cpuinfo") if l.startswith("model name")), None),
        "mem_total_gb": round(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2**30, 1),
        "numpy": numpy.__version__, "scipy": scipy.__version__, "mpmath": mpmath.__version__,
    }
    for mod in ("numba", "hypothesis", "sympy", "pytest"):
        try:
            info[mod] = __import__(mod).__version__
        except Exception:
            info[mod] = None
    try:
        info["git_sha"] = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        info["git_sha"] = "n/a (synced working tree)"
    json.dump(info, open(out, "w"), indent=2)
    print(json.dumps(info, indent=2))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "computations/results/ENVIRONMENT.json")

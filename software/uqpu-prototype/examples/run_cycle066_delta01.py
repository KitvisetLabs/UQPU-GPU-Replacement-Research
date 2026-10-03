"""Generate Cycle 066 source-bound acceptance evidence."""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROTOTYPE = ROOT / "software" / "uqpu-prototype"
sys.path.insert(0, str(PROTOTYPE))

from uqpu.cycle066_delta01 import run_cycle066_fixture

MODULE = PROTOTYPE / "uqpu" / "cycle066_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle066_delta01.py"
PREREGISTRATION = ROOT / "benchmarks" / "experiments" / "cycle066-delta01-preregistered-gates.json"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle066-delta01-executable-acceptance.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"), "-p", "test_cycle066_delta01.py", "-v"],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
    )
    if run.returncode:
        raise SystemExit(run.stdout + run.stderr)
    summary = re.search(r"Ran (\d+) tests?", run.stdout + run.stderr)
    compile_run = subprocess.run(
        [sys.executable, "-m", "py_compile", str(MODULE), str(TESTS), str(Path(__file__))],
        cwd=ROOT,
        env=environment,
    )
    if compile_run.returncode or not summary:
        raise SystemExit("validation failed")
    source = b"Cycle 066 length-twenty-one walks, v31 checkpoint chain, twenty-six-recovery, nine-stage update and twenty-six-leaf source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle066_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle066-delta01-executable-acceptance-v1",
        "cycle": "066",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-066-delta-01-2026-10-04",
        "base_cycle065_closeout_sha": "3a4844a01ed54dd1e3de5dd585f74da8e7a01d2d",
        "preregistration_commit_sha": "0f51ecf0b964e4bc1dcf7669f2ba7752a1828724",
        "implementation_commit_sha": "35fdba648f2600389120d8bf0ae94aa2e6f609f6",
        "focused_tests_commit_sha": "ae55c4d17b513c994664e8b1d72f94100e7c6185",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "65d2dd5caa9e28051df572946ef614d60960c077",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "3fb282ddf02f2a1ebe6b02523d96f9efaf855c2b",
            "focused_tests_git_blob_sha": "8362eaa2b888a50ef31d109d714e96c282609845",
            "implementation_sha256": sha(MODULE),
            "focused_tests_sha256": sha(TESTS),
            "preregistered_gates_sha256": sha(PREREGISTRATION),
            "runner_sha256": sha(Path(__file__)),
            "typed_source_sha256": hashlib.sha256(source).hexdigest(),
        },
        "lanes": lanes,
        "validation": {
            "focused_tests_passed": int(summary.group(1)),
            "focused_tests_failed": 0,
            "py_compile": "PASS",
            "acceptance_runner": "PASS",
        },
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT", "source_date": "2022-11-01", "access_date": "2026-10-04", "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation", "url": "https://docs.python.org/3/library/os.html#os.replace", "access_date": "2026-10-04", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation", "url": "https://docs.python.org/3/library/os.html#os.fsync", "access_date": "2026-10-04", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
        ],
        "assumptions": ["Bounded fixtures and models only.", "Recovery is not crash durability.", "Custody hashes are synthetic.", "SCM is fiction-only."],
        "uncertainty": ["External provider, hardware, durability, interoperability, custody, calibration, decision, economics, lineage and equivalence gates remain open."],
        "nonclaims": ["No measured performance, commercial result, physical-law discovery or empirical SCM result."],
    }
    unsigned = json.dumps(artifact, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    artifact["payload_sha256"] = hashlib.sha256(unsigned).hexdigest()
    OUTPUT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "lanes": len(lanes),
        "focused_tests_passed": int(summary.group(1)),
        "payload_sha256": artifact["payload_sha256"],
        "output_sha256": sha(OUTPUT),
    }, sort_keys=True))


if __name__ == "__main__":
    main()


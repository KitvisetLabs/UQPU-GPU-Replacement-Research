"""Generate Cycle 083 source-bound acceptance evidence."""
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

from uqpu.cycle083_delta01 import run_cycle083_fixture

MODULE = PROTOTYPE / "uqpu" / "cycle083_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle083_delta01.py"
PREREGISTRATION = ROOT / "benchmarks" / "experiments" / "cycle083-delta01-preregistered-gates.json"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle083-delta01-executable-acceptance.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"), "-p", "test_cycle083_delta01.py", "-v"],
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
    source = b"Cycle 083 length-thirty-eight walks, v48 checkpoint chain, forty-three-recovery, twenty-six-stage update and forty-three-leaf source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle083_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle083-delta01-executable-acceptance-v1",
        "cycle": "083",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-083-delta-01-2026-10-08",
        "base_cycle082_closeout_sha": "66f6bb424270e176d01caa6a01e1cb5230f6c645",
        "preregistration_commit_sha": "00ee5a7728fc72594c20d3dd01a90a915459d417",
        "implementation_commit_sha": "644e616384244a6e44e95466cf1a603954d020ad",
        "focused_tests_commit_sha": "ce82e28556fc91e7e4d33c3b9588f5e7191718ab",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "522d496b097adbae52853b6d2bbaa7bd0a126e10",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "b1f30ea70ab6ed36a7eefa2f02745df2315dfdf0",
            "focused_tests_git_blob_sha": "44c5476cd4ce4d81342085ef34a196828146c7be",
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

"""Generate Cycle 077 source-bound acceptance evidence."""
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

from uqpu.cycle077_delta01 import run_cycle077_fixture

MODULE = PROTOTYPE / "uqpu" / "cycle077_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle077_delta01.py"
PREREGISTRATION = ROOT / "benchmarks" / "experiments" / "cycle077-delta01-preregistered-gates.json"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle077-delta01-executable-acceptance.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"), "-p", "test_cycle077_delta01.py", "-v"],
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
    source = b"Cycle 077 length-thirty-two walks, v42 checkpoint chain, thirty-seven-recovery, twenty-stage update and thirty-seven-leaf source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle077_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle077-delta01-executable-acceptance-v1",
        "cycle": "077",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-077-delta-01-2026-10-07",
        "base_cycle076_closeout_sha": "aeeb440481706599cec1aa20eb1a6ba67178cb6b",
        "preregistration_commit_sha": "de391c83728dfc184f0100816fe3fc0a074d2dd6",
        "implementation_commit_sha": "d3292923eb6b35bc2c799cdf17e48bfb711b4b2d",
        "focused_tests_commit_sha": "d5643e9238a485285a977e3bc19f1f1a39f30221",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "4e6e57f2d979bbbf87de30665abbd6fefa653b8a",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "c4e7636c2c3b28cdbbff11b7ceab9412de03c139",
            "focused_tests_git_blob_sha": "f1f2e93478d9bf9481dc12c39b667518771f490b",
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

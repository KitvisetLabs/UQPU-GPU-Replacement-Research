"""Generate Cycle 047 source-bound acceptance evidence."""
# Exact-SHA retry checkpoint: run 36841862770 retained an in-progress Python 3.12
# unit-test step after the 3.10 and 3.11 matrix legs had completed successfully.
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
PROTOTYPE = ROOT / "software" / "uqpu-prototype"
sys.path.insert(0, str(PROTOTYPE))

from uqpu.cycle047_delta01 import run_cycle047_fixture

MODULE = PROTOTYPE / "uqpu" / "cycle047_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle047_delta01.py"
PREREGISTRATION = ROOT / "benchmarks" / "experiments" / "cycle047-delta01-preregistered-gates.json"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle047-delta01-executable-acceptance.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"), "-p", "test_cycle047_delta01.py", "-v"],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
    )
    if run.returncode:
        raise SystemExit(run.stdout + run.stderr)
    summary = re.search(r"Ran (\d+) tests?", run.stdout + run.stderr)
    compile_run = subprocess.run([sys.executable, "-m", "py_compile", str(MODULE), str(TESTS), str(Path(__file__))], cwd=ROOT, env=environment)
    if compile_run.returncode or not summary:
        raise SystemExit("validation failed")
    source = b"Cycle 047 quotient-path, v12 checkpoint, seven-recovery and seven-leaf source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle047_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle047-delta01-executable-acceptance-v1",
        "cycle": "047",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-047-delta-01-2026-10-01",
        "base_cycle046_closeout_sha": "21df2c312280915daeb191b88cef5152b6c62ee7",
        "preregistration_commit_sha": "e3a0ad38e8f81847fb5fdef5d5a11400172f2480",
        "implementation_commit_sha": "eee090d3ac74af2786be2b1586d7b9f5c3394390",
        "focused_tests_commit_sha": "2dcacf70408aaf6aa770a8f35a2ff63af867debe",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "06f96aba0d288ebe619a69cb2394687e113b81aa",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "183a10ea9858f23624ae93d2affc9b999e5b8946",
            "focused_tests_git_blob_sha": "e301b02febffc5d54273cd0b1160b548fe2ddd1c",
            "implementation_sha256": sha(MODULE),
            "focused_tests_sha256": sha(TESTS),
            "preregistered_gates_sha256": sha(PREREGISTRATION),
            "runner_sha256": sha(Path(__file__)),
            "typed_source_sha256": hashlib.sha256(source).hexdigest(),
        },
        "lanes": lanes,
        "validation": {"focused_tests_passed": int(summary.group(1)), "focused_tests_failed": 0, "py_compile": "PASS", "acceptance_runner": "PASS"},
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT", "source_date": "2022-11-01", "access_date": "2026-10-01", "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation", "url": "https://docs.python.org/3/library/os.html#os.replace", "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation", "url": "https://docs.python.org/3/library/os.html#os.fsync", "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
        ],
        "assumptions": ["Bounded fixtures and models only.", "Recovery is not crash durability.", "Custody hashes are synthetic.", "SCM is fiction-only."],
        "uncertainty": ["External provider, hardware, durability, interoperability, custody, calibration, decision, lineage and equivalence gates remain open."],
        "nonclaims": ["No measured performance, commercial result, physical-law discovery or empirical SCM result."],
    }
    unsigned = json.dumps(artifact, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    artifact["payload_sha256"] = hashlib.sha256(unsigned).hexdigest()
    OUTPUT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"lanes": len(lanes), "focused_tests_passed": int(summary.group(1)), "payload_sha256": artifact["payload_sha256"], "output_sha256": sha(OUTPUT)}, sort_keys=True))


if __name__ == "__main__":
    main()

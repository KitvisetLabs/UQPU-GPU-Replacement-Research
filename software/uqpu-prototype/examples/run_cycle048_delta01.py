"""Generate Cycle 048 source-bound acceptance evidence."""
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

from uqpu.cycle048_delta01 import run_cycle048_fixture

MODULE = PROTOTYPE / "uqpu" / "cycle048_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle048_delta01.py"
PREREGISTRATION = ROOT / "benchmarks" / "experiments" / "cycle048-delta01-preregistered-gates.json"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle048-delta01-executable-acceptance.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"), "-p", "test_cycle048_delta01.py", "-v"],
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
    source = b"Cycle 048 length-three paths, v13 checkpoint chain, eight-recovery and eight-leaf source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle048_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle048-delta01-executable-acceptance-v1",
        "cycle": "048",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-048-delta-01-2026-10-01",
        "base_cycle047_closeout_sha": "65b83a6ce4504de9c2e299a8a296a48f7ba8b474",
        "preregistration_commit_sha": "dee234b9aace73ff8bf63eb0ad3cd145e9e183f0",
        "implementation_commit_sha": "7056f90f8378fe418628019e87980196d8f8327e",
        "focused_tests_commit_sha": "320916c7576fa5371699c8c714742c25f75f7aad",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "96aaa37ef1e6499d71fef87d0639d427c4b0badc",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "2e019beb84420eed996d059092d51efe62c0324f",
            "focused_tests_git_blob_sha": "8b5e981ec82678b40c210a8481597d76bcd6ca6e",
            "implementation_sha256": sha(MODULE),
            "focused_tests_sha256": sha(TESTS),
            "preregistered_gates_sha256": sha(PREREGISTRATION),
            "runner_sha256": sha(Path(__file__)),
            "typed_source_sha256": hashlib.sha256(source).hexdigest(),
        },
        "lanes": lanes,
        "validation": {"focused_tests_passed": int(summary.group(1)), "focused_tests_failed": 0, "py_compile": "PASS", "acceptance_runner": "PASS"},
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT", "source_date": "2022-11-01", "access_date": "2026-10-03", "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation", "url": "https://docs.python.org/3/library/os.html#os.replace", "access_date": "2026-10-03", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation", "url": "https://docs.python.org/3/library/os.html#os.fsync", "access_date": "2026-10-03", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
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

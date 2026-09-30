"""Generate the source-bound Cycle 039 executable acceptance artifact."""
from __future__ import annotations

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

from uqpu.cycle039_delta01 import run_cycle039_fixture  # noqa: E402

MODULE = PROTOTYPE / "uqpu" / "cycle039_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle039_delta01.py"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle039-delta01-executable-acceptance.json"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    test_run = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s",
                               str(PROTOTYPE / "tests"), "-p", "test_cycle039_delta01.py", "-v"],
                              cwd=ROOT, env=environment, text=True, capture_output=True)
    if test_run.returncode:
        raise SystemExit(test_run.stdout + test_run.stderr)
    summary = re.search(r"Ran (\d+) tests?", test_run.stdout + test_run.stderr)
    if not summary:
        raise RuntimeError("unittest summary unavailable")
    compile_run = subprocess.run([sys.executable, "-m", "py_compile", str(MODULE), str(TESTS),
                                  str(Path(__file__))], cwd=ROOT, env=environment,
                                 text=True, capture_output=True)
    if compile_run.returncode:
        raise SystemExit(compile_run.stdout + compile_run.stderr)
    source = b"Cycle 039 provenance, frontier and schedule-slack acceptance source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle039_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle039-delta01-executable-acceptance-v1", "cycle": "039",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN", "lane_count": len(lanes),
        "branch": "research/cycle-039-delta-01-2026-10-01",
        "base_cycle038_closeout_sha": "cec07614c17b4b43fe23a29b9f0e2422590c964f",
        "preregistration_commit_sha": "8f5e0c9e34b843b6e809c39b668ea5b6016576d2",
        "implementation_commit_sha": "37b6b64cd4c980fa49392385d49eb4f597dda97b",
        "focused_tests_commit_sha": "625cc874d785e3ab3337e12a3e5788b2a082086b",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "4949c9d0ea61e90995d687f9f616deaf86dba0f1",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "85009290d2f940865b401132f98bae88d70d3c80",
            "focused_tests_git_blob_sha": "8742ff2b370bc745a408d76ad502f7f8660b7b38",
            "implementation_sha256": file_sha256(MODULE), "focused_tests_sha256": file_sha256(TESTS),
            "runner_sha256": file_sha256(Path(__file__)), "typed_source_sha256": hashlib.sha256(source).hexdigest()},
        "lanes": lanes,
        "validation": {"focused_tests_passed": int(summary.group(1)), "focused_tests_failed": 0,
                       "py_compile": "PASS", "acceptance_runner": "PASS"},
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
             "source_date": "2022-11-01", "access_date": "2026-10-01",
             "locator": "sections 4.3.6, 4.3.7, 4.3.9, 4.3.11, 4.3.12 and 4.3.14–4.3.16",
             "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation", "url": "https://docs.python.org/3/library/os.html#os.replace",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation", "url": "https://docs.python.org/3/library/os.html#os.fsync",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"}],
        "assumptions": ["All graph, receipt, archive, custody, covariance, ranking, lineage and operator inputs are bounded fixtures or models.",
                        "Injected cross-device rename and journal failures do not establish crash or power-loss durability.",
                        "Custody receipt signatures are synthetic hashes, not cryptographic signatures or authority evidence.",
                        "SCM records are fiction-only and cannot be cast to empirical evidence."],
        "uncertainty": ["Provider authorization and billing, crash durability, independent archive interoperability, operational custody, measured covariance and calibration, owner priorities, independent equation derivation, real held-out equivalence and target hardware evidence remain open."],
        "nonclaims": ["No measured QPU or GPU performance, scaling or quantum advantage.",
                      "No provider execution, invoice, commercial economics or capital result.",
                      "No crash durability, cryptographic signature claim, calibration, physical sample, new physical law, AI equivalence or empirical SCM result."]}
    unsigned = json.dumps(artifact, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    artifact["payload_sha256"] = hashlib.sha256(unsigned).hexdigest()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(artifact, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"lanes": len(lanes), "focused_tests_passed": int(summary.group(1)),
                      "payload_sha256": artifact["payload_sha256"],
                      "output_sha256": file_sha256(OUTPUT)}, sort_keys=True))


if __name__ == "__main__":
    main()

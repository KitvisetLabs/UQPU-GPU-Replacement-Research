"""Generate the source-bound Cycle 038 executable acceptance artifact."""
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

from uqpu.cycle038_delta01 import run_cycle038_fixture  # noqa: E402

MODULE = PROTOTYPE / "uqpu" / "cycle038_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle038_delta01.py"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle038-delta01-executable-acceptance.json"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    test_run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"),
         "-p", "test_cycle038_delta01.py", "-v"],
        cwd=ROOT, env=environment, text=True, capture_output=True,
    )
    if test_run.returncode:
        raise SystemExit(test_run.stdout + test_run.stderr)
    summary = re.search(r"Ran (\d+) tests?", test_run.stdout + test_run.stderr)
    if not summary:
        raise RuntimeError("unittest summary unavailable")
    compile_run = subprocess.run(
        [sys.executable, "-m", "py_compile", str(MODULE), str(TESTS), str(Path(__file__))],
        cwd=ROOT, env=environment, text=True, capture_output=True,
    )
    if compile_run.returncode:
        raise SystemExit(compile_run.stdout + compile_run.stderr)

    source = b"Cycle 038 schema-default, multiproof and work-schedule acceptance source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle038_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle038-delta01-executable-acceptance-v1",
        "cycle": "038",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN",
        "lane_count": len(lanes),
        "branch": "research/cycle-038-delta-01-2026-10-01",
        "base_cycle037_closeout_sha": "0f932fa74c86267a25f3cf6e8b095bfd1144ce68",
        "preregistration_commit_sha": "b88a3ad966c5d3226a1fe81a4e9bcbe6cfc9c298",
        "implementation_commit_sha": "2eae04ec95be04c0bb9259d54c7677989d7626c3",
        "focused_tests_commit_sha": "102580b25d9320fff1ca7499d3f78e137f401a38",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "b3614259491da9e8d0e3fc4a258c5f9b3b843f36",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "9ab85f0a197e78d93f0ab4f6600449d36e8a8b41",
            "focused_tests_git_blob_sha": "39640d2169fbd4c60d6a82c1bd8e88209f9cf3de",
            "implementation_sha256": file_sha256(MODULE),
            "focused_tests_sha256": file_sha256(TESTS),
            "runner_sha256": file_sha256(Path(__file__)),
            "typed_source_sha256": hashlib.sha256(source).hexdigest(),
        },
        "lanes": lanes,
        "validation": {"focused_tests_passed": int(summary.group(1)),
                       "focused_tests_failed": 0, "py_compile": "PASS",
                       "acceptance_runner": "PASS"},
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL",
             "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
             "source_date": "2022-11-01", "access_date": "2026-10-01",
             "locator": "sections 4.3.6, 4.3.7, 4.3.9, 4.3.11, 4.3.12 and 4.3.14–4.3.16",
             "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation",
             "url": "https://docs.python.org/3/library/os.html#os.replace",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation",
             "url": "https://docs.python.org/3/library/os.html#os.fsync",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
        ],
        "assumptions": [
            "All graph, receipt, archive, custody, covariance, ranking, lineage and operator inputs are bounded fixtures or models.",
            "Partial-write, fsync, rename and cleanup failure paths do not establish crash or power-loss durability.",
            "Custody receipt signatures are synthetic hashes, not cryptographic signatures or authority evidence.",
            "SCM records are fiction-only and cannot be cast to empirical evidence.",
        ],
        "uncertainty": [
            "Provider authorization and billing, crash durability, independent archive interoperability, operational custody, measured covariance and calibration, owner priorities, independent equation derivation, real held-out equivalence and target hardware evidence remain open."
        ],
        "nonclaims": [
            "No measured QPU or GPU performance, scaling or quantum advantage.",
            "No provider execution, invoice, commercial economics or capital result.",
            "No crash durability, cryptographic signature claim, calibration, physical sample, new physical law, AI equivalence or empirical SCM result.",
        ],
    }
    unsigned = json.dumps(artifact, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    artifact["payload_sha256"] = hashlib.sha256(unsigned).hexdigest()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(artifact, indent=2, sort_keys=True, allow_nan=False) + "\n",
                      encoding="utf-8")
    print(json.dumps({"lanes": len(lanes), "focused_tests_passed": int(summary.group(1)),
                      "payload_sha256": artifact["payload_sha256"],
                      "output_sha256": file_sha256(OUTPUT)}, sort_keys=True))


if __name__ == "__main__":
    main()

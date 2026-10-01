"""Generate the source-bound Cycle 043 executable acceptance artifact."""
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

from uqpu.cycle043_delta01 import run_cycle043_fixture  # noqa: E402

MODULE = PROTOTYPE / "uqpu" / "cycle043_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle043_delta01.py"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle043-delta01-executable-acceptance.json"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    test_run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"),
         "-p", "test_cycle043_delta01.py", "-v"], cwd=ROOT, env=environment,
        text=True, capture_output=True,
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
    source = b"Cycle 043 double-coset, checkpoint-merge, triple-recovery and three-leaf multiproof source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle043_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle043-delta01-executable-acceptance-v1", "cycle": "043",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN", "lane_count": len(lanes),
        "branch": "research/cycle-043-delta-01-2026-10-01",
        "base_cycle042_closeout_sha": "42a08afc73ce104e4314b482a0ff438455d7aba1",
        "preregistration_commit_sha": "51cc7aceef91148317766e12a1804bd32be5c95e",
        "implementation_commit_sha": "419f5450507c5ccaacbfe0ef974fc7ed7fb71579",
        "focused_tests_commit_sha": "9b5974dea21ce62e36d8bcd890bbc1c17cc2224a",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "c0c287d32534b68c98036aa628ce5b05864912de",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "a0634cab26715b73e5fc8ad60f5f0986a71fd97a",
            "focused_tests_git_blob_sha": "0d4fac5f34cc6ae1a6e289a240fdd0f02d3ef7a6",
            "implementation_sha256": file_sha256(MODULE), "focused_tests_sha256": file_sha256(TESTS),
            "runner_sha256": file_sha256(Path(__file__)),
            "typed_source_sha256": hashlib.sha256(source).hexdigest(),
        },
        "lanes": lanes,
        "validation": {"focused_tests_passed": int(summary.group(1)), "focused_tests_failed": 0,
                       "py_compile": "PASS", "acceptance_runner": "PASS"},
        "source_evidence": [
            {"title": "PKWARE APPNOTE v6.3.10 FINAL",
             "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
             "source_date": "2022-11-01", "access_date": "2026-10-01",
             "locator": "sections 4.3.7, 4.3.9, 4.3.11, 4.3.15 and 4.3.16",
             "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
            {"title": "Python os.replace documentation",
             "url": "https://docs.python.org/3/library/os.html#os.replace",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
            {"title": "Python os.fsync documentation",
             "url": "https://docs.python.org/3/library/os.html#os.fsync",
             "access_date": "2026-10-01", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
        ],
        "assumptions": ["All inputs are bounded fixtures or models.",
                        "Injected triple recovery does not establish crash or power-loss durability.",
                        "Custody hashes are synthetic, not signatures.",
                        "SCM records are fiction-only."],
        "uncertainty": ["Provider, hardware, durability, interoperability, custody, calibration, decision, lineage and equivalence gates remain open."],
        "nonclaims": ["No measured QPU/GPU performance, scaling or quantum advantage.",
                      "No provider execution, invoice, commercial economics or capital result.",
                      "No crash durability, signature claim, calibration, physical sample, new physical law, AI equivalence or empirical SCM result."],
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

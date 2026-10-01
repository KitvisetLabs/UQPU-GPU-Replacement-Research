"""Generate the source-bound Cycle 044 executable acceptance artifact."""
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

from uqpu.cycle044_delta01 import run_cycle044_fixture  # noqa: E402

MODULE = PROTOTYPE / "uqpu" / "cycle044_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle044_delta01.py"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle044-delta01-executable-acceptance.json"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    test_run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"),
         "-p", "test_cycle044_delta01.py", "-v"], cwd=ROOT, env=environment,
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
    source = b"Cycle 044 representative, lineage, four-recovery and four-leaf multiproof source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle044_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle044-delta01-executable-acceptance-v1", "cycle": "044",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN", "lane_count": len(lanes),
        "branch": "research/cycle-044-delta-01-2026-10-01",
        "base_cycle043_closeout_sha": "9fc66217d1e2131c71162631a316e35b760f8389",
        "preregistration_commit_sha": "8d34ab0ffb056c8283ce1ada0c8533d40e1622bb",
        "implementation_commit_sha": "c3aefd082be096b9311b31fd6e179fe8128c18b8",
        "focused_tests_commit_sha": "1122365f40fd9445fc9ecaef4b87b47856707677",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "9e965299e841f028a3ce14da36460013eddbca3f",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "da96947b215c308b5973a3c2f4458e8d62563934",
            "focused_tests_git_blob_sha": "e5335cf450e583df418932ddbaeaa1a63012701a",
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
                        "Injected four-journal recovery does not establish crash or power-loss durability.",
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

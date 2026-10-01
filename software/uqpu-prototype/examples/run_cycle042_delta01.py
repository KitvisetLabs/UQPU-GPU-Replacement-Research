"""Generate the source-bound Cycle 042 executable acceptance artifact."""
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

from uqpu.cycle042_delta01 import run_cycle042_fixture  # noqa: E402

MODULE = PROTOTYPE / "uqpu" / "cycle042_delta01.py"
TESTS = PROTOTYPE / "tests" / "test_cycle042_delta01.py"
OUTPUT = ROOT / "benchmarks" / "results" / "cycle042-delta01-executable-acceptance.json"


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE) + os.pathsep + environment.get("PYTHONPATH", "")
    test_run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(PROTOTYPE / "tests"),
         "-p", "test_cycle042_delta01.py", "-v"], cwd=ROOT, env=environment,
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
    source = b"Cycle 042 coset, checkpoint, dual-recovery and multiproof acceptance source\n"
    with tempfile.TemporaryDirectory() as root:
        lanes = run_cycle042_fixture(source, root)
    artifact = {
        "schema": "uqpu-cycle042-delta01-executable-acceptance-v1", "cycle": "042",
        "status": "PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN", "lane_count": len(lanes),
        "branch": "research/cycle-042-delta-01-2026-10-01",
        "base_cycle041_closeout_sha": "332bffbc4e032bc1a009adfd90fe71487edec860",
        "preregistration_commit_sha": "9db68ea6560596ca3f6c1c75ab3f5f3d4d0c1c37",
        "implementation_commit_sha": "8674044cda23669e4f5320977d37b671ef7407a6",
        "focused_tests_commit_sha": "1e44d29136e68bc6d4ff7e539543a8968a91366a",
        "source_identity": {
            "preregistered_gates_git_blob_sha": "e61fd0697dbc1ada11cbbb1376bb288890ce3709",
            "portfolio_git_blob_sha": "27a8da9b68c6e896c67b38e9e6a49525c181dc73",
            "implementation_git_blob_sha": "28798eb2ab48cc6f21d1e86b7c68d006568333a5",
            "focused_tests_git_blob_sha": "3a63250cd4a14579144f6c3c2b3fb18e5ac9a6c4",
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
                        "Injected dual recovery does not establish crash or power-loss durability.",
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

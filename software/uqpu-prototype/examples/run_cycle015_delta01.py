"""Write the deterministic Cycle 015 local acceptance artifact."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from uqpu.cycle015_delta01 import LANES, run_cycle015_fixture

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md"
MODULE = ROOT / "software/uqpu-prototype/uqpu/cycle015_delta01.py"
TESTS = ROOT / "software/uqpu-prototype/tests/test_cycle015_delta01.py"
PREREG = ROOT / "benchmarks/experiments/cycle015-delta01-preregistered-gates.json"


def main():
    source_bytes = SOURCE.read_bytes()
    result = run_cycle015_fixture(source_bytes)
    if set(result) != set(LANES):
        raise SystemExit("lane acceptance set mismatch")
    output = {
        "schema": "uqpu-cycle015-delta01-executable-acceptance-v1",
        "cycle": "015",
        "delta": "01",
        "date": "2026-09-28",
        "branch": "research/cycle-015-delta-01-2026-09-28",
        "base_closeout": "6114b36912f2e3b93a6571ee45091f831e9c7eb6",
        "lane_count": len(LANES),
        "all_lane_fixture_acceptance_passed": True,
        "all_external_gates_closed": False,
        "source_hashes": {
            "umrl": hashlib.sha256(source_bytes).hexdigest(),
            "cycle015_module": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
            "cycle015_tests": hashlib.sha256(TESTS.read_bytes()).hexdigest(),
            "preregistered_gates": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        },
        "lanes": result,
        "nonclaims": [
            "No measured QPU/GPU performance, quantum advantage, or GPU replacement.",
            "No provider execution, authorization, receipt signature, or invoice.",
            "No crash/power-loss durability, calibrated device/custody evidence, or commercial economics.",
            "No physical-law claim; SCM remains fiction-only with empirical coupling null.",
            "No AI functional-equivalence claim and no QOS hardware claim.",
        ],
    }
    path = ROOT / "benchmarks/results/cycle015-delta01-executable-acceptance.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(path.relative_to(ROOT)), "lanes": len(result), "status": "PASS_LOCAL_FIXTURES"}, sort_keys=True))


if __name__ == "__main__":
    main()

"""Write the deterministic Cycle 016 local acceptance artifact."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from uqpu.cycle016_delta01 import LANES, run_cycle016_fixture

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md"
MODULE = ROOT / "software/uqpu-prototype/uqpu/cycle016_delta01.py"
TESTS = ROOT / "software/uqpu-prototype/tests/test_cycle016_delta01.py"
PREREG = ROOT / "benchmarks/experiments/cycle016-delta01-preregistered-gates.json"


def main():
    source = SOURCE.read_bytes()
    lanes = run_cycle016_fixture(source)
    if set(lanes) != set(LANES):
        raise SystemExit("lane acceptance set mismatch")
    payload = {
        "schema": "uqpu-cycle016-delta01-executable-acceptance-v1",
        "cycle": "016", "delta": "01", "date": "2026-09-28",
        "branch": "research/cycle-016-delta-01-2026-09-28",
        "base_closeout": "736d9513af8500f881b858ee83f755041b830029",
        "lane_count": len(LANES), "all_lane_fixture_acceptance_passed": True,
        "all_external_gates_closed": False,
        "source_hashes": {
            "umrl": hashlib.sha256(source).hexdigest(),
            "cycle016_module": hashlib.sha256(MODULE.read_bytes()).hexdigest(),
            "cycle016_tests": hashlib.sha256(TESTS.read_bytes()).hexdigest(),
            "preregistered_gates": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        },
        "lanes": lanes,
        "nonclaims": [
            "No measured QPU/GPU performance, quantum advantage or GPU replacement.",
            "No provider authorization, execution, provider signature, job or invoice.",
            "No crash durability, calibrated physical sample or commercial economics.",
            "No physical-law, AI-equivalence, capital or empirical SCM claim; QOS hardware null."
        ],
    }
    out = ROOT / "benchmarks/results/cycle016-delta01-executable-acceptance.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(out.relative_to(ROOT)), "lane_count": len(lanes), "status": "PASS_LOCAL_FIXTURES"}, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate Cycle 014's local synthetic/fiction-only acceptance artifact."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from uqpu.cycle014_delta01 import LANES, run_cycle014_fixture  # noqa: E402

REPO = ROOT.parents[1]
OUTPUT = REPO / "benchmarks/results/cycle014-delta01-executable-acceptance.json"
source_paths = {
    "preregistered_gates": REPO / "benchmarks/experiments/cycle014-delta01-preregistered-gates.json",
    "module": ROOT / "uqpu/cycle014_delta01.py",
    "tests": ROOT / "tests/test_cycle014_delta01.py",
    "runner": Path(__file__).resolve(),
    "umrl_source": REPO / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
}
lanes = run_cycle014_fixture()
result = {
    "schema": "uqpu-cycle014-delta01-executable-acceptance-v1",
    "cycle": "014",
    "delta": "01",
    "date": "2026-09-28",
    "branch": "research/cycle-014-delta-01-2026-09-28",
    "base_closeout": "06218a1f6ad053fe96d1086305431e1260a2d5d4",
    "evidence_class": "LOCAL_SYNTHETIC_AND_FICTION_ONLY",
    "lane_count": len(LANES),
    "status": "PASS_LOCAL",
    "source_sha256": {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in source_paths.items()
    },
    "lanes": lanes,
    "nonclaims": [
        "no QPU or GPU performance result",
        "no provider execution, job identifier, or invoice",
        "subprocess termination fixture does not establish crash or power-loss durability",
        "ZIP64 fixture checks metadata only and reads no archive payload",
        "cost, priority, covariance, and AI metrics are synthetic/model-only",
        "SCM remains fiction-only; empirical coupling is null",
        "QOS/QSVT hardware receipt remains null",
    ],
}
result["payload_sha256"] = hashlib.sha256(
    json.dumps(lanes, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
).hexdigest()
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "artifact": str(OUTPUT),
    "lane_count": result["lane_count"],
    "status": result["status"],
    "payload_sha256": result["payload_sha256"],
    "artifact_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
}, indent=2))

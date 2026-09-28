#!/usr/bin/env python3
"""Generate Cycle 013's deterministic local synthetic/fiction-only artifact."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from uqpu.cycle013_delta01 import run_cycle013_fixture  # noqa: E402

REPO = ROOT.parents[1]
OUTPUT = REPO / "benchmarks/results/cycle013-delta01-executable-acceptance.json"
source_paths = {
    "preregistered_gates": REPO / "benchmarks/experiments/cycle013-delta01-preregistered-gates.json",
    "module": ROOT / "uqpu/cycle013_delta01.py",
    "tests": ROOT / "tests/test_cycle013_delta01.py",
    "runner": Path(__file__).resolve(),
    "umrl_source": REPO / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
}
registry_source_bytes = source_paths["umrl_source"].read_bytes()
registry_sha256 = hashlib.sha256(registry_source_bytes).hexdigest()
lanes = run_cycle013_fixture(registry_sha256, registry_source_bytes)
result = {
    "schema": "uqpu-cycle013-delta01-executable-acceptance-v1",
    "cycle": "013",
    "delta": "01",
    "date": "2026-09-28",
    "branch": "research/cycle-013-delta-01-2026-09-28",
    "base_closeout": "707750fb4bec7d701d2c6c35f155c3e381c72b00",
    "evidence_class": "LOCAL_SYNTHETIC_AND_FICTION_ONLY",
    "lane_count": 12,
    "status": "PASS_LOCAL",
    "source_sha256": {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in source_paths.items()
    },
    "lanes": lanes,
    "nonclaims": [
        "no QPU or GPU result",
        "no provider execution or bill",
        "no measured material, device, or lifecycle cost",
        "no new physical law or hardware advantage",
        "SCM remains fiction-only; empirical coupling is null",
        "priority and cost intervals are model/synthetic outputs only",
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

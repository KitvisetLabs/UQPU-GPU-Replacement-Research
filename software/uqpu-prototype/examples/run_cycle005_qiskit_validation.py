"""Cross-check persisted Cycle 004 Qiskit output and the Cycle 005 grammar gate."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from uqpu.cycle005_delta01 import build_qos_gate


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
PERSISTED = ROOT / "benchmarks/results/cycle005-delta01-cycle004-qiskit-ci-parse.json"
CYCLE004_RUNNER = ROOT / "software/uqpu-prototype/examples/run_cycle004_qiskit_validation.py"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_cycle004_runner():
    spec = importlib.util.spec_from_file_location("cycle004_qiskit_runner", CYCLE004_RUNNER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run() -> dict:
    raw = MANIFEST.read_bytes()
    manifest = json.loads(raw)
    persisted = _load(PERSISTED)
    gate = build_qos_gate(manifest, persisted, hashlib.sha256(raw).hexdigest())
    if not gate["all_checks_passed"]:
        raise AssertionError(f"Cycle 005 persisted/grammar gate failed: {gate['errors']}")
    live = _load_cycle004_runner().run(MANIFEST)
    fields = ("candidate_id", "qasm_sha256", "num_qubits", "num_clbits",
              "operation_counts", "logical_depth_qiskit", "measurement_map", "parse_passed")
    persisted_rows = {row["candidate_id"]: row for row in persisted["rows"]}
    mismatches = []
    for row in live["rows"]:
        saved = persisted_rows.get(row["candidate_id"])
        if saved is None:
            mismatches.append(f"missing:{row['candidate_id']}")
            continue
        normalized = dict(saved)
        normalized["measurement_map"] = {
            int(key): value for key, value in saved["measurement_map"].items()
        }
        for field in fields:
            if row[field] != normalized[field]:
                mismatches.append(f"{row['candidate_id']}:{field}")
    if mismatches:
        raise AssertionError(f"persisted Qiskit output drift: {mismatches}")
    return {
        "schema": "uqpu-cycle005-live-persisted-qiskit-and-grammar-crosscheck-v1",
        "all_passed": True,
        "qiskit_version": live["qiskit_version"],
        "candidate_count": len(live["rows"]),
        "persisted_provenance": persisted["provenance"],
        "grammar_subset": gate["stdlib_grammar_rows"][0]["grammar_subset"],
        "provider_transpile": gate["provider_transpile"],
        "hardware_executed": False,
        "evidence_class": "LIVE_PINNED_SDK_RECHECK_PLUS_LIMITED_GRAMMAR_CHECK_NOT_PROVIDER_VALIDATION",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

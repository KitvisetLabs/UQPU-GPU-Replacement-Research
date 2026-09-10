"""Batch 017: extract calibration properties only for routed physical qubits/operations.

Uses the saved FakeKingston system snapshot. No live account/backend access and no paid job.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from uqpu.target_calibration import active_instruction_calibration


def run(input_path: Path):
    from qiskit import qasm3, transpile
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    data = json.loads(input_path.read_text())
    fixture = next(row for row in data["fixtures"] if row["name"] == "triangle")
    payload = next(row for row in fixture["providers"] if row["provider_id"] == "ibm_quantum")
    if hashlib.sha256(payload["payload"].encode()).hexdigest() != payload["payload_sha256"]:
        raise ValueError("QASM payload hash mismatch")

    backend = FakeKingston()
    circuit = qasm3.loads(payload["payload"])
    routed = transpile(circuit, backend=backend, optimization_level=2, seed_transpiler=17)
    calibration = active_instruction_calibration(backend, routed)

    return {
        "schema": "uqpu-active-target-calibration-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "CALIBRATION_SNAPSHOT_SIMULATION_INPUT",
        "backend": "FakeKingston",
        "backend_name": str(getattr(backend, "name", "unknown")),
        "contract_id": fixture["contract_id"],
        "instance_sha256": fixture["instance_sha256"],
        "qasm_sha256": payload["payload_sha256"],
        "routed_depth": routed.depth(),
        "calibration": calibration,
        "live_calibration": False,
        "paid_job_submitted": False,
        "limitations": [
            "Properties come from a saved fake-backend system snapshot, not a live backend query.",
            "Only operations actually present in this routed 3-qubit fixture are summarized.",
            "Instruction error fields are calibration/model inputs; multiplying them is not a valid complete circuit-fidelity model.",
            "This artifact does not establish real-QPU performance or economic advantage.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[3] / "benchmarks/results/batch012-qaoa-verification.json",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({
        "active_physical_qubits": result["calibration"]["active_physical_qubits"],
        "operation_counts": result["calibration"]["operation_counts"],
        "used_error_summary": result["calibration"]["used_error_summary"],
    }, sort_keys=True))

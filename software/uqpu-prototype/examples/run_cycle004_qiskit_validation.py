"""Parse Cycle 003 ER6 QASM with the pinned independent Qiskit SDK."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path

from uqpu.sdk_verification import terminal_measurement_map


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"


def run(path: Path) -> dict:
    from qiskit import qasm3

    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for item in payload["lane_a_b_c_qos"]["paired_circuits"]:
        text = item["openqasm_3"]
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if digest != item["openqasm_3_sha256"]:
            raise AssertionError("QASM input hash mismatch")
        circuit = qasm3.loads(text)
        counts = {name: int(count) for name, count in circuit.count_ops().items()}
        expected = item["logical_gate_counts"]
        for name, count in expected.items():
            if counts.get(name, 0) != count:
                raise AssertionError(f"operation count mismatch for {name}")
        if circuit.num_qubits != 6 or circuit.num_clbits != 6:
            raise AssertionError("register width drift")
        measurement_map = terminal_measurement_map(circuit)
        if measurement_map != {index: index for index in range(6)}:
            raise AssertionError("terminal measurement map drift")
        rows.append({
            "candidate_id": item["candidate_id"],
            "qasm_sha256": digest,
            "num_qubits": circuit.num_qubits,
            "num_clbits": circuit.num_clbits,
            "operation_counts": counts,
            "logical_depth_qiskit": circuit.depth(),
            "measurement_map": measurement_map,
            "parse_passed": True,
        })
    return {
        "schema": "uqpu-cycle004-qiskit-qasm-parse-v1",
        "input_path": str(path.relative_to(ROOT)),
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "qiskit_version": importlib.metadata.version("qiskit"),
        "rows": rows,
        "all_passed": len(rows) == 2 and all(row["parse_passed"] for row in rows),
        "provider_transpilation": None,
        "hardware_executed": False,
        "evidence_class": "PINNED_INDEPENDENT_SDK_PARSE_NOT_PROVIDER_VALIDATION",
        "limitations": [
            "Qiskit parsing is not evidence that any provider accepts or executes the circuit.",
            "Depth is SDK logical depth, not physical target depth.",
            "No topology, calibration, noise, duration, energy or cost is measured.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"all_passed": result["all_passed"], "qiskit_version": result["qiskit_version"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

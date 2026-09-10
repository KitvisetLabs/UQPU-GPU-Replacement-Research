"""Target-aware noisy simulation from an IBM fake-backend system snapshot.

This job uses qiskit_ibm_runtime.fake_provider and Qiskit Aer. It does not
initialize an IBM account, discover live backends, submit a QPU job, or incur
provider charges. Fake backends contain saved system snapshots and therefore
must not be described as current live calibration.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import platform
from time import perf_counter

from uqpu.optimization_baseline import QuboInstance


def qubo_from_portable(payload: dict) -> QuboInstance:
    return QuboInstance(
        linear={int(i): float(w) for i, w in payload["linear"].items()},
        quadratic={(int(i), int(j)): float(w) for i, j, w in payload["quadratic"]},
        constant=float(payload.get("constant", 0.0)),
    )


def select_fixture(data: dict, fixture_name: str) -> dict:
    for row in data.get("fixtures", []):
        if row.get("name") == fixture_name:
            return row
    available = sorted(str(row.get("name")) for row in data.get("fixtures", []))
    raise ValueError(f"unknown fixture {fixture_name!r}; available={available}")


def instruction_summary(backend, name: str):
    if name not in backend.target.operation_names:
        return None
    errors, durations = [], []
    for _, prop in backend.target[name].items():
        if prop is None:
            continue
        if getattr(prop, "error", None) is not None:
            errors.append(float(prop.error))
        if getattr(prop, "duration", None) is not None:
            durations.append(float(prop.duration))

    def stats(values):
        if not values:
            return None
        values = sorted(values)
        return {
            "count": len(values),
            "min": values[0],
            "median": values[len(values) // 2],
            "max": values[-1],
        }

    return {"error": stats(errors), "duration_seconds": stats(durations)}


def run(
    input_path: Path,
    *,
    fixture_name: str = "triangle",
    shots: int = 4096,
    seed: int = 1601,
):
    from qiskit import qasm3, transpile
    from qiskit_aer import AerSimulator
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    data = json.loads(input_path.read_text())
    fixture = select_fixture(data, fixture_name)
    payload = next(row for row in fixture["providers"] if row["provider_id"] == "ibm_quantum")
    if hashlib.sha256(payload["payload"].encode()).hexdigest() != payload["payload_sha256"]:
        raise ValueError("QASM payload hash mismatch")

    circuit = qasm3.loads(payload["payload"])
    qubo = qubo_from_portable(fixture["input"])
    exact_optimum = float(fixture["reference"]["objective"])

    backend = FakeKingston()
    simulator = AerSimulator.from_backend(backend)
    start = perf_counter()
    routed = transpile(circuit, backend=backend, optimization_level=2, seed_transpiler=17)
    transpile_seconds = perf_counter() - start

    start = perf_counter()
    result = simulator.run(routed, shots=shots, seed_simulator=seed).result()
    simulation_seconds = perf_counter() - start
    counts = result.get_counts(0)

    optimum_hits = 0
    energy_histogram = Counter()
    for bitstring, count in counts.items():
        clean = bitstring.replace(" ", "")
        index = int(clean, 2)
        assignment = {i: (index >> i) & 1 for i in qubo.variables}
        energy = qubo.energy(assignment)
        energy_histogram[str(energy)] += int(count)
        if math.isclose(energy, exact_optimum, rel_tol=0.0, abs_tol=1e-10):
            optimum_hits += int(count)

    coupling = getattr(backend, "coupling_map", None)
    edges = coupling.get_edges() if coupling is not None else []
    package_names = ("qiskit", "qiskit-aer", "qiskit-ibm-runtime")
    packages = {name: importlib.metadata.version(name) for name in package_names}

    return {
        "schema": "uqpu-target-snapshot-noise-v2",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "CALIBRATION_SNAPSHOT_SIMULATION",
        "backend": {
            "fake_backend_class": type(backend).__name__,
            "backend_name": str(getattr(backend, "name", "unknown")),
            "num_qubits": int(backend.num_qubits),
            "coupling_edges": len(edges),
            "operation_names": sorted(backend.target.operation_names),
            "instruction_summaries": {
                name: instruction_summary(backend, name)
                for name in ("measure", "x", "sx", "rz", "cz", "ecr")
                if name in backend.target.operation_names
            },
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "packages": packages,
        },
        "fixture": {
            "name": fixture["name"],
            "contract_id": fixture["contract_id"],
            "instance_sha256": fixture["instance_sha256"],
            "qasm_sha256": payload["payload_sha256"],
            "logical_qubits": circuit.num_qubits,
            "logical_depth": circuit.depth(),
            "logical_ops": dict(circuit.count_ops()),
            "routed_width": routed.num_qubits,
            "routed_depth": routed.depth(),
            "routed_ops": dict(routed.count_ops()),
            "layout": str(routed.layout),
        },
        "shots": shots,
        "seed_simulator": seed,
        "exact_optimum": exact_optimum,
        "ideal_optimum_probability": fixture["single_shot_optimum_probability_ideal"],
        "snapshot_noisy_optimum_hits": optimum_hits,
        "snapshot_noisy_optimum_probability": optimum_hits / shots,
        "counts": counts,
        "energy_histogram": dict(sorted(energy_histogram.items())),
        "transpile_seconds": transpile_seconds,
        "simulation_seconds": simulation_seconds,
        "paid_job_submitted": False,
        "real_qpu_executed": False,
        "quantum_advantage_demonstrated": False,
        "limitations": [
            "FakeKingston is a saved system snapshot, not a current live backend calibration.",
            "AerSimulator.from_backend constructs an approximate device noise model; it is not exact hardware behavior.",
            f"This bounded job executes only the {fixture['name']} correctness fixture.",
            "No queueing, calibration drift after the snapshot, provider billing, mitigation, QEC, energy, or network cost is measured.",
            "This result cannot establish quantum advantage or the 100M-unit moonshot.",
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
    parser.add_argument("--fixture", default="triangle")
    parser.add_argument("--shots", type=int, default=4096)
    args = parser.parse_args()
    if not 1 <= args.shots <= 100_000:
        raise SystemExit("shots must be in 1..100000")
    result = run(args.input, fixture_name=args.fixture, shots=args.shots)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({
        "backend": result["backend"]["fake_backend_class"],
        "fixture": result["fixture"]["name"],
        "ideal_optimum_probability": result["ideal_optimum_probability"],
        "snapshot_noisy_optimum_probability": result["snapshot_noisy_optimum_probability"],
        "routed_depth": result["fixture"]["routed_depth"],
        "shots": result["shots"],
    }, sort_keys=True))

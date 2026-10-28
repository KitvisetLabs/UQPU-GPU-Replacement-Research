"""Run the pinned Qiskit signed-Max-Cut operator cross-check (no QPU access)."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform

from uqpu.sdk_signed_maxcut import (
    DEFAULT_TOLERANCE,
    PINNED_QISKIT_VERSION,
    qiskit_signed_maxcut_scores,
    tiny_signed_maxcut_fixtures,
)
from uqpu.signed_maxcut_objective import compile_signed_maxcut


def run() -> dict:
    qiskit_version = importlib.metadata.version("qiskit")
    if qiskit_version != PINNED_QISKIT_VERSION:
        raise RuntimeError(
            f"expected pinned Qiskit {PINNED_QISKIT_VERSION}, found {qiskit_version}"
        )

    fixtures = []
    maximum_absolute_error = 0.0
    for name, vertex_count, edges in tiny_signed_maxcut_fixtures():
        lowering = compile_signed_maxcut(vertex_count, edges)
        sdk_scores = qiskit_signed_maxcut_scores(lowering)
        rows = []
        for basis_index, sdk_score in enumerate(sdk_scores):
            bits = tuple((basis_index >> qubit) & 1 for qubit in range(vertex_count))
            direct = lowering.direct_score(bits)
            qubo = lowering.qubo_score(bits)
            ising = lowering.ising_score(bits)
            error = max(abs(direct - qubo), abs(direct - ising), abs(direct - sdk_score))
            maximum_absolute_error = max(maximum_absolute_error, error)
            rows.append({
                "basis_index_lsb_qubit0": basis_index,
                "bits_q0_to_qn": "".join(str(bit) for bit in bits),
                "direct_score": direct,
                "qubo_score": qubo,
                "ising_score": ising,
                "qiskit_operator_diagonal": sdk_score,
                "max_abs_error": error,
            })

        best = max(row["direct_score"] for row in rows)
        direct_argmax = sorted(
            row["bits_q0_to_qn"] for row in rows
            if abs(row["direct_score"] - best) <= DEFAULT_TOLERANCE
        )
        sdk_best = max(row["qiskit_operator_diagonal"] for row in rows)
        sdk_argmax = sorted(
            row["bits_q0_to_qn"] for row in rows
            if abs(row["qiskit_operator_diagonal"] - sdk_best) <= DEFAULT_TOLERANCE
        )
        negative_min = min(-row["qiskit_operator_diagonal"] for row in rows)
        minimize_negative = sorted(
            row["bits_q0_to_qn"] for row in rows
            if abs(-row["qiskit_operator_diagonal"] - negative_min) <= DEFAULT_TOLERANCE
        )
        if direct_argmax != sdk_argmax or direct_argmax != minimize_negative:
            raise AssertionError(f"complete argmax/sign mismatch in fixture {name}")
        fixtures.append({
            "name": name,
            "vertex_count": vertex_count,
            "edge_count": len(edges),
            "enumerated_assignments": len(rows),
            "maximum_score": best,
            "complete_argmax": direct_argmax,
            "qiskit_argmax": sdk_argmax,
            "minimize_negative_score_argmin": minimize_negative,
            "max_abs_score_error": max(row["max_abs_error"] for row in rows),
            "assignments": rows,
        })

    root = Path(__file__).resolve().parents[1]
    source_paths = (
        "uqpu/signed_maxcut_objective.py",
        "uqpu/sdk_signed_maxcut.py",
        "examples/run_signed_maxcut_qiskit_crosscheck.py",
    )
    return {
        "schema": "uqpu-signed-maxcut-qiskit-crosscheck-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "qiskit": qiskit_version,
            "pinned_qiskit_expected": PINNED_QISKIT_VERSION,
        },
        "source_sha256": {
            path: hashlib.sha256((root / path).read_bytes()).hexdigest()
            for path in source_paths
        },
        "fixture_count": len(fixtures),
        "assignment_count": sum(item["enumerated_assignments"] for item in fixtures),
        "maximum_absolute_score_error": maximum_absolute_error,
        "tolerance": DEFAULT_TOLERANCE,
        "fixtures": fixtures,
        "paid_job_submitted": False,
        "qpu_executed": False,
        "evidence_level": "PINNED_SDK_ALGEBRAIC_CROSSCHECK",
        "limitations": [
            "This is finite tiny-instance semantic equivalence, not QAOA solution quality.",
            "The matrix diagonal and classical oracle share the declared objective contract; this is not independent physics validation.",
            "No provider target, calibration, real-QPU execution, task latency, wall-plug energy or cost was measured.",
            "A passing check does not establish quantum advantage or the 100,000,000-unit moonshots.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "
")
    print(json.dumps({
        "fixture_count": result["fixture_count"],
        "assignment_count": result["assignment_count"],
        "maximum_absolute_score_error": result["maximum_absolute_score_error"],
        "qiskit": result["environment"]["qiskit"],
        "paid_job_submitted": result["paid_job_submitted"],
    }, sort_keys=True))

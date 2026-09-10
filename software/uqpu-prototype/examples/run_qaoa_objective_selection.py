"""Batch 019: compare mean-energy vs CVaR parameter selection on ER6.

This is ideal bounded CPU simulation only. Every strategy sees the same 24x24
p=1 QAOA parameter grid, so the shared circuit-evaluation budget is 576.
"""
from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
import json
import platform

from uqpu.benchmark_contract import OptimizationBenchmarkContract
from uqpu.qaoa_objective_selection import compare_p1_grid_objectives
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut


def main() -> int:
    instance = seeded_erdos_renyi_maxcut(6, 0.5, 42)
    contract = OptimizationBenchmarkContract("er6", "batch012-verification-fixture", 42, 6)
    sweep = compare_p1_grid_objectives(
        instance,
        alphas=(0.25, 0.5, 0.75),
        gamma_steps=24,
        beta_steps=24,
        contract_id=contract.contract_id,
    )
    mean = sweep.selections[0]
    rows = [asdict(x) for x in sweep.selections]
    for row in rows:
        row["optimum_probability_ratio_vs_mean"] = (
            row["optimum_probability"] / mean.optimum_probability
            if mean.optimum_probability > 0 else None
        )
    payload = {
        "schema": "uqpu-qaoa-objective-selection-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "SIMULATION",
        "fixture": "er6",
        "contract_id": contract.contract_id,
        "qubits": 6,
        "exact_optimum": sweep.exact_optimum,
        "shared_grid_evaluations": sweep.evaluations,
        "gamma_steps": sweep.gamma_steps,
        "beta_steps": sweep.beta_steps,
        "selection_strategies": rows,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
        "paid_job_submitted": False,
        "real_qpu_executed": False,
        "quantum_advantage_demonstrated": False,
        "limitations": [
            "Ideal exact statevector simulation only; no target noise or real QPU execution.",
            "The 24x24 p=1 grid is a bounded heuristic search, not a global variational optimum proof.",
            "CVaR uses exact simulated probabilities; real hardware would estimate it from finite shots.",
            "Optimum probability is reported diagnostically and is not used to select CVaR parameters.",
            "No GPU/NPU/CPU competitive baseline or end-to-end cost advantage is inferred.",
        ],
    }
    print(json.dumps(payload, sort_keys=True, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

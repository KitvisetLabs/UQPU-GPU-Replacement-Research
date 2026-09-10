"""Batch 017: convert snapshot-simulated accepted-output probability into shot budgets.

This computes quality-adjusted *shot requirements*, not provider-dollar cost.
Actual financial cost requires current provider pricing and real execution evidence.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.accepted_solution_economics import (
    expected_independent_shots_to_success,
    shots_for_success_confidence,
)


def run(input_path: Path) -> dict:
    data = json.loads(input_path.read_text())
    p = float(data["snapshot_noisy_optimum_probability"])
    ideal = float(data["ideal_optimum_probability"])
    return {
        "schema": "uqpu-quality-adjusted-shot-budget-v1",
        "source_schema": data["schema"],
        "evidence_level": data["evidence_level"],
        "fixture": data["fixture"]["name"],
        "contract_id": data["fixture"]["contract_id"],
        "snapshot_noisy_success_probability_per_shot": p,
        "ideal_success_probability_per_shot": ideal,
        "probability_retention_fraction": p / ideal if ideal > 0 else None,
        "expected_independent_shots_to_one_accepted_solution": expected_independent_shots_to_success(p),
        "shots_for_at_least_one_success": {
            "0.95": shots_for_success_confidence(p, 0.95),
            "0.99": shots_for_success_confidence(p, 0.99),
            "0.999": shots_for_success_confidence(p, 0.999),
            "0.9999": shots_for_success_confidence(p, 0.9999),
        },
        "provider_dollar_cost_calculated": False,
        "real_qpu_executed": False,
        "limitations": [
            "Independent-shot Bernoulli model; correlated hardware drift is not modeled.",
            "The input probability comes from a saved-backend snapshot simulation, not live QPU data.",
            "No provider price, queue time, session minimum, mitigation, QEC or host cost is included.",
            "A high success probability on a 3-qubit correctness fixture is not evidence of useful quantum advantage.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps(result, sort_keys=True))

"""Batch 023: connect saved target instruction durations to inverse ML bounds.

Input is the JSON emitted by ``run_active_target_calibration.py``.  No live
provider access is performed here.  The output is a diagnostic of what mean
energy above ground would make the Margolus-Levitin lower bound equal each
recorded unitary instruction duration.  It does not estimate actual gate energy.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

from uqpu.control_limit_gap import summarize_ml_duration_requirements


def run(calibration_path: Path) -> dict:
    data = json.loads(calibration_path.read_text())
    if "calibration" not in data:
        raise ValueError("input must be an active-target-calibration artifact")
    diagnostic = summarize_ml_duration_requirements(data["calibration"])
    return {
        "schema": "uqpu-batch023-control-limit-gap-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "CALIBRATION_SNAPSHOT_DERIVED_BOUND",
        "source_calibration_schema": data.get("schema"),
        "backend": data.get("backend"),
        "backend_name": data.get("backend_name"),
        "fixture": data.get("fixture"),
        "contract_id": data.get("contract_id"),
        "live_calibration": bool(data.get("live_calibration", False)),
        "paid_job_submitted": False,
        "real_qpu_executed": False,
        "diagnostic": diagnostic,
        "claims": {
            "actual_gate_energy_measured": False,
            "actual_quantum_speed_limit_gap_measured": False,
            "engineering_speedup_demonstrated": False,
            "quantum_advantage_demonstrated": False,
        },
        "limitations": [
            "Fake-backend instruction durations are saved calibration-snapshot properties, not a live timing measurement.",
            "The inverse Margolus-Levitin energy is a mathematical requirement for equality of the ideal bound, not an estimate of pulse or device energy.",
            "Not every gate is an orthogonal-state transition, so the ML expression is not automatically a gate-time performance limit.",
            "Virtual zero-duration instructions and measurement are excluded from the unitary-duration diagnostic.",
            "Summed instruction durations are not wall-clock circuit latency because gates may execute in parallel.",
            "A true gap requires energy provenance for the same physical evolution plus control, cryogenic and wall-plug resource accounting.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--calibration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.calibration)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    summary = result["diagnostic"]["summary_by_operation"]
    print(json.dumps({
        "backend": result["backend"],
        "fixture": result["fixture"],
        "included_instruction_count": result["diagnostic"]["included_instruction_count"],
        "summary_by_operation": summary,
        "actual_quantum_speed_limit_gap_measured": False,
    }, sort_keys=True))

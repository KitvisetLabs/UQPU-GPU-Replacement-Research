"""Fail-closed matched comparison contract for FND-003 speed-limit studies.

This module checks provenance and comparability metadata. It does not derive a
quantum-speed-limit theorem, execute a measurement, or establish physical truth.
Elapsed-time ratios are descriptive only and are exposed only for accepted,
matched outputs with declared laboratory/published measurements.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any

SCHEMA = "uqpu-fnd003-matched-comparison-v1"
WORK_ID = "FND-003-MATCHED-COMPARISON"
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_MEASURED_CLASSES = frozenset({"LAB_MEASURED", "PUBLISHED_EXPERIMENT"})
_MEASUREMENT_CLASSES = frozenset({
    "SYNTHETIC_TEST_FIXTURE",
    "SIMULATION_ONLY",
    "DRY_RUN_ONLY",
    "CALIBRATION_SNAPSHOT",
    "LAB_MEASURED",
    "PUBLISHED_EXPERIMENT",
})


def canonical_sha256(value: Any) -> str:
    """Hash a canonical JSON value; this is metadata binding, not authentication."""
    try:
        payload = json.dumps(
            value, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("value must be canonical-JSON serializable") from exc
    return hashlib.sha256(payload).hexdigest()


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a nonempty string")
    return value.strip()


def _sha(value: Any, field: str) -> str:
    if not isinstance(value, str) or not _HASH_RE.fullmatch(value):
        raise ValueError(f"{field} must be a lowercase SHA-256 digest")
    return value


def _number(value: Any, field: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a finite number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{field} must be a finite number")
    if positive and number <= 0.0:
        raise ValueError(f"{field} must be greater than zero")
    return number


def _task_contract(task: Any) -> dict[str, Any]:
    if not isinstance(task, dict):
        raise ValueError("task_contract must be a mapping")
    direction = task.get("quality_direction")
    if direction not in {"MINIMUM", "MAXIMUM"}:
        raise ValueError("quality_direction must be MINIMUM or MAXIMUM")
    return {
        "workload_id": _text(task.get("workload_id"), "workload_id"),
        "input_sha256": _sha(task.get("input_sha256"), "input_sha256"),
        "output_contract_sha256": _sha(
            task.get("output_contract_sha256"), "output_contract_sha256"
        ),
        "acceptance_metric": _text(task.get("acceptance_metric"), "acceptance_metric"),
        "quality_direction": direction,
        "quality_threshold": _number(task.get("quality_threshold"), "quality_threshold"),
        "time_boundary_id": _text(task.get("time_boundary_id"), "time_boundary_id"),
        "held_out_case_id": _text(task.get("held_out_case_id"), "held_out_case_id"),
    }


def _energy_measurement(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("wall_plug_energy must be a mapping or null")
    return {
        "joules": _number(value.get("joules"), "wall_plug_energy.joules", positive=True),
        "uncertainty_j": _number(
            value.get("uncertainty_j"), "wall_plug_energy.uncertainty_j"
        ),
        "boundary_id": _text(value.get("boundary_id"), "wall_plug_energy.boundary_id"),
        "meter_source": _text(value.get("meter_source"), "wall_plug_energy.meter_source"),
    } | _validate_energy_uncertainty(value)


def _validate_energy_uncertainty(value: dict[str, Any]) -> dict[str, Any]:
    if _number(value.get("uncertainty_j"), "wall_plug_energy.uncertainty_j") < 0:
        raise ValueError("wall_plug_energy.uncertainty_j cannot be negative")
    return {}


def _run(
    value: Any,
    *,
    method: str,
    task_sha256: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{method.lower()}_run must be a mapping")
    run_id = _text(value.get("run_id"), f"{method.lower()}_run.run_id")
    if value.get("task_contract_sha256") != task_sha256:
        raise ValueError(f"{method.lower()} run is not bound to the shared task contract")
    elapsed = _number(
        value.get("elapsed_seconds"),
        f"{method.lower()}_run.elapsed_seconds",
        positive=True,
    )
    uncertainty = _number(
        value.get("elapsed_uncertainty_seconds"),
        f"{method.lower()}_run.elapsed_uncertainty_seconds",
    )
    if uncertainty < 0.0:
        raise ValueError("elapsed_uncertainty_seconds cannot be negative")
    quality = _number(value.get("quality_value"), f"{method.lower()}_run.quality_value")
    measurement_class = value.get("measurement_class")
    if measurement_class not in _MEASUREMENT_CLASSES:
        raise ValueError("unknown measurement_class")
    artifact_hash = value.get("measurement_artifact_sha256")
    if measurement_class in _MEASURED_CLASSES:
        artifact_hash = _sha(
            artifact_hash, f"{method.lower()}_run.measurement_artifact_sha256"
        )
    elif artifact_hash is not None:
        artifact_hash = _sha(
            artifact_hash, f"{method.lower()}_run.measurement_artifact_sha256"
        )

    energy = _energy_measurement(value.get("wall_plug_energy"))
    normalized = {
        "run_id": run_id,
        "method": method,
        "task_contract_sha256": task_sha256,
        "elapsed_seconds": elapsed,
        "elapsed_uncertainty_seconds": uncertainty,
        "quality_value": quality,
        "measurement_class": measurement_class,
        "measurement_artifact_sha256": artifact_hash,
        "wall_plug_energy": energy,
    }
    if method == "QUANTUM":
        normalized["evolution_contract_sha256"] = _sha(
            value.get("evolution_contract_sha256"),
            "quantum_run.evolution_contract_sha256",
        )
    threshold = None
    # The caller inserts this private field only for quality classification.
    if "_quality_threshold" in value:
        threshold = _number(value["_quality_threshold"], "_quality_threshold")
    if threshold is None:
        normalized["quality_accepted"] = None
    else:
        normalized["quality_accepted"] = (
            quality >= threshold
            if value.get("_quality_direction", "MINIMUM") == "MINIMUM"
            else quality <= threshold
        )
    return normalized


def _evolution_contract(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("evolution_contract must be a mapping")
    return {
        "initial_state_sha256": _sha(
            value.get("initial_state_sha256"), "initial_state_sha256"
        ),
        "final_state_sha256": _sha(value.get("final_state_sha256"), "final_state_sha256"),
        "hamiltonian_sha256": _sha(value.get("hamiltonian_sha256"), "hamiltonian_sha256"),
        "dynamics_model_sha256": _sha(
            value.get("dynamics_model_sha256"), "dynamics_model_sha256"
        ),
        "state_distance_definition": _text(
            value.get("state_distance_definition"), "state_distance_definition"
        ),
        "coarse_graining_definition": _text(
            value.get("coarse_graining_definition"), "coarse_graining_definition"
        ),
        "entropy_production_definition": _text(
            value.get("entropy_production_definition"), "entropy_production_definition"
        ),
    }


def build_fnd003_matched_comparison_contract(
    task_contract: dict[str, Any],
    control_run: dict[str, Any],
    quantum_run: dict[str, Any],
    speed_limit: dict[str, Any],
) -> dict[str, Any]:
    """Bind a shared useful-output task to control, quantum and theorem records.

    The caller supplies a theorem-derived bound only after its applicability
    assumptions have been audited. The function never derives that bound.
    """
    task = _task_contract(task_contract)
    task_sha = canonical_sha256(task)
    direction = task["quality_direction"]
    threshold = task["quality_threshold"]

    control_input = dict(control_run)
    quantum_input = dict(quantum_run)
    control_input["_quality_threshold"] = threshold
    control_input["_quality_direction"] = direction
    quantum_input["_quality_threshold"] = threshold
    quantum_input["_quality_direction"] = direction
    control = _run(control_input, method="CONTROL", task_sha256=task_sha)
    quantum = _run(quantum_input, method="QUANTUM", task_sha256=task_sha)
    if control["run_id"] == quantum["run_id"]:
        raise ValueError("control and quantum run_id values must differ")

    if not isinstance(speed_limit, dict):
        raise ValueError("speed_limit must be a mapping")
    theorem_id = _text(speed_limit.get("theorem_id"), "theorem_id")
    source_url = _text(speed_limit.get("source_url"), "source_url")
    if not source_url.startswith("https://"):
        raise ValueError("source_url must use HTTPS")
    source_version = _text(speed_limit.get("source_version"), "source_version")
    theorem_scope = _text(speed_limit.get("theorem_scope"), "theorem_scope")
    if speed_limit.get("task_contract_sha256") != task_sha:
        raise ValueError("speed-limit record is not bound to the shared task contract")
    if speed_limit.get("quantum_run_id") != quantum["run_id"]:
        raise ValueError("speed-limit record must name the matched quantum run")

    evolution = _evolution_contract(speed_limit.get("evolution_contract"))
    evolution_sha = canonical_sha256(evolution)
    declared_evolution_sha = _sha(
        speed_limit.get("evolution_contract_sha256"),
        "evolution_contract_sha256",
    )
    if declared_evolution_sha != evolution_sha:
        raise ValueError("evolution_contract_sha256 does not match exact evolution metadata")
    if quantum["evolution_contract_sha256"] != evolution_sha:
        raise ValueError("quantum run is not bound to the speed-limit evolution contract")

    assumptions_verified = speed_limit.get("assumptions_verified")
    if type(assumptions_verified) is not bool:
        raise ValueError("assumptions_verified must be boolean")
    bound_raw = speed_limit.get("bound_seconds")
    if assumptions_verified:
        bound_seconds = _number(bound_raw, "bound_seconds", positive=True)
        derivation_sha = _sha(
            speed_limit.get("bound_derivation_sha256"), "bound_derivation_sha256"
        )
        audit_sha = _sha(
            speed_limit.get("assumption_audit_sha256"), "assumption_audit_sha256"
        )
        bound_status = "DECLARED_APPLICABLE_WITH_AUDIT_ARTIFACTS"
    else:
        if bound_raw is not None:
            raise ValueError("unverified theorem assumptions must not carry bound_seconds")
        bound_seconds = None
        derivation_sha = speed_limit.get("bound_derivation_sha256")
        audit_sha = speed_limit.get("assumption_audit_sha256")
        if derivation_sha is not None:
            derivation_sha = _sha(derivation_sha, "bound_derivation_sha256")
        if audit_sha is not None:
            audit_sha = _sha(audit_sha, "assumption_audit_sha256")
        bound_status = "NOT_APPLICABLE_OR_UNVERIFIED"

    normalized_speed_limit = {
        "theorem_id": theorem_id,
        "source_url": source_url,
        "source_version": source_version,
        "theorem_scope": theorem_scope,
        "task_contract_sha256": task_sha,
        "quantum_run_id": quantum["run_id"],
        "evolution_contract": evolution,
        "evolution_contract_sha256": evolution_sha,
        "assumptions_verified": assumptions_verified,
        "assumption_audit_sha256": audit_sha,
        "bound_derivation_sha256": derivation_sha,
        "bound_seconds": bound_seconds,
        "bound_status": bound_status,
    }

    control_ok = control["quality_accepted"]
    quantum_ok = quantum["quality_accepted"]
    both_accepted = control_ok and quantum_ok
    both_measured = (
        control["measurement_class"] in _MEASURED_CLASSES
        and quantum["measurement_class"] in _MEASURED_CLASSES
    )
    if not both_accepted:
        result_status = "OUTPUT_QUALITY_GATE_FAILED"
    elif not both_measured:
        result_status = "ACCEPTED_OUTPUTS_BUT_LAB_MEASUREMENTS_REQUIRED"
    else:
        result_status = "MATCHED_ACCEPTED_OUTPUTS_MEASURED"

    time_ratio = (
        control["elapsed_seconds"] / quantum["elapsed_seconds"]
        if both_accepted and both_measured
        else None
    )
    quantum_bound_ratio = (
        quantum["elapsed_seconds"] / bound_seconds
        if quantum_ok
        and quantum["measurement_class"] in _MEASURED_CLASSES
        and assumptions_verified
        and bound_seconds is not None
        else None
    )

    control_energy = control["wall_plug_energy"]
    quantum_energy = quantum["wall_plug_energy"]
    if control_energy is None or quantum_energy is None:
        energy_boundary_status = "MISSING_ENERGY_MEASUREMENT"
        energy_ratio = None
    elif control_energy["boundary_id"] != quantum_energy["boundary_id"]:
        energy_boundary_status = "ENERGY_BOUNDARIES_DO_NOT_MATCH"
        energy_ratio = None
    elif not (both_accepted and both_measured):
        energy_boundary_status = "ACCEPTED_LAB_MEASUREMENTS_REQUIRED"
        energy_ratio = None
    else:
        energy_boundary_status = "MATCHED_ENERGY_BOUNDARY"
        energy_ratio = control_energy["joules"] / quantum_energy["joules"]

    payload = {
        "schema": SCHEMA,
        "work_id": WORK_ID,
        "task_contract": task,
        "task_contract_sha256": task_sha,
        "control_run": control,
        "quantum_run": quantum,
        "speed_limit": normalized_speed_limit,
        "comparison": {
            "status": result_status,
            "control_quality_accepted": control_ok,
            "quantum_quality_accepted": quantum_ok,
            "control_over_quantum_elapsed_time_ratio": time_ratio,
            "quantum_elapsed_over_applicable_bound_ratio": quantum_bound_ratio,
            "wall_plug_energy_boundary_status": energy_boundary_status,
            "control_over_quantum_wall_plug_energy_ratio": energy_ratio,
            "ratio_uncertainty_propagated": False,
            "interpretation": "DESCRIPTIVE_ONLY_NOT_AN_ADVANTAGE_CLAIM",
        },
        "evidence_class": "CONTRACT_ONLY",
        "measured_advantage_established": False,
        "physical_law_established": False,
        "nonclaims": [
            "does not derive or independently verify the cited theorem",
            "does not execute or authenticate a measurement",
            "does not infer wall-plug energy from entropy production or intrinsic energy",
            "does not treat summed instruction durations as wall-clock latency",
            "does not combine one provider's quality with another provider's price",
            "does not establish quantum advantage, memory replacement, or a new physical law",
        ],
    }
    payload["contract_sha256"] = canonical_sha256(payload)
    return payload


def validate_fnd003_matched_comparison_contract(contract: dict[str, Any]) -> list[str]:
    """Recompute the record from its inputs and reject changed derived fields."""
    if not isinstance(contract, dict):
        return ["contract_must_be_a_mapping"]
    try:
        expected = build_fnd003_matched_comparison_contract(
            contract.get("task_contract"),
            contract.get("control_run"),
            contract.get("quantum_run"),
            contract.get("speed_limit"),
        )
    except (TypeError, ValueError):
        return ["contract_inputs_invalid"]
    return [] if contract == expected else ["contract_mismatch"]

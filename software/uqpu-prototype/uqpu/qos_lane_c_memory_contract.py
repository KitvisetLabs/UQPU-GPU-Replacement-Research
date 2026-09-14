"""Executable Lane-C memory/economics contract for QOS/UQPU candidates.

This module prevents logical-machine-size or projected-block results from being
silently promoted into DRAM/HBM replacement or cost claims.  Ratios are only
computed for matched accepted functions with explicitly supplied physical
measurements/estimates and evidence labels.

Batch 050 binds the contract to the current QOS state: Batch 037 has an explicit
numerical degree-81 polynomial candidate, but phase synthesis, formal all-real
boundedness, and a full-channel repaired D.23 contract remain open.  Therefore
QOS is not currently eligible for a Lane-C replacement/economic winner claim.
"""

from __future__ import annotations

from dataclasses import dataclass


EVIDENCE_LEVELS = {
    "MEASURED",
    "SOURCE_REPORTED",
    "ENGINEERING_ESTIMATE",
    "MODEL_ONLY",
    "UNKNOWN",
}

ROLE_FIELDS = (
    "capacity_bytes",
    "sustained_bandwidth_bytes_per_s",
    "latency_seconds",
    "memory_energy_j_per_accepted_task",
    "memory_cost_per_accepted_task",
    "materialized_bytes_per_accepted_task",
)

UPSTREAM_REQUIRED_GATES = (
    "formal_polynomial_boundedness_closed",
    "qsp_phase_sequence_synthesized",
    "qsp_response_independently_reconstructed",
    "projected_block_robustness_closed",
    "full_channel_contract_closed",
    "logical_to_physical_resource_mapping_closed",
)


@dataclass(frozen=True)
class Metric:
    value: float | None
    evidence: str

    def validate(self, *, name: str, strictly_positive: bool = True) -> None:
        if self.evidence not in EVIDENCE_LEVELS:
            raise ValueError(f"unknown evidence level for {name}: {self.evidence}")
        if self.value is None:
            if self.evidence != "UNKNOWN":
                raise ValueError(f"missing {name} value must use UNKNOWN evidence")
            return
        if strictly_positive and self.value <= 0.0:
            raise ValueError(f"{name} must be positive")
        if not strictly_positive and self.value < 0.0:
            raise ValueError(f"{name} must be non-negative")


def _validate_profile(profile: dict[str, Metric], *, label: str) -> None:
    missing = sorted(set(ROLE_FIELDS) - set(profile))
    extra = sorted(set(profile) - set(ROLE_FIELDS))
    if missing or extra:
        raise ValueError(f"{label} profile fields mismatch: missing={missing}, extra={extra}")
    for field in ROLE_FIELDS:
        profile[field].validate(name=f"{label}.{field}")


def memory_role_contract(
    *,
    baseline: dict[str, Metric],
    candidate: dict[str, Metric],
    same_accepted_function: bool,
    upstream_gates: dict[str, bool],
) -> dict[str, object]:
    """Evaluate matched physical memory roles and claim readiness.

    Ratios use baseline/candidate so values >1 indicate lower candidate resource
    use for that specific role only.  No aggregate winner is formed from
    incomparable or missing roles.
    """
    _validate_profile(baseline, label="baseline")
    _validate_profile(candidate, label="candidate")

    missing_gate_keys = sorted(set(UPSTREAM_REQUIRED_GATES) - set(upstream_gates))
    extra_gate_keys = sorted(set(upstream_gates) - set(UPSTREAM_REQUIRED_GATES))
    if missing_gate_keys or extra_gate_keys:
        raise ValueError(
            f"upstream gate fields mismatch: missing={missing_gate_keys}, extra={extra_gate_keys}"
        )

    ratios: dict[str, float | None] = {}
    ratio_evidence: dict[str, str] = {}
    all_roles_quantified = True
    all_roles_non_model = True
    for field in ROLE_FIELDS:
        base = baseline[field]
        cand = candidate[field]
        if base.value is None or cand.value is None:
            ratios[field] = None
            ratio_evidence[field] = "UNAVAILABLE"
            all_roles_quantified = False
            all_roles_non_model = False
            continue
        ratios[field] = base.value / cand.value
        if "MODEL_ONLY" in (base.evidence, cand.evidence):
            ratio_evidence[field] = "MODEL_ONLY_COMPARISON"
            all_roles_non_model = False
        elif "ENGINEERING_ESTIMATE" in (base.evidence, cand.evidence):
            ratio_evidence[field] = "ESTIMATE_COMPARISON"
            all_roles_non_model = False
        elif "SOURCE_REPORTED" in (base.evidence, cand.evidence):
            ratio_evidence[field] = "SOURCE_REPORTED_COMPARISON"
        else:
            ratio_evidence[field] = "MEASURED_COMPARISON"

    upstream_closed = all(bool(upstream_gates[key]) for key in UPSTREAM_REQUIRED_GATES)
    replacement_claim_ready = (
        same_accepted_function
        and upstream_closed
        and all_roles_quantified
        and all_roles_non_model
    )

    return {
        "evidence_level": "EXECUTABLE_MATCHED_ROLE_CONTRACT",
        "same_accepted_function": same_accepted_function,
        "ratios_baseline_over_candidate": ratios,
        "ratio_evidence": ratio_evidence,
        "all_roles_quantified": all_roles_quantified,
        "all_roles_non_model_or_estimate": all_roles_non_model,
        "upstream_gates": dict(upstream_gates),
        "upstream_contract_closed": upstream_closed,
        "dram_hbm_replacement_claim_ready": replacement_claim_ready,
        "economic_winner_claim_ready": replacement_claim_ready,
        "machine_size_reduction_equals_memory_replacement": False,
        "capacity_ratio_equals_end_to_end_winner": False,
    }


def batch050_qos_lane_c_certificate() -> dict[str, object]:
    """Freeze current QOS-to-Lane-C readiness without inventing hardware data."""
    unknown_profile = {
        field: Metric(value=None, evidence="UNKNOWN") for field in ROLE_FIELDS
    }
    current_qos_gates = {
        "formal_polynomial_boundedness_closed": False,
        "qsp_phase_sequence_synthesized": False,
        "qsp_response_independently_reconstructed": False,
        "projected_block_robustness_closed": True,
        "full_channel_contract_closed": False,
        "logical_to_physical_resource_mapping_closed": False,
    }
    contract = memory_role_contract(
        baseline=unknown_profile,
        candidate=unknown_profile,
        same_accepted_function=False,
        upstream_gates=current_qos_gates,
    )
    return {
        "gate": "LANE-C-QOS-MEMORY-001",
        "classification": "QOS_LANE_C_REPLACEMENT_AND_ECONOMICS_NOT_READY",
        "qos_state_input": {
            "batch": 37,
            "degree_81_numerical_polynomial_candidate": True,
            "formal_global_boundedness_proof_closed": False,
            "qsp_phase_sequence_synthesized": False,
            "full_channel_repaired_D23_established": False,
        },
        "contract": contract,
        "next_required_measurements": list(ROLE_FIELDS),
        "next_required_upstream_gates": [
            key for key, value in current_qos_gates.items() if not value
        ],
        "non_claims": {
            "real_qpu": True,
            "quantum_advantage": True,
            "gpu_npu_ram_dram_hbm_replacement": True,
            "hundred_x": True,
            "hundred_million_x": True,
            "new_physical_law": True,
        },
    }

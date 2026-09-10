"""Executable, version-scoped audits for QOS Lemma D.19 -> Lemma D.23.

The source under audit is arXiv:2604.07639v1.  The checks in this module
separate three claims that must not be conflated:

1. a marginal error guarantee for each component channel;
2. a joint error guarantee for a composition that shares one realization;
3. the downstream block-encoding guarantee in Lemma D.23.

The shared-realization rotation certificate is an abstract channel-composition
witness.  It demonstrates that marginal average-channel control alone does not
imply a joint word/channel guarantee when the same hidden realization is reused.
It is not claimed to be a counterexample to the specific D.19 matrix stream.
"""

from __future__ import annotations

import math
from collections.abc import Iterable


MEMORY_TRANSLATION_REQUIRED_FIELDS = (
    "system_dram_capacity_bytes",
    "system_dram_sustained_bandwidth_bytes_per_s",
    "system_dram_latency_seconds",
    "dram_refresh_idle_energy_j_per_task",
    "accelerator_hbm_gddr_bytes",
    "sram_cache_bytes",
    "host_accelerator_data_movement_bytes",
    "memory_data_movement_energy_j_per_task",
    "logical_qubits",
    "estimated_physical_qubits",
    "qec_control_memory_bytes",
    "wall_seconds_per_accepted_task",
    "memory_cost_per_accepted_task",
    "total_cost_per_accepted_task",
)


def average_random_z_rotation_error(theta: float) -> float:
    """Unnormalized diamond error of the sign-averaged Z rotation vs identity.

    For S uniform on {-1,+1} and U_S = exp(i S theta Z / 2), the averaged
    channel is a dephasing channel and its unnormalized diamond distance from
    identity is 1-cos(theta).
    """
    if not math.isfinite(theta):
        raise ValueError("theta must be finite")
    return 1.0 - math.cos(theta)


def shared_realization_joint_error(*, bit_count: int, theta: float) -> float:
    """Error after reusing the same random sign for `bit_count` compositions."""
    if bit_count <= 0:
        raise ValueError("bit_count must be positive")
    if not math.isfinite(theta):
        raise ValueError("theta must be finite")
    return 1.0 - math.cos(bit_count * theta)


def conditional_revealed_slot_error(theta: float) -> float:
    """Distance of one fixed-sign rotation from identity after the sign is known."""
    if not math.isfinite(theta):
        raise ValueError("theta must be finite")
    return 2.0 * abs(math.sin(theta / 2.0))


def d19_shared_realization_certificate(
    *, bit_count: int = 8, target_epsilon: float = 1.0e-3
) -> dict[str, object]:
    """Build a small-error witness for the marginal-to-joint inference in D.19.

    We deliberately choose theta so that the *sum* of b marginal average errors
    is exactly target_epsilon.  If the b slots share one hidden sign, the joint
    average error can nevertheless exceed target_epsilon by an O(b) factor in
    the small-angle regime.  Therefore merely changing a marginal target from
    epsilon to epsilon/b does not repair a shared-realization proof; one needs a
    direct joint bound, fresh/independent realizations, or conditional full-
    channel bounds suitable for a repeated-use hybrid.
    """
    if bit_count <= 0:
        raise ValueError("bit_count must be positive")
    if not (0.0 < target_epsilon < 1.0):
        raise ValueError("target_epsilon must lie in (0, 1)")

    marginal_target = target_epsilon / bit_count
    theta = math.acos(1.0 - marginal_target)
    marginal_error = average_random_z_rotation_error(theta)
    marginal_sum = bit_count * marginal_error
    joint_error = shared_realization_joint_error(bit_count=bit_count, theta=theta)
    revealed_slot_error = conditional_revealed_slot_error(theta)
    conditional_hybrid_bound = marginal_error + (bit_count - 1) * revealed_slot_error

    return {
        "scope": "abstract shared-realization channel witness relevant to arXiv:2604.07639v1 D.148-D.150",
        "evidence_level": "THEORY_EXECUTABLE_INTERFACE_WITNESS",
        "bit_count": bit_count,
        "target_epsilon": target_epsilon,
        "theta": theta,
        "marginal_average_error_per_slot": marginal_error,
        "sum_of_marginal_average_errors": marginal_sum,
        "marginal_sum_within_target": marginal_sum <= target_epsilon * (1.0 + 1.0e-12),
        "shared_realization_joint_error": joint_error,
        "joint_over_target_ratio": joint_error / target_epsilon,
        "joint_within_target": joint_error <= target_epsilon,
        "joint_over_marginal_sum_ratio": joint_error / marginal_sum,
        "conditional_revealed_slot_error": revealed_slot_error,
        "valid_repeated_use_hybrid_upper_bound": conditional_hybrid_bound,
        "epsilon_over_b_marginal_control_alone_repairs_shared_realization": False,
        "specific_d19_matrix_stream_counterexample_claimed": False,
        "d19_theorem_refuted": False,
        "qos_globally_invalidated": False,
    }


def d23_dependency_certificate() -> dict[str, object]:
    """Return the UQPU evidence state of the D.19/D.21 -> D.23 dependency chain."""
    return {
        "scope": "arXiv:2604.07639v1 Lemma D.23 / Eqs. D211-D218",
        "evidence_level": "THEORY_DEPENDENCY_AUDIT",
        "source_dependencies": {
            "D16": "SOURCE_V1_SCOPED_COUNTEREXAMPLE_REPRODUCED_BY_UQPU",
            "D19": "MARGINAL_TO_JOINT_SHARED_REALIZATION_INTERFACE_NOT_CLOSED",
            "D20": "BOUNDARY_AND_VISIBLE_ARITHMETIC_GAPS_REPRODUCED_BY_UQPU",
            "D21": "DISPLAYED_COMPOSITION_ERROR_BUDGET_SHORTFALL_REPRODUCED_BY_UQPU",
            "D22": "IMPORTED_STANDARD_SPARSE_BLOCK_ENCODING_NOT_REAUDITED_THIS_BATCH",
        },
        "source_d23_uses_d19_and_d21": True,
        "source_d23_outer_oracle_composition_requires_full_channel_guarantees": True,
        "d23_dependency_chain_closed": False,
        "d23_theorem_refuted": False,
        "d23_sample_complexity_ready_for_uqpu_advantage_claim": False,
        "qsvt_amplification_contract_independently_closed_by_uqpu": False,
        "qos_globally_invalidated": False,
        "quantum_advantage_demonstrated_by_uqpu": False,
    }


def qos_machine_size_memory_translation_gate(
    provided_fields: Iterable[str] | None = None,
) -> dict[str, object]:
    """Gate translation from QOS machine-size units to UQPU memory replacement.

    The QOS paper compares logical qubits with classical floating-point memory
    units.  Batch 031 makes DRAM/HBM/GDDR/SRAM roles explicit.  UQPU therefore
    requires physical memory, data movement, QEC/control and cost fields before
    a machine-size reduction may be promoted to a DRAM/HBM economic-replacement
    result.
    """
    provided = set(provided_fields or ())
    required = set(MEMORY_TRANSLATION_REQUIRED_FIELDS)
    missing = sorted(required - provided)
    return {
        "source_machine_size_metric": "logical qubits versus classical floating-point numbers",
        "uqpu_memory_taxonomy": [
            "system DRAM/RAM",
            "accelerator-local HBM/GDDR/VRAM",
            "SRAM/cache",
            "persistent storage and data movement",
        ],
        "required_fields": list(MEMORY_TRANSLATION_REQUIRED_FIELDS),
        "provided_fields": sorted(provided),
        "missing_fields": missing,
        "translation_complete": not missing,
        "dram_hbm_replacement_claim_ready": not missing,
        "machine_size_reduction_equals_cost_reduction": False,
    }

"""Degree-conditioned approximate-input robustness ledger for QOS D.23.

Scope is deliberately narrow. Batch 034 closes an exact-input positive-margin
endpoint contract only. This module adds a sufficient operator-norm input
accuracy contract for applying a degree-n QSVT polynomial to an approximate
normalized projected block X=A/s.

Published robustness routes kept separate:
- Gilyen et al. Lemma 22: ||P^SV(X)-P^SV(X~)|| <= 4 n sqrt(eta).
- Chakraborty-Morolia-Peduri Theorem 8: when ||X|| <= 1/2, input
  block-encoding error eta <= delta/(2 n) is sufficient for output error <= delta.

The polynomial degree is an explicit conditioning input; no exact degree,
compiled depth, runtime, full-unitary distance, or channel/diamond distance is
inferred here.
"""

from __future__ import annotations


def approximate_input_robustness_ledger(
    *,
    sparsity: int,
    total_error: float,
    polynomial_degree: int,
    bias_fraction: float = 0.25,
    amplification_fraction: float = 0.25,
    matrix_norm: float = 1.0,
) -> dict[str, object]:
    """Return a sufficient degree-conditioned projected-block error ledger."""
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if polynomial_degree < 2:
        raise ValueError("polynomial_degree must be at least 2")
    if not (0.0 < total_error < 0.5):
        raise ValueError("total_error must lie in (0, 0.5)")
    if not (0.0 < bias_fraction < 1.0):
        raise ValueError("bias_fraction must lie in (0, 1)")
    if not (0.0 < amplification_fraction < 1.0):
        raise ValueError("amplification_fraction must lie in (0, 1)")
    if bias_fraction + amplification_fraction >= 1.0:
        raise ValueError("bias and amplification fractions must leave robustness budget")
    if not (0.0 < matrix_norm <= 1.0):
        raise ValueError("matrix_norm must lie in (0, 1]")

    robustness_fraction = 1.0 - bias_fraction - amplification_fraction
    bias_budget = bias_fraction * total_error
    amplification_budget = amplification_fraction * total_error
    robustness_budget = robustness_fraction * total_error

    target_scale = 1.0 - bias_budget / matrix_norm
    if target_scale <= 0.0:
        raise ValueError("bias budget is too large for matrix norm")

    gamma = sparsity * target_scale
    positive_margin_delta = 1.0 - gamma * (matrix_norm / sparsity)
    if positive_margin_delta <= 0.0:
        raise ValueError("positive-margin repair requires delta > 0")

    ideal_normalized_block_norm_bound = matrix_norm / sparsity
    half_norm_premise = ideal_normalized_block_norm_bound <= 0.5

    lemma22_eta_max = (robustness_budget / (4.0 * polynomial_degree)) ** 2
    theorem8_eta_max = robustness_budget / (2.0 * polynomial_degree)

    amplification_additive_contribution = (
        target_scale * matrix_norm * amplification_budget
    )
    additive_total = bias_budget + amplification_additive_contribution + robustness_budget

    return {
        "scope": "arXiv:2604.07639v1 D.23 repaired positive-margin route",
        "evidence_level": "PUBLISHED_THEOREM_DERIVED_EXECUTABLE_SUFFICIENT_CONTRACT",
        "sparsity": sparsity,
        "matrix_norm": matrix_norm,
        "polynomial_degree": polynomial_degree,
        "degree_status": "EXPLICIT_CONDITIONING_INPUT_NOT_SYNTHESIZED_OR_MEASURED",
        "total_error_budget": total_error,
        "normalization_bias_budget": bias_budget,
        "ideal_input_amplification_error_budget": amplification_budget,
        "approximate_input_robustness_budget": robustness_budget,
        "target_scale": target_scale,
        "amplification_gamma": gamma,
        "positive_margin_delta": positive_margin_delta,
        "ideal_normalized_block_norm_bound": ideal_normalized_block_norm_bound,
        "robust_qsvt_half_norm_premise": half_norm_premise,
        "gilyen_lemma22_input_eta_max": lemma22_eta_max,
        "gilyen_lemma22_bound_form": "4*n*sqrt(eta)",
        "robust_qsvt_theorem8_input_eta_max": theorem8_eta_max,
        "robust_qsvt_theorem8_bound_form": "eta <= delta_out/(2*n) for ||X||<=1/2",
        "linear_vs_sqrt_eta_allowance_ratio": theorem8_eta_max / lemma22_eta_max,
        "amplification_additive_contribution": amplification_additive_contribution,
        "additive_error_upper_bound_at_theorem8_limit": additive_total,
        "total_budget_respected": additive_total <= total_error,
        "approximate_input_projected_block_contract_closed_conditionally": half_norm_premise,
        "exact_polynomial_degree_certified": False,
        "full_unitary_error_closed": False,
        "full_channel_or_diamond_error_closed": False,
        "earlier_D16_D19_D20_D21_dependencies_closed": False,
        "physical_resource_or_economic_advantage_closed": False,
    }


def batch050_certificate() -> dict[str, object]:
    """Freeze representative degree-conditioned diagnostics, not degree claims."""
    degree_grid = (64, 256, 1024, 4096)
    examples = {
        f"degree_{degree}": approximate_input_robustness_ledger(
            sparsity=4, total_error=0.01, polynomial_degree=degree
        )
        for degree in degree_grid
    }
    return {
        "gate": "QOS-AUDIT-007",
        "classification": "D23_APPROX_INPUT_ROBUSTNESS_DEGREE_CONDITIONED_SUFFICIENT_CONTRACT",
        "canonical_case": {
            "sparsity": 4,
            "matrix_norm": 1.0,
            "total_error": 0.01,
            "bias_fraction": 0.25,
            "amplification_fraction": 0.25,
            "robustness_fraction": 0.5,
        },
        "examples": examples,
        "non_claims": {
            "exact_qsvt_degree_or_depth_measured": True,
            "full_channel_bound_closed": True,
            "real_qpu": True,
            "quantum_advantage": True,
            "gpu_npu_ram_dram_hbm_replacement": True,
            "hundred_x": True,
            "hundred_million_x": True,
            "new_physical_law": True,
        },
    }

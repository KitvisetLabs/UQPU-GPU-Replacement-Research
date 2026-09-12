"""Executable positive-margin repair tradeoff for QOS arXiv:2604.07639v1 D.23.

This module tests one explicit repair route for the endpoint ||A||=1: amplify
A/s only to (1-b)A, reserving b as normalization bias.  It uses the contract
of Gilyen et al. Theorem 30 (uniform singular-value amplification), whose
query degree is O((gamma/delta) log(gamma/epsilon)).

The calculation closes only this exact-input theorem-contract endpoint.  It
does not repair earlier D.16/D.19/D.20/D.21 dependencies or establish a
full-channel error bound for an approximate projected block encoding.
"""

from __future__ import annotations

import math


def positive_margin_repair(
    *, sparsity: int, total_error: float, bias_fraction: float = 0.5, matrix_norm: float = 1.0
) -> dict[str, object]:
    """Return a sufficient positive-margin repair ledger.

    We target (1-b)A, where b=bias_fraction*total_error.  Starting from A/s,
    the amplification factor is gamma=s(1-b).  At ||A||=1 the largest
    theorem margin is delta=b.  The remaining error budget is assigned to
    the theorem's relative amplification error.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if not (0.0 < total_error < 0.5):
        raise ValueError("total_error must lie in (0, 0.5)")
    if not (0.0 < bias_fraction < 1.0):
        raise ValueError("bias_fraction must lie in (0, 1)")
    if not (0.0 < matrix_norm <= 1.0):
        raise ValueError("matrix_norm must lie in (0, 1]")

    bias_budget = bias_fraction * total_error
    target_scale = 1.0 - bias_budget / matrix_norm
    if target_scale <= 0.0:
        raise ValueError("bias budget is too large for matrix norm")

    gamma = sparsity * target_scale
    maximum_delta = 1.0 - gamma * (matrix_norm / sparsity)
    amplification_error_budget = total_error - bias_budget
    if maximum_delta <= 0.0 or amplification_error_budget <= 0.0:
        raise ValueError("repair requires positive margin and amplification error budget")

    theorem_scaling_proxy = (gamma / maximum_delta) * math.log(
        gamma / amplification_error_budget
    )
    source_nominal_proxy = sparsity * math.log(sparsity / total_error)

    return {
        "scope": "arXiv:2604.07639v1 Lemma D.23 / Eqs. D214-D215",
        "evidence_level": "THEORY_EXECUTABLE_SUFFICIENT_REPAIR_CONTRACT",
        "sparsity": sparsity,
        "matrix_norm": matrix_norm,
        "total_error_budget": total_error,
        "bias_fraction": bias_fraction,
        "normalization_bias_budget": bias_budget,
        "target_scale": target_scale,
        "target_operator": "(target_scale)*A",
        "amplification_gamma": gamma,
        "maximum_positive_margin_delta": maximum_delta,
        "amplification_relative_error_budget": amplification_error_budget,
        "additive_error_upper_bound_exact_input": bias_budget
        + target_scale * matrix_norm * amplification_error_budget,
        "theorem30_degree_scaling": "O((gamma/delta)*log(gamma/epsilon_amp))",
        "theorem30_scaling_proxy_without_hidden_constant": theorem_scaling_proxy,
        "source_nominal_s_log_proxy": source_nominal_proxy,
        "proxy_ratio_to_source_nominal": theorem_scaling_proxy / source_nominal_proxy,
        "endpoint_positive_margin_contract_closed_for_exact_input": True,
        "approximate_input_robustness_closed": False,
        "full_channel_error_closed": False,
        "earlier_dependencies_closed": False,
    }


def batch034_certificate(*, sparsity: int = 4) -> dict[str, object]:
    examples = {
        f"epsilon_{eps:g}": positive_margin_repair(
            sparsity=sparsity, total_error=eps, bias_fraction=0.5, matrix_norm=1.0
        )
        for eps in (0.05, 0.01, 0.001, 0.0001)
    }
    return {
        "repair_route": "positive target margin via controlled under-amplification",
        "examples": examples,
        "classification": "D23_ENDPOINT_POSITIVE_MARGIN_REPAIR_EXACT_INPUT_ONLY",
        "d23_theorem_refuted": False,
        "qos_globally_invalidated": False,
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "gpu_npu_dram_hbm_replacement_demonstrated": False,
    }

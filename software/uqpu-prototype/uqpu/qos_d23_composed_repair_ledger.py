"""Executable composition ledger for QOS arXiv:2604.07639v1 Lemma D.23.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Public research links:
- https://www.facebook.com/LoveMoneyTH
- https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: primary-source theorem/interface audit, mathematical
composition, executable implementation, reproducibility design, and documentation.

Scope
-----
This module composes the Batch-034 positive-margin endpoint repair with the
Batch-035 projected-block robustness contract.  It makes the polynomial
interface in Gilyen et al. Theorem 30 explicit:

    P_amp(x) = gamma * x * P_rect(x),

where P_rect is the even rectangle polynomial from Lemma 29 with the exact
parameter substitution used in the proof of Theorem 30.

The primary source still states the rectangle/sign polynomial degree only in
big-O notation, so this module does not invent a numerical hidden constant or
promote a scaling proxy to an actual circuit depth.
"""

from __future__ import annotations

import math

from uqpu.qos_d23_approx_input_robustness import (
    max_projected_input_error_for_linear_budget,
    projected_transform_robustness,
)


def theorem30_repair_interface(
    *,
    sparsity: int,
    total_error: float,
    bias_fraction: float = 1.0 / 3.0,
    amplification_fraction: float = 1.0 / 3.0,
) -> dict[str, object]:
    """Map the Batch-034 endpoint repair into the proof parameters of Theorem 30.

    The endpoint case ||A||=1 is targeted as (1-b)A.  The remaining projected
    error budget is reserved for approximate-input robustness.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if not (0.0 < total_error < 0.5):
        raise ValueError("total_error must lie in (0, 0.5)")
    if not (0.0 < bias_fraction < 1.0):
        raise ValueError("bias_fraction must lie in (0, 1)")
    if not (0.0 < amplification_fraction < 1.0):
        raise ValueError("amplification_fraction must lie in (0, 1)")
    if bias_fraction + amplification_fraction >= 1.0:
        raise ValueError("bias and amplification fractions must leave robustness budget")

    bias_budget = bias_fraction * total_error
    amplification_error_budget = amplification_fraction * total_error
    robustness_budget = total_error - bias_budget - amplification_error_budget

    target_scale = 1.0 - bias_budget
    gamma = sparsity * target_scale
    delta = bias_budget
    if not (gamma > 1.0 and 0.0 < delta < 0.5):
        raise ValueError("Theorem-30 repair parameters are outside the imported contract")

    # Exact substitution in the proof of Gilyen et al. Theorem 30.
    rectangle_center = (1.0 - delta / 2.0) / gamma
    rectangle_half_transition = delta / (2.0 * gamma)
    rectangle_error = amplification_error_budget / gamma
    certified_linear_domain_endpoint = (1.0 - delta) / gamma

    # The endpoint identity is exact up to floating arithmetic:
    # (1-delta)/gamma = 1/sparsity.
    endpoint_identity_residual = certified_linear_domain_endpoint - 1.0 / sparsity

    return {
        "scope": "QOS arXiv:2604.07639v1 Lemma D.23 / Gilyen et al. Theorem 30",
        "evidence_level": "THEORY_EXECUTABLE_IMPORTED_INTERFACE_COMPOSITION",
        "sparsity": sparsity,
        "total_projected_error_budget": total_error,
        "normalization_bias_budget": bias_budget,
        "amplification_relative_error_budget": amplification_error_budget,
        "projected_input_robustness_budget": robustness_budget,
        "target_scale": target_scale,
        "amplification_gamma": gamma,
        "positive_margin_delta": delta,
        "theorem30_rectangle_t": rectangle_center,
        "theorem30_rectangle_delta_prime": rectangle_half_transition,
        "theorem30_rectangle_epsilon_prime": rectangle_error,
        "theorem30_polynomial_form": "P_amp(x)=gamma*x*P_rect(x)",
        "theorem30_polynomial_parity": "odd",
        "theorem30_global_bound_contract": "|P_amp(x)|<=1 for x in [-1,1]",
        "certified_linear_domain_endpoint": certified_linear_domain_endpoint,
        "ideal_A_over_s_endpoint": 1.0 / sparsity,
        "endpoint_identity_residual": endpoint_identity_residual,
        "rectangle_inner_endpoint": rectangle_center - rectangle_half_transition,
        "corollary18_real_polynomial_route": True,
        "lemma23_corollary8_bridge": (
            "Corollary 18 lifts the real P_amp to a Corollary-8 polynomial P; "
            "apply Lemma 23 to P and P* and average as in the Corollary-18 proof"
        ),
        "source_local_lemma_D8_even_only": True,
        "source_local_D8_directly_covers_linear_odd_polynomial": False,
        "numeric_degree_from_primary_source_closed": False,
        "numeric_degree_blocker": (
            "Theorem 30 -> Lemma 29 -> Lemma 25 gives degree only in big-O notation; "
            "the inspected primary source does not expose a numerical universal constant"
        ),
    }


def composed_projected_ledger(
    *,
    sparsity: int,
    total_error: float,
    actual_degree: int,
    bias_fraction: float = 1.0 / 3.0,
    amplification_fraction: float = 1.0 / 3.0,
) -> dict[str, object]:
    """Compose bias, amplification approximation, and projected-input robustness.

    `actual_degree` is caller supplied.  It is not inferred from a big-O bound.
    The Theorem-30 polynomial is odd, so the composed audit requires odd degree.
    """
    if actual_degree < 1 or actual_degree % 2 == 0:
        raise ValueError("actual_degree must be a positive odd integer")

    interface = theorem30_repair_interface(
        sparsity=sparsity,
        total_error=total_error,
        bias_fraction=bias_fraction,
        amplification_fraction=amplification_fraction,
    )
    robustness_budget = float(interface["projected_input_robustness_budget"])
    eta = max_projected_input_error_for_linear_budget(
        sparsity=sparsity,
        degree=actual_degree,
        robustness_budget=robustness_budget,
    )
    robust = projected_transform_robustness(
        sparsity=sparsity,
        degree=actual_degree,
        projected_input_error=eta,
    )
    robustness_bound = float(robust["lemma23_linear_error_bound"])
    target_scale = float(interface["target_scale"])
    bias_budget = float(interface["normalization_bias_budget"])
    amplification_error_budget = float(interface["amplification_relative_error_budget"])

    amplification_additive_bound = target_scale * amplification_error_budget
    projected_total_bound = bias_budget + amplification_additive_bound + robustness_bound

    # The channel guarantee in source D.216 is a separate requirement from the
    # projected-block operator error.  For d sequential approximate oracle calls,
    # ordinary diamond-norm subadditivity gives the sufficient per-call budget eps/d.
    channel_error_budget = total_error
    per_query_channel_error_budget = channel_error_budget / actual_degree

    return {
        "interface": interface,
        "actual_degree_parameter": actual_degree,
        "degree_is_measured_circuit_depth": False,
        "max_projected_input_error_eta": eta,
        "lemma23_linear_robustness_bound": robustness_bound,
        "normalization_bias_bound": bias_budget,
        "amplification_additive_bound": amplification_additive_bound,
        "projected_total_error_upper_bound": projected_total_bound,
        "projected_total_budget_respected": projected_total_bound <= total_error * (1.0 + 1e-12),
        "separate_channel_error_budget": channel_error_budget,
        "sufficient_per_query_diamond_error_budget": per_query_channel_error_budget,
        "diamond_subadditivity_check": actual_degree * per_query_channel_error_budget,
        "projected_block_error_is_full_channel_error": False,
        "full_unitary_error_bound_established": False,
        "full_channel_repaired_D23_established": False,
    }


def asymptotic_repair_consequence(
    *, sparsity: int, total_error: float, bias_fraction: float = 1.0 / 3.0,
    amplification_fraction: float = 1.0 / 3.0,
) -> dict[str, object]:
    """Return asymptotic and diagnostic consequences without inventing constants."""
    interface = theorem30_repair_interface(
        sparsity=sparsity,
        total_error=total_error,
        bias_fraction=bias_fraction,
        amplification_fraction=amplification_fraction,
    )
    gamma = float(interface["amplification_gamma"])
    delta = float(interface["positive_margin_delta"])
    epsilon_amp = float(interface["amplification_relative_error_budget"])

    repair_degree_proxy = (gamma / delta) * math.log(gamma / epsilon_amp)
    # Source D.215 chooses epsilon_2=epsilon/2 and states d=O(s log(1/epsilon_2)).
    source_degree_proxy = sparsity * math.log(2.0 / total_error)
    degree_proxy_ratio = repair_degree_proxy / source_degree_proxy

    return {
        "sparsity": sparsity,
        "total_error": total_error,
        "repair_degree_scaling": "O((s/epsilon)*log(s/epsilon)) for fixed positive budget fractions",
        "required_projected_input_error_scaling": (
            "O(epsilon^2/(s*log(s/epsilon))) conditional on the repaired degree scaling "
            "and Lemma-23 linear robustness"
        ),
        "per_query_channel_error_scaling": (
            "O(epsilon^2/(s*log(s/epsilon))) under d-fold diamond subadditivity"
        ),
        "source_D217_general_structure": "M = O(R^2*n^2*s^3*d^2*polylog/epsilon)",
        "repaired_conditional_sample_structure": (
            "O(R^2*n^2*s^5*polylog/epsilon^3) after substituting the sufficient repaired d; "
            "polylog and hidden constants remain unresolved"
        ),
        "repair_degree_proxy_without_hidden_constant": repair_degree_proxy,
        "source_degree_proxy_without_hidden_constant": source_degree_proxy,
        "diagnostic_degree_proxy_ratio": degree_proxy_ratio,
        "diagnostic_D217_common_factor_ratio": degree_proxy_ratio**2,
        "diagnostic_ratios_are_measured_resources": False,
        "numeric_degree_closed": False,
    }


def batch036_certificate(*, sparsity: int = 4) -> dict[str, object]:
    canonical_epsilon = 0.01
    actual_degree_examples = {
        f"degree_{degree}": composed_projected_ledger(
            sparsity=sparsity, total_error=canonical_epsilon, actual_degree=degree
        )
        for degree in (101, 1001, 10001)
    }
    scaling_examples = {
        f"epsilon_{eps:g}": asymptotic_repair_consequence(
            sparsity=sparsity, total_error=eps
        )
        for eps in (0.05, 0.01, 0.001, 0.0001)
    }
    return {
        "classification": "D23_REPAIRED_PROJECTED_LEDGER_COMPOSED_NUMERIC_DEGREE_OPEN",
        "evidence_level": "THEORY_EXECUTABLE_IMPORTED_INTERFACE_COMPOSITION",
        "source_version": "arXiv:2604.07639v1",
        "imported_primary_source": "arXiv:1806.01838v1 Lemma 23, Lemma 29, Theorem 30, Corollary 18",
        "canonical_actual_degree_examples": actual_degree_examples,
        "asymptotic_scaling_examples": scaling_examples,
        "theorem30_polynomial_interface_bridge_closed": True,
        "batch034_to_batch035_robustness_bridge_closed_conditionally_on_degree": True,
        "numeric_degree_constant_closed": False,
        "d23_theorem_proved": False,
        "d23_theorem_refuted": False,
        "qos_globally_invalidated": False,
        "full_channel_repaired_D23_established": False,
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "gpu_npu_ram_dram_hbm_replacement_demonstrated": False,
        "advantage_100x_demonstrated": False,
        "advantage_100000000x_demonstrated": False,
        "new_physical_law_claimed": False,
    }

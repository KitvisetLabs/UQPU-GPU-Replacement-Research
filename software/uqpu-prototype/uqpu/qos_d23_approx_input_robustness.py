"""Executable QOS D.23 approximate projected-block robustness interface audit.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Public research links:
- https://www.facebook.com/LoveMoneyTH
- https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: theorem/interface audit, mathematical derivation,
implementation, reproducibility design, and documentation preparation.

Scope
-----
This module imports only the robustness contracts of Gilyen et al.,
"Quantum singular value transformation and beyond", arXiv:1806.01838v1,
Lemmas 22 and 23, and applies them to the projected block A/s appearing in
QOS arXiv:2604.07639v1, Lemma D.23 / Eqs. D214-D215.

It does NOT prove QOS Lemma D.23, establish a full-unitary/full-channel error
bound, or demonstrate any real-QPU, quantum-advantage, subsystem-replacement,
or physical/economic claim.
"""

from __future__ import annotations

import math


def lemma23_margin_cap(*, sparsity: int) -> float:
    """Return a sufficient maximum projected-block input error for Lemma 23.

    Let B=A/s with ||A||<=1 and let ||B_tilde-B||<=eta.  Then

        ||(B+B_tilde)/2|| <= 1/s + eta/2.

    Gilyen et al. Lemma 23 is therefore guaranteed applicable whenever

        eta + (1/s + eta/2)^2 <= 1.

    Solving equality for the positive root gives the returned cap.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    return 2.0 * (math.sqrt(2.0 + 2.0 / sparsity) - 1.0 - 1.0 / sparsity)


def projected_transform_robustness(
    *, sparsity: int, degree: int, projected_input_error: float
) -> dict[str, object]:
    """Evaluate generic and interior-margin QSVT robustness upper bounds.

    `degree` is the actual polynomial degree supplied by the caller.  It is
    deliberately not inferred from big-O notation.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if degree < 1:
        raise ValueError("degree must be positive")
    if not (0.0 <= projected_input_error <= 1.0):
        raise ValueError("projected_input_error must lie in [0, 1]")

    eta = projected_input_error
    average_norm_upper = 1.0 / sparsity + eta / 2.0
    lemma23_condition_lhs = eta + average_norm_upper**2
    lemma23_applicable = lemma23_condition_lhs <= 1.0

    generic_lemma22_bound = 4.0 * degree * math.sqrt(eta)
    linear_lemma23_bound = None
    linear_coefficient = None
    if lemma23_applicable:
        denominator = 1.0 - average_norm_upper**2
        if denominator <= 0.0:
            lemma23_applicable = False
        else:
            linear_coefficient = math.sqrt(2.0 / denominator)
            linear_lemma23_bound = degree * linear_coefficient * eta

    return {
        "scope": "QOS arXiv:2604.07639v1 Lemma D.23 / Eqs. D214-D215",
        "evidence_level": "THEORY_EXECUTABLE_IMPORTED_ROBUSTNESS_INTERFACE_AUDIT",
        "sparsity": sparsity,
        "degree": degree,
        "projected_input_error": eta,
        "ideal_projected_block_norm_upper": 1.0 / sparsity,
        "average_projected_block_norm_upper": average_norm_upper,
        "lemma23_condition_lhs_upper": lemma23_condition_lhs,
        "lemma23_condition_satisfied": lemma23_applicable,
        "lemma23_sufficient_input_error_cap": lemma23_margin_cap(sparsity=sparsity),
        "lemma22_generic_sqrt_error_bound": generic_lemma22_bound,
        "lemma23_linear_coefficient_upper": linear_coefficient,
        "lemma23_linear_error_bound": linear_lemma23_bound,
        "full_unitary_error_bound_established": False,
        "full_channel_error_bound_established": False,
    }


def max_projected_input_error_for_linear_budget(
    *, sparsity: int, degree: int, robustness_budget: float, iterations: int = 100
) -> float:
    """Numerically invert the sufficient Lemma-23 linear robustness ledger.

    Returns the largest eta found by deterministic bisection such that both
    the sufficient interior condition and the Lemma-23 output-error bound are
    within `robustness_budget`.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if degree < 1:
        raise ValueError("degree must be positive")
    if robustness_budget <= 0.0:
        raise ValueError("robustness_budget must be positive")
    if iterations < 20:
        raise ValueError("iterations must be at least 20")

    low = 0.0
    high = lemma23_margin_cap(sparsity=sparsity)
    for _ in range(iterations):
        middle = (low + high) / 2.0
        result = projected_transform_robustness(
            sparsity=sparsity, degree=degree, projected_input_error=middle
        )
        bound = result["lemma23_linear_error_bound"]
        if result["lemma23_condition_satisfied"] and bound is not None and bound <= robustness_budget:
            low = middle
        else:
            high = middle
    return low


def batch035_certificate(*, sparsity: int = 4, total_error: float = 0.01) -> dict[str, object]:
    """Return the canonical Batch-035 conditional projected-block certificate."""
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if not (0.0 < total_error < 0.5):
        raise ValueError("total_error must lie in (0, 0.5)")

    robustness_budget = total_error / 3.0
    degrees = (10, 100, 1000, 10000)
    examples: dict[str, object] = {}
    for degree in degrees:
        eta_linear = max_projected_input_error_for_linear_budget(
            sparsity=sparsity,
            degree=degree,
            robustness_budget=robustness_budget,
        )
        eta_generic = (robustness_budget / (4.0 * degree)) ** 2
        linear_eval = projected_transform_robustness(
            sparsity=sparsity,
            degree=degree,
            projected_input_error=eta_linear,
        )
        examples[f"degree_{degree}"] = {
            "actual_degree_parameter": degree,
            "robustness_budget": robustness_budget,
            "max_projected_input_error_linear_lemma23": eta_linear,
            "max_projected_input_error_generic_lemma22": eta_generic,
            "linear_to_generic_tolerance_ratio": eta_linear / eta_generic,
            "lemma23_bound_at_linear_tolerance": linear_eval["lemma23_linear_error_bound"],
            "lemma23_condition_lhs_at_linear_tolerance": linear_eval[
                "lemma23_condition_lhs_upper"
            ],
        }

    return {
        "classification": "D23_PROJECTED_BLOCK_LINEAR_ROBUSTNESS_MARGIN_CONTRACT_IDENTIFIED",
        "evidence_level": "THEORY_EXECUTABLE_IMPORTED_ROBUSTNESS_INTERFACE_AUDIT",
        "source_version": "arXiv:2604.07639v1",
        "imported_theorem_source": "arXiv:1806.01838v1 Lemmas 22-23",
        "sparsity": sparsity,
        "total_error_for_diagnostic_split": total_error,
        "robustness_budget": robustness_budget,
        "lemma23_sufficient_input_error_cap": lemma23_margin_cap(sparsity=sparsity),
        "examples": examples,
        "source_d215_linear_O_d_eta_form_supportable_under_explicit_interior_contract": True,
        "d23_theorem_proved": False,
        "d23_theorem_refuted": False,
        "qos_globally_invalidated": False,
        "full_unitary_error_bound_established": False,
        "full_channel_error_bound_established": False,
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "gpu_npu_ram_dram_hbm_replacement_demonstrated": False,
    }

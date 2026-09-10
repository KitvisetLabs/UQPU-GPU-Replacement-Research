"""Scoped dependency and error-budget checks for QOS Lemma D.21.

This module audits the displayed composition accounting in arXiv:2604.07639v1
without claiming that Quantum Oracle Sketching (QOS) as a whole is invalid.
It also propagates the visible D.20 sqrt(R) arithmetic correction only as a
conditional constant-factor sensitivity calculation.
"""

from __future__ import annotations

import math


def _log2_width(cardinality: int) -> int:
    if cardinality <= 0:
        raise ValueError("cardinality must be positive")
    if cardinality == 1:
        return 0
    return math.ceil(math.log2(cardinality))


def d21_counter_oracle_use_count(*, dimension: int, row_sparsity: int) -> dict[str, int]:
    """Return the number of cumulative-counter-oracle uses shown in D.207-D.209."""
    if dimension <= 1:
        raise ValueError("dimension must exceed one")
    if row_sparsity <= 0 or row_sparsity > dimension:
        raise ValueError("row_sparsity must lie in [1, dimension]")
    n = _log2_width(dimension)
    m = _log2_width(row_sparsity)
    uses = n + m
    return {"n": n, "m": m, "uses": uses}


def source_d21_per_call_epsilon(*, epsilon: float, n: int) -> float:
    """Per-call epsilon_2 printed in the final D.21 composition paragraph."""
    if epsilon <= 0 or n <= 0:
        raise ValueError("epsilon and n must be positive")
    return epsilon / n


def triangle_safe_per_call_epsilon(*, epsilon: float, uses: int) -> float:
    """A simple telescoping/triangle-safe allocation for `uses` approximate calls."""
    if epsilon <= 0 or uses <= 0:
        raise ValueError("epsilon and uses must be positive")
    return epsilon / uses


def d21_error_budget_certificate(
    *, dimension: int = 2**20, row_sparsity: int = 1024, epsilon: float = 0.01
) -> dict[str, object]:
    """Audit the displayed D.21 per-call error allocation.

    D.209 states that the construction uses n+ceil(log2(s_r)) <= 2n calls to
    cV_c, then sets epsilon_2 = epsilon/n. If one uses the standard telescoping
    bound with an epsilon_2 approximation for every call, the displayed choice
    certifies at most (uses/n)*epsilon. A factor-tight repair is
    epsilon_2 = epsilon/uses. This is a proof-accounting check, not a
    counterexample to the D.21 theorem itself.
    """
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    counts = d21_counter_oracle_use_count(dimension=dimension, row_sparsity=row_sparsity)
    n = counts["n"]
    uses = counts["uses"]
    source_per_call = source_d21_per_call_epsilon(epsilon=epsilon, n=n)
    triangle_bound = uses * source_per_call
    safe_per_call = triangle_safe_per_call_epsilon(epsilon=epsilon, uses=uses)

    return {
        "scope": "arXiv:2604.07639v1 Lemma D.21 / Eqs. D207-D209 displayed composition",
        "evidence_level": "THEORY_EXECUTABLE_ERROR_BUDGET_AUDIT",
        "dimension": dimension,
        "row_sparsity": row_sparsity,
        "epsilon": epsilon,
        "n": n,
        "m": counts["m"],
        "counter_oracle_uses": uses,
        "source_displayed_epsilon2": source_per_call,
        "triangle_bound_using_source_epsilon2": triangle_bound,
        "triangle_bound_over_target_ratio": triangle_bound / epsilon,
        "displayed_allocation_alone_certifies_target": triangle_bound <= epsilon,
        "triangle_safe_epsilon2": safe_per_call,
        "required_precision_tightening_factor": source_per_call / safe_per_call,
        "worst_case_ratio_when_row_sparsity_le_dimension": 2.0,
        "asymptotic_order_changed_by_constant_factor_repair": False,
        "d21_theorem_refuted": False,
        "qos_globally_invalidated": False,
        "quantum_advantage_demonstrated": False,
        "uqpu_advantage_demonstrated": False,
    }


def source_d20_local_coefficient(repetition_number: float) -> float:
    """Linear-R coefficient appearing in the displayed D.184/D.185 route."""
    if repetition_number <= 0:
        raise ValueError("repetition_number must be positive")
    r = repetition_number
    return ((math.pi * math.pi + 4.0 * math.pi) / 2.0) * r


def corrected_visible_d20_local_coefficient(repetition_number: float) -> float:
    """Coefficient obtained by retaining the sqrt(R) term visible before D.184."""
    if repetition_number <= 0:
        raise ValueError("repetition_number must be positive")
    r = repetition_number
    return math.pi * math.pi * r / 2.0 + 2.0 * math.pi * math.sqrt(r)


def d20_visible_coefficient_inflation(repetition_number: float) -> float:
    return corrected_visible_d20_local_coefficient(repetition_number) / source_d20_local_coefficient(
        repetition_number
    )


def d20_downstream_inflation_certificate() -> dict[str, object]:
    """Bound the specific visible-arithmetic constant inflation for uniform support.

    For the audited uniform hierarchical model, nondegenerate support K>=2 gives
    R >= 1-1/K >= 1/2. The ratio can be written
      (pi^2/2 + 2*pi/sqrt(R)) / (pi^2/2 + 2*pi),
    which decreases with R. Hence the maximum on R in [1/2,1] is at R=1/2.
    This says only that this *specific* arithmetic correction need not change
    the downstream asymptotic order; unresolved D.20 proof issues remain.
    """
    samples = [0.5, 0.6, 0.75, 0.9, 1.0]
    ratios = {f"{r:.2f}": d20_visible_coefficient_inflation(r) for r in samples}
    maximum = d20_visible_coefficient_inflation(0.5)
    return {
        "scope": "Conditional propagation of the D.20 visible sqrt(R) correction into downstream sample coefficients",
        "evidence_level": "THEORY_EXECUTABLE_SENSITIVITY_ANALYSIS",
        "uniform_nondegenerate_minimum_R": 0.5,
        "sampled_inflation_ratios": ratios,
        "maximum_ratio_on_R_in_[0.5,1]": maximum,
        "maximum_percent_inflation": 100.0 * (maximum - 1.0),
        "asymptotic_order_changed_by_this_specific_correction": False,
        "complete_d20_repair_claimed": False,
        "d21_or_d23_validity_established": False,
        "qos_globally_invalidated": False,
    }

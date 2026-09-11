"""Executable QSVT endpoint/margin checks for QOS arXiv:2604.07639v1 D.23.

This module does not claim that Lemma D.23 is false.  It audits whether the
standard bounded-polynomial / uniform singular-value-amplification contract
used to amplify A/s back to A is established at the endpoint ||A|| = 1.
"""

from __future__ import annotations

import math


def uniform_sva_margin_certificate(*, matrix_norm: float, sparsity: int) -> dict[str, object]:
    """Check the positive-margin requirement for amplification A/s -> A.

    Standard uniform singular-value amplification with amplification gamma=s
    requires ||A/s|| <= (1-delta)/s for some delta>0.  Equivalently,
    ||A|| <= 1-delta.  Hence a theorem stated for all ||A||<=1 includes a
    saturation case where no positive delta is available through this route.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2 for this amplification audit")
    if matrix_norm < 0 or matrix_norm > 1:
        raise ValueError("matrix_norm must lie in [0, 1]")

    normalized_norm = matrix_norm / sparsity
    gamma = float(sparsity)
    maximum_delta = 1.0 - matrix_norm
    return {
        "scope": "arXiv:2604.07639v1 Lemma D.23 / Eqs. D214-D215",
        "evidence_level": "THEORY_EXECUTABLE_IMPORTED_THEOREM_CONTRACT_AUDIT",
        "matrix_norm": matrix_norm,
        "sparsity": sparsity,
        "normalized_block_norm": normalized_norm,
        "requested_amplification_gamma": gamma,
        "maximum_positive_margin_delta": maximum_delta,
        "positive_margin_exists": maximum_delta > 0.0,
        "endpoint_saturation_case": math.isclose(matrix_norm, 1.0, rel_tol=0.0, abs_tol=1e-15),
        "standard_uniform_sva_route_established_at_endpoint": maximum_delta > 0.0,
        "d23_theorem_refuted": False,
        "qos_globally_invalidated": False,
    }


def endpoint_bounded_polynomial_degree_lower_bound(*, sparsity: int, epsilon: float) -> dict[str, object]:
    """Lower-bound the degree of a bounded endpoint-saturating polynomial.

    Assume a real polynomial P of degree d satisfies
      |P(x)| <= 1 on [-1,1]
    and
      |P(x) - s*x| <= epsilon on [0,1/s].

    Put x0=(1-4e)/s and x1=1/s.  The mean-value theorem gives a point xi in
    (x0,x1) with P'(xi)>=s/2.  Uniform approximation also gives
    P(xi)>=1-5e.  The sharp pointwise Bernstein-Markov inequality

      |P'(x)| / sqrt(1-P(x)^2) <= d / sqrt(1-x^2)

    then yields

      d >= (s/2)*sqrt(1-1/s^2)/sqrt(10e-25e^2).

    This is an interpretation-level obstruction to an O(s log(1/e)) bounded
    polynomial family that remains valid all the way to the saturation
    endpoint as e->0.  It is not, by itself, a counterexample to D.23.
    """
    if sparsity < 2:
        raise ValueError("sparsity must be at least 2")
    if epsilon <= 0 or epsilon >= 0.2:
        raise ValueError("epsilon must lie in (0, 0.2)")

    denominator_sq = 10.0 * epsilon - 25.0 * epsilon * epsilon
    lower_bound = (
        (sparsity / 2.0)
        * math.sqrt(1.0 - 1.0 / (sparsity * sparsity))
        / math.sqrt(denominator_sq)
    )
    nominal_s_log = sparsity * math.log(1.0 / epsilon)
    return {
        "scope": "bounded-polynomial interpretation of D.23 endpoint amplification",
        "evidence_level": "THEORY_EXECUTABLE_APPROXIMATION_LOWER_BOUND",
        "sparsity": sparsity,
        "epsilon": epsilon,
        "degree_lower_bound": lower_bound,
        "nominal_s_log_1_over_epsilon": nominal_s_log,
        "lower_bound_over_nominal_s_log": lower_bound / nominal_s_log,
        "asymptotic_lower_bound_scaling": "Omega(s/sqrt(epsilon))",
        "displayed_source_degree_scaling": "O(s*log(1/epsilon))",
        "endpoint_bounded_polynomial_contract_established": False,
        "d23_theorem_refuted": False,
    }


def batch033_certificate(*, sparsity: int = 4) -> dict[str, object]:
    return {
        "endpoint_margin": uniform_sva_margin_certificate(matrix_norm=1.0, sparsity=sparsity),
        "interior_margin_example": uniform_sva_margin_certificate(matrix_norm=0.9, sparsity=sparsity),
        "degree_lower_bound_e1e4": endpoint_bounded_polynomial_degree_lower_bound(
            sparsity=sparsity, epsilon=1e-4
        ),
        "degree_lower_bound_e1e6": endpoint_bounded_polynomial_degree_lower_bound(
            sparsity=sparsity, epsilon=1e-6
        ),
        "classification": "SOURCE_V1_D23_QSVT_ENDPOINT_CONTRACT_NOT_ESTABLISHED",
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "uqpu_advantage_demonstrated": False,
    }

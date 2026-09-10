"""Scoped arithmetic and boundary checks for QOS Lemma D.20 (arXiv:2604.07639v1).

The source proof's displayed Eq. (D183) contains a square-root dependence on
the repetition number R immediately before replacing it by a linear R term.
This module makes that visible arithmetic executable and also reproduces the
R=0 / zero-sample boundary witness discussed in the independent audit.

The checks are theorem- and version-scoped. They do not claim that Quantum
Oracle Sketching as a whole is invalid.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class D20BoundaryWitness:
    """Public-parameter boundary witness for the cumulative-counter lemma."""

    dimension: int = 4
    row_sparsity: int = 1
    support_size: int = 1
    repetition_number: float = 0.0
    epsilon: float = 0.5


def printed_d185_sample_count(
    *,
    dimension: int,
    row_sparsity: int,
    repetition_number: float,
    epsilon: float,
) -> float:
    """Evaluate the sample prescription printed in Eq. (D185).

    M = ((pi^2 + 4*pi)/2) * R * N * s_r / epsilon.
    """
    if dimension <= 0 or row_sparsity <= 0:
        raise ValueError("dimension and row_sparsity must be positive")
    if repetition_number < 0:
        raise ValueError("repetition_number must be nonnegative")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return (
        (math.pi * math.pi + 4.0 * math.pi)
        / 2.0
        * repetition_number
        * dimension
        * row_sparsity
        / epsilon
    )


def printed_d184_visible_error_bound(*, support_size: int, repetition_number: float, samples: int) -> float:
    """Evaluate the final displayed D184 bound after the R-for-sqrt(R) substitution."""
    if support_size <= 0:
        raise ValueError("support_size must be positive")
    if repetition_number < 0:
        raise ValueError("repetition_number must be nonnegative")
    if samples <= 0:
        raise ValueError("samples must be positive")
    return (
        (math.pi * math.pi + 4.0 * math.pi)
        * support_size
        * repetition_number
        / (2.0 * samples)
    )


def corrected_visible_arithmetic_bound(
    *, support_size: int, repetition_number: float, samples: int
) -> float:
    """Follow D182-D184 while retaining the sqrt(R) term visible in D183.

    This is only an arithmetic correction to the displayed proof route, not a
    repaired theorem.
    """
    if support_size <= 0:
        raise ValueError("support_size must be positive")
    if repetition_number < 0:
        raise ValueError("repetition_number must be nonnegative")
    if samples <= 0:
        raise ValueError("samples must be positive")
    r = repetition_number
    return (
        math.pi * math.pi * support_size * r / (2.0 * samples)
        + 2.0 * math.pi * support_size * math.sqrt(r) / samples
    )


def source_bias_substitution_ratio(repetition_number: float) -> float:
    """Return sqrt(R)/R for R>0, quantifying the D183 substitution gap."""
    if not 0.0 < repetition_number:
        raise ValueError("repetition_number must be positive")
    return math.sqrt(repetition_number) / repetition_number


def minimally_integerized_visible_sample_count(
    *, support_size: int, repetition_number: float, epsilon: float
) -> int:
    """Positive-integer sample count for the corrected visible arithmetic only.

    ceil[K/epsilon * (pi^2 R / 2 + 2*pi*sqrt(R))], with an explicit floor of 1.
    This does not repair the history-selected-coordinate issue.
    """
    if support_size <= 0:
        raise ValueError("support_size must be positive")
    if repetition_number < 0:
        raise ValueError("repetition_number must be nonnegative")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    raw = (
        support_size
        / epsilon
        * (math.pi * math.pi * repetition_number / 2.0 + 2.0 * math.pi * math.sqrt(repetition_number))
    )
    return max(1, math.ceil(raw))


def d20_zero_sample_boundary_certificate(
    witness: D20BoundaryWitness | None = None,
) -> dict[str, object]:
    """Return the scoped R=0 boundary certificate.

    For two target unitaries on the |a1>,|a2> span, the |+> output states have
    overlap 1/2, so their unnormalized trace-norm distance is sqrt(3).
    By triangle inequality, any common zero-sample channel is at unnormalized
    diamond distance at least sqrt(3)/2 from one target.
    """
    witness = witness or D20BoundaryWitness()
    printed_samples = printed_d185_sample_count(
        dimension=witness.dimension,
        row_sparsity=witness.row_sparsity,
        repetition_number=witness.repetition_number,
        epsilon=witness.epsilon,
    )
    output_overlap = 0.5
    unnormalized_trace_distance = 2.0 * math.sqrt(1.0 - output_overlap * output_overlap)
    common_channel_lower_bound = unnormalized_trace_distance / 2.0

    return {
        "scope": "arXiv:2604.07639v1 Lemma D.20 / Eq. D185 boundary",
        "evidence_level": "THEORY_EXECUTABLE_REPRODUCTION",
        "dimension": witness.dimension,
        "row_sparsity": witness.row_sparsity,
        "support_size": witness.support_size,
        "repetition_number": witness.repetition_number,
        "epsilon": witness.epsilon,
        "printed_d185_sample_count": printed_samples,
        "printed_formula_permits_zero_samples": printed_samples == 0.0,
        "target_output_overlap": output_overlap,
        "target_output_unnormalized_trace_distance": unnormalized_trace_distance,
        "common_zero_sample_channel_diamond_lower_bound": common_channel_lower_bound,
        "stated_epsilon_cannot_hold_for_both_targets": common_channel_lower_bound > witness.epsilon,
        "qos_globally_invalidated": False,
        "quantum_advantage_demonstrated": False,
        "uqpu_advantage_demonstrated": False,
    }


def d20_arithmetic_gap_certificate(
    *, support_size: int = 2, repetition_number: float = 0.5, epsilon: float = 0.05
) -> dict[str, object]:
    """Quantify the visible D183 sqrt(R)->R arithmetic gap at a legal nondegenerate example."""
    if support_size < 2:
        raise ValueError("support_size must be at least 2 for this nondegenerate example")
    if not 0.0 < repetition_number < 1.0:
        raise ValueError("repetition_number must lie in (0, 1)")
    min_r_from_uniform_support = 1.0 - 1.0 / support_size
    if repetition_number < min_r_from_uniform_support:
        raise ValueError("repetition_number violates R >= 1 - 1/K for the audited model")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")

    source_integer_samples = math.ceil(
        (math.pi * math.pi + 4.0 * math.pi)
        * support_size
        * repetition_number
        / (2.0 * epsilon)
    )
    corrected_integer_samples = minimally_integerized_visible_sample_count(
        support_size=support_size,
        repetition_number=repetition_number,
        epsilon=epsilon,
    )

    source_bound_at_source_m = printed_d184_visible_error_bound(
        support_size=support_size,
        repetition_number=repetition_number,
        samples=source_integer_samples,
    )
    corrected_bound_at_source_m = corrected_visible_arithmetic_bound(
        support_size=support_size,
        repetition_number=repetition_number,
        samples=source_integer_samples,
    )
    corrected_bound_at_corrected_m = corrected_visible_arithmetic_bound(
        support_size=support_size,
        repetition_number=repetition_number,
        samples=corrected_integer_samples,
    )

    return {
        "scope": "arXiv:2604.07639v1 D182-D185 displayed arithmetic",
        "evidence_level": "THEORY_EXECUTABLE_ARITHMETIC_AUDIT",
        "support_size": support_size,
        "repetition_number": repetition_number,
        "uniform_support_minimum_repetition_number": min_r_from_uniform_support,
        "epsilon": epsilon,
        "sqrt_r_over_r": source_bias_substitution_ratio(repetition_number),
        "source_integer_samples_from_displayed_linear_R_bound": source_integer_samples,
        "corrected_visible_integer_samples": corrected_integer_samples,
        "source_displayed_bound_at_source_samples": source_bound_at_source_m,
        "corrected_visible_bound_at_source_samples": corrected_bound_at_source_m,
        "corrected_visible_bound_exceeds_epsilon_at_source_samples": corrected_bound_at_source_m > epsilon,
        "corrected_visible_bound_at_corrected_samples": corrected_bound_at_corrected_m,
        "corrected_visible_bound_meets_epsilon": corrected_bound_at_corrected_m <= epsilon,
        "repaired_d20_theorem_claimed": False,
        "qos_globally_invalidated": False,
        "quantum_advantage_demonstrated": False,
        "uqpu_advantage_demonstrated": False,
    }

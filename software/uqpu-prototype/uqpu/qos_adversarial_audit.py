"""Scoped adversarial checks for Quantum Oracle Sketching (QOS).

This module independently reproduces the arithmetic and channel-coherence
certificate for the repeated-pair witness against Theorem D.16 / Eq. (D99) of
arXiv:2604.07639v1. It does not claim that QOS as a whole is invalid.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math


@dataclass(frozen=True)
class D16RepeatedPairWitness:
    """Parameters of the public repeated-pair counterexample witness."""

    t: float = 2.0 * math.pi
    p_max: float = 0.5
    alphabet_size: int = 2
    repetition_number: float = 1.0
    epsilon: float = 1.0 / 20.0
    samples: int = 752


def printed_d16_sample_threshold(
    *,
    t: float,
    p_max: float,
    alphabet_size: int,
    repetition_number: float,
    epsilon: float,
) -> float:
    """Evaluate the sufficient sample threshold printed in Eq. (D99).

    M >= [(t^2 p_max + 2 t sqrt(2 p_max |X|)) / epsilon] R_D.
    """
    if t <= 0 or epsilon <= 0:
        raise ValueError("t and epsilon must be positive")
    if not 0 < p_max <= 1:
        raise ValueError("p_max must lie in (0, 1]")
    if alphabet_size <= 0 or repetition_number < 0:
        raise ValueError("alphabet_size must be positive and repetition_number nonnegative")
    return (
        (t * t * p_max + 2.0 * t * math.sqrt(2.0 * p_max * alphabet_size))
        / epsilon
        * repetition_number
    )


def smallest_even_integer_at_least(value: float) -> int:
    """Return the smallest even integer M with M >= value."""
    if not math.isfinite(value) or value < 0:
        raise ValueError("value must be finite and nonnegative")
    candidate = math.ceil(value)
    return candidate if candidate % 2 == 0 else candidate + 1


def repeated_pair_coherence(*, t: float, samples: int) -> float:
    """Average off-diagonal coherence for fair repeated pairs.

    The M samples consist of q=M/2 independent fair parent bits, each repeated
    twice. Relative to the target global phase, averaging over the q parent
    bits gives c = cos(t/q)^q.
    """
    if t <= 0:
        raise ValueError("t must be positive")
    if samples <= 0 or samples % 2:
        raise ValueError("samples must be a positive even integer")
    pairs = samples // 2
    return math.cos(t / pairs) ** pairs


def repeated_pair_diamond_error(*, t: float, samples: int) -> float:
    """Unnormalized diamond distance from the target identity channel.

    For this two-dimensional dephasing witness, the averaged channel multiplies
    off-diagonal entries by c, hence ||D_c - I||_diamond = 1 - c.
    """
    coherence = repeated_pair_coherence(t=t, samples=samples)
    return 1.0 - coherence


def rational_envelope_checks() -> dict[str, bool]:
    """Check the audit's simple rational envelopes for the explicit witness.

    The standard rational bounds 333/106 < pi < 22/7 are checked against the
    runtime value of pi and then used only as conservative arithmetic envelopes.
    """
    pi_lower = Fraction(333, 106)
    pi_upper = Fraction(22, 7)
    y0 = Fraction(24649, 470000)

    threshold_upper = Fraction(36784, 49)
    exp_second_order_upper = 1 - y0 + y0 * y0 / 2

    return {
        "pi_lower_bound_runtime_check": float(pi_lower) < math.pi,
        "pi_upper_bound_runtime_check": math.pi < float(pi_upper),
        "printed_threshold_upper_bound_below_752": threshold_upper < 752,
        "pi_squared_over_188_above_y0": pi_lower * pi_lower / 188 > y0,
        "exp_second_order_upper_below_19_over_20": exp_second_order_upper < Fraction(19, 20),
    }


def d16_repeated_pair_certificate(
    witness: D16RepeatedPairWitness | None = None,
) -> dict[str, object]:
    """Return a machine-readable scoped counterexample certificate."""
    witness = witness or D16RepeatedPairWitness()
    threshold = printed_d16_sample_threshold(
        t=witness.t,
        p_max=witness.p_max,
        alphabet_size=witness.alphabet_size,
        repetition_number=witness.repetition_number,
        epsilon=witness.epsilon,
    )
    coherence = repeated_pair_coherence(t=witness.t, samples=witness.samples)
    error = 1.0 - coherence

    return {
        "scope": "arXiv:2604.07639v1 Theorem D.16 / Eq. D99 repeated-pair witness",
        "evidence_level": "THEORY_EXECUTABLE_REPRODUCTION",
        "source_claim_scope": "correlated-data sufficient threshold only",
        "t": witness.t,
        "p_max": witness.p_max,
        "alphabet_size": witness.alphabet_size,
        "repetition_number": witness.repetition_number,
        "epsilon": witness.epsilon,
        "samples": witness.samples,
        "pairs": witness.samples // 2,
        "printed_threshold": threshold,
        "smallest_even_integer_meeting_threshold": smallest_even_integer_at_least(threshold),
        "threshold_condition_satisfied": witness.samples >= threshold,
        "coherence": coherence,
        "unnormalized_diamond_error": error,
        "stated_error_target_violated": error > witness.epsilon,
        "rational_envelope_checks": rational_envelope_checks(),
        "qos_globally_invalidated": False,
        "quantum_advantage_demonstrated": False,
        "uqpu_advantage_demonstrated": False,
    }

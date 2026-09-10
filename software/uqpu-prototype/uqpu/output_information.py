"""Executable information-output lower bounds for FND-002.

The functions here constrain the *classical information that a workload contract
requires at its output*.  They do not estimate quantum state size, computation
cost, memory capacity, communication capacity with side information, or an
achievable implementation.
"""
from __future__ import annotations

import math


def _outcome_count(value: int) -> int:
    if type(value) is not int or value < 1:
        raise ValueError("outcome_count must be an integer >= 1")
    return value


def minimum_bits_for_distinguishable_outcomes(outcome_count: int) -> int:
    """Worst-case fixed-length bits needed to label one of M outcomes exactly.

    A b-bit fixed-length label has at most 2**b distinct values, so exact
    identification of any one of M distinguishable outcomes requires
    b >= ceil(log2(M)).  This is an output-label counting bound only.
    """
    m = _outcome_count(outcome_count)
    return (m - 1).bit_length()


def fixed_width_output_bitrate_bps(
    outcome_count: int,
    results_per_second: float,
) -> float:
    """Raw bitrate for independent fixed-width outcome labels.

    This is ``ceil(log2(M)) * results_per_second``.  Correlations, variable-
    length coding, side information or a different application contract can
    change actual transport requirements, so this must not be called a general
    channel-capacity lower bound.
    """
    rate = float(results_per_second)
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("results_per_second must be finite and >= 0")
    return minimum_bits_for_distinguishable_outcomes(outcome_count) * rate


def binary_entropy_bits(probability: float) -> float:
    """Binary entropy h2(p), in bits."""
    p = float(probability)
    if not math.isfinite(p) or not 0.0 <= p <= 1.0:
        raise ValueError("probability must be finite and in [0, 1]")
    if p in (0.0, 1.0):
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def fano_mutual_information_lower_bound_bits(
    outcome_count: int,
    error_probability: float,
) -> float:
    """Fano-derived information lower bound for equiprobable M-way identity.

    For a uniformly distributed target X over M outcomes and a decoder with
    error probability Pe, Fano's inequality gives

        I(X;Y) >= log2(M) - h2(Pe) - Pe*log2(M-1).

    Negative numerical lower bounds are clipped to zero.  This constrains
    mutual information for the stated statistical decision problem; it is not
    automatically the number of qubits, transmitted bits, memory cells or
    operations required by a physical implementation.
    """
    m = _outcome_count(outcome_count)
    p = float(error_probability)
    if not math.isfinite(p) or not 0.0 <= p <= 1.0:
        raise ValueError("error_probability must be finite and in [0, 1]")
    if m == 1:
        return 0.0
    bound = math.log2(m) - binary_entropy_bits(p) - p * math.log2(m - 1)
    return max(0.0, bound)


def bitstring_assignment_output_floor_bits(variable_count: int) -> int:
    """Exact identity-output floor for one arbitrary n-bit assignment.

    There are 2**n possible assignments, therefore exact identity of an
    arbitrary assignment requires n classical output bits in the absence of
    side information.  This says nothing about the effort required to compute
    the assignment.
    """
    if type(variable_count) is not int or variable_count < 0:
        raise ValueError("variable_count must be an integer >= 0")
    return variable_count

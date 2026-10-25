"""Synthetic, finite-sample memory-order diagnostics for FND-001.

This module estimates adjacent-lag conditional mutual information in bits:
I(X_t; X_{t-k-1} | X_{t-k}, ..., X_{t-1}).

It is a descriptive diagnostic only. A small value is not a proof of Markov
order, and this module does not estimate entropy production, heat, wall-plug
energy, or any physical-system parameter.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Sequence
import math


def conditional_mutual_information_bits(
    sequence: Sequence[Hashable],
    conditioning_order: int,
) -> float:
    """Return the plug-in adjacent-lag conditional mutual information in bits.

    conditioning_order=k estimates I(X_t; X_{t-k-1} | X_{t-k:t-1}).
    For k=0 this is I(X_t; X_{t-1}). The estimate uses empirical frequencies
    and has finite-sample bias; no confidence interval or model-selection
    threshold is implied.
    """
    if (
        not isinstance(conditioning_order, int)
        or isinstance(conditioning_order, bool)
        or conditioning_order < 0
    ):
        raise ValueError("conditioning_order must be a nonnegative integer")

    values = tuple(sequence)
    if len(values) < conditioning_order + 2:
        raise ValueError("sequence is too short for the requested conditioning order")
    try:
        for symbol in values:
            hash(symbol)
    except TypeError as exc:
        raise ValueError("sequence symbols must be hashable") from exc

    joint = Counter()
    current_context = Counter()
    lagged_context = Counter()
    context_counts = Counter()

    for t in range(conditioning_order + 1, len(values)):
        current = values[t]
        lagged = values[t - conditioning_order - 1]
        context = values[t - conditioning_order:t]
        joint[(current, lagged, context)] += 1
        current_context[(current, context)] += 1
        lagged_context[(lagged, context)] += 1
        context_counts[context] += 1

    sample_count = len(values) - conditioning_order - 1
    terms = []
    for (current, lagged, context), count in joint.items():
        numerator = count * context_counts[context]
        denominator = (
            current_context[(current, context)]
            * lagged_context[(lagged, context)]
        )
        terms.append((count / sample_count) * math.log2(numerator / denominator))

    # Empirical CMI is nonnegative; clamp only floating-point roundoff.
    return max(0.0, math.fsum(terms))


def adjacent_lag_cmi_profile_bits(
    sequence: Sequence[Hashable],
    max_order: int,
) -> dict[int, float]:
    """Return adjacent-lag CMI estimates for conditioning orders 0..max_order.

    This profile can distinguish selected synthetic processes with known
    memory structure, but it does not prove a Markov order. Real-data use
    requires preregistered thresholds, uncertainty calibration, counterexample
    tests, and a separate validated entropy-production estimator.
    """
    if (
        not isinstance(max_order, int)
        or isinstance(max_order, bool)
        or max_order < 0
    ):
        raise ValueError("max_order must be a nonnegative integer")
    values = tuple(sequence)
    if len(values) < max_order + 2:
        raise ValueError("sequence is too short for the requested profile")
    return {
        order: conditional_mutual_information_bits(values, order)
        for order in range(max_order + 1)
    }

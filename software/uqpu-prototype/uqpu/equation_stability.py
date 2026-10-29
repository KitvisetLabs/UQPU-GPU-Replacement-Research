"""Finite-perturbation stability diagnostics for equation candidates.

This normalized sensitivity proxy is not the published Effective Information
Criterion (EIC), proof of structural rationality, or evidence that a candidate
is a physical law. Interpretation depends on declared scales and perturbations.
"""
from __future__ import annotations
from collections.abc import Iterable
import math


def _finite_vector(name: str, values: Iterable[object]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{name} must be a non-string iterable of numeric values")
    try:
        raw_values = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be iterable") from exc
    if not raw_values:
        raise ValueError(f"{name} must not be empty")
    converted: list[float] = []
    for value in raw_values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} values must be numeric and not boolean")
        try:
            number = float(value)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError(f"{name} values must convert to finite floats") from exc
        if not math.isfinite(number):
            raise ValueError(f"{name} values must be finite")
        converted.append(number)
    return tuple(converted)


def _normalized_l2_delta(name: str, reference: tuple[float, ...],
                         perturbed: tuple[float, ...],
                         scales: tuple[float, ...]) -> float:
    if len(reference) != len(perturbed) or len(reference) != len(scales):
        raise ValueError(f"{name} reference, perturbed values, and scales must have equal lengths")
    components: list[float] = []
    for before, after, scale in zip(reference, perturbed, scales):
        if scale <= 0.0:
            raise ValueError(f"{name} scales must be strictly positive")
        delta = (after - before) / scale
        if not math.isfinite(delta):
            raise ValueError(f"{name} normalized deltas must be finite")
        components.append(delta)
    norm = math.hypot(*components)
    if not math.isfinite(norm):
        raise ValueError(f"{name} normalized L2 delta must be finite")
    return norm


def normalized_perturbation_amplification(
    reference_input: Iterable[object],
    perturbed_input: Iterable[object],
    reference_output: Iterable[object],
    perturbed_output: Iterable[object],
    input_scales: Iterable[object],
    output_scales: Iterable[object],
) -> float:
    """Return normalized output change divided by normalized input change.

    Scales must be positive and declared before comparison. The result is
    dimensionless but comparable only with the same scales, perturbation design,
    precision and domain. Identical inputs with different outputs fail closed.
    """
    x0 = _finite_vector("reference_input", reference_input)
    x1 = _finite_vector("perturbed_input", perturbed_input)
    y0 = _finite_vector("reference_output", reference_output)
    y1 = _finite_vector("perturbed_output", perturbed_output)
    sx = _finite_vector("input_scales", input_scales)
    sy = _finite_vector("output_scales", output_scales)
    dx = _normalized_l2_delta("input", x0, x1, sx)
    dy = _normalized_l2_delta("output", y0, y1, sy)
    if dx == 0.0:
        if dy == 0.0:
            return 0.0
        raise ValueError("nonzero output change with zero input perturbation")
    ratio = dy / dx
    if not math.isfinite(ratio):
        raise ValueError("normalized perturbation amplification must be finite")
    return ratio

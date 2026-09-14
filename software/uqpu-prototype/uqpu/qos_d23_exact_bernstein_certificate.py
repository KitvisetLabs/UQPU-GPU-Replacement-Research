from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import comb

from uqpu.qos_d23_explicit_polynomial_candidate import (
    AMPLIFICATION_ERROR_BUDGET,
    DEGREE,
    GAMMA,
    ODD_CHEBYSHEV_COEFFICIENTS,
    TARGET_ENDPOINT,
)


def _fraction_from_runtime_float(value: float) -> Fraction:
    """Capture the exact binary rational represented by a Python float."""
    return Fraction.from_float(value)


def coefficient_fingerprint() -> str:
    """Bind the certificate to the exact runtime float payloads."""
    payload = "|".join(value.hex() for value in ODD_CHEBYSHEV_COEFFICIENTS)
    payload += f"|gamma={GAMMA.hex()}|budget={AMPLIFICATION_ERROR_BUDGET.hex()}"
    return sha256(payload.encode("ascii")).hexdigest()


def _chebyshev_power_basis(max_degree: int) -> list[list[Fraction]]:
    if max_degree < 0:
        raise ValueError("max_degree must be non-negative")
    if max_degree == 0:
        return [[Fraction(1)]]
    basis = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for degree in range(2, max_degree + 1):
        current = [Fraction(0)] * (degree + 1)
        for index, value in enumerate(basis[-1]):
            current[index + 1] += 2 * value
        for index, value in enumerate(basis[-2]):
            current[index] -= value
        basis.append(current)
    return basis


def frozen_polynomial_power_coefficients() -> tuple[Fraction, ...]:
    """Convert the frozen Chebyshev polynomial to exact rational power form."""
    basis = _chebyshev_power_basis(DEGREE)
    power = [Fraction(0)] * (DEGREE + 1)
    for index, coefficient in enumerate(ODD_CHEBYSHEV_COEFFICIENTS):
        degree = 2 * index + 1
        exact_coefficient = _fraction_from_runtime_float(coefficient)
        for power_index, value in enumerate(basis[degree]):
            power[power_index] += exact_coefficient * value
    return tuple(power)


def _compose_affine_power(
    power: tuple[Fraction, ...] | list[Fraction],
    start: Fraction,
    width: Fraction,
) -> list[Fraction]:
    """Return coefficients of p(start + width*t) in the power basis."""
    degree = len(power) - 1
    composed = [Fraction(0)] * (degree + 1)
    for source_degree, coefficient in enumerate(power):
        for target_degree in range(source_degree + 1):
            composed[target_degree] += (
                coefficient
                * comb(source_degree, target_degree)
                * start ** (source_degree - target_degree)
                * width ** target_degree
            )
    return composed


def _power_to_bernstein(power: list[Fraction]) -> list[Fraction]:
    """Convert a degree-n power polynomial on t in [0,1] to Bernstein form."""
    degree = len(power) - 1
    bernstein: list[Fraction] = []
    for k in range(degree + 1):
        value = Fraction(0)
        for j in range(k + 1):
            value += power[j] * Fraction(comb(k, j), comb(degree, j))
        bernstein.append(value)
    return bernstein


def _split_bernstein_half(
    coefficients: list[Fraction],
) -> tuple[list[Fraction], list[Fraction]]:
    """Exact de Casteljau subdivision at t=1/2."""
    levels = [coefficients]
    for _ in range(1, len(coefficients)):
        previous = levels[-1]
        levels.append(
            [
                (previous[index] + previous[index + 1]) / 2
                for index in range(len(previous) - 1)
            ]
        )
    left = [levels[index][0] for index in range(len(coefficients))]
    right = [
        levels[len(coefficients) - 1 - index][index]
        for index in range(len(coefficients))
    ]
    return left, right


@dataclass(frozen=True)
class BernsteinCertificate:
    threshold: Fraction
    leaf_intervals: int
    maximum_depth: int
    certified: bool
    tightest_margin: Fraction

    @property
    def threshold_float(self) -> float:
        return float(self.threshold)

    @property
    def tightest_margin_float(self) -> float:
        return float(self.tightest_margin)


def _certify_bernstein_range(
    coefficients: list[Fraction],
    *,
    threshold: Fraction,
    max_depth: int,
) -> BernsteinCertificate:
    """Prove |p| <= threshold by exact Bernstein convex-hull subdivision."""
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")

    stack: list[tuple[list[Fraction], int]] = [(coefficients, 0)]
    leaves = 0
    maximum_depth = 0
    tightest_margin = threshold

    while stack:
        current, depth = stack.pop()
        lower = min(current)
        upper = max(current)
        local_margin = min(threshold - upper, lower + threshold)

        # A polynomial on [0,1] lies in the convex hull of its Bernstein
        # coefficients.  These comparisons are exact Fraction arithmetic.
        if lower >= -threshold and upper <= threshold:
            leaves += 1
            maximum_depth = max(maximum_depth, depth)
            tightest_margin = min(tightest_margin, local_margin)
            continue

        if depth >= max_depth:
            return BernsteinCertificate(
                threshold=threshold,
                leaf_intervals=leaves,
                maximum_depth=max(maximum_depth, depth),
                certified=False,
                tightest_margin=min(tightest_margin, local_margin),
            )

        left, right = _split_bernstein_half(current)
        stack.append((right, depth + 1))
        stack.append((left, depth + 1))

    return BernsteinCertificate(
        threshold=threshold,
        leaf_intervals=leaves,
        maximum_depth=maximum_depth,
        certified=True,
        tightest_margin=tightest_margin,
    )


def global_boundedness_certificate(max_depth: int = 16) -> BernsteinCertificate:
    """Certify |P_81(x)| <= 1 for every real x in [-1,1]."""
    power = frozen_polynomial_power_coefficients()
    unit_interval_power = _compose_affine_power(power, Fraction(-1), Fraction(2))
    bernstein = _power_to_bernstein(unit_interval_power)
    return _certify_bernstein_range(
        bernstein,
        threshold=Fraction(1),
        max_depth=max_depth,
    )


def target_error_certificate(max_depth: int = 16) -> BernsteinCertificate:
    """Certify |P_81(x)-gamma*x| <= epsilon/3 on the target interval."""
    power = list(frozen_polynomial_power_coefficients())
    power[1] -= _fraction_from_runtime_float(GAMMA)
    target_interval_power = _compose_affine_power(
        power,
        _fraction_from_runtime_float(-TARGET_ENDPOINT),
        _fraction_from_runtime_float(2.0 * TARGET_ENDPOINT),
    )
    bernstein = _power_to_bernstein(target_interval_power)
    return _certify_bernstein_range(
        bernstein,
        threshold=_fraction_from_runtime_float(AMPLIFICATION_ERROR_BUDGET),
        max_depth=max_depth,
    )


def batch051_certificate() -> dict[str, object]:
    global_cert = global_boundedness_certificate()
    target_cert = target_error_certificate()
    return {
        "gate": "QOS-AUDIT-010A",
        "classification": "D23_FROZEN_FLOAT_POLYNOMIAL_EXACT_BERNSTEIN_BOUNDEDNESS_CERTIFIED_PHASES_OPEN",
        "evidence_level": "EXACT_RATIONAL_BERNSTEIN_CERTIFICATE_FOR_FROZEN_RUNTIME_FLOAT_POLYNOMIAL",
        "degree": DEGREE,
        "coefficient_fingerprint_sha256": coefficient_fingerprint(),
        "global_all_real_bound": {
            "domain": [-1.0, 1.0],
            "threshold": global_cert.threshold_float,
            "certified": global_cert.certified,
            "leaf_intervals": global_cert.leaf_intervals,
            "maximum_depth": global_cert.maximum_depth,
            "tightest_bernstein_margin_lower_bound": global_cert.tightest_margin_float,
        },
        "target_error_bound": {
            "domain": [-TARGET_ENDPOINT, TARGET_ENDPOINT],
            "threshold": target_cert.threshold_float,
            "certified": target_cert.certified,
            "leaf_intervals": target_cert.leaf_intervals,
            "maximum_depth": target_cert.maximum_depth,
            "tightest_bernstein_margin_lower_bound": target_cert.tightest_margin_float,
        },
        "formal_global_boundedness_for_frozen_runtime_polynomial_closed": global_cert.certified,
        "formal_target_error_bound_for_frozen_runtime_polynomial_closed": target_cert.certified,
        "qsp_phase_sequence_synthesized": False,
        "qsp_response_independently_reconstructed": False,
        "full_channel_repaired_D23_established": False,
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "gpu_npu_ram_dram_hbm_replacement_demonstrated": False,
        "hundred_x_advantage_demonstrated": False,
        "hundred_million_x_advantage_demonstrated": False,
        "new_physical_law": False,
    }

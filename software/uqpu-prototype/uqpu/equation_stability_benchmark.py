"""Synthetic known-equivalent-form fixture for equation-stability diagnostics.

This is a MODEL_ONLY floating-point test, not the published EIC algorithm and
not evidence that any candidate is a physical law.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
import math

from .equation_stability import normalized_perturbation_amplification


def _high_precision_reference(x: float) -> float:
    """Evaluate 1/(sqrt(1+x)+1) with an 80-digit Decimal intermediate."""
    with localcontext() as context:
        context.prec = 80
        decimal_x = Decimal(str(x))
        value = Decimal(1) / ((Decimal(1) + decimal_x).sqrt() + Decimal(1))
        return float(value)


def run_cancellation_stability_fixture() -> dict[str, object]:
    """Compare stable and cancellation-prone equivalent expressions near zero.

    For x > 0, (sqrt(1+x)-1)/x equals 1/(sqrt(1+x)+1) algebraically.
    Float64 cancellation can destroy that identity numerically at small x.
    The input/output scales are declared here solely for this synthetic fixture.
    """
    inputs = (1e-16, 4e-16)
    reference = tuple(_high_precision_reference(x) for x in inputs)
    stable = tuple(1.0 / (math.sqrt(1.0 + x) + 1.0) for x in inputs)
    cancellation_prone = tuple(
        (math.sqrt(1.0 + x) - 1.0) / x for x in inputs
    )
    input_scale = (1e-16,)
    output_scale = (1.0,)

    stable_amplification = normalized_perturbation_amplification(
        (inputs[0],), (inputs[1],), (stable[0],), (stable[1],),
        input_scale, output_scale,
    )
    cancellation_amplification = normalized_perturbation_amplification(
        (inputs[0],), (inputs[1],),
        (cancellation_prone[0],), (cancellation_prone[1],),
        input_scale, output_scale,
    )

    return {
        "fixture_id": "EQN-STABILITY-CANCEL-001",
        "evidence_class": "MODEL_ONLY_SYNTHETIC_FLOATING_POINT",
        "formula_identity": (
            "(sqrt(1+x)-1)/x = 1/(sqrt(1+x)+1), for x > 0"
        ),
        "input_points": list(inputs),
        "input_scale": input_scale[0],
        "output_scale": output_scale[0],
        "reference_kind": "80-digit Decimal intermediate, rounded to float64",
        "stable_rationalized": {
            "formula": "1/(sqrt(1+x)+1)",
            "outputs": list(stable),
            "max_abs_error": max(
                abs(value - target) for value, target in zip(stable, reference)
            ),
            "normalized_perturbation_amplification": stable_amplification,
        },
        "cancellation_prone": {
            "formula": "(sqrt(1+x)-1)/x",
            "outputs": list(cancellation_prone),
            "max_abs_error": max(
                abs(value - target)
                for value, target in zip(cancellation_prone, reference)
            ),
            "normalized_perturbation_amplification": cancellation_amplification,
        },
        "claim_boundary": (
            "Synthetic numeric diagnostic only. It does not reproduce EIC, "
            "prove structural rationality, establish physical truth, or imply "
            "device, material, fuel, fusion, finance, or QPU advantage."
        ),
    }

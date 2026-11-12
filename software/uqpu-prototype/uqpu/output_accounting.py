"""Per-accepted-result output-information accounting for FND-002.

This module connects a workload's semantic output contract to observed output
bytes and reconstruction time. Information-theoretic bounds remain distinct
from physical memory, channel capacity, energy, or implementation cost.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from .output_information import (
    fano_mutual_information_lower_bound_bits,
    fixed_width_output_bitrate_bps,
    minimum_bits_for_distinguishable_outcomes,
)

_ENCODING_MODES = {
    "fixed_width",
    "variable_length",
    "batched",
    "interactive",
    "compressed",
}


@dataclass(frozen=True)
class OutputInformationContract:
    """Output semantics and the assumptions needed for a defensible bound.

    distinguishable_outcomes counts accepted output classes under the
    workload's equivalence/quality rule, not internal states or amplitudes.
    If side information is available, the count is conditional on that
    explicitly described information. A Fano bound is available only when the
    target is uniform over those classes and allowed_error_probability describes
    decoder error.
    """

    distinguishable_outcomes: int
    exactness_required: bool = True
    allowed_error_probability: float | None = None
    uniform_prior_assumed: bool = False
    side_information_available: bool = False
    side_information_description: str | None = None
    encoding_mode: str = "fixed_width"
    required_results_per_second: float | None = None

    def validate(self) -> None:
        minimum_bits_for_distinguishable_outcomes(self.distinguishable_outcomes)
        if type(self.exactness_required) is not bool:
            raise ValueError("exactness_required must be a bool")
        if type(self.uniform_prior_assumed) is not bool:
            raise ValueError("uniform_prior_assumed must be a bool")
        if type(self.side_information_available) is not bool:
            raise ValueError("side_information_available must be a bool")
        if self.side_information_available:
            if not isinstance(self.side_information_description, str) or not self.side_information_description.strip():
                raise ValueError("side_information_description is required when side information is available")
        elif self.side_information_description is not None:
            raise ValueError("side_information_description requires side_information_available=True")
        if not isinstance(self.encoding_mode, str) or self.encoding_mode not in _ENCODING_MODES:
            raise ValueError(f"encoding_mode must be one of {sorted(_ENCODING_MODES)}")

        p = self.allowed_error_probability
        if p is not None:
            p = float(p)
            if not math.isfinite(p) or not 0.0 <= p <= 1.0:
                raise ValueError("allowed_error_probability must be finite and in [0, 1]")
        if self.exactness_required and p not in (None, 0, 0.0):
            raise ValueError("exact output requires allowed_error_probability to be 0 or None")
        if not self.exactness_required and p is None:
            raise ValueError("approximate output requires an explicit allowed_error_probability")
        if self.uniform_prior_assumed and self.exactness_required:
            raise ValueError("uniform_prior_assumed is only used for approximate Fano bounds")
        if self.uniform_prior_assumed and p is None:
            raise ValueError("Fano bound requires an explicit allowed_error_probability")
        if self.required_results_per_second is not None:
            rate = float(self.required_results_per_second)
            if not math.isfinite(rate) or rate < 0.0:
                raise ValueError("required_results_per_second must be finite and >= 0")

    @property
    def information_lower_bound_bits(self) -> float | None:
        """Return a bound only when the stated output model justifies one."""
        self.validate()
        if self.exactness_required:
            return float(minimum_bits_for_distinguishable_outcomes(
                self.distinguishable_outcomes
            ))
        if self.uniform_prior_assumed and self.allowed_error_probability is not None:
            return fano_mutual_information_lower_bound_bits(
                self.distinguishable_outcomes,
                self.allowed_error_probability,
            )
        return None

    @property
    def fixed_width_label_bitrate_lower_bound_bps(self) -> float | None:
        """Fixed-width label rate; None when encoding/side-info assumptions differ."""
        self.validate()
        if (
            self.encoding_mode != "fixed_width"
            or self.side_information_available
            or self.required_results_per_second is None
        ):
            return None
        return fixed_width_output_bitrate_bps(
            self.distinguishable_outcomes,
            self.required_results_per_second,
        )


@dataclass(frozen=True)
class OutputMeasurement:
    """Observed output and reconstruction quantities per accepted useful result."""

    measured_output_bytes_per_accepted_result: int
    reconstruction_seconds_per_accepted_result: float
    side_information_bytes_per_accepted_result: int = 0
    measured_accepted_results_per_second: float | None = None
    measured_error_probability: float | None = None

    def validate(self) -> None:
        for name, value in (
            ("measured_output_bytes_per_accepted_result",
             self.measured_output_bytes_per_accepted_result),
            ("side_information_bytes_per_accepted_result",
             self.side_information_bytes_per_accepted_result),
        ):
            if type(value) is not int or value < 0:
                raise ValueError(f"{name} must be an integer >= 0")

        reconstruction = float(self.reconstruction_seconds_per_accepted_result)
        if not math.isfinite(reconstruction) or reconstruction < 0.0:
            raise ValueError(
                "reconstruction_seconds_per_accepted_result must be finite and >= 0"
            )
        if self.measured_accepted_results_per_second is not None:
            rate = float(self.measured_accepted_results_per_second)
            if not math.isfinite(rate) or rate < 0.0:
                raise ValueError("measured_accepted_results_per_second must be finite and >= 0")
        if self.measured_error_probability is not None:
            error = float(self.measured_error_probability)
            if not math.isfinite(error) or not 0.0 <= error <= 1.0:
                raise ValueError("measured_error_probability must be finite and in [0, 1]")


@dataclass(frozen=True)
class OutputAccountingAudit:
    information_lower_bound_bits: float | None
    fixed_width_label_floor_bits: int | None
    measured_output_bits_per_accepted_result: int
    measured_egress_bits_per_accepted_result: int
    fixed_width_label_status: str
    error_budget_status: str
    measured_egress_bitrate_bps: float | None
    reconstruction_seconds_per_accepted_result: float


def audit_output_accounting(
    contract: OutputInformationContract,
    measurement: OutputMeasurement,
) -> OutputAccountingAudit:
    """Compare an explicit output contract with per-accepted-result observations.

    A payload below the fixed-width label floor is flagged for review rather
    than silently accepted. The audit never infers joules, physical memory
    capacity, channel capacity, QPU advantage, or total economic advantage.
    """
    contract.validate()
    measurement.validate()
    if measurement.side_information_bytes_per_accepted_result > 0 and not contract.side_information_available:
        raise ValueError(
            "measured side-information bytes require side_information_available=True"
        )

    output_bits = measurement.measured_output_bytes_per_accepted_result * 8
    egress_bits = (
        measurement.measured_output_bytes_per_accepted_result
        + measurement.side_information_bytes_per_accepted_result
    ) * 8

    floor = None
    if contract.encoding_mode == "fixed_width" and not contract.side_information_available:
        floor = minimum_bits_for_distinguishable_outcomes(
            contract.distinguishable_outcomes
        )
        fixed_status = "PASS" if output_bits >= floor else "BELOW_FLOOR_REQUIRES_REVIEW"
    else:
        fixed_status = "NOT_COMPARABLE"

    allowed_error = (
        0.0
        if contract.exactness_required
        else (
            float(contract.allowed_error_probability)
            if contract.allowed_error_probability is not None
            else None
        )
    )
    if measurement.measured_error_probability is None:
        error_status = "UNMEASURED"
    elif allowed_error is None:
        error_status = "NO_ERROR_BUDGET"
    elif float(measurement.measured_error_probability) <= allowed_error:
        error_status = "PASS"
    else:
        error_status = "FAIL"

    measured_rate = measurement.measured_accepted_results_per_second
    bitrate = egress_bits * float(measured_rate) if measured_rate is not None else None

    return OutputAccountingAudit(
        information_lower_bound_bits=contract.information_lower_bound_bits,
        fixed_width_label_floor_bits=floor,
        measured_output_bits_per_accepted_result=output_bits,
        measured_egress_bits_per_accepted_result=egress_bits,
        fixed_width_label_status=fixed_status,
        error_budget_status=error_status,
        measured_egress_bitrate_bps=bitrate,
        reconstruction_seconds_per_accepted_result=float(
            measurement.reconstruction_seconds_per_accepted_result
        ),
    )

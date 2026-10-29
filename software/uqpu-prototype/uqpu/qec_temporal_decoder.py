"""Evidence-gated, matched comparisons for temporal QEC decoder reports.

This helper validates provenance and apples-to-apples latency comparisons. It
cannot establish decoder correctness, quantum advantage, or physical hardware
performance from a paper's simulation/synthesis numbers.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

_EVIDENCE = {
    "LITERATURE_ONLY",
    "MODEL_ONLY",
    "SIMULATION",
    "SYNTHESIS_ESTIMATE",
    "DEVICE_MEASURED",
    "INDEPENDENTLY_REPRODUCED",
}
_STAGES = {"RTL_SIMULATION", "LOGIC_SYNTHESIS", "FPGA_MEASURED", "ASIC_MEASURED"}
_MEASURED_STAGES = {"FPGA_MEASURED", "ASIC_MEASURED"}


def _nonempty(name: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")


def _finite_positive(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric and not boolean")
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise ValueError(f"{name} must be finite and > 0")
    return result


@dataclass(frozen=True)
class DecoderObservation:
    study_id: str
    decoder_name: str
    code_family: str
    code_distance: int
    noise_model: str
    physical_error_rate: float
    syndrome_rounds: int
    target_process: str
    implementation_stage: str
    measurement_basis: str
    mean_latency_ns: float
    worst_latency_ns: float
    source_url: str
    evidence_class: str
    circuit_area_mm2: float | None = None

    def validate(self) -> None:
        for name in (
            "study_id", "decoder_name", "code_family", "noise_model",
            "target_process", "implementation_stage", "measurement_basis",
            "source_url", "evidence_class",
        ):
            _nonempty(name, getattr(self, name))
        if not self.source_url.startswith("https://"):
            raise ValueError("source_url must use https")
        for name, value in (
            ("code_distance", self.code_distance),
            ("syndrome_rounds", self.syndrome_rounds),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        rate = self.physical_error_rate
        if (
            isinstance(rate, bool)
            or not isinstance(rate, (int, float))
            or not math.isfinite(float(rate))
            or not 0 <= rate < 1
        ):
            raise ValueError("physical_error_rate must be finite and in [0, 1)")
        mean = _finite_positive("mean_latency_ns", self.mean_latency_ns)
        worst = _finite_positive("worst_latency_ns", self.worst_latency_ns)
        if mean > worst:
            raise ValueError("mean_latency_ns cannot exceed worst_latency_ns")
        if self.implementation_stage not in _STAGES:
            raise ValueError("implementation_stage is outside the governed taxonomy")
        if self.evidence_class not in _EVIDENCE:
            raise ValueError("evidence_class is outside the governed taxonomy")
        if self.circuit_area_mm2 is not None:
            _finite_positive("circuit_area_mm2", self.circuit_area_mm2)
        if self.evidence_class == "DEVICE_MEASURED" and self.implementation_stage not in _MEASURED_STAGES:
            raise ValueError("DEVICE_MEASURED requires a physical FPGA/ASIC measurement stage")


def latency_reduction_percent(
    baseline: DecoderObservation,
    candidate: DecoderObservation,
    metric: str = "mean",
) -> float:
    """Return relative latency reduction; negative values mean regression.

    Both observations must share a study, code/noise workload, error rate,
    syndrome-round count, process, implementation stage, measurement basis and
    evidence class. A cross-paper or synthesis-vs-silicon comparison fails
    closed rather than pooling incompatible results.
    """
    baseline.validate()
    candidate.validate()
    matched = (
        "study_id", "code_family", "code_distance", "noise_model",
        "physical_error_rate", "syndrome_rounds", "target_process",
        "implementation_stage", "measurement_basis", "evidence_class",
    )
    mismatches = [
        name for name in matched
        if getattr(baseline, name) != getattr(candidate, name)
    ]
    if mismatches:
        raise ValueError("unmatched decoder comparison: " + ", ".join(mismatches))
    if metric not in {"mean", "worst"}:
        raise ValueError("metric must be 'mean' or 'worst'")
    field = "mean_latency_ns" if metric == "mean" else "worst_latency_ns"
    before = float(getattr(baseline, field))
    after = float(getattr(candidate, field))
    return (before - after) / before * 100.0


def is_physical_device_evidence(observation: DecoderObservation) -> bool:
    """True only for explicitly measured/replicated physical-device records."""
    observation.validate()
    return (
        observation.implementation_stage in _MEASURED_STAGES
        and observation.evidence_class in {"DEVICE_MEASURED", "INDEPENDENTLY_REPRODUCED"}
    )

"""FND-007B3 quality-adjusted hardware/resource ledger for the 2D-QED qudit route.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Facebook: https://www.facebook.com/LoveMoneyTH
YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: primary-source hardware-data audit, conditional quality
model, finite-shot bounds, coherence-exposure diagnostics, tests and documentation.

This module does not assert measured end-to-end qudit advantage. It turns the
source-scoped gate-count advantage from Batch 042 into falsifiable conditional
hardware thresholds. Counts are circuit-resource / entangler-equivalent counts;
per-gate success variables are hypothetical inputs unless independently measured
and pinned for a concrete implementation.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class SourceHardwareContext:
    """Hardware/statistical values exposed in the 2025 Nature Physics article."""

    qutrit_repetitions: int = 150
    ququint_repetitions: int = 300
    time_evolution_repetitions: int = 150
    motional_coherence_seconds: float = 0.0274
    heating_rate_phonons_per_second: float = 2.7
    optical_t1_seconds: float = 1.1
    optical_t2_seconds: float = 0.092
    representative_blue_sideband_rabi_hz: float = 4000.0
    source: str = "Meth et al., Nature Physics 21, 570-576 (2025)"
    doi: str = "10.1038/s41567-025-02797-w"


@dataclass(frozen=True)
class SamplingEnvelope:
    repetitions: int
    outcome_abs_bound: float
    confidence: float
    worst_case_standard_error: float
    hoeffding_half_width: float


@dataclass(frozen=True)
class ResourcePair:
    name: str
    native_qudit_entangler_equivalents: int
    one_hot_qubit_entanglers: int


FULL_GAUGE_D3 = ResourcePair(
    name="full_gauge_d3",
    native_qudit_entangler_equivalents=26,
    one_hot_qubit_entanglers=90,
)

PURE_GAUGE_D3 = ResourcePair(
    name="pure_gauge_d3",
    native_qudit_entangler_equivalents=8,
    one_hot_qubit_entanglers=84,
)


def _validate_probability(value: float, name: str) -> None:
    if not (0.0 < value <= 1.0):
        raise ValueError(f"{name} must be in (0, 1]")


def circuit_survival_proxy(entanglers: int, per_entangler_success: float) -> float:
    """Independent-identical entangler survival proxy p**G.

    This intentionally ignores SPAM, coherent errors, correlations, compiler
    details and error mitigation. It is a threshold diagnostic, not a device
    fidelity model.
    """
    if entanglers <= 0:
        raise ValueError("entanglers must be positive")
    _validate_probability(per_entangler_success, "per_entangler_success")
    return per_entangler_success**entanglers


def quality_adjusted_entangler_cost(
    entanglers: int,
    per_entangler_success: float,
) -> float:
    """Entangler-equivalent attempts per successful-circuit proxy: G / p**G."""
    return entanglers / circuit_survival_proxy(entanglers, per_entangler_success)


def native_qudit_success_threshold(
    native_qudit_entanglers: int,
    one_hot_qubit_entanglers: int,
    one_hot_qubit_per_entangler_success: float,
) -> float:
    """Minimum native-qudit p for lower G/p**G than the qubit comparator.

    Solves
        G_d / p_d**G_d <= G_b / p_b**G_b
    for p_d. The count comparison must favor the native-qudit construction.
    """
    if native_qudit_entanglers <= 0 or one_hot_qubit_entanglers <= 0:
        raise ValueError("entangler counts must be positive")
    if native_qudit_entanglers >= one_hot_qubit_entanglers:
        raise ValueError("native_qudit_entanglers must be smaller for this threshold")
    _validate_probability(
        one_hot_qubit_per_entangler_success,
        "one_hot_qubit_per_entangler_success",
    )
    threshold = (
        (native_qudit_entanglers / one_hot_qubit_entanglers)
        * one_hot_qubit_per_entangler_success**one_hot_qubit_entanglers
    ) ** (1.0 / native_qudit_entanglers)
    return threshold


def serial_duration_ceiling_seconds(coherence_seconds: float, entanglers: int) -> float:
    """Mean serial duration budget per counted entangler within one coherence time."""
    if coherence_seconds <= 0.0:
        raise ValueError("coherence_seconds must be positive")
    if entanglers <= 0:
        raise ValueError("entanglers must be positive")
    return coherence_seconds / entanglers


def bounded_mean_sampling_envelope(
    repetitions: int,
    outcome_abs_bound: float = 1.0,
    confidence: float = 0.95,
) -> SamplingEnvelope:
    """Worst-case SEM and Hoeffding half-width for outcomes in [-B, B]."""
    if repetitions <= 0:
        raise ValueError("repetitions must be positive")
    if outcome_abs_bound <= 0.0:
        raise ValueError("outcome_abs_bound must be positive")
    if not (0.0 < confidence < 1.0):
        raise ValueError("confidence must be in (0, 1)")
    alpha = 1.0 - confidence
    worst_case_standard_error = outcome_abs_bound / math.sqrt(repetitions)
    hoeffding_half_width = outcome_abs_bound * math.sqrt(
        2.0 * math.log(2.0 / alpha) / repetitions
    )
    return SamplingEnvelope(
        repetitions=repetitions,
        outcome_abs_bound=outcome_abs_bound,
        confidence=confidence,
        worst_case_standard_error=worst_case_standard_error,
        hoeffding_half_width=hoeffding_half_width,
    )


def repetitions_for_hoeffding(
    target_half_width: float,
    outcome_abs_bound: float = 1.0,
    confidence: float = 0.95,
) -> int:
    """Sufficient iid repetitions for a two-sided Hoeffding half-width target."""
    if target_half_width <= 0.0:
        raise ValueError("target_half_width must be positive")
    if outcome_abs_bound <= 0.0:
        raise ValueError("outcome_abs_bound must be positive")
    if not (0.0 < confidence < 1.0):
        raise ValueError("confidence must be in (0, 1)")
    alpha = 1.0 - confidence
    required = (
        2.0
        * outcome_abs_bound**2
        * math.log(2.0 / alpha)
        / target_half_width**2
    )
    return math.ceil(required)


def expected_heating_over_interval(
    heating_rate_phonons_per_second: float,
    interval_seconds: float,
) -> float:
    if heating_rate_phonons_per_second < 0.0:
        raise ValueError("heating rate must be non-negative")
    if interval_seconds < 0.0:
        raise ValueError("interval_seconds must be non-negative")
    return heating_rate_phonons_per_second * interval_seconds


def quality_threshold_grid(resource_pair: ResourcePair) -> list[dict[str, float]]:
    """Threshold and equal-fidelity proxy comparisons at frozen diagnostic points."""
    rows: list[dict[str, float]] = []
    for qubit_success in (0.98, 0.99, 0.995, 0.999):
        qudit_threshold = native_qudit_success_threshold(
            resource_pair.native_qudit_entangler_equivalents,
            resource_pair.one_hot_qubit_entanglers,
            qubit_success,
        )
        qudit_equal_fidelity_cost = quality_adjusted_entangler_cost(
            resource_pair.native_qudit_entangler_equivalents,
            qubit_success,
        )
        qubit_cost = quality_adjusted_entangler_cost(
            resource_pair.one_hot_qubit_entanglers,
            qubit_success,
        )
        rows.append(
            {
                "one_hot_qubit_per_entangler_success": qubit_success,
                "native_qudit_break_even_success": qudit_threshold,
                "equal_fidelity_native_qudit_cost": qudit_equal_fidelity_cost,
                "equal_fidelity_one_hot_qubit_cost": qubit_cost,
                "equal_fidelity_qubit_to_qudit_cost_ratio": (
                    qubit_cost / qudit_equal_fidelity_cost
                ),
            }
        )
    return rows


def batch044_certificate() -> dict[str, object]:
    hardware = SourceHardwareContext()
    sampling_150 = bounded_mean_sampling_envelope(hardware.qutrit_repetitions)
    sampling_300 = bounded_mean_sampling_envelope(hardware.ququint_repetitions)

    serial_budgets = {}
    for pair in (FULL_GAUGE_D3, PURE_GAUGE_D3):
        serial_budgets[pair.name] = {
            "motional_coherence_native_qudit_us": 1e6
            * serial_duration_ceiling_seconds(
                hardware.motional_coherence_seconds,
                pair.native_qudit_entangler_equivalents,
            ),
            "motional_coherence_one_hot_qubit_us": 1e6
            * serial_duration_ceiling_seconds(
                hardware.motional_coherence_seconds,
                pair.one_hot_qubit_entanglers,
            ),
            "optical_t2_native_qudit_us": 1e6
            * serial_duration_ceiling_seconds(
                hardware.optical_t2_seconds,
                pair.native_qudit_entangler_equivalents,
            ),
            "optical_t2_one_hot_qubit_us": 1e6
            * serial_duration_ceiling_seconds(
                hardware.optical_t2_seconds,
                pair.one_hot_qubit_entanglers,
            ),
        }

    return {
        "batch": 44,
        "gate": "FND-007B3",
        "classification": "LATTICE_QED_QUDIT_QUALITY_ADJUSTED_HARDWARE_THRESHOLD_LEDGER",
        "evidence_level": "SOURCE_GROUNDED_CONDITIONAL_HARDWARE_DIAGNOSTIC",
        "source_hardware_context": asdict(hardware),
        "resource_pairs": [asdict(FULL_GAUGE_D3), asdict(PURE_GAUGE_D3)],
        "quality_thresholds": {
            FULL_GAUGE_D3.name: quality_threshold_grid(FULL_GAUGE_D3),
            PURE_GAUGE_D3.name: quality_threshold_grid(PURE_GAUGE_D3),
        },
        "serial_coherence_budgets": serial_budgets,
        "sampling": {
            "qutrit_150": asdict(sampling_150),
            "ququint_300": asdict(sampling_300),
            "hoeffding_repetitions_for_abs_error_0_10": repetitions_for_hoeffding(0.10),
            "hoeffding_repetitions_for_abs_error_0_05": repetitions_for_hoeffding(0.05),
            "hoeffding_repetitions_for_abs_error_0_02": repetitions_for_hoeffding(0.02),
            "hoeffding_repetitions_for_abs_error_0_01": repetitions_for_hoeffding(0.01),
        },
        "motional_heating_during_one_motional_coherence_time": expected_heating_over_interval(
            hardware.heating_rate_phonons_per_second,
            hardware.motional_coherence_seconds,
        ),
        "interpretation": {
            "positive": (
                "The source-scoped gate-count advantage has substantial conditional "
                "headroom under a simple independent-entangler survival proxy."
            ),
            "falsifier": (
                "If measured native-qudit entangler quality, duration, SPAM, control "
                "overhead, or cost crosses the frozen break-even boundary, the gate-count "
                "advantage does not survive as a quality-adjusted hardware advantage."
            ),
            "unresolved": (
                "This batch does not pin directly comparable native-qudit and one-hot-qubit "
                "per-entangler fidelities, exact compiled durations, readout confusion "
                "matrices, parallel schedules, calibration burden, or monetary cost."
            ),
        },
        "non_claims": {
            "measured_end_to_end_qudit_advantage": False,
            "real_qpu_reproduction_by_uqpu": False,
            "quantum_advantage": False,
            "direct_quark_computer": False,
            "qcd_simulation_demonstrated_by_uqpu": False,
            "universal_qudit_advantage": False,
            "gpu_npu_ram_dram_hbm_replacement": False,
            "one_hundred_x": False,
            "one_hundred_million_x": False,
            "new_physical_law": False,
        },
    }

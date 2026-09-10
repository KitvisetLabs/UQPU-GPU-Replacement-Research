"""Small executable physical-limit helpers for deep-frontier research.

These functions expose ideal lower bounds, not engineering performance predictions.
They are intended for evidence-gated comparison against measured systems.
"""
from __future__ import annotations

import math

BOLTZMANN_CONSTANT_J_PER_K = 1.380649e-23  # exact SI value
PLANCK_CONSTANT_J_S = 6.62607015e-34       # exact SI value
HBAR_J_S = PLANCK_CONSTANT_J_S / (2.0 * math.pi)


def _positive_finite(name: str, value: float) -> float:
    x = float(value)
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name} must be finite and > 0")
    return x


def landauer_minimum_joule_per_bit(temperature_kelvin: float) -> float:
    """Ideal minimum heat for erasing one classical bit at temperature T.

    E_min = k_B T ln(2). This is a lower bound for logically irreversible
    erasure, not a prediction of processor, memory, network or refrigerator
    energy consumption.
    """
    t = _positive_finite("temperature_kelvin", temperature_kelvin)
    return BOLTZMANN_CONSTANT_J_PER_K * t * math.log(2.0)


def landauer_minimum_joule(erased_bits: float, temperature_kelvin: float) -> float:
    """Ideal Landauer heat lower bound for a number of erased bits."""
    bits = float(erased_bits)
    if not math.isfinite(bits) or bits < 0.0:
        raise ValueError("erased_bits must be finite and >= 0")
    return bits * landauer_minimum_joule_per_bit(temperature_kelvin)


def landauer_max_bit_erasures_per_joule(temperature_kelvin: float) -> float:
    """Reciprocal of the Landauer per-bit floor; an ideal bound only."""
    return 1.0 / landauer_minimum_joule_per_bit(temperature_kelvin)


def margolus_levitin_min_seconds(mean_energy_above_ground_joule: float) -> float:
    """Orthogonal-state transition time lower bound in the ML setting.

    tau >= pi*hbar/(2 E) = h/(4 E), where E is mean energy above the
    ground state. This must not be interpreted as an achievable gate time.
    """
    energy = _positive_finite(
        "mean_energy_above_ground_joule", mean_energy_above_ground_joule
    )
    return PLANCK_CONSTANT_J_S / (4.0 * energy)


def margolus_levitin_max_orthogonal_transitions_per_second(
    mean_energy_above_ground_joule: float,
) -> float:
    """Reciprocal of the ML minimum transition time; an ideal upper bound."""
    return 1.0 / margolus_levitin_min_seconds(mean_energy_above_ground_joule)


def margolus_levitin_required_mean_energy_joule(
    observed_duration_seconds: float,
) -> float:
    """Invert the ML expression for a supplied duration.

    Returns E_req = h/(4*t). This is the mean energy above the ground state
    that would make the Margolus-Levitin lower bound equal ``t`` in the
    orthogonal-state setting. It is *not* an estimate of the actual device or
    control energy and does not prove that a hardware gate is an orthogonal
    state transition.
    """
    duration = _positive_finite("observed_duration_seconds", observed_duration_seconds)
    return PLANCK_CONSTANT_J_S / (4.0 * duration)


def margolus_levitin_equivalent_frequency_hz(
    observed_duration_seconds: float,
) -> float:
    """Return E_req/h = 1/(4*t) for the inverse ML duration diagnostic.

    The result is an equivalent energy-frequency scale, not a qubit resonance,
    drive frequency, Rabi rate or measured control bandwidth.
    """
    duration = _positive_finite("observed_duration_seconds", observed_duration_seconds)
    return 1.0 / (4.0 * duration)


def margolus_levitin_observed_to_bound_ratio(
    observed_duration_seconds: float,
    mean_energy_above_ground_joule: float,
) -> float:
    """Ratio of an observed duration to the ML lower-bound time.

    Interpret this ratio only when the supplied energy refers to the same
    physical evolution and the Margolus-Levitin assumptions are appropriate.
    A large ratio by itself does not imply an engineering speedup is attainable.
    """
    observed = _positive_finite("observed_duration_seconds", observed_duration_seconds)
    return observed / margolus_levitin_min_seconds(mean_energy_above_ground_joule)

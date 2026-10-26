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


def fault_tolerance_memory_log_overhead_term(
    logical_qubits: int,
    time_steps: int,
    target_error: float,
) -> float:
    """Return log(S / epsilon) / K for a scoped fault-tolerant memory model.

    Bharti, Haug and Tanggara (arXiv:2608.26272) show
    C_min(K,S,epsilon) = Theta(S * (K + log(S/epsilon))) for their
    independent-erasure memory model with the stated noise/error assumptions
    and ideal recovery. This helper returns only the dimensionless
    log(S/epsilon)/K term that controls the width-duration crossover.

    This is an asymptotic scaling diagnostic, not an exact overhead, a
    hardware-resource prediction, a bound for arbitrary noise models, or
    evidence of a physical or economic advantage. Applying the paper's
    theorem still requires checking its full assumptions.
    """
    if (
        not isinstance(logical_qubits, int)
        or isinstance(logical_qubits, bool)
        or logical_qubits <= 0
    ):
        raise ValueError("logical_qubits must be a positive integer")
    if (
        not isinstance(time_steps, int)
        or isinstance(time_steps, bool)
        or time_steps <= 0
    ):
        raise ValueError("time_steps must be a positive integer")
    epsilon = float(target_error)
    if not math.isfinite(epsilon) or not 0.0 < epsilon < 1.0:
        raise ValueError("target_error must be finite and strictly between 0 and 1")
    # Difference of logs avoids overflow in time_steps / epsilon.
    return (math.log(time_steps) - math.log(epsilon)) / logical_qubits

def squeezed_vacuum_mean_photon_number(squeezing_parameter: float) -> float:
    """Mean photon number nbar = sinh(r)^2 for a single-mode squeezed vacuum.

    This is a probe-state resource count, not wall-plug energy for generating,
    stabilizing or detecting the squeezed field. The helper does not model a
    two-mode protocol's total photon budget or any device inefficiency.
    """
    r = float(squeezing_parameter)
    if not math.isfinite(r) or r < 0.0:
        raise ValueError("squeezing_parameter must be finite and >= 0")
    try:
        value = math.sinh(r) ** 2
    except OverflowError as exc:
        raise ValueError("squeezing_parameter exceeds floating-point range") from exc
    if not math.isfinite(value):
        raise ValueError("squeezing_parameter exceeds floating-point range")
    return value


def squeezed_vacuum_squeezing_for_mean_photon_number(
    mean_photon_number: float,
) -> float:
    """Invert nbar = sinh(r)^2 for a single-mode squeezed vacuum.

    The inverse is r = asinh(sqrt(nbar)); it is a state-resource relation,
    not an estimate of source/pump electricity or practical hardware cost.
    """
    nbar = float(mean_photon_number)
    if not math.isfinite(nbar) or nbar < 0.0:
        raise ValueError("mean_photon_number must be finite and >= 0")
    return math.asinh(math.sqrt(nbar))

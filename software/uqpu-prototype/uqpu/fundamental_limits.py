"""Executable physical-limit and statistical-certificate helpers.

Physical-limit functions expose scoped ideal lower bounds, not engineering
predictions. Statistical helpers encode explicit sampling assumptions and do
not replace physical-energy measurement or accepted-task cost accounting.
"""
from __future__ import annotations

import math
from collections.abc import Sequence

BOLTZMANN_CONSTANT_J_PER_K = 1.380649e-23  # exact SI value
PLANCK_CONSTANT_J_S = 6.62607015e-34       # exact SI value
HBAR_J_S = PLANCK_CONSTANT_J_S / (2.0 * math.pi)


def _positive_finite(name: str, value: float) -> float:
    x = float(value)
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name} must be finite and > 0")
    return x


def planckian_thermalization_min_seconds(temperature_kelvin: float) -> float:
    """Conditional lower bound for a universal thermalization machine.

    In the framework of Abiuso et al., a fixed machine that must thermalize
    multiple possible Hamiltonians to their corresponding Gibbs states has
    tau >= hbar/(2*k_B*T) in the sufficiently mixed finite-temperature regime
    (beta*Delta less than or of order one), with sufficiently small output
    error. This is not a generic computation/gate-time bound and does not
    apply to preparing one known thermal state by an arbitrary task-specific
    routine. It is a theoretical lower bound, not a device prediction.
    """
    t = _positive_finite("temperature_kelvin", temperature_kelvin)
    return HBAR_J_S / (2.0 * BOLTZMANN_CONSTANT_J_PER_K * t)


def low_temperature_gap_thermalization_min_seconds(
    spectral_gap_joule: float,
) -> float:
    """Conditional low-temperature thermalization bound, tau >= hbar/Delta.

    This asymptotic regime applies to the same universal thermalization-machine
    task when beta*Delta is much greater than one. It is not a general lower
    bound for arbitrary computation or a claim about measured device latency.
    """
    gap = _positive_finite("spectral_gap_joule", spectral_gap_joule)
    return HBAR_J_S / gap


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



def landauer_gap_ratio_for_accepted_task(
    measured_joule_per_accepted_task: float,
    irreversible_erased_bits_per_accepted_task: float,
    temperature_kelvin: float,
) -> float:
    """Compare measured task energy with a matched Landauer erasure floor.

    Inputs must share one accepted-task boundary. The erasure count is the
    average logically irreversible bit erasures per accepted result; include
    failed attempts/retries only when their energy is in the numerator. The
    single temperature must fit the counted erasures; multiple temperatures
    require a stage-resolved sum.

    This diagnostic does not claim the floor is reachable or equals total
    device energy. A ratio below one triggers a boundary/measurement/uncertainty
    audit, not a new-physics conclusion.
    """
    if isinstance(measured_joule_per_accepted_task, bool):
        raise ValueError("measured_joule_per_accepted_task must not be boolean")
    if isinstance(irreversible_erased_bits_per_accepted_task, bool):
        raise ValueError("irreversible_erased_bits_per_accepted_task must not be boolean")
    measured = _positive_finite(
        "measured_joule_per_accepted_task", measured_joule_per_accepted_task
    )
    erased_bits = _positive_finite(
        "irreversible_erased_bits_per_accepted_task",
        irreversible_erased_bits_per_accepted_task,
    )
    temperature = _positive_finite("temperature_kelvin", temperature_kelvin)
    floor = landauer_minimum_joule(erased_bits, temperature)
    return measured / floor


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



def bounded_observable_hoeffding_radii(
    shots_per_observable: "Sequence[int]",
    failure_probability: float,
) -> tuple[float, ...]:
    """Return union-bound Hoeffding radii for bounded observable estimates.

    Implements epsilon_i = sqrt(2 * ln(2*K/delta) / N_i), as used by
    Pagliaro et al., "Certifying Ergotropy under Partial Information"
    (Phys. Rev. Lett. 137, 130401 (2026), arXiv:2603.18828).

    Assumptions: K >= 1 observables, each observable has spectrum in [-1, 1],
    each estimate uses N_i independent shots, and 0 < delta < 1 is the total
    failure-probability allocation. The union bound gives simultaneous
    coverage of at least 1-delta under these assumptions.

    This is only a statistical confidence-radius helper. It does not solve the
    paper's semidefinite programs, calculate ergotropy, validate a Hamiltonian,
    or measure total device energy.
    """
    if not isinstance(shots_per_observable, Sequence) or isinstance(
        shots_per_observable, (str, bytes)
    ):
        raise ValueError("shots_per_observable must be a nonempty sequence of positive integers")
    shots = tuple(shots_per_observable)
    if not shots:
        raise ValueError("shots_per_observable must not be empty")
    if any(
        not isinstance(n, int) or isinstance(n, bool) or n <= 0
        for n in shots
    ):
        raise ValueError("each shot count must be a positive integer")
    delta = float(failure_probability)
    if not math.isfinite(delta) or not 0.0 < delta < 1.0:
        raise ValueError("failure_probability must be finite and strictly between 0 and 1")
    observable_count = len(shots)
    log_term = math.log(2.0 * observable_count / delta)
    return tuple(math.sqrt(2.0 * log_term / n) for n in shots)

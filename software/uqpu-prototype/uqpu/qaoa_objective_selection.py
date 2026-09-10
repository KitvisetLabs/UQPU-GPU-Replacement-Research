"""Objective-selection experiments for bounded p=1 QAOA grids.

This module is deliberately limited to small exact-statevector verification
fixtures. It compares mean-energy selection against lower-tail CVaR selection
using exactly the same candidate parameter grid. It is not a scalable optimizer
and it is not evidence of real-QPU advantage.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

from .optimization_baseline import QuboInstance
from .qaoa import qaoa_program, qubo_to_ising
from .small_statevector import probabilities


@dataclass(frozen=True)
class ObjectiveSelectionResult:
    objective: str
    alpha: float | None
    score: float
    gamma: float
    beta: float
    expected_energy: float
    optimum_probability: float


@dataclass(frozen=True)
class ObjectiveSweepResult:
    evaluations: int
    gamma_steps: int
    beta_steps: int
    exact_optimum: float
    selections: tuple[ObjectiveSelectionResult, ...]


def _validate_distribution(probabilities_: Iterable[float], energies: Iterable[float]):
    probs = tuple(float(p) for p in probabilities_)
    ens = tuple(float(e) for e in energies)
    if not probs or len(probs) != len(ens):
        raise ValueError("probabilities and energies must be non-empty and equal length")
    if any(not math.isfinite(p) or p < 0.0 for p in probs):
        raise ValueError("probabilities must be finite and non-negative")
    if any(not math.isfinite(e) for e in ens):
        raise ValueError("energies must be finite")
    if not math.isclose(sum(probs), 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError("probabilities must sum to one")
    return probs, ens


def expected_energy(probabilities_: Iterable[float], energies: Iterable[float]) -> float:
    probs, ens = _validate_distribution(probabilities_, energies)
    return sum(p * e for p, e in zip(probs, ens))


def cvar_minimization(probabilities_: Iterable[float], energies: Iterable[float], alpha: float) -> float:
    """Return lower-tail CVaR for a minimization objective.

    The best (lowest-energy) probability mass is accumulated until ``alpha``.
    The final state may contribute only a fractional probability mass so the
    denominator is exactly alpha. At alpha=1 this equals the ordinary mean.
    """
    probs, ens = _validate_distribution(probabilities_, energies)
    a = float(alpha)
    if not math.isfinite(a) or not 0.0 < a <= 1.0:
        raise ValueError("alpha must be finite and in (0, 1]")
    remaining = a
    weighted = 0.0
    for energy, probability in sorted(zip(ens, probs), key=lambda row: row[0]):
        take = min(remaining, probability)
        weighted += take * energy
        remaining -= take
        if remaining <= 1e-15:
            break
    if remaining > 1e-9:
        raise ValueError("insufficient probability mass")
    return weighted / a


def _optimum_probability(probabilities_: tuple[float, ...], energies: tuple[float, ...], optimum: float) -> float:
    return sum(
        p for p, e in zip(probabilities_, energies)
        if math.isclose(e, optimum, rel_tol=0.0, abs_tol=1e-10)
    )


def compare_p1_grid_objectives(
    instance: QuboInstance,
    *,
    alphas: tuple[float, ...] = (0.25, 0.5, 0.75),
    gamma_steps: int = 24,
    beta_steps: int = 24,
    contract_id: str = "",
) -> ObjectiveSweepResult:
    """Compare mean-energy and CVaR selection on one shared p=1 grid.

    Every strategy sees the identical parameter candidates. ``evaluations`` is
    therefore the shared circuit-evaluation budget, not a sum over strategies.
    """
    if type(gamma_steps) is not int or type(beta_steps) is not int:
        raise ValueError("grid steps must be integers")
    if not 2 <= gamma_steps <= 128 or not 2 <= beta_steps <= 128:
        raise ValueError("grid steps must be in 2..128")
    if not alphas:
        raise ValueError("at least one CVaR alpha is required")
    normalized_alphas = tuple(float(a) for a in alphas)
    if len(set(normalized_alphas)) != len(normalized_alphas):
        raise ValueError("CVaR alphas must be unique")
    if any(not math.isfinite(a) or not 0.0 < a <= 1.0 for a in normalized_alphas):
        raise ValueError("CVaR alphas must be finite and in (0, 1]")

    objective = qubo_to_ising(instance)
    n = len(objective.variables)
    if n > 12:
        raise ValueError("objective-selection verification is capped at 12 qubits")
    energies = tuple(instance.energy(objective.assignment(i)) for i in range(1 << n))
    optimum = min(energies)

    best_mean = None
    best_cvar = {alpha: None for alpha in normalized_alphas}
    evaluations = 0

    for gi in range(gamma_steps):
        gamma = math.pi * gi / gamma_steps
        for bi in range(beta_steps):
            beta = math.pi * bi / beta_steps
            probs = probabilities(qaoa_program(instance, [gamma], [beta], shots=1, contract_id=contract_id))
            mean = expected_energy(probs, energies)
            optimum_probability = _optimum_probability(probs, energies, optimum)
            evaluations += 1

            mean_candidate = (mean, gamma, beta, optimum_probability)
            if best_mean is None or mean_candidate[:3] < best_mean[:3]:
                best_mean = mean_candidate

            for alpha in normalized_alphas:
                score = cvar_minimization(probs, energies, alpha)
                candidate = (score, mean, gamma, beta, optimum_probability)
                previous = best_cvar[alpha]
                # Mean energy is a deterministic secondary criterion when a
                # CVaR tail is flat; optimum probability is diagnostic only.
                if previous is None or candidate[:4] < previous[:4]:
                    best_cvar[alpha] = candidate

    selections = [
        ObjectiveSelectionResult(
            objective="mean_energy",
            alpha=None,
            score=best_mean[0],
            gamma=best_mean[1],
            beta=best_mean[2],
            expected_energy=best_mean[0],
            optimum_probability=best_mean[3],
        )
    ]
    for alpha in normalized_alphas:
        score, mean, gamma, beta, optimum_probability = best_cvar[alpha]
        selections.append(ObjectiveSelectionResult(
            objective="cvar_minimization",
            alpha=alpha,
            score=score,
            gamma=gamma,
            beta=beta,
            expected_energy=mean,
            optimum_probability=optimum_probability,
        ))

    return ObjectiveSweepResult(
        evaluations=evaluations,
        gamma_steps=gamma_steps,
        beta_steps=beta_steps,
        exact_optimum=float(optimum),
        selections=tuple(selections),
    )

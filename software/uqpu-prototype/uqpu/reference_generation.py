from __future__ import annotations
from dataclasses import dataclass

from .benchmark_tiers import BenchmarkTier
from .optimized_solver import ortools_available, solve_qubo_ortools
from .reference_certificate import ObjectiveReference, ReferenceKind


@dataclass(frozen=True)
class ReferenceGenerationResult:
    reference: ObjectiveReference
    runtime_seconds: float
    solver_status: str
    proven_optimal: bool


def generate_ortools_reference(
    tier: BenchmarkTier,
    *,
    time_limit_seconds: float = 60.0,
    workers: int = 1,
) -> ReferenceGenerationResult:
    if not ortools_available():
        raise RuntimeError("OR-Tools optional dependency is unavailable")
    result=solve_qubo_ortools(
        tier.instance(),
        time_limit_seconds=time_limit_seconds,
        workers=workers,
    )
    kind=ReferenceKind.EXACT_OPTIMUM if result.proven_optimal else ReferenceKind.BEST_KNOWN_FEASIBLE
    reference=ObjectiveReference(
        contract_id=tier.contract().contract_id,
        kind=kind,
        objective=result.objective,
        method=result.solver_name,
        evidence_level="MEASURED_LOCAL",
        source="generated://uqpu/reference_generation/generate_ortools_reference",
        notes=(
            f"tier={tier.name}; solver_status={result.solver_status}; "
            f"runtime_seconds={result.runtime_seconds}; workers={workers}; "
            "EXACT_OPTIMUM is emitted only when the solver reports OPTIMAL."
        ),
    )
    reference.validate()
    return ReferenceGenerationResult(reference,result.runtime_seconds,result.solver_status,result.proven_optimal)

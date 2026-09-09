from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter

from .benchmark_artifact import BenchmarkArtifact
from .benchmark_tiers import BenchmarkTier
from .scalable_qubo import greedy_bitflip
from .optimized_solver import ortools_available, solve_qubo_ortools
from .reference_certificate import ObjectiveReference, assess_minimization_quality


@dataclass(frozen=True)
class TierRun:
    tier: str
    contract_id: str
    artifact: BenchmarkArtifact


def _accepted(tier: BenchmarkTier, objective: float, reference: ObjectiveReference | None) -> tuple[bool,str]:
    if reference is None:
        return False,"quality_unverified:no_reference"
    if reference.contract_id != tier.contract().contract_id:
        raise ValueError("reference contract_id does not match benchmark tier")
    q=assess_minimization_quality(objective,reference,tier.required_relative_gap)
    return q.verified_quality,(
        f"quality_certificate={q.certificate_id}; kind={q.reference_kind.value}; "
        f"relative_gap={q.relative_gap}; accepted={q.accepted}; verified_quality={q.verified_quality}"
    )


def run_greedy_tier(
    tier: BenchmarkTier,
    *,
    restarts: int = 8,
    seed: int = 0,
    reference: ObjectiveReference | None = None,
) -> TierRun:
    instance=tier.instance()
    t0=perf_counter()
    _, objective=greedy_bitflip(instance,restarts=restarts,seed=seed)
    runtime=perf_counter()-t0
    accepted,quality_note=_accepted(tier,objective,reference)
    artifact=BenchmarkArtifact(
        contract_id=tier.contract().contract_id,
        implementation="uqpu.scalable_qubo.greedy_bitflip",
        solver_class="heuristic-classical-cpu",
        objective=objective,
        accepted=accepted,
        runtime_seconds=runtime,
        evidence_level="MEASURED_LOCAL",
        notes=f"tier={tier.name}; restarts={restarts}; seed={seed}; {quality_note}",
    )
    artifact.validate()
    return TierRun(tier.name,tier.contract().contract_id,artifact)


def run_ortools_tier(
    tier: BenchmarkTier,
    *,
    time_limit_seconds: float = 30.0,
    workers: int = 1,
    reference: ObjectiveReference | None = None,
) -> TierRun:
    if not ortools_available():
        raise RuntimeError("OR-Tools optional dependency is unavailable")
    result=solve_qubo_ortools(tier.instance(),time_limit_seconds=time_limit_seconds,workers=workers)
    accepted,quality_note=_accepted(tier,result.objective,reference)
    artifact=BenchmarkArtifact(
        contract_id=tier.contract().contract_id,
        implementation="uqpu.optimized_solver.solve_qubo_ortools",
        solver_class="optimized-classical-cpu",
        objective=result.objective,
        accepted=accepted,
        runtime_seconds=result.runtime_seconds,
        evidence_level="MEASURED_LOCAL",
        notes=(
            f"tier={tier.name}; status={result.solver_status}; proven_optimal={result.proven_optimal}; "
            f"workers={workers}; {quality_note}"
        ),
    )
    artifact.validate()
    return TierRun(tier.name,tier.contract().contract_id,artifact)

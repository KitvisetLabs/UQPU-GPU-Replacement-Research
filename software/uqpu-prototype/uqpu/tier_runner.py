from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter

from .benchmark_artifact import BenchmarkArtifact
from .benchmark_tiers import BenchmarkTier
from .scalable_qubo import greedy_bitflip
from .optimized_solver import ortools_available, solve_qubo_ortools


@dataclass(frozen=True)
class TierRun:
    tier: str
    contract_id: str
    artifact: BenchmarkArtifact


def run_greedy_tier(tier: BenchmarkTier, *, restarts: int = 8, seed: int = 0) -> TierRun:
    instance=tier.instance()
    t0=perf_counter()
    _, objective=greedy_bitflip(instance,restarts=restarts,seed=seed)
    runtime=perf_counter()-t0
    artifact=BenchmarkArtifact(
        contract_id=tier.contract().contract_id,
        implementation="uqpu.scalable_qubo.greedy_bitflip",
        solver_class="heuristic-classical-cpu",
        objective=objective,
        accepted=True,
        runtime_seconds=runtime,
        evidence_level="MEASURED_LOCAL",
        notes=f"tier={tier.name}; restarts={restarts}; seed={seed}; acceptance requires a separate reference objective",
    )
    artifact.validate()
    return TierRun(tier.name,tier.contract().contract_id,artifact)


def run_ortools_tier(tier: BenchmarkTier, *, time_limit_seconds: float = 30.0, workers: int = 1) -> TierRun:
    if not ortools_available():
        raise RuntimeError("OR-Tools optional dependency is unavailable")
    result=solve_qubo_ortools(tier.instance(),time_limit_seconds=time_limit_seconds,workers=workers)
    artifact=BenchmarkArtifact(
        contract_id=tier.contract().contract_id,
        implementation="uqpu.optimized_solver.solve_qubo_ortools",
        solver_class="optimized-classical-cpu",
        objective=result.objective,
        accepted=result.proven_optimal,
        runtime_seconds=result.runtime_seconds,
        evidence_level="MEASURED_LOCAL",
        notes=f"tier={tier.name}; status={result.solver_status}; proven_optimal={result.proven_optimal}; workers={workers}",
    )
    artifact.validate()
    return TierRun(tier.name,tier.contract().contract_id,artifact)

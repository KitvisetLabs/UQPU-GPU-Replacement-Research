from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable, List

from .compiler import SemanticCompiler
from .cost import CostModel
from .ir import Workload


@dataclass
class BenchmarkResult:
    workload: str
    backend: str
    evidence_level: str
    uqpu_cost_per_task: float
    gpu_cost_per_task: float
    cost_advantage: float
    cost_tier: str
    total_seconds: float
    logical_qubits: int
    physical_qubits: int
    shots: int
    confidence: float
    classification: str

    def to_dict(self):
        return asdict(self)


def classify(advantage: float) -> str:
    if advantage >= 100:
        return "COMPETITIVELY_SUPPORTED"
    if advantage > 1:
        return "QUANTUM_ADVANTAGE_CANDIDATE"
    return "NO_ADVANTAGE_FOUND"


def cost_tier(advantage: float) -> str:
    thresholds = [
        (100_000_000, "C7_100M_MOONSHOT"),
        (10_000_000, "C6_10M"),
        (1_000_000, "C5_1M"),
        (100_000, "C4_100K"),
        (10_000, "C3_10K"),
        (1_000, "C2_1K"),
        (100, "C1_100X_MINIMUM"),
    ]
    for threshold, label in thresholds:
        if advantage >= threshold:
            return label
    return "BELOW_TARGET"


def run_benchmarks(workloads: Iterable[Workload], gpu_costs: dict[str, float], compiler: SemanticCompiler | None = None) -> List[BenchmarkResult]:
    compiler = compiler or SemanticCompiler()
    results: List[BenchmarkResult] = []
    for workload in workloads:
        if workload.name not in gpu_costs:
            raise KeyError(f"missing GPU cost baseline for {workload.name}")
        plan = compiler.compile(workload)
        gpu_cost = gpu_costs[workload.name]
        uqpu_cost = plan.selected.cost.total
        advantage = CostModel.advantage(gpu_cost, uqpu_cost)
        r = plan.selected.assessment.resources
        results.append(BenchmarkResult(
            workload=workload.name,
            backend=plan.selected.assessment.backend,
            evidence_level="MODEL_ONLY",
            uqpu_cost_per_task=uqpu_cost,
            gpu_cost_per_task=gpu_cost,
            cost_advantage=advantage,
            cost_tier=cost_tier(advantage),
            total_seconds=r.total_seconds,
            logical_qubits=r.logical_qubits,
            physical_qubits=r.physical_qubits,
            shots=r.shots,
            confidence=r.confidence,
            classification=classify(advantage),
        ))
    return results

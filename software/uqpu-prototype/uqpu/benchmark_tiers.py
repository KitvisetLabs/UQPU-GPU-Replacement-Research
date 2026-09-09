from __future__ import annotations
from dataclasses import dataclass
from .benchmark_contract import OptimizationBenchmarkContract
from .scalable_qubo import seeded_erdos_renyi_maxcut

@dataclass(frozen=True)
class BenchmarkTier:
    name: str
    variable_count: int
    edge_probability: float
    seed: int
    required_relative_gap: float
    purpose: str

    def contract(self) -> OptimizationBenchmarkContract:
        return OptimizationBenchmarkContract(
            workload_id=f"maxcut-er-{self.name}",
            instance_family=f"erdos-renyi-p{self.edge_probability:g}",
            instance_seed=self.seed,
            variable_count=self.variable_count,
            required_relative_gap=self.required_relative_gap,
        )

    def instance(self):
        return seeded_erdos_renyi_maxcut(self.variable_count,self.edge_probability,self.seed)

def representative_tiers() -> tuple[BenchmarkTier,...]:
    return (
        BenchmarkTier("small",32,0.15,101,0.00,"correctness and adapter smoke"),
        BenchmarkTier("medium",128,0.08,202,0.02,"optimized CPU scaling and simulator mapping"),
        BenchmarkTier("large",512,0.03,303,0.05,"competitive multicore/GPU and hybrid-QPU economics"),
    )

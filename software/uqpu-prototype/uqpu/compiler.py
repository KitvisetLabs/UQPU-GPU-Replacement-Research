from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .backends import Backend, BackendAssessment, QuantumNativeBackend, ReversibleBackend
from .cost import CostBreakdown, CostModel
from .ir import Workload, ResultContract


@dataclass
class CompilationCandidate:
    assessment: BackendAssessment
    cost: CostBreakdown


@dataclass
class CompilationPlan:
    workload: str
    selected: CompilationCandidate
    candidates: List[CompilationCandidate]
    reason: str


class SemanticCompiler:
    def __init__(self, backends: Iterable[Backend] | None = None, cost_model: CostModel | None = None):
        self.backends = list(backends or [QuantumNativeBackend(), ReversibleBackend()])
        self.cost_model = cost_model or CostModel()

    def compile(self, workload: Workload) -> CompilationPlan:
        workload.validate()
        candidates: List[CompilationCandidate] = []
        for backend in self.backends:
            assessment = backend.assess(workload)
            if not assessment.supported:
                continue
            if workload.contract == ResultContract.EXACT and assessment.expected_quality < 1.0:
                continue
            cost = self.cost_model.estimate(
                assessment.resources,
                io_bytes=workload.input_bytes + workload.output_bytes,
            )
            candidates.append(CompilationCandidate(assessment=assessment, cost=cost))

        if not candidates:
            raise RuntimeError("no backend can satisfy the workload contract")

        candidates.sort(key=lambda c: (c.cost.total, c.assessment.resources.total_seconds))
        selected = candidates[0]
        reason = (
            f"Selected {selected.assessment.backend} because it has the lowest estimated "
            f"end-to-end cost among contract-compatible candidates."
        )
        return CompilationPlan(workload=workload.name, selected=selected, candidates=candidates, reason=reason)

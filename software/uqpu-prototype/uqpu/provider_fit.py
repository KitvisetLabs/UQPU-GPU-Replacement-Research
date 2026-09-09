from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

from .cloud import QuantumParadigm
from .workload_contracts import WorkloadContract


@dataclass(frozen=True)
class ProviderFit:
    provider_id: str
    paradigm: QuantumParadigm
    workload_id: str
    fit_score: float
    reasons: tuple[str, ...]
    evidence_level: str = "MODEL_ONLY"

    def validate(self) -> None:
        if not (0 <= self.fit_score <= 1):
            raise ValueError("fit_score must be in [0,1]")
        if not self.provider_id or not self.workload_id:
            raise ValueError("provider/workload required")


def infer_candidate_paradigms(contract: WorkloadContract) -> tuple[QuantumParadigm, ...]:
    wid=contract.workload_id
    if wid=="combinatorial_optimization":
        return (QuantumParadigm.ANNEALING, QuantumParadigm.GATE_MODEL, QuantumParadigm.ANALOG)
    if wid=="monte_carlo_like_estimation":
        return (QuantumParadigm.GATE_MODEL,)
    if wid=="linear_algebra_subroutine":
        return (QuantumParadigm.GATE_MODEL, QuantumParadigm.PHOTONIC)
    if wid=="stateful_checkpoint_workflow":
        return (QuantumParadigm.GATE_MODEL, QuantumParadigm.PHOTONIC, QuantumParadigm.HYBRID)
    return (QuantumParadigm.GATE_MODEL,)


def rank_provider_fits(
    contract: WorkloadContract,
    provider_paradigms: dict[str, QuantumParadigm],
) -> list[ProviderFit]:
    candidates=set(infer_candidate_paradigms(contract))
    out=[]
    for pid,paradigm in provider_paradigms.items():
        match=paradigm in candidates
        score=1.0 if match else 0.15
        reasons=("paradigm_match",) if match else ("paradigm_mismatch_or_unproven",)
        out.append(ProviderFit(pid,paradigm,contract.workload_id,score,reasons))
    return sorted(out,key=lambda x:x.fit_score,reverse=True)

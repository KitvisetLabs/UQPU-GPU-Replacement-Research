from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QECBudgetResult:
    target_advantage: float
    qec_budget_per_task: float
    max_qec_runtime_seconds: float
    max_physical_qubits: int
    max_non_clifford_operations: int


def derive_qec_budget(
    target_advantage: float,
    qec_budget_per_task: float,
    *,
    qec_cost_per_second: float,
    physical_qubit_cost_per_task: float,
    non_clifford_cost_per_op: float,
) -> QECBudgetResult:
    if target_advantage <= 0:
        raise ValueError("target_advantage must be positive")
    if qec_budget_per_task < 0:
        raise ValueError("qec_budget_per_task must be non-negative")
    if qec_cost_per_second <= 0:
        raise ValueError("qec_cost_per_second must be positive")
    if physical_qubit_cost_per_task <= 0:
        raise ValueError("physical_qubit_cost_per_task must be positive")
    if non_clifford_cost_per_op <= 0:
        raise ValueError("non_clifford_cost_per_op must be positive")

    third = qec_budget_per_task / 3.0
    return QECBudgetResult(
        target_advantage=target_advantage,
        qec_budget_per_task=qec_budget_per_task,
        max_qec_runtime_seconds=third / qec_cost_per_second,
        max_physical_qubits=max(0, int(third / physical_qubit_cost_per_task)),
        max_non_clifford_operations=max(0, int(third / non_clifford_cost_per_op)),
    )

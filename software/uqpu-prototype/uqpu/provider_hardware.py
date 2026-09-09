from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class HardwareSnapshot:
    provider_id: str
    system_name: str
    paradigm: str
    physical_qubits: Optional[int] = None
    logical_qubits: Optional[int] = None
    two_qubit_fidelity: Optional[float] = None
    single_qubit_fidelity: Optional[float] = None
    max_operations_claimed: Optional[int] = None
    cloud_accessible: bool = True
    evidence_date: str = ""
    evidence_level: str = "PUBLISHED_EXPERIMENT"
    source_url: str = ""
    notes: str = ""


@dataclass(frozen=True)
class RequirementVector:
    paradigm: str
    min_physical_qubits: Optional[int] = None
    min_logical_qubits: Optional[int] = None
    min_two_qubit_fidelity: Optional[float] = None
    min_single_qubit_fidelity: Optional[float] = None
    min_operations: Optional[int] = None
    require_cloud_access: bool = True


@dataclass(frozen=True)
class HardwareGap:
    provider_id: str
    system_name: str
    paradigm_match: bool
    cloud_match: bool
    physical_qubit_gap: Optional[int]
    logical_qubit_gap: Optional[int]
    two_qubit_fidelity_gap: Optional[float]
    single_qubit_fidelity_gap: Optional[float]
    operations_gap: Optional[int]
    unknown_fields: tuple[str, ...]
    meets_known_requirements: bool


def _gap_min(required, actual):
    if required is None:
        return None
    if actual is None:
        return None
    return max(0, required - actual)


def compare_snapshot(snapshot: HardwareSnapshot, req: RequirementVector) -> HardwareGap:
    unknown = []
    checks = []

    paradigm_match = snapshot.paradigm == req.paradigm
    checks.append(paradigm_match)
    cloud_match = (not req.require_cloud_access) or snapshot.cloud_accessible
    checks.append(cloud_match)

    pairs = [
        ("physical_qubits", req.min_physical_qubits, snapshot.physical_qubits),
        ("logical_qubits", req.min_logical_qubits, snapshot.logical_qubits),
        ("two_qubit_fidelity", req.min_two_qubit_fidelity, snapshot.two_qubit_fidelity),
        ("single_qubit_fidelity", req.min_single_qubit_fidelity, snapshot.single_qubit_fidelity),
        ("max_operations", req.min_operations, snapshot.max_operations_claimed),
    ]
    for name, required, actual in pairs:
        if required is None:
            continue
        if actual is None:
            unknown.append(name)
            continue
        checks.append(actual >= required)

    return HardwareGap(
        provider_id=snapshot.provider_id,
        system_name=snapshot.system_name,
        paradigm_match=paradigm_match,
        cloud_match=cloud_match,
        physical_qubit_gap=_gap_min(req.min_physical_qubits, snapshot.physical_qubits),
        logical_qubit_gap=_gap_min(req.min_logical_qubits, snapshot.logical_qubits),
        two_qubit_fidelity_gap=_gap_min(req.min_two_qubit_fidelity, snapshot.two_qubit_fidelity),
        single_qubit_fidelity_gap=_gap_min(req.min_single_qubit_fidelity, snapshot.single_qubit_fidelity),
        operations_gap=_gap_min(req.min_operations, snapshot.max_operations_claimed),
        unknown_fields=tuple(unknown),
        meets_known_requirements=all(checks) and not unknown,
    )


def rank_known_gaps(snapshots: Iterable[HardwareSnapshot], req: RequirementVector) -> list[HardwareGap]:
    gaps = [compare_snapshot(s, req) for s in snapshots]
    return sorted(
        gaps,
        key=lambda g: (
            not g.paradigm_match,
            not g.cloud_match,
            len(g.unknown_fields),
            (g.logical_qubit_gap or 0),
            (g.physical_qubit_gap or 0),
            (g.operations_gap or 0),
        ),
    )

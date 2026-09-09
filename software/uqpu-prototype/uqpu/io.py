from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .ir import Operation, OperationKind, ResultContract, Workload, WorkloadDomain


def workload_from_dict(data: dict[str, Any]) -> Workload:
    return Workload(
        name=data["name"],
        domain=WorkloadDomain(data["domain"]),
        operations=[Operation(OperationKind(op["kind"]), op.get("params", {})) for op in data["operations"]],
        contract=ResultContract(data["contract"]),
        input_bytes=int(data.get("input_bytes", 0)),
        output_bytes=int(data.get("output_bytes", 0)),
        metadata=dict(data.get("metadata", {})),
    )


def load_workload(path: str | Path) -> Workload:
    with Path(path).open("r", encoding="utf-8") as f:
        workload = workload_from_dict(json.load(f))
    workload.validate()
    return workload

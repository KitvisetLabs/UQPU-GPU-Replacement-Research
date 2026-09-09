from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class ResultContract(str, Enum):
    EXACT = "exact"
    BOUNDED_ERROR = "bounded_error"
    APPROXIMATE = "approximate"
    SAMPLED = "sampled"
    PROBABILISTIC = "probabilistic"


class WorkloadDomain(str, Enum):
    AI = "ai"
    GRAPHICS = "graphics"
    HPC = "hpc"
    DATA = "data"
    MEDIA = "media"
    SIGNAL = "signal"
    GENERAL = "general"


class OperationKind(str, Enum):
    LINEAR_SOLVE = "linear_solve"
    EXPECTATION = "expectation"
    OPTIMIZE = "optimize"
    SAMPLE = "sample"
    SEARCH = "search"
    EIGEN = "eigen"
    TRANSFORM = "transform"
    CLASSIFY = "classify"
    TRAIN = "train"
    RENDER = "render"
    TRACE = "trace"
    ENCODE = "encode"
    DECODE = "decode"
    GENERAL_KERNEL = "general_kernel"


@dataclass(frozen=True)
class Operation:
    kind: OperationKind
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Workload:
    name: str
    domain: WorkloadDomain
    operations: List[Operation]
    contract: ResultContract
    input_bytes: int = 0
    output_bytes: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("workload name must be non-empty")
        if not self.operations:
            raise ValueError("workload must contain at least one operation")
        if self.input_bytes < 0 or self.output_bytes < 0:
            raise ValueError("input/output byte counts must be non-negative")

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from ..ir import Workload
from ..resources import ResourceEstimate


@dataclass
class BackendAssessment:
    backend: str
    supported: bool
    rationale: List[str]
    resources: ResourceEstimate
    expected_quality: float = 1.0
    mode: str = "unknown"


class Backend(ABC):
    name: str

    @abstractmethod
    def assess(self, workload: Workload) -> BackendAssessment:
        raise NotImplementedError

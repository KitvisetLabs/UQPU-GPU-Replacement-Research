from __future__ import annotations

from dataclasses import dataclass

from .hardware import QuantumHardwareProfile


@dataclass(frozen=True)
class SurfaceCodeEstimate:
    code_distance: int
    physical_qubits_per_logical: int
    total_physical_qubits: int
    logical_error_per_cycle: float
    qec_runtime_seconds: float


class SurfaceCodeEstimator:
    """Transparent phenomenological surface-code MODEL_ONLY estimator.

    This model is intentionally simple and must not be treated as a
    provider-specific fault-tolerant resource estimate.
    """

    def __init__(self, profile: QuantumHardwareProfile, prefactor: float = 0.1):
        profile.validate()
        if prefactor <= 0:
            raise ValueError("prefactor must be positive")
        self.profile = profile
        self.prefactor = prefactor

    def logical_error(self, distance: int) -> float:
        if distance < 3 or distance % 2 == 0:
            raise ValueError("surface-code distance must be odd and >= 3")
        ratio = self.profile.physical_error_rate / self.profile.qec_threshold
        return self.prefactor * (ratio ** ((distance + 1) / 2))

    def choose_distance(self, target_logical_error_per_cycle: float) -> int:
        if not (0 < target_logical_error_per_cycle < 1):
            raise ValueError("target logical error must be in (0,1)")
        for distance in range(3, 1001, 2):
            if self.logical_error(distance) <= target_logical_error_per_cycle:
                return distance
        raise RuntimeError("required code distance exceeds model search bound")

    def estimate(
        self,
        logical_qubits: int,
        logical_depth: int,
        target_failure_probability: float = 1e-6,
    ) -> SurfaceCodeEstimate:
        if logical_qubits <= 0 or logical_depth <= 0:
            raise ValueError("logical_qubits and logical_depth must be positive")
        if not (0 < target_failure_probability < 1):
            raise ValueError("target_failure_probability must be in (0,1)")

        opportunities = max(1, logical_qubits * logical_depth)
        target_per_cycle = target_failure_probability / opportunities
        distance = self.choose_distance(target_per_cycle)
        physical_per_logical = 2 * distance * distance
        total_physical = logical_qubits * physical_per_logical
        logical_error = self.logical_error(distance)
        qec_runtime = logical_depth * self.profile.logical_cycle_seconds

        return SurfaceCodeEstimate(
            code_distance=distance,
            physical_qubits_per_logical=physical_per_logical,
            total_physical_qubits=total_physical,
            logical_error_per_cycle=logical_error,
            qec_runtime_seconds=qec_runtime,
        )

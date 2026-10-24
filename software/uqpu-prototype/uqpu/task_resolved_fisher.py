"""Evidence-gated task-resolved Fisher-information and measurement-budget ledger.

This module validates comparable information matrices and resource metadata. It
does not reproduce a paper, establish a quantum advantage, or infer physical
truth from Fisher information. Unknown energy/cost stays unknown, never zero.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import re

Matrix = tuple[tuple[float, ...], ...]

_ALLOWED_EVIDENCE = {
    "LITERATURE_ONLY",
    "CONCEPT",
    "THEORY",
    "MODEL_ONLY",
    "SIMULATION",
    "LAB_RESULT",
    "PUBLISHED_EXPERIMENT",
    "REAL_QPU",
    "PRODUCTION_DATA",
}
_ALLOWED_MATRIX_SEMANTICS = {"ANALYTIC", "ESTIMATED"}
_ALLOWED_RESOURCE_SCOPES = {"END_TO_END_RUN", "DEVICE_ONLY", "HOST_ONLY", "UNKNOWN"}
_ALLOWED_QUALITY_DIRECTIONS = {"LOWER_IS_BETTER", "HIGHER_IS_BETTER"}
_TOL = 1e-9


def _finite(name: str, value: float) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _nonnegative(name: str, value: float | None) -> None:
    if value is not None and _finite(name, value) < 0.0:
        raise ValueError(f"{name} must be non-negative when supplied")


def _subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def _matrix_is_psd(matrix: Matrix, tolerance: float = _TOL) -> bool:
    """Check positive-semidefiniteness with a tolerance-aware LDLᵀ factorization."""
    n = len(matrix)
    scale = max([1.0] + [abs(float(v)) for row in matrix for v in row])
    eps = tolerance * scale
    lower = [[0.0] * n for _ in range(n)]
    diagonal = [0.0] * n

    for j in range(n):
        pivot = matrix[j][j] - sum(
            lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)
        )
        if pivot < -eps:
            return False
        if pivot <= eps:
            diagonal[j] = 0.0
            for i in range(j + 1, n):
                residual = matrix[i][j] - sum(
                    lower[i][k] * lower[j][k] * diagonal[k]
                    for k in range(j)
                )
                if abs(residual) > eps:
                    return False
                lower[i][j] = 0.0
            continue

        diagonal[j] = pivot
        for i in range(j + 1, n):
            residual = matrix[i][j] - sum(
                lower[i][k] * lower[j][k] * diagonal[k]
                for k in range(j)
            )
            lower[i][j] = residual / pivot
    return True


def _validate_matrix(name: str, matrix: Matrix, expected_dimension: int | None = None) -> int:
    if not matrix:
        raise ValueError(f"{name} must be a non-empty square matrix")
    n = len(matrix)
    if expected_dimension is not None and n != expected_dimension:
        raise ValueError(f"{name} dimension does not match the task-score basis")
    if any(len(row) != n for row in matrix):
        raise ValueError(f"{name} must be square")
    for row in matrix:
        for value in row:
            _finite(name, value)
    scale = max([1.0] + [abs(float(v)) for row in matrix for v in row])
    for i in range(n):
        for j in range(i + 1, n):
            if abs(matrix[i][j] - matrix[j][i]) > _TOL * scale:
                raise ValueError(f"{name} must be symmetric")
    if not _matrix_is_psd(matrix):
        raise ValueError(f"{name} must be positive semidefinite")
    return n


def _trace(matrix: Matrix) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))


@dataclass(frozen=True)
class FeatureInformation:
    """Fisher-information matrix retained by a specific feature-order cutoff."""

    order: int
    information_matrix: Matrix
    bytes_per_history: int


@dataclass(frozen=True)
class TaskResolvedFisherRecord:
    """One workload/score-basis/measurement context; never mix target prices."""

    workload_id: str
    model_id: str
    task_score_basis_id: str
    split_sha256: str
    provenance: str
    evidence_level: str
    matrix_semantics: str
    qfi_matrix: Matrix
    complete_record_fi_matrix: Matrix
    retained_features: tuple[FeatureInformation, ...]
    shots_per_history: int
    history_count: int
    measurement_setting_count: int
    raw_record_bytes_per_history: int
    evaluated_task_count: int
    accepted_task_count: int
    quality_metric: str
    quality_value: float
    quality_threshold: float
    quality_direction: str
    cost_scope: str = "UNKNOWN"
    total_run_cost_usd: float | None = None
    energy_scope: str = "UNKNOWN"
    total_run_energy_joules: float | None = None
    wall_clock_seconds: float | None = None
    host_compute_seconds: float | None = None
    provider_id: str | None = None
    target_id: str | None = None

    def validate(self) -> None:
        for name in (
            "workload_id",
            "model_id",
            "task_score_basis_id",
            "provenance",
            "quality_metric",
        ):
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} is required")
        if not re.fullmatch(r"[0-9a-fA-F]{64}", self.split_sha256):
            raise ValueError("split_sha256 must be a 64-character SHA-256 hex digest")
        if self.evidence_level not in _ALLOWED_EVIDENCE:
            raise ValueError(f"unknown evidence level: {self.evidence_level}")
        if self.matrix_semantics not in _ALLOWED_MATRIX_SEMANTICS:
            raise ValueError("matrix_semantics must be ANALYTIC or ESTIMATED")
        if self.quality_direction not in _ALLOWED_QUALITY_DIRECTIONS:
            raise ValueError("unknown quality_direction")
        if self.cost_scope not in _ALLOWED_RESOURCE_SCOPES:
            raise ValueError("unknown cost_scope")
        if self.energy_scope not in _ALLOWED_RESOURCE_SCOPES:
            raise ValueError("unknown energy_scope")

        dimension = _validate_matrix("qfi_matrix", self.qfi_matrix)
        _validate_matrix(
            "complete_record_fi_matrix", self.complete_record_fi_matrix, dimension
        )
        if not self.retained_features:
            raise ValueError("at least one retained feature-order matrix is required")

        previous_order = 0
        for feature in self.retained_features:
            if feature.order <= previous_order:
                raise ValueError("feature orders must be positive and strictly increasing")
            if feature.bytes_per_history <= 0:
                raise ValueError("feature bytes_per_history must be positive")
            _validate_matrix(
                f"retained feature matrix at order {feature.order}",
                feature.information_matrix,
                dimension,
            )
            previous_order = feature.order

        positive_counts = (
            "shots_per_history",
            "history_count",
            "measurement_setting_count",
            "raw_record_bytes_per_history",
            "evaluated_task_count",
        )
        for name in positive_counts:
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if (
            not isinstance(self.accepted_task_count, int)
            or isinstance(self.accepted_task_count, bool)
            or self.accepted_task_count < 0
            or self.accepted_task_count > self.evaluated_task_count
        ):
            raise ValueError("accepted_task_count must be between zero and evaluated_task_count")

        _finite("quality_value", self.quality_value)
        _finite("quality_threshold", self.quality_threshold)
        _nonnegative("total_run_cost_usd", self.total_run_cost_usd)
        _nonnegative("total_run_energy_joules", self.total_run_energy_joules)
        _nonnegative("wall_clock_seconds", self.wall_clock_seconds)
        _nonnegative("host_compute_seconds", self.host_compute_seconds)

        if bool(self.provider_id) != bool(self.target_id):
            raise ValueError("provider_id and target_id must be supplied together")
        if self.evidence_level == "REAL_QPU" and not (self.provider_id and self.target_id):
            raise ValueError("REAL_QPU evidence requires the exact provider and target")

        if self.matrix_semantics == "ANALYTIC":
            violations = self.information_hierarchy_violations()
            if violations:
                raise ValueError("analytic information hierarchy failed: " + "; ".join(violations))

    def information_hierarchy_violations(self) -> tuple[str, ...]:
        """Return matrix-order violations; estimated values may fluctuate with finite data."""
        violations: list[str] = []
        if not _matrix_is_psd(_subtract(self.qfi_matrix, self.complete_record_fi_matrix)):
            violations.append("QFI does not dominate complete-record Fisher information")
        previous = self.complete_record_fi_matrix
        previous_label = "complete measurement record"
        for feature in self.retained_features:
            if not _matrix_is_psd(_subtract(feature.information_matrix, previous)):
                violations.append(
                    f"feature order {feature.order} does not dominate {previous_label}"
                )
            previous = feature.information_matrix
            previous_label = f"feature order {feature.order}"
        return tuple(violations)

    @property
    def diagnostics(self) -> tuple[str, ...]:
        self.validate()
        if self.matrix_semantics == "ANALYTIC":
            return ()
        return tuple(
            "ESTIMATED-MATRIX WARNING: " + item
            + "; inspect uncertainty, score-basis identity and sampling before interpretation"
            for item in self.information_hierarchy_violations()
        )

    @property
    def quality_pass(self) -> bool:
        self.validate()
        if self.quality_direction == "LOWER_IS_BETTER":
            return self.quality_value <= self.quality_threshold
        return self.quality_value >= self.quality_threshold

    def information_retention_ratio(self, order: int) -> float | None:
        """Trace ratio only within this exact orthonormal task-score basis."""
        self.validate()
        feature = next((item for item in self.retained_features if item.order == order), None)
        if feature is None:
            raise ValueError(f"unknown feature order: {order}")
        denominator = _trace(self.complete_record_fi_matrix)
        if denominator <= 0.0:
            return None
        return _trace(feature.information_matrix) / denominator

    def record_byte_reduction_ratio(self, order: int) -> float:
        """Raw-record bytes / retained-feature bytes; not quantum-state capacity."""
        self.validate()
        feature = next((item for item in self.retained_features if item.order == order), None)
        if feature is None:
            raise ValueError(f"unknown feature order: {order}")
        return self.raw_record_bytes_per_history / feature.bytes_per_history

    @property
    def end_to_end_cost_per_accepted_task_usd(self) -> float | None:
        self.validate()
        if (
            self.total_run_cost_usd is None
            or self.cost_scope != "END_TO_END_RUN"
            or self.accepted_task_count == 0
        ):
            return None
        return self.total_run_cost_usd / self.accepted_task_count

    @property
    def end_to_end_energy_per_accepted_task_joules(self) -> float | None:
        self.validate()
        if (
            self.total_run_energy_joules is None
            or self.energy_scope != "END_TO_END_RUN"
            or self.accepted_task_count == 0
        ):
            return None
        return self.total_run_energy_joules / self.accepted_task_count

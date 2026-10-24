"""Small deterministic local-identifiability audit for equation discovery.

This is a MODEL_ONLY governance helper. It analyzes normalized sensitivity
matrices at one candidate parameter point; it does not prove global
identifiability, physical truth, or experimental-class completeness.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

_IDENTIFIABILITY_VERDICTS = {
    "NOT_YET_SOLVED",
    "IDENTIFIABLE",
    "LOCALLY_NON_IDENTIFIABLE",
    "EXPERIMENT_CLASS_EXHAUSTED",
}


@dataclass(frozen=True)
class SensitivityDesign:
    """One declared design and its dimensionless, scale-normalized Jacobian.

    The matrix must be normalized using documented observation and parameter
    scales before it reaches this helper. Rank is scale-sensitive; raw
    dimensional derivatives are not an acceptable input.
    """

    design_id: str
    dimensionless_sensitivity_matrix: tuple[tuple[float, ...], ...]
    normalization_provenance: tuple[str, ...]


@dataclass(frozen=True)
class IdentifiabilityReport:
    verdict: str
    rank: int
    parameter_count: int
    nullspace_basis: tuple[tuple[float, ...], ...]
    design_ranks: tuple[tuple[str, int], ...]
    solver_converged: bool
    experiment_class_complete: bool
    tolerance: float


def _validated_matrix(
    matrix: Sequence[Sequence[float]], tolerance: float
) -> tuple[tuple[float, ...], ...]:
    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)):
        raise ValueError("tolerance must be a finite number in (0, 1)")
    tolerance = float(tolerance)
    if not math.isfinite(tolerance) or not 0.0 < tolerance < 1.0:
        raise ValueError("tolerance must be a finite number in (0, 1)")
    try:
        rows = tuple(tuple(row) for row in matrix)
    except TypeError as exc:
        raise ValueError("sensitivity matrix must be a rectangular numeric sequence") from exc
    if not rows or not rows[0]:
        raise ValueError("sensitivity matrix must have at least one row and one column")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("sensitivity matrix must be rectangular")
    converted: list[tuple[float, ...]] = []
    for row in rows:
        values: list[float] = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("sensitivity entries must be numeric, not booleans")
            number = float(value)
            if not math.isfinite(number):
                raise ValueError("sensitivity entries must be finite")
            values.append(number)
        converted.append(tuple(values))
    return tuple(converted)


def _rref_rank_and_nullspace(
    matrix: tuple[tuple[float, ...], ...], tolerance: float
) -> tuple[int, tuple[tuple[float, ...], ...]]:
    """Return numerical rank and a basis for the right null space.

    A single global rescaling removes irrelevant overall magnitude. Per-column
    normalization must already have been justified and recorded by the caller.
    """
    scale = max(abs(value) for row in matrix for value in row)
    if scale == 0.0:
        normalized = [[0.0 for _ in row] for row in matrix]
    else:
        normalized = [[value / scale for value in row] for row in matrix]

    row_count = len(normalized)
    column_count = len(normalized[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        if pivot_row >= row_count:
            break
        selected = max(
            range(pivot_row, row_count),
            key=lambda index: abs(normalized[index][column]),
        )
        if abs(normalized[selected][column]) <= tolerance:
            continue
        normalized[pivot_row], normalized[selected] = (
            normalized[selected],
            normalized[pivot_row],
        )
        pivot = normalized[pivot_row][column]
        normalized[pivot_row] = [value / pivot for value in normalized[pivot_row]]
        for index in range(row_count):
            if index == pivot_row:
                continue
            factor = normalized[index][column]
            if abs(factor) <= tolerance:
                normalized[index][column] = 0.0
                continue
            normalized[index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(
                    normalized[index], normalized[pivot_row]
                )
            ]
            normalized[index] = [
                0.0 if abs(value) <= tolerance else value
                for value in normalized[index]
            ]
        pivot_columns.append(column)
        pivot_row += 1

    free_columns = [
        column for column in range(column_count) if column not in pivot_columns
    ]
    basis: list[tuple[float, ...]] = []
    for free_column in free_columns:
        vector = [0.0] * column_count
        vector[free_column] = 1.0
        for index, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -normalized[index][free_column]
        vector = [
            0.0 if abs(value) <= tolerance else value for value in vector
        ]
        basis.append(tuple(vector))
    return len(pivot_columns), tuple(basis)


def assess_local_identifiability(
    primary_design: SensitivityDesign,
    *,
    solver_converged: bool,
    alternative_designs: Sequence[SensitivityDesign] = (),
    experiment_class_complete: bool = False,
    tolerance: float = 1e-10,
) -> IdentifiabilityReport:
    """Classify a candidate using a bounded, local sensitivity-rank audit.

    EXPERIMENT_CLASS_EXHAUSTED is returned only when the caller declares a
    finite design class complete, at least two distinct designs are supplied,
    and every design remains rank deficient. This does not exhaust all
    imaginable experiments or establish global non-identifiability.
    """
    if not isinstance(solver_converged, bool):
        raise ValueError("solver_converged must be boolean")
    if not isinstance(experiment_class_complete, bool):
        raise ValueError("experiment_class_complete must be boolean")

    designs = (primary_design, *tuple(alternative_designs))
    identifiers: list[str] = []
    matrices: list[tuple[tuple[float, ...], ...]] = []
    for design in designs:
        if not isinstance(design, SensitivityDesign):
            raise ValueError("each design must be a SensitivityDesign")
        if not isinstance(design.design_id, str) or not design.design_id.strip():
            raise ValueError("design_id is required")
        if design.design_id in identifiers:
            raise ValueError("design_id values must be unique")
        if not design.normalization_provenance or any(
            not isinstance(item, str) or not item.strip()
            for item in design.normalization_provenance
        ):
            raise ValueError("normalization_provenance must document the scaling")
        matrix = _validated_matrix(
            design.dimensionless_sensitivity_matrix, tolerance
        )
        identifiers.append(design.design_id)
        matrices.append(matrix)

    parameter_count = len(matrices[0][0])
    if any(len(matrix[0]) != parameter_count for matrix in matrices):
        raise ValueError("all declared designs must use the same parameter basis")

    ranks_and_bases = [
        _rref_rank_and_nullspace(matrix, float(tolerance))
        for matrix in matrices
    ]
    primary_rank, primary_nullspace = ranks_and_bases[0]
    design_ranks = tuple(
        (design.design_id, ranks_and_bases[index][0])
        for index, design in enumerate(designs)
    )

    if not solver_converged:
        verdict = "NOT_YET_SOLVED"
    elif primary_rank == parameter_count:
        verdict = "IDENTIFIABLE"
    elif (
        experiment_class_complete
        and len(designs) >= 2
        and all(rank < parameter_count for rank, _ in ranks_and_bases)
    ):
        verdict = "EXPERIMENT_CLASS_EXHAUSTED"
    else:
        verdict = "LOCALLY_NON_IDENTIFIABLE"

    assert verdict in _IDENTIFIABILITY_VERDICTS
    return IdentifiabilityReport(
        verdict=verdict,
        rank=primary_rank,
        parameter_count=parameter_count,
        nullspace_basis=primary_nullspace,
        design_ranks=design_ranks,
        solver_converged=solver_converged,
        experiment_class_complete=experiment_class_complete,
        tolerance=float(tolerance),
    )

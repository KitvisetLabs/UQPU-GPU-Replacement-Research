from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from time import perf_counter

from .optimization_baseline import QuboInstance


@dataclass(frozen=True)
class OptimizedSolverResult:
    assignment: dict[int, int]
    objective: float
    runtime_seconds: float
    solver_name: str
    solver_status: str
    proven_optimal: bool


def ortools_available() -> bool:
    return importlib.util.find_spec("ortools") is not None


def solve_qubo_ortools(
    instance: QuboInstance,
    *,
    time_limit_seconds: float = 30.0,
    workers: int = 1,
) -> OptimizedSolverResult:
    if time_limit_seconds <= 0:
        raise ValueError("time_limit_seconds must be positive")
    if workers <= 0:
        raise ValueError("workers must be positive")
    if not ortools_available():
        raise RuntimeError("OR-Tools is not installed; install optional benchmark dependency 'ortools'")

    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    variables = {i: model.NewBoolVar(f"x_{i}") for i in instance.variables}

    # CP-SAT requires integer objective coefficients. For benchmark QUBOs we
    # support coefficients that are exactly integral after rounding.
    def as_int(value: float) -> int:
        rounded = int(round(value))
        if abs(value - rounded) > 1e-9:
            raise ValueError("OR-Tools QUBO adapter currently requires integer coefficients")
        return rounded

    terms = []
    for i, weight in instance.linear.items():
        terms.append(as_int(weight) * variables[i])

    for (i, j), weight in instance.quadratic.items():
        y = model.NewBoolVar(f"y_{i}_{j}")
        model.Add(y <= variables[i])
        model.Add(y <= variables[j])
        model.Add(y >= variables[i] + variables[j] - 1)
        terms.append(as_int(weight) * y)

    constant = as_int(instance.constant)
    model.Minimize(sum(terms) + constant)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit_seconds
    solver.parameters.num_search_workers = workers

    t0 = perf_counter()
    status = solver.Solve(model)
    runtime = perf_counter() - t0

    valid = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    if not valid:
        raise RuntimeError(f"OR-Tools failed to produce a feasible QUBO solution; status={solver.StatusName(status)}")

    assignment = {i: int(solver.Value(v)) for i, v in variables.items()}
    objective = instance.energy(assignment)
    return OptimizedSolverResult(
        assignment=assignment,
        objective=objective,
        runtime_seconds=runtime,
        solver_name="ortools-cp-sat",
        solver_status=solver.StatusName(status),
        proven_optimal=status == cp_model.OPTIMAL,
    )

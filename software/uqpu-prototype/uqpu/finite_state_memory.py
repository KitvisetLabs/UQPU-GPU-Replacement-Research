"""Exact finite-state evaluator for FND-001 active-memory work-rate models.

Evaluates W = H(A_t | M_t) - H(S_t | M_t) on the unique stationary joint
(M,S) chain. Analytic MODEL_ONLY; not a joule, device/software-energy, task-quality,
or economics estimator.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
import json, math
from collections.abc import Sequence
from typing import Any

_TOL = 1e-12
_RESIDUAL_TOL = 1e-9

def _distribution(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence) or not values:
        raise ValueError(f"{name} must be a nonempty probability sequence")
    out = []
    for value in values:
        if isinstance(value, bool):
            raise ValueError(f"{name} entries must be finite probabilities")
        try:
            p = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} entries must be finite probabilities") from exc
        if not math.isfinite(p) or p < 0.0 or p > 1.0:
            raise ValueError(f"{name} entries must be finite probabilities in [0, 1]")
        out.append(p)
    if not math.isclose(math.fsum(out), 1.0, rel_tol=0.0, abs_tol=_TOL):
        raise ValueError(f"{name} must sum to one within {_TOL:g}")
    return tuple(out)

def entropy_bits(probabilities: Sequence[float]) -> float:
    p = _distribution("probabilities", probabilities)
    return -math.fsum(x * math.log2(x) for x in p if x > 0.0)

def _stochastic_matrix(name: str, matrix: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if isinstance(matrix, (str, bytes)) or not isinstance(matrix, Sequence) or not matrix:
        raise ValueError(f"{name} must be a nonempty matrix")
    rows = tuple(_distribution(f"{name} row {i}", row) for i, row in enumerate(matrix))
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError(f"{name} must have nonempty equal-width rows")
    return rows

def stationary_distribution(transition: Sequence[Sequence[float]]) -> tuple[float, ...]:
    """Solve pi P=pi with normalization; reject non-unique stationary laws."""
    p = _stochastic_matrix("transition", transition)
    n = len(p)
    if any(len(row) != n for row in p):
        raise ValueError("transition must be square")
    a = [[p[j][i] - (1.0 if i == j else 0.0) for j in range(n)] for i in range(n)]
    b = [0.0] * n
    a[-1] = [1.0] * n
    b[-1] = 1.0
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) <= _TOL:
            raise ValueError("stationary distribution is not uniquely determined by this transition matrix")
        a[col], a[pivot] = a[pivot], a[col]
        b[col], b[pivot] = b[pivot], b[col]
        scale = a[col][col]
        a[col] = [v / scale for v in a[col]]
        b[col] /= scale
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor:
                a[row] = [a[row][k] - factor * a[col][k] for k in range(n)]
                b[row] -= factor * b[col]
    if any(not math.isfinite(x) or x < -_RESIDUAL_TOL for x in b):
        raise ValueError("stationary solution is not a valid probability distribution")
    cleaned = tuple(max(0.0, x) for x in b)
    total = math.fsum(cleaned)
    if total <= 0.0:
        raise ValueError("stationary solution has zero mass")
    result = tuple(x / total for x in cleaned)
    residual = max(abs(math.fsum(result[i] * p[i][j] for i in range(n)) - result[j]) for j in range(n))
    if residual > _RESIDUAL_TOL:
        raise ValueError(f"stationary residual {residual:g} exceeds tolerance")
    return result

@dataclass(frozen=True)
class FiniteStateWorkRate:
    state_order: tuple[tuple[int, int], ...]
    joint_transition: tuple[tuple[float, ...], ...]
    stationary_joint: tuple[float, ...]
    memory_probabilities: tuple[float, ...]
    percept_probabilities: tuple[float, ...]
    action_probabilities_given_memory: tuple[tuple[float, ...], ...]
    percept_probabilities_given_memory: tuple[tuple[float, ...], ...]
    h_action_given_memory_bits: float
    h_percept_given_memory_bits: float
    work_rate_kbt_ln2_per_round: float
    stationary_residual: float

def evaluate_finite_state_channel(policy, memory_update, environment_transition) -> FiniteStateWorkRate:
    """Evaluate W=H(A|M)-H(S|M) for policy[m][s][a], update[m][s][a][m'], env[s][a][s']."""
    if isinstance(policy, (str, bytes)) or not isinstance(policy, Sequence) or not policy:
        raise ValueError("policy must have at least one memory state")
    n_m = len(policy)
    n_s = len(policy[0])
    if n_s == 0 or any(len(row) != n_s for row in policy):
        raise ValueError("policy must have equal nonzero percept count for each memory state")
    pi = tuple(tuple(_distribution(f"policy[{m}][{s}]", row) for s, row in enumerate(mem)) for m, mem in enumerate(policy))
    n_a = len(pi[0][0])
    if n_a == 0 or any(len(row) != n_a for mem in pi for row in mem):
        raise ValueError("policy action-alphabet sizes must match")
    if isinstance(environment_transition, (str, bytes)) or not isinstance(environment_transition, Sequence) or len(environment_transition) != n_s:
        raise ValueError("environment_transition must contain one block per percept")
    env = []
    for s, action_rows in enumerate(environment_transition):
        if len(action_rows) != n_a:
            raise ValueError("environment_transition must contain one row per action")
        rows = tuple(_distribution(f"environment_transition[{s}][{a}]", row) for a, row in enumerate(action_rows))
        if any(len(row) != n_s for row in rows):
            raise ValueError("environment next-percept alphabet size mismatch")
        env.append(rows)
    env = tuple(env)
    if len(memory_update) != n_m:
        raise ValueError("memory_update must contain one block per memory state")
    upd = []
    for m, block in enumerate(memory_update):
        if len(block) != n_s:
            raise ValueError("memory_update must contain one row per percept")
        new_block = []
        for s, actions in enumerate(block):
            if len(actions) != n_a:
                raise ValueError("memory_update must contain one row per action")
            rows = [_distribution(f"memory_update[{m}][{s}][{a}]", row) for a, row in enumerate(actions)]
            if any(len(row) != n_m for row in rows):
                raise ValueError("memory_update next-memory alphabet size mismatch")
            new_block.append(rows)
        upd.append(new_block)
    states = tuple((m, s) for m in range(n_m) for s in range(n_s))
    trans = []
    for m, s in states:
        row = []
        for mn, sn in states:
            row.append(math.fsum(pi[m][s][a] * upd[m][s][a][mn] * env[s][a][sn] for a in range(n_a)))
        if not math.isclose(math.fsum(row), 1.0, rel_tol=0.0, abs_tol=1e-10):
            raise ValueError("constructed joint transition row does not sum to one")
        trans.append(tuple(row))
    trans = tuple(trans)
    stationary = stationary_distribution(trans)
    residual = max(abs(math.fsum(stationary[i] * trans[i][j] for i in range(len(states))) - stationary[j]) for j in range(len(states)))
    p_m = tuple(math.fsum(stationary[i] for i, (mm, _) in enumerate(states) if mm == m) for m in range(n_m))
    p_s = tuple(math.fsum(stationary[i] for i, (_, ss) in enumerate(states) if ss == s) for s in range(n_s))
    action_given, percept_given = [], []
    h_a_m = h_s_m = 0.0
    for m in range(n_m):
        if p_m[m] <= _TOL:
            action_given.append(tuple(0.0 for _ in range(n_a)))
            percept_given.append(tuple(0.0 for _ in range(n_s)))
            continue
        ap = tuple(math.fsum(stationary[i] * pi[m][s][a] for i, (mm, s) in enumerate(states) if mm == m) / p_m[m] for a in range(n_a))
        sp = tuple(math.fsum(stationary[i] for i, (mm, s) in enumerate(states) if mm == m and s == ss) / p_m[m] for ss in range(n_s))
        action_given.append(ap)
        percept_given.append(sp)
        h_a_m += p_m[m] * entropy_bits(ap)
        h_s_m += p_m[m] * entropy_bits(sp)
    return FiniteStateWorkRate(states, trans, stationary, p_m, p_s, tuple(action_given), tuple(percept_given), h_a_m, h_s_m, h_a_m - h_s_m, residual)

def make_environment(p_stay_action0: float):
    """Two-state channel: varied state-0 persistence; state-1 persistence fixed at q=0.7."""
    p = float(p_stay_action0)
    if not math.isfinite(p) or not 0.0 < p < 1.0:
        raise ValueError("p_stay_action0 must be strictly between zero and one")
    q = 0.7
    return (((p, 1-p), (1-p, p)), ((1-q, q), (q, 1-q)))

def policy_fixtures(p_stay_action0: float) -> dict[str, dict[str, Any]]:
    env = make_environment(p_stay_action0)
    one_update = ((((1.0,), (1.0,)), ((1.0,), (1.0,))),)
    p0 = 1.0 / math.sqrt(2.0)
    memoryless = (((p0, 1-p0), (p0, 1-p0)),)
    predictive = (((0.9, 0.1), (0.1, 0.9)), ((0.1, 0.9), (0.9, 0.1)))
    predictive_update = tuple(tuple(tuple((1.0, 0.0) if s == 0 else (0.0, 1.0) for _a in range(2)) for s in range(2)) for _m in range(2))
    bounded = (((0.9, 0.1), (0.9, 0.1)), ((0.1, 0.9), (0.1, 0.9)))
    bounded_update = tuple(tuple(tuple((1.0, 0.0) if a == 0 else (0.0, 1.0) for a in range(2)) for _s in range(2)) for _m in range(2))
    return {
        "MEMORYLESS": {"policy": memoryless, "memory_update": one_update, "environment_transition": env},
        "PREDICTIVE": {"policy": predictive, "memory_update": predictive_update, "environment_transition": env},
        "BOUNDED_MEMORY": {"policy": bounded, "memory_update": bounded_update, "environment_transition": env},
    }

def evaluate_policy_set(p_stay_action0: float) -> dict[str, Any]:
    results = {}
    for name, spec in policy_fixtures(p_stay_action0).items():
        r = evaluate_finite_state_channel(**spec)
        results[name] = {**asdict(r), "work_rate_kbt_ln2_per_round": r.work_rate_kbt_ln2_per_round}
    return {
        "p_stay_action0": p_stay_action0,
        "evidence_class": "MODEL_ONLY_FINITE_STATE_STATIONARY_ANALYSIS",
        "results": results,
        "physical_memory_bytes": None,
        "measured_energy_joules": None,
        "accepted_useful_task_quality": None,
        "measured_cost_usd": None,
        "paid_qpu_jobs": 0,
    }

if __name__ == "__main__":
    print(json.dumps(evaluate_policy_set(0.8), indent=2, sort_keys=True))

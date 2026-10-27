"""Symbolic-only, fail-closed contract for sparse-state-preparation bounds.

The source gives asymptotic statements in a Clifford+T synthesis model. This
module records those statements symbolically; it deliberately does not convert
O-tilde/Omega expressions into numerical gate counts or hardware economics.
Cross-paper comparability with sparse-QROM state-preparation corollaries remains
unresolved until the full theorem assumptions and input representations align.
"""
from __future__ import annotations

import hashlib
import json
import math
from typing import Any

SCHEMA = "uqpu-sparse-stateprep-bound-contract-v1"
WORK_ID = "RG-STATEPREP-SPARSE-001"
SOURCE_URL = "https://arxiv.org/abs/2608.00414"
UPPER_EXPRESSION = (
    "O_tilde(min(s, n^(3/4)*sqrt(s)) + "
    "sqrt(s*log(1/epsilon)) + log(1/epsilon))"
)
LOWER_EXPRESSION = "Omega(min(s, sqrt(n*s)))"


def _positive_int(value: Any, field: str) -> int:
    if type(value) is not int or value < 1:
        raise ValueError(f"{field} must be an integer >= 1")
    return value


def _at_most_power_of_two(value: int, exponent: int) -> bool:
    """Check value <= 2**exponent without constructing a huge power."""
    bits = value.bit_length()
    if bits <= exponent:
        return True
    return bits == exponent + 1 and (value & (value - 1)) == 0


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_sparse_stateprep_bound_contract(
    n_qubits: int, support_size: int, epsilon: float
) -> dict[str, Any]:
    """Return a symbolic theorem-reference contract, never a numeric gate count.

    The paper's stated lower bound applies only for 0 < epsilon <= 1/6 and
    2 <= support_size <= 2**(n_qubits/2). Outside that regime, the lower-bound
    field is null rather than extrapolated.
    """
    n = _positive_int(n_qubits, "n_qubits")
    s = _positive_int(support_size, "support_size")
    if not _at_most_power_of_two(s, n):
        raise ValueError("support_size must not exceed 2**n_qubits")
    if isinstance(epsilon, bool) or not isinstance(epsilon, (int, float)):
        raise ValueError("epsilon must be a finite number in (0, 1/6]")
    eps = float(epsilon)
    if not math.isfinite(eps) or not 0.0 < eps <= (1.0 / 6.0):
        raise ValueError("epsilon must be a finite number in (0, 1/6]")

    lower_applies = s >= 2 and _at_most_power_of_two(s * s, n)
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "work_id": WORK_ID,
        "source": {
            "title": "Sparse Quantum State Preparation with Sublinear T-Count",
            "url": SOURCE_URL,
            "first_posted": "2026-08-01",
            "evidence_class": "OFFICIAL_ARXIV_PREPRINT",
            "full_theorem_model_audit": "PENDING",
        },
        "input_contract": {
            "n_qubits": n,
            "support_size": s,
            "epsilon": eps,
            "target_state_scope": (
                "n-qubit target state supported on at most s computational-basis states"
            ),
            "gate_model": "Clifford+T synthesis as stated in the source",
        },
        "theorem_reference": {
            "upper_bound_expression": UPPER_EXPRESSION,
            "upper_bound_status": "ASYMPTOTIC_O_TILDE_ONLY",
            "lower_bound_expression": LOWER_EXPRESSION if lower_applies else None,
            "lower_bound_status": (
                "APPLICABLE_IN_STATED_RANGE"
                if lower_applies
                else "NOT_APPLICABLE_OUTSIDE_STATED_RANGE"
            ),
            "lower_bound_conditions": (
                "0 < epsilon <= 1/6 and 2 <= s <= 2^(n/2)"
            ),
            "lower_bound_range_checked": lower_applies,
        },
        "cross_paper_alignment": {
            "sparse_qrom_2607_28260_v2": "NOT_ESTABLISHED",
            "reason": (
                "The nearby sparse-QROM preprint also states a sparse-state-preparation "
                "corollary. Full theorem definitions, input/access representations, "
                "precision and synthesis assumptions must be reconciled before comparing."
            ),
        },
        "unknown_resources": {
            "numeric_t_count": None,
            "exact_circuit_depth": None,
            "ancilla_count": None,
            "classical_description_bytes": None,
            "preprocessing_work": None,
            "physical_memory_bytes": None,
            "data_transfer_bytes": None,
            "runtime_seconds": None,
            "energy_j": None,
            "provider_cost": None,
        },
        "evidence_class": "MODEL_ONLY",
        "nonclaims": [
            "not an exact T count",
            "not a numerical certified upper or lower gate-count bound",
            "not a circuit-depth, ancilla, runtime, energy, physical-memory or cost result",
            "not a readable-classical-storage or Hilbert-space memory-equivalence result",
            "not an independent reproduction of the source theorem",
            "not evidence of quantum advantage or a new physical law",
            "not directly comparable to the sparse-QROM theorem until model alignment passes",
        ],
    }
    payload["contract_sha256"] = _canonical_sha256(payload)
    return payload


def validate_sparse_stateprep_bound_contract(contract: dict[str, Any]) -> list[str]:
    """Fail closed on altered inputs, theorem labels, range flags or nonclaims."""
    if not isinstance(contract, dict):
        return ["contract_must_be_a_mapping"]
    inputs = contract.get("input_contract")
    if not isinstance(inputs, dict):
        return ["input_contract_missing"]
    try:
        expected = build_sparse_stateprep_bound_contract(
            inputs.get("n_qubits"),
            inputs.get("support_size"),
            inputs.get("epsilon"),
        )
    except (TypeError, ValueError):
        return ["input_contract_invalid"]
    if contract != expected:
        return ["contract_mismatch"]
    return []

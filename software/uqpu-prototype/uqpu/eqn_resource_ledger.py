"""Fairness/resource ledger for EQN-002C symbolic-regression comparisons.

Candidate-count parity is necessary but not sufficient for a fair comparison.
This module freezes the accounting fields required before BANK, direct-LLM,
union, or LLM-guided-search-space methods are compared as compute/cost claims.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping


METHOD_ARMS = (
    "BANK",
    "LLM_DIRECT",
    "UNION",
    "LLM_GUIDED_SEARCH_SPACE",
)

REQUIRED_LEDGER_FIELDS = (
    "method_arm",
    "candidate_evaluations",
    "optimizer_evaluations",
    "llm_calls",
    "prompt_tokens",
    "completion_tokens",
    "wall_seconds",
    "peak_memory_bytes",
    "hardware_description",
    "monetary_cost_usd",
)

_NUMERIC_NONNEGATIVE_FIELDS = (
    "candidate_evaluations",
    "optimizer_evaluations",
    "llm_calls",
    "prompt_tokens",
    "completion_tokens",
    "wall_seconds",
    "peak_memory_bytes",
    "monetary_cost_usd",
)


def validate_resource_ledger(record: Mapping[str, object]) -> dict[str, object]:
    missing = [field for field in REQUIRED_LEDGER_FIELDS if field not in record]
    errors: list[str] = []

    if "method_arm" in record and record["method_arm"] not in METHOD_ARMS:
        errors.append("method_arm must be one of the frozen EQN-002C arms")

    for field in _NUMERIC_NONNEGATIVE_FIELDS:
        if field not in record:
            continue
        value = record[field]
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            errors.append(f"{field} must be a non-negative number")

    if "hardware_description" in record:
        value = record["hardware_description"]
        if not isinstance(value, str) or not value.strip():
            errors.append("hardware_description must be a non-empty string")

    return {
        "complete": not missing and not errors,
        "missing_fields": missing,
        "errors": errors,
    }


def resource_parity_summary(records: Iterable[Mapping[str, object]]) -> dict[str, object]:
    rows = list(records)
    validations = [validate_resource_ledger(row) for row in rows]
    all_complete = bool(rows) and all(item["complete"] for item in validations)

    candidate_counts = [row.get("candidate_evaluations") for row in rows]
    candidate_budget_equal = bool(rows) and all(
        isinstance(value, (int, float)) and not isinstance(value, bool) for value in candidate_counts
    ) and len(set(candidate_counts)) == 1

    method_arms = [row.get("method_arm") for row in rows]
    unique_method_arms = len(set(method_arms)) == len(method_arms) if rows else False

    return {
        "method_arms": method_arms,
        "candidate_budget_equal": candidate_budget_equal,
        "all_resource_ledgers_complete": all_complete,
        "unique_method_arms": unique_method_arms,
        "full_resource_comparison_ready": all_complete and candidate_budget_equal and unique_method_arms,
        "candidate_budget_parity_equals_compute_cost_parity": False,
        "validations": validations,
    }

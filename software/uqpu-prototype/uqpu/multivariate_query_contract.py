"""Evidence-gated contracts for multivariate polynomial query claims.

This module records theorem assumptions and blocks invalid cross-model query
comparisons. It does not implement the cited algorithms, prove a theorem, or
turn asymptotic bounds into measured hardware cost.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass

_SHA256 = re.compile(r"[0-9a-f]{64}")
_ORACLE_MODELS = {
    "JOINT_BLOCK_ACCESS",
    "ROW_BLOCK_ACCESS",
    "MULTIVARIABLE_SIGNAL_ORACLE",
    "COMMUTING_UNITARY_ACCESS",
    "M_QSP_SIGNAL_OPERATORS",
    "COHERENT_KRAUS_ACCESS",
    "UNKNOWN_CHANNEL_ACCESS",
}
_BOUND_CLASSES = {
    "ASYMPTOTIC_UPPER",
    "EXACT_QUERY_COUNT",
    "OPTIMAL_PER_VARIABLE",
    "UPPER_AND_LOWER",
    "NOT_CLAIMED",
}
_EVIDENCE_CLASSES = {
    "LITERATURE_ONLY",
    "MODEL_ONLY",
    "SIMULATION",
    "PUBLISHED_EXPERIMENT",
    "REAL_QPU",
}


@dataclass(frozen=True)
class MultiOracleQueryContract:
    contract_id: str
    source_id: str
    source_reference: str
    source_sha256: str
    polynomial_sha256: str
    output_semantics_sha256: str
    theorem_scope: str
    oracle_model: str
    variable_names: tuple[str, ...]
    degree_by_variable: tuple[int, ...]
    bound_class: str
    symbolic_query_bound: str
    evidence_class: str = "LITERATURE_ONLY"
    normalization_tau: float | None = None
    approximation_error: float | None = None
    error_metric: str | None = None
    declared_degree: int | None = None
    exact_query_count_by_variable: tuple[int, ...] | None = None
    measured_query_count: int | None = None
    provider_target_id: str | None = None
    execution_record_reference: str | None = None

    def validate(self) -> None:
        required = (
            "contract_id", "source_id", "source_reference", "theorem_scope",
            "symbolic_query_bound",
        )
        for name in required:
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} is required")
        for name in ("source_sha256", "polynomial_sha256", "output_semantics_sha256"):
            if not _SHA256.fullmatch(getattr(self, name)):
                raise ValueError(f"{name} must be a lowercase SHA-256 digest")
        if self.oracle_model not in _ORACLE_MODELS:
            raise ValueError(f"unsupported oracle_model: {self.oracle_model}")
        if self.bound_class not in _BOUND_CLASSES:
            raise ValueError(f"unsupported bound_class: {self.bound_class}")
        if self.evidence_class not in _EVIDENCE_CLASSES:
            raise ValueError(f"unsupported evidence_class: {self.evidence_class}")
        if len(self.variable_names) < 2 or len(self.variable_names) != len(self.degree_by_variable):
            raise ValueError("multivariate contracts require >=2 variables and a matching degree vector")
        if len(set(self.variable_names)) != len(self.variable_names):
            raise ValueError("variable_names must be unique")
        if any(not isinstance(v, str) or not v.strip() for v in self.variable_names):
            raise ValueError("variable names must be non-empty strings")
        if any(not isinstance(d, int) or isinstance(d, bool) or d < 0 for d in self.degree_by_variable):
            raise ValueError("degrees must be non-negative integers")
        if self.declared_degree is not None and (
            not isinstance(self.declared_degree, int)
            or isinstance(self.declared_degree, bool)
            or self.declared_degree < 0
        ):
            raise ValueError("declared_degree must be a non-negative integer")

        if self.oracle_model == "JOINT_BLOCK_ACCESS":
            if self.bound_class != "ASYMPTOTIC_UPPER":
                raise ValueError("joint-block-access contract must retain the theorem's asymptotic bound class")
            if self.normalization_tau is None or not math.isfinite(self.normalization_tau) or not 0 < self.normalization_tau < 1:
                raise ValueError("joint block access requires 0 < normalization_tau < 1")
            if "D/sqrt(tau)" not in self.symbolic_query_bound.replace(" ", ""):
                raise ValueError("joint block access must preserve the stated O(D/sqrt(tau)) expression")

        if self.oracle_model == "ROW_BLOCK_ACCESS":
            if self.bound_class != "EXACT_QUERY_COUNT" or self.declared_degree is None:
                raise ValueError("row-block access requires an exact D-query statement and declared_degree")
            if self.symbolic_query_bound.strip() != "D":
                raise ValueError("row-block exact-query statement must be recorded as D, not as a measurement")

        if self.oracle_model == "MULTIVARIABLE_SIGNAL_ORACLE":
            if self.bound_class != "OPTIMAL_PER_VARIABLE":
                raise ValueError("multivariable signal oracle requires the per-variable optimal-bound class")
            if self.exact_query_count_by_variable != self.degree_by_variable:
                raise ValueError("per-variable query counts must match the theorem's per-variable degree vector")

        if self.oracle_model == "M_QSP_SIGNAL_OPERATORS" and self.bound_class != "NOT_CLAIMED":
            raise ValueError("M-QSP decision/synthesis literature cannot be silently converted to an application query bound")

        if self.approximation_error is not None and (
            not math.isfinite(self.approximation_error) or not 0 < self.approximation_error < 1
        ):
            raise ValueError("approximation_error must be finite and in (0, 1)")
        if self.measured_query_count is not None:
            if not isinstance(self.measured_query_count, int) or isinstance(self.measured_query_count, bool) or self.measured_query_count < 0:
                raise ValueError("measured_query_count must be a non-negative integer")
            if self.evidence_class == "LITERATURE_ONLY":
                raise ValueError("literature-only asymptotics cannot be labelled as a measured query count")
            if not str(self.execution_record_reference or "").strip():
                raise ValueError("measured query counts require an execution record reference")
            if self.evidence_class == "REAL_QPU" and not str(self.provider_target_id or "").strip():
                raise ValueError("real-QPU query counts require an exact provider/target identity")


@dataclass(frozen=True)
class QueryComparisonDecision:
    comparable: bool
    status: str
    reason: str


def compare_query_contracts(
    left: MultiOracleQueryContract,
    right: MultiOracleQueryContract,
) -> QueryComparisonDecision:
    """Only permit comparisons under a matched mathematical and oracle contract."""
    try:
        left.validate()
        right.validate()
    except (TypeError, ValueError) as exc:
        return QueryComparisonDecision(False, "CONTRACT_INVALID", str(exc))

    matched_fields = (
        "polynomial_sha256",
        "output_semantics_sha256",
        "theorem_scope",
        "oracle_model",
        "variable_names",
        "degree_by_variable",
        "bound_class",
        "evidence_class",
        "normalization_tau",
        "approximation_error",
        "error_metric",
    )
    mismatches = [field for field in matched_fields if getattr(left, field) != getattr(right, field)]
    if mismatches:
        return QueryComparisonDecision(
            False,
            "INCOMPARABLE",
            "mismatched contract fields: " + ", ".join(mismatches),
        )
    return QueryComparisonDecision(
        True,
        "MATCHED_CONTRACT",
        "same polynomial/output contract and same oracle, theorem, normalization, and evidence assumptions",
    )

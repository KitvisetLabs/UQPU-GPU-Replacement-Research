"""Scope-only contract for the quantum natural-proofs barrier.

This module classifies whether a declared lower-bound proof strategy falls inside
one conditional theorem's stated scope. It never rejects the mathematical claim,
proves a lower bound, or establishes empirical physical truth.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

SCHEMA = "uqpu-stateprep-lower-bound-methodology-v1"
SOURCE_URL = "https://arxiv.org/abs/2610.06826"
SOURCE_VERSION = "2610.06826v1"
_NATURALNESS = frozenset({"NATURAL", "NON_NATURAL", "UNRESOLVED"})
_SCOPE = frozenset(
    {
        "METHOD_BARRIER_APPLIES_TO_PROOF_STRATEGY_ONLY",
        "OUTSIDE_STATED_SCOPE",
        "ASSUMPTION_NOT_ADOPTED",
        "UNRESOLVED",
    }
)


def _canonical_digest(record: dict[str, Any]) -> str:
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _is_bool_or_none(value: Any) -> bool:
    return value is True or value is False or value is None


def _scope_classification(record: dict[str, Any]) -> str:
    naturalness = record["naturalness_status"]
    if naturalness == "UNRESOLVED":
        return "UNRESOLVED"
    if naturalness == "NON_NATURAL":
        return "OUTSIDE_STATED_SCOPE"
    scope_flags = (
        "target_is_superpolynomial_lower_bound",
        "against_fixed_magic_hierarchy_level",
        "approximation_regime_matches_source",
        "target_uses_polynomial_size_circuits",
        "cryptographic_assumption_matches_source",
    )
    if any(record[name] is False for name in scope_flags):
        return "OUTSIDE_STATED_SCOPE"
    if any(record[name] is None for name in scope_flags):
        return "UNRESOLVED"
    if record["standard_cryptographic_assumption_adopted"] is None:
        return "UNRESOLVED"
    if record["standard_cryptographic_assumption_adopted"] is False:
        return "ASSUMPTION_NOT_ADOPTED"
    return "METHOD_BARRIER_APPLIES_TO_PROOF_STRATEGY_ONLY"


def build_stateprep_lower_bound_methodology(
    *,
    claim_id: str,
    claim_statement: str,
    proof_method: str,
    naturalness_status: str,
    holds_for_sufficient_fraction_of_haar_random_states: bool | None,
    efficiently_testable_given_all_amplitudes: bool | None,
    target_is_superpolynomial_lower_bound: bool | None,
    against_fixed_magic_hierarchy_level: bool | None,
    approximation_regime_matches_source: bool | None,
    target_uses_polynomial_size_circuits: bool | None,
    cryptographic_assumption_statement: str,
    cryptographic_assumption_matches_source: bool | None,
    standard_cryptographic_assumption_adopted: bool | None,
    assessment_basis: str,
    source_url: str = SOURCE_URL,
    source_version: str = SOURCE_VERSION,
) -> dict[str, Any]:
    """Build and validate a proof-method scope record from explicit declarations."""
    text_fields = {
        "claim_id": claim_id,
        "claim_statement": claim_statement,
        "proof_method": proof_method,
        "cryptographic_assumption_statement": cryptographic_assumption_statement,
        "assessment_basis": assessment_basis,
        "source_url": source_url,
        "source_version": source_version,
    }
    for name, value in text_fields.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} is required")
    if source_url != SOURCE_URL:
        raise ValueError("source_url must identify the pinned official arXiv record")
    if source_version != SOURCE_VERSION:
        raise ValueError("source_version must remain pinned to the reviewed preprint version")
    if naturalness_status not in _NATURALNESS:
        raise ValueError("unknown naturalness_status")
    flags = {
        "holds_for_sufficient_fraction_of_haar_random_states": holds_for_sufficient_fraction_of_haar_random_states,
        "efficiently_testable_given_all_amplitudes": efficiently_testable_given_all_amplitudes,
        "target_is_superpolynomial_lower_bound": target_is_superpolynomial_lower_bound,
        "against_fixed_magic_hierarchy_level": against_fixed_magic_hierarchy_level,
        "approximation_regime_matches_source": approximation_regime_matches_source,
        "target_uses_polynomial_size_circuits": target_uses_polynomial_size_circuits,
        "cryptographic_assumption_matches_source": cryptographic_assumption_matches_source,
        "standard_cryptographic_assumption_adopted": standard_cryptographic_assumption_adopted,
    }
    for name, value in flags.items():
        if not _is_bool_or_none(value):
            raise ValueError(f"{name} must be True, False, or None")
    if naturalness_status == "NATURAL" and (
        holds_for_sufficient_fraction_of_haar_random_states is not True
        or efficiently_testable_given_all_amplitudes is not True
    ):
        raise ValueError("NATURAL requires both the largeness and constructivity criteria to be True")
    if naturalness_status == "NON_NATURAL" and (
        holds_for_sufficient_fraction_of_haar_random_states is not False
        and efficiently_testable_given_all_amplitudes is not False
    ):
        raise ValueError("NON_NATURAL requires at least one naturalness criterion to be False")

    record: dict[str, Any] = {
        "schema": SCHEMA,
        "claim_id": claim_id,
        "claim_statement": claim_statement,
        "proof_method": proof_method,
        "naturalness_status": naturalness_status,
        "holds_for_sufficient_fraction_of_haar_random_states": holds_for_sufficient_fraction_of_haar_random_states,
        "efficiently_testable_given_all_amplitudes": efficiently_testable_given_all_amplitudes,
        "target_is_superpolynomial_lower_bound": target_is_superpolynomial_lower_bound,
        "against_fixed_magic_hierarchy_level": against_fixed_magic_hierarchy_level,
        "approximation_regime_matches_source": approximation_regime_matches_source,
        "target_uses_polynomial_size_circuits": target_uses_polynomial_size_circuits,
        "cryptographic_assumption_statement": cryptographic_assumption_statement,
        "cryptographic_assumption_matches_source": cryptographic_assumption_matches_source,
        "standard_cryptographic_assumption_adopted": standard_cryptographic_assumption_adopted,
        "scope_classification": "UNRESOLVED",
        "claim_rejected_by_barrier": False,
        "empirical_physics_established": False,
        "assessment_basis": assessment_basis,
        "source_url": source_url,
        "source_version": source_version,
    }
    record["scope_classification"] = _scope_classification(record)
    record["record_sha256"] = _canonical_digest(record)
    validate_stateprep_lower_bound_methodology(record)
    return record


def validate_stateprep_lower_bound_methodology(record: dict[str, Any]) -> bool:
    """Validate metadata and digest; this does not validate a proof or theorem."""
    if not isinstance(record, dict) or record.get("schema") != SCHEMA:
        raise ValueError("unknown or missing schema")
    for name in (
        "claim_id",
        "claim_statement",
        "proof_method",
        "cryptographic_assumption_statement",
        "assessment_basis",
    ):
        value = record.get(name)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} is required")
    if record.get("naturalness_status") not in _NATURALNESS:
        raise ValueError("unknown naturalness_status")
    for name in (
        "holds_for_sufficient_fraction_of_haar_random_states",
        "efficiently_testable_given_all_amplitudes",
        "target_is_superpolynomial_lower_bound",
        "against_fixed_magic_hierarchy_level",
        "approximation_regime_matches_source",
        "target_uses_polynomial_size_circuits",
        "cryptographic_assumption_matches_source",
        "standard_cryptographic_assumption_adopted",
    ):
        if not _is_bool_or_none(record.get(name)):
            raise ValueError(f"{name} must be True, False, or None")
    if record["naturalness_status"] == "NATURAL" and (
        record["holds_for_sufficient_fraction_of_haar_random_states"] is not True
        or record["efficiently_testable_given_all_amplitudes"] is not True
    ):
        raise ValueError("NATURAL requires both the largeness and constructivity criteria to be True")
    if record["naturalness_status"] == "NON_NATURAL" and (
        record["holds_for_sufficient_fraction_of_haar_random_states"] is not False
        and record["efficiently_testable_given_all_amplitudes"] is not False
    ):
        raise ValueError("NON_NATURAL requires at least one naturalness criterion to be False")
    if record.get("scope_classification") not in _SCOPE:
        raise ValueError("unknown scope_classification")
    if record.get("scope_classification") != _scope_classification(record):
        raise ValueError("scope_classification does not match declared scope fields")
    if record.get("claim_rejected_by_barrier") is not False:
        raise ValueError("the barrier must not automatically reject a mathematical claim")
    if record.get("empirical_physics_established") is not False:
        raise ValueError("this methodology record cannot establish empirical physics")
    if record.get("source_url") != SOURCE_URL or record.get("source_version") != SOURCE_VERSION:
        raise ValueError("source must remain pinned to the declared official preprint version")
    if record.get("record_sha256") != _canonical_digest(record):
        raise ValueError("record_sha256 does not match canonical record content")
    return True

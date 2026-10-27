"""Fail-closed, MODEL_ONLY scale proxy for sparse-QROM T-count theory.

The source theorem is asymptotic in a fixed Clifford+T circuit model. The
numeric expression returned here is a scale proxy, NOT an exact T count,
certified numeric upper/lower bound, physical-memory estimate, wall-clock
prediction, energy estimate, or economic result.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any

SCHEMA = "uqpu-sparse-qrom-proxy-contract-v1"
WORK_ID = "RG-QROM-SPARSE-001"
SOURCE_URL = "https://arxiv.org/abs/2607.28260"
SOURCE_VERSION = "v2-revised-2026-10-01"
MAX_ADDRESS_BITS_FOR_FLOAT_PROXY = 1000
MAX_DATA_BITS_FOR_FLOAT_PROXY = 10**9
_HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def _positive_int(
    value: Any,
    field: str,
    *,
    minimum: int = 1,
    maximum: int | None = None,
) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{field} must be an integer >= {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{field} exceeds the supported numeric proxy range")
    return value


def sparse_qrom_t_count_scale_proxy(
    address_bits: int,
    data_bits: int,
    support_size: int,
) -> dict[str, Any]:
    """Return the leading-scale proxy for the paper's exact sparse-QROM theorem.

    The paper reports Theta(n + min{s, sqrt(s * (m + log2(2^(n+1)/s)))})
    for n-bit addresses, m-bit words (m >= 2), and support size s in [1, 2^n].
    Because Theta hides constants, the returned scalar is not a numeric gate
    count or a certified numerical bound.
    """
    n = _positive_int(
        address_bits, "address_bits", maximum=MAX_ADDRESS_BITS_FOR_FLOAT_PROXY
    )
    m = _positive_int(
        data_bits, "data_bits", minimum=2, maximum=MAX_DATA_BITS_FOR_FLOAT_PROXY
    )
    s = _positive_int(support_size, "support_size")
    if s > (1 << n):
        raise ValueError("support_size must not exceed 2**address_bits")

    # log2(2**(n+1)/s) = n + 1 - log2(s), avoiding a huge intermediate ratio.
    log2_ratio = (n + 1) - math.log2(s)
    sqrt_branch = math.sqrt(s) * math.sqrt(m + log2_ratio)
    support_branch = float(s)
    scale_proxy = float(n) + min(support_branch, sqrt_branch)
    return {
        "address_bits_n": n,
        "data_bits_m": m,
        "support_size_s": s,
        "log2_ratio_term": log2_ratio,
        "sqrt_branch_proxy": sqrt_branch,
        "support_branch_proxy": support_branch,
        "asymptotic_scale_proxy": scale_proxy,
        "asymptotic_expression": (
            "Theta(n + min(s, sqrt(s * (m + log2(2^(n+1)/s)))))"
        ),
        "logarithm_base": 2,
        "theorem_scope": "exact sparse QROM in the stated Clifford+T circuit model",
        "not_exact_t_count": True,
        "not_certified_numeric_upper_or_lower_bound": True,
        "evidence_class": "MODEL_ONLY_ASYMPTOTIC_CIRCUIT_COMPLEXITY_PROXY",
    }


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_sparse_qrom_proxy_contract(manifest: dict[str, Any]) -> dict[str, Any]:
    """Build a declared-input contract; this function does not verify table bytes."""
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be a mapping")

    address_bits = _positive_int(
        manifest.get("address_bits"),
        "address_bits",
        maximum=MAX_ADDRESS_BITS_FOR_FLOAT_PROXY,
    )
    data_bits = _positive_int(
        manifest.get("data_bits"),
        "data_bits",
        minimum=2,
        maximum=MAX_DATA_BITS_FOR_FLOAT_PROXY,
    )
    support_size = _positive_int(manifest.get("support_size"), "support_size")
    if support_size > (1 << address_bits):
        raise ValueError("support_size must not exceed 2**address_bits")

    table_sha256 = manifest.get("table_sha256_declared")
    if not isinstance(table_sha256, str) or not _HASH_RE.fullmatch(table_sha256):
        raise ValueError("table_sha256_declared must be 64 hexadecimal characters")
    output_contract_id = manifest.get("output_contract_id")
    if not isinstance(output_contract_id, str) or not output_contract_id.strip():
        raise ValueError("output_contract_id must be nonempty")
    evidence_ref = manifest.get("sparse_promise_evidence_ref")
    if not isinstance(evidence_ref, str) or not evidence_ref.strip():
        raise ValueError("sparse_promise_evidence_ref must be nonempty")
    if manifest.get("sparse_promise_accepted") is not True:
        raise ValueError("sparse address promise must be explicitly accepted")
    if manifest.get("dense_fallback_available") is not True:
        raise ValueError("a dense/no-promise fallback must remain available")

    proxy = sparse_qrom_t_count_scale_proxy(address_bits, data_bits, support_size)
    contract = {
        "schema": SCHEMA,
        "work_id": WORK_ID,
        "source": {
            "title": "Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding",
            "url": SOURCE_URL,
            "version": SOURCE_VERSION,
            "scope": "sparse-QROM asymptotic T-count theorem only",
        },
        "input_contract": {
            "address_bits": address_bits,
            "data_bits": data_bits,
            "support_size": support_size,
            "table_sha256_declared": table_sha256.lower(),
            "table_hash_status": "DECLARED_NOT_VERIFIED_BY_THIS_MODULE",
            "output_contract_id": output_contract_id.strip(),
            "sparse_promise_accepted": True,
            "sparse_promise_status": "CALLER_DECLARED_NOT_INDEPENDENTLY_VERIFIED",
            "sparse_promise_evidence_ref": evidence_ref.strip(),
            "dense_fallback_available": True,
        },
        "resource_proxy": proxy,
        "unknown_resources": {
            "exact_t_count": None,
            "circuit_depth": None,
            "ancilla_count": None,
            "preprocessing_work": None,
            "classical_table_storage_bytes": None,
            "physical_memory_bytes": None,
            "data_transfer_bytes": None,
            "wall_clock_seconds": None,
            "energy_j": None,
            "provider_cost": None,
        },
        "evidence_class": "MODEL_ONLY",
        "nonclaims": [
            "not an exact gate count",
            "not a certified numeric upper or lower bound",
            "not a physical-memory or readable-classical-storage result",
            "not a wall-clock, energy, provider-billing, or cost-per-task result",
            "not a measured UQPU advantage",
            "does not cover sparse state-preparation or block-encoding formulas",
            "does not authenticate the declared table hash or sparse-promise evidence",
        ],
    }
    contract["contract_sha256"] = _canonical_sha256(contract)
    return contract


def validate_sparse_qrom_proxy_contract(contract: dict[str, Any]) -> list[str]:
    """Check schema, digest, declared assumptions, and MODEL_ONLY boundaries."""
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["contract_must_be_a_mapping"]
    if contract.get("schema") != SCHEMA:
        errors.append("schema_mismatch")
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id_mismatch")

    claimed_digest = contract.get("contract_sha256")
    payload = dict(contract)
    payload.pop("contract_sha256", None)
    if not isinstance(claimed_digest, str) or claimed_digest != _canonical_sha256(payload):
        errors.append("contract_digest_mismatch")

    inputs = contract.get("input_contract")
    if not isinstance(inputs, dict):
        errors.append("input_contract_missing")
        inputs = {}
    if inputs.get("sparse_promise_accepted") is not True:
        errors.append("sparse_promise_not_accepted")
    if inputs.get("dense_fallback_available") is not True:
        errors.append("dense_fallback_missing")
    if inputs.get("table_hash_status") != "DECLARED_NOT_VERIFIED_BY_THIS_MODULE":
        errors.append("table_hash_status_overclaim")
    if inputs.get("sparse_promise_status") != "CALLER_DECLARED_NOT_INDEPENDENTLY_VERIFIED":
        errors.append("sparse_promise_status_overclaim")

    try:
        expected_proxy = sparse_qrom_t_count_scale_proxy(
            inputs.get("address_bits"),
            inputs.get("data_bits"),
            inputs.get("support_size"),
        )
        if contract.get("resource_proxy") != expected_proxy:
            errors.append("resource_proxy_mismatch")
    except (TypeError, ValueError):
        errors.append("resource_proxy_inputs_invalid")

    proxy = contract.get("resource_proxy", {})
    if not isinstance(proxy, dict):
        errors.append("resource_proxy_missing")
        proxy = {}
    if proxy.get("not_exact_t_count") is not True:
        errors.append("exact_t_count_boundary_missing")
    if proxy.get("not_certified_numeric_upper_or_lower_bound") is not True:
        errors.append("numeric_bound_boundary_missing")
    if contract.get("evidence_class") != "MODEL_ONLY":
        errors.append("evidence_class_overclaim")

    unknowns = contract.get("unknown_resources", {})
    required_unknowns = (
        "exact_t_count",
        "circuit_depth",
        "ancilla_count",
        "preprocessing_work",
        "classical_table_storage_bytes",
        "physical_memory_bytes",
        "data_transfer_bytes",
        "wall_clock_seconds",
        "energy_j",
        "provider_cost",
    )
    if not isinstance(unknowns, dict) or any(unknowns.get(k) is not None for k in required_unknowns):
        errors.append("unmeasured_resources_must_remain_null")
    return errors

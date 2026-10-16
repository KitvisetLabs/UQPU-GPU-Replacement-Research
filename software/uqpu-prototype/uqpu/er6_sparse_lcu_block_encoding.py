"""Workload-derived LCU block-encoding contract for the frozen ER6 MaxCut case.

This module replaces a dense signal-unitary *input assumption* with an explicit
linear-combination-of-unitaries (LCU) description of the MaxCut cost operator.
It verifies the projected operator algebraically on all 64 basis states.  It
does not synthesize PREP/SELECT gates, execute QSVT, or establish scalability,
hardware performance, energy, cost, or quantum advantage.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any


CONTRACT_ID = "QOS-AUDIT-010B6"
SOURCE_CONTRACT_ID = "8efaa94bb3306d25"
SOURCE_ISING_SHA256 = "bc3fb615b6fd2530694b097fde804e62f165fd7d0953bf66aff4602cd77fa201"
POLYNOMIAL_DEGREE = 81


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _cut_value(index: int, edges: list[tuple[int, int]]) -> int:
    return sum(((index >> u) & 1) != ((index >> v) & 1) for u, v in edges)


def build_lcu_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    fixture = frozen["fixture"]
    output = frozen["output_contract"]
    node_count = int(fixture["generator"]["node_count"])
    edges = [tuple(map(int, edge)) for edge in fixture["edges"]]
    if fixture["case_id"] != "er6" or node_count != 6:
        raise ValueError("expected frozen six-variable ER6 fixture")
    if output["contract_id"] != SOURCE_CONTRACT_ID:
        raise ValueError("source output contract drift")
    if any(u == v or not (0 <= u < node_count and 0 <= v < node_count) for u, v in edges):
        raise ValueError("invalid ER6 edge")
    if len(edges) != len(set(edges)) or not edges:
        raise ValueError("ER6 edges must be unique and nonempty")

    alpha = float(len(edges))
    terms = [{"term_id": "I", "coefficient": alpha / 2.0, "pauli_z_qubits": []}]
    terms.extend(
        {"term_id": f"ZZ_{u}_{v}", "coefficient": -0.5,
         "pauli_z_qubits": [u, v]}
        for u, v in edges
    )
    probabilities = [abs(term["coefficient"]) / alpha for term in terms]
    select_qubits = math.ceil(math.log2(len(terms)))
    padded_terms = 1 << select_qubits

    residuals = []
    diagonal = []
    for index in range(1 << node_count):
        direct = _cut_value(index, edges) / alpha
        projected = 0.0
        for term in terms:
            eigenvalue = 1
            for qubit in term["pauli_z_qubits"]:
                eigenvalue *= 1 if ((index >> qubit) & 1) == 0 else -1
            projected += term["coefficient"] * eigenvalue / alpha
        residuals.append(abs(direct - projected))
        diagonal.append(direct)

    accepted = [int(row["index"]) for row in output["accepted_outputs"]]
    accepted_values = [diagonal[index] for index in accepted]
    contract = {
        "schema": "uqpu-er6-sparse-lcu-block-encoding-v1",
        "work_id": CONTRACT_ID,
        "source": {
            "fixture": "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json",
            "output_contract_id": SOURCE_CONTRACT_ID,
            "ising_instance_sha256": SOURCE_ISING_SHA256,
            "variable_order": "variable_0_is_lsb",
        },
        "operator": {
            "definition": "A=H_cut/alpha; H_cut=sum_(u,v) (I-Z_u Z_v)/2",
            "system_qubits": node_count,
            "matrix_dimension": 1 << node_count,
            "edges": [list(edge) for edge in edges],
            "alpha": alpha,
            "spectral_interval": [min(diagonal), max(diagonal)],
            "active_lcu_terms": len(terms),
            "select_qubits": select_qubits,
            "padded_select_terms": padded_terms,
            "terms": terms,
            "prep_probabilities": probabilities,
        },
        "verification": {
            "basis_states_exhaustively_checked": 1 << node_count,
            "max_projected_diagonal_residual": max(residuals),
            "prep_probability_sum_residual": abs(sum(probabilities) - 1.0),
            "accepted_assignment_indices": accepted,
            "accepted_normalized_cut_values": accepted_values,
            "passed": max(residuals) <= 1e-15 and abs(sum(probabilities) - 1.0) <= 1e-15,
        },
        "resource_contract": {
            "qsvt_polynomial_degree": POLYNOMIAL_DEGREE,
            "block_encoding_queries_if_used_by_degree_81_sequence": POLYNOMIAL_DEGREE,
            "logical_system_qubits": node_count,
            "logical_select_qubits": select_qubits,
            "logical_qubits_before_work_registers": node_count + select_qubits,
            "select_pauli_zz_branches_per_query": len(edges),
            "prep_calls_per_block_encoding_query": 2,
            "prep_gate_count": None,
            "select_decomposed_gate_count": None,
            "fault_tolerant_t_count": None,
            "serialized_circuit_bytes": None,
            "shots": 0,
            "provider_jobs": 0,
            "provider_cost": None,
            "energy_j": None,
        },
        "scaling_and_access_boundary": {
            "lcu_term_growth": "1+|E|",
            "select_branch_growth": "|E|",
            "general_sparse_qrom_bound_applied": False,
            "reason": "No fault-tolerant precision or concrete PREP/QROM implementation is fixed; asymptotic sparse-QROM bounds are not measured resources.",
            "remaining_gate": "provider-neutral PREP/SELECT circuit synthesis, independent SDK operator check, and measured decomposition scaling",
        },
        "evidence_class": "SIMULATION_ALGEBRAIC_BLOCK_ENCODING_CONTRACT",
        "nonclaims": [
            "not a decomposed circuit", "not a provider execution", "not a scalability proof",
            "not a competitive workload", "not a cost or energy advantage",
        ],
    }
    contract["contract_sha256"] = _canonical_sha256(contract)
    return contract


def validate_lcu_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    if contract.get("source", {}).get("output_contract_id") != SOURCE_CONTRACT_ID:
        errors.append("source_contract_mismatch")
    if contract.get("operator", {}).get("active_lcu_terms") != 10:
        errors.append("unexpected_lcu_term_count")
    if contract.get("operator", {}).get("select_qubits") != 4:
        errors.append("unexpected_select_qubits")
    if contract.get("verification", {}).get("passed") is not True:
        errors.append("algebraic_verification_failed")
    resources = contract.get("resource_contract", {})
    if resources.get("provider_jobs") != 0 or resources.get("shots") != 0:
        errors.append("provider_fields_must_remain_zero")
    if any(resources.get(field) is not None for field in
           ("provider_cost", "energy_j", "prep_gate_count", "fault_tolerant_t_count")):
        errors.append("unmeasured_resource_must_remain_null")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _canonical_sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))

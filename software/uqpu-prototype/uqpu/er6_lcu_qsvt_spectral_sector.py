"""Independent two-dimensional spectral-sector check for the ER6 QSVT prefix.

For each of the 64 diagonal workload eigenvalues ``a``, a Hermitian involutory
block encoding reduces on the signal subspace to
``[[a, sqrt(1-a^2)], [sqrt(1-a^2), -a]]``.  This module evaluates the frozen
two-query projector-phase recurrence in that 2x2 sector and cross-checks it
against an independently derived closed form.  It is a simulation contract,
not a provider execution or an end-to-end degree-81 result.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from typing import Any

from .er6_lcu_prep_select_qiskit import build_provider_neutral_contract
from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040, phase_fingerprint


CONTRACT_ID = "QOS-AUDIT-010B10"
PHASE_INDICES = (0, 1, 2)
TOLERANCE = 2e-12


def _sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _matmul2(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def signal_involution(eigenvalue: float):
    if not -1.0 <= eigenvalue <= 1.0:
        raise ValueError("block-encoded eigenvalue must lie in [-1, 1]")
    complement = math.sqrt(max(0.0, 1.0 - eigenvalue * eigenvalue))
    return ((eigenvalue, complement), (complement, -eigenvalue))


def projector_phase(phase: float):
    return ((cmath.exp(1j * phase), 0j), (0j, cmath.exp(-1j * phase)))


def explicit_two_query_amplitude(eigenvalue: float) -> complex:
    phases = [FROZEN_PHASES_V040[index] for index in PHASE_INDICES]
    signal = signal_involution(eigenvalue)
    product = projector_phase(phases[0])
    for factor in (
        signal,
        projector_phase(phases[1]),
        signal,
        projector_phase(phases[2]),
    ):
        product = _matmul2(product, factor)
    return complex(product[0][0])


def closed_form_two_query_amplitude(eigenvalue: float) -> complex:
    phi0, phi1, phi2 = [FROZEN_PHASES_V040[index] for index in PHASE_INDICES]
    a2 = eigenvalue * eigenvalue
    return cmath.exp(1j * (phi0 + phi2)) * (
        a2 * cmath.exp(1j * phi1) + (1.0 - a2) * cmath.exp(-1j * phi1)
    )


def spectral_sector_amplitudes(frozen: dict[str, Any]) -> list[complex]:
    upstream = build_provider_neutral_contract(frozen)
    return [
        explicit_two_query_amplitude(float(value))
        for value in upstream["block_encoding"]["expected_projected_diagonal"]
    ]


def build_spectral_sector_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    from .er6_lcu_qsvt_two_query import build_two_query_contract

    upstream = build_provider_neutral_contract(frozen)
    two_query = build_two_query_contract(frozen)
    alpha = float(upstream["block_encoding"]["normalization_alpha"])
    values = upstream["block_encoding"]["expected_projected_diagonal"]
    rows = []
    for index, raw_value in enumerate(values):
        eigenvalue = float(raw_value)
        explicit = explicit_two_query_amplitude(eigenvalue)
        closed = closed_form_two_query_amplitude(eigenvalue)
        rows.append({
            "system_index": index,
            "cut_value": int(round(eigenvalue * alpha)),
            "normalized_eigenvalue": eigenvalue,
            "signal_complement": math.sqrt(max(0.0, 1.0 - eigenvalue * eigenvalue)),
            "explicit_2x2_amplitude": [explicit.real, explicit.imag],
            "closed_form_amplitude": [closed.real, closed.imag],
            "max_abs_residual": abs(explicit - closed),
        })
    unique_values = sorted(set(float(value) for value in values))
    max_residual = max(row["max_abs_residual"] for row in rows)
    contract = {
        "schema": "uqpu-er6-lcu-qsvt-spectral-sector-v1",
        "work_id": CONTRACT_ID,
        "upstream_work_id": two_query["work_id"],
        "upstream_two_query_sha256": two_query["contract_sha256"],
        "phase_source": {
            "phase_fingerprint": phase_fingerprint(),
            "selected_indices": list(PHASE_INDICES),
            "selected_values": [FROZEN_PHASES_V040[index] for index in PHASE_INDICES],
        },
        "spectral_contract": {
            "sector_dimension": 2,
            "workload_sectors": len(rows),
            "unique_normalized_eigenvalues": unique_values,
            "signal_operator": "[[a,sqrt(1-a^2)],[sqrt(1-a^2),-a]]",
            "projector_phase": "diag(exp(i*phi),exp(-i*phi))",
            "recurrence": "P(phi_0) U_a P(phi_1) U_a P(phi_2)",
            "rows": rows,
        },
        "verification": {
            "all_64_sectors_checked": len(rows) == 64,
            "explicit_vs_closed_form_max_abs_residual": max_residual,
            "tolerance": TOLERANCE,
            "passed": len(rows) == 64 and max_residual <= TOLERANCE,
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "evidence_class": "SIMULATION_SPECTRAL_SECTOR_CHECK",
        "nonclaims": [
            "not full degree-81 synthesis",
            "not target-aware transpilation or provider execution",
            "not hardware, energy, cost, advantage, or replacement evidence",
        ],
    }
    contract["contract_sha256"] = _sha256(contract)
    return contract


def validate_spectral_sector_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    spectral = contract.get("spectral_contract", {})
    rows = spectral.get("rows", [])
    if spectral.get("sector_dimension") != 2:
        errors.append("sector_dimension_mismatch")
    if len(rows) != 64 or [row.get("system_index") for row in rows] != list(range(64)):
        errors.append("sector_coverage_mismatch")
    if any(not -1.0 <= float(row.get("normalized_eigenvalue", 2.0)) <= 1.0 for row in rows):
        errors.append("spectral_domain_violation")
    verification = contract.get("verification", {})
    if verification.get("passed") is not True:
        errors.append("verification_failed")
    if verification.get("explicit_vs_closed_form_max_abs_residual", math.inf) > TOLERANCE:
        errors.append("recurrence_residual_exceeded")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))

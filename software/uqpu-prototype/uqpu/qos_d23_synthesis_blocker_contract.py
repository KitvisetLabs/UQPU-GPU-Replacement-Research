from __future__ import annotations

from dataclasses import dataclass

EXPECTED_FINGERPRINT = "4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a"
EXPECTED_EXCEPTION = "could not broadcast input array from shape (41,) into shape (42,)"


@dataclass(frozen=True)
class BlockerDecision:
    status: str
    evidence_level: str
    phase_vector_usable: bool
    independent_reconstruction_allowed: bool
    mathematical_infeasibility_claim_allowed: bool
    next_gate: str


def classify_batch053_result(result: dict[str, object]) -> BlockerDecision:
    """Fail-closed classification of the Batch-053 pinned solver result.

    This contract prevents a third-party implementation exception from being
    promoted to mathematical QSP infeasibility or to a usable phase vector.
    """
    contract = result.get("contract")
    if not isinstance(contract, dict):
        return BlockerDecision(
            "PROVENANCE_INVALID",
            "UNVERIFIED_INPUT",
            False,
            False,
            False,
            "restore pinned coefficient/solver provenance",
        )
    if contract.get("coefficient_fingerprint") != EXPECTED_FINGERPRINT:
        return BlockerDecision(
            "PROVENANCE_INVALID",
            "UNVERIFIED_INPUT",
            False,
            False,
            False,
            "restore frozen Batch-051 coefficient fingerprint",
        )

    status = result.get("status")
    if status == "SYNTHESIS_EXCEPTION" and result.get("exception_message") == EXPECTED_EXCEPTION:
        return BlockerDecision(
            "TOOL_BLOCKED_REPRODUCED",
            "PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_EXCEPTION",
            False,
            False,
            False,
            "QOS-AUDIT-010B2A: minimal odd-parity Jacobian contract or independent maintained solver",
        )

    if status == "SYNTHESIS_CONVERGED" and result.get("qsp_phase_sequence_synthesized") is True:
        phases = result.get("phases")
        if isinstance(phases, list) and len(phases) == 82:
            return BlockerDecision(
                "PHASE_VECTOR_REQUIRES_RECONSTRUCTION",
                "PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_EXECUTION",
                True,
                True,
                False,
                "QOS-AUDIT-010B3: repository-owned independent 2x2 reconstruction",
            )

    return BlockerDecision(
        "UNRESOLVED_SYNTHESIS_RESULT",
        "NUMERICAL_RESULT_NOT_PROMOTABLE",
        False,
        False,
        False,
        "preserve result and audit declared solver contract",
    )

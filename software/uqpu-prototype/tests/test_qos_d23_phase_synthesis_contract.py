from uqpu.qos_d23_phase_synthesis_contract import (
    EXPECTED_FINGERPRINT,
    PINNED_CRITERIA,
    PINNED_METHOD,
    PINNED_PACKAGE,
    PINNED_PARITY,
    PINNED_PHASE_TYPE,
    PINNED_TARGET_PRE,
    PINNED_VERSION,
    frozen_contract,
    synthesize_with_pinned_qsppack,
)


def test_contract_is_explicit_and_bound_to_batch051_candidate():
    contract = frozen_contract()
    assert contract.package == PINNED_PACKAGE == "qsppack"
    assert contract.version == PINNED_VERSION
    assert contract.method == PINNED_METHOD == "Newton"
    assert contract.parity == PINNED_PARITY == 1
    assert contract.target_pre is PINNED_TARGET_PRE is True
    assert contract.phase_type == PINNED_PHASE_TYPE == "full"
    assert contract.criteria == PINNED_CRITERIA == 1e-12
    assert contract.coefficient_fingerprint == EXPECTED_FINGERPRINT
    assert contract.fingerprint_matches_batch051


def test_unpinned_environment_cannot_be_promoted_to_verified_phases():
    result = synthesize_with_pinned_qsppack()
    if result["status"] in {"DEPENDENCY_NOT_INSTALLED", "PINNED_VERSION_MISMATCH"}:
        assert result["qsp_phase_sequence_synthesized"] is False
        assert result["independent_reconstruction_passed"] is False
    else:
        # Even a converged external synthesis is not independent reconstruction.
        assert result["independent_reconstruction_passed"] is False
        if result["status"] == "SYNTHESIS_CONVERGED":
            assert result["qsp_phase_sequence_synthesized"] is True
            assert result["phase_count"] == 82
        else:
            assert result["qsp_phase_sequence_synthesized"] is False

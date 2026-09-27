from uqpu.scm_preregistration import (
    REQUIRED_LEAKAGE_ITEMS, SCMPreregistration, ready_to_collect,
    validate_preregistration,
)

def complete(**changes):
    d=dict(
        study_id="SCM-P2-CAL-001", protocol_version="1.0",
        primary_hypothesis="Known interference increases registered anomaly rate.",
        null_hypothesis="Interference condition does not change anomaly rate.",
        primary_outcome="precommitted threshold exceedance rate",
        sample_size=1000, stopping_rule="fixed-N; no optional stopping",
        randomization_method="CSPRNG blocked randomization",
        blinding_roles=("operator","analyst"),
        exclusion_rules=("documented hardware failure only",),
        leakage_audit_items=REQUIRED_LEAKAGE_ITEMS,
        calibration_plan="inject traceable known signals before and after run",
        analysis_plan="fixed threshold and condition comparison",
        replication_plan="repeat from frozen manifest at independent site",
    )
    d.update(changes)
    return SCMPreregistration(**d)

def test_complete_preregistration_is_ready():
    p=complete()
    assert validate_preregistration(p)==()
    assert ready_to_collect(p)
    assert p.evidence_class=="PREREGISTRATION_ONLY_NO_EMPIRICAL_RESULT"

def test_optional_sample_size_is_rejected():
    assert "invalid:sample_size" in validate_preregistration(complete(sample_size=0))

def test_missing_leakage_item_blocks_collection():
    p=complete(leakage_audit_items=("target_metadata",))
    assert not ready_to_collect(p)
    assert any(x.startswith("missing_leakage:") for x in validate_preregistration(p))

def test_human_study_requires_ethics_reference():
    p=complete(human_participants=True)
    assert "missing:ethics_approval_ref" in validate_preregistration(p)

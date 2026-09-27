from uqpu.scm_replication_contract import (
    REQUIRED_ENVIRONMENT_FIELDS, ReplicationManifest, compare_replications,
    sha256_bytes, validate_manifest, verify_dataset,
)

def manifest(data=b"frozen-data"):
    return ReplicationManifest(
        protocol_id="SCM-GATE-003", protocol_version="1.0",
        code_commit="abc123", data_sha256=sha256_bytes(data),
        schema_version="scm-trial-v1", randomization_method="CSPRNG-after-isolation",
        scoring_rule="exact-match-v1", exclusion_rules=("hardware-failure-only",),
        environment_fields=REQUIRED_ENVIRONMENT_FIELDS,
    )

def test_complete_manifest_validates_and_dataset_verifies():
    m=manifest()
    assert validate_manifest(m) == ()
    assert verify_dataset(m,b"frozen-data")
    assert m.evidence_class == "REPLICATION_INFRASTRUCTURE_ONLY"

def test_changed_dataset_fails_integrity():
    assert not verify_dataset(manifest(),b"changed")

def test_missing_environment_log_blocks_contract():
    m=manifest()
    bad=ReplicationManifest(**{**m.__dict__,"environment_fields":("utc_start",)})
    errors=validate_manifest(bad)
    assert any(x.startswith("missing_environment:") for x in errors)

def test_replication_comparison_reports_protocol_drift():
    a={"scoring":"v1","labels":"4","hardware":"A"}
    b={"scoring":"v2","labels":"4","hardware":"B"}
    assert compare_replications(a,b,("scoring","labels")) == ("scoring",)

from uqpu.cycle001_delta05 import *

def test_equal_output_certificate_is_neutral():
    c=ising_certificate()
    assert c.error_tolerance==0.01 and c.confidence==0.95
    assert "NO_ADVANTAGE" in c.evidence_class

def test_provider_template_is_not_evidence():
    x=blank_provider_manifest_for_ising()
    assert x["execution_id"]==""
    assert x["status"]=="TEMPLATE_NOT_EXECUTION_EVIDENCE"

def test_residual_sensitivity():
    rows=residual_sensitivity(1_000_000,100,[1e-3,1e-5])
    assert not rows[0]["passes_necessary_condition"]
    assert rows[1]["passes_necessary_condition"]

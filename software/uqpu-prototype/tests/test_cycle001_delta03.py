from uqpu.cycle001_delta03 import *

def test_provider_manifest_requires_execution_provenance():
    m=ProviderEvidenceManifest("p","b","w","sha","","2026-09-28T00:00Z",100,"contract","invoice",1)
    assert "missing:execution_id" in validate_provider(m)

def test_provider_manifest_accepts_zero_cost_if_provenance_complete():
    m=ProviderEvidenceManifest("p","b","w","sha","run","2026-09-28T00:00Z",100,"contract","provider record",0)
    assert validate_provider(m)==()

def test_capital_gate_requires_failure_action():
    g=CapitalGate("x","MODEL","G1","bench",100,"advance","")
    assert "missing:failure_action" in validate_capital_gate(g)

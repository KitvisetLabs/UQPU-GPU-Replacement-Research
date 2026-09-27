"""Cycle-001 Delta-03 evidence and capital contracts."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProviderEvidenceManifest:
    provider:str; backend:str; workload_id:str; code_commit:str
    execution_id:str; utc_time:str; shots:int
    accepted_output_contract:str; billing_source:str; billed_cost:float
    evidence_class:str="PROVIDER_EVIDENCE_MANIFEST"

def validate_provider(m):
    e=[]
    for n in ("provider","backend","workload_id","code_commit","execution_id","utc_time","accepted_output_contract","billing_source"):
        if not getattr(m,n).strip(): e.append("missing:"+n)
    if m.shots<=0:e.append("invalid:shots")
    if m.billed_cost<0:e.append("invalid:billed_cost")
    return tuple(e)

@dataclass(frozen=True)
class CapitalGate:
    project_id:str; evidence_state:str; next_gate:str
    cheapest_decisive_test:str; capital_at_risk:float
    success_unlock:str; failure_action:str
    evidence_class:str="CAPITAL_GOVERNANCE_ONLY"

def validate_capital_gate(g):
    e=[]
    for n in ("project_id","evidence_state","next_gate","cheapest_decisive_test","success_unlock","failure_action"):
        if not getattr(g,n).strip():e.append("missing:"+n)
    if g.capital_at_risk<0:e.append("invalid:capital_at_risk")
    return tuple(e)

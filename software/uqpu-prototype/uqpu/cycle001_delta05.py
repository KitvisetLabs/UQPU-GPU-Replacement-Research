"""Cycle-001 Delta-05 benchmark/provider/AI-cost fixtures."""
from dataclasses import dataclass
from .cycle001_delta03 import ProviderEvidenceManifest

@dataclass(frozen=True)
class EqualOutputCertificate:
    case_id:str; output_contract:str; classical_method:str; quantum_method:str
    error_tolerance:float; confidence:float
    evidence_class:str="BENCHMARK_CONTRACT_NO_ADVANTAGE_CLAIM"

def ising_certificate():
    return EqualOutputCertificate(
      "OBS-ISING-ENERGY-001",
      "same scalar Ising energy expectation under identical epsilon/confidence",
      "competitive exact/tensor/sampling baseline selected by instance structure",
      "QOS/QSVT or other quantum estimator with all state-prep/shots/readout charged",
      0.01,0.95)

def blank_provider_manifest_for_ising():
    return {
      "provider":"","backend":"","workload_id":"OBS-ISING-ENERGY-001",
      "code_commit":"","execution_id":"","utc_time":"","shots":0,
      "accepted_output_contract":"same scalar Ising energy expectation under identical epsilon/confidence",
      "billing_source":"","billed_cost":0.0,
      "status":"TEMPLATE_NOT_EXECUTION_EVIDENCE"}

def residual_sensitivity(baseline_cost,target_cost,residual_fractions):
    target_fraction=target_cost/baseline_cost
    return tuple({"residual_fraction":r,
      "infinite_speedup_cost":baseline_cost*r,
      "passes_necessary_condition":r<=target_fraction} for r in residual_fractions)

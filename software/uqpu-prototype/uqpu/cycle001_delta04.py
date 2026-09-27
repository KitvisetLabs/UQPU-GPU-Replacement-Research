"""Cycle-001 Delta-04 named research cases and sensitivity helpers.

Named cases are research fixtures, not measured performance.
"""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class CompactObservableCase:
    case_id:str; problem:str; accepted_output:str; output_cardinality:int
    full_state_dimension:int; evidence_class:str="NAMED_ANALYTIC_CASE_ONLY"
    def output_floor_bits(self): return math.log2(self.output_cardinality)
    def naive_full_state_index_bits(self): return math.log2(self.full_state_dimension)

def ising_energy_case(n_qubits:int=20)->CompactObservableCase:
    return CompactObservableCase(
      "OBS-ISING-ENERGY-001",
      "estimate one bounded Ising-Hamiltonian energy expectation",
      "scalar expectation within preregistered absolute error epsilon",
      2**16, 2**n_qubits)

@dataclass(frozen=True)
class ResidualSensitivity:
    baseline_cost:float; target_cost:float
    def required_total_fraction(self): return self.target_cost/self.baseline_cost
    def infinite_speedup_floor(self,residual_fraction): return self.baseline_cost*residual_fraction
    def residual_passes_necessary_condition(self,residual_fraction):
        return residual_fraction<=self.required_total_fraction()

@dataclass(frozen=True)
class DeviceMaterialFactoryCase:
    case_id:str; device_primitive:str; target_function:str; material_candidate:str
    process_route:str; metrology:str; evidence_class:str="PATHWAY_SELECTION_NOT_QUALIFICATION"

def biomass_emi_pathway():
    return DeviceMaterialFactoryCase(
      "DMF-BIOCARBON-EMI-001",
      "conductive EMI-shielding enclosure/coating",
      "attenuate electromagnetic interference while meeting mass/thermal/process constraints",
      "purified/activated or graphitized biomass-derived carbon composite",
      "pyrolysis -> purification -> activation/graphitization as justified -> composite/coating fabrication",
      "shielding effectiveness vs frequency + conductivity + thickness + thermal/mechanical checks")

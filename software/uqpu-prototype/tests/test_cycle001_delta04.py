from uqpu.cycle001_delta04 import *

def test_named_observable_is_compact_relative_to_state_index():
    c=ising_energy_case(30)
    assert c.output_floor_bits()==16
    assert c.naive_full_state_index_bits()==30

def test_residual_necessary_condition():
    s=ResidualSensitivity(1_000_000,100)
    assert s.required_total_fraction()==1e-4
    assert s.residual_passes_necessary_condition(1e-5)
    assert not s.residual_passes_necessary_condition(1e-3)

def test_biomass_pathway_is_not_qualification():
    x=biomass_emi_pathway()
    assert "EMI" in x.device_primitive
    assert x.evidence_class=="PATHWAY_SELECTION_NOT_QUALIFICATION"

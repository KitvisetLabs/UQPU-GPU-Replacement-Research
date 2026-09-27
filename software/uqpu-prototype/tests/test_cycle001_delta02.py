from uqpu.cycle001_delta02 import *
from uqpu.cross_lane_contracts import validate_useful_output,validate_device_factory,validate_difference

def test_instantiated_contracts_complete():
    w,d,p=cycle001_fixtures()
    assert validate_useful_output(w)==()
    assert validate_device_factory(d)==()
    assert validate_difference(p)==()

def test_output_information_floor():
    assert minimum_output_bits(1)==0
    assert minimum_output_bits(256)==8

def test_residual_cost_floor_dominates_infinite_speedup():
    x=ResidualCostCase(1_000_000,1e-3,1e12)
    assert x.projected_cost()>=1000

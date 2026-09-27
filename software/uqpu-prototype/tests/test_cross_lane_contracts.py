from uqpu.cross_lane_contracts import *

def test_useful_output_contract():
    x=UsefulOutputLedger("q1","energy estimate","abs error <= 0.01",1024,1,2,64,0.5,3,40)
    assert validate_useful_output(x)==()
    assert x.evidence_class=="ACCOUNTING_CONTRACT_ONLY"

def test_device_factory_requires_complete_chain():
    x=DeviceFactoryChain("T1","<100 us","","anneal temperature","sheet resistance","good dies/wafer","cost/good die")
    assert "missing:material_property" in validate_device_factory(x)

def test_difference_contract_requires_falsifier():
    x=DifferenceToTechnology("candidate phase","blind classifier","prep","drive","coherence","sensor","switch","energy","")
    assert "missing:falsifier" in validate_difference(x)

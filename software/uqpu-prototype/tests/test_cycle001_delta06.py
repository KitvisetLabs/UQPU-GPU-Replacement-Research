from uqpu.cycle001_delta06 import *

def test_resource_total_and_validation():
    x=MatchedResourceLedger("x","y",1,2,100,3,4,5,6)
    assert validate_resource(x)==()
    assert x.total_seconds()==10

def test_coupon_is_preregistered_not_measured():
    x=pangola_emi_coupon()
    assert x.frequency_band=="PRECOMMIT_BEFORE_MEASUREMENT"
    assert x.evidence_class=="PREREGISTRATION_NO_MEASUREMENTS"

def test_ai_cost_rows_have_both_baselines():
    rows=ai_cost_canonical_rows()
    assert len(rows)==12
    assert {x[0] for x in rows}=={10_000_000_000_000,100_000_000_000_000}

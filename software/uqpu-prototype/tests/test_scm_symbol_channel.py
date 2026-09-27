from uqpu.scm_symbol_channel import SymbolChannelResult, validate_result

def test_chance_level_has_no_verified_credit():
    r=SymbolChannelResult(100,4,25,0,10)
    assert validate_result(r)==()
    assert r.verified_bits_upper_account==0

def test_above_chance_credit_is_descriptive_only():
    r=SymbolChannelResult(100,4,80,5,20)
    assert r.verified_bits_upper_account>0
    assert r.verified_bit_rate_upper_account>0
    assert r.evidence_class=="MODEL_PROTOCOL_ONLY_NO_SOURCE_IDENTITY"

def test_invalid_counts_rejected():
    assert "invalid:counts" in validate_result(SymbolChannelResult(10,4,9,2,1))

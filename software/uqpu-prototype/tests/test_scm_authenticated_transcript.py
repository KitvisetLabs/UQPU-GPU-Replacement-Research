from uqpu.scm_authenticated_transcript import *
from uqpu.scm_session_auth import create_challenge
from uqpu.scm_symbol_channel import SymbolChannelResult

def good():
    cs=tuple(create_challenge("s",str(i%4),"salt"+str(i),"n"+str(i)) for i in range(4))
    r=SymbolChannelResult(4,4,2,0,10)
    return AuthenticatedTranscript("SCM-3A-v1",cs,r,REQUIRED_LEAKAGE)

def test_complete_transcript_validates():
    assert validate_transcript(good())==()

def test_missing_leakage_blocks():
    t=good()
    bad=AuthenticatedTranscript(t.protocol_id,t.challenges,t.result,t.leakage_checks[:-1])
    assert any(x.startswith("missing_leakage:") for x in validate_transcript(bad))

def test_trial_count_must_match_challenges():
    t=good()
    bad=AuthenticatedTranscript(t.protocol_id,t.challenges[:-1],t.result,t.leakage_checks)
    assert "mismatch:challenge_trial_count" in validate_transcript(bad)

from uqpu.scm_transcript_replication import *
from uqpu.scm_authenticated_transcript import *
from uqpu.scm_session_auth import create_challenge
from uqpu.scm_symbol_channel import SymbolChannelResult

def fixture(correct=2):
    cs=tuple(create_challenge("s",str(i%4),"salt"+str(i),"n"+str(i)) for i in range(4))
    return AuthenticatedTranscript("SCM-3A-v1",cs,SymbolChannelResult(4,4,correct,0,10),REQUIRED_LEAKAGE)

def test_hash_is_deterministic():
    assert transcript_sha256(fixture())==transcript_sha256(fixture())

def test_changed_result_changes_hash():
    assert transcript_sha256(fixture(2))!=transcript_sha256(fixture(3))

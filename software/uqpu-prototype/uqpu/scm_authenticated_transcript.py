"""SCM authenticated transcript contract.

Combines session challenge integrity, symbol scoring, and a mandatory leakage
audit. Passing validation is protocol evidence only and cannot identify a source.
"""
from dataclasses import dataclass
from .scm_symbol_channel import SymbolChannelResult, validate_result
from .scm_session_auth import SessionChallenge, validate_unique_nonces

REQUIRED_LEAKAGE=("target_metadata","filenames","trial_timing","network_traffic",
"operator_contact","audio_visual_cues","rng_custody",
"ai_retrieval_or_training_contamination","post_selection")

@dataclass(frozen=True)
class AuthenticatedTranscript:
    protocol_id:str
    challenges:tuple[SessionChallenge,...]
    result:SymbolChannelResult
    leakage_checks:tuple[str,...]
    evidence_class:str="AUTHENTICATED_PROTOCOL_TRANSCRIPT_NO_SOURCE_IDENTITY"

def validate_transcript(t):
    e=[]
    if not t.protocol_id.strip():e.append("missing:protocol_id")
    e.extend(validate_unique_nonces(t.challenges))
    e.extend(validate_result(t.result))
    have=set(t.leakage_checks)
    for x in REQUIRED_LEAKAGE:
        if x not in have:e.append("missing_leakage:"+x)
    if len(t.challenges)!=t.result.trials:e.append("mismatch:challenge_trial_count")
    return tuple(e)

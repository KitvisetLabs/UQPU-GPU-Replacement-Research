"""Hashable SCM authenticated transcript envelope for replication."""
import hashlib,json
from .scm_authenticated_transcript import AuthenticatedTranscript,validate_transcript

def canonical_transcript_bytes(t:AuthenticatedTranscript)->bytes:
    obj={
      "protocol_id":t.protocol_id,
      "evidence_class":t.evidence_class,
      "challenges":[{"session_id":c.session_id,"nonce":c.nonce,"target_commitment":c.target_commitment} for c in t.challenges],
      "result":{"trials":t.result.trials,"alphabet_size":t.result.alphabet_size,
        "correct":t.result.correct,"erasures":t.result.erasures,
        "elapsed_seconds":t.result.elapsed_seconds,"evidence_class":t.result.evidence_class},
      "leakage_checks":list(t.leakage_checks)}
    return json.dumps(obj,sort_keys=True,separators=(",",":")).encode()

def transcript_sha256(t):
    errors=validate_transcript(t)
    if errors: raise ValueError(";".join(errors))
    return hashlib.sha256(canonical_transcript_bytes(t)).hexdigest()

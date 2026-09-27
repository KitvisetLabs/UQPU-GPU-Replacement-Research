"""SCM-3A session authentication primitives.

Protocol plumbing only. A valid transcript proves internal commitment integrity,
not the identity or metaphysical nature of a sender.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,hmac,secrets

def digest(session_id:str, nonce:str, symbol:str, salt:str)->str:
    msg="\0".join((session_id,nonce,symbol,salt)).encode()
    return hashlib.sha256(msg).hexdigest()

@dataclass(frozen=True)
class SessionChallenge:
    session_id:str; nonce:str; target_commitment:str

def create_challenge(session_id:str,target_symbol:str,salt:str,nonce:str|None=None):
    n=nonce or secrets.token_hex(16)
    return SessionChallenge(session_id,n,digest(session_id,n,target_symbol,salt))

def verify_reveal(c:SessionChallenge,target_symbol:str,salt:str)->bool:
    return hmac.compare_digest(c.target_commitment,digest(c.session_id,c.nonce,target_symbol,salt))

def validate_unique_nonces(challenges)->tuple[str,...]:
    seen=set(); errors=[]
    for c in challenges:
        key=(c.session_id,c.nonce)
        if key in seen: errors.append(f"replay:{c.session_id}:{c.nonce}")
        seen.add(key)
    return tuple(errors)

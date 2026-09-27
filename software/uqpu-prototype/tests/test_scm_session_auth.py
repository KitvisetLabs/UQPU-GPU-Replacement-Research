from uqpu.scm_session_auth import *

def test_reveal_and_tamper():
    c=create_challenge("s1","B","salt","nonce-1")
    assert verify_reveal(c,"B","salt")
    assert not verify_reveal(c,"A","salt")

def test_replay_nonce_detected():
    a=create_challenge("s1","A","x","n")
    b=create_challenge("s1","B","y","n")
    assert validate_unique_nonces([a,b])

def test_same_nonce_different_session_not_replay():
    a=create_challenge("s1","A","x","n")
    b=create_challenge("s2","A","x","n")
    assert validate_unique_nonces([a,b])==()

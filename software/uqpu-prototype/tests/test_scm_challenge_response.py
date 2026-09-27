from uqpu.scm_challenge_response import (
    RevealedTrial,
    commit_challenge,
    freeze_response,
    score_exact_trials,
    verify_reveal,
)


def _trial(target="B", response="B"):
    return RevealedTrial(
        trial_id="trial-1",
        target=target,
        target_salt="t" * 32,
        scoring_rule="exact-match-v1",
        scoring_salt="s" * 32,
        response=response,
        response_salt="r" * 32,
    )


def test_commit_freeze_reveal_roundtrip():
    t = _trial()
    c = commit_challenge(t.trial_id, t.target, t.target_salt, t.scoring_rule, t.scoring_salt)
    f = freeze_response(t.trial_id, t.response, t.response_salt)
    assert verify_reveal(c, f, t)


def test_tampering_fails_verification():
    t = _trial()
    c = commit_challenge(t.trial_id, t.target, t.target_salt, t.scoring_rule, t.scoring_salt)
    f = freeze_response(t.trial_id, t.response, t.response_salt)
    changed = RevealedTrial(**{**t.__dict__, "target": "C"})
    assert not verify_reveal(c, f, changed)


def test_exact_scoring_reports_zero_bits_at_chance():
    labels = ("A", "B", "C", "D")
    trials = tuple(
        RevealedTrial(str(i), labels[i % 4], "t"*32, "exact-match-v1", "s"*32,
                      labels[(i // 4) % 4], "r"*32)
        for i in range(16)
    )
    summary = score_exact_trials(trials, labels)
    assert summary.exact_hits == 4
    assert summary.verified_bits == 0.0
    assert summary.evidence_class == "PROTOCOL_ONLY_NO_SOURCE_CLAIM"


def test_all_correct_has_positive_descriptive_information_credit():
    labels = ("A", "B", "C", "D")
    trials = tuple(
        RevealedTrial(str(i), labels[i % 4], "t"*32, "exact-match-v1", "s"*32,
                      labels[i % 4], "r"*32)
        for i in range(20)
    )
    assert score_exact_trials(trials, labels).verified_bits > 0

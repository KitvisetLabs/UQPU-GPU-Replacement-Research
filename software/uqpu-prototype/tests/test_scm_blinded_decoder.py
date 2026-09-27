from uqpu.scm_blinded_decoder import commitment, score_trials, simulate_noise_decoder


LABELS = ("voice-A", "voice-B", "voice-C", "none")


def test_commitment_is_stable_and_salt_sensitive():
    assert commitment("target", "salt") == commitment("target", "salt")
    assert commitment("target", "salt") != commitment("target", "other")


def test_null_decoder_stays_near_chance_at_scale():
    trials = simulate_noise_decoder(LABELS, trials=20_000, seed=13)
    summary = score_trials(trials, LABELS)
    assert summary.evidence_class == "MODEL_ONLY_BLINDED_CONTROL"
    assert abs(summary.excess_over_chance) < 0.02


def test_priming_bias_does_not_create_target_information():
    trials = simulate_noise_decoder(
        LABELS, trials=20_000, priming_strength=0.8, seed=17
    )
    summary = score_trials(trials, LABELS)
    assert abs(summary.excess_over_chance) < 0.02
    assert sum(t.primed for t in trials) > 10_000


def test_rejects_undeclared_response():
    from uqpu.scm_blinded_decoder import BlindedTrial
    try:
        score_trials((BlindedTrial("x", "voice-A", "unknown"),), LABELS)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")

from uqpu.scm_null_characterization import (
    DEFAULT_CHANNELS,
    SensorChannel,
    gaussian_two_sided_tail,
    simulate_null_run,
)


def test_gaussian_tail_is_small_at_four_sigma():
    p = gaussian_two_sided_tail(4.0)
    assert 0 < p < 0.0001


def test_synthetic_null_is_deterministic_and_labeled_model_only():
    a = simulate_null_run(DEFAULT_CHANNELS, samples=5000, seed=7)
    b = simulate_null_run(DEFAULT_CHANNELS, samples=5000, seed=7)
    assert a == b
    assert a.evidence_class == "MODEL_ONLY_SYNTHETIC_CONTROL"
    assert a.injected_events > 0


def test_common_mode_interference_can_create_false_coincidences():
    clean = simulate_null_run(
        DEFAULT_CHANNELS,
        samples=20_000,
        interference_probability=0.0,
        seed=11,
    )
    contaminated = simulate_null_run(
        DEFAULT_CHANNELS,
        samples=20_000,
        interference_probability=0.01,
        seed=11,
    )
    assert contaminated.coincidence_exceedances > clean.coincidence_exceedances


def test_rejects_invalid_sigma():
    try:
        simulate_null_run((SensorChannel("bad", 0.0),), samples=1)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")

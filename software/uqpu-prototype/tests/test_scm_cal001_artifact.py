from uqpu.scm_cal001_artifact import build_cal001_artifact

def test_artifact_is_deterministic_and_labeled_synthetic():
    a,ha=build_cal001_artifact(samples=5000,seed=9)
    b,hb=build_cal001_artifact(samples=5000,seed=9)
    assert a==b and ha==hb
    assert a["evidence_class"]=="SYNTHETIC_PIPELINE_VALIDATION_ONLY"

def test_known_interference_increases_multimodal_coincidences():
    a,_=build_cal001_artifact(samples=20000,seed=11)
    assert a["known_interference"]["coincidence_exceedances"] > a["control"]["coincidence_exceedances"]

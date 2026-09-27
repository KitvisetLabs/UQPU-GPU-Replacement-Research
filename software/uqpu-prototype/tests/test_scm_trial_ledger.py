from uqpu.scm_trial_ledger import CalibrationRecord, TrialRecord, sha256_bytes, validate_trial

CAL=(CalibrationRecord("cal-1","rf-1","reference injection","1 mV","2026-09-28T00:00:00Z","calibration-operator"),)

def test_valid_synthetic_ledger_record():
    t=TrialRecord("trial-1","control",sha256_bytes(b"synthetic"),("cal-1",),False,evidence_class="SYNTHETIC_FIXTURE")
    assert validate_trial(t,CAL)==()

def test_unknown_calibration_blocks_record():
    t=TrialRecord("trial-1","control",sha256_bytes(b"x"),("missing",),False)
    assert "unknown_calibration:missing" in validate_trial(t,CAL)

def test_exclusion_requires_reason():
    t=TrialRecord("trial-1","known-interference",sha256_bytes(b"x"),("cal-1",),True)
    assert "missing:exclusion_reason" in validate_trial(t,CAL)

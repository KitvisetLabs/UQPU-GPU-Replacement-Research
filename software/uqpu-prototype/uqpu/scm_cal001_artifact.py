"""SCM-P2-CAL-001 frozen synthetic benchmark artifact.

Builds a deterministic, hashable artifact from SCM-GATE-001. This validates
analysis/reproducibility plumbing only; it is not empirical sensor evidence.
"""
from __future__ import annotations
import hashlib, json
from .scm_null_characterization import DEFAULT_CHANNELS, simulate_null_run

def build_cal001_artifact(*, samples=50000, seed=20260928):
    clean=simulate_null_run(DEFAULT_CHANNELS,samples=samples,seed=seed,interference_probability=0.0)
    injected=simulate_null_run(DEFAULT_CHANNELS,samples=samples,seed=seed,interference_probability=0.01)
    payload={
      "study_id":"SCM-P2-CAL-001-SYNTHETIC",
      "evidence_class":"SYNTHETIC_PIPELINE_VALIDATION_ONLY",
      "seed":seed,"samples_per_condition":samples,
      "threshold_sigma":clean.threshold_sigma,
      "channels":[c.name for c in DEFAULT_CHANNELS],
      "control":{"coincidence_exceedances":clean.coincidence_exceedances,
                 "channel_exceedances":clean.channel_exceedances},
      "known_interference":{"coincidence_exceedances":injected.coincidence_exceedances,
                 "channel_exceedances":injected.channel_exceedances,
                 "injected_events":injected.injected_events},
    }
    raw=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    return payload, hashlib.sha256(raw).hexdigest()

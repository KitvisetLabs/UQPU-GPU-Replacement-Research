# Eight-Lane Batch 009 — Reference Certificates and QUBO Routing

Batch 009 enforces that execution success is not output-quality success.

A tier artifact now defaults to `accepted=false` unless a matching reference certificate is supplied.

Reference kinds:
- EXACT_OPTIMUM — can verify quality.
- PROVEN_LOWER_BOUND — can verify a minimization gap.
- BEST_KNOWN_FEASIBLE — comparison only; cannot certify the true gap by itself.

Every certificate has contract ID, method, evidence level, source/provenance and a stable certificate ID.

The benchmark QUBO can now be serialized to:
- `uqpu-qubo-v1` provider-neutral form;
- the `{"Q": ...}` convention consumed by the UQPU D-Wave adapter.

This closes part of the software path from Lane A workload generation into Lane B annealing execution without claiming universal provider-native compatibility.

Next gate: generate defensible reference certificates for small/medium tiers, then carry the same contract through simulator or authorized cloud execution.

No quantum advantage or >=100x result is claimed.

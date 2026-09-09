# UQPU Software Prototype v0.2

Executable research software for the UQPU project.

## Current capabilities

- semantic workload IR
- explicit result contracts
- quantum-native backend estimator
- reversible deterministic fallback estimator
- end-to-end cost model
- semantic compiler/backend selection
- benchmark classification and 100×–100M× cost tiers
- JSON workload input
- CLI
- unit tests

## Important scientific status

All resource and cost numbers in this prototype are currently **MODEL_ONLY** placeholders used to exercise the architecture. They are **not predictions of existing quantum hardware** and must not be cited as demonstrated quantum advantage.

The model deliberately includes state preparation, QEC, measurement, decoding, energy and I/O so future calibrated models cannot silently omit these costs.

## Run

```bash
python -m unittest discover -s tests -v
python -m uqpu.cli demo
python -m uqpu.cli compile examples/search_workload.json
```

## Development direction

Next versions should replace heuristic backend models with literature-backed resource estimators, calibrated QEC models, measured GPU baselines, and provider-specific QPU parameters.

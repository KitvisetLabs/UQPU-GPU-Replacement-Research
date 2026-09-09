# UQPU Software Prototype v0.3

Executable research software for the UQPU project.

## Current capabilities

- semantic workload IR
- explicit result contracts
- quantum-native backend estimator
- reversible deterministic fallback estimator
- end-to-end UQPU cost model
- semantic compiler/backend selection
- benchmark classification and 100×–100M× cost tiers
- configurable quantum hardware profiles
- generic GPU hardware/economic profiles
- phenomenological surface-code QEC estimator
- GPU cost-per-task baseline model
- sensitivity sweeps
- target solver for 100× through 100,000,000×
- JSON workload input
- CLI
- unit tests
- GitHub Actions CI

## Scientific status

All resource, QEC, hardware and cost numbers remain **MODEL_ONLY** unless explicitly replaced by calibrated literature or measured data.

The reference profiles under `profiles/` are deliberately generic and must not be cited as vendor specifications.

## Cost target solver

For a measured GPU baseline cost (C_G) and desired advantage (A):

[
C_{UQPU,max} = C_G / A
]

The prototype provides target levels:

- 100×
- 1,000×
- 10,000×
- 100,000×
- 1,000,000×
- 10,000,000×
- 100,000,000×

## QEC model

`uqpu.qec.SurfaceCodeEstimator` currently uses a transparent phenomenological model to estimate:

- code distance
- logical error/cycle
- physical qubits/logical qubit
- total physical qubits
- QEC runtime

This is an architecture/sensitivity tool, not a provider-specific prediction.

## Run

```bash
python -m unittest discover -s tests -v
python -m uqpu.cli demo
python -m uqpu.cli compile examples/search_workload.json
```

## Development direction

Next versions should add literature-backed algorithm estimators, uncertainty distributions, real GPU benchmark ingestion, provider-specific experimental profiles, and automated inverse design that searches hardware parameters required to meet a selected cost-supremacy tier.

# Inverse Hardware Design for UQCS

## Purpose

Convert the economic target into hardware requirements.

Forward design asks:

> What does this architecture cost?

Inverse design asks:

> If the architecture must be 100×, 1M× or 100M× cheaper per useful task, what must the hardware be capable of?

## Pipeline

```text
Measured conventional cost/task
        |
        v
Target advantage tier
        |
        v
Maximum UQCS cost/task
        |
        v
Subsystem budgets
 compute / memory / storage / fabric / control-QEC / operations
        |
        v
Derived constraints
 power / bandwidth / yield / loss / utilization / QEC resources
```

## Current implementation

The software now derives MODEL_ONLY monotonic target constraints for:

- maximum subsystem cost/task
- minimum utilization
- maximum operating power
- minimum effective bandwidth
- maximum photonic loss
- minimum fabrication yield
- maximum QEC runtime
- maximum physical-qubit budget
- maximum non-Clifford-operation budget
- detector/source/switch performance targets

These are architecture-search constraints, not claims about existing hardware.

## Research use

If the derived requirements are physically unrealistic, that is useful evidence that:

- the workload is not suitable for the target tier;
- the architecture needs a new algorithm;
- data movement/materialization must be reduced;
- a different quantum modality may be needed;
- the target tier is not feasible for that workload.

## Next steps

- replace heuristic exponents with literature-calibrated models;
- couple requirements to real cloud-QPU pricing;
- add fabrication/yield economics;
- add memory bandwidth/energy calibration;
- add uncertainty intervals;
- add automatic modality search across superconducting, trapped-ion, neutral-atom, photonic and annealing architectures.

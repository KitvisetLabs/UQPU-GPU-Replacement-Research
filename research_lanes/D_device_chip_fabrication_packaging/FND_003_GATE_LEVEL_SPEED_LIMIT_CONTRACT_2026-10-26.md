# FND-003 gate-level quantum speed-limit measurement contract

**Date:** 2026-10-26  
**Primary owner:** Lane D — device/control/calibration  
**Consumers:** A, B, C, F and G; publication/integration: H  
**Evidence class:** literature-only inputs + software schema/unit tests  
**Status:** protocol/tooling advance; no physical timing measurement

## Purpose

Extend the existing FND-003 matched-control measurement program with a gate-/operator-specific record. The recent APS accepted-paper records for Nelson & Barnes (accepted 2026-10-15, DOI 10.1103/28zn-ch8y) and Stepanenko et al. (accepted 2026-10-21, DOI 10.1103/rsjw-pk53) motivate this scope, but their full theorem statements and derivations must be independently checked before implementation of a numerical bound.

## Contract

Primary implementation: `software/uqpu-prototype/uqpu/gate_speed_limit_contract.py`. Tests: `software/uqpu-prototype/tests/test_gate_speed_limit_contract.py`.

Each record binds:
- exact theorem reference and theorem-source SHA-256;
- a separate bound-derivation SHA-256;
- target gate/unitary, Hamiltonian model, target identity and calibration SHA-256;
- target kind and evidence level;
- observed duration and uncertainty, lower bound and uncertainty (all in seconds);
- repeat count, observation method and explicit scope checks for bounded spectral width, gate identity, initial/final operator, control boundary, noise/environment and calibration validity.

The module validates record completeness, compares uncertainty intervals and exposes `assert_matches_schedule()` so Lane A cannot reuse a record with a different gate/unitary, target kind, Hamiltonian model or calibration. It deliberately does **not** calculate a theorem bound from incomplete literature, assert that a bound is physically correct, or promote a result to new physics.

### Result semantics

- `CONSISTENT_WITH_BOUND_INTERVAL`: intervals are separated in the expected order; this is not proof that the gate is optimal.
- `OVERLAPPING_UNCERTAINTY_INTERVALS`: the available uncertainty does not distinguish the intervals.
- `BELOW_BOUND_REQUIRES_THEOREM_AND_METROLOGY_AUDIT`: stop and audit theorem scope, source version, Hamiltonian bandwidth, target identity, timing boundary, calibration and uncertainty. This label is not a law-violation claim.

Hardware-target records require a provider job ID and `LAB_RESULT` or `PUBLISHED_EXPERIMENT` evidence. Simulator records cannot be labeled as lab evidence. This is a record-validation rule, not authorization to submit a paid job.

## Reproduction

From `software/uqpu-prototype/`:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_gate_speed_limit_contract.py' -v
```

The isolated local harness passed 14/14 focused tests on 2026-10-26, including exact compiler-schedule identity matching and mismatched-target rejection. Hosted CI on the latest source head is required before this is considered repository-validated.

## Cross-lane interfaces

- **A:** pass the frozen unitary identity and keep gate time distinct from full-circuit makespan and accepted-task latency.
- **B:** bind any later device record to the exact provider target and receipt; this cycle made no provider call.
- **C:** preserve host, state, output and transfer accounting; no storage equivalence is implied.
- **D/G:** use validated gate/control requirements only after target-aware scheduling and calibration; no fabrication result is produced.
- **E:** no direct evidence change for biomass carbon, bio-oil, fusion electricity or cooling.
- **F:** require same-workload baseline, measurement uncertainty, energy and total cost per accepted useful task before economic interpretation.
- **H:** preserve the multilingual strategy and publish the next gate; no capital or WACC authorization.
- **FND/EQN:** present physical constraints remain binding; any apparent discrepancy must be falsifiable and independently replicated.

## Next gate

Obtain the full accepted-paper theorem, independently implement its assumptions and small-system examples, freeze matched target/control settings, then collect repeated timing/uncertainty data only under appropriate authorization. No QPU execution, hardware measurement, new physical law, cost advantage or mission-level result is claimed in this cycle.

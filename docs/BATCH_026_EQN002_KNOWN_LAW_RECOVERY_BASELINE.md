# Batch 026 — EQN-002 Known-Law Recovery Baseline

**Date:** 2026-09-10  
**Program:** INV-035 / EQN-002  
**Evidence:** MODEL_ONLY + EXECUTABLE SOFTWARE BASELINE  
**REAL_QPU:** No  
**New physical law:** No

## Purpose

Before using AI to search for unknown physics, calibrate the discovery workflow on equations whose structure is already known but hidden from the search routine.

A discovery engine that cannot reliably rediscover known laws under held-out testing and physics constraints should not be trusted to propose unknown laws.

## First benchmark

`software/uqpu-prototype/uqpu/equation_recovery_benchmark.py` implements a deterministic scalar power-law baseline:

`y ~= c * x^p`

For each candidate integer power, the code fits coefficient `c` only on the training subset and selects a model using a disjoint holdout subset. An optional dimensional gate can eliminate candidates before ranking.

The initial hidden-law calibration uses fixed-mass kinetic-energy data generated from the known relation

`E = 0.5 * m * v^2`

while the recovery routine is offered candidate velocity powers `p = 1,2,3,4`.

With the coefficient permitted to carry mass dimension only, dimensional analysis requires the velocity exponent to be `p=2` in order to match the energy dimension `(M^1 L^2 T^-2)`.

The executable test verifies that the benchmark recovers:

- selected power: `2`;
- coefficient for `m=3`: `1.5`;
- zero held-out RMSE on the noiseless fixture;
- only power `2` survives the stated dimensional gate.

This is deliberately easy. It calibrates infrastructure rather than demonstrating scientific novelty.

## Why held-out evidence is mandatory

A formula can fit its training data while failing outside the fitted region. Therefore the permanent equation-discovery program treats training fit as insufficient. Candidate comparison must preserve a hidden/held-out regime or another genuinely independent predictive test.

Future versions will add noise, parameter identifiability, wider candidate grammars, differential equations, symmetry/conservation constraints and extrapolation outside the training domain.

## Important negative case

The test suite also demonstrates that a physics constraint can force selection of a candidate with worse numerical fit when the numerically best expression violates the declared dimensional search space. This is intentional: the project distinguishes

`best curve fit`

from

`best admissible physical candidate under stated assumptions`.

The assumptions themselves may later be challenged, but only through INV-035's explicit new-equation falsification process.

## Next EQN-002 gates

1. add noisy hidden-law fixtures and report structure-recovery probability;
2. add unit-consistent competing expressions rather than letting dimensions solve the entire fixture;
3. score complexity/parsimony separately from error;
4. include extrapolation beyond the training interval;
5. add at least one ODE/PDE recovery fixture;
6. compare a conventional enumerative symbolic baseline against an AI-assisted generator under the same expression/evaluation budget;
7. report false-discovery rate, not only successful rediscovery.

## Mission relevance

This work does not relax any current physical limit. It creates the measurement discipline needed if future AI proposes a relation that appears to improve QPU control, materials, fusion, bio-oil, thermal transport or another North-Star bottleneck.

No quantum advantage, new fundamental law, 100x/100,000,000x advantage or Data-Center-to-Phone feasibility is demonstrated.
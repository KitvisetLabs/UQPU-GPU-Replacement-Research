# Research gap — FND-003 Planckian thermalization bound mapping

**Date opened:** 2026-10-26  
**Status:** OPEN — theorem mapped to scoped helpers; no matched physical experiment  
**Primary owner:** Lane F — evidence, benchmark and integration  
**Implementation owner:** Lane A — fundamental-limit helper and tests  
**Publication owner:** Lane H — literature provenance  
**Related:** FND-001, FND-003, FND-006, EQN-001–006, INV-034/035  
**Literature watch:** docs/literature_watch/2026-10-26-planckian-thermalization-bound-fnd003.md

## Objective

Determine whether a workload in this project actually satisfies the assumptions of the universal-thermalization task studied by Abiuso et al. before using the published theoretical lower bound in any performance comparison.

## Known

- The peer-reviewed paper “An information-theoretic proof of the Planckian bound for thermalization,” Nature Physics, version of record 2026-09-24, DOI 10.1038/s41567-026-03397-y, proves a bound for a fixed thermalization machine required to produce states close to Gibbs states for multiple possible Hamiltonians.
- In a sufficiently mixed finite-temperature regime, with the stated small-error condition, the bound approaches tau >= hbar/(2 k_B T). In the low-temperature, gap-dominated regime, the asymptotic scale is tau >= hbar/Delta.
- The executable helpers and unit tests were added to fundamental_limits.py and test_fundamental_limits_and_frontier.py. They encode only these scoped expressions and reject non-positive/non-finite inputs.
- This result is a theoretical lower bound. It is not an experimental timing result, an arbitrary gate-time limit, or an economic measurement.

## Blocking unknowns

- No UQPU workload currently declares the required universal family of Hamiltonians, a common fixed routine, thermal-state error tolerance and state-distance metric as an accepted-output contract.
- No independent formal reconstruction of the paper's proof has been performed by this repository.
- No thermalization device, matched control, calibrated timing, physical energy, heat, or cost per accepted task was measured.
- A single known-Hamiltonian state-preparation task may not satisfy the theorem's universal-task premise and must not inherit this bound automatically.

## Unlock criteria

1. Freeze a candidate workload and a hash-addressed family of Hamiltonians, temperature, spectral-gap regime, initial-state contract, error tolerance and acceptance metric.
2. Independently derive the code expressions from the publisher's theorem and verify units, limiting regimes and constants.
3. Compare at least two methods on identical Hamiltonian families and accuracy gates; include all setup, control, reset, readout and reconstruction time.
4. Record calibration uncertainty, failed runs, retries, total physical energy where measurable, and the matched control's complete resource boundary.
5. Hold out Hamiltonians and require independent replication. Report the theoretical bound, measured duration and measured economics as separate quantities.

## Falsification / stop rules

- If the workload does not require one fixed routine to thermalize multiple possible Hamiltonians, mark the bound NOT_APPLICABLE to that task.
- If the mixed-state or low-temperature regime assumptions are not satisfied, do not use the corresponding simplified expression; evaluate the full theorem only if its other conditions are established.
- If the timing comparison changes task quality, Hamiltonian family or output-error tolerance, reject the comparison as unmatched.
- If the measured duration appears below the theoretical bound, audit assumptions, state-distance/error definitions, Hamiltonian range and timing calibration before making any physics claim.
- A theoretical lower bound alone cannot establish an achievable runtime, energy saving, quantum advantage or mission-level benefit.

## Mission boundary

This gap does not close INV-029 through INV-033. No phone-class physical compression, Pangola material substitution, accepted biomass liquid fuel, net reliable fusion electricity, financing-principal reduction or WACC effect is demonstrated. It advances INV-034/035 only by turning a published theorem into a narrowly scoped, falsifiable research interface.

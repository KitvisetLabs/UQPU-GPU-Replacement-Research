# Literature watch — 2026-10-26: information-theoretic Planckian bound for universal thermalization

**Source date:** published 2026-09-24  
**Primary owner:** Lane H — research publication and strategic context  
**Technical owner:** Lane A — fundamental-limit helpers and workload semantics  
**Evidence owner:** Lane F — assumption audit, benchmark and evidence boundary  
**Feeds:** FND-001, FND-003, FND-006, EQN-001–006, INV-034/035  
**Evidence class:** PEER-REVIEWED THEORETICAL LOWER BOUND  
**UQPU physical or economic evidence promoted:** none

## Source and precise result

Paolo Abiuso, Alberto Rolandi, John Calsamiglia, Pavel Sekatski and Martí Perarnau-Llobet, “An information-theoretic proof of the Planckian bound for thermalization,” *Nature Physics* (version of record 2026-09-24), DOI https://doi.org/10.1038/s41567-026-03397-y. Official publisher page: https://www.nature.com/articles/s41567-026-03397-y.

The authors formulate a **universal thermalization machine**: one fixed routine must bring a system close to its Gibbs state for multiple possible Hamiltonians. Assuming the system plus machine/environment follows quantum mechanics, they use state distinguishability and quantum-information geometry to derive a lower bound. In a sufficiently mixed finite-temperature regime, with sufficiently small output error, the bound approaches

\[
\tau \ge \frac{\hbar}{2 k_B T}.
\]

In the low-temperature regime where the spectral gap \(\Delta\) dominates, the paper gives the asymptotic scale

\[
\tau \ge \frac{\hbar}{\Delta}.
\]

The full result is parameterized by the range of Hamiltonians and the tolerated thermalization error. Those details are part of the theorem, not optional caveats.

## Genuine novelty and limitations

The contribution is a model-independent, information-theoretic lower bound for a **multi-Hamiltonian thermalization task**, rather than a claim about one specific material or bath. The proof connects distinguishability of different Gibbs states to how quickly the same machine's output can respond to changes in the system Hamiltonian.

This is not a universal minimum time for every computation, gate, QAOA circuit, or state-preparation task. The paper explicitly distinguishes thermalizing across multiple possible Hamiltonians from preparing a single known thermal state with a task-specific routine. Its theorem is theoretical; this UQPU cycle did not reproduce the paper's proof independently or measure a thermalization device. It does not establish a new physical law beyond the quantum-mechanical assumptions used in the derivation.

## Exact UQPU relevance

- **FND-003 — matched control versus quantum-speed-limit measurement:** this is a candidate *theoretical reference bound* for a narrowly defined thermalization workload. It does not close the required matched experimental comparison.
- **FND-001 — thermodynamic-gap accounting:** it can inform the time/accuracy side of a thermalization subtask, but does not convert entropy differences into work, heat or joules.
- **Lane A:** if a UQPU workload ever requires one routine to thermalize a declared family of Hamiltonians, encode that family, temperature, spectral-gap regime, tolerated output error and accepted-output predicate in the workload contract before applying the bound.
- **Lane C:** quantum state-space dimension is not readable classical memory. The bound supplies no byte count, storage capacity or memory-transfer advantage.
- **Lane F:** keep theoretical lower-bound time separate from measured latency, energy, billable usage and cost per accepted useful task.
- **Lanes D/G:** no device, process, packaging or manufacturing implication is established without a validated physical implementation.
- **Lanes E/H:** no biomass, material, fusion, financing, valuation or WACC conclusion follows from this theorem.

## Executable mapping added in this cycle

software/uqpu-prototype/uqpu/fundamental_limits.py now contains two narrowly scoped helpers:
- planckian_thermalization_min_seconds(T) returns \(\hbar/(2k_BT)\) for the stated mixed-state universal-thermalizer regime.
- low_temperature_gap_thermalization_min_seconds(Delta) returns \(\hbar/\Delta\) for the stated low-temperature, gap-dominated regime.

Unit tests cover the formulas, inverse-temperature scaling, and invalid inputs. The helpers' docstrings explicitly reject generic gate-time or device-performance interpretation. Exact-head hosted CI was not observable through the available commit-status/workflow query at publication time, so CI remains UNKNOWN until a workflow result is tied to the final commit.

## Falsifiable follow-up — FND003-THERMALIZATION-BOUND-001

1. Freeze a task that requires the *same* routine to thermalize a declared set of distinct Hamiltonians, with explicit temperature, gap, output-error tolerance and state-distance metric.
2. Verify the theorem-to-code expressions independently from the publisher's equations and test the mixed and low-temperature regimes separately.
3. Record the Hamiltonian-family hash, initial states, control protocol, calibration, timing uncertainty, thermal-state error, retries and total resource use. Compare the observed duration to the applicable bound only when every theorem assumption is met.
4. Use a matched control that performs the same accepted task and accuracy requirement. Report total energy and cost separately; do not infer them from the time bound.
5. Hold out Hamiltonians and independently reproduce the analysis. If the task is only preparation of one known state, the universal-thermalizer bound is **not applicable**. If a measured apparent violation occurs, audit task definition, error metric, Hamiltonian range and assumptions before treating it as a challenge to quantum mechanics.

## Non-claims

No UQPU workload was benchmarked against this bound in this cycle. No gate-depth improvement, QPU speedup, energy saving, new physical law, Data-Center-to-Phone compression, critical-material substitution, accepted biomass liquid fuel, net fusion electricity, lower project principal/interest or lower WACC is demonstrated.

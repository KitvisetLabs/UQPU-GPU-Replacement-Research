# FND-003 — Control Energy / Quantum-Speed-Limit Measurement Contract

**Owner:** Lane D — Devices / Chip / Fabrication / Packaging  
**Upstream foundation:** INV-034 / FND-003  
**Consumers:** A, B, C, F, G and the Data-Center-to-One-Phone integration path

## Purpose

Batch 023 established that an instruction duration by itself is insufficient to quantify a physical distance from a Margolus–Levitin or other quantum-speed-limit bound. This contract defines the minimum matched evidence needed before a numerical `observed/control time ÷ fundamental bound` ratio may be published as a physical result.

## Required identity

Every record must identify:

- provider / device / backend and calibration timestamp;
- operation or complete state-transfer experiment;
- physical qubit(s) / mode(s) and layout;
- initial state, target/final state and distinguishability or fidelity criterion;
- pulse/control schedule and observed physical duration with uncertainty;
- Hamiltonian/model version and provenance;
- theorem/bound being invoked and its assumptions.

## Intrinsic quantum-system energy

For the standard orthogonal-state Margolus–Levitin expression, the record must provide a defensible mean energy above the ground state for the **same physical evolution**. Required fields include:

- definition of the ground-state energy reference;
- method used to obtain the expectation/mean energy;
- whether the Hamiltonian is time-independent over the compared evolution;
- uncertainty/error interval;
- source: direct measurement, calibrated model, tomography/inference, or other method;
- justification that the chosen quantum-speed-limit formula applies.

If the control Hamiltonian is time-dependent or the evolution does not meet the orthogonal-state assumptions, use an appropriate generalized speed-limit theorem rather than forcing the standard ML expression.

## External engineering energy is separate

The intrinsic energy quantity used by a quantum-speed-limit theorem must not be confused with economic energy consumption. Record separately where measurable:

- arbitrary-waveform / microwave / laser / RF control energy;
- room-temperature electronics;
- amplifiers, DAC/ADC, FPGA and classical orchestration;
- cryogenic refrigeration and thermal-management power;
- readout chain;
- network/host compute;
- wall-plug energy per accepted useful result.

A low intrinsic quantum-system energy does not imply low wall-plug energy.

## Timing boundary

Do not sum instruction durations and call the result wall-clock latency when scheduling allows parallel operations. A valid timing comparison needs the scheduled critical path or measured start-to-finish duration for the same experiment.

## Evidence levels

- saved duration only: `CALIBRATION_SNAPSHOT_DERIVED_BOUND`; no physical QSL gap;
- matched Hamiltonian/energy + timing model: `DEVICE_MODEL` unless directly measured;
- matched laboratory timing + energy evidence: `LAB_RESULT`;
- published/reproduced experiment: `PUBLISHED_EXPERIMENT` as applicable.

No evidence level by itself establishes engineering speedup or economic advantage. Those require the normal useful-output and total-cost gates.

## Falsification / negative-result rule

If the correct energy quantity cannot be measured or the theorem assumptions cannot be justified, publish the gap as **not identifiable from available evidence** rather than substituting qubit resonance, pulse-generator power, gate duration, or wall-plug power into the theorem.

## Next experiment

Select one backend/control stack for which pulse schedule, state evolution and Hamiltonian/energy provenance are accessible. Freeze a single operation/state-transfer contract, collect the matched fields above, compute uncertainty-aware physical bounds, then pass the result to Lane F for full control/cryo/wall-plug economics.

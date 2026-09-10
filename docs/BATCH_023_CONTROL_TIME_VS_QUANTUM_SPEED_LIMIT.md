# Batch 023 — Control Time vs Quantum Speed Limit

**Date:** 2026-09-10  
**Primary foundation:** INV-034 / FND-003  
**Evidence:** CALIBRATION_SNAPSHOT_DERIVED_BOUND + CI_MEASURED SOFTWARE  
**REAL_QPU:** No  
**Paid QPU job:** No

## Research question

Can the instruction durations extracted from the saved IBM `FakeKingston` target snapshot be used to measure how far the current routed QAOA control stack is from the Margolus–Levitin (ML) quantum speed limit?

## Result — the direct gap is not measurable from duration alone

**No.** The saved target exposes calibrated instruction durations, but it does not provide the mean energy above the ground state for the same physical evolution in the form required by the standard orthogonal-state Margolus–Levitin expression.

Therefore this batch does **not** report `observed gate time / quantum speed limit` as a physical speedup opportunity. Doing so from gate duration alone would manufacture an unsupported denominator.

Instead the executable diagnostic in `uqpu/control_limit_gap.py` computes only the inverse question:

> What mean energy above ground would make the ideal orthogonal-state ML lower bound equal to the recorded instruction duration?

For the standard ML expression

`tau >= h / (4 E)`

this inverse diagnostic is

`E_required(tau) = h / (4 tau)`.

It is a mathematical reference scale, **not** measured device energy, pulse energy, qubit frequency, Rabi rate, control power or wall-plug energy.

## CI evidence

GitHub Actions run **34458341082** completed successfully after adding the diagnostic. Python 3.12 reported **206 tests passed, 4 skipped**; Python 3.10/3.11, independent Qiskit verification, reference benchmark and target-snapshot-noise jobs also completed successfully.

The target snapshot used `generic_backend_120q_fake_kingston_v2` / `fake_kingston`.

### Triangle fixture

Active physical qubits: `108, 109, 110`.

Included positive-duration unitary instructions:

| operation | count | snapshot duration | inverse ML E_required | E_required / h |
|---|---:|---:|---:|---:|
| sx | 21 | 32 ns | 5.1766173046875e-27 J | 7.8125 MHz |
| x | 1 | 32 ns | 5.1766173046875e-27 J | 7.8125 MHz |
| cz | 9 | 68 ns | 2.4364228492647058e-27 J | 3.676470588235294 MHz |

31 unitary instruction instances were included. Three measurements and 42 virtual `rz` instances were excluded. The serial sum of included durations is `1.316 us`; **this is not circuit wall-clock latency**, because operations can execute in parallel.

### ER6 fixture

Active physical qubits: `69, 68, 67, 66, 65, 64`.

| operation | count | snapshot duration | inverse ML E_required | E_required / h |
|---|---:|---:|---:|---:|
| sx | 36 | 32 ns | 5.1766173046875e-27 J | 7.8125 MHz |
| cz | 26 | 68 ns | 2.4364228492647058e-27 J | 3.676470588235294 MHz |

62 unitary instruction instances were included. Six measurements and 324 virtual `rz` instances were excluded. The serial duration sum is `2.92 us`, again explicitly **not** wall-clock circuit latency.

## Why this negative result matters

FND-003 is intended to find the difference between engineering/control limits and fundamental physical limits. A large numerical ratio is useful only if its numerator and denominator describe the same physical evolution under a valid theorem.

The missing measurement is not a minor detail. For a defensible physical gap we need, at minimum:

- a specified initial state, final state and distinguishability target;
- the Hamiltonian model and its ground-state reference;
- mean energy above ground for the same evolution, with uncertainty/provenance;
- a statement of whether the standard orthogonal-state ML form applies or which more general quantum-speed-limit theorem is being used;
- pulse/control timing and parallel scheduling;
- external control, cryogenic and wall-plug energy recorded separately from intrinsic quantum-system energy.

The required measurement contract is published in `research_lanes/D_device_chip_fabrication_packaging/FND_003_CONTROL_ENERGY_MEASUREMENT_CONTRACT.md`.

## Connection to the North Star

The Data-Center-to-One-Phone mission cannot multiply an ideal quantum-speed-limit number by a circuit count and call the result an achievable phone throughput. Batch 023 establishes a stronger rule: **fundamental bounds are constraints and diagnostic references; engineering headroom must be measured with matched physical quantities.**

## Next gate

1. obtain target/pulse/Hamiltonian data sufficient to define the relevant physical evolution;
2. measure or derive the correct energy quantity with uncertainty and provenance;
3. choose the applicable speed-limit theorem;
4. compare against scheduled physical duration, not serial gate-duration sum;
5. only then compute a physical control-to-bound ratio;
6. separately carry wall-plug, cryogenic, classical-control and readout energy into economic accounting.

No quantum advantage, >=100x/100,000,000x advantage, universal subsystem replacement or Data-Center-to-Phone feasibility is demonstrated by this batch.

# Batch 145 — Quantum Processor GPU Replacement Experiment Program

**Date:** 2026-11-27  
**Work ID:** QGR-EXP-001  
**Status:** DESIGN PUBLISHED / EXPERIMENTS NOT RUN  
**Primary lane:** A — quantum programming, algorithms, compiler and runtime  
**Cross-lane interfaces:** B provider integration; C memory/data movement; D device/chip; E energy/cooling; F benchmark/evidence/economics; G manufacturing; H strategy/publication.

## Objective

Advance the long-term research target of replacing GPU compute capability with quantum processing. The target is deliberately broader than a QPU co-processor: investigate whether a quantum processor can independently execute useful workload families now assigned to GPUs, with fewer logical qubits where possible.

This is a falsifiable moonshot, not a demonstrated capability. A small register has a large mathematical state space, but its amplitudes cannot be read out as an equally large classical array. Input encoding, state preparation, oracle construction, gates, fault tolerance, shots, measurement, output reconstruction and classical support must all be counted.

## Published artifacts

- [Full experiment program](../research_lanes/A_quantum_programming_runtime/QUANTUM_GPU_REPLACEMENT_EXPERIMENT_PROGRAM_2026-11-27.md): mission, functional replacement definition, evidence classes, hypotheses H0–H7, open questions Q-001–Q-018, experiment protocols EXP-00–EXP-12, statistical design, resource accounting, decision gates G0–G9 and next-agent handoff.
- [Experiment matrix](../benchmarks/experiments/qgr-exp-001-experiment-matrix-2026-11-27.csv): machine-readable summary of all 13 experiments, candidate methods, baselines, outputs and falsifiers.
- [Preregistration JSON](../benchmarks/manifests/qgr-exp-001-preregistration-2026-11-27.json): stable work ID, hypotheses, experiment states, qubit sweep, comparison rules, gates and authorization restrictions.
- [Daily A–H integration report](../integration/DAILY_CYCLE_2026-11-27_QUANTUM_GPU_REPLACEMENT.md).
- [Machine-readable integration record](../integration/INT-20261127-QUANTUM-GPU-REPLACEMENT.json).

## Experiment portfolio

The 13 designed experiments cover semantic/exact-reference controls; optimized CPU/GPU baseline validation; ideal quantum algorithm feasibility; simulator diversity; noisy-circuit robustness; QSVT/block-encoding matrix tasks; Grover/QAOA search and optimization; amplitude estimation/Monte Carlo; AI kernel-to-whole-graph replacement; real-QPU execution; fault-tolerant physical resource estimates; complete energy/economic crossover; and held-out/adversarial generalization.

Multiple experimental forms are specified: analytic/theoretical, exact small-instance, ideal simulation, tensor-network/stabilizer where applicable, noisy simulation, compiler/resource estimation, actual QPU, measured GPU, end-to-end system measurement and independent replication.

## Key hypotheses

H1: at least one practical workload family has a matched-output end-to-end QPU advantage over a strong GPU baseline.  
H2: a small logical register can efficiently represent selected useful tasks after all encoding and readout costs.  
H3: QSVT/block encoding or quantum linear solvers can win on selected structured matrix workloads.  
H4: quantum search/optimization can improve accepted solution quality per total resource.  
H5: amplitude estimation can beat variance-reduced classical Monte Carlo for selected error/confidence targets.  
H6: quantum-native methods can replace selected AI kernels or graphs at matched quality.  
H7: algorithm/compiler/device co-design can move the full-stack resource frontier.  
H0: optimized classical systems remain superior over the tested range.

Each has explicit competing explanations and falsifiers in the full program. Negative and inconclusive results are to be retained.

## Initial execution order

1. Freeze EXP-00 semantics and EXP-01 optimized GPU baselines.
2. Select one structured matrix task for EXP-05; make input-access/oracle cost explicit.
3. Reuse the repository's existing signed-Max-Cut held-out fixtures for EXP-06; do not duplicate or alter the frozen split.
4. Design one amplitude-estimation task for EXP-07 with a known integral and variance-reduced classical comparator.
5. Run ideal/noisy simulation and target-aware resource analysis before considering real hardware.
6. Escalate to AI subgraphs and whole graphs only with matched-quality contracts.
7. Perform physical, energy and cost analysis for candidates passing earlier gates.

## Evidence and nonclaims

This batch is **RESEARCH_DESIGN / PREREGISTERED_DRAFT**, not a result. No new experiment, simulation, GPU measurement, QPU job, hardware measurement or quantum advantage was produced by this publication. Existing QSVT/QAOA artifacts are reused as starting points, not represented as proof of speedup. Logical and physical qubit counts remain separate. No free QRAM, oracle, state preparation, QEC, measurement or postprocessing is assumed.

No paid QPU job, hardware purchase or external spend is authorized. Any such action requires explicit user approval and a bounded budget.

## Next gate

Start with EXP-00 and EXP-01 contract/test harnesses, then freeze one EXP-05 workload and its exact reference. Publish measured results only with raw data, software/hardware provenance, accepted-output parity, uncertainty and the full resource boundary.

Research-Sync: main

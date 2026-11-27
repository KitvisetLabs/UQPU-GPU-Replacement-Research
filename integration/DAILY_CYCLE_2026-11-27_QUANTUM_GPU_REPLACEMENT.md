# Daily Eight-Lane Integration — 2026-11-27 — QGR-EXP-001

**Status:** DESIGN PUBLISHED / EXPERIMENTS NOT RUN  
**Primary work:** Quantum Processor GPU Replacement Experiment Program  
**Canonical main merge:** 749c0c7f9841a51f640aee35988f2745dce3d9be  
**PR:** #164 — merged  
**Evidence:** RESEARCH_DESIGN + PREREGISTERED_DRAFT; no execution evidence.

## Lane status and assignments

- **A — Quantum programming/runtime:** owns QGR-EXP-001; develop exact semantics, quantum algorithms, compiler/runtime costs and EXP-00/02/05/06/07/08.
- **B — Cloud QPU/provider integration:** remain provider-neutral and no-submit. Define target device/calibration/job metadata and provider abstraction for EXP-03/04/09. No paid jobs.
- **C — Memory/state/data movement:** quantify data encoding, state preparation, oracle access, memory traffic, output reconstruction and classical-host dependency. No free QRAM assumption.
- **D — Device/chip fabrication/packaging:** estimate topology, native gates, connectivity, control, physical/logical qubits and QEC overhead for EXP-04/09/10.
- **E — Energy/cooling/infrastructure:** define full QPU energy boundary including cryogenic/laser/control and cooling overhead; compare against GPU system energy in EXP-11. No measured energy claim.
- **F — Economics/benchmarks/evidence:** own fair GPU baseline, statistical protocol, accepted-task definition, cost per accepted task and uncertainty; maintain evidence classes and no-claim discipline.
- **G — Manufacturing:** assess manufacturability, yield, packaging, interconnect and supply constraints only after a concrete architecture/resource envelope exists.
- **H — Strategy/publication:** maintain the full GPU replacement north star while publishing workload-specific evidence without extrapolating a narrow win into universal replacement.

## Cross-lane gates

1. G0/G1: A+F freeze exact output contracts and optimized classical baselines.
2. G2/G3: A+C establish algorithm applicability and realistic input/oracle costs.
3. G4/G5: A+B+D estimate noise, mapping, logical-to-physical overhead and device feasibility.
4. G6: B coordinates real-QPU execution only after explicit authorization.
5. G7: C+E+F count complete end-to-end time, energy and cost.
6. G8/G9: A–H evaluate workload coverage before any replacement claim.

## Current evidence

The experiment program, CSV matrix and JSON preregistration are published. Existing repository QSVT and signed-Max-Cut parity-QAOA artifacts are starting references only. No new test suite, simulation, benchmark, QPU run, hardware result, GPU measurement or energy measurement was executed in this batch.

## Next actions

A: inspect existing Lane A fixtures and freeze EXP-00/01 and one EXP-05 case.  
B/D: define a provider-neutral target-resource record without submitting jobs.  
C: specify input-access and output-readout accounting for the selected matrix fixture.  
F: define benchmark run metadata, repeated-run statistics and cost/energy schema.  
E/G: prepare system-boundary and physical feasibility templates.  
H: preserve the full replacement objective and publish only evidence-supported claims.

Research-Sync: main

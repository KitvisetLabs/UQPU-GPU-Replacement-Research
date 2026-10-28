# Daily Eight-Lane Integration — 2026-10-29 — GPU stabilizer simulation and parity-QAOA

**Starting main:** 96485219b3dfc3911abc4ba695775296560318de  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** B, C, F, H; D/G co-design preserved; E remains active on BIO-001/FUS-001  
**Evidence class:** PEER-REVIEWED COMPUTATIONAL BENCHMARK / LITERATURE-ONLY / UQPU REPRODUCTION OPEN

## Integration summary

The new-to-repository primary source is Osama, Thanos and Laarman, *Quantum* 10, 2225 (2026-10-01), DOI https://doi.org/10.22331/q-2026-10-01-2225. It describes QuaSARQ, a GPU-accelerated classical simulator for stabilizer/Clifford circuits, and reports benchmark-specific speed/energy gains. UQPU has not reproduced these results. The simulator is not a generic backend for arbitrary non-Clifford QAOA rotations.

The latest starting-head code commit's exhaustive parity encode/decode test passed core/invariant CI run #1972 and cold-start audit #1233. It checks a classical graph-parity mapping over 1,099 labelled graphs through five vertices. The parity-QAOA circuit and matched accepted-task comparison remain open.

## Shared acceptance contract

For QuaSARQ reproduction, freeze source revision, dependencies, circuit suite, seeds, hardware/software environment, output/syndrome reference and acceptance predicate. Record setup and steady-state time separately, throughput, correctness, retries, peak host/device memory, transfer bytes/time, host work and energy where measurable. Compare with matched versions and hold out a circuit family; preserve failed cases. Unknown energy components remain unknown, not zero.

For parity-QAOA, continue the existing RG-QAOA-PARITY-001 gate: exact small-graph objective/argmax and decoder certificates; identical workload, output predicate, target/configuration, shots, optimizer evaluations and repetitions; target-aware simulation before any authorized hardware execution.

## A–H integration

- **A:** parity mapping is CI-verified on the starting head; QAOA circuit not implemented; QuaSARQ reproduction gap opened.
- **B:** no provider adapter/target run; simulator and real-QPU evidence remain distinct.
- **C:** require tableau memory, host/device I/O, transfer, reconstruction and peak memory.
- **D/G:** no new physical device or manufacturing evidence; preserve continuous co-design and do not infer hardware benefits from simulator benchmarks.
- **E:** BIO-001/FUS-001 remain open; no Pangola fuel or fusion experiment.
- **F:** full cost/energy per accepted correct task, matched baseline and uncertainty remain mandatory.
- **H:** literature watch and handoff record published; six-language strategic references retained.

## Foundational layers and invariants

FND-001–006 and EQN-001–010 remain active; no new fundamental bound or physical law was established. INV-029–035 and INV-025/026/027 remain evidence-gated. The US$10T–US$100T ambition proxy is not a present valuation; physical Data-Center-to-One-Phone compression requires honest external infrastructure, energy, thermal and lifecycle accounting. Biomass carbon remains functional substitution/minimization/recovery/hybridization/redesign, never elemental transmutation. Accepted bio-oil, net reliable fusion electricity, lower project WACC and commercial claims remain unproven.

## Next gate

Implement parity-QAOA with independent exact certificates, then target-aware simulation. In parallel, pin and reproduce a small QuaSARQ stabilizer workload with matched baselines. Paid QPU execution remains disabled without credentials, a bounded budget and explicit user consent.

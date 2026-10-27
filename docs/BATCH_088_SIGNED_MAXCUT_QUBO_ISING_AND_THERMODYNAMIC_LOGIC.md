# Batch 088 — signed Max-Cut objective lowering and thermodynamic gate energy boundary

**Date:** 2026-10-28  
**Canonical starting main:** 7734020a3f48cfcd12c1eb198e8ca43dbafc1ca2  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** B, C, D, E, F, G and H; FND-001/FND-004/FND-006 and EQN-001–006  
**Evidence classes:** SOFTWARE_CONTRACT_ONLY + PEER_REVIEWED_SIMULATION/LITERATURE_ONLY  
**Paid QPU job:** no

## Starting-state and governance

The newest committed main state was resolved from GitHub, not from a remembered batch number. Main's latest published batch was 086. Batch 087 exists in open PR #144 and is not canonical main. The main-head prototype/invariant workflow and cold-start audit passed. PR #144's current exact-head workflow runs also report success, but its updated legacy nine-lane scoreboard and manifest conflict with the permanent A–H architecture in the Research Operating System. It is therefore not treated as merged project memory; reconcile that A–H/A–I drift before merge.

The required charter, invariants, goals, README, operating system, open-frontier directive, strategic model, strategic references and permanent root directives 00/00A/01–06 were inspected. Thai, English, Chinese, Japanese, Korean and German public master-plan links and recorded AI-agent/funding references remain preserved. INV-025–027 remain active and evidence-gated.

## Lane A — signed Max-Cut lowering contract

Added a pure-Python signed weighted Max-Cut lowering contract. For the frozen objective C(x) = sum w_uv (x_u XOR x_v), it derives QUBO linear/quadratic terms and the Ising constant/couplings under s_v = 1 - 2 x_v. Signed weights, including negative and zero weights, retain their exact objective meaning. The helper rejects malformed graphs, duplicate undirected edges, self-loops, booleans and non-finite weights rather than silently altering semantics.

Six focused test methods passed in an isolated local run. They exhaustively check all bitstrings for four fixtures and all 27 signed-weight patterns on a triangle, compare direct/QUBO/Ising objective values, verify the complete set of maximizers, and test canonical edge ordering and invalid-input rejection. These are software-contract results, not QAOA circuits, SDK validation, target simulation or quantum advantage.

## Fresh literature surveillance — thermodynamic logic gates

Whitelam, “Evolutionary design of thermodynamic logic gates and their heat emission,” *Physical Review E* 114, 034135, published 2026-09-21, DOI 10.1103/9lv8-drtp, is newly recorded in a dated watch. The publisher abstract describes simulation results for evolved logic gates where control-system heat can be comparable to heat emitted by information-bearing degrees of freedom, and some designs shift dissipation into the control unit.

The follow-up gate requires a pinned model, identical truth table/error/throughput, held-out initial states, and separate accounting for controller, measurement, feedback, actuation, initialization, reset, readout, power-supply energy and cooling. Heat emission is not automatically wall-plug electricity. No model reproduction or physical result is claimed.

## A–H status ledger

- **A — Workloads/compiler/runtime:** implemented exact direct/QUBO/Ising objective equivalence and exhaustive small-instance tests; next is provider-neutral lowering and independent SDK convention checks.
- **B — Cloud/QPU/provider integration:** no provider adapter changes or execution; provider-neutral path preserved, simulator/dry-run first, paid jobs remain unauthorized.
- **C — RAM/VRAM/HBM/storage/state/data movement:** no memory-equivalence claim; preserve output-information and reconstruction accounting. Hilbert-space dimension is not readable classical storage.
- **D — Devices/chips/process/fabrication/packaging:** no device or fabrication result; D/G co-design remains continuous.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** new thermodynamic-gate literature gate only; no Pangola material, accepted liquid-fuel or net-electric fusion data.
- **F — Economics/benchmarks/evidence/integration:** no cost or energy advantage; any follow-up must measure full accepted-task energy/cost and compare against a matched baseline.
- **G — Manufacturing equipment/software/factory systems:** no equipment, yield or cost-per-good-device evidence; maintain D/G interface.
- **H — Strategic plan/publication:** dated source watch and cycle report added; multilingual master-plan and strategic AI-agent/funding references preserved.

## Foundational and equation-discovery progress

- **FND-001:** adds a falsifiable literature-derived energy-accounting gate; no measured work, heat, wall-plug energy or accepted-task energy result.
- **FND-002:** unchanged; output-information/reconstruction contracts remain; no state-space-to-classical-memory equivalence.
- **FND-003:** unchanged; the OTOC quantum-speed-limit source remains assumption-scoped and unreproduced; no matched control experiment.
- **FND-004:** thermodynamic computing is an alternative-primitive lead only; no UQPU primitive demonstrated.
- **FND-005:** no experimentally validated QFT/particle mechanism or credible anomaly promoted.
- **FND-006:** exact objective lowering reinforces the need to freeze mathematical semantics before model comparison; no new equation of nature.
- **EQN-001–006:** unchanged evidence gates: constraints, held-out prediction, counterexample search, proof/simulation, discriminating experiment and independent validation remain required.

## INV-029 through INV-035

- **INV-029:** no data-center-to-phone service, energy, physical-compression or lifecycle-cost milestone.
- **INV-030:** no Pangola carbon substitution, recovery or material qualification.
- **INV-031:** no Pangola-specific accepted liquid-energy/fuel result.
- **INV-032:** no net delivered fusion electricity or commercial low-cost result.
- **INV-033:** no lower principal, absolute interest, project WACC or macro-rate result.
- **INV-034:** advances the foundational research method only.
- **INV-035:** keeps equations evidence-gated; no AI-generated or fitted expression is promoted to physical law.

## CI, synchronization and next gate

At the starting main head, the prototype/invariant workflow and cold-start audit passed. The new commit must pass its own exact-head Actions checks; a local six-test run is not a substitute for repository CI. No paid QPU execution was attempted.

WORKLOG.md and RESEARCH_GAPS.md are large append-only files and PR #144 has concurrent append-only changes to them. This cycle leaves those aggregate histories untouched to avoid an unsafe prefix replacement/conflict; this dated batch, the dedicated gap and the integration record carry the complete update. **Sync debt remains open** until the pending PR and A–H/A–I architecture discrepancy are reconciled.

Next highest-value gates:
1. pass exact-head CI and cold-start audit;
2. bind the signed Max-Cut objective hash to provider-neutral lowering and independently verify QUBO/Ising sign/constant conventions in an SDK, then target-aware simulation;
3. pin and independently reconstruct the thermodynamic logic-gate model with full energy accounting;
4. reconcile PR #144's legacy nine-lane scoreboard against the permanent A–H architecture before merging;
5. keep real-QPU execution disabled until credentials, bounded budget and explicit user consent exist.

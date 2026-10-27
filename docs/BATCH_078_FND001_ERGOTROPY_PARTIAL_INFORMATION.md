# Batch 078 — FND-001 partial-information ergotropy certificate

**Date:** 2026-10-27  
**Starting main SHA:** `20dd5cab2272e204465889d3f77c377a41fa8cd9`  
**Primary technical owner:** Lane A — executable statistical contract  
**Evidence/integration owner:** Lane F  
**Literature/publication owner:** Lane H  
**Evidence class:** PEER_REVIEWED_THEORY + SOFTWARE_CONTRACT; full SDP reproduction not run

## Research question

Can UQPU reuse a published finite-shot confidence construction for partially observed quantum systems without confusing a lower bound on extractable work with total device energy, thermodynamic dissipation, or accepted-task economics?

## Fresh literature delta

Pagliaro et al., “Certifying Ergotropy under Partial Information,” *Physical Review Letters* 137, 130401 (published online 2026-09-21; DOI 10.1103/pl26-g6vy; preprint https://arxiv.org/abs/2603.18828), formulate a two-stage semidefinite-programming certificate for ergotropy from partial observable expectations, assuming a known Hamiltonian. Their finite-statistics treatment uses confidence regions from Hoeffding's inequality and a union bound. The authors report synthetic examples and a four-qubit IBM-processor example; UQPU has not reproduced the SDP or submitted any QPU job.

The literature watch was absent from the current repository search. This adds a source-bounded work-certificate lead, not a new physical limit or a measured UQPU energy result.

## Lane A implementation

Added `bounded_observable_hoeffding_radii` to `software/uqpu-prototype/uqpu/fundamental_limits.py` and focused tests in `software/uqpu-prototype/tests/test_fundamental_limits_and_frontier.py`.

The helper implements only epsilon_i = sqrt(2 ln(2K/delta) / N_i) for a nonempty list of positive integer shot counts, K observables with eigenvalues in [-1,1], independent samples per observable and 0 < delta < 1. It rejects malformed counts and invalid confidence probabilities. It does not compute ergotropy, solve an SDP, or claim physical energy efficiency.

## Cross-lane review A–H

- **A — Workloads/compiler/runtime:** added the finite-shot statistical helper and tests; no QAOA workload or equation-discovery winner is promoted.
- **B — Cloud/QPU:** provider-neutral no-submit path preserved; no credentials or billable hardware execution used.
- **C — Memory/state/data movement:** no memory/storage equivalence claim; shot count and measurement overhead must remain explicit.
- **D — Devices/material physics:** no device or material result; any later Hamiltonian/measurement mapping must be target-specific.
- **E — Biomass/materials/bio-oil/fusion/cooling:** no Pangola, accepted-liquid, fusion or cooling measurements.
- **F — Evidence/economics/integration:** separates extractable-work certificate from total energy and accepted-task cost; aggregate RESEARCH_GAPS.md sync is deferred to avoid replacing a large append-only file.
- **G — Manufacturing/factory systems:** no process, yield or cost-per-good-device result; D/G co-design remains active.
- **H — Strategy/publication:** published a dated primary-source watch and preserved the Kanusanan Pongpanna Model and all six multilingual public master-plan links as strategic context.

## Foundational and permanent invariants

- **FND-001:** improves the statistical boundary around a possible work-resource certificate; no entropy-production, heat, wall-plug energy or cost/task result.
- **FND-002:** no new output-information or memory lower bound.
- **FND-003:** no matched control-versus-quantum-speed-limit experiment; the ergotropy result is not a gate-time bound.
- **FND-004/005:** no alternative physical primitive or QFT/particle mechanism validated.
- **FND-006 / EQN-001–006:** a source-bounded method is mapped into a falsifiable reproduction plan; no equation was discovered by UQPU.
- **INV-029:** no phone-boundary or physical-compression milestone.
- **INV-030:** no biomass-carbon substitution; elemental transmutation remains excluded.
- **INV-031:** no accepted Pangola liquid product or commercial cost.
- **INV-032:** no reliable net fusion-electricity or lifecycle-cost result.
- **INV-033:** no financed-principal, interest or WACC reduction measured.
- **INV-034/035:** mathematics-first discovery remains open, while current physical limits and independent evidence remain binding.
- **INV-025/026/027:** 100,000,000-unit and universal replacement goals remain falsifiable targets, not achievements.

## Validation, sync debt and next gate

The preceding head `20dd5cab2272e204465889d3f77c377a41fa8cd9` has successful hosted prototype/invariant and cold-start audit workflows (core run #1812, audit #1020). This batch adds Python code and tests, so the exact-head workflows triggered by this commit must pass before the helper is considered CI-validated. Local tests were not run because the current execution environment could not clone the repository.

The large append-only `RESEARCH_GAPS.md` was not rewritten; RG-FND001-ERGOTROPY-PARTIAL-INFO-001 is the canonical focused gap and aggregate sync debt is explicitly retained.

Next gate: confirm exact-head CI, then pin the paper's SDP equations and compare certificate values with exact spectral ergotropy on small systems. Do not start paid QPU execution; it is unnecessary for the first reproduction.

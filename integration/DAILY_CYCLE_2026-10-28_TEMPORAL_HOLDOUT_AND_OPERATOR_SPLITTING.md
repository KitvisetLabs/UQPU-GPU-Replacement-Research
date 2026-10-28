# Daily Eight-Lane UQPU integration — 2026-10-28 — temporal holdout and neural-operator splitting

**Integration ID:** INT-20261028-TEMPORAL-HOLDOUT-001  
**Starting main SHA:** 3ee200dcd9c7c4b34d2d73474964648281b1cca2  
**Primary owner:** Lane A — benchmark/model acceptance  
**Evidence owner:** Lane F — reproducibility and resource accounting  
**Publication owner:** Lane H — literature surveillance  
**Cross-lane consumers:** C, D, E, G; INV-034/035 feed A–H  
**Evidence class:** SOFTWARE_IMPLEMENTATION + SYNTHETIC_UNIT_FIXTURES + LITERATURE_ONLY  
**Paid QPU jobs:** none

## Integrated artifacts

- `software/uqpu-prototype/uqpu/temporal_holdout.py` — chronological, group-disjoint holdout certificate.
- `software/uqpu-prototype/tests/test_temporal_holdout.py` — 11 deterministic synthetic cases.
- `research_lanes/A_quantum_programming_runtime/TEMPORAL_HOLDOUT_ACCEPTANCE_CONTRACT.md` — stable Lane A interface.
- `docs/literature_watch/2026-10-28-neural-operator-splitting-heldout-regimes.md` — official PMLR source analysis.
- `docs/RESEARCH_GAP_TEMPORAL_HOLDOUT_ORDERING_2026-10-28.md` — RG-A-TEMPORAL-HOLDOUT-ORDERING-001.
- `docs/BATCH_103_TEMPORAL_HOLDOUT_CERTIFICATE_AND_OPERATOR_SPLITTING.md` — complete cycle record.

## Integration result

The helper composes the existing raw-record split-manifest builder/verifier with timezone-aware timestamp parsing, strict chronological ordering and an optional positive embargo. It records hashes, split ranges, counts and temporal gaps. This closes a metadata-level gap: a declared TIME_BLOCK group split can be group-disjoint yet still fail to represent future-time extrapolation if timestamps are out of order.

The new PMLR paper provides a method lead for test-time composition of pretrained neural operators on unseen dynamics. The source's results remain literature-only; the new helper has synthetic fixtures only. No external model/data/code was reproduced, no physical system was tested, and no economic advantage was measured.

## A–H and cross-pillar disposition

- **A:** temporal holdout contract added; signed-Max-Cut QAOA and pinned-SDK follow-on remains in open PRs #149/#150 and is not claimed as merged.
- **B:** provider-neutral adapter path preserved; no provider or target job.
- **C:** data/time/group hashes improved; no state or storage equivalence.
- **D:** no device/fabrication result; D/G co-design retained.
- **E:** possible future application to thermal-fluid, biomass conversion and fusion-component models only after source-pinned data and physical validation.
- **F:** leakage gate improved; no cost/task or finance result.
- **G:** process drift remains a future measured-data application; no factory/yield result.
- **H:** source-specific publication and autonomous handoff artifacts added; all six strategic-language links preserved.

FND-001–006 and EQN-001–010 remain evidence-gated. BIO-001, FUS-001 and FIN-001 remain open. INV-029–035 and INV-025/026/027 are unchanged; no physical law or mission-level advantage is claimed.

## CI and sync

At the starting head, cold-start audit #1228 passed and core/invariant run #1967 was queued. The combined commit-status endpoint exposed no contexts. The new head requires its own exact-head Actions. The main README, integration index, lane scoreboard, root research-gap ledger, worklog and cold-start manifest are synchronized in the same commit. The new manifest references the current starting SHA and includes all new handoff paths. No prior append-only history was replaced.

**Next gate:** exact-head core/invariant and cold-start Actions; then independent review of pending signed-Max-Cut PRs and a source-pinned, matched-budget temporal-generalization benchmark.

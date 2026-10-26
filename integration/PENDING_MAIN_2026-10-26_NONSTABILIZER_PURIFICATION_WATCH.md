# Pending-main sync — EQN-PURIFY-001 purification resource-law watch (2026-10-26)

**Status:** PENDING REVIEW — summary only; source artifacts are not canonical main  
**Canonical starting main SHA:** 412403efebabd7186dcbfca286d8481308dab176  
**Source PR:** #120 — Oct 26 cycle: nonstabilizerness purification resource-law watch  
**Source PR URL:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/120  
**Source branch:** automation/2026-10-26-nonstabilizer-purification-watch  
**Latest source head at synchronization:** 4ec590ab017eda71e4b8b62addbca44d3ebdfaa2  
**Source commits observed:** 209a26f46f739a240079a4be200d4127d1761535; 9fb9b405d798b409659817a1b36bbff9aac9dc26; 0ce2ae30d56a18429a88fab1fa8b04a8cf7e12b8; 8126eab90a2666b41d48ac9ac7a461b58adf41c9; b62e3429992d665aeae914adb952e4416442e260; 979c5ac0f72d429a28d00aadbb54f96ef1b2910a; ecc8b41dff5239f77344488e91174dc7c16f21bc; 4ec590ab017eda71e4b8b62addbca44d3ebdfaa2  
**Work item:** EQN-PURIFY-001 / RG-051  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — economics/benchmarks/evidence  
**Publication support:** Lane H

## Why this record exists

The main-commit synchronization policy requires pending branch research to be discoverable from main without falsely claiming that code, tests, or results have merged. This file is a separately reviewed pending-main summary only. It does not copy the source artifacts into main and does not close the work item.

## Proposed source artifacts

- `docs/literature_watch/2026-10-26-nonstabilizerness-resource-law-purification.md`
- `research_lanes/A_quantum_programming_runtime/EQN-PURIFY-001.md`
- `docs/RESEARCH_GAP_RG051_PURIFICATION_RESOURCE_LAW.md`
- `integration/INT-20261026-052-NONSTABILIZER-PURIFICATION.json`

## Research summary

Fresh surveillance found He, Xiong and Wang's arXiv preprint “A Nonstabilizerness Resource Law for Universal Quantum State Purification” (arXiv:2607.08626, submitted 2026-07-09), alongside the related peer-reviewed *Physical Review Letters* two-copy no-go result (136, 090204; 2026-03-04). The preprint reports an exact linear mana law in odd dimensions, a two-sided linear robustness law for multi-qubit systems (exact for a single qubit), and an explicit purification map.

The proposed follow-up freezes the exact source version and theorem assumptions; independently reproduces the two-copy boundary; separates proof-level results from numerical SDP evidence for three/four copies; searches held-out state families and counterexamples; and keeps mana/robustness distinct from gates, shots, energy, dollars and accepted useful outputs.

## Evidence and boundaries

- Source evidence: ARXIV_PREPRINT plus a related PEER_REVIEWED_THEOREM; LITERATURE_ONLY for UQPU.
- No UQPU implementation, formal proof assistant run, SDP solve, simulator run, provider call or QPU job was executed in the documentation/specification source PR.
- No new physical law, quantum advantage, memory/storage equivalence, material/fuel/fusion result, financing effect or Data-Center-to-Phone closure is claimed.
- No paid/free QPU job, physical experiment, material purchase or funding action is authorized.
- Latest source PR #120 exact-head CI is being re-triggered after a provenance-only update. An earlier source head passed the Python 3.10/3.11/3.12 unit/invariant/CLI jobs; extended QSVT/QSP/independent-SDK jobs were still queued/in progress. Do not call the latest workflow passed until all required jobs complete.

## Canonical gap-ledger sync debt

The large append-only `RESEARCH_GAPS.md` history was inspected but not replaced from a partial/stale extract. RG-051 is a dated supplemental gap artifact in the source PR; this pending-main record makes the gap discoverable without asserting that it is already in the canonical living ledger.

## Next reconciliation gate

Review/merge source PR #120 after all exact-head CI jobs and scientific-scope review. If merged, record the full source-to-main SHA mapping and final CI result. Until then, this summary must remain clearly marked pending and must not be treated as canonical implementation or evidence.

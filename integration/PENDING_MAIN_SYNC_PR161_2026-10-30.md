# Pending-main synchronization record — PR #161 — QEC, device and D/G agentic co-design

**Date:** 2026-10-30  
**Canonical main base:** `41fac3953773ae0016a09539be57c3ed6b379771`  
**Source PR:** [#161 — peer-reviewed QEC, quantum-device and foundational frontier](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/161)  
**Source branch:** `research/2026-10-30-qec-device-foundation-frontier`  
**Source head:** `4a520e5dc4d217db53369a9bcd9f5636205689be`  
**Compare:** 12 commits ahead, 0 behind; 24 changed files.  
**PR state:** draft/open/unmerged. **No source SHA is mapped to main.**

## Purpose and scope

This is a pending-main summary only. It makes PR #161 discoverable to new agents without claiming that its research artifacts or source commits are already on canonical main.

The source PR adds:
- Mamba state-space QEC decoder literature and reproduction gate (Lane B).
- Planar qLDPC gapped-boundary construction and algorithmic transfer contract (Lane A; D/G interfaces).
- Transmon-waveguide and GaAs triple-dot spin-qubit device literature, with D/G transfer gap.
- Quantum strong-Mpemba and Majorana self-testing literature for FND-001/FND-005.
- **DG-AGENTIC-CODESIGN-001:** VIBRATO differentiable full-simulation / agent-guided detector co-design watch, focused D/G gap, Lane D/G transfer contract, A–H report and machine-readable record.

The new VIBRATO transfer is methodological only. The detector-specific physics model is not a quantum-chip model; staged optimization is not proof of joint global optimality; the source's ADC-power estimate uses assumed coefficients and is not measured wall-plug power.

## Source-commit reconciliation

The GitHub compare endpoint reports 12 source commits ahead of the base. The following 10 commit SHAs were returned directly by the write operations in this cycle and are recorded here:

1. `40ef2f2dd48e29860ab2a676bab1471cc2250605` — add agentic differentiable detector co-design literature watch.
2. `7dc82af4dc5159e3b054be9541c94df64b46cbbd` — record D/G reproduction gap.
3. `d80dab67c4a55393358d8c39e31f8e088c168445` — add D/G transfer contract.
4. `855a877372ff7df136dc1176f82f950b01394749` — publish A–H cycle report.
5. `a305770778208d2debb6f69845ceb6e5e136e968` — add machine-readable integration record.
6. `5f2da63efe527eedcca5a3f1c27f7cd2106bbc88` — index work in root README.
7. `730d3cabd58f3640318e428aba6d6f7e13df13bc` — index work in integration hub.
8. `137db4aae1a32d8ff7c11481947a3adc59ff463c` — refresh cold-start handoff manifest.
9. `38bda360588d79e4d9b4400e2ce93ae3320d484f` — update Lane D index.
10. `4a520e5dc4d217db53369a9bcd9f5636205689be` — update Lane G index and current source head.

**Enumeration debt:** two commits already present on the source branch before this cycle are included in the compare's 12-commit total, but their individual SHAs were not exposed by the available branch/commit-list operations. No SHA is invented. A complete source-to-main mapping remains blocked until those two source SHAs can be retrieved and reconciled.

## Files and durable records in the source PR

- `docs/literature_watch/2026-10-30-mamba-qec-decoder-peer-reviewed.md`
- `docs/literature_watch/2026-10-30-planar-qldpc-gapped-boundary-construction.md`
- `docs/literature_watch/2026-10-30-quantum-thermodynamics-and-majorana-self-testing.md`
- `docs/literature_watch/2026-10-30-transmon-waveguide-and-triple-dot-device-frontier.md`
- `docs/literature_watch/2026-10-30-agentic-differentiable-detector-codesign.md`
- Focused QEC and D/G gaps, including `DG-AGENTIC-CODESIGN-001).
- Lane A, B and D/G transfer contracts.
- `integration/DAILY_CYCLE_2026-10-30_QEC_DEVICE_AND_FOUNDATIONAL_FRONTIER.md`
- `integration/DAILY_CYCLE_2026-10-30_AGENTIC_DETECTOR_COSIGN.md`
- Corresponding machine-readable integration records.
- README, integration hub, Lane A/B/D/G indexes and cold-start handoff manifest.

## A–H and invariant impact

| Lane | Pending contribution |
|---|---|
| A | Planar qLDPC boundary/defect algorithmic construction; no implementation or QPU advantage. |
| B | Mamba QEC decoder transfer; no target/provider execution. |
| C | Syndrome, model, hidden-state, buffer and transfer accounting requirements; no memory measurement. |
| D | Transmon-waveguide, triple-dot and VIBRATO co-design literature; no UQPU device result. |
| E | No Pangola material, accepted bio-oil, fusion electricity or cooling result. |
| F | Reproduction, equal-budget, yield-adjusted cost and evidence contracts; no measured economics. |
| G | Process-window, metrology, defectivity, packaging and yield interfaces; no factory result. |
| H | Source-attributed publication; six-language strategic plan remains canonical context. |

FND-001–006 and EQN-001–006 remain active. INV-025/026/027 and INV-029–035 remain preserved. No AI-generated equation or external result is promoted to a physical law or project evidence.

## CI and merge gate

- Exact source head: `4a520e5dc4d217db53369a9bcd9f5636205689be`.
- Core workflow run #2332 is **queued** at this observation.
- Combined-status contexts are empty; no exact-head cold-start result is exposed.
- PR #161 remains draft/open/unmerged.
- Exact-head core and cold-start checks, review, source-SHA enumeration and source-to-main mapping are required before merge.
- Predecessor CI does not transfer to the current head.

## Evidence boundary and next action

No UQPU reproduction, paid QPU job, quantum-device fabrication, manufacturing-yield improvement, Pangola substitution, accepted fuel, reliable net fusion electricity, lower project WACC, financing advantage, new physical law or Data-Center-to-One-Phone milestone is claimed.

**Next action:** retrieve the two unresolved source commit SHAs, wait for exact-head core/cold-start CI, obtain review, then reconcile all 12 source commits to the resulting main SHA after merge. This summary PR does not merge PR #161 or assert its artifacts are on main.

# Batch 084 — AI mathematics corpus provenance and formal-check gate

**Date:** 2026-10-28  
**Canonical starting head:** `272f2a59ce0053c5f4b518edfacd5531b69eb5d1`  
**Primary owner:** Lane A — formal/equation evidence tooling  
**Cross-lane owners:** Lane F — evidence/resource accounting; Lane H — literature/publication  
**Evidence classes:** `LITERATURE_ONLY`; no new UQPU theorem, equation, device or economic result claimed  
**Scope:** Documentation/research protocol only; no code change and no paid QPU execution

## Starting-state and CI check

The canonical starting state was read from `main`, not inferred from a fixed batch number. Required charter, invariant, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, high-visibility root directives, newest Batch documents, focused gaps, foundational/equation-discovery helpers and handoff manifest were inspected.

The starting head `272f2a59ce0053c5f4b518edfacd5531b69eb5d1` had exact-head GitHub Actions success:
- [Prototype and project invariants run #1819](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40547643401): 15/15 jobs successful, including Python 3.10/3.11/3.12 and the existing reference, Qiskit and QSVT checks.
- [Cold-start handoff audit #1034](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40547643503): successful.

These runs validate the **starting head only**. The new documentation commit still requires its own Actions result. No local code tests, real-QPU job or hardware experiment is claimed in this documentation-only cycle.

## Literature delta

Ying Xie's arXiv preprint [2610.17090](https://arxiv.org/abs/2610.17090), posted 2026-10-12, surveys a public set of AI-written mathematical manuscripts and proposes a structured extraction of mathematical instruments, antecedents, caveats, formalization status and dependencies. The survey samples 38 problem families from a collection described as 722 manuscripts / 372 families. Its novelty judgments are provisional; source comparisons do not certify proofs or priority, and the survey reports no Lean development compiled or kernel-checked.

The new [dated literature watch](literature_watch/2026-10-28-ai-mathematical-instruments-corpus-audit.md) distinguishes this provenance/triage layer from Batch 083's proof-structure metric work. Both remain external literature, not reproduced UQPU evidence.

## Research decision

Extend the existing **RG-048** gate rather than create a duplicative gap. The survey suggests a useful candidate-triage record—claim, instrument, antecedents/dependencies, caveats, exact source version and formalization status—but does not justify a new score or acceptance rule.

The [RG-048 supplementary source section](RESEARCH_GAP_AI_PROOF_STRUCTURE_METRICS_2026-10-28.md) specifies a small pinned reconstruction: three records from one family, source/corpus/toolchain hashes, independent claim and dependency reconstruction, Lean kernel-check where feasible, positive and negative controls, automation/tactic sensitivity and retained failures. The existing exact-byte proof binding and allowed proof statuses remain unchanged.

## A–H status

| Lane | Status / advancement this cycle |
|---|---|
| **A — Quantum programming/workloads/compiler/runtime** | Added a source-provenance triage gate downstream of RG-EQN-008 and RG-048. No equation-discovery method is promoted as a winner; no proof metric is implemented. |
| **B — Cloud/QPU/provider integration** | Provider-neutral paths preserved. No provider credentials/pricing were newly verified and no job was submitted. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Formal corpus size, proof bytes, quantum state and readable classical storage remain distinct quantities. No memory/storage replacement result. |
| **D — Devices/chips/process/packaging** | No device or fabrication evidence changed. |
| **E — Biomass/materials/bio-oil/fusion/cooling** | BIO-001 and FUS-001 remain open. No Pangola material substitution, accepted-liquid cost or net-electricity result. |
| **F — Economics/benchmarks/evidence/integration** | Future accounting includes corpus indexing, formalization/checking, independent review, retries, host compute, memory and measured energy. No accepted-task cost advantage measured. |
| **G — Manufacturing equipment/software/factory systems** | D/G co-design preserved; no yield, process-window or cost-per-good-device result. |
| **H — Kanusanan Pongpanna Model, strategic finance and publication** | Published the new source watch and updated README/handoff context; all six language editions and strategic AI-agent/funding references remain preserved. |

## Foundational agenda and permanent invariants

- **FND-001:** no new thermodynamic-gap or wall-plug energy measurement.
- **FND-002:** no new output-information or readable-storage bound.
- **FND-003:** no matched control-versus-quantum-speed-limit experiment.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new QFT/particle mechanism validated.
- **FND-006 / EQN-001–006:** strengthened literature triage and provenance; no theorem, equation or physical law promoted.
- **INV-029:** Data-Center-to-One-Phone remains an unachieved physical-compression goal; the US$10T–US$100T number remains an ambition-scale proxy.
- **INV-030:** no elemental transmutation or functional Pangola-carbon substitution claim.
- **INV-031:** no commercial ultra-low-cost bio-oil/fuel evidence.
- **INV-032:** no commercial fusion or reliable net-delivered-electricity cost evidence.
- **INV-033:** no measured reduction in financed principal, absolute interest, risk premium or WACC.
- **INV-034/035:** mathematics-first invention remains active; present physics binds engineering claims and all new hypotheses remain subject to proof/experiment, falsification and independent validation.

INV-025/026/027, the 100,000,000-unit and 100,000,000x cost moonshots, subsystem-specific useful-output contracts and the no-qubit-equals-readable-byte rule remain intact.

## Integration, preservation and sync

The README points to this Batch, the literature watch and RG-048. The handoff manifest records the latest frontier, lane owners, exact starting-head CI and next independent action. The permanent root directives `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md`, `00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md`, `01`–`06` strategy/foundation files, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md` and the Thai/English/Chinese/Japanese/Korean/German public master-plan links are preserved.

The large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were not rewritten from partial snapshots. RG-048 remains the focused canonical gap; aggregate append-only synchronization debt remains explicit.

## Next highest-value gate

Pin the corpus and toolchain, reconstruct three claim/instrument records with positive/negative controls, obtain kernel-check and independent-rebuild outcomes, then decide whether any normalized proof-structure diagnostic is robust enough to implement. Continue in parallel with RG-EQN-008, FND-001/FND-003, BIO-001, FUS-001 and FIN-001. No paid QPU job without credentials, bounded budget and explicit user consent.

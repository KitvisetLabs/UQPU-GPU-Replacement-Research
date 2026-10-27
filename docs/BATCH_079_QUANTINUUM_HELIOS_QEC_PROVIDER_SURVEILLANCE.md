# Batch 079 — Quantinuum Helios color-code QEC provider surveillance

**Date:** 2026-10-27  
**Starting main SHA:** `e698c4fc6064d6e9faadf8388ae791b8d90af6f5`  
**Primary owner:** Lane B — cloud/QPU provider integration  
**Device/manufacturing co-owners:** Lanes D and G  
**Compiler/runtime owner:** Lane A  
**Evidence/economics owner:** Lane F  
**Publication owner:** Lane H  
**Evidence class:** OFFICIAL PREPRINT REPORTING EXPERIMENTAL QEC; not independently reproduced by UQPU

## Research question

Does a newly published target-specific logical-error-suppression result change UQPU's provider-neutral target evidence and benchmark priorities, without being misrepresented as application-level quantum advantage?

## Literature delta

Lavasani et al., “Quantum error correction well below the color code threshold,” official arXiv preprint 2610.24077 (submitted 2026-10-16; updated 2026-10-20), report triangular color-code distances 3, 5 and 7 on Quantinuum Helios. Their abstract reports logical memory error rates as low as 5×10^-6, error suppression factor 12 with uncertainty -2/+3 per tested increase in code distance, and a logical two-qubit Clifford error around 7×10^-5 at distance 5 with suppression factor 9 and uncertainty -3/+8. CNN and Transformer decoders are compared with algorithmic decoders, with reported decoder throughput exceeding syndrome-extraction cadence in their setup.

Official primary source: https://arxiv.org/abs/2610.24077. Quantinuum's 2026-10-19 announcement is linked in the dated watch. The company roadmap remains forward-looking. UQPU has not reproduced the study or submitted a QPU job.

## Work completed

- Added a dated source-bounded literature watch and RG-QEC-HELIOS-COLORCODE-REPRODUCTION-001.
- Recorded target-specific acceptance metrics and a reproducibility path that separates logical memory, logical gates, decoder timing and application-level quality.
- Integrated the source into the provider-neutral target registry workflow and continuous D/G co-design agenda.
- Updated README, WORKLOG and cold-start handoff in the same commit.
- No provider adapter code, live job, benchmark result or economic claim was added.

## A–H status

- **A — Workloads/compiler/runtime:** Batch 078's confidence-radius helper remains under exact-head CI; this new QEC source becomes a target-specific benchmark candidate only. The compiler must not collapse logical-memory fidelity into task success.
- **B — Cloud/QPU integration:** new provider-specific literature lead; actual cloud access, supported APIs, pricing and job limits still need verification.
- **C — Memory/state/data movement:** physical-qubit overhead, syndrome streams and decoder memory/latency must be included; no classical memory replacement is implied.
- **D — Device/chip/process/packaging:** target-specific QEC depends on connectivity, leakage control, measurement and calibrated operations; no device-general inference.
- **E — Biomass/materials/bio-oil/fusion/cooling:** no new energy, material, fuel, fusion or cooling evidence.
- **F — Economics/evidence/integration:** full cost per accepted task and competitive baselines remain required; no cost claim.
- **G — Manufacturing/factory systems:** D/G co-design now has a current logical-error versus physical-resource/decoder-throughput literature lead; no manufacturing yield or cost-per-good-device data.
- **H — Strategy/publication:** official preprint and company announcement recorded with the claims and limitations separated.

## Foundations and invariants

FND-001 receives no thermodynamic measurement. FND-002 receives no new output-information lower bound. FND-003 receives a target-specific QEC timing/resource lead, not a quantum-speed-limit measurement. FND-004/005 show no new primitive or particle/QFT mechanism. FND-006 and EQN-001–006 receive a source-pinned falsifiable reproduction path, not a new equation.

INV-029 remains a physical-compression mission with no milestone claimed. INV-030–033 remain unproven at their target material, fuel, fusion and finance outcomes. INV-034/035 remain evidence-gated; no physical law is proposed. INV-025/026/027 remain falsifiable moonshots, not achieved results. All permanent root directives and six-language master-plan references are preserved.

## CI and next gate

At batch start, the preceding head's Python 3.10/3.11/3.12 unit/invariant matrix passed, but extended QSP/QSVT/Qiskit/reference jobs were still running; the cold-start audit passed. This documentation-only provider watch does not alter the code under test, but exact-head CI must still be checked after commit.

Next gate: pin and reproduce the preprint's error rates/suppression factors, then verify real provider access and pricing. Simulator/dry-run first; no paid QPU execution without credentials, bounded budget and explicit user consent.

# Batch 117 — near-memory QUBO for RAG: a classical baseline and matched UQPU gate

**Date:** 2026-10-29  
**Starting main SHA:** d1fe37724dd3f30dda1f99787151154bce285ea9  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Cross-lane interfaces:** B provider routes; C memory/state/data movement; D/G device and manufacturing co-design; E energy/material/infrastructure accounting; F evidence/economics; H publication and strategic continuity  
**Cross-cutting:** INV-025–037, especially INV-026/029/034/035; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Evidence class:** OFFICIAL ARXIV PREPRINT / THIRD-PARTY SILICON CLAIMS AND MODEL-BASED APPLICATION EVALUATION; UQPU NOT REPRODUCED  
**Paid QPU execution:** not authorized or attempted

## 1. Canonical start and integrity

Re-resolved `main` at `d1fe37724dd3f30dda1f99787151154bce285ea9`. The latest committed tree contains Batches 113–116, their focused gaps and integration records, the eight-lane workspace, the root directives 00/00A/01–06, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and the existing FND/EQN, BIO-001, FUS-001 and FIN-001 programs. The required Thai, English, Chinese, Japanese, Korean and German public master-plan links remain in the strategic references.

On the starting SHA, GitHub Actions `UQPU Prototype and Project Invariants` run [#1983](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40792512034) and `Autonomous Cold-Start Handoff Audit` run [#1244](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40792512009) completed successfully. This is the starting-head state only; the new commit still requires exact-head Actions.

## 2. New literature delta

The official arXiv preprint [“p-DCIM: A 28nm Probabilistic SRAM DCIM based Ising Machine for Near-Memory Context Selection in LLM-RAG Pipeline”](https://arxiv.org/abs/2610.37033), posted 2026-10-27, reports a fabricated 28-nm, 32-Kb SRAM digital compute-in-memory macro that reuses its datapath for QUBO construction and probabilistic Ising updates. The paper reports 0.16 mm² area, 500 MHz and approximately 0.413 mW active macro power in probabilistic mode. Ten small QUBOs that fit the macro reportedly reached the brute-force optimum. Larger HotpotQA workloads use a measurement-parameterized behavioral model; the HBM/HBF package-level integration is proposed, not fabricated. The reported approximately 2.2 ms and 0.9 µJ selection figures are explicitly macro-normalized, not a complete system energy measurement. The paper reports a 67% total-query-energy reduction for its evaluated pipeline, but that application-scale result must be interpreted with its model-based larger-workload evaluation and LLM-selector baseline.

The genuine project delta is a concrete *classical near-memory QUBO baseline* for the existing QAOA/optimization work. It does not demonstrate a quantum advantage, general GPU replacement, a memory replacement, or a universal energy ratio. The full source-specific evidence boundary and falsifiable protocol are recorded in the [literature watch](literature_watch/2026-10-29-pdcim-near-memory-isings-for-rag.md).

## 3. Lane A advancement — freeze the workload before comparing solvers

Added `RAG_CONTEXT_SELECTION_CONTRACT_2026-10-29.json` as a machine-readable preregistration and a small test that guards its evidence labels and required fields. The intended workload is requirement-aware selection of a bounded set of passages from a fixed retrieved candidate pool. All methods must consume the same candidate/embedding/QUBO manifests, context budget, held-out query split and downstream answer-generation configuration.

The benchmark matrix distinguishes:
- exact brute-force references for small instances;
- classical CPU/GPU optimization baselines;
- p-DCIM direct-silicon runs only for instances actually executed on the fabricated macro;
- p-DCIM behavioral-model results for larger instances, labeled MODEL_ONLY;
- QAOA simulation before any hardware escalation;
- real QPU or D-Wave hardware only after account/target verification and explicit bounded-budget consent.

The contract freezes quality thresholds before evaluation rather than borrowing the paper's results as UQPU acceptance thresholds. It requires feasible selections, a common objective/reference, downstream answer quality, latency, throughput, state/I/O/transfer, host work, retries, reconstruction, energy boundary and cost per accepted useful task. Unknown cost/energy remains unknown, not zero.

## 4. Explicit A–H status

- **A — advanced:** new matched RAG/QUBO workload contract, source-specific literature watch and regression guard; no algorithm result claimed.
- **B — reviewed:** retain provider-neutral lowering and simulator-first routing. No new provider adapter is justified by this paper; no paid job was submitted.
- **C — advanced as a contract input:** explicitly count embeddings, QUBO construction/storage, transfers and the selected-output return path. SRAM/near-memory compute is not equivalent to general readable RAM/VRAM/HBM/storage.
- **D — reviewed:** source reports a fabricated 28-nm macro; no UQPU device, yield, lifetime or package qualification is established.
- **E — reviewed:** no new Pangola-carbon, accepted bio-oil, fusion net-electricity, cooling or infrastructure economics evidence.
- **F — advanced as a measurement design:** the contract prevents macro-only energy and model-only application results from being reported as complete accepted-task economics.
- **G — reviewed with D/G co-design preserved:** a 28-nm design is a process lead, not proof of UQPU manufacturing capability, yield or cost per good package.
- **H — maintained:** strategic master document, multilingual public links and AI-agent/funding context remain canonical and are not treated as scientific or financing evidence.

## 5. Invariants, foundations and energy/finance boundaries

- **INV-029:** near-memory data-movement reduction may be a subsystem-level stepping stone; it is not Data-Center-to-One-Phone physical compression. External GPU/LLM, HBM/HBF, host and infrastructure remain in the boundary.
- **INV-030–033:** no material substitution, accepted liquid fuel, net delivered fusion electricity, reduced financed principal or WACC effect is demonstrated by this computing paper.
- **INV-034/035:** no new physical law is proposed. EQN-001 receives a literature-surveillance entry; EQN-002/003 gain a candidate *method-comparison* use case only. EQN-004–006 remain evidence-gated.
- **FND-001/003–006:** no new foundational bound or physical mechanism is established. FND-002 is not advanced by the paper itself; the RAG task is a possible application-level output-information testbed, not a new lower bound.
- **BIO-001/FUS-001/FIN-001:** remain open; this batch contributes no calibrated fuel, fusion-electricity or finance data.
- **INV-025/026:** the 100M-unit and 100M-GPU targets remain falsifiable moonshots. QUBO state-space size is not readable classical memory, and no NPU equivalence is inferred.

## 6. Next highest-value gate

Create a frozen, versioned RAG test manifest and exact small-instance QUBO certificates. Run identical objective/acceptance checks against brute force and CPU/GPU baselines; use p-DCIM silicon only for source-supported direct-silicon-sized cases and keep larger model outputs separately labeled. Then run QAOA simulation with the same objective and output-quality contract. Record all resource and energy boundaries. Only after these gates should provider-specific QPU comparisons be considered; never submit a paid job without credentials, bounded budget and explicit consent.

## Non-claims

This batch does not establish UQPU reproduction of the preprint, QAOA advantage, real-QPU performance, 100×/100,000,000× economics, general GPU/CPU/NPU or memory/storage replacement, Pangola-material substitution, commercial bio-oil, low-cost fusion, reduced WACC, a new physical law, or Data-Center-to-One-Phone completion.


## Handoff / CI follow-up

The first commit carrying this batch triggered the cold-start audit, which failed solely because its commit message omitted the required `Research-Sync: main` trailer. The next main commit repairs that metadata and records this follow-up. This does not change the literature evidence class, the preregistered comparison contract or any scientific claim. Recheck the exact repaired head before treating the handoff as complete.

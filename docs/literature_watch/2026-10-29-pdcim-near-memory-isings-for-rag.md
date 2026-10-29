# Literature watch — p-DCIM near-memory Ising hardware for RAG context selection

**Date checked:** 2026-10-29  
**Primary owner:** Lane A — workload/algorithm/compiler/runtime  
**Interfaces:** B provider-neutral execution; C memory and data movement; D/G device/process/packaging; F accepted-task evidence and economics; H strategic publication  
**Evidence class:** OFFICIAL ARXIV PREPRINT; third-party fabricated macro plus model-based application evaluation; **not independently reproduced by UQPU**  
**Stable ID:** LIT-2026-10-27-PDCIM-RAG-NEAR-MEMORY

## Source and date

Madhav Vadlamani, Rahul Singh, Yuyao Kong, Haomei Liu, Zheng Zhang and Shimeng Yu, “p-DCIM: A 28nm Probabilistic SRAM DCIM based Ising Machine for Near-Memory Context Selection in LLM-RAG Pipeline,” official arXiv preprint posted **2026-10-27**: https://arxiv.org/abs/2610.37033.

## What is genuinely new

The paper reports a fabricated 28-nm, 32-Kb SRAM digital compute-in-memory (DCIM) macro for requirement-aware RAG passage selection. It reuses one SRAM/adder datapath for deterministic construction of the QUBO coefficients and probabilistic Ising updates; measured SRAM pseudo-read disturbances provide stochasticity, while a digital bit-plane schedule controls the effective cooling. The reported macro is 0.16 mm² at 500 MHz, with about 0.406 mW deterministic-mode and 0.413 mW probabilistic-mode active power. The authors report that all ten small QUBO instances directly run on the macro reached the brute-force optimum.

For larger HotpotQA workloads, the paper uses a measurement-parameterized behavioral model that incorporates measured device statistics and finite precision. It reports about 2.2 ms selection latency and 0.9 µJ selection energy, and a 67% reduction in evaluated total query energy against an LLM-based selection pass while maintaining competitive answer-quality metrics. The paper explicitly characterizes 0.9 µJ as a macro-normalized estimate based on measured macro power, not a full-array/full-system measurement. Its HBM/HBF-integrated package is a proposed architecture; that package-level system was not fabricated in this work. Source: https://arxiv.org/abs/2610.37033.

## Limitations and evidence boundary

- This is a preprint, and UQPU has not reproduced its silicon measurements, benchmark data or application pipeline.
- Direct silicon evidence is bounded to small instances fitting the fabricated macro; larger application instances use a measurement-parametrized model. Do not relabel those modeled outcomes as direct chip measurements.
- The HBM/HBF package integration is proposed rather than demonstrated in a fabricated package.
- The reported baseline is an LLM-based selector in a GPU RAG pipeline. It is not a matched comparison against every classical QUBO solver, QAOA, D-Wave, or a competitive full-stack GPU/CPU/NPU baseline.
- The macro-normalized selection energy excludes the right to claim complete system energy by itself. Query embedding/requirements and final answer generation still involve the GPU; retrieval, memory traffic, host control, package, cooling and lifetime/capital costs need explicit boundaries.
- A classical CMOS Ising accelerator is not a quantum processor. It does not demonstrate quantum advantage, general-purpose GPU replacement, universal RAM/VRAM/HBM/storage replacement, or a new physical law.

## Exact UQPU relevance

**Lane A / INV-025–027:** this is a valuable QUBO workload baseline to compare with exact references, classical CPU/GPU solvers, QAOA simulation and—only later—authorized hardware. Use the identical QUBO coefficients, objective sense, feasible-output rule, held-out queries and accepted-answer contract. A solver's execution success or low objective alone is not accepted useful output.

**Lane C / INV-026:** the architectural lesson is that *where* QUBO construction and solution occur can dominate data movement. Count candidate/embedding transfers, QUBO storage, host work and output reconstruction. SRAM macro capacity is not a substitute for general-purpose addressable/persistent memory semantics.

**Lanes D/G:** the reported 28-nm macro is a third-party device result and a useful process/packaging design reference. It is not evidence of UQPU fabrication, production yield, reliability, lifetime or cost per good package. D/G must co-design against a defined function and package boundary.

**Lane F / INV-029:** compare total cost and energy per accepted downstream answer, not only selection-stage energy. Preserve separate evidence labels for direct silicon, measured macro parameters, behavioral-model projections and full-system measurements. The paper's reported reduction is a source claim for its evaluated pipeline, not a UQPU result.

**Lane E / INV-030–032:** no Pangola carbon substitution, accepted biomass liquid fuel or net delivered fusion-electricity result follows from this paper. **INV-033:** no financing-principal or WACC effect is established. **Lane H:** preserve the Kanusanan Pongpanna Model and multilingual strategic references as context, not evidence.

**INV-034/035:** this is an architecture/algorithm result, not a new physical equation. It can inform EQN-001 literature monitoring and a controlled EQN-002/003 *method* benchmark; it does not advance FND-001/003–006 or prove a new law. FND-002's information lower bounds remain unchanged.

## Proposed falsifiable follow-up

1. Freeze a versioned manifest for query groups, candidate passages, embedding model/version/precision, requirements, context budget, QUBO matrix, slack-variable encoding and downstream answer-generation model/prompt/decoding.
2. For small QUBOs, publish exact brute-force certificates and test objective/feasibility. For larger instances, identify a separate bound or best-known reference and do not call it exact.
3. Compare CPU, GPU, p-DCIM (direct silicon only when actually run on-chip), p-DCIM behavioral model, and QAOA simulator on identical QUBOs. Keep model-only outputs separate from measured hardware records.
4. Use disjoint query/topic holdouts and preregister answer-quality non-inferiority margins before evaluation; report exact match, Gold-Contains, token F1, feasibility, objective gap and failure cases.
5. Record query embedding/requirement generation, QUBO construction, data movement, solver runtime, peak memory, output reconstruction, retries, measured energy boundary, cooling/host costs and total cost per accepted useful task. Unknown costs are unknown, never zero.
6. Only after simulator and contract gates pass, consider a real-QPU/D-Wave comparison with target-specific price snapshots and explicit bounded-budget consent. Never mix one target's success probability with another target's price.

**Decision:** adopt as a high-value classical near-memory baseline and benchmark-design input. No UQPU, quantum, material, fuel, fusion, financing or mission-level advantage is promoted by this literature watch.

# Eight-Lane UQPU Research Cycle — Provider and QEC Hybrid Watch

**Cycle date:** 2026-10-26  
**Canonical starting main SHA:** 412403efebabd7186dcbfca286d8481308dab176  
**Branch:** research/2026-10-26-provider-qec-hybrid-watch  
**Status:** review-branch artifacts; not canonical until merged  
**Primary owner:** Lane B; implementation owner Lane A; integration owner Lane F; publication owner Lane H

## Starting-state and governance

The canonical main head is 412403efebabd7186dcbfca286d8481308dab176. Required mission/invariant documents, root directives 00/00A/01–06, the Kanusanan Pongpanna Model and STRATEGIC_PLAN_REFERENCES.md remain preserved. Batches 060–063 are the newest canonical Batch range inspected; multiple Batch 064 proposals are open, so this work uses stable IDs rather than a new numbered batch. The six-language Thai/English/Chinese/Japanese/Korean/German strategic links remain intact. Large append-only README.md, WORKLOG.md and RESEARCH_GAPS.md are not overwritten from partial reads.

## Fresh provider surveillance

### AWS — Ising Decoding and QEC latency

AWS's 2026-10-21 provider technical post reports GPU training on P4d/P5/P5en/P6/G6e instances using eight GPUs per instance and Stim-generated distance-9 surface-code syndromes under a circuit-level depolarizing model. The post reports simulated distance-31 inference latency reductions of roughly 2.4x–2.9x per round for tested pre-decoder+MWPM configurations, with improved reported logical error rate. These are provider-reported simulation results, not an independently reproduced UQPU result or a real-QPU end-to-end measurement.

**Mission relevance:** QEC decoding may require classical processing on the same microsecond-scale cycle as the quantum hardware. If a proposed UQPU system still depends on an external GPU decoder, its compute, memory, transfer, controller, energy and cost must remain inside the equivalent-useful-output boundary.

### Quandela — NVQLink and regional access

Quandela's 2026-10-13 NVQLink post describes a DGX Spark / FPGA-based controller / photonic-QPU integration workflow; the GTC Berlin demo QPU is simulated, while the company refers separately to prior physical-QPU integration validation. The post does not provide a complete independently audited end-to-end cost/latency ledger.

A 2026-10-22 announcement says Quandela and Quanova plan a MosaiQ deployment at Quang Trung University in Vietnam with training/research infrastructure. This is a planned deployment, not a verified live target or price/access route. No UQPU adapter is claimed.

## A–H status

| Lane | Status this cycle | Next gate |
|---|---|---|
| A — workloads/software | QEC decoder-aware latency and accepted-logical-operation comparison identified; no QPU advantage claimed. | Reproduce simulated decoder benchmark under frozen noise/quality contracts. |
| B — cloud/QPU/provider | Official AWS and photonic-provider updates recorded. | Verify actual endpoint, modality, API, pricing and access before adding adapter support. |
| C — memory/data movement | Syndrome transfer, controller buffers and host/GPU movement identified as required accounting. | Record bytes, queueing and end-to-end round-trip latency. |
| D — devices/chips/packaging | Photonic controller integration remains a co-design topic. | Obtain physical-target timing/noise data; separate simulated and physical modes. |
| E — materials/energy | No direct material, fuel or fusion result. | Continue BIO-001/FUS-001 under accepted-product/net-electricity gates. |
| F — economics/evidence | AWS cost/time trade-offs are source-reported and region/date-specific. | Independently reproduce with exact billing boundary and total cost per accepted logical operation. |
| G — manufacturing systems | Controller/packaging/test dependencies surfaced; no manufacturing result. | Translate validated timing and interface requirements into test/process specifications. |
| H — strategy/publication | Dated source watch and integration record added. | Keep regional ecosystem announcements separate from technical capability evidence. |

## Foundational and equation-discovery mapping

FND-001: no energy measurement or thermodynamic-gap result.  
FND-002: count syndrome data, output/logical-state information and reconstruction.  
FND-003: decoder latency is not a quantum-speed-limit result.  
FND-004: hybrid classical decoding is a known engineering component, not a new physical primitive.  
FND-005: no QFT/particle mechanism implied.  
FND-006 and EQN-001–006: no new equation or physical law is proposed by these provider announcements; testable system constraints and negative regimes are the useful outputs.

## INV-029–035

No mission-level gate passed. No material substitution, accepted bio-oil, net fusion electricity, principal/interest/WACC reduction, real-QPU advantage or Data-Center-to-One-Phone compression is established. INV-034/035 remain evidence-gated; provider announcements and simulated benchmark reports do not override present physical limits or constitute independent project evidence.

## Next highest-value gate

Reproduce the AWS simulated QEC-decoder benchmark with pinned code, dependencies, container, noise model and seeds. Compare MWPM and pre-decoder+MWPM at the same logical-error target, recording decoder latency distribution, GPU/host memory, syndrome transfer, retries, energy if measurable and cost per accepted logical operation. Keep real-QPU work simulator/dry-run first and require explicit user consent plus bounded budget for any paid execution.

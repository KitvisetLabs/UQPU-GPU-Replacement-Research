# Research Gap RG-PROVIDER-QEC-001 — provider-matched QEC and hybrid integration accounting

**Created:** 2026-10-26  
**Primary owner:** Lane B — provider integration  
**Implementation owner:** Lane A — workload contracts/runtime  
**Integration owners:** Lanes C/D/F/G; publication owner Lane H  
**Status:** OPEN — OFFICIAL PROVIDER SOURCES IDENTIFIED; UQPU REPRODUCTION NOT STARTED  
**Evidence class:** provider-reported benchmark + provider announcement; no UQPU evidence promoted

## Question

Can a provider-neutral workload contract capture the latency, accepted logical error rate, data movement and full cost of a hybrid QPU-plus-classical-decoder workflow without treating external GPUs, controllers, network links or provider services as free?

## Current evidence

- AWS's 2026-10-21 post reports NVIDIA Ising Decoding training across EC2 GPU instance types and simulated surface-code decoding validation. Its syndrome data are generated with Stim under a specified noise model; the reported distance-31 latency results are not a UQPU reproduction or a real-QPU system measurement.
- Quandela's 2026-10-13 NVQLink post describes a GPU/FPGA-controller/photonic-QPU integration demonstrator. The GTC Berlin QPU is simulated; the company refers separately to earlier physical-QPU integration validation without publishing a complete independently audited end-to-end ledger in this post.
- Quandela's 2026-10-22 Vietnam announcement describes a planned MosaiQ deployment and ecosystem program, not a confirmed operational UQPU target or published access/pricing route.

## Blockers

1. No pinned, independently reproduced Ising Decoding result with hashes, seeds, and complete cost/latency records.
2. No UQPU-compatible provider endpoint, target identity, SDK/API and current price verified for the announced Vietnam deployment.
3. No complete syndrome payload, controller/GPU transfer, queueing, retry, reconstruction and accepted-output ledger.
4. No same-noise, same-logical-error-target comparison across MWPM, pre-decoder+MWPM and alternative decoders.
5. No real-QPU or full-stack energy measurements.

## Unlock criteria

- [ ] Pin source repository, dependency versions, container, data generation and training configuration.
- [ ] Independently reproduce the simulated training/inference benchmark.
- [ ] Freeze noise model, code distance, syndrome access, logical-error acceptance and timing boundary.
- [ ] Record GPU type, memory, throughput, latency distribution, retries, controller/host work and cost per accepted logical operation.
- [ ] Distinguish simulated targets, physical targets and announced-but-not-yet-available deployments.
- [ ] Verify provider endpoint, modality, credentials, pricing and user authorization before any real execution.
- [ ] Preserve negative regimes where the decoder adds overhead or fails the logical-error gate.

## Promotion rule

Reproduction of the AWS simulated workload can only promote this gap to an independently reproduced simulation benchmark. It cannot establish real-QPU performance, quantum advantage, lower total cost than a competitive GPU/CPU baseline, or any material/fuel/fusion/finance benefit. Provider announcements alone do not establish availability or price.

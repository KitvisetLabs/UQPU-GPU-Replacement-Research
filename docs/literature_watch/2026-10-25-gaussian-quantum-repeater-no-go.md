# Literature watch — 2026-10-25: Gaussian quantum-repeater no-go boundary

**Accessed:** 2026-10-25  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Integration owner:** Lane F — evidence and architecture accounting  
**Publication integration:** Lane H  
**Feeds:** B/C/D/F; INV-027, INV-029, INV-034/035  
**Evidence class:** PEER_REVIEWED_PRIMARY_RESULT / LITERATURE_ONLY_FOR_UQPU  
**UQPU project evidence promoted:** none

## Source and date

Rabsan Galib Ahmed and Graeme Smith, “No-Go Theorem for Gaussian Quantum Repeaters from Fractional Extendibility,” *Physical Review Letters* 137, 170804, published 2026-10-23; accepted 2026-09-28; DOI 10.1103/5cyh-2mqf. Official source: https://journals.aps.org/prl/abstract/10.1103/5cyh-2mqf.

## Result and genuine novelty

The authors prove that a chain of repeater nodes restricted to Gaussian operations, homodyne measurements and classical communication cannot increase the quantum or private capacity of a pure-loss bosonic attenuation channel beyond direct transmission. They also state a no-improvement result for two-way capacities under arbitrary Gaussian LOCC. The proof introduces fractional extendibility for Gaussian states.

This is a theorem with a defined channel and operation class, not a universal impossibility result for every quantum-network architecture.

## Limits and evidence boundary

The theorem's scope is the stated pure-loss channel and Gaussian-operation family. It does not rule out all non-Gaussian operations, all channel models, all network protocols, or ordinary classical networking used by cloud-QPU APIs. It does not measure a provider's latency, reliability, billing, or workload quality. UQPU has not independently reproduced the proof and does not currently claim a quantum-repeater advantage.

## Exact UQPU relevance

- **Lane B:** if a future architecture assumes quantum repeaters improve end-to-end quantum communication, identify the operations/channel and check whether the proposed design lies inside this no-go scope before claiming a capacity gain.
- **Lane C:** quantum-channel capacity is not classical RAM/storage capacity. A network model still needs input/output bytes, latency, throughput, buffering and reconstruction accounting.
- **Lane D/G:** no photonic-device or manufacturing consequence follows unless a specific out-of-scope operation or different channel model is proposed and engineered.
- **Lane F / INV-029/033:** no phone-compression or finance claim follows. Any future network comparison must use the same useful-output contract and include repeater resources, classical support, failure probability and lifecycle cost.
- **INV-034/035:** a rigorous no-go result is a boundary to respect, not a prompt to hand-wave away established mathematics. A proposal outside its assumptions must state exactly which assumption changes and provide a discriminating capacity/observable test.

## Proposed falsifiable follow-up — QNET-GAUSS-001

Before any UQPU distributed-QPU or quantum-network claim relies on repeaters, record: channel model and transmissivity; permitted operations (Gaussian/non-Gaussian); measurement and feed-forward assumptions; direct-transmission baseline; end-to-end capacity/rate definition; failure budget; latency, memory, hardware and energy costs. If the architecture stays within the theorem's stated scope, do not claim repeater capacity improvement. If it leaves that scope, specify the changed operation or channel, derive a distinct quantitative prediction, and test it against direct transmission with independent verification.

**Current status:** LITERATURE_ONLY_FOR_UQPU. No change to current provider adapters, no paid job, and no network-capacity advantage claimed.

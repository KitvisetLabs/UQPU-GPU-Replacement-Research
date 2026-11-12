# Literature watch — 2026-10-25: Gaussian quantum repeater no-go theorem and network scope

**Accessed:** 2026-10-25  
**Primary owner:** Lane B — quantum cloud, QPU/provider and network integration  
**Integration owner:** Lane C — state, storage and data movement; Lane F — evidence  
**Feeds:** FND-002, FND-004, INV-027, INV-034, INV-035; conditional relevance to lanes B/C  
**Evidence class:** PEER-REVIEWED PRIMARY PAPER  
**UQPU project evidence promoted:** none

## Source and publication date

Rabsan Galib Ahmed and Graeme Smith, “No-Go Theorem for Gaussian Quantum Repeaters from Fractional Extendibility,” *Physical Review Letters* 137, 170804, published 2026-10-23; accepted 2026-09-28. DOI: https://doi.org/10.1103/5cyh-2mqf. Official publisher page: https://journals.aps.org/prl/abstract/10.1103/5cyh-2mqf

## Genuine result

The authors prove that, for pure-loss bosonic attenuation channels, a repeater chain restricted to Gaussian operations, homodyne measurements and arbitrary classical communication cannot improve quantum or private capacity beyond direct transmission. The paper also states a two-way-capacity no-go for arbitrary Gaussian local operations and classical communication among repeater nodes. The proof introduces a fractional-extendibility framework for Gaussian states.

This is a scoped impossibility theorem for a precisely described family of communication protocols, not a general theorem that quantum networking or all repeaters are useless.

## Assumptions and limitations

The theorem's scope is defined by the channel and allowed operations. It must not be extrapolated automatically to protocols that use non-Gaussian operations, a different channel model, additional resources or assumptions not covered by the proof. Those alternatives must be formulated explicitly rather than invoked as vague escape clauses.

The UQPU repository has no evidence that its cloud-QPU execution path depends on Gaussian repeater chains. Therefore this result is a conditional architecture constraint and literature finding, not a blocker to the existing provider-neutral software path.

## Exact UQPU relevance

- **Lane B:** if a proposed provider/network architecture relies on Gaussian repeater nodes over a pure-loss channel, compare it against direct transmission and identify the exact capacity metric before claiming a scaling benefit.
- **Lane C:** communication latency, loss, state preparation, storage and reconstruction remain separate costs. A repeater cannot be counted as an automatic capacity multiplier merely because it adds nodes.
- **FND-002 / FND-004:** record the theorem as a no-go boundary under stated assumptions; it does not alter general quantum-computing or classical memory lower bounds.
- **INV-029:** no direct evidence for or against physical data-center-to-phone compression; remote network infrastructure must still be counted.
- **INV-035:** if proposing a different physical/network model, state which theorem assumption changes, specify the alternative model and produce a discriminating observable. Do not call a hypothesis a law.

## Proposed falsifiable follow-up

If a UQPU network proposal uses repeaters, freeze: (1) channel transmissivity/noise model, (2) allowed Gaussian/non-Gaussian operations, (3) classical communication and entanglement resources, (4) target capacity/rate/fidelity, (5) direct-transmission baseline, and (6) total state-preparation, memory, measurement, communication and cost boundary. Verify whether the proposal falls within the theorem's assumptions before simulating it. A claimed improvement must survive a held-out parameter regime and independent implementation; if it changes an assumption, state the new observable and the experiment that could falsify the proposed gain.

No hardware execution, new physical law, quantum advantage or cost improvement is claimed.

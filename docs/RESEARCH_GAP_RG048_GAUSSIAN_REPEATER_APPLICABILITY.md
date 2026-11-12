# Research Gap RG-048 — Gaussian repeater theorem applicability to UQPU network proposals

**Opened:** 2026-10-25  
**Primary owner:** Lane B — quantum cloud/provider/network integration  
**Integration owner:** Lane C — state and data movement; Lane F — evidence  
**Related invariants:** INV-027, INV-029, INV-034, INV-035  
**Status:** LITERATURE_ONLY / CONDITIONAL_ARCHITECTURE_CHECK

## Objective

Prevent a proposed UQPU communication architecture from assuming that Gaussian repeater nodes automatically improve communication capacity over direct transmission on a pure-loss bosonic attenuation channel.

## Evidence

Ahmed and Smith, *Physical Review Letters* 137, 170804 (published 2026-10-23), prove a no-go theorem for Gaussian repeater chains with Gaussian operations, homodyne measurements and classical communication over pure-loss attenuation channels. The paper also bounds the two-way capacities for arbitrary Gaussian LOCC among repeater nodes. See `docs/literature_watch/2026-10-25-gaussian-repeater-no-go-scope.md`.

The theorem is peer-reviewed literature, not a UQPU experiment. No current project evidence shows that the provider-neutral cloud-QPU path uses such repeaters.

## Blockers / scope conditions

- No concrete UQPU network design is currently shown to fall within the theorem's exact assumptions.
- The channel transmissivity/noise model, allowed operations, resources and capacity metric must be stated before applicability can be decided.
- The result must not be generalized to non-Gaussian operations, different channel models or resources outside its scope without separate analysis.
- No direct conclusion about quantum computation, memory replacement or Data-Center-to-Phone physical compression follows from this communication theorem.

## Unlock criteria

1. For any repeater-based proposal, freeze the channel model, operation set, resource assumptions, capacity/fidelity target and direct-transmission baseline.
2. Check theorem applicability before simulation or cost modeling.
3. If a proposal claims an improvement, identify the precise assumption it changes and derive a measurable difference from the direct-transmission baseline.
4. Test that difference on held-out channel conditions and seek independent implementation/replication.
5. Include state preparation, measurement, memory, classical communication, retry, decoding and full lifecycle cost in the comparison.

Until such a design exists, this gap remains a literature-driven guardrail, not a reason to block unrelated QPU programming or provider integration.

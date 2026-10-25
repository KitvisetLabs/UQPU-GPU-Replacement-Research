# Research gap RG-040 — quantum-feedback side-information resource accounting

**Date opened:** 2026-10-26  
**Primary owner:** Lane F — economics, benchmarks and evidence  
**Cross-cutting owners:** FND-001 / FND-002 / FND-003; Lane A implementation; Lane C state/memory/data movement; Lane H publication  
**Evidence state:** `LITERATURE_ONLY`; proposed follow-up `NOT_IMPLEMENTED`  
**Project evidence promoted:** no  
**Canonical starting main:** `5fbe3d295ad6ca5b7c701f05c64899829910cbe8`

## Objective

Prevent a future UQPU quantum-feedback claim from treating quantum side information as a free classical record or from confusing a theoretical thermodynamic work bound with measured wall-plug energy, provider billing, or cost per accepted useful task.

## Evidence and scope

Ji, Gour and Wilde, “Fundamental limits for thermodynamic control with quantum feedback,” *Physical Review Letters*, accepted 2026-10-06, DOI 10.1103/x67n-33gr; authors’ arXiv manuscript 2503.09012, v4 revised 2026-10-09. The authors report single-shot work-of-formation and extractable-work bounds for quantum side information and an asymptotic generalized second law expressed through conditional Helmholtz free energy.

This is a literature result under stated operational assumptions. It is not a project measurement, an UQPU implementation, a new physical law, a quantum-advantage demonstration or evidence of lower energy/economic cost.

## Blockers

- The paper’s exact theorem, notation and assumptions have not yet been independently transcribed into a project implementation.
- No frozen finite-dimensional fixture compares quantum, classical/dephased and absent side information under the same Hamiltonian and state-transition contract.
- No controller resource ledger currently linked to this proposed work item records acquisition, preparation, retention, processing, transfer, measurement, reset/disposal and uncertainty together.
- No physical device, wall-plug energy, provider-billing or lifecycle-cost data exist for this proposed feedback path.
- A work bound alone does not establish a speedup, useful-task quality, lower cost, or an advantage over a competitive classical controller.

## Unlock criteria

1. Transcribe and pin the exact source theorem and assumptions from the public manuscript.
2. Independently implement the single-shot bounds and asymptotic limit for frozen qubit fixtures; test held-out parameter combinations and source-consistent limiting cases.
3. Include quantum-side-information, matched classical/dephased-record and no-side-information controls.
4. Fail closed when any side-information acquisition, memory/retention, controller processing, transfer, measurement or reset/disposal term is missing or the comparison boundary changes.
5. Keep thermodynamic work, wall-plug energy, provider charges and cost per accepted useful task as separate typed quantities.
6. Obtain independent review before any laboratory proposal. Paid QPU execution requires credentials, a bounded budget and explicit user consent.

## Best current alternative

Continue using the existing FND-001/FND-002 resource-accounting contracts without claiming a quantum-feedback benefit. Treat the new theorem as a specification for a future model-only test, not as a substitute for workload measurement or complete energy accounting.

## Next action

Implement FND-QFB-001 only after source-equation transcription. Cross-check it against the existing `fundamental_limits.py` and accepted-task ledger without overwriting canonical append-only histories. Record null results and any failure of the quantum-side-information case to improve the allowed work interval under a complete matched boundary. Do not update `RESEARCH_GAPS.md` from a partial read; this dated artifact is the traceable gap record.

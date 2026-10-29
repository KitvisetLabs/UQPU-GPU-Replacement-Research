# Research gap RG-A-RAG-PDCIM-MATCHED-001 — accepted-output QUBO comparison for near-memory RAG

**Opened:** 2026-10-29  
**Primary owner:** Lane A  
**Cross-lane interfaces:** B provider routing; C state/data movement; D/G device/process/packaging; E infrastructure; F economics/evidence; H publication  
**Status:** PREREGISTERED CONTRACT / NOT YET RUN  
**Related:** INV-025–027, INV-026, INV-029, INV-034/035, EQN-001–003, BIO-001, FUS-001, FIN-001

## Objective

Determine whether any UQPU/QAOA path can improve *accepted downstream RAG answer quality per full-stack cost* against classical and near-memory QUBO baselines on identical context-selection instances. The purpose is not to assume that quantum optimization beats the new classical silicon baseline.

## Current evidence

The official arXiv preprint [2610.37033](https://arxiv.org/abs/2610.37033), posted 2026-10-27, reports a fabricated 28-nm SRAM DCIM Ising macro and ten small direct-silicon QUBOs that reportedly reached brute-force optimum. Larger HotpotQA evaluations use a measurement-parameterized model; the HBM/HBF integration is proposed, not fabricated. UQPU has not independently reproduced these claims. See the source-specific [literature watch](literature_watch/2026-10-29-pdcim-near-memory-isings-for-rag.md).

## Blockers

- No frozen UQPU query/candidate/embedding/QUBO manifests or held-out group split exists for this comparison.
- No independently reproduced p-DCIM source dataset/silicon run is available in this project.
- No matched CPU/GPU/QAOA comparison under the same downstream answer-quality gate exists.
- The source's macro-normalized selection energy and modeled large-workload results cannot be treated as full-system measured energy.
- Provider billing, host orchestration, input/embedding preparation, data movement, retries, reconstruction, energy, cooling and capital/lifetime allocation are not yet jointly calibrated for this workload.

## Required unlock criteria

1. Freeze and hash the workload, QUBO, query split, acceptance contract, reference certificate and each target configuration before the run.
2. Verify feasibility and exact objective against brute force on small instances; retain counterexamples and failures.
3. Run CPU/GPU baselines and QAOA simulation on the same QUBOs and downstream generation configuration.
4. Keep p-DCIM direct-silicon observations distinct from its behavioral-model results; no model result may be relabeled silicon.
5. Preregister non-inferiority margins for exact match, Gold-Contains and token F1; require context-budget and task constraints.
6. Report total cost/energy per accepted answer with explicit measured/modelled/unknown components. Unknown is not zero.
7. Require independent reproduction before any comparative performance conclusion; require explicit user consent, credentials and bounded budget before paid QPU jobs.

## Falsifiers / stop conditions

The candidate path fails to show an accepted useful-task improvement if quality falls outside the frozen margins, feasibility/context-budget constraints fail, objective certificates disagree, held-out performance collapses, or full-stack cost/energy removes the apparent advantage. Stop promotion if source data cannot be reproduced or solver access models differ materially. A successful QUBO objective alone is not downstream answer acceptance.

## Non-claims

No UQPU or QPU advantage, no 100×/100,000,000× economics, no general GPU/CPU/NPU or RAM/VRAM/HBM/storage replacement, no new physical law, no Pangola-carbon substitution, no accepted bio-oil, no net fusion electricity, no lower WACC and no Data-Center-to-One-Phone milestone is established.

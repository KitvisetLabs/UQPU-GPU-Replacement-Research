# Literature watch — adaptive monitored circuits and mid-circuit feedback

**Access/update date:** 2026-10-23  
**Primary owner:** Lane H — literature synthesis  
**Integration owners:** Lane A (runtime semantics), Lane B (provider capabilities), Lane F (evidence and economics)  
**Evidence class:** \`PUBLISHED_EXTERNAL_EXPERIMENT\`  
**UQPU evidence promotion:** none

## Primary source and dated result

Bibek Pokharel et al., *Order from chaos with adaptive circuits on quantum hardware*, **Nature Physics**, version of record published 2026-10-09. Official publisher page: https://www.nature.com/articles/s41567-026-03470-6. Author preprint: https://arxiv.org/abs/2509.18259 (first submitted 2025-09-22).

The study reports adaptive monitored circuits on an IBM superconducting quantum processor with up to 100 qubits. It interleaves entangling operations with local mid-circuit measurements and resets, reporting nearly 5,000 entangling gates and 5,000 non-unitary mid-circuit operations. The experiment studies a quantum Bernoulli-map circuit in which scrambling competes with measurement-conditioned feedback and reports a dynamical transition between quantum-like and classical-like behavior.

## Genuine novelty for UQPU

The relevant systems lesson is that adaptive circuits are not equivalent to a static gate list followed by one terminal measurement. Runtime and provider adapters need explicit semantics for mid-circuit measurement results, reset, classical conditionals, feedback ordering, and target-specific dynamic-circuit limits. The external experiment gives a concrete workload family for capability-contract testing.

## Limits and evidence boundaries

- This is an experiment on a designed chaos-control protocol, not a demonstration of general-purpose fault-tolerant computation or arbitrary logical error correction.
- The observed transition does not prove that a useful UQPU workload has lower cost or better quality than a classical baseline.
- The publisher states that the experimental dataset and numerical simulations are available from the corresponding author on request because of their size; source-data CSV files are supplied for selected figures. Independent end-to-end reproduction is therefore not immediate from a fully public code/data bundle.
- This publication does not establish that every IBM target, any other provider, or the UQPU adapters support the required dynamic-circuit semantics.
- The paper supplies no UQPU accepted-task economics, Data-Center-to-One-Phone result, new fundamental law, material substitution, bio-oil result, fusion-electricity result, or finance/WACC result.

## Exact project relevance

- **A — programming/runtime:** model mid-circuit measurement, reset and conditional branches as explicit IR operations with validation and deterministic fallback behavior.
- **B — cloud/QPU:** require target-specific official capability evidence and API/version provenance; never infer support across providers.
- **C — memory/data movement:** account for classical measurement records and feed-forward state; this does not make a quantum state readable classical RAM/VRAM/storage.
- **D/G — device and manufacturing co-design:** future control-loop latency, calibration and packaging requirements must come from target-specific measurements, not the paper's qubit count alone.
- **E — biomass/materials/energy:** no new material, fuel, cooling or fusion evidence.
- **F — economics/evidence:** compare complete accepted-task quality and cost, including host feedback, shots, retries, transfer and billing.
- **H — strategy/publication:** preserve the result as external experimental evidence without upgrading mission claims.

## Falsifiable follow-up

Use the new provider-neutral contract in \`integration/adaptive_circuit_capability_contract.md\` and its executable validator. For each named target, freeze source URL, checked timestamp, source digest, API version, mid-circuit measurement/reset/conditional support, documented limits and latency when measured. Then test a small deterministic feedback workload with positive and negative branches on simulator/dry-run before any separately authorized hardware attempt.

Reject route construction if a capability is unknown, provenance is stale/missing, or the target/API cannot express the same branch semantics. Reject any advantage claim unless the same useful-output contract beats a competitive classical control baseline after full host, I/O, latency, billing, retries and energy accounting. Do not combine one provider's output quality with another provider's price.

## Next gate

Build and validate the per-target capability matrix, then use simulator/dry-run tests to check branch semantics. Paid or billable QPU execution remains disabled absent credentials, a bounded budget and explicit user consent.

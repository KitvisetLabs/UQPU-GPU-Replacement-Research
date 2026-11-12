# Literature watch — 2026-10-24: task-resolved Fisher spectroscopy for measurement and feature budgets

**Primary owner:** Lane H — strategic research and publication  
**Cross-lane consumers:** Lane A (workload/runtime), Lane C (state, measurement records and feature storage), Lane F (benchmark/economics)  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`  
**UQPU reproduction:** `NOT EXECUTED`  
**Hardware/provider execution:** `NONE`  
**Related:** INV-025–027, INV-029, INV-034–035, FND-001–003, FND-006, EQN-001–006

## Primary source and date

Yang Peng, “Task-Resolved Fisher Spectroscopy for Quantum Reservoir Computing,” arXiv:2609.29570, submitted 26 August 2026. Official preprint: https://arxiv.org/abs/2609.29570.

The paper proposes task-score coordinates derived from the prediction targets and uses them to compare three distinct layers: state-level quantum Fisher information (QFI), classical Fisher information in the complete measurement record, and information retained by features truncated at a selected many-body order. Its numerical demonstration uses a five-spin open quantum reservoir. The author reports that low-order feature compression can require orders-of-magnitude more sampling to recover some higher-order temporal information, while a conventional parity target can remain accessible.

## Genuine methodological delta

A single benchmark error or nominal feature count cannot identify whether a temporal task is limited by (1) the reservoir state, (2) the chosen measurement, (3) compression of measured records into classical features, or (4) finite-shot sampling. The paper offers a task-resolved diagnostic intended to separate those losses using stationary labeled records and measured outcome strings, without requiring quantum-state tomography for its measurement-level quantities.

For UQPU, this creates a concrete Lane-C interface: bind information matrices to an immutable task-score basis, workload/model ID, train/validation/held-out split digest, measurement protocol, shot budget and feature-order cutoff. Measure retained-feature bytes and the number of shots/measurement settings needed to reach the same accepted prediction quality. The byte ratio is a classical record/feature representation metric; it is not quantum Hilbert-space dimension and does not imply readable quantum memory.

## Evidence class and limitations

- The result is a third-party preprint with a numerical open-spin-reservoir study. It is not an independent UQPU reproduction, real-QPU result, commercial device result or universal theorem about all reservoirs.
- The five-spin example and chosen target family do not establish that the same feature-order or shot trade-off generalizes to other tasks, devices, noise levels or providers.
- Fisher matrices estimated from finite records can show apparent hierarchy violations from sampling error, model mismatch or incompatible score bases. Such violations must be reported with uncertainty and investigated, not hidden or promoted to a new physical law.
- A feature-count or byte reduction alone is not useful-output equivalence. Held-out quality, latency, throughput, shot/measurement cost, host reconstruction, memory/data movement and total cost per accepted task must be compared.
- The project has not run the source code, downloaded or hashed source artifacts, reproduced the five-spin study, measured energy, or invoked any cloud provider. Unknown energy/cost is not zero.

## Falsifiable UQPU follow-up

1. Audit the full preprint, source code and licensing; pin code/environment/data-generation provenance and SHA-256 hashes before execution.
2. Freeze one task-score basis and separate train, validation and blind held-out histories. Preserve target generation, washout, normalization, prediction horizon, precision, seeds and quality threshold.
3. Reproduce the source's five-spin numerical result before changing the protocol. Save failed reproductions and all seeds.
4. Compare complete measured bit-string records against feature truncation orders (r=1,2,ldots) and at least two shot budgets. Use the same histories and acceptance predicate for every arm.
5. Record QFI, complete-record Fisher information and retained-feature matrices in the same score coordinates; report matrix uncertainty and test the expected information hierarchy. Keep exact/analytic matrices distinct from estimated matrices.
6. Report held-out NRMSE or the preregistered task metric, accepted prediction windows, shots per history, measurement settings, raw-record and feature bytes, host compute, latency/throughput, reconstruction, energy when measured, and total cost per accepted window. Use one provider/target price context per record.
7. Compare against a tuned classical reservoir and a simple baseline under a matched total resource budget. Do not treat exact expectation values from a simulator as free hardware readout.

**Falsifiers / negative outcomes:** the feature-order diagnosis fails to predict held-out quality; the apparent information hierarchy depends on score-basis leakage; finite-shot overhead erases any storage/readout benefit; the classical baseline reaches the same quality at lower cost; or independent replay fails. These outcomes close or narrow the hypothesis rather than justify changing the acceptance rule after inspecting held-out data.

## Exact mission and lane relevance

- **A:** workload semantics and accepted prediction contract; same task and quality across feature orders.
- **B:** provider-neutral only; no provider calls or paid QPU jobs.
- **C:** primary technical consumer; quantify raw record, retained-feature bytes, state/I/O and shot budget without equating Hilbert-space dimension with readable memory.
- **D:** no device requirement changes until a repeatable target-specific measurement effect is established.
- **E:** no new Pangola-carbon, bio-oil, fusion, cooling or energy evidence; only a future measurement-accounting interface.
- **F:** quality-adjusted cost per accepted task and uncertainty, with energy/cost unknown when unmeasured.
- **G:** no fabrication-tool, process-window or yield claim; D/G co-design remains downstream of validated device requirements.
- **H:** preserve provenance and strategic context; no funding, WACC or commercialization claim follows from this paper.
- **I (repository specialist lane):** no causal link to contactless vehicle-lift research is established by this result.

## Foundational and invariant traceability

- **FND-001:** adds a measurement-budget input to future thermodynamic-gap accounting; no energy gap was measured here.
- **FND-002:** directly motivates task-specific output-information and representation accounting; it does not weaken any information lower bound.
- **FND-003:** supplies a possible observable for later matched controls, but no speed-limit experiment was performed.
- **FND-004/005:** no new physical primitive or particle/QFT mechanism.
- **FND-006 / EQN-001:** advances literature surveillance and a testable measurement-model workflow. EQN-002–006 remain subject to their existing proof, held-out, experiment and independent-validation gates.
- **INV-029:** improves the specification for state/output/data-movement accounting only; no phone-class physical-compression result.
- **INV-030–033:** no direct material, accepted liquid-fuel, net fusion-electricity or financing evidence.
- **INV-034–035:** a new analysis method is a candidate diagnostic, not a new law. Current physics remains binding.

This watch is intentionally separate from any root-level append-only ledger. The permanent 00–06 directives, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and Thai/English/Chinese/Japanese/Korean/German public master-plan references remain unchanged.

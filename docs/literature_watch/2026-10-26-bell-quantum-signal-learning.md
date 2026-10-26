# Literature Watch — Bell Quantum Signal Learning and matched advantage accounting

**Audit date:** 2026-10-26  
**Source publication date:** 2026-10-23  
**Primary owner:** Lane A — workloads / algorithm contracts  
**Integration owners:** Lanes B, C, D, F and G; publication owner Lane H  
**Evidence class:** PEER_REVIEWED_THEORY_AND_INFORMATION_THEORETIC_ANALYSIS  
**Project status:** EXTERNAL_RESULT_NOT_INDEPENDENTLY_REPRODUCED_BY_UQPU

## Primary source

Jordan Cotler, Daine L. Danielson and Ishaan Kannan, “Quantum Advantage for Sensing Properties of Classical Fields,” Physical Review X 16, 041025 (2026), published 2026-10-23. DOI: 10.1103/6ps1-mw9l. Official APS article: https://journals.aps.org/prx/abstract/10.1103/6ps1-mw9l. The authors' arXiv preprint is https://arxiv.org/abs/2602.17591.

The paper introduces Bell quantum signal learning (QSL): a bosonic sensing protocol using two-mode squeezing, passive optics and static homodyne measurements to estimate multiple predeclared properties of a classical signal from the same experimental dataset. The authors prove query-complexity separations for specified sensing tasks, including worst-case exponential separation from entanglement-free strategies, and report practical comparisons relative to homodyne/heterodyne baselines.

## Genuine novelty for this repository

The result is a concrete candidate workload for a matched useful-output and resource-accounting benchmark, rather than another generic quantum-algorithm claim. The same data stream can support post-hoc estimation of multiple properties, so the benchmark must compare a vector-valued accepted output—not a single cherry-picked scalar—against the best eligible classical/entanglement-free baseline. It also makes squeezing and entanglement explicit resources rather than free preprocessing.

A search of the current canonical repository for the article title and its distinctive “quantum signal learning” phrase returned no matching indexed artifact. This watch records a new-to-canonical literature delta; it does not imply priority over work on other branches.

## Resource-normalization caveat found in the source

The preprint's Appendix E.4 distinguishes entanglement-enabled Bell-QSL results from a separate squeezing-only example. In that squeezing-only construction, choosing the squeezing parameter as (r = \frac{1}{2}\log n) gives mean photon number \(\bar n = \sinh^2(r) = \Theta(n)\). The associated exponential sample-complexity separation therefore uses a probe-energy budget that grows with instance size; it must not be described as a fixed-energy advantage. The preprint explicitly discusses how a fixed energy budget bounds (r) and changes the interpretation of that squeezing-only lower-bound argument.

This is a crucial comparator distinction, not a refutation of the paper's separate entanglement-enabled Bell-QSL results. The benchmark must transcribe each theorem's exact assumptions and keep (a) equal-total-probe-energy comparisons, (b) comparisons that treat squeezing as a separately budgeted resource, and (c) source/pump wall-plug energy as distinct ledgers. Mean probe photon number is not a substitute for electrical energy used to generate and stabilize squeezing.

## Exact UQPU relevance

- **Lane A:** candidate sensing/property-learning workload and common output contract; not evidence that a general-purpose QPU replaces GPU/CPU/NPU tasks.
- **Lane B:** target eligibility must be modality-aware. A gate-model provider cannot be treated as a bosonic photonic or oscillator platform without a documented encoding, controls and equivalent-output mapping.
- **Lane C:** account for signal capture, sampling, data movement, reconstruction, storage and post-hoc classical processing. Hilbert-space dimension is not readable classical storage.
- **Lane D:** optical/oscillator sources, squeezing, detector efficiency, losses, bandwidth and calibration are device requirements to measure, not assume away.
- **Lane E:** include the energy and infrastructure cost of squeezing/source generation, pumps, detectors and any required cooling when physically applicable.
- **Lane F:** compare total cost, energy and wall-clock time per accepted property-vector estimate against a matched baseline. Keep theorem-level query complexity separate from practical end-to-end cost.
- **Lane G:** only after validated control requirements exist, translate them into source, detector, packaging, calibration and manufacturing/yield constraints.
- **Lane H:** publish negative and positive results with the strategic plan intact; no economic or mission-level promotion follows from the paper alone.

## Limitations and non-claims

The source's query-complexity theorem is scoped to its formal sensing model, signal/task family, access assumptions and comparison classes. It is not automatically a hardware benchmark. Practical performance depends on the resource convention, squeezing generation, loss, finite bandwidth, detector inefficiency, control calibration, signal acquisition, classical estimation and the chosen quality threshold. An asymptotic separation does not itself establish an exponential wall-clock, energy or cost advantage in a finite device.

UQPU has not independently reproduced the proof, run the protocol, accessed a sensing provider, or measured a device. No real-QPU advantage, physical-law discovery, lower electricity cost or Data-Center-to-One-Phone result is claimed.

## Proposed falsifiable follow-up

1. Extract the exact theorem assumptions, property family, oracle/query model, signal prior, resource units and comparator class from the paper and supplemental material.
2. Freeze a vector-valued output contract: property names, estimator, error/loss, confidence intervals, acceptable failure rate and held-out signal distribution.
3. Independently implement the smallest analytically checkable instance and a simulator for the Bell-QSL protocol; validate covariance/noise propagation against a separate calculation.
4. Compare with homodyne, heterodyne and the strongest eligible entanglement-free baseline at equal task quality, signal access, bandwidth, acquisition duration and declared resources. Report both resource-explicit and full end-to-end accounting. Explicitly label any instance-scaled squeezing-energy convention.
5. Hold out signal shapes, correlations, phases and noise parameters. Include detector loss, finite squeezing, calibration drift, finite bandwidth and reconstruction overhead. Record failed regimes and uncertainty.
6. **Falsifier:** the practical advantage fails if it disappears under matched resource accounting, fails the preregistered output-quality gate, does not generalize to held-out signals, or is dominated in total cost/energy/latency by the strongest eligible baseline. Any exponential separation that relies on uncharged instance-scaled probe energy fails the corresponding fair-comparison claim.
7. Only after simulator and independent-SDK checks, consider target-specific execution. No paid QPU job without credentials, a bounded budget and explicit user consent.

## Cross-cutting foundation mapping

- **FND-001:** measure source/control/readout energy and any thermodynamic gap; no Landauer or wall-plug claim from query counts alone.
- **FND-002:** count the number and precision of classical output values plus reconstruction and confidence reporting.
- **FND-003:** do not call a query-complexity separation a quantum-speed-limit violation; matched physical controls and time are separate.
- **FND-004:** bosonic squeezed-light/entanglement protocols are an alternative computational/sensing primitive within known physics, not a new law.
- **FND-005:** no elementary-particle or QFT mechanism is implied.
- **FND-006 / EQN-001–006:** theorem assumptions -> independent model -> held-out tests -> counterexamples -> experimental discriminator -> system consequences -> economics.

## Literature-surveillance notes

The same surveillance pass checked symbolic regression and equation discovery (including MorphingNet, already represented by pending PR #117), AI-generated mathematical instruments (already covered by canonical Batch 062), physics-informed/automated modeling, new effective laws, lower bounds and credible experimental anomalies. Existing or pending results were not relabeled as newly merged evidence. This Bell-QSL article is the selected new coverage candidate for this cycle.

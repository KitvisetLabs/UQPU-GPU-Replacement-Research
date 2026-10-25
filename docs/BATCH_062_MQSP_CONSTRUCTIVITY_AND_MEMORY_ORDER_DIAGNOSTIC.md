# Eight-Lane Research Batch 062 — M-QSP constructivity and memory-order diagnostics

**Cycle date:** 2026-10-25  
**Canonical starting main:** b51900f31b5175e1b844d4a4c8e3ee2ef5b1d9cd  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owners:** Lane C — memory/state/data movement; Lane F — evidence/economics  
**Publication owner:** Lane H  
**Evidence class:** numerical algorithm prototype + unit tests + MODEL_ONLY synthetic benchmark + literature-only analysis  
**Promotion:** no real-QPU, quantum-advantage, physical-law, material, fuel, fusion-electricity, energy or economic claim promoted

## Starting-state and invariant audit

The current main tree was inspected before this work. The required charter, version invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, newest Batch documents, gaps and current Actions state were reviewed. Batches 056–061 and gaps RG-028, RG-036 and RG-037 were inspected. All eight high-visibility root directives (00, 00A and 01–06) are present. The multilingual Thai, English, Chinese, Japanese, Korean and German public master-plan links remain in STRATEGIC_PLAN_REFERENCES.md. INV-025/026/027 and INV-029–035 remain preserved; the additional permanent invariants remain in the canonical registry.

At the starting head b51900f, the latest prototype workflow run 40160702332 completed successfully: all 15 listed jobs passed, including Python 3.10/3.11/3.12, reference benchmark, QSP synthesis/reconstruction, Qiskit verification, bounded QSVT prefixes, routed probes, target snapshot identity, no-submit transpilation and target-noise checks. The cold-start handoff check on the same head passed. The new commit's own Actions state must be checked after publication; baseline CI does not pre-validate new code.

## Highest-value Lane A delta — numerical M-QSP-CDA transcription

The new module software/uqpu-prototype/uqpu/mqsp_constructivity.py transcribes the recursive structure of Algorithm 1 from Ito, Mori, Sakamoto and Fujii, “Polynomial time constructive decision algorithm for multivariable quantum signal processing,” Quantum 10, 2102 (published 2026-05-12; DOI 10.22331/q-2026-05-12-2102; arXiv:2410.02332v3).

The recursion:
1. checks the zero-step base condition (constant unit-modulus P and Q=0);
2. removes two nominal steps when the total degree permits the theorem's recursion;
3. otherwise searches a variable whose leading coefficient polynomials admit a unit-modulus phase ratio;
4. applies the inverse signal/phase transformation and recurses;
5. returns a numerical candidate witness containing zero-based signal indices and phase angles.

This is an intentionally bounded first implementation, not an exact or formally verified reproduction. The paper itself warns that finite-precision matrix computations can accumulate numerical error and may be unstable in practice. The module therefore uses an explicit tolerance, labels its result a candidate, and requires independent witness reconstruction. A negative result near tolerance boundaries is not a proof of infeasibility.

The new tests include:
- one-variable, one-signal feasible pair generated independently from the circuit definition and reconstructed from the returned witness;
- two-variable, two-signal feasible pair with independently generated Laurent-polynomial coefficients and witness reconstruction;
- a zero-step non-unit scalar negative control derived from the definition;
- term-insertion-order invariance;
- fail-closed malformed-input checks.

Local isolated test result: 5/5 passed. The full theorem-scoped gate is not closed: a published nontrivial infeasible counterexample, exact-arithmetic checks, tolerance sweeps and an independent implementation remain required. No provider lowering or QPU job was performed.

## Foundational / Lane F delta — FND-001 memory-order diagnostic

The new helper software/uqpu-prototype/uqpu/thermodynamic_memory_order.py estimates adjacent-lag conditional mutual information from discrete sequences. A frozen synthetic benchmark covers:
- a first-order binary Markov chain with P(stay)=0.9, seed 1729, length 30,000;
- a second-order noisy-XOR process with independent flip probability 0.03, seed 2718, length 30,000.

The resulting profiles are recorded in benchmarks/results/fnd001-memory-order-cmi-synthetic-2026-10-25.json. The first-order fixture has CMI 0.51472338, 0.00014050 and 0.00020681 bits for conditioning orders 0–2. The second-order fixture has 0.00002509, 0.80845387 and 0.00010050 bits.

The contrast validates only that this statistic separates these selected known-truth synthetic cases. Adjacent-lag CMI is not entropy production and does not prove Markov order. No confidence intervals, finite-sample correction, calibrated threshold, heat, wall-plug energy or real-system thermodynamic estimate is provided. New gap RG-038 records the blockers and unlock criteria.

## Literature delta

A fresh search incorporated Ying Xie's arXiv preprint “What the Machine Invented” (arXiv:2610.17090, submitted 2026-10-12). It describes an instrument-level review of selected AI-generated mathematical manuscripts and explicitly notes provisional novelty judgments and that no Lean development was compiled or kernel-checked for that survey. The new literature watch records why instrument extraction, prior-art checks, formal statement faithfulness and kernel verification should be separate gates. It does not certify the underlying AI-generated claims.

The peer-reviewed M-QSP-CDA paper remains the direct algorithm source. Related October M-QSP preprints already recorded in the repository are not treated as new project evidence.

A second material method result was recorded in the new formalization-faithfulness watch: Bastounis, Circelli and Hansen (arXiv:2610.08144, submitted 2026-10-06) argue that the Lean formalization accompanying the September 8 Navier–Stokes announcement does not semantically match its natural-language proof; they do not claim the natural-language proof is false. A Communications Physics editorial published 2026-10-14 separately explains why a continuum singularity does not imply an observed infinite velocity in real fluid outside the continuum model's validity range. This is a verification/effective-theory boundary, not a new physical anomaly.

A third method source was recorded for Lane E: Varughese et al., arXiv:2609.16526 (submitted 2026-09-15), report a weighted symbolic ensemble of aluminum interatomic potentials that improves agreement with DFT across several property families. The paper is a computational preprint, not experimental evidence for biomass-derived carbon or functional material substitution. Its actionable contribution is a multi-property, held-out validation template for future material candidates; the new literature watch records a falsifiable follow-up and the limits of DFT-only evidence.

No new physical equation or credible mission-relevant anomaly was established this cycle.

## A–H status

- **A — Quantum programming/workloads/compiler/runtime:** numerical M-QSP-CDA prototype and independently reconstructed feasible fixtures added. Exact arithmetic, theorem-derived nontrivial negative fixtures, adversarial/tolerance tests and independent implementation remain open.
- **B — Cloud/QPU/provider integration:** no provider interface, target pricing or hardware claim changed. Simulator/dry-run policy remains; no paid job submitted.
- **C — RAM/VRAM/HBM/storage/state/data movement:** temporal-memory diagnostic added; it does not equate Hilbert-space dimension with readable classical storage and does not measure actual I/O or energy.
- **D — Devices/chip/process/fabrication/packaging:** no device or fabrication result. Native-gate/control requirements remain downstream of validated algorithm lowering; D/G co-design is retained.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** latest lithium-retention/FUS-001 evidence map and Pangola/bio-oil tracks remain active; this cycle adds no accepted-fuel, material-substitution, net-electricity or cooling measurement.
- **F — Economics/benchmarks/evidence/integration:** added a reproducible synthetic CMI result and explicit finite-sample limitations; no cost or thermodynamic advantage measured.
- **G — Manufacturing equipment/software/factory systems:** no new manufacturing evidence; future requirements remain contingent on validated device and process windows.
- **H — strategic/financial/future-industry research and publication:** published this batch, a dated AI-mathematics literature watch, RG-038 and integration INT-20261025-018. Strategic plan links and root directives remain intact.

Auxiliary Lane I remains auxiliary and does not replace A–H. Directory-depth policy remains unchanged.

## Foundational and equation-discovery status

- **FND-001:** advances a synthetic known-truth memory-order diagnostic; entropy production, heat and wall-plug energy remain unmeasured.
- **FND-002:** no new readable-output-information lower bound; quantum state-space size is not classical storage.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new QFT/particle mechanism or credible anomaly established.
- **FND-006:** algorithm and formal-proof methods are mathematical tools, not new physics.
- **EQN-001–006:** the literature watch strengthens instrument-level provenance, prior-art and formalization gates; no AI-generated equation is promoted as a physical law.

## INV-029 through INV-035

- **INV-029:** Data-Center-to-One-Phone remains the highest physical-compression mission; this batch does not close service, energy, physical-support or lifecycle-cost contracts.
- **INV-030:** no Pangola carbon substitution/recovery/hybridization result and no elemental-transmutation claim.
- **INV-031:** no accepted biomass liquid-energy product, yield/upgrading or full-cost closure.
- **INV-032:** no reliable net delivered fusion-electricity or full lifecycle-cost result.
- **INV-033:** no measured financed-principal, interest, time-to-evidence or WACC change.
- **INV-034:** strengthens theorem-scoped algorithm checks and calibrated inference gates without claiming a new physical result.
- **INV-035:** keeps mathematical generation separate from formal proof, numerical robustness, physical validation and engineering evidence.

The 100x and 100,000,000x targets, universal subsystem replacement, commercial low-cost bio-oil/fusion and phone-class physical compression remain goals. Provider-specific probability/price mixing is not used.

## Sync and next highest-value gates

Large append-only RESEARCH_GAPS.md and WORKLOG.md were not rewritten from partial reads. RG-038 and this dated batch preserve the new work without risking history truncation.

Next gates:
1. Add the published nontrivial M-QSP counterexample as a frozen negative fixture; cross-check the numerical recursion against an independent implementation and tolerance sweeps.
2. Expand synthetic CMI calibration across sample lengths, alphabet sizes and memory orders; preregister uncertainty and false-classification thresholds.
3. Keep provider-neutral lowering, target-aware resource accounting, accepted useful-output tests and total cost per accepted task downstream of the mathematical gate.
4. Continue BIO-001, FUS-001 and FIN-001 with measured end-to-end mass, energy, lifecycle cost and financing inputs rather than MODEL_ONLY scenarios.

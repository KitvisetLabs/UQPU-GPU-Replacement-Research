# Literature watch — dimensionality-aware and adaptive equation discovery

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance and publication  
**Cross-lane interfaces:** A (equation/workload acceptance), C (state and data volume), D/G (device and process models), E (materials/energy constitutive models), F (matched-budget evidence and economics)  
**Evidence class:** EXTERNAL_PREPRINT / LITERATURE_ONLY; no UQPU reproduction  
**Related:** INV-034–035, FND-006, EQN-001–EQN-008

## Sources and dated observations

1. **Gah, “SymFM: Physics-Informed, Dimensionality-Aware Symbolic Regression for Governing Equation Discovery in High-Dimensional Nonlinear Dynamical Systems.”** Zenodo preprint v1, published 2026-08-25, DOI [10.5281/zenodo.22093560](https://doi.org/10.5281/zenodo.22093560); [released code and experiment notes](https://github.com/Eddiegah/SymFM).
2. **Wang et al., “LLM-Based Scientific Equation Discovery via Physics-Informed Token-Regularized Policy Optimization” (PiT-PO).** [arXiv:2602.10576](https://arxiv.org/abs/2602.10576), version 2 listed 2026-07-27. This is an arXiv preprint, not independent project evidence.
3. Context checked against **STRIDE** [arXiv:2605.17790](https://arxiv.org/abs/2605.17790) and **LLM-PySR search control** [arXiv:2607.04156](https://arxiv.org/abs/2607.04156), already covered by earlier UQPU watches. The new delta is a more explicit dimensionality-reduction / partial-observation pipeline and an adaptive policy-optimization candidate generator, not a claim that equation discovery is solved.

## Genuine methodological contribution

SymFM reports a pipeline of (i) reconstructing latent system state from partial/noisy observations, (ii) learning a sparse active subspace to reduce the dimension of the symbolic search, and (iii) extracting interpretable equations through a hierarchical KAN head and symbolic post-processing. Its authors explicitly state that the proposed physics-informed Transformer/foundation encoder is **not implemented** and that the reported results do not depend on it. The released repository also documents a prior SEIRD chronological-split/near-zero-denominator metric artifact, preserves the original result, and reports a corrected representative split; this transparency is useful, while the correction still needs independent reproduction.

The authors report exact-structure recovery for selected benchmarks including a 1,024-dimensional Navier–Stokes case under their metric, but report **0% exact equation recovery** on the tested SEIRD cases at their strict tolerance. This mixed result is important: reducing effective dimension may help search, but neither a high-dimensional success case nor state-estimation accuracy guarantees equation identifiability or generalization.

PiT-PO proposes adapting the language-model candidate generator using policy optimization, hierarchical physics constraints and token-level penalties against redundant structures. Its abstract reports benchmark gains and turbulence-model discovery. Until code, datasets, training configuration, budgets and held-out evaluation can be pinned and reproduced, these remain source-reported claims. A language-model score or reward cannot certify physical truth.

## Limitations and evidence boundary

- These are external method reports; no UQPU implementation, independent reproduction, material model, fuel-yield model, fusion model, theorem or physical law is validated by this watch.
- The SymFM foundation encoder is a designed but unimplemented component. Its demonstrated pipeline is the implemented state estimator, active-subspace projection and symbolic head.
- Equation recovery is non-identifiable when observations, excitation, symmetries or parameter coverage are insufficient. Dimensional reduction can discard a physically important variable; it must be tested by reconstruction error and counterexample search, not accepted by sparsity alone.
- A fit, symbolic expression, reward, formal proof of a chosen model, or numerical solver convergence does not establish that the model describes nature.
- PiT-PO's claims are not treated as established superiority; exact training/evaluation versions and resource parity require audit.

## Exact UQPU relevance

- **FND-006 / EQN-001–006:** use active-subspace and adaptive-generation ideas only as candidate-generation arms. Keep the incumbent model, units, symmetry, conservation, causality and limiting cases explicit. EQN-007 must continue to separate formal validity from physical prediction; EQN-008 must enforce matched resources and grouped held-out tests.
- **Lane A:** candidate equations may support workload cost models and compiler/runtime policies only after semantic and held-out acceptance. The current signed-Max-Cut pinned-SDK gate remains algebraic semantics, not a quantum algorithm or accepted-task advantage.
- **Lane C:** report latent-state dimension separately from bytes, addressability, state-preparation cost and output reconstruction. A reduced latent representation is not equivalent to RAM/VRAM/HBM/storage.
- **Lanes D/G:** any proposed device/process constitutive relation must preserve identifiable process variables and be validated against independent device or manufacturing data; no fabrication advantage follows from a fit.
- **Lane E / BIO-001 / FUS-001:** potential use is limited to testable surrogate candidates for biomass mass/energy balances, pyrolysis/upgrading, heat transfer, plasma/thermal-fluid auxiliaries or cooling. Fuel acceptance and fusion success still require full mass/energy balance and net delivered electricity.
- **Lane F / FIN-001:** compare methods on wall time, CPU/GPU/accelerator time, peak memory, candidate evaluations, generated tokens, model/API calls, retries, proof/checker time, false discoveries, abstentions and cost per accepted equation. Do not translate tokens to dollars without a dated pricing basis; no WACC reduction is inferred.

## Falsifiable follow-up protocol

1. Freeze a known-law synthetic suite plus at least one independent, physically meaningful benchmark. Pin source commits, environments, data hashes, preprocessing, grammar, unit schema, acceptance rule and split manifests.
2. Compare at equal hard ceilings: numerical symbolic regression baseline, LLM-PySR search control, an independently implemented staged/progressive search, SymFM-style active-subspace plus symbolic head, and PiT-PO only if its runnable implementation/configuration becomes available. Do not use the withdrawn/contested CoSR source as a validated positive result.
3. Preregister at least 30 seeds per method and grouped held-out tests across law family, scale, geometry or device/material family. Keep train/validation/test groups disjoint.
4. Require exact symbolic or tolerance-defined recovery, held-out predictive error, dimensional consistency, symmetry/conservation/causality checks, limiting-case checks, adversarial counterexamples, false-discovery and undecided counts, and independent review. Track any dimensionality reduction that removes a required variable.
5. Publish all failed runs and raw records. Only after independent reproduction may a candidate be promoted to a device/system test; technology/economic claims still require separate end-to-end evidence.

**Decision:** add these methods to the candidate portfolio, not the truth-selection authority. Established physical laws remain binding for present engineering claims. No new physical law, quantum advantage, material substitution, accepted liquid fuel, net fusion electricity, financing-rate reduction or Data-Center-to-Phone milestone is claimed.

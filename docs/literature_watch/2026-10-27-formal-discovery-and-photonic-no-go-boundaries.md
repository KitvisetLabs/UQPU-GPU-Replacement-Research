# Literature watch — 2026-10-27: verified theorem discovery, photonic repeater limits, and physics-informed models

**Accessed:** 2026-10-27  
**Primary publication owner:** Lane H  
**Implementation owners:** Lane A for formal/equation contracts; Lane B/C for quantum-network and data-movement boundaries; Lane D/E for physical-model candidates; Lane F for evidence and matched comparisons  
**Feeds:** FND-001–006; EQN-001–006; INV-029–035; lanes A–H  
**Evidence class:** PEER-REVIEWED PRIMARY RESULT + OFFICIAL PREPRINTS + PUBLIC DATASET METADATA  
**UQPU evidence promoted:** none

## Executive delta

This surveillance pass found a newly published quantum-network no-go result and two useful methodological candidates for the project's formal-discovery and physics-informed-modeling pipeline. It also pinned metadata for a public symbolic-regression dataset candidate. None of these sources demonstrates a UQPU advantage, a new physical law, a qualified material, saleable bio-oil, net fusion electricity, or a project-finance improvement.

## 1. Gaussian quantum repeaters: a precise no-go boundary

**Primary source:** Rabsan Galib Ahmed and Graeme Smith, “No-Go Theorem for Gaussian Quantum Repeaters from Fractional Extendibility,” *Physical Review Letters* 137, 170804, published 2026-10-23. [APS article and DOI 10.1103/5cyh-2mqf](https://journals.aps.org/prl/abstract/10.1103/5cyh-2mqf).

**Reported result:** for a pure-loss bosonic attenuation channel, a repeater chain restricted to Gaussian operations, homodyne measurements, and arbitrary classical communication cannot raise quantum capacity beyond direct transmission. The work introduces fractional extendibility for Gaussian states to establish the bound.

**Genuine novelty for this cycle:** this is a current, peer-reviewed no-go boundary that can be encoded as a specific architecture filter for photonic networking and quantum data movement. It is more useful than a vague statement that “quantum repeaters may be hard”: the theorem names the channel class and permitted operations.

**Scope and limitations:** this is not a no-go theorem for every repeater architecture, all optical channels, non-Gaussian resources, every communication task, or every physical implementation. The cycle did not independently reproduce the proof or measure a device. The result does not establish a hardware cost, fidelity, throughput, or energy figure.

**Exact UQPU relevance:** Lane B must not assume Gaussian-only repeaters increase pure-loss-channel quantum capacity. Lane C should retain loss, data movement, and communication capacity as explicit constraints rather than equating a large quantum state space with usable classical memory. Lanes D/G may treat non-Gaussian operations, sources, detectors, and control as possible alternative architecture elements, but any cost or manufacturability claim needs its own evidence. For INV-029, this bounds one potential networking route; it does not settle the overall Data-Center-to-One-Phone mission.

**Falsifiable follow-up:** encode the theorem's channel and operation assumptions in a small model-level acceptance contract. A claimed capacity improvement must either fail the theorem's assumptions explicitly or provide a reproducible counterexample with the exact channel, operation class, capacity definition, and independent verification. Do not infer an advantage from simulator success alone.

## 2. Self-supervised formal theorem discovery

**Official preprint:** Kazuki Ota, Takayuki Osa, and Tatsuya Harada, “Self-Supervised Theorem Discovery in a Formal Axiomatic System,” arXiv:2606.28747, submitted 2026-06-27. [arXiv record](https://arxiv.org/abs/2606.28747).

**Reported result:** the authors describe alternating proof search with extraction and reuse of useful theorems in a growing library, reporting many discovered theorems and solutions to human-written benchmark problems in their formal system.

**Genuine novelty for UQPU:** it suggests a candidate architecture for FND-006/EQN-001–006 in which accepted lemmas become reusable search assets, instead of treating every generated equation or proof as an isolated text answer. The essential boundary is the formal statement plus its axioms, imports, definitions, and kernel-check result.

**Limitations:** this is an official preprint, not an independent UQPU reproduction. The reported theorem counts are author-reported outcomes; they do not establish physical truth, empirical applicability, or a new law of nature.

**Falsifiable follow-up:** compare a fixed theorem suite with and without a reused-lemma library under identical theorem-family splits, prover/toolchain versions, wall-clock, CPU, memory, accelerator and cost budgets. Freeze statements and imports before search. Report proof completion, kernel checks, axiom/import audit, counterexamples, failed searches, proof-term size, retries, and held-out-family performance.

## 3. Physics-informed architecture with interpretable intermediate variables

**Peer-reviewed source:** Jay Mahishi et al., “PINNA: Physics-Informed Neural Networks Architecture for Implicit Governing Physics With Interpretability,” *International Journal for Numerical Methods in Engineering*, first published 2026-09-03. [Wiley DOI 10.1002/nme.70399](https://onlinelibrary.wiley.com/doi/10.1002/nme.70399).

**Reported result:** the proposed architecture uses intermediate physically meaningful predictions as supervised signals and reports results on composite-material and combustion benchmarks.

**Genuine novelty for this cycle:** intermediate variables may provide a useful audit surface for equation/constitutive-model discovery, especially where a single end-task loss hides compensating errors. This is a candidate method, not a validated UQPU component.

**Limitations:** the paper's reported benchmark performance was not reproduced here. Better prediction error does not by itself establish the correct governing law, extrapolation beyond the tested domain, physical causality, material qualification, or device/economic benefit.

**Falsifiable follow-up:** compare against declared PINN/operator-learning baselines using the same data, preprocessing, parameter/search budgets, and held-out material or geometry families. Check dimensional consistency, conservation, stability, residuals, uncertainty calibration, and out-of-domain failures. Retain false discoveries and negative controls.

## 4. Public equation-discovery benchmark candidate: SRSD-Feynman Easy

**Source:** [Hugging Face dataset card](https://huggingface.co/datasets/yoshitomo-matsubara/srsd-feynman_easy) and [pinned dataset revision](https://huggingface.co/datasets/yoshitomo-matsubara/srsd-feynman_easy/tree/78a2026e61eaa000fb7ed5e30f0639329e912f9d). The card declares CC-BY-4.0, describes 30 physics formulas, and lists 8,000 train, 1,000 validation, and 1,000 test rows per formula. The associated official code repository is [omron-sinicx/srsd-benchmark](https://github.com/omron-sinicx/srsd-benchmark), pinned at commit 7d00b45d56250717ac08a256dc9f79b836d61027 and licensed MIT. The dataset and code have separate license declarations; do not infer the data license from the code repository.

**Source-audit result:** metadata and an immutable revision are identified, but the raw files were not acquired and hashed in this cycle. Therefore this is a candidate record, not an accepted provenance manifest. The published splits hold out rows within each equation; they do not by themselves test generalization to an unseen law family. The ground-truth equation files are Python pickle files; do not unpickle them as part of a routine acquisition or CI path. Hash the bytes safely and use a reviewed text/JSON equation representation where available.

**Next gate:** acquire the pinned train/validation/test files, compute SHA-256 over exact bytes, verify the CC-BY-4.0 attribution and source revision, record schema/preprocessing/inclusion policy, and independently rebuild the split manifest. Then preregister a resource-matched comparison with at least 30 seeds. Keep per-equation recovery and cross-law generalization as distinct tasks.

## Cross-lane disposition

- **A:** formal proof reuse and equation-discovery comparisons remain software/method work; no algorithmic winner is accepted.
- **B:** the Gaussian-repeater theorem becomes a provider-neutral architecture constraint for its stated channel and operation class; no live provider was queried or used.
- **C:** capacity and data movement remain separate from readable RAM/VRAM/HBM/storage; no memory replacement is demonstrated.
- **D/G:** PINNA and non-Gaussian photonic options are research candidates; no chip, process, package, equipment, or yield result follows.
- **E:** no Pangola material qualification, accepted bio-oil, or fusion electricity result follows from these papers.
- **F:** raw source hashes, matched resource budgets, uncertainty, and full lifecycle economics remain acceptance requirements.
- **H:** the sources are recorded with dates, scope, limitations, and falsifiable follow-ups; strategic intent and multilingual master-plan references remain context, not evidence.

## INV-029–035

**INV-029:** the phone-class physical-compression mission remains unachieved.  
**INV-030:** no biomass-derived functional substitution or critical-material reduction is qualified here; no elemental transmutation is claimed.  
**INV-031:** no accepted liquid-fuel or full-boundary bio-oil cost result.  
**INV-032:** no reliable net delivered fusion-electricity or lifecycle-cost result.  
**INV-033:** no measured reduction in financed principal, absolute interest, project WACC, or economy-wide rates.  
**INV-034:** foundational theorem/bound and model-discovery methods are candidates for controlled tests.  
**INV-035:** generated mathematics remains a hypothesis until formal/empirical gates pass; current physical constraints remain binding for engineering claims.

All third-party results remain LITERATURE_ONLY. No equation or theorem is promoted to a new physical law by this watch.

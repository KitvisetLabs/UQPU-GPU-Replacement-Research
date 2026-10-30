# Literature watch — 2026-10-30 — nonequilibrium thermodynamics, formal discovery and constitutive modeling

**Date:** 2026-10-30 (Asia/Bangkok)  
**Primary owner:** INV-034/INV-035 cross-cutting literature surveillance; publication interface Lane H  
**Consumers:** A–H, with primary technical relevance to A, D, E, F and G  
**Evidence class:** PEER-REVIEWED EXPERIMENTS + PEER-REVIEWED METHODS + OFFICIAL PREPRINTS + PEER-REVIEWED REVIEW / NO PROJECT REPRODUCTION

This watch records source-level advances found in the current cycle. It does not promote any external result to UQPU evidence, a new physical law, a material substitution, a commercial fuel/electricity result or a computing advantage.

## 1. Dago & Bellon — feedback-shifted Landauer erasure cost

**Source/date:** Salambô Dago and Ludovic Bellon, “Shifting Erasure Cost below the Landauer Bound with a Demon-Biased Thermal Bath,” Physical Review Letters 137, 147101; published 2026-09-30, issue dated 2026-10-02. [APS article / DOI 10.1103/rw6w-bskc](https://doi.org/10.1103/rw6w-bskc).

**Evidence class:** Peer-reviewed experimental information-thermodynamics result; this cycle inspected the publisher abstract and bibliographic record, not the complete article or raw data.

**Genuine novelty:** A microresonator information bit is reset under a feedback-generated hysteretic bias. The authors report an adjustable nonequilibrium effective temperature different from the bath temperature and erasure costs more than 20% below the reference k_B T_0 ln 2. At zero bias, the platform recovers the standard quasistatic result; nonzero bias shifts the asymptotic cost.

**Incumbent assumption and interpretation:** The comparison k_B T_0 ln 2 assumes an equilibrium thermal reference at T_0. The experiment engineers a nonequilibrium steady state and uses feedback as an information engine. The result should therefore be described as a shifted operating bound for the bit under the engineered resource boundary, not as a universal violation of Landauer's principle. The feedback controller, hysteresis generation, information flow, hidden controller state, noise source and reset of the controller must be included in a full-cycle accounting.

**Limitations:** The publisher abstract alone does not establish the all-resource cost of a cyclic bit-plus-controller machine. No UQPU memory, reset, cryogenic, QEC or wall-plug energy advantage follows.

**Exact relevance:** FND-001 thermodynamic-gap accounting; EQN-001/002 information-versus-energy constraints; INV-034/035. It motivates a more complete accounting boundary for state reset, QEC and memory operations.

**Falsifiable follow-up:** Reproduce the zero-bias control, sweep hysteresis h, measure effective temperature and bit-erasure work, quantify feedback/control energy and information, reset the controller, and close the complete cycle. Compare bit-only cost and full-device-cycle cost. Independent replication must recover the h=0 limit and the reported bias dependence before any engineering implication is considered.

## 2. Sundelin et al. — experimental quantum thermodynamic-uncertainty-relation result

**Source/date:** Simon Sundelin et al., “A quantum thermal machine surpassing the classical thermodynamic limit on precision,” arXiv:2609.37149, submitted 2026-09-29. [Official arXiv record](https://arxiv.org/abs/2609.37149).

**Evidence class:** Experimental preprint; not treated as peer-reviewed or independently reproduced by this project.

**Genuine novelty:** A superconducting quantum thermal machine is reported to reach a steady-state thermodynamic-uncertainty ratio Q = 1.71 ± 0.17, below the canonical classical steady-state bound Q >= 2, at a reported bath temperature of 81 mK. At 31 mK the reported ratio remains above 2. The device uses a microwave waveguide as a cold bath and classical broadband noise as an effective infinite-temperature bath.

**Incumbent assumption and interpretation:** The classical TUR applies to a specified class of classical stochastic steady-state dynamics. A quantum open-system device with coherent drive and quantum transitions is not automatically within that class. This is a candidate experimentally discriminating change of model class, not a declaration that thermodynamics or conservation laws fail.

**Limitations:** The reported output statistics are inferred from heterodyne records rather than direct photon counting. The entropy-production estimate assumes waveguide emission dominates. The available paper summary notes no matched classical-device control that isolates coherence as the sole cause. The measured Q is not an efficiency, useful-work or energy-per-computation metric.

**Exact relevance:** FND-001 and FND-004; possible device-level test of nonclassical fluctuation/dissipation relations. No QPU speedup, lower wall-plug energy or commercial thermal-machine advantage is established.

**Falsifiable follow-up:** Independently reconstruct the master equation and full-counting statistics; reproduce the 81 mK and 31 mK regimes; calibrate detector efficiency and unresolved loss; close the entropy-production boundary; and add a matched classical control with the same observables and operating conditions.

## 3. Singh et al. — algebraic no-go certificates for specified linear-optical state-generation tasks

**Source/date:** Deepesh Singh, Ryan J. Marshman, Luis Villegas-Aguilar, Jens Eisert and Nora Tischler, “Rigorous no-go theorems for heralded linear-optical state generation tasks,” arXiv:2602.09495, submitted 2026-02-10; Physical Review A 113, 063735 (2026). [Official arXiv record](https://arxiv.org/abs/2602.09495) · [journal DOI](https://doi.org/10.1103/fzjk-8w3m).

**Evidence class:** Peer-reviewed mathematical/theoretical result with algebraic-geometry no-go certificates.

**Genuine novelty:** The authors map feasibility of specified heralded linear-optical state-generation patterns to polynomial-system feasibility and apply a Nullstellensatz linear-algebra method to prove infeasibility and establish resource lower bounds for selected optical states and gates.

**Limitations:** The no-go applies to the stated input states, linear-optical operations and measurement patterns. It does not rule out every photonic architecture, nonlinear interaction, encoded resource or different protocol. The exact polynomial assumptions must be reconstructed before transferring a bound.

**Exact relevance:** FND-004 alternative physical primitives; Lane D/G photonic device and manufacturing co-design; INV-034. It provides a way to stop impossible photonic sub-designs before fabrication.

**Falsifiable follow-up:** Translate one proposed UQPU photonic primitive into the exact polynomial constraints, reproduce the certificate independently, identify which assumption would have to change for a proposed alternative, and derive a distinct observable/resource prediction. Do not bypass a no-go with an unspecified “future physics” claim.

## 4. Cogentic — multi-agent formal proof discovery

**Source/date:** “Cogentic: Multi-Agent Orchestration for Automated Proof Discovery,” arXiv:2609.40324, submitted 2026-09-30. [Official arXiv record](https://arxiv.org/abs/2609.40324).

**Evidence class:** Official preprint and reported expert-verified mathematical case studies.

**Genuine novelty:** A multi-agent workflow coordinates proof discovery and verification, reporting five results across online learning, auction theory and mechanism design. Its methodological contribution is the separation of candidate generation, independent checking and a persistent verified-result record.

**Limitations:** These are not physics equations, experiments or new physical laws. Expert verification and formal proof artifacts must be inspected before any workflow is adopted as a project validation layer.

**Exact relevance:** FND-006 and EQN-001–006. It supports a disciplined generator → independent prover/checker → counterexample search → proof artifact → verified ledger architecture, while preserving false discoveries and failed conjectures.

**Falsifiable follow-up:** Reproduce one published theorem from its formal artifact, use independent provers and adversarial counterexample search, and measure false-positive/false-negative rates on a held-out theorem set. Only then consider adapting the orchestration pattern to physical-equation candidates.

## 5. Yu et al. — hierarchical symbolic AI for constitutive modeling

**Source/date:** Haozhe Yu et al., “A Hierarchical Deep Symbolic AI Method for Closed-Form, Interpretable Constitutive Modeling,” International Journal for Numerical Methods in Engineering 127(14), e70387; first published 2026-07-22. [Wiley article / DOI 10.1002/nme.70387](https://doi.org/10.1002/nme.70387).

**Evidence class:** Peer-reviewed numerical-methods research article; source-level method and abstract inspected, no project reproduction.

**Genuine novelty:** The HDSAI method evolves symbolic expressions layer by layer, propagating evaluated intermediate features to reduce uncontrolled symbolic-tree growth. It combines prediction error and structural complexity with physical admissibility screening, and reports rediscovery of known hyperelastic constitutive forms against GPTIPS, PySR and LoHM baselines.

**Limitations:** The benchmarks include known/synthetic constitutive forms; some comparisons use 25 training and 30 test points. The paper's constraints include nonnegative strain energy, zero-stress reference and a local convexity screen. The authors explicitly note that this does not guarantee global polyconvexity, rank-one convexity or strong ellipticity. A good fit or rediscovery of a known equation is not a new material law.

**Exact relevance:** INV-030; Lane D/G materials and manufacturing; EQN-003/005/006. It is a candidate search method for Pangola-carbon composites only after actual measured stress/strain/thermal/electrical data and symmetry/thermodynamic constraints exist.

**Falsifiable follow-up:** Reproduce one known hyperelastic benchmark with fixed data splits and baselines; add frame indifference, material symmetry, dimensional constraints, stability/convexity checks over the full domain, loading-path holdouts, noise tests and independent material measurements. Do not claim Pangola substitution from synthetic benchmarks.

## 6. Asamoah, Brown & Malmsheimer — pyrolysis TEA meta-analysis

**Source/date:** Samuel Sarpong Asamoah, Tristan Brown and Robert W. Malmsheimer, “A techno-economic evaluation of pyrolysis pathways for lignocellulosic biofuels: A systematic review and meta-analysis,” Journal of Analytical and Applied Pyrolysis 197, 107847 (2026), DOI 10.1016/j.jaap.2026.107847. [Bibliographic record and DOI](https://doi.org/10.1016/j.jaap.2026.107847).

**Evidence class:** Peer-reviewed systematic review/meta-analysis of 50 TEA studies published 2019–2025; not a plant measurement.

**Genuine novelty:** The review harmonizes minimum selling prices and reports lower average prices for primary pyrolysis fuels (about US$0.57/L) than upgraded pyrolysis fuels (about US$1.23/L, with a reported US$0.12–3.53/L range). Its summary identifies feedstock cost and product yield as leading cost drivers and finds weaker scale correlation after upgrading.

**Limitations:** Cross-study heterogeneity, process boundaries, feedstock, currency/year, financing, upgrading depth and coproduct accounting must be reconciled before comparing values. These are not Pangola-specific data, and crude primary pyrolysis liquid is not accepted finished fuel.

**Exact relevance:** BIO-001, INV-031 and INV-033. It reinforces the requirement to optimize final accepted liquid-energy/fuel function, including feedstock logistics, yield, upgrading/hydrogen/catalysts, utilities, CAPEX/OPEX and financing.

**Falsifiable follow-up:** Extract the 50 study-level boundary variables and normalize currency/year, moisture basis, feedstock gate price, product yield, upgrading, hydrogen, utilities, CAPEX, capacity factor, financing and coproduct credits. Then preregister a Pangola/residue case and validate with measured mass/energy balances and accepted-fuel specifications.

## 7. McArdle, Gilyén & Berta — state preparation without coherent arithmetic

**Source/date:** Sam McArdle, András Gilyén and Mario Berta, “Quantum State Preparation without Coherent Arithmetic,” Physical Review Letters 136, 240603, published 2026-06-18. [APS article / DOI 10.1103/ntvs-c48s](https://doi.org/10.1103/ntvs-c48s).

**Evidence class:** Peer-reviewed quantum-algorithm method paper.

**Genuine novelty:** A template quantum eigenvalue-transformation circuit prepares function-amplitude states from a low-cost block encoding of the sine function without handcrafted reversible arithmetic or quantum table reads. The paper reports four ancillas (three for definite-parity approximants) for Gaussian and Kaiser window examples.

**Limitations:** Ancilla count is not total resource cost. Gate count is described as similar when the function admits a compact polynomial/Fourier approximation. No universal state-preparation cost advantage, accepted workload speedup or end-to-end economics follows.

**Exact relevance:** Lane A workload/state-preparation compiler path and Lane C state/data semantics. It is a candidate algorithm to compare under identical output fidelity, gate count, depth, routing, shots, memory and host-reconstruction contracts.

**Falsifiable follow-up:** Reproduce one Gaussian/Kaiser instance with an independent SDK, derive reference amplitudes and error bounds, compare against arithmetic/table-based and classical alternatives, and count total gates, depth, ancillas, routing, shots, state I/O, host work and accepted-output cost.

## Cross-source synthesis and project gates

- **FND-001:** Nonequilibrium feedback and quantum fluctuation measurements demand explicit system/controller/bath/measurement boundaries. Keep Landauer, generalized information-cost relations and classical TUR assumptions distinct.
- **FND-002:** No new output-information lower bound was found in this watch.
- **FND-003:** No new matched control-versus-quantum-speed-limit measurement was found.
- **FND-004:** The linear-optical algebraic no-go and quantum TUR experiment are concrete candidate physical-primitive constraints/observables; each applies only under its stated model assumptions.
- **FND-005:** No new QFT/elementary-particle mechanism evidence was found.
- **FND-006 / EQN-001–006:** Formal proof orchestration and hierarchical symbolic discovery can improve candidate generation and verification, but fit, theorem proof and physical truth are separate gates.
- **BIO-001 / INV-031:** The TEA meta-analysis strengthens the need to distinguish primary pyrolysis liquid from upgraded accepted fuel; it supplies no Pangola result.
- **INV-030:** HDSAI is a method candidate, not evidence that Pangola carbon substitutes a critical material.
- **INV-032 / INV-033:** No new fusion plant, net-electricity or UQPU financing result changed Batch 140's open gaps.
- **INV-029:** None of these results closes phone-class physical compression.

**Deduplication:** SymbolFit (arXiv:2607.19750) and LLM-PySR (arXiv:2607.04156) were already indexed in the 2026-10-28 literature watches; they were not republished as new discoveries here.

**Promotion rule:** No external paper, AI-generated equation, symbolic fit, mathematical no-go, preprint experiment or TEA scenario is project evidence until source assets are pinned, methods reproduced, assumptions checked, held-out predictions passed and independent validation completed.

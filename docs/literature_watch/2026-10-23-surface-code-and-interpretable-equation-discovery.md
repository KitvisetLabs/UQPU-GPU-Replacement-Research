# Literature Watch — surface-code teleportation and interpretable equation discovery

**Search/update date:** 2026-10-23  
**Primary owner:** Lane H (literature synthesis); Lane F owns evidence integration  
**Status:** external literature delta; no UQPU evidence promotion

## Sources and evidence classes

1. **Y. Zou et al., “Teleportation transition of surface codes on a superconducting quantum processor.”** Nature Physics, version of record published 2026-10-22; preprint arXiv:2602.21293 first posted 2026-02-24.  
   Primary source: https://www.nature.com/articles/s41567-026-03484-0  
   Official preprint: https://arxiv.org/abs/2602.21293  
   Data: https://doi.org/10.5281/zenodo.21885571  
   **Evidence class:** published external experiment. The paper reports logical surface-code-state teleportation on a 125-qubit superconducting processor for code distances up to 7, maps a teleportation transition by tuning entangling gates, and reports a higher threshold with coherent rotations that inject non-Clifford magic resources.

2. **K. A. Richardson, S. Trifinopoulos and M. Williams, “Interpretable AI reveals hidden structure in nuclear masses.”** Communications AI & Computing, published 2026-10-21.  
   Primary source: https://www.nature.com/articles/s44488-026-00017-9  
   Code/data provenance: https://doi.org/10.5281/zenodo.21415298  
   **Evidence class:** published external computational/method result. Using 2,325 nuclei from AME2020, the authors report that interpretable learned representations recover liquid-drop-model structure and a localized form of Jaffe factorization, a relation previously described through Garvey–Kelson nuclear-mass relations. Local corrections to WS4 are reported at about 115 keV RMS on the evaluated measured-nuclei set.

3. **F. Güvercin and M. Özavşar, “Reducing boundary conditions for the Thomas–Fermi equation using a hybrid q-deformation and neural network method.”** Scientific Reports, published 2026-10-22.  
   Primary source: https://www.nature.com/articles/s41598-026-74682-2  
   **Evidence class:** published external numerical-method result. The method uses a q-deformation to combine boundary constraints and reports a lower median RMSE than a physics-informed neural network in 42 of 45 matched runs. The authors also report that paired tests did not establish a difference, two outliers changed the mean comparison, and the pointwise q-ANN was about 102 times slower than the vectorized PINN.


4. **E. V. C. Lopes et al., “Engineering quantum phases in two dimensions via vacancy-induced electronic reconstruction.”** Communications Materials, published 2026-10-23.  
   Primary source: https://www.nature.com/articles/s43246-026-01365-w  
   **Evidence class:** published theoretical/computational DFT result. The authors propose that vacancy-induced dangling-bond states and their coupling can drive topological transitions and stabilize quantum spin Hall, quantum anomalous Hall, or Weyl-semimetal phases. The article is a computational mechanism proposal, not an experimental demonstration.

5. **W. Liu et al., “Nontrivial boundary-mediated superconducting transport in a TRSB topological iron-based superconductor.”** Physical Review X 16, 041022 (2026), published 2026-10-22.  
   Primary source: https://doi.org/10.1103/8vgt-twh5  
   APS research synopsis: https://physics.aps.org/articles/v19/s134  
   **Evidence class:** published external experiment with an unresolved interpretation. Edge-sensitive conductance in FeTe0.55Se0.45 shows a zero-voltage plateau reproduced across ten samples and absent from related-material controls. The result is a candidate topological-superconductivity signature, not direct proof; the APS synopsis identifies chirality/direction-sensitive edge-current measurements as an important discriminating test.

## Genuine novelty and limitations

### Surface-code teleportation

The material update is the peer-reviewed publication of an experimental, finite-size surface-code teleportation transition and an experimentally explored control parameter that shifts the transition. This is useful device/QEC evidence for the broader field, not evidence that UQPU has a fault-tolerant distributed route.

Limits: code distance is at most 7 on this specific 125-qubit device; the result does not establish scalable logical error suppression, full distributed fault tolerance, a UQPU useful-work contract, provider-specific route feasibility, energy per accepted task, production yield, or cost. Source data are available, while the paper says relevant source code is available from the authors on request.

### Interpretable nuclear-mass model

The useful methodological novelty is a transparent route from learned representations to a known physical/mathematical structure, followed by a simpler local correction rule. The Jaffe factorization itself is a rediscovery of a historical relation, not a newly established fundamental law. The evaluation excludes each target nucleus when fitting its prediction, but it is still largely within the measured nuclear domain; the authors explicitly leave extrapolation into the r-process regime as an open question. The double-helix embedding geometry depends on regularization and is not a unique physical ontology.

### q-deformed physics-informed solver

The result is a numerical boundary-condition transformation with a classical limit as q approaches 1. It is not evidence that the Thomas–Fermi physical law has changed. The synthetic/reference setting, initialization sensitivity, limited parameter coverage, lack of a statistically established paired advantage, and reported runtime penalty prevent treating the RMSE comparison as a general efficiency claim.


### Vacancy-induced topological phases

The new result is a proposed defect-engineering mechanism derived from large-scale density-functional calculations and an interpretable orbital-based Hamiltonian. It is relevant to materials design, but the abstract does not report experimental realization of the predicted phases. It must not be treated as a qualified material, device, fabrication process, or new universal law. Defect chemistry, concentration disorder, finite-size effects, competing phases, and experimental observables remain discriminating gates.

### Boundary-mediated superconducting transport candidate

The measured zero-voltage conductance plateau is a credible, replicated-across-samples anomaly with useful control-material comparisons. The interpretation remains open: the experiment does not by itself prove a topological superconducting state. Direction/chirality-sensitive edge-current measurements and independent replication are necessary before promoting the topological interpretation.

## Exact UQPU relevance

- **Lane A:** no change to the current QSVT circuit or accepted-workload contract. The new QEC result motivates future workload-specific QEC cost accounting only after target, route, and useful-output semantics are fixed.
- **Lane B:** QOS-AUDIT-010B25 remains the prerequisite for any IBM target-specific route. This literature watch does not authenticate a target, establish access, or authorize submission.
- **Lane C:** logical teleportation is state-transfer evidence, not readable classical RAM/VRAM/HBM/storage equivalence. Any future comparison must include classical communication, feed-forward, recovery, and output costs.
- **Lane D/G:** the surface-code experiment supplies external device-level evidence, while the vacancy study supplies a computational material-design hypothesis and the superconducting-transport study supplies a candidate experimental signature. None establishes a UQPU device, qualified substitute material, fabrication recipe, process window, packaging yield, or manufacturing-cost result. D/G co-design remains conditional on an accepted circuit and measured target requirements.
- **Lane E:** none of these papers measures Pangola-derived material properties, accepted bio-oil cost, net fusion electricity, or cooling/infrastructure economics. The q-deformation method is only a possible modeling technique, not a fuel/material result.
- **Lane F:** the q-ANN runtime penalty is a reminder to compare accuracy and full compute cost together. None of the papers supplies a provider-matched accepted-task price, project-finance principal, interest saving, or WACC reduction.
- **Lane H:** preserve the staged investment strategy and use evidence gates to decide when QEC, AI equation discovery, or physics-informed modeling deserves additional capital.

## Falsifiable follow-up gates

1. **QEC replication:** retrieve the paper's source data from Zenodo, freeze preprocessing and the reported observables, reproduce the distance-dependent teleportation phase diagram, and report uncertainty and resource use. Reject the imported result if the preregistered observables cannot be reproduced within the source's stated uncertainty. Do not map it to a UQPU workload until accepted-output semantics and all host/classical communication costs are explicit.
2. **Nuclear-model reproduction:** reproduce the published code path and AME2020 leave-one-target-out evaluation, then preregister blocked isotopic/isotonic bands and a neutron-rich extrapolation comparison against WS4 and local Jaffe corrections. The candidate fails its transfer claim if improvements disappear under blocked splits, cluster around known shell exceptions without calibrated uncertainty, or depend on target leakage.
3. **q-deformation reproduction:** freeze q values, seeds, parameter ranges and reference solver; test q-to-1 convergence, boundary residuals, multiple ionization degrees and held-out parameter sets. Report RMSE and wall-clock/runtime together. Reject a general-efficiency claim if the error difference is not statistically resolved or the runtime penalty dominates under the same accuracy contract.


4. **Vacancy-material validation:** reproduce the DFT and orbital-Hamiltonian assumptions from the paper, preregister defect concentration/arrangement sweeps and competing phases, then identify a measured spectral or transport observable that distinguishes the proposed topological phase from trivial defect bands. Reject a device claim if the predicted signature is not robust to realistic disorder or is not experimentally observed.
5. **Superconducting-boundary anomaly:** replicate the edge/surface electrode geometry and control-material comparison, then measure direction-sensitive (chiral) edge transport with preregistered reversal and null controls. Reject the topological interpretation if chirality-sensitive evidence is absent or the plateau can be explained by non-topological contact/edge effects.

## Foundational/equation-discovery decision

These papers support the generator → explicit constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics workflow. The vacancy result remains computational, and the superconducting transport plateau remains an unresolved experimental interpretation. They do not change thermodynamic, information, causality, no-cloning, or quantum-speed-limit boundaries. No equation is promoted by this article; no new physical law is claimed. EQN-001 through EQN-006 remain governed by the existing discovery contract, and FND-001 through FND-006 retain their current evidence classes.

## Non-claims

No UQPU real-QPU run, quantum advantage, accepted useful-task cost reduction, Data-Center-to-Phone result, RAM/VRAM/storage replacement, qualified biomass/material substitution, commercial bio-oil, commercial fusion electricity, lower financing rate/WACC, confirmed topological superconductivity, or new fundamental law is established by these external sources.

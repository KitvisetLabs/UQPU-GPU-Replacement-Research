# Literature watch — 2026-10-24: AI-designed physics experiments, closed-loop validation, and model discrimination

**Accessed:** 2026-10-24 (Asia/Bangkok)  
**Primary owner:** Lane H — strategy, finance, future-industry research and publication  
**Integration owners:** Lane A (workload/objective contracts), Lane B (provider boundaries), Lane C (state/I/O accounting), Lane D/G (instrument and fabrication feasibility), Lane E (materials/energy), Lane F (experimental economics)  
**Feeds:** FND-001..006; EQN-001..006; BIO-001; FUS-001; FIN-001; INV-029, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY` for third-party sources; no project evidence promotion

## Why this watch matters

The relevant advance is not that AI can declare new laws. It is that experiment design can be framed as a constrained search over instrument configurations, simulators, objective functions and discrete/continuous choices, and some agentic systems have progressed from virtual testing to bounded operation on real scientific instruments. UQPU can borrow the workflow discipline, but must independently validate every result and count the full cost of producing an accepted observation.

## Sources and evidence classes

1. **Jonathan Klimesch et al., “Designing physics experiments with artificial intelligence,” Nature 657, 47–58, published 2026-09-02.** Peer-reviewed review. DOI: https://doi.org/10.1038/s41586-026-10898-6. It organizes AI-assisted physics experiment design around expressive search spaces, fast/reliable simulators, computable scientific objectives, and search across discrete and continuous design choices. The review explicitly identifies trade-offs among computational tractability, experimental feasibility, interpretability and reliability.
2. **“An agentic artificially intelligent X-ray scientist,” Nature Machine Intelligence 8, 1075–1086, published 2026-07-01.** Peer-reviewed research article. DOI: https://doi.org/10.1038/s42256-026-01261-5. The authors report an LLM-driven agent that trained in a virtual beamline environment and was deployed to a real synchrotron beamline for reference-reflection identification and orientation-matrix determination. This is a bounded instrument task, not autonomous discovery of a new physical law.
3. **“Agentic artificial intelligence for multistage physics experiments at a large-scale user facility particle accelerator,” Physical Review Research 8, L012017, published 2026-01-16.** Peer-reviewed primary research. DOI: https://doi.org/10.1103/jtqy-9jz1. The authors report plan-first, bounded agent execution across archive retrieval, control-channel resolution, script generation, controlled machine interaction and analysis; their representative machine-physics task reduced preparation time by two orders of magnitude. That figure is source-specific and must not be transferred to UQPU or treated as a reduction in total experiment cost.
4. **Hanqiao Yu et al., “Discovering multiscale deep formulas in complex systems via neural-guided lambda calculus,” Nature Communications 17, 7639, published 2026-06-16.** Peer-reviewed primary research. DOI: https://doi.org/10.1038/s41467-026-74299-z. Deflex combines neural-guided representations with lambda-calculus symbolic regression and reports up to seven-fold efficiency gains across six studied systems. This motivates a matched-budget candidate-generator comparison; it does not establish universal generalization or physical validity.
5. **Yu-Han Tseng et al., “Optomechanical Detection of Individual Gas Collisions,” Physical Review Letters 137, 173601, published 2026-10-19.** Peer-reviewed recent experimental result. DOI: https://doi.org/10.1103/xtzh-6t1f. The paper reports single-collision momentum-transfer measurements for several gas species and agreement with theoretical expectations. It is a useful example of an observable tied to a specified mechanism, not a credible anomaly or a revision of incumbent physics.

The Nature review and the beamline/accelerator articles are methodology evidence. Deflex is third-party benchmark evidence. The gas-collision article is an experimental measurement in its stated apparatus. None is evidence of UQPU advantage, a new UQPU physical primitive, Pangola material substitution, commercial bio-oil, low-cost fusion electricity or financing-rate reduction.

## Genuine delta for UQPU

The integration opportunity is to promote **experiment-design provenance and staged authorization** to first-class fields in the equation-discovery workflow:

- distinguish the candidate generator from the simulator, experiment planner, instrument controller, evaluator and evidence adjudicator;
- encode scientific objectives as typed observables with units, uncertainty, valid ranges, acceptance thresholds and a preregistered falsifier;
- treat simulator-to-instrument transfer as a separate validation gate, including model discrepancy and calibration drift;
- enforce instrument capability, safety and authorization constraints as hard constraints rather than soft model preferences;
- measure preparation time separately from total generator, simulator, host, data-transfer, instrument, retry, reconstruction and replication costs;
- preserve failed candidates, unexpected observations and counterexamples rather than filtering them from the report.

This is a workflow recommendation derived from the sources, not a claim that the sources share an identical architecture or that their reported performance generalizes to this repository.

## Falsifiable follow-up — EXP-DESIGN-002

**Status:** proposed offline benchmark; not executed in this watch.

1. Freeze a small suite of known governing equations, noisy observations, one held-out parameter/domain regime per model, and deliberately non-identifiable training sets. Record immutable data hashes and model assumptions.
2. Compare (a) a human-written baseline plan, (b) a simple information-gain/optimal-design baseline, and (c) an AI-proposed plan under the same simulator calls, wall-clock budget, CPU/GPU time and energy where measurable.
3. Require every proposed experiment to name the incumbent model, alternative model, observable that distinguishes them, predicted distributions under both models, uncertainty, feasibility constraints, and the observation that would falsify the alternative.
4. Evaluate held-out model discrimination, calibration, replicate stability, counterexample detection, constraint violations and accepted discriminating results per total resource budget. Include failed runs and the cost of candidate generation and evaluation.
5. Use independent simulator implementations or analytic cases where possible. A candidate that only improves its own simulator score, violates a hard constraint, fails held-out predictions or cannot be independently reproduced is rejected.
6. Keep all physical-instrument and QPU actions disabled in the offline benchmark. Any future instrument trial requires its own authorization, bounded budget and human approval. No paid QPU job is authorized by this article.

**Falsifier for the workflow hypothesis:** under matched budgets, the AI planner does not improve accepted held-out model discrimination over the simple baseline, or any apparent gain disappears after accounting for simulator calls, failures, safety constraints, reconstruction and independent replication. A null result remains publishable.

## Cross-lane integration

| Lane | Concrete interface | Evidence boundary |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Shared workload contract: target observable, success threshold, query/shot budget, held-out cases and reconstruction cost. | Offline planning only; no quantum advantage. |
| B — cloud/QPU/provider integration | Provider-neutral capability metadata and no-submit preflight; simulator/dry-run precedes any authorized execution. | No provider contact or job in this watch. |
| C — state/memory/storage/data movement | Record state preparation, measurement output, bytes transferred, decoding/reconstruction and classical memory separately. | Hilbert-space dimension is not readable classical storage. |
| D — devices/chips/process/fabrication | Include measurable device/instrument feasibility and calibrated parameter ranges in the search-space contract. | No device or fabrication claim. |
| E — materials, bio-oil, fusion, cooling/infrastructure | Future experiments must use Pangola-specific material functional units or net-delivered-electricity definitions; generic AI methods supply no such data. | BIO-001 and FUS-001 remain without new measurement. |
| F — economics/benchmarks/evidence | Cost per accepted discriminating result includes generation, simulation, instrumentation, energy, transfer, retries and replication. | No commercial cost, interest or WACC result. |
| G — manufacturing equipment/factory systems | D/G co-design can use constrained experiment planning for process windows only after instrument/process measurements exist. | No factory-yield or manufacturing-cost result. |
| H — strategy/finance/future industries | Own this literature record and keep time-to-evidence distinct from an asserted lower financing rate. | Literature-only. |
| I — repository extension | Reviewed as an adjacent research lane; no validated lift/propulsion consequence follows from this literature. | No vehicle or field-control claim. |

Relevant meaningful edges are A↔F (objective and total-cost accounting), A↔B (provider-neutral no-submit execution gates), C↔F (output and reconstruction costs), D↔G (instrument/process co-design), D↔E (material/energy observables), and H↔all lanes (strategic evidence governance). Other pairings are not forced merely to create a link.

## Foundational and equation-discovery implications

- **FND-001:** the planner must record energy and duration for the same physical evolution; ideal bounds remain ideal bounds until matched measurements exist.
- **FND-002:** accepted output semantics, precision and reconstruction determine information requirements; a large mathematical state space is not readable memory.
- **FND-003:** design a matched control/candidate comparison with the same transition, boundary, duration and success predicate before discussing speed limits.
- **FND-004:** any proposed alternative primitive must specify which incumbent assumption changes and the observable that distinguishes it.
- **FND-005:** the recent gas-collision measurement illustrates mechanism-linked observables, but agrees with expected theory and supplies no project anomaly.
- **FND-006 / EQN-001–006:** generators may propose equations and experiments; explicit constraints, held-out prediction, counterexample search, proof/simulation, discriminating experiment and independent replication remain separate gates.

## INV-029–035 and economic boundaries

- **INV-029:** a shorter planning workflow is not physical data-center-to-phone compression. The final phone must satisfy useful-service, energy, thermal, I/O, form-factor and lifecycle-cost contracts within its declared physical boundary.
- **INV-030:** no elemental transmutation or universal carbon substitution is implied.
- **INV-031:** no accepted Pangola-derived liquid-fuel mass/energy/cost result is implied.
- **INV-032:** no net reliable delivered fusion-electricity result is implied.
- **INV-033:** shorter evidence cycles could reduce capital lock-up only if measured; lower principal reduces absolute interest at unchanged terms, while lower WACC/risk premium requires separate evidence.
- **INV-034:** preserve the path from mathematics and foundational physics to falsifiable experiments and engineering.
- **INV-035:** imagination is maximized at hypothesis generation; physical claims remain governed by present evidence until a discriminating, independently validated result justifies revision.

## Surveillance conclusion and next gate

The targeted scan found useful methods and a recent precision-measurement example, but **no verified new physical law, no credible project-relevant anomaly, and no new general no-go theorem** that changes UQPU's incumbent engineering assumptions. The next highest-value research gate is to implement EXP-DESIGN-002 as an offline, matched-budget benchmark and compare its result against the existing equation-discovery and falsification contracts. No change is made to the IBM `ibm_kingston` read-only snapshot preregistration or the no-paid-QPU boundary.

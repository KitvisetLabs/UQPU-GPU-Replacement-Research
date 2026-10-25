# Literature watch — 2026-10-25: uncertainty-calibrated experiment selection and constraint-aware equation discovery

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — strategy, foundational research publication and future-industry integration  
**Integration owner:** Lane F — evidence, benchmark and lifecycle-cost accounting  
**Feeds:** A–H; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001; INV-029–035  
**Evidence class:** LITERATURE_ONLY  
**Project evidence promotion:** none

## Executive delta

A repository-scoped search found no existing mention of the GOLLuM study or the ASP-assisted symbolic-regression paper. These are not newly published today; they are newly incorporated literature leads in this cycle. Together they support a practical methodological refinement: candidate generation should be separated from uncertainty-calibrated experiment selection, and symbolic candidates should be filtered through explicit domain constraints before expensive experiments. Neither paper establishes a new physical law or any UQPU, Pangola, fusion, or financing advantage.

## Source 1 — uncertainty-calibrated LLM-assisted experimental optimization

Bojana Ranković, Ryan-Rhys Griffiths and Philippe Schwaller, “Large language models as uncertainty-calibrated optimizers for experimental discovery,” *Nature Machine Intelligence* 8, 1466–1477 (published 2026-08-28). Official article: https://www.nature.com/articles/s42256-026-01283-z. The study presents GOLLuM, which jointly trains a language-model representation with a Gaussian-process objective rather than trusting prompt-only candidate rankings. The article reports 23 optimization tasks, cold starts from ten low-performing observations, and a mean 36.3% top-5% coverage at a 50-experiment budget for its leading variant. In five Buchwald–Hartwig reaction benchmarks, its reported high-yield discovery rate rises from 24% for a static representation to 43% after optimization-aware adaptation. The paper also reports that prompt-only LLM proposals often fail through invalid, duplicate, or unparseable suggestions.

**Evidence class:** peer-reviewed method with benchmark and experimental-chemistry results reported by the authors; not a UQPU replication.

**Limitations:** the 23 tasks are chemistry/materials/process/molecular-design benchmarks, not UQPU workloads, Pangola conversion, fusion plant operation, or semiconductor fabrication. Performance depends on the design-space representation and benchmark protocol. The paper notes cubic scaling for standard Gaussian processes and weaker applicability where data are high-dimensional and lack a useful linguistic structure. Static LLM embeddings can underperform specialized descriptors; direct prompting is not a substitute for calibrated uncertainty or domain constraints.

## Source 2 — Answer Set Programming constraints for symbolic regression

Theofanis Aravanis et al., “ASP-assisted symbolic regression for interpretable modelling of 3D laminar channel flow,” *Scientific Reports* 16, article 20105 (published 2026-04-30). Official article: https://www.nature.com/articles/s41598-026-49762-y. The work fits compact symbolic expressions to numerical data for a 3D laminar-channel flow case and describes a hybrid symbolic-regression / Answer Set Programming workflow to reject candidates that violate encoded domain constraints. It reproduces expected parabolic velocity and linear pressure-drop behavior on that case.

**Evidence class:** peer-reviewed method demonstration on a bounded flow problem whose reference behavior is already known; not evidence of a newly discovered law.

**Limitations:** the reported flow case is narrow and simulation-based. An equation that fits one generated dataset and satisfies encoded constraints may still be non-identifiable, overfit, or wrong outside the tested domain. The constraint set itself may be incomplete or incorrect.

## Genuine novelty for UQPU

The useful new project-level synthesis is an operational ordering, not a new algorithmic advantage claim:

1. Generate multiple candidates without assigning them truth.
2. Apply typed dimensional, symmetry, conservation, causality, domain and safety constraints.
3. Rank the remaining experiments with calibrated uncertainty and an explicit cost-to-information budget.
4. Freeze train/held-out splits and candidate hashes before evaluation.
5. Search for counterexamples and duplicate/invalid proposals.
6. Require proof or simulation where appropriate, then a discriminating experiment and independent replication.
7. Carry only accepted outcomes into device/system models and total lifecycle economics.

A proof checker can certify a formal statement only within its formalized assumptions; an uncertainty model ranks experiments but does not validate physical truth. These tools are complementary, not interchangeable.

## Exact project relevance

- **Lane A / INV-025–027:** use uncertainty-aware selection for bounded workload and compiler experiments only after semantic equivalence, competitive classical baselines, and the accepted-output contract are fixed.
- **Lane C / INV-029:** use information-gain-per-cost to prioritize memory/state and data-movement measurements. Do not equate Hilbert-space dimension with readable classical memory.
- **Lanes D/G / INV-030:** a constrained candidate ranking may help prioritize carbon composite, surface, process-window and fabrication experiments, but accepted functional substitution still requires measured conductivity, strength, lifetime, purity, yield and incumbent-function parity. No elemental transmutation.
- **Lane E / BIO-001 / INV-031:** once quality-controlled Pangola feedstock and product assays exist, rank experiments on saleable-liquid yield, upgrading severity, hydrogen/catalyst demand, utilities, contaminants and mass/energy closure. Raw oil yield alone is not the objective.
- **Lane E / FUS-001 / INV-032:** use uncertainty-aware experiment design for material-damage, heat-exhaustion, maintenance and net-electricity parameters only where validated measurements or credible datasets exist. Ignition or gross gain is not net delivered electricity.
- **Lane F / FIN-001 / INV-033:** price each proposed experiment by setup, instrument time, consumables, labor, failure probability, delay and capital lock-up. Reduced financed principal can lower absolute interest at unchanged terms; a lower WACC/risk premium needs separate evidence.
- **INV-034/035:** this is a way to make equation generation and falsification more efficient, not permission to replace present physics with an AI-generated equation.

## Proposed falsifiable follow-up — EQN-EXP-001

Build a local, deterministic synthetic benchmark before using physical data. Freeze a set of known equations with units, symmetries, limiting cases, train/held-out domains, distractor variables and planted counterexamples. Compare, under the same candidate-evaluation budget and seeds: random search; prompt-only LLM ranking if a local model is available; a calibrated Gaussian-process baseline; and symbolic regression filtered by an explicit constraint set. Do not label the GOLLuM method reproduced unless its actual implementation and training protocol are implemented and independently verified.

Record held-out error, false-discovery rate, dimensional/constraint violations, duplicate or invalid candidates, calibration error, number of expensive evaluations, wall-clock/compute cost, and sensitivity to omitted variables. The null is that uncertainty calibration and constraint filtering do not improve accepted-candidate yield under equal budget. A pass requires a preregistered improvement on held-out tasks without increasing false discoveries or constraint violations; an apparent gain that vanishes under held-out-domain or counterexample tests is a failed hypothesis and must be recorded.

Only after synthetic gates pass should a separately authorized, low-risk experimental design be considered. No wet-lab, fabrication, fusion, or paid QPU experiment is authorized by this proposal.

## A–H status and evidence boundary

- **A — Quantum programming/compiler/runtime:** QSP/QSVT feasibility metadata contract is being added as a preregistration gate; no M-QSP theorem implementation or target execution yet.
- **B — Cloud/QPU integration:** provider-neutral route remains; no provider job submitted and no cross-provider price/probability mixing.
- **C — Memory/state/data movement:** readable-output and I/O accounting remains required; no classical-memory replacement evidence.
- **D — Device/chip/process/packaging:** candidate-selection method may prioritize tests; no material or device claim promoted.
- **E — Biomass/materials/bio-oil/fusion/cooling:** BIO-001 and FUS-001 remain evidence gaps; literature gives methods, not project measurements.
- **F — Economics/benchmarks/finance/integration:** proposed equal-budget and cost-to-information ledger; no commercial TEA, interest or WACC result promoted.
- **G — Manufacturing equipment/factory systems:** process-window and yield measurements remain future gates; co-design with D is retained.
- **H — Strategy/publication:** literature and falsifiable follow-up published here; the multilingual strategic master plan remains canonical context.

## Next highest-value gate

Implement EQN-EXP-001 as a deterministic synthetic test harness with blinded held-out equations and explicit false-discovery accounting. In parallel, continue QOS-QSVT-FEAS-001 from a metadata/preregistration contract to a pinned implementation of the published multivariate decision algorithm and independent feasible/infeasible fixtures. Do not skip the existing Batch-056 univariate regression control. No physical-law, real-QPU, material, fuel, net-electricity, or economic advantage is claimed.

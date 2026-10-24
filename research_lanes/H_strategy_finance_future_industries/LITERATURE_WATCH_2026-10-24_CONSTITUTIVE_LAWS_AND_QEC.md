# Literature watch — 2026-10-24: constitutive-law discovery and continuous-QEC scope

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance and future-industry research  
**Cross-lane integration:** A/B (runtime and provider capability contracts), C (state/readout), D/G (device and manufacturing co-design), E (materials/energy), F (evidence and economics)  
**Feeds:** FND-004–006; EQN-001–006; INV-029, INV-030, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY` — peer-reviewed methods and model-scoped limitations  
**Project evidence promotion:** none

## Source 1 — graph-based constitutive-law discovery in solids

Hao Xu et al., “Beyond empirical models: Discovering constitutive laws in solids with graph-based equation discovery,” *Science Advances*, published 2026-09-11, DOI: https://doi.org/10.1126/sciadv.aec0989. The research team's public institutional report is available at https://www.eitech.edu.cn/en/2026/0917/c577a9997/page.htm.

The reported GraphED method represents equations as operator/variable graphs and jointly searches formula structure and material-specific parameters across multiple datasets. The authors report tests on alloy steel, lithium metal and filled rubber, with improved prediction over selected conventional empirical models in those studied datasets.

**Genuine UQPU relevance:** graph representations may be another candidate generator for EQN-002/003 when equations contain shared structure plus material-specific parameters. The relevant method is candidate generation and held-out testing, not the proposition that the discovered relations are universal laws.

**Limitations:** the results are tied to the reported materials, experiments, data splits and baselines. This watch has not independently reproduced the paper's numbers or audited all dataset leakage/identifiability risks. Steel, lithium and rubber are not Pangola-derived carbon; these results establish no biomass-carbon substitution, elemental transmutation, semiconductor performance, or commercial economics.

**Falsifiable follow-up:** reproduce one published benchmark from its original data and code where available; freeze splits; compare against the stated empirical baseline and a simpler symbolic-regression baseline; audit units, parameter identifiability, held-out material/temperature/strain-rate regimes, residual structure and counterexamples. Only after reproducing the source result should the method be considered for a separately designed Pangola-carbon characterization dataset.

## Source 2 — physics-informed symbolic regression for particle/interface dynamics

Teddy Lazebnik, Chen Mortenfeld and Alex Liberzon, “Physics-informed symbolic regression reveals a delayed oscillatory closure for particle–interface dynamics,” *Machine Learning: Science and Technology* 7, 055004 (2026), published September 2026, DOI: https://doi.org/10.1088/2632-2153/ae9c8b. Bibliographic record: https://cris.haifa.ac.il/en/publications/physics-informed-symbolic-regression-reveals-a-delayed-oscillator/.

The authors apply physics-informed symbolic regression to high-resolution trajectories of spheres crossing water–salt and water–glycerol stratified interfaces. They report a compact delayed, exponentially damped oscillatory force closure that captures transient features and improves reconstruction over a virtual-mass-based baseline in transient-rich cases.

**Genuine UQPU relevance:** this is a concrete example of combining experimental time series, physical constraints and symbolic model selection to propose an effective closure. It motivates explicit tests of units, limits, held-out domains and residual structure for EQN-003/004.

**Limitations:** the closure is specific to the studied particle/interface regimes and remains an effective model for those observations. It is not a universal force law, a new fundamental interaction, a UQPU primitive or evidence of a project-relevant anomaly.

**Falsifiable follow-up:** freeze the original training/held-out split and baseline; test unseen particle sizes, density contrasts and fluid pairs; check the no-interface and long-time limits and dimensional consistency; compare independent trajectory data and report cases where the closure fails. If the claimed gain disappears on held-out regimes or independent data, reject generalization and preserve the negative result.

## Source 3 — continuous quantum error correction has an assumption-scoped failure mode

Anton Halaski and Christiane P. Koch, “Obstacles to continuous quantum error correction via parity measurements,” *Physical Review Applied* 26, 034074, published **2026-09-30**, DOI: https://doi.org/10.1103/8bkm-b48b. Official publisher record: https://journals.aps.org/prapplied/abstract/10.1103/8bkm-b48b. Public preprint: https://arxiv.org/abs/2603.02106.

The authors analyze common continuous parity-measurement protocols in circuit QED. Under the studied continuous-operation model, approximating a three-body interaction with a sum of two-body meter couplings causes measurement backaction that corrupts logical information. They discuss native three-body interactions and erasure-based encodings as possible alternatives.

**Genuine UQPU relevance:** a provider-neutral capability record must not collapse ordinary mid-circuit measurement/reset/conditional-gate support into a claim of continuous syndrome-measurement or fault-tolerant capability. If a future workload requires continuous QEC, the relevant interaction and measurement architecture must be explicitly modeled and validated. This is a D/G co-design input, not a conclusion that one device family is generally impossible.

**Limitations:** this is a model- and protocol-scoped result, not a no-go theorem for all quantum error correction, all encodings or all hardware. The paper itself distinguishes autonomous correction via engineered dissipation from the failure mechanism studied. No UQPU target was tested.

**Falsifiable follow-up:** encode the paper's exact assumptions and observable; reproduce its logical-subspace/backaction result numerically; add a native-three-body or erasure-encoding control as specified by the model; then compare against independent implementations. A changed assumption must yield a distinct predicted observable. No provider contact or hardware run is part of this follow-up.

## Cross-lane integration

- **A:** add explicit workload capability requirements for mid-circuit operations versus continuous syndrome measurement; no capability is inferred from an API label alone.
- **B:** preserve provider-neutral, read-only preflight and no-submit policy. These papers do not authorize QPU execution.
- **C:** account for syndrome/readout volume, decoding, classical state and reconstruction separately; no Hilbert-space-to-memory equivalence follows.
- **D/G:** map any candidate native interaction or device requirement to measurable process, control, yield and packaging contracts only after independent model reproduction.
- **E:** GraphED/PISR are candidate methods for material/energy constitutive models; Pangola feedstock, functional substitution, accepted liquid fuel and net delivered fusion electricity still require their own measured functional units.
- **F:** include model search, parameter fitting, failed candidates, independent data, validation and total accepted-result cost. No cost-per-task or financing result is measured.
- **H:** retain source provenance, assumptions, counterexamples and public follow-up protocols.

## Relation to lower-bound surveillance

The official preprint “Fault-tolerant quantum computation cannot be achieved with constant spacetime overhead” (arXiv:2608.26272, submitted 2026-08-26) was also encountered in this scan. Its logarithmic spacetime-overhead result is assumption-scoped; it is not a universal no-go for useful quantum computation. The repository's separate open PR #50 already records this source, so this article does not duplicate that artifact or treat it as merged to `main`.

## INV-029 through INV-035

- **INV-029:** neither a material constitutive equation nor a QEC limitation demonstrates physical data-center-to-phone compression.
- **INV-030:** no Pangola-derived material has been qualified by these papers; no transmutation claim.
- **INV-031:** no accepted liquid-fuel mass/energy/cost result.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no financed-principal, interest or WACC result.
- **INV-034:** advances model-scoped methods and explicit falsification routes without changing established physics.
- **INV-035:** AI may generate candidate equations; constraints, held-out predictions, counterexamples, independent reproduction and physical evidence remain decisive.

**Surveillance conclusion:** these sources provide useful methods and one specific quantum-control limitation, but no verified new fundamental physical law or credible UQPU-relevant anomaly. No material/fuel/fusion/economic claim is promoted.

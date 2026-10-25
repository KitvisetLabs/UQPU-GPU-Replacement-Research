# Eight-Lane Research Batch 064 — M-QSP order-invariance and WEST wall-protection reliability

**Cycle date:** 2026-10-25  
**Canonical starting main:** 70796ef8b918fe2e95382bc49cd7016a825db7e1  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-cutting owners:** Lane E — materials/energy/infrastructure; Lane F — economics/evidence/integration; FND-001 and EQN-001–006  
**Publication owner:** Lane H — strategy/publication  
**Evidence class:** SOFTWARE REGRESSION TEST + LITERATURE-ONLY FUSION RELIABILITY WATCH  
**Promotion:** no theorem proof, real-QPU result, new physical law, material substitution, accepted fuel, net-electricity, cost or economic advantage promoted

## Starting-state and invariant audit

The cycle started from current canonical main SHA `70796ef8b918fe2e95382bc49cd7016a825db7e1`, not an assumed batch number. The required charter, invariants, goals, README, Research Operating System, Open Frontier directive, Kanusanan Pongpanna model, strategic references, root directives 00/00A/01–06, newest Batch 063, RG-038/RG-039, current integration records and CI evidence were inspected. The six public strategic-plan language editions (Thai, English, Chinese, Japanese, Korean and German) and recorded AI-agent/funding context remain preserved. INV-025/026/027 and INV-029–035 remain active; INV-036/037 were not modified. The repository also has an auxiliary Lane I, but this cycle explicitly reviews all required lanes A–H.

Large append-only `WORKLOG.md`, `RESEARCH_GAPS.md` and historical scoreboards were not rewritten from partial excerpts. Sync debt is recorded here pending a safe, reviewed append-only reconciliation.

## Lane A — M-QSP negative-fixture order-invariance test

Added a regression test that permutes the insertion order of the published two-variable nonconstructible M-QSP Laurent-polynomial pair in four deterministic ways and repeats the numerical decision at tolerances `1e-12`, `1e-9` and `1e-6`. The test requires rejection and an empty constructive witness for every permutation. This complements the existing feasible/infeasible fixtures and tolerance sweep without changing the published coefficients or the decision algorithm.

**Interpretation:** mapping insertion order is semantically irrelevant to the polynomial pair, so a classification change would expose a numerical/order-dependence bug. The test is pending exact-head CI. Even if it passes, it is a software robustness check—not an independent M-QSP implementation, exact/algebraic proof, full theorem verification or application-level QSVT feasibility result.

**Next Lane A gate:** independently implement the published M-QSP-CDA algorithm, compare witnesses/classifications against the frozen feasible and infeasible corpus, and use exact/algebraic checks where feasible. Keep Batch 056 as the univariate regression control. Do not lower to paid hardware without the existing explicit-consent, bounded-budget and target-accounting gates.

## Literature delta — Lane E / FUS-001

Added [the WEST wall-protection reliability watch](literature_watch/2026-10-25-west-wall-protection-long-pulse-reliability.md) for the 2026-10-08 arXiv preprint `2610.11871`. The report describes multi-diagnostic wall protection and ML-assisted indicators during long-pulse WEST operation, while explicitly not demonstrating that the active protection caused the 1,337-second record. It does not supply a validated false-negative rate, component lifetime extension, net-electricity ledger or commercial cost.

The fresh literature sweep also checked symbolic regression, AI theorem discovery, physics-informed constitutive modeling, fusion long-pulse operation and foundational no-go claims. Closely related agentic-proof, equation-discovery and fusion-experience-rate items are already represented in open PRs (including #71, #87 and #88); they are not claimed as merged main-branch evidence. No search result was promoted to project evidence.

## Explicit A–H status

| Lane | This cycle | Evidence boundary / next gate |
|---|---|---|
| **A — Quantum programming/workloads/compiler/runtime** | Added order-permutation regression for the published M-QSP negative fixture. | Exact-head CI pending; independent M-QSP implementation and exact/algebraic cross-check remain open. |
| **B — Cloud/QPU/provider integration** | Provider-neutral and no-submit path retained. | No credentials used, no provider call, no job/shots/billing; real-QPU execution remains unauthorized. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Reviewed state/output-information constraints and the FND-001 calibration boundary. | No readable-classical-memory equivalence or measured state/I/O/transfer result. |
| **D — Device/chip/process/fabrication/packaging** | Reviewed the WEST wall-protection implications for sensors and plasma-facing components. | No UQPU device, material-property or fabrication result; device-level consequence remains conditional. |
| **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure** | Added source-bounded WEST wall-protection reliability watch. | No Pangola material substitution, accepted bio-oil, reliable net delivered fusion electricity or lifecycle-cost closure. |
| **F — Economics/benchmarks/evidence/integration** | Linked potential reliability inputs to FUS-001/FIN-001 without assigning unmeasured savings. | No accepted-task cost, plant TEA, principal/interest saving or WACC change. |
| **G — Quantum-chip manufacturing equipment/software/factory systems** | Preserved D/G co-design; process-control/metrology relevance noted. | No equipment capability, process window, yield or factory-cost evidence. |
| **H — Kanusanan Pongpanna Model strategy/finance/future industries/publication** | Published Batch 064 and the dated literature watch. | Multilingual strategic links and AI-agent/funding references preserved; no financing outcome claimed. |

## Foundational and equation-discovery status

- **FND-001:** the latest repeated-seed adjacent-lag CMI calibration remains `MODEL_ONLY / SYNTHETIC_KNOWN_TRUTH`. Positive finite-sample null CMI is a warning against treating the statistic as entropy production or thermodynamic heat. No wall-clock, wall-power or plasma diagnostic signal is substituted for thermodynamic measurement.
- **FND-002:** output-information lower bounds remain contract-level; no readable-output advantage measured.
- **FND-003:** matched control-versus-quantum-speed-limit measurement remains unperformed.
- **FND-004:** alternative physical primitives remain hypotheses without controllable/readable device evidence.
- **FND-005:** QFT/elementary-particle mechanism scans remain literature/theory only.
- **FND-006:** mathematics-first invention is strengthened by counterexample handling and order-invariance testing; no new theorem is claimed.
- **EQN-001–006:** dimensional/symmetry/conservation/causality, limiting-case, held-out, counterexample and independent-validation gates remain binding. AI-generated or fitted equations are not physical laws by declaration.

## INV-029 through INV-035 evaluation

- **INV-029:** no service/capability, physical-support, energy or lifecycle-cost contract closes Data-Center-to-One-Phone.
- **INV-030:** no Pangola/biomass-carbon functional substitution, critical-material reduction or recovery result.
- **INV-031:** no accepted liquid-energy/fuel yield, upgrading or cost-per-delivered-energy result.
- **INV-032:** WEST wall-protection evidence is an external reliability lead only; no net delivered electricity or full lifecycle cost is established.
- **INV-033:** no principal, capital lock-up, interest or WACC change measured. Lower financed principal can reduce absolute interest at unchanged terms; rate/WACC effects remain separate.
- **INV-034:** the mathematical counterexample pipeline receives a stronger numerical-order robustness check; no new physical result.
- **INV-035:** the cycle continues to separate hypothesis, numerical classification, proof, independent physical validation and technology promotion.

## CI, commit and synchronization status

The test update is on a dedicated research branch; exact-head Actions must decide acceptance. The GitHub combined-status connector returned no status contexts for starting main SHA `70796ef8b918fe2e95382bc49cd7016a825db7e1`, and the available commit-workflow lookup returned no runs. The latest recorded validation in the canonical integration record is for the earlier code/test commit `25b5a6b03fe527760d84cbdc51388b4d34ff18ba` (Python 3.10/3.11/3.12, cold-start and QSP/QSVT reference-target checks passed; extended status was recorded as in progress at 06:19 UTC). It is not valid to infer that the later FND-001 follow-up commit or this branch passed.

This branch is **pending review and not on main** until merged. Large append-only WORKLOG/RESEARCH_GAPS/scoreboard synchronization is explicitly deferred rather than overwritten.

## Next highest-value gate

1. Get exact-head CI for the order-invariance regression; repair any order-dependent classification before claiming numerical robustness.
2. Independently reproduce M-QSP-CDA and compare against the frozen fixtures; retain failed hypotheses/counterexamples.
3. Expand RG-039 with known-truth K=1/2/3 data, correlated/noisy families, blocked holdouts, unit transformations and false multi-law rates.
4. For FUS-001, obtain WEST source data and pre-register held-out wall-event detection/calibration metrics before feeding reliability assumptions into a net-electricity/lifecycle-cost ledger.
5. Continue BIO-001 and FIN-001 only with measured mass/energy and traceable financing inputs.

No paid QPU jobs, wet-lab work, fabrication, fusion experiments or external financial actions were performed.

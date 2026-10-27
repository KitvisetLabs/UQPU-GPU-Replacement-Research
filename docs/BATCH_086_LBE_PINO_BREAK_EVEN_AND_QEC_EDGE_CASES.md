# Batch 086 — physics-informed LBE surrogate break-even and QEC interval edge cases

**Date:** 2026-10-28  
**Canonical starting head:** `4374cdcea951178b048cebdfb87234d933c7eacd`  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** Lane C, D, E, F, G and H  
**Evidence classes:** `SOFTWARE_CONTRACT_ONLY` + `LITERATURE_ONLY`  
**Paid QPU job:** no

## Starting-state and CI

The cycle started from the dynamically resolved main head, not a remembered batch number. Required charter/invariant/goal/README/operating-system/open-frontier/strategic documents and the permanent root directives were checked. The newest existing batch was Batch 085. The current gap set includes RG-048 proof-structure metrics, the QEC ML certificate gap, sparse-QROM memory cost, FND-003 matched comparison, BIO-001 accepted-liquid cost and FUS-001 economic-gain/learning-rate sensitivity.

At starting head `4374cdcea951178b048cebdfb87234d933c7eacd`, the [prototype/invariant workflow](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40568854150) and [cold-start audit](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40568854240) passed. Exact-head CI for this batch commit remains required.

## Lane A — stronger conservative decoder-contract tests

Four tests now exercise touching interval boundaries, malformed/non-finite interval bounds, non-finite/negative/boolean exact minima, and non-finite candidate costs. Strict interval separation remains necessary for SUCCESS/FAILURE; touching or overlapping intervals remain UNDECIDED. The implementation is unchanged and remains a generic finite-candidate oracle/contract—not a QLDPC decoder or a source-paper reproduction.

## Fresh literature delta — physics-informed neural operator for lattice-Boltzmann dynamics

Xue et al., “Fast-forward prediction of lattice Boltzmann dynamics with physics-informed neural operators,” *Nature Communications* 17, 9243 (published 2026-07-29; version of record 2026-08-31), DOI https://doi.org/10.1038/s41467-026-75730-1, was not previously indexed in this repository. The peer-reviewed study learns large-time-jump evolution of distribution fields using moment-matching and lattice-equivariance constraints. Its authors report case-specific simulation speedups, but also state that models are trained per case over relatively narrow geometry/parameter ranges. UQPU has not reproduced the dataset, code, predictions, memory, stability or cost break-even.

The new watch and gap define a pinned, falsifiable follow-up. No paper-reported speedup is treated as UQPU evidence or transferred directly to Pangola processing, fusion, cooling hardware or quantum workloads.

## A–H work ledger

- **A — Workloads/software/compiler/runtime:** added fail-closed QEC interval edge tests; exact useful-output and source-reproduction requirements remain.
- **B — Cloud/QPU/provider integration:** no provider-specific claim, credentials, paid job or real-QPU execution.
- **C — Memory/state/data movement:** require peak memory, distribution-field bytes, transfers and output reconstruction in any future LBE surrogate comparison; quantum state-space dimension is not classical storage.
- **D — Devices/process/packaging:** no device or fabrication evidence; only a possible future thermal-fluid simulation method.
- **E — Materials/biomass/bio-oil/fusion/cooling:** source watch plus open domain-transfer gap; no Pangola or fuel evidence.
- **F — Economics/evidence/integration:** break-even must include data generation, training, validation, inference, energy and maintenance; no commercial economics.
- **G — Manufacturing equipment/software/factory:** continuous D/G co-design retained; no process-yield or cost-per-good-device evidence.
- **H — Strategy/publication:** README and dated artifacts updated; multilingual master-plan and strategic AI-agent/funding references preserved.

## Foundational and equation-discovery state

FND-001 remains MODEL_ONLY; FND-002 still requires sparse-QROM/output-information mapping to an actual workload; FND-003's OTOC speed-limit source remains assumption-scoped and unreproduced; FND-004 has no demonstrated alternative primitive; FND-005 has no validated QFT/particle mechanism; FND-006 continues with explicit constraints, held-out tests, counterexamples and independent validation. EQN-001–006 remain evidence-gated; no candidate equation is promoted to a physical law.

## INV-029 through INV-035 and moonshots

- **INV-029:** no phone-class physical compression, service/energy boundary or lifecycle-cost closure.
- **INV-030:** no biomass-carbon functional substitution/recovery result and no transmutation claim.
- **INV-031:** BIO-001 accepted-liquid mass/energy/full-cost evidence remains open.
- **INV-032:** FUS-001 remains a cost-driver model/gap; no net delivered electricity or commercial plant result.
- **INV-033:** absolute interest can fall with lower financed principal at unchanged terms; no lower WACC/risk-premium or economy-wide rate claim.
- **INV-034:** the new paper informs a testable modeling method, not a foundational-law change.
- **INV-035:** equations remain hypotheses until incumbent assumptions, dimensional/symmetry/conservation/causality checks, limits, falsifiers, held-out predictions and independent validation pass.

INV-025/026/027 remain falsifiable goals; no 100M-GPU or universal 100M-unit subsystem equivalence or cost target is achieved. The US$10T–US$100T number remains an ambition-scale proxy.

## Evidence, synchronization and next gate

The new watch, gap, Batch 086, integration report, four tests and README summary are prepared as one atomic commit. The prior `RESEARCH_GAPS.md` is retained exactly and a pointer to the new open gap is appended. The next highest-value Lane A gate is a tiny pinned syndrome/logical-class instance for the QEC certificate, with an independently enumerable reference. The Lane E gate is to pin the LBE-PINO data/code and reproduce one trajectory with invariant checks before any transfer claim.

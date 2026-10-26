# Eight-Lane UQPU Research Cycle — Bell Quantum Signal Learning

**Cycle date:** 2026-10-26  
**Canonical starting main SHA:** 412403efebabd7186dcbfca286d8481308dab176  
**Proposed branch:** research/2026-10-26-bell-quantum-signal-learning  
**Status:** review-branch artifacts; not canonical until merged  
**Primary owner:** Lane A; integration owner Lane F; publication owner Lane H

## Canonical-state audit

Read the project charter, version invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, latest merged Batches 061–063, recent gap/integration material and available CI status. All required root directives were found. The multilingual Thai/English/Chinese/Japanese/Korean/German public master-plan links and strategic AI-agent/funding references remain in STRATEGIC_PLAN_REFERENCES.md. INV-025/026/027 and INV-029–035 remain preserved.

The canonical branch already has substantial recent parallel work. The README records Batches 060–063; newer work appears in multiple open PRs, including competing Batch 064 proposals. Batch numbers are not safe unique identifiers. This cycle uses a unique work-item ID and dated artifact paths rather than creating another numbered batch or rewriting the append-only canonical WORKLOG.md/RESEARCH_GAPS.md.

The canonical commit-status endpoint returned no status entries. The current canonical starting commit's historical workflow evidence and any review-branch run must not be conflated with exact-head validation. All proposed artifacts remain non-canonical until review and merge.

## Literature surveillance

Primary new-to-canonical coverage candidate: Cotler, Danielson and Kannan, “Quantum Advantage for Sensing Properties of Classical Fields,” Physical Review X 16, 041025, published 2026-10-23, DOI 10.1103/6ps1-mw9l. The source reports Bell quantum signal learning, a bosonic protocol using two-mode squeezing, passive optics and static homodyne measurements; it proves query-complexity separations for specified sensing models and reports practical comparisons against homodyne/heterodyne baselines.

### Material source caveat recorded

The official arXiv preprint (arXiv:2602.17591), Appendix E.4, distinguishes a separate squeezing-only construction from the entanglement-enabled Bell-QSL result. For that squeezing-only construction, (r=\frac12\log n) implies mean photon number (̄n=\sinh^2(r)=\Theta(n)); its exponential sample-complexity separation therefore uses instance-scaled probe energy and is not a fixed-energy claim. The literature watch, Lane A benchmark contract, gap RG-BELL-QSL-001 and integration JSON now record this distinction. Probe photon number and source/pump wall-plug energy are separate ledgers.

This caveat is not a refutation of the paper's distinct Bell-QSL theorem. It prevents accidentally transferring a resource convention from one theorem/result class to another.

### Small executable resource-model check

Added `squeezed_vacuum_mean_photon_number` and its inverse to `software/uqpu-prototype/uqpu/fundamental_limits.py`, plus `test_squeezing_probe_resources.py`. The test checks the analytic identity for a single-mode squeezed vacuum and the source example `r = 0.5*log(n)`, where the photon count grows as `(n + 1/n - 2)/4 = Theta(n)`. This is **MODEL_ONLY analytic resource accounting**; it does not simulate Bell-QSL, prove a quantum advantage, or estimate wall-plug energy. Exact-head CI remains the acceptance gate.

Other surveillance deltas were checked against current repository coverage:
- MorphingNet symbolic regression has pending-branch coverage (PR #117); it was not duplicated as merged evidence.
- AI-generated mathematical instruments are covered by canonical Batch 062.
- Searches also covered theorem discovery, physics-informed/automated modeling, new effective laws, lower bounds, experimentally motivated anomalies, biomass/materials, fusion and provider updates. No third-party result was promoted into project evidence.

## A–H status

| Lane | Status | Next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Candidate Bell-QSL property-vector workload scoped; squeezing-only and entanglement-enabled resource conventions explicitly separated. | Extract exact theorem assumptions and independently implement an analytic small instance. |
| B — cloud/QPU/provider integration | Provider-neutral policy retained; modality mismatch is an explicit gate. | Map only to a compatible, authorized sensing platform; simulator/dry-run first. |
| C — memory/state/data movement | Output precision, reconstruction, I/O and persistence required in the contract. | Measure full acquisition-to-output data path. |
| D — devices/chip/process/packaging | Squeezing, source, detector, loss, bandwidth and calibration requirements recorded. | Obtain target-specific controls/noise and loss data. |
| E — biomass/materials/bio-oil/fusion/energy/cooling | No direct new result. | Continue BIO-001/FUS-001 with accepted-product and net-electricity evidence. |
| F — economics/benchmarks/evidence/integration | Matched baseline, probe-energy convention, wall-plug source energy and total cost per accepted output separately required. | Implement resource-normalized ledger; retain negative results. |
| G — manufacturing systems | Downstream only; no equipment/fab claim. | Translate only validated control needs into yield/process requirements. |
| H — strategy/publication | Dated source analysis and integration record added on review branch. | Preserve strategic references and wait for review/CI before canonical promotion. |

## Foundation and equation-discovery tracks

- **FND-001:** full source/control/readout energy required; no measured thermodynamic gap.
- **FND-002:** count classical output dimension, precision and reconstruction; no memory replacement result.
- **FND-003:** query-complexity separation is not a quantum-speed-limit violation.
- **FND-004:** bosonic squeezing/entanglement is a known-physics candidate primitive; not a new primitive claim.
- **FND-005:** no elementary-particle or QFT mechanism follows.
- **FND-006:** source assumptions, independent model and falsifiers are frozen before execution.
- **EQN-001–006:** no AI-generated equation or physical law promoted.

## INV-029–035

No mission-level gate passed. No Pangola material substitution, accepted bio-oil, net fusion electricity, project-principal/interest reduction or WACC change was measured. INV-034/035 remain upstream constraints: explore widely, but current physics governs engineering and new equations require held-out predictions, falsifiers and independent validation.

## Validation and synchronization

The JSON benchmark manifest and integration record were parsed before publication and rechecked after the resource-normalization amendment. No scientific simulation, provider SDK run, physical experiment or paid QPU job was executed.

An earlier Actions run (40262334339) passed on a superseded PR head, but that commit is no longer part of the current branch history after the commit-trailer repair and resource-helper/test additions. It is **not** validation of the current head. The exact current head's own workflow run must complete before merge or promotion. The combined commit-status endpoint may return no entries even when workflow runs exist, so inspect the workflow run/jobs directly.

Canonical main remains unchanged. README and append-only ledgers are intentionally untouched until review, collision reconciliation and exact-head CI.

## Highest-value next gate

Extract the paper's exact task/oracle/resource assumptions from the article and supplemental material; independently implement one analytically checkable signal family; compare the entire property vector against homodyne, heterodyne and the strongest eligible entanglement-free baseline at matched quality and signal access; then sweep squeezing, loss, detector efficiency, bandwidth and calibration. Report equal-total-probe-energy and separately budgeted-squeezing comparisons independently, including source/pump energy. Stop promotion if the advantage vanishes after full resource accounting or fails held-out cases.

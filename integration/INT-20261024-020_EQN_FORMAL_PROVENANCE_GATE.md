# Integration handoff — INT-20261024-020 equation proof/provenance gate

**Date:** 2026-10-24  
**Status:** PROPOSED / PR REVIEW REQUIRED  
**Canonical main at cycle start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-eqn-proof-provenance-gate`  
**Primary owners:** Lane A owns the validator and tests; Lane H owns the literature watch; integration hub owns this cross-lane routing record.  
**Evidence class:** SOFTWARE_CONTRACT_CHANGE + LITERATURE_ONLY  
**Project evidence promotion:** none

## What changed

- `software/uqpu-prototype/uqpu/equation_discovery.py`: required data/proof provenance and an independent-validation plan to be present and nonblank; validate all required tuple entries; reject nonnumeric, non-finite or negative held-out errors; require a nonnegative integer independent-validation count.
- `software/uqpu-prototype/tests/test_equation_discovery.py`: add fail-closed tests for missing provenance/validation, blank tuple entries, NaN/infinities, negative/nonnumeric errors and invalid replication counts.
- `docs/literature_watch/2026-10-24-formal-proof-search-and-ai-math-revision-boundary.md`: record the *Science* formal-proof-search result, the official AI-mathematics release's correction/withdrawal history, limitations and falsifiable UQPU follow-up.

This patch closes a metadata-validation inconsistency: `required_discovery_fields()` listed both provenance and independent validation, but `validate()` did not enforce them, and `testable` accepted either field. It also prevents NaN/infinite values from slipping past a simple negative-error check. It does **not** evaluate whether an equation is true or whether a mathematical formalization faithfully models nature.

## A–H status and integration edges

| Lane | Current result / next gate |
|---|---|
| A — quantum programming/workloads/compiler/runtime | Validator hardening and adversarial unit tests added; exact-commit hosted CI is pending. Priority remains unchanged. |
| B — cloud/QPU/provider integration | No credentials, target query, provider call or QPU job; dry-run boundary unchanged. |
| C — RAM/VRAM/HBM/storage/state/data movement | Output-information and explicit classical I/O contracts remain binding; proof artifacts are not readable-state or storage advantage. |
| D — device/chip/process/fabrication/packaging | No device evidence; D/G co-design continues without promotion. |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | BIO-001, FUS-001 and Pangola routes receive no new measurement or evidence promotion. |
| F — economics/benchmarks/evidence/integration | Record formal-check outcome separately from held-out quality, false-discovery rate, review effort and total cost per accepted task. FIN-001 remains measurement-gated. |
| G — manufacturing equipment/software/factory | No tooling, process-window, yield or factory economics evidence. Continue D/G co-design. |
| H — strategic finance/publication/future industries | Literature-only result recorded with revision history and bounded, falsifiable follow-up. Multilingual strategic-plan links remain untouched. |

The repository currently also has an experimental Lane I program; this A–H integration does not silently reclassify it or replace the user's permanent A–H architecture.

## Invariant contribution

- **INV-029:** no Data-Center-to-One-Phone capability, physical-compression, energy or lifecycle-cost result.
- **INV-030:** no critical-material substitution or biomass-carbon experiment.
- **INV-031:** no accepted-liquid fuel yield, quality or cost result.
- **INV-032:** no net delivered fusion-electricity or commercial cost result.
- **INV-033:** no measured principal, interest, financing-rate or WACC change.
- **INV-034:** strengthens the mathematics-first proof/falsification workflow without relaxing current physical limits.
- **INV-035:** requires traceable provenance and an independent-validation path; AI-generated equations remain hypotheses until the relevant proof/experiment and replication gates pass.
- **INV-025/026/027:** no moonshot promotion; functional equivalence, lower-bound and open-frontier rules remain intact.

## Validation and synchronization

- Source files were read from canonical main SHA `c7b5958af58fad04a101ef5c6abf6a29293c867e` before editing.
- Unit tests have been added but **are not yet reported as passed**; hosted CI on the exact source commit is the next gate.
- No paid QPU job, material/fuel experiment, fusion experiment, purchase or credentialed provider call was made.
- This source branch is not on canonical `main`. Do not claim canonical synchronization until the PR is reviewed and merged. Record the source-SHA-to-main-SHA mapping and rerun the cold-start audit after merge.
- Existing INV-029–035 root directives, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md` and the Thai/English/Chinese/Japanese/Korean/German public-link table are preserved and unmodified.

## Next highest-value gate

Obtain exact-commit CI for the validator tests. If green, review the diff for compatibility and merge only through the repository's normal review/synchronization policy. Then design EQN-002's sealed-split benchmark with record-level disjointness certificates; a formal proof or a symbolic-regression fit alone is not physical evidence.

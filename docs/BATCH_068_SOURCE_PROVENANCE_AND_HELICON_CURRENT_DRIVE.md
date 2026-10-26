# Batch 068 — source-provenance preflight and helicon current-drive evidence boundary

**Date:** 2026-10-26  
**Canonical starting main SHA:** 5879e658587a5d45bf8f85bda8077340e04b4bd3  
**Primary owner:** Lane A — quantum programming/runtime and reproducible equation-discovery tooling  
**Energy evidence owner:** Lane E — fusion, cooling and infrastructure  
**Integration/economics owner:** Lane F  
**Publication/strategy owner:** Lane H  
**Shared IDs:** RG-046, FUS-001, FND-003/006, EQN-001–006, INV-029–035  
**Evidence class:** SOFTWARE CONTRACT + UNIT TESTS PENDING EXACT-HEAD CI + PEER-REVIEWED EXTERNAL LITERATURE; NO UQPU ADVANTAGE OR NET-ELECTRICITY CLAIM PROMOTED

## Starting-state inspection

Started from the current main head, not a remembered batch number. Inspected PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the latest committed Batch 067, RG-046 and related gaps, the integration hub, root directives 00/00A/01–06, the eight-lane scoreboard and the GitHub Actions workflow/run state.

The permanent root directives, INV-025/026/027, research_lanes A–H, integration hub, and public Thai/English/Chinese/Japanese/Korean/German master-plan links remain intact. No append-heavy aggregate history was overwritten. Paid QPU execution remains unauthorized and was not attempted.

## Lane A implementation

Added a provider-neutral source-provenance manifest contract in software/uqpu-prototype/uqpu/dataset_provenance.py and regression tests in software/uqpu-prototype/tests/test_dataset_provenance.py.

The preflight binds:
- HTTPS source URL and a non-branch-alias source revision identifier;
- explicit license identifier and acquisition date;
- normalized relative raw-file paths and SHA-256 values;
- the raw-record-bound dataset digest and row count from the split manifest;
- hashes of schema, deterministic preprocessing, inclusion policy, exclusion policy and group-holdout policy;
- a canonical digest over the provenance manifest.

The bundle preflight composes this manifest with the existing raw-record binding and split-disjointness verifier. Tests cover the valid bundle path, deterministic raw-file ordering, tampering, cross-dataset reuse, mutable branch aliases, missing license, non-HTTPS source, unsafe/duplicate paths, malformed digests and changed raw records.

**Non-claim:** this is a local consistency contract. It does not download the source, independently authenticate bytes, establish legal license compliance, prove that the dataset is representative, or validate an equation. No public benchmark has yet been pinned and audited. RG-046 therefore remains OPEN.

## Fresh literature surveillance

Published docs/literature_watch/2026-10-26-helicon-current-drive-fusion-boundary.md for Lestz et al., *Physical Review Letters* 137, 155101, published 2026-10-09, DOI 10.1103/mbn4-fd4v. The peer-reviewed DIII-D result supports helicon-wave core power deposition and auxiliary current drive in the tested conditions. It is relevant as an additional FUS-001 architecture input, but supplies no plant wall-plug efficiency, recirculating-power ledger, net electricity, availability, CAPEX, lifecycle cost or financing result.

The literature watch separates plasma-coupled RF power from wall-plug electrical input, requires matched controls and source-data reconstruction, and defines falsifiable follow-up. It does not convert third-party experimental results into project evidence.

## A–H status

- **A — Quantum programming/workloads/compiler/runtime:** source-provenance bundle preflight and tests added. Still no pinned public dataset or matched >=30-seed method comparison; no workload-level QPU advantage.
- **B — Cloud/QPU/provider integration:** provider-neutral adapter and simulator/dry-run-first rules preserved; no credentials or paid jobs.
- **C — RAM/VRAM/HBM/storage/state/data movement:** provenance and row counts are metadata, not physical memory capacity or readable quantum-state storage; no device-level memory result.
- **D — Device/chip/process/fabrication/packaging:** helicon antenna/diagnostic interfaces added to the evidence map; no UQPU device, process-window, packaging or lifetime qualification. Continue D/G co-design.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** a peer-reviewed current-drive experiment is newly indexed for FUS-001; no Pangola functional substitution, accepted bio-oil, commercial fusion or net delivered electricity demonstrated.
- **F — Economics/benchmarks/evidence/integration:** provenance is linked to dataset/split hashes and policies; fusion accounting keeps plasma-coupled power separate from wall-plug demand. No accepted-task cost, LCOE or WACC change measured.
- **G — Manufacturing equipment/software/factory systems:** RF source, antenna, diagnostics, metrology, maintenance and replacement are explicit future cost/yield interfaces; no manufacturing throughput or yield evidence.
- **H — Strategy/finance/future industries:** dated literature watch and this integration batch preserve the strategy-to-evidence boundary and financing discipline.

## Foundational and equation-discovery status

- **FND-001:** finite-state/thermodynamic-gap accounting remains MODEL_ONLY; no measured physical work, heat, memory traffic or accepted-task quality added.
- **FND-002:** output-information and reconstruction lower-bound work unchanged; no equivalence between Hilbert-space dimension and readable classical storage.
- **FND-003:** no matched control-vs-quantum-speed-limit measurement. Helicon current-drive data are an external plasma-control lead, not a speed-limit experiment.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no validated QFT/particle mechanism or promoted anomaly.
- **FND-006:** source provenance is strengthened as a precondition for reproducible equation-discovery benchmarks; no equation candidate is promoted.
- **EQN-001–006:** generator → constraints → evaluator → held-out test → counterexample search → proof/simulation → discriminating experiment → independent replication → device/system consequence → economics remains the required chain. Provenance is a prerequisite, not a result.

## INV-029 through INV-035

- **INV-029:** Data-Center-to-One-Phone remains a falsifiable long-horizon physical-compression mission; this cycle provides no phone-class integration or lifecycle-cost evidence.
- **INV-030:** no elemental transmutation; no qualified Pangola/residue-carbon functional substitute or recovery/recycling benefit measured.
- **INV-031:** no accepted liquid fuel, complete process yield or saleable bio-oil cost result.
- **INV-032:** helicon current drive is an external experimental control milestone; no net reliable delivered electricity or full lifecycle cost is shown.
- **INV-033:** no measured financed-principal, absolute-interest, WACC or economy-wide-rate change.
- **INV-034:** the deep-frontier agenda remains active with explicit external-evidence and falsification boundaries.
- **INV-035:** current physics remains binding for engineering claims; AI-generated equations and fitted models are not physical laws by declaration.

INV-025/026/027 and the 100,000,000-GPU / universal 100,000,000-unit goals remain evidence-gated. NPU comparison still requires workload semantics, quality, precision, latency, throughput, data movement and total cost.

## CI and synchronization

At the start of this batch, the exact-head workflow for 5879e658587a5d45bf8f85bda8077340e04b4bd3 had Python 3.10/3.11/3.12 test jobs and the reference benchmark passing, with several independent Qiskit/QSP/QSVT jobs still running. The cold-start handoff audit had passed. The combined-status endpoint returned no legacy status rows; Actions jobs are the relevant CI record. Exact-head CI for this batch must be checked after commit.

The large append-heavy RESEARCH_GAPS.md and WORKLOG.md remain untouched. RG-046 is updated in its standalone artifact; aggregate-index synchronization remains debt.

## Next highest-value gate

1. Choose one public, licensed, immutable equation-discovery benchmark source.
2. Record actual raw file hashes, exact revision, license/usage terms, acquisition date, schema, deterministic preprocessing and inclusion/exclusion/group policy hashes.
3. Have an independent reviewer rebuild the provenance and split manifests from the same pinned source.
4. Run a preregistered, resource-matched comparison with at least 30 identical seeds per method, held-out law families/scales, counterexample and false-discovery accounting, and consistent compute/energy/cost basis.
5. In parallel, obtain the helicon paper's detailed power and uncertainty data, reconstruct matched-control observables, and propagate only traceable values into FUS-001.

No root invariant, multilingual strategic reference or append-only history was removed or weakened.

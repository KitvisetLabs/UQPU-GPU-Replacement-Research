# Research gap RG-A-QGPA-SPECS-001 — application-level workload contracts

**Opened:** 2026-10-30  
**Primary owner:** Lane A — workloads/runtime  
**Evidence owner:** Lane F  
**Publication owner:** Lane H  
**Status:** OFFICIAL DOMAIN LIST FOUND / APPLICATION-LEVEL SPECIFICATION INCOMPLETE / NO UQPU REPRODUCTION  
**Related:** INV-029, INV-034/035, FND-001–006, EQN-001–EQN-006; lanes A–H

## Current evidence

The U.S. Department of Energy's 2026-10-08 announcement, [DOE Announces Science Applications for Quantum Computing](https://www.energy.gov/science/articles/doe-announces-science-applications-quantum-computing), states that eight Quantum Genesis Priority Applications span chemistry, materials, subatomic physics, and applied mathematics. The announcement body describes these four domains but does not enumerate all eight application-level specifications. The DOE [Genesis Agent Skills release](https://www.energy.gov/science/articles/genesis-agent-skills-release-support-innovation-across-genesis-mission) (2026-10-15) and [hackathon recap](https://www.energy.gov/undersecretaryforscience/genesis-mission/articles/genesis-mission-hackathon-brings-research) (2026-10-21) provide official scientific-workflow and interoperability context, not benchmark results.

The Lane A contract map at `research_lanes/A_quantum_programming_runtime/DOE_QGPA_DOMAIN_CONTRACT_MAP_2026-10-30.json` records only source-listed domains and common acceptance fields. It intentionally does not infer missing application names or target computations.

## Unlock criteria

1. Retrieve the complete official application list/specifications and any reference data, source code, license, and version metadata.
2. Define each named application's accepted output, error tolerance, input encoding, output/readout requirements, and exact/reference baseline.
3. Freeze group-disjoint held-out regimes and equal resource budgets before tuning; include misspecified-model, null, and failed-run controls.
4. Compare classical baselines and provider-neutral lowering with target-aware simulation before any authorized hardware run.
5. Record quality, latency, throughput, host compute, memory/state, I/O/transfer, reconstruction, retries, energy when measurable, billable usage, pricing provenance, and cost per accepted task.
6. Require independent review and exact-head CI. Paid QPU execution requires credentials, a bounded budget, and explicit user consent.

## Nonclaims

This gap is not evidence of quantum advantage, new physics, memory/storage replacement, material substitution, commercial bio-oil, net fusion electricity, lower WACC, or Data-Center-to-One-Phone feasibility. The DOE program's priorities and resources are not UQPU measurements.

# Research gap RG-QEC-TEMPORAL-DECODER-001 — temporal-parallel decoder transfer

**Opened:** 2026-10-30  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Co-owners:** A — workload/reference correctness; C — syndrome state and I/O; D/G — device/process/equipment; F — benchmark/evidence/economics; H — publication  
**Status:** OPEN / LITERATURE_ONLY / SOURCE REPRODUCTION NOT RUN  
**Source:** Itoh et al., arXiv:2607.27930, https://arxiv.org/abs/2607.27930  
**Related:** INV-004/007/019/022/024/025/026/027/029/034/035; FND-003; FIN-001

## Objective

Determine whether temporal-window sandwich decoding with a Union-Find inner decoder provides a reproducible latency/quality benefit under a matched surface-code workload, and whether any benefit survives area, memory, power, reliability and lifecycle-cost accounting.

## Current evidence and limitations

The source reports RTL simulation, Rust/Stim threshold simulation and ASIC logic-synthesis estimates for TSMC CMOS 22 nm and ASAP7 predictive 7 nm. It does not report fabricated-silicon measurements or an independent UQPU reproduction.

At d=21 and phenomenological p=1%, the paper reports about 34.9% lower mean latency and 11.5% lower worst-case latency versus batch Union-Find. At p=0.1%, it reports about 34.6% lower mean latency but 7.2% worse worst-case latency. Synthesized area is reported around 1.3–1.5x the batch design. Phenomenological thresholds are reported as 1.6% (batch) and 1.5% (sandwich); the circuit-level result is approximately 0.25% for both. These values are model-/tool-/source-specific, not UQPU measurements.

## Blockers

- Upstream RTL, exact repository revision, license, simulator configurations and synthesis scripts are not yet pinned and hashed in this project.
- No independently regenerated identical syndrome corpus, held-out noise configuration, confidence interval or UQPU test run exists.
- No physical FPGA/ASIC latency, power, area, yield, thermal, reliability or lifecycle-cost measurement exists.
- The paper's d=23 batch synthesis failed under a 450 GB virtual-memory cap; the reason and repeatability must be separated from algorithmic scaling.
- A mean-latency improvement does not establish a per-round deadline guarantee; worst-case regressions must remain visible.

## Unlock protocol

1. Pin source/data/tool/PDK versions and SHA-256 hashes; preserve license and provenance.
2. Reproduce the published batch and sandwich decoder arms using identical Stim syndrome instances, code distance, syndrome rounds and noise model. Keep p=1% and p=0.1% separate and run the circuit-level model as a separate arm.
3. Report mean/p50/p95/p99/worst latency, deadline-miss fraction, logical failure rate with uncertainty, maximum frequency, area, memory/FIFO/ring-buffer bytes, power if measurable, resource use and all failed runs.
4. Cross-check software, RTL simulation and synthesized results; include d=23 stress behavior without interpreting host memory exhaustion as a physical lower bound.
5. Require independent reproduction and physical device measurements before any device-level or system-cost promotion.

## Acceptance / rejection

Accept the narrow latency hypothesis only if the matched baseline and candidate use identical task/noise/provenance contracts, output quality meets a predeclared threshold with uncertainty, the relevant latency tail meets the actual control deadline, and area/memory/power/resource tradeoffs are reported. Reject or narrow the hypothesis if worst-case deadline misses or logical failures worsen, comparisons mix process/noise/evidence contexts, or system overhead erases the gain.

## Cross-lane consequences

- A/B: no QPU execution success or advantage claim follows from decoder simulation.
- C: count syndrome, ring-buffer, FIFO, seam and reconstruction state; no readable-memory equivalence claim.
- D/G: co-design clock/process/area and production-test requirements; synthesis is not silicon.
- E: no new biomass/material/bio-oil/fusion evidence.
- F/H: no measured economics, financing, WACC or capital-efficiency claim; strategic plans remain context.

No paid QPU job is authorized. This gap is not evidence of quantum advantage, new physics, physical memory replacement or Data-Center-to-One-Phone feasibility.

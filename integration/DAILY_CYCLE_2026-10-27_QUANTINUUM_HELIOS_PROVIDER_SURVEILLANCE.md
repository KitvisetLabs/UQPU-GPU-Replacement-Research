# Eight-Lane integration — 2026-10-27 — Quantinuum Helios QEC provider surveillance

**Cycle artifact:** Batch 079  
**Start head:** `e698c4fc6064d6e9faadf8388ae791b8d90af6f5`  
**Evidence class:** OFFICIAL PREPRINT REPORTING EXPERIMENTAL QEC; independent reproduction OPEN  
**Canonical gap:** `docs/RESEARCH_GAP_QEC_HELIOS_COLORCODE_REPRODUCTION_2026-10-27.md`

## Integration outcome

The official preprint arXiv:2610.24077 reports below-threshold triangular color-code memory experiments at code distances 3, 5 and 7 on Quantinuum Helios, with logical memory error down to 5×10^-6 per correction round and an estimated suppression factor of 12 (uncertainty -2/+3) per tested distance increase. It reports logical two-qubit Clifford error around 7×10^-5 at distance 5 and compares decoder methods. These are external experimental results, not UQPU reproduction.

The result matters to B/D/G because it gives a current, target-specific logical-error and physical-resource co-design case. It matters to A because workload contracts must distinguish memory error, gate error, decoder latency and accepted-task quality. It does not establish universal fault tolerance, full application advantage, lower cost or lower energy.

## Cross-lane actions

- **A:** maintain distinct metric types and require target-aware lowering plus identical useful-output contracts.
- **B:** verify Helios access route, supported API/SDK, pricing and job constraints before a hardware plan.
- **C:** include physical-qubit ratio, syndrome data movement and decoder memory/latency.
- **D/G:** co-design code distance, device operations, measurement cadence, control and fabrication assumptions; no yield/cost claim.
- **E/F:** no energy, fuel, fusion, finance or accepted-task economics result; preserve full-system cost boundaries.
- **H:** preserve official preprint and company-source links, distinguishing observed experimental scope from roadmap claims.

## Validation and next gate

Batch 078's Python unit/invariant matrix passed on Python 3.10, 3.11 and 3.12; the extended workflow remained in progress at last inspection. The Batch 078 cold-start handoff audit passed. The current provider-watch commit must also pass exact-head CI. No paid QPU job was submitted.

Next: independently reproduce source tables/uncertainties and validate the actual provider-access path; only then design a bounded, consented workload experiment.

# Batch 106 — in-situ photonic training evidence gate and eight-lane integration

**Date:** 2026-10-29
**Starting main SHA:** c9c55b275d60798cb7a2428693fee39e251ab30e
**Primary lane:** D (photonic device/training method); A remains Priority #1 for software/useful-output contracts
**Cross-cutting:** A–H; INV-025–027 and INV-029–035; FND-001–006; EQN-001–010; BIO-001, FUS-001, FIN-001
**Evidence class:** PEER-REVIEWED THIRD-PARTY EXPERIMENTAL LITERATURE / ACCEPTANCE CONTRACT / UQPU REPRODUCTION OPEN
**QPU spending:** none; no paid QPU execution authorized or attempted

## 1. Canonical-state and invariant audit

Started from the current GitHub main head, not a fixed batch number. Read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the 00/00A/01–06 root directives, Batch 105 and its parity/catalyst artifacts, the latest October 28 gaps, integration reports, lane map and CI state.

Main at start: c9c55b275d60798cb7a2428693fee39e251ab30e. At audit, both exact-head Actions workflows completed successfully: UQPU Prototype and Project Invariants (run 1970) and Autonomous Cold-Start Handoff Audit (run 1231). The legacy combined commit-status endpoint had no status records and reported pending; Actions run conclusions are the direct CI evidence used here.

All eight operational lanes A–H and the D/G co-design requirement remain active. The root directives, six multilingual public master-plan editions (Thai, English, Chinese, Japanese, Korean and German), strategic AI-agent/funding references, INV-025/026/027, and permanent mission pillars are preserved.

## 2. Lane A priority and useful-output contract

Batch 105's independent GF(2) graph-parity rank oracle is now covered by the exact-head CI run. This establishes a bounded classical mapping/rank check only. It does not implement a higher-order parity-QAOA circuit or establish quantum advantage.

Lane A next gate remains: implement or pin a parity-QAOA circuit; compare its decoded outputs against exact small-graph objective/reference certificates; record circuit depth, two-qubit gates, qubits, shots, optimizer evaluations, retries, reconstruction, host time, state/I/O/memory and target-specific pricing; then run matched simulator tests. Only after these gates may authorized real-QPU execution be considered. Execution success is not quality acceptance.

## 3. Fresh literature delta — photonic in-situ physical gradient descent

A primary paper published 2026-10-05 in *Nature Computational Science* reports INSPIRE, an in-situ photonic training method using on-chip synthetic time-reversal holography to estimate physical gradients. The authors report 0.26% relative error on trained matrices, training through scattering media beyond the native tunable-element count, 251-fold model compression and 136-fold task-specific training acceleration. Paper: https://doi.org/10.1038/s43588-026-01057-y. Code/training package: https://doi.org/10.5281/zenodo.21918485.

The genuine novelty is a hardware-in-the-loop training method for photonic circuits whose fabricated physical response may differ from a digital model. These metrics are source-reported and workload-specific. UQPU has not reproduced the paper, and the reported compression/acceleration is not a full-system energy/cost or universal computing advantage.

Added a focused Lane D gap that freezes the workload and acceptance predicate, requires clean-source reproduction and held-out device/topology/wavelength tests, and accounts for laser/control/readout/ADC-DAC/host energy, calibration, data movement, fabrication yield, packaging, service life and lifecycle cost. Falsification is explicit: if these overheads or held-out failures erase the benefit, the advantage hypothesis is rejected.

## 4. Eight-lane status

| Lane | This cycle | Next gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | Exact-head CI passed the independent GF(2) rank test; a follow-up adds exhaustive encode/decode-bijection checks for every simple graph through five vertices (follow-up CI pending). | Parity-QAOA circuit + exact objective/decode oracle + matched simulator. |
| B — cloud/QPU/provider integration | Provider-neutral adapters retained; no SDK target or paid QPU job used. | Simulator/dry-run first; preserve target-specific calibration, probability and price pairing. |
| C — RAM/VRAM/HBM/storage/state/data movement | Added explicit optical-electronic conversion, readout, calibration-data, transfer and reconstruction accounting to the photonic acceptance gate. | Measure bytes, peak memory, conversion latency and full-system energy per accepted task. |
| D — devices/chips/process/packaging | Added a peer-reviewed INSPIRE literature watch and falsifiable reproduction gap. | Pin code/data; replicate on held-out device/topology/wavelength. |
| E — biomass/materials/bio-oil/fusion/cooling | BIO-001 catalyst-char and yield-basis gaps; FUS-001 pyFECONs account-mapping gap remain open. No new experiment. | Pangola dry-basis mass/energy closure and FUS-001 net-electric account reproduction. |
| F — economics/benchmarks/evidence/integration | Enforced task-level acceptance and full overhead/cost boundary; source results remain external evidence. | Compare total cost/energy per accepted task with uncertainty and no double-counted credits. |
| G — manufacturing equipment/factory systems | Explicit D/G interface: tunable-element count, device yield, metrology, calibration, package, drift and cost per good device. | Build cost/yield evidence from a pinned fabrication flow; no manufacturing advantage claimed. |
| H — strategy/finance/future industries | Ketskaew Chulamani / Kanusanan Pongpanna Model and six-language master-plan links retained. | Translate verified compute/material/energy results into financed-principal and time-to-evidence scenarios without treating them as funding or WACC evidence. |

All 28 unordered A–H pairs were reviewed conceptually through the shared integration interface. Active links for this batch are A↔C, A↔D, A↔F, C↔D, C↔F, D↔G, D↔F, F↔G and F↔H. Other pairs are retained as N/A for this particular photonic experiment because no defensible direct causal dependency is established; this does not suspend any lane.

## 5. Foundations, equation discovery and permanent pillars

- **FND-001–006:** no new lower bound, proof or physical experiment. Existing thermodynamic, output-information, quantum-speed-limit, measurement/readout and causality limits remain binding. Photonic in-situ training is an alternative implementation lead, not evidence of a changed fundamental limit.
- **EQN-001–010:** no new physical equation or law discovered. Any gradient or device-response model must be checked against the incumbent optical model, units, conservation/energy balance, held-out predictions, counterexamples and independent validation.
- **BIO-001 / INV-030–031:** Batch 105's catalyst-loaded biochar watch remains literature-only; no Pangola transfer, accepted commercial fuel or critical-material substitution is demonstrated.
- **FUS-001 / INV-032:** the pyFECONs account mapping and uncertainty reproduction remain open; no commercial fusion-electricity result.
- **FIN-001 / INV-033:** lower financed principal or shorter lock-up can reduce absolute interest at unchanged terms; no lower WACC/risk premium is inferred here.
- **INV-029:** the $10T–$100T ambition scale remains a proxy that must be translated to equivalent compute/AI/memory/storage/networking/energy/thermal/reliability/lifecycle-cost contracts. External lasers, control, readout, host, power and cooling count against physical compression.
- **INV-034–035:** deep-frontier and AI equation-discovery principles remain active. No equation is promoted to a physical law by fit, elegance or AI generation.
- **INV-025/026/027:** the 100,000,000-GPU and universal 100,000,000-unit targets remain falsifiable goals; Hilbert-space dimension is not readable classical memory, and NPU comparisons require workload quality/precision/latency/throughput/memory/data movement/cost.

## 6. Integration and CI

Added `docs/literature_watch/2026-10-29-photonic-in-situ-physical-gradient-descent.md`, `docs/RESEARCH_GAP_PHOTONIC_INSPIRE_END_TO_END_2026-10-29.md`, and an integration report. A follow-up also adds an exhaustive encode/decode-bijection test over all simple graphs through five vertices and corrects the research-gap index path. Updated README, WORKLOG, RESEARCH_GAPS and integration navigation in the same main commit so the project landing page records the change. Root strategy files and multilingual links were not overwritten.

Base-head CI was green: `uqpu-tests.yml` run 1970 and `cold-start-handoff.yml` run 1231. The new commit still requires its own exact-head runs. No local reproduction, photonic lab work, biomass/fusion experiment, or paid QPU execution occurred.

## 7. Next highest-value gate

Lane A: implement and verify the parity-QAOA circuit against exact small-instance objective and decode certificates. In parallel, Lane D/G should pin and reproduce INSPIRE's source package, then evaluate held-out device performance under a matched end-to-end task/energy/cost contract. Keep BIO-001, FUS-001 and FIN-001 gaps open until their full evidence gates pass.
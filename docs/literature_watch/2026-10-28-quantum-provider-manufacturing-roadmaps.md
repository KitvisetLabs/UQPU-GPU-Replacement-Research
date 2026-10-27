# Provider/device surveillance — 2026-10-28 — integrated quantum control and manufacturing roadmaps

**Accessed:** 2026-10-28  
**Evidence class:** COMPANY_ANNOUNCEMENT / ROADMAP_ONLY  
**Owners:** Lane B (provider integration), Lane D (device/chip), Lane G (manufacturing equipment/software), Lane F (evidence/economics), Lane H (publication)  
**Feeds:** INV-010, INV-013, INV-015/016, INV-024, INV-029, INV-034/035

## 1. IonQ Superion 256 and SkyWater manufacturing

IonQ's 2026-09-08 company announcement says its Superion 256 product family has integrated 256-qubit QPU chips fabricated at its SkyWater subsidiary and ions trapped in prototype systems, with customer deliveries planned for 2027. The company also projects a greater-than-300x reduction in cost per qubit across its roadmap as electronic control replaces laser-based control. Source: https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing.

**Interpretation:** this is a material Lane D/G co-design signal: quantum device architecture, control electronics, foundry process, packaging and production iteration are being treated as a coupled manufacturing problem. It is also a Lane B provider-discovery lead because production-grade systems are expected to be offered through IonQ cloud.

**Evidence boundary:** these are company statements and roadmap claims. This cycle did not independently verify production yield, shipping systems, customer deliveries, target availability, calibration, pricing, uptime, total energy, accepted-task cost or the projected cost-per-qubit reduction. Cost per qubit is not cost per accepted useful task and cannot substitute for a workload-specific benchmark.

## 2. Pasqal photonic integrated-circuit control

Pasqal's 2026-08-10 announcement says it used a photonic integrated circuit from Aeponyx to generate laser light that traps individual atoms, positioning integrated photonics as a possible route to reduce the complexity of free-space optical control. Source: https://www.pasqal.com/newsroom/pasqal-brings-qubit-control-on-chip-advancing-the-path-to-fault-tolerant-quantum-computing-at-scale/.

**Interpretation:** another Lane D/G co-design lead: compare photonic-control integration with electronic-control integration under explicit device yield, stability, calibration, power, packaging, serviceability and lifecycle-cost metrics. This announcement is not an independent reproduction or proof of a scalable fault-tolerant system.

## Provider-neutral follow-up

Keep IBM Quantum, Amazon Braket, Azure Quantum and their hosted providers, IonQ, Rigetti QCS, D-Wave Leap, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers behind provider-neutral capability descriptors. For each route, separately record provider/target identity, SDK/API version, availability and access restrictions, calibration snapshot, native operations, qubit/mode topology, error metrics, shot/task billing, host and data-transfer costs, energy where measurable, and output-quality acceptance. Never combine one target's probability or calibration with another target's price.

Before any live submission, use simulator/dry-run first. Paid execution remains disabled until credentials, a bounded budget and explicit user consent exist.

## Falsifiable follow-up

1. Track whether Superion 256 becomes an actually accessible target, with dated documentation and target-specific calibration/pricing.
2. Compare electronic versus photonic control only after matched useful workload, gate/error requirements, availability, packaging, power and cost data exist.
3. Separate company projections from measured device, fab-yield and end-to-end task evidence.
4. Require independent validation before promoting roadmap statements to device or economic evidence.

**Non-claims:** no current provider capability or pricing change is asserted; no quantum advantage, production-yield result, lower cost per accepted task, new physical law, or INV-029 achievement is established.

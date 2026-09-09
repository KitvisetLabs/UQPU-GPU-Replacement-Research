# Quantum Market Delta — 2026-09-09

## Why this matters
This delta records market changes that alter active UQPU/UQCS research assumptions across Lane B, D, F, G and H.

## IBM Quantum — Nighthawk r2 / ibm_phoenix
IBM's September 2026 Quantum Compute Service changelog reports the first Nighthawk r2 QPU, `ibm_phoenix`, now available to Premium, Flex and Pay-As-You-Go plans.

Official IBM claims:
- 120 programmable qubits;
- square-lattice high connectivity;
- up to 25x higher throughput than Heron while matching fidelity;
- default repetition delay reduced to 1 microsecond via independent high-speed reset;
- throughput above 100,000 MCPS.

Source:
https://quantum.cloud.ibm.com/docs/en/guides/changelog-quantum-compute-service

### UQPU implication
For Priority #1 programming work, throughput is now a first-class provider-selection metric. A smaller physical-qubit count can be economically preferable if higher circuit throughput reduces billed runtime and experimentation latency.

## Quantinuum — Helix QEC on Helios
Quantinuum reported Helix, a scalable fault-tolerant architecture experimentally validated on Helios, including logical memory, logical computation and logical entanglement across multiple QEC codes, with logical-level results outperforming corresponding physical-level results without post-selection.

Sources:
https://www.quantinuum.com/news/blog
https://www.quantinuum.com/blog/quantinuums-fault-tolerance-advantage-turning-quantum-reliability-into-commercial-usefulness

### UQPU implication
Lane A/C should treat logical state-service and logical-memory semantics as an increasingly practical research target rather than only a far-future abstraction. Lane F must still include logical-operation overhead and provider pricing.

## Quantinuum — manufacturing and cloud expansion
Quantinuum announced:
- Oracle Cloud Infrastructure partnership to deploy Helios as an OCI service;
- a USD 100 million CHIPS R&D award supporting trapped-ion quantum semiconductor manufacturing;
- collaboration with GlobalFoundries for next-generation ion traps/control electronics and Monarch Quantum for lasers/optical components.

Sources:
https://ir.quantinuum.com/news-releases/news-release-details/quantinuum-reports-second-quarter-2026-results
https://ir.quantinuum.com/news-releases/news-release-details/quantinuum-finalizes-100-million-chips-rd-award-us-department

### UQPU implication
Lane B provider surveillance should add OCI as a future/active access route when public service details are available. Lane D/G should track ion-trap fabrication, control electronics and optical-component manufacturing as concrete industrial reference architectures.

## IonQ — platform plus foundry integration
IonQ reported increased 2026 guidance following its SkyWater acquisition and described manufacturing scale as part of its path toward commercial fault-tolerant quantum computing.

Source:
https://www.ionq.com/news/ionq-announces-increased-full-year-2026-financial-outlook-following-skywater-acquisition

### UQPU implication
Lane G should track vertically integrated quantum-foundry strategies as a comparison point for in-house-vs-partner manufacturing economics.

## Evidence boundary
These are official company announcements/current service documentation. They are not independent proof of UQPU economic advantage. All workload-level claims remain subject to reproducible benchmarking.

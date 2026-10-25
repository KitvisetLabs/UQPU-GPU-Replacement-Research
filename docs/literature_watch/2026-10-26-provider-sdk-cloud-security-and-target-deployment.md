# Provider watch — 2026-10-26: SDK interoperability, cloud boundary and target deployment

**Accessed:** 2026-10-26  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Integration owners:** Lane A — compiler/runtime; Lane C — data movement; Lane D/G — device and manufacturing; Lane F — evidence and cost  
**Evidence class:** OFFICIAL PROVIDER ANNOUNCEMENTS  
**UQPU performance/economic evidence promotion:** none

## 1. IBM Qiskit SDK v2.6 — published 2026-10-22

Official source: https://www.ibm.com/quantum/blog/qiskit-2-6-release-summary

IBM describes v2.6 as a C-API-focused release adding a customizable pass-manager framework, multi-IR lowering, C-API QPY serialization and custom operations. QPY format v18 becomes the default; the release notes warn that v18 output may not load in older Qiskit versions unless an older format is requested. Python 3.10 is supported by v2.6, but the release states that v2.6 is the last Qiskit version supporting Python 3.10 and v2.7 requires Python 3.11 or newer.

**UQPU relevance:** this is a concrete Lane-A compatibility lead for provider-neutral lowering, serialization and independent SDK checks. It does not establish better circuit quality or hardware performance. The existing pinned Qiskit 2.5.2 checkpoint must remain reproducible; do not update its baseline merely because a newer SDK exists.

**Falsifiable follow-up — QISKIT-IR-002:** freeze source circuit, canonical circuit digest, target-independent logical operation list and toolchain. Test a QPY round trip under the pinned SDK and v2.6, test explicit legacy QPY version output, compare logical semantics and measurement mapping, and record payload size, lowering changes and failures. Pass only if the useful-output contract and circuit semantics remain identical; a smaller QPY payload alone is not a workload advantage.

## 2. Amazon Braket FedRAMP Class C scope — published 2026-10-16

Official source: https://aws.amazon.com/about-aws/whats-new/2026/10/braket-fedramp-class-c/

AWS says the Braket-operated API/SDK, job orchestration, compilation and S3 result-storage components are in the stated FedRAMP Class C boundary in the listed US regions. Quantum workloads execute on third-party quantum hardware providers outside that boundary.

**UQPU relevance:** this is a security/compliance boundary update, not a target capability, price or performance change. Provider-neutral records must continue to distinguish the cloud control plane from the actual QPU provider/target and its data, pricing and calibration provenance.

**Follow-up:** preserve provider, target, region and data-boundary metadata in the no-submit manifest. Do not infer that third-party hardware is inside the AWS authorization boundary or that compliance status implies a scientific advantage.

## 3. D-Wave Advantage2 deployment in Italy — announced 2026-10-15

Official source: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-delivers-italy-s-first-annealing-quantum-computer/

D-Wave reports that a 4,400+ qubit Advantage2 system arrived in Lombardy for installation and was planned to become accessible through Leap once operational. The announcement also describes a €10 million agreement and an allocation of system capacity; those are deployment/business facts, not a UQPU benchmark.

**UQPU relevance:** this is a target-discovery lead for Lane B and a manufacturing/deployment lead for Lane D/G. Arrival for installation is not equivalent to verified live target availability, target calibration, an accessible account, or accepted workload advantage.

**Follow-up:** before selecting the target, verify official Leap availability, region/access, current target identifier, topology/calibration snapshot, current pricing, supported QUBO semantics and solver/service boundaries. Start with simulator/dry-run and the same useful-output contract; do not submit a paid job without explicit consent and a bounded budget.

## 4. IonQ provider surveillance — current official newsroom

Official source: https://www.ionq.com/news

The newsroom lists additional October announcements, including a Cambridge Quantum Innovation Centre (2026-10-15), a quantum-memory-enhanced interconnect (2026-10-09) and progress to the final stage of DARPA's Quantum Benchmarking Initiative (2026-10-07). The Superion 256 manufacturing announcement is already covered by pending UQPU work and is not duplicated here.

These are provider-reported program and deployment announcements. They do not supply UQPU's exact target calibration, current price, same-contract accepted-output probability, or an independently reproduced workload result.

## Cross-provider conclusion and evidence boundaries

No adapter, pricing model, target identity or benchmark baseline is changed by this watch. The immediate implementation gate is SDK/version compatibility and provenance, not assuming a newer product is better.

- **Lane A:** freeze SDK and circuit semantics; compare Qiskit 2.5.2 with 2.6 in a no-submit interoperability test.
- **Lane B:** preserve exact provider/target/region/route and price provenance; no live provider was initialized.
- **Lane C:** record QPY payload bytes and host serialization/reconstruction cost; no end-to-end memory/transfer saving is claimed.
- **Lane D/G:** deployment and manufacturing claims remain vendor-reported until device/process/yield/availability data are independently verified.
- **Lane F:** do not infer performance, cost per accepted useful task or energy from qubit counts, compliance status, product announcements or pricing alone.
- **INV-029–035:** no data-center-to-phone compression, material substitution, bio-oil, fusion electricity, financing benefit or new physical law follows from these announcements.

No credentials were used and no QPU job was submitted. Simulator/dry-run remains the default. Any paid execution requires explicit user consent and a predeclared bounded budget.

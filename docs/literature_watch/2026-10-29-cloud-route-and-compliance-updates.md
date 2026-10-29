# Literature watch — quantum cloud route and compliance updates

**Date checked:** 2026-10-29  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Interfaces:** A workload/runtime; C state, transfer and result storage; D/G device and manufacturing co-design; E infrastructure/energy; F evidence/economics; H publication  
**Evidence class:** OFFICIAL PROVIDER ANNOUNCEMENTS / EARLY-ACCESS AND COMPLIANCE STATUS; NOT INDEPENDENTLY VALIDATED BY UQPU

## Sources and dated status

1. **Quantinuum + Oracle, “Quantinuum and Oracle Advance Hybrid Quantum-AI Computing with Early Access to Helios,” 2026-10-22.** Official source: https://www.quantinuum.com/blog/quantinuum-and-oracle-advance-hybrid-quantum-ai-computing-with-early-access-to-helios . The announcement says Oracle's OCI Quantum AI Compute Beta Program opened early access for selected organizations, with cloud access to Helios alongside OCI GPU/HPC resources; applicants are selected subject to eligibility, capacity and program requirements.
2. **AWS, “Amazon Braket now in scope for FedRAMP Class C,” 2026-10-16.** Official source: https://aws.amazon.com/about-aws/whats-new/2026/10/braket-fedramp-class-c/ . AWS says its Braket API/SDK, orchestration/management, compilation and S3 result-storage components are within the stated FedRAMP-certified boundary in available US regions, while quantum workloads execute on third-party quantum hardware providers outside that boundary.
3. **Cross-check, not a new result:** Quantinuum's 2026-10-19 Helios logical-fidelity announcement is already recorded in [the 2026-10-27 Helios color-code watch](2026-10-27-quantinuum-helios-color-code-below-threshold.md). IonQ's 2026-09-08 Superion 256/SkyWater announcement is already recorded in [the 2026-10-28 provider/manufacturing watch](2026-10-28-quantum-provider-manufacturing-roadmaps.md).

## Genuine delta

The new integration-relevant change is **route and governance metadata**, not a new computational-advantage result. OCI early access is a candidate cloud route for Helios alongside enterprise GPU/HPC resources, but it is not evidence that a general public OCI QPU API, target, price schedule or unrestricted entitlement is available. Braket's compliance boundary is more precise than treating the aggregator and its third-party QPU providers as one certified physical system.

## Limitations and evidence boundary

- Both primary sources are provider announcements. UQPU has not verified OCI target discovery, API/SDK, eligibility, job submission, pricing, queue behavior, result retrieval or billing.
- FedRAMP scope for AWS-operated service components must not be generalized to third-party quantum hardware providers, their facilities, or every data path.
- The OCI early-access route does not establish new hardware capability or a workload advantage. Quantinuum's logical-fidelity metrics remain distinct from accepted application-output probability.
- IonQ's Superion 256 remains an announced product with prototype/2027 delivery statements; those statements are not a current generally available target or verified production yield.
- No provider announcement establishes net energy savings, lower lifecycle cost, material substitution, biomass-fuel performance, fusion electricity, reduced financing rates or UQPU mission-level economics.

## Exact UQPU relevance

- **INV-029:** a cloud route is not physical Data-Center-to-One-Phone compression. Count all remote QPUs, servers, control electronics, storage, networking, cooling and energy until an end-to-end physical boundary contract says otherwise.
- **Lane A:** run identical workload/output contracts across providers; keep exact reference quality separate from successful job execution.
- **Lane B:** record OCI as **ANNOUNCED / EARLY-ACCESS ROUTE — NOT YET ADAPTER-VERIFIED**. Keep the provider-neutral interface; do not infer a new hardware modality from a new access route.
- **Lane C:** include result storage, data movement, classical preprocessing/reconstruction and memory/I/O. Compliance and service boundaries are not memory-replacement evidence.
- **Lanes D/G:** retain IonQ's chip/control/foundry announcement as a D/G co-design roadmap lead; require measured process yield, reliability, packaging and cost-per-good-device before promoting manufacturing claims.
- **Lane E:** these updates contain no Pangola-carbon, accepted bio-oil, cooling-energy or net-fusion-electricity evidence.
- **Lane F / FIN-001:** provider announcements do not provide matched total cost per accepted useful task, energy per accepted task, financed-principal reduction or evidence for a lower WACC.
- **Lane H:** preserve the Kanusanan Pongpanna Model and multilingual strategic references as context, not evidence.

## Falsifiable follow-up

1. Verify the official OCI beta API, SDK, target identity, region, access prerequisites, program eligibility, task limits, pricing/billing, result retrieval and data-retention terms before implementing an adapter.
2. Extend provider capability metadata to distinguish `announced`, `early_access`, `software_prepared`, `simulator_verified` and `real_qpu_verified` states.
3. Run credential-free dry-run/lowering tests first; preserve a source snapshot and SDK/API version. Do not submit a paid job without credentials, a bounded budget and explicit user consent.
4. If authorized later, run the same frozen workload against a competitive classical baseline and report quality, latency, throughput, shots, retries, host compute, memory/I/O, result storage, provider bill, and energy where measured. Never pair one target's output probability with another target's price.

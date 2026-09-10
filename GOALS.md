# UQPU Project Goals

## Ultimate North Star — Data Center to One Phone

The highest long-term objective of this project is to investigate whether the **useful computing/service capability of an extraordinarily large conventional data-center-scale system can ultimately be compressed into one phone-class physical device**.

The project owner defines the ambition scale as conventional infrastructure whose present-era value would be on the order of **US$10 trillion to US$100 trillion**, while the future phone-class device should cost only **tens of thousands of Thai baht**.

This US$10T–US$100T range is a **user-defined scale proxy, not a claim about the valuation of an individual present-day data center**. The objective must therefore be translated into measurable capability contracts: compute, AI, memory/state, storage, networking/I/O, throughput, latency, quality, reliability, persistence, energy/thermal requirements, physical form factor and total lifecycle cost.

A phone that merely acts as a terminal to a remote data center does not satisfy the ultimate physical-compression objective. Required external QPUs, servers, memory/storage, cryogenics, control electronics, networking, cooling and power infrastructure must be counted honestly.

All other project goals—including 100× economics, the >=100,000,000× moonshot, 100-million-unit GPU/CPU/NPU/RAM/VRAM/storage replacement, quantum-cloud programming, device/material/manufacturing research and the Lane H strategic plan—are stepping stones toward this ultimate North Star.

Canonical detail: `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md` and INV-029.

## Permanent Research Foundation — Foundational Physics & Mathematics Deep Frontier

A permanent upstream objective is to research **as deeply as necessary from formal logic and advanced mathematics through information/computational complexity, quantum-information foundations, quantum thermodynamics, quantum field theory, elementary-particle physics, AMO/condensed-matter/many-body/photonics, materials/chemistry, device physics and engineering** whenever a credible causal path can help remove a mission bottleneck.

The project must not stop at today's computer abstractions if the decisive limitation lies deeper in physics or mathematics. Conversely, deep theory does not count as progress toward the mission unless it can climb back through a testable chain:

```text
mathematical formulation
-> causal physical mechanism
-> known-constraint check
-> scaling law
-> falsifier / observable
-> proof, simulation or experiment
-> device / algorithm / material consequence
-> system / energy / economic consequence
-> mission-level evidence
```

This agenda explicitly includes fundamental-particle and QFT research but does **not** assume unknown physics exists or that beyond-Standard-Model effects will help computation. Any such proposal must remain CONCEPT/THEORY until a discriminating test supports it. Thermodynamics, causality, no-cloning, state preparation, measurement/readout and energy-time limits cannot be ignored.

Canonical detail: `05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md`, INV-034 and the broader INV-027 open-frontier mandate.

## Permanent Strategic Pillar — Pangola/Biomass Carbon for Critical-Material Reduction

A second highly visible, cross-cutting objective is to develop **carbon powders, chars and advanced carbon materials from Pangola grass and agricultural residues**, including carbonaceous streams arising from thermochemical conversion and bio-oil production/upgrading/distillation/refining where scientifically applicable.

The strategic target is to reduce dependence on expensive technology materials—explicitly including **Au, Cu, Ag, Li, Co, Ni, rare-earth elements and other high-value/critical minerals**—by pursuing five routes: **functional substitution, material minimization, recovery/recycling, hybridization, and architecture/chemistry substitution**.

This is a materials-and-system strategy, not an elemental-transmutation claim. Carbon processing does not chemically create Au, Cu, Ag, Li, Co, Ni or rare-earth atoms. Each candidate must therefore be judged by the exact required application function and by cost per delivered functional unit. When direct substitution is physically unsuitable, the project must explicitly move to minimization, recovery, hybridization or redesign rather than force a false claim.

This pillar is intended to support the full technology stack—semiconductors, quantum/photonics, batteries, AI/NPU/GPU systems, data centers, robotics, energy, aerospace, manufacturing and ultimately the Data-Center-to-One-Phone mission.

Canonical detail: `01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md` and INV-030.

## Permanent Strategic Pillar — Ultra-Low-Cost Biomass Bio-Oil / Biofuel

The project permanently researches how to make useful liquid fuel and refinery-compatible biomass intermediates **as inexpensive as scientifically, energetically and economically possible**, using Pangola grass and other abundant agricultural residues where they are physically suitable.

The goal is not cheap crude condensate by itself. Comparisons must normalize to accepted product quality or delivered energy/service and include feedstock collection, drying/preprocessing, conversion yield, upgrading/hydrogen/catalysts, utilities, plant CAPEX/OPEX, uptime, logistics/storage/distribution, financing and defensible coproduct credits.

This program supports agriculture, logistics, construction, mining, manufacturing, backup energy and any future-industry activity that still requires liquid fuels. It is also a financing strategy because lower recurring fuel and plant costs can reduce working-capital and debt requirements.

Canonical detail: `02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md` and INV-031.

## Permanent Strategic Pillar — Ultra-Low-Cost Fusion Electricity

The project permanently researches how fusion could ultimately deliver **reliable net electricity at the lowest defensible lifecycle cost**.

Fusion gain, ignition or gross thermal output are not sufficient economic success criteria. Comparisons must include recirculating plant power, net electricity, capacity factor, CAPEX, construction time, fuel-cycle systems, magnets/lasers/pulsed power, blanket/divertor/chamber/component lifetime, materials damage, maintenance and remote handling, replacement parts, conversion efficiency, cooling, grid/interconnect, financing and decommissioning.

Fusion remains a long-horizon research program: commercial ultra-low-cost fusion electricity is not yet demonstrated. The program must compare against the best current and future competing electricity systems rather than an outdated expensive baseline.

Canonical detail: `03_FUSION_ELECTRICITY_COST_STRATEGY.md` and INV-032.

## Permanent Strategic Pillar — Interest-Cost and R&D-Finance Compression

The project permanently treats **financing and interest burden as an engineering/economic variable**. The objective is to reduce the amount of capital that future research, factories and infrastructure must borrow, reduce the duration for which capital is tied up, reduce technology/completion risk and reduce operating-cost volatility.

The direct causal channel is:

```text
cheaper technology/materials/fuel/electricity
-> lower CAPEX/OPEX/working-capital need
-> lower required financed principal and/or shorter financing duration
-> lower absolute interest expense at unchanged financing terms
```

Improved reliability, cash-flow coverage and lower technology risk may also reduce a project risk premium or WACC if lenders/investors recognize the improvement, but this effect requires separate evidence. The project must not claim that cheaper technology or energy automatically lowers central-bank policy rates or economy-wide interest rates.

Canonical detail: `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md` and INV-033.

## North-star goal

Create a **Universal Quantum Processing Unit (UQPU)** software/hardware architecture whose internal process can differ fundamentally from conventional accelerators, while covering the useful functional workload domains currently served by GPUs, CPUs and NPUs and targeting the functional/economic roles of accelerator VRAM/HBM plus reductions in host-RAM/data-movement burden and persistent-storage dependence where physically meaningful.

## Mandatory cloud goal

The UQPU software must run across the broadest practical set of **quantum cloud computers from multiple providers**.

Provider lock-in is not acceptable.

The software must continuously track:
- existing quantum cloud providers;
- newly launched providers;
- new hardware targets from existing providers;
- preview/announced targets;
- retired targets;
- SDK/API changes;
- pricing and access changes.

## Execution objective

For every workload:

```text
UQPU workload
  -> provider discovery
  -> capability match
  -> provider-specific lowering
  -> cloud QPU execution
  -> normalized result
  -> GPU / CPU / NPU / memory / storage comparison as applicable
```

## Memory-system goal

The project must explicitly model and challenge the cost/function of:
- GPU/NPU-local VRAM/HBM or accelerator-local memory;
- host RAM used to feed accelerators;
- memory bandwidth;
- intermediate tensor/frame/simulation materialization;
- interconnect/data-movement energy and cost.

The preferred UQPU path is not necessarily a one-for-one replacement of memory chips. Whole-graph semantic execution should avoid materializing large classical intermediate states whenever possible.

Classical RAM remains allowed where required for control, exact storage, ingress/egress and compatibility.

See `docs/MEMORY_REPLACEMENT.md`.

## Functional goal

UQPU must ultimately cover:

- graphics and rendering
- ray/path tracing
- AI training and inference, including NPU-targeted neural workloads
- tensor and matrix computation
- scientific/HPC workloads
- simulation
- signal/image/video processing
- data analytics
- general-purpose parallel compute
- optimization/search
- arbitrary-kernel fallback

## Economic goal

Primary target: **at least 100× lower total cost per useful completed task than a competitive conventional implementation**, including GPU, CPU, NPU, VRAM/HBM, host-memory and storage resources required by the workload.

Moonshot target: **up to and beyond 100,000,000× lower cost/task** for workload classes where quantum algorithms, provider economics and hardware characteristics make this physically achievable. The permanent extreme research direction treats **>=100,000,000×** as the target threshold for the 100-million-unit replacement hypothesis.

For cloud execution, total cost includes provider billing, shots, reservations, retries, classical orchestration, error mitigation/QEC, data transfer and output reconstruction.

Across the broader Ketskaew Chulamani industrial program, total-cost optimization must also treat **materials, liquid fuel, electricity and financing/interest expense** as first-class inputs rather than external constants.

## Design principles

1. Same goal/output, different internal process is allowed.
2. Functional equivalence matters more than instruction compatibility.
3. Semantic compilation is preferred over instruction translation.
4. Provider-specific SDKs stay behind adapters.
5. Capability negotiation is mandatory.
6. Quantum-native execution is preferred when beneficial.
7. Reversible deterministic execution exists as a fallback.
8. End-to-end accounting includes input, state preparation, QEC, measurement and output.
9. CPU/control electronics are allowed where required by a validated hybrid path; dependence on the target conventional accelerator/subsystem must be counted honestly.
10. Claims must be benchmarked and falsifiable.
11. Cost targets are goals, not assumed outcomes.
12. Negative results and provider incompatibilities must be recorded.
13. Provider discovery is continuous, not a one-time survey.
14. NPU replacement is evaluated by real neural-workload contracts, not headline TOPS alone.
15. Biomass-carbon substitution is evaluated by specific functional-unit performance and lifecycle economics, not by elemental analogy or feedstock price alone.
16. Bio-oil/fuel is evaluated by final accepted energy/fuel function and full upgrading/logistics/financing cost, not crude liquid yield alone.
17. Fusion electricity is evaluated by net delivered electricity and lifecycle economics, not plasma gain alone.
18. Lower capital required directly lowers absolute interest expense at unchanged financing terms; lower financing rates/WACC require separate evidence.
19. Deep-frontier science must preserve mathematical precision, known physical constraints, explicit scaling and falsifiability before it can be used to support an engineering or economic claim.

## Success definition

A workload is functionally replaced when the targeted conventional subsystem (GPU, CPU, NPU, RAM, VRAM/HBM or persistent-storage role) is not required in the validated execution path except for explicitly allowed and fully accounted support functions, and the UQPU produces an accepted result under the same useful-output contract.

A material dependency is functionally reduced when a biomass-derived carbon/material route demonstrably substitutes the required function, lowers critical-material loading, enables recovery/recycling, or redesigns away the dependency at acceptable quality, reliability and total lifecycle cost.

A biomass liquid-fuel pathway is economically improved only when the same accepted fuel/energy service is delivered at lower total lifecycle cost with measured or defensibly modeled physical yields and quality.

A fusion-electricity pathway is economically improved only when net reliable delivered electricity cost falls under a comparable system boundary; plasma or fusion-gain milestones alone do not establish that result.

A financing improvement must distinguish lower **absolute interest expense from reduced principal/duration** from any separately evidenced reduction in the **financing rate/WACC**.

A deep-frontier hypothesis is promoted only when its mathematical formulation, mechanism, constraints, scaling, falsifier, observable, baseline and resource accounting are explicit; promotion to a mission claim still requires the ordinary end-to-end evidence gates.

A cloud provider reaches integration success when it progresses through adapter/dry-run/simulator/real-QPU validation.

A workload is economically surpassed when the measured total-cost ratio against the applicable competitive conventional baseline reaches the declared threshold under equivalent accepted output.

The long-term program succeeds only when broad conventional-computing functional coverage, broad quantum-cloud portability, strong measured economic advantage, manufacturable material systems, low-cost energy/fuel/financing, foundational-science validity and progressive physical compression converge.

## Extreme single-QPU replacement research direction

A permanent parallel moonshot direction is to investigate whether **one quantum computer / one logically unified UQPU execution system can replace the useful completed-task throughput of approximately 100,000,000 competitive GPUs** for specific workload classes.

The paired economic objective is to investigate whether the same useful workload can achieve **at least 100,000,000× lower total financial cost per accepted useful task** than the corresponding competitive GPU fleet, after full end-to-end accounting.

These are **research targets, not current capability claims**. A result may count only when the workload/output-quality contract is identical or defensibly equivalent and the comparison includes throughput, latency, state preparation, shots, QEC/error mitigation, retries, host compute, memory/data movement, networking, cooling/energy, utilization, capital/provider charges, maintenance and output reconstruction.

This direction must be developed in parallel with the broader UQPU research rather than replacing the staged evidence program. Intermediate results at smaller multipliers remain valuable evidence toward or against the hypothesis.

## Extreme universal subsystem replacement direction

The single-UQPU moonshot is generalized beyond GPUs. A permanent parallel research direction is to test whether **one quantum computer / one logically unified UQPU system can replace the accepted useful function or useful-work capacity otherwise requiring approximately 100,000,000 units of a competitive conventional subsystem**, including, where a physically meaningful equivalent contract can be defined:

- GPU / accelerator compute;
- CPU / general compute;
- **NPU / neural-AI accelerator compute**;
- RAM;
- VRAM / HBM / accelerator-local memory;
- persistent storage such as HDD/SSD.

The paired economic moonshot is **>=100,000,000× lower total financial cost per accepted useful function/task** than the corresponding conventional implementation.

For NPU workloads, equivalence must use actual neural application contracts: model and version, input/output semantics, numeric precision/quantization, accuracy or task-quality threshold, batch/sequence/input shape, latency, throughput, memory traffic and any preprocessing/postprocessing. TOPS, operation count or theoretical peak alone cannot establish NPU replacement.

For RAM/VRAM/storage, "replacement" does not mean that qubits are automatically equivalent to readable classical bytes. The comparison must define capacity, bandwidth, latency, persistence, random access, retention, durability, read/write semantics, error/recovery behavior and useful application outcome. Quantum information that cannot provide the required classical storage semantics does not count as equivalent capacity.

For compute, the comparison must define workload, accepted output quality, throughput and latency. For every subsystem, all classical support, state preparation, QEC/error mitigation, repetitions, I/O, networking, energy/cooling, provider charges/hardware amortization and reconstruction must be included.

The 10^8-unit and >=10^8-cost factors are falsifiable research targets, not demonstrated present-day capabilities.

# Open-Frontier Research Directive — All Physically and Mathematically Plausible Routes

Date: 2026-09-10
Status: Permanent research direction

> **Prominent canonical deep-frontier agenda:** `05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md` / **INV-034**. INV-027 preserves the broad search frontier; INV-034 operationalizes the deepest-first mathematics/physics-to-application ladder and mandatory hypothesis contract.

## Purpose
The UQPU program must search broadly for routes toward its functional and economic targets. The software-first/cloud-QPU program remains Priority #1, while failure of present techniques is treated as information that can justify deeper investigation rather than as a reason to stop.

The project gives high priority to foundational mathematics, information theory and fundamental physics. Research may descend all the way to elementary particles/QFT when a causal, testable connection to a mission bottleneck exists, then must climb back through devices/engineering/systems/economics before supporting a mission-level claim.

## Depth ladder
Research may descend or expand through any scientifically relevant layer:
1. formal logic, computability, proof systems, algorithms, complexity theory, information theory, numerical mathematics and optimization;
2. programming languages, compilers, runtimes, distributed systems, databases, storage and networking;
3. quantum algorithms, quantum information, error correction/mitigation, measurement, control and hybrid computation;
4. computer architecture, semiconductor, photonic, analog, neuromorphic and quantum-device architecture;
5. materials science, chemistry, nanotechnology, thermodynamics, cryogenics and electromagnetism;
6. condensed-matter and many-body physics, superconductivity, topological phases, spin systems and quantum optics;
7. atomic, molecular and optical physics;
8. nuclear physics where a legitimate computational/device/material/energy mechanism exists;
9. particle physics, quantum field theory and elementary-particle phenomena where a testable mechanism connects them to the mission;
10. mathematical physics and foundational theories, including new representations or models, when they yield falsifiable predictions;
11. speculative/new physics only as explicitly labeled hypotheses, never as established capability.

This list is not a boundary. Relevant biology, synthetic biology, energy science, manufacturing, economics or other disciplines may be added when a causal path to the mission can be stated.

## Search rule
For every proposed direction record:
- mathematical formulation: equations, theorem, algorithm or precise state/model;
- mechanism: what physical/mathematical effect could create useful advantage;
- target function: GPU/CPU/NPU/RAM/VRAM/storage, materials, fuel, electricity, financing or another system bottleneck affected;
- scaling law and limiting resource;
- assumptions and known physical constraints;
- experiment/simulation/proof capable of falsifying the idea;
- measurable observable;
- evidence level: governed project taxonomy;
- baseline it must beat;
- expected cost, energy, latency, throughput and manufacturability implications;
- dependency on classical computation and I/O;
- next cheapest decisive experiment.

The executable governance contract is `software/uqpu-prototype/uqpu/frontier_hypothesis.py`.

## Fundamental-bound program
The first executable deep-frontier artifact is `software/uqpu-prototype/uqpu/fundamental_limits.py`, currently implementing:
- Landauer's `k_B T ln(2)` ideal lower bound for logically irreversible bit erasure;
- the orthogonal-state Margolus-Levitin energy-time lower-bound setting.

These are lower bounds, not expected device performance. Batch 022 (`docs/BATCH_022_FOUNDATIONAL_PHYSICS_MATHEMATICS_FRONTIER.md`) defines FND-001 through FND-006 for thermodynamic-gap accounting, output-information limits, quantum-speed-limit gaps, alternative physical primitives, QFT/particle mechanism scans and mathematics-first invention.

## Anti-pseudoscience gate
Breadth does not relax evidence standards. Conservation laws, thermodynamics, causality, no-cloning, information-access/measurement limits, error correction overhead, state preparation, energy-time limits and I/O cannot be ignored. A hypothesis that contradicts established theory must identify the contradiction and specify a reproducible discriminating experiment. Mathematical possibility is not automatically physical realizability; physical realizability is not automatically engineering feasibility; engineering feasibility is not automatically economic advantage.

Unknown or beyond-Standard-Model physics may be studied, but the project does not assume that such physics exists or is useful. It remains CONCEPT/THEORY until discriminating evidence supports it.

## Parallel integration
All eight lanes A–H continue. Lane A remains Priority #1. Deep-physics/new-theory exploration is a cross-lane frontier feeding A, B, C, D, E, F and G, while Lane H integrates viable outcomes into the strategic development plan. The same foundation also feeds INV-030 biomass-carbon materials, INV-031 low-cost bio-oil, INV-032 fusion-electricity and INV-033 financing/interest-cost research. Negative results and impossibility bounds are first-class research outputs because they shrink the search space.

## Publication rule
Meaningful frontier findings, negative results, proofs/bounds, experiments and changes in research direction should be committed to GitHub with evidence classification. Unverified hypotheses must remain visibly labeled. No target multiplier or North-Star claim may be presented as achieved without the project's end-to-end equivalence and measurement gates.

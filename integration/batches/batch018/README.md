# Batch 018 — Six-Qubit Target-Snapshot Integration

Date: 2026-09-10  
Primary integration contract: ER6 MaxCut/QUBO, contract `8efaa94bb3306d25`  
Evidence level: `CALIBRATION_SNAPSHOT_SIMULATION`

## Result

The target-aware pipeline was generalized from the 3-qubit triangle fixture to named fixtures and executed on the 6-qubit `er6` contract using Qiskit Aer built from the saved IBM `FakeKingston` system snapshot. This is not a live IBM backend and no QPU job or provider charge occurred.

ER6 measured-on-CI simulation result:

- exact optimum: -7.0;
- ideal p=1 QAOA optimum probability: 0.25391734004004546;
- snapshot-noisy optimum probability: 956 / 4096 = 0.2333984375;
- retention versus ideal probability: 0.9191906211020902;
- expected independent shots to one optimum sample: 4.2845188284518825;
- shots for >=99% probability of at least one optimum sample under the independent-shot model: 18;
- logical depth: 24; routed depth: 76;
- logical CX count: 18; routed CZ count: 26;
- active physical qubits: 138, 148, 149, 150, 151, 152;
- active CZ mean calibration error in the saved snapshot: 0.0018280599216830488;
- active measurement mean calibration error: 0.006306966145833333.

Compared with the 3-qubit triangle, the 6-qubit fixture requires about 4.20x more expected shots per optimum sample under these two snapshot simulations. This ratio is descriptive for these fixtures only; it is not an asymptotic scaling law.

## Eight-lane integration

A -> B: one stable optimization contract is compiled and routed to a target-aware Qiskit path.  
B -> C: finite-shot success probability becomes an explicit output/readout and reconstruction burden.  
C -> D/G: the routed operation footprint identifies the physical-qubit/control/calibration surface actually used.  
D <-> G: active gate error/duration and routing are measurable device/tool feedback inputs rather than whole-chip medians.  
D/G -> E: energy/cooling/facility cost per accepted result remains missing and must be measured or sourced before economic claims.  
A/B/C/D/E/G -> F: all overhead must converge into cost per accepted useful task against the same competitive baseline.  
F -> H: capital should advance from simulation to paid execution only when the next experiment reduces a clearly quantified uncertainty.  
H -> A-G: strategic funding and sequencing feed back into the cheapest decisive technical experiment.

## Pairwise integration review

All 28 lane pairs were reviewed. Direct active interfaces in this batch are A-B, A-C, A-F, B-C, B-D, B-F, C-D, C-F, D-F, D-G, E-F, E-G, F-G and F-H. Other pairs remain `INDIRECT/NEXT` rather than being falsely labeled active. Their next useful connection is through the shared accepted-output and total-cost contract.

## Research-source direction

Two current routes are prioritized for the next controlled algorithm comparison while preserving the exact ER6 contract and snapshot pipeline:

1. IBM's current warm-start QAOA workflow uses a continuous relaxation to initialize the state and a custom mixer, specifically to improve practical convergence/quality versus random initialization: https://quantum.cloud.ibm.com/docs/en/tutorials/warm-start-qaoa
2. IBM Research's QCE 2025 E-QAOA work reports equal or higher accuracy and reduced variance than COBYLA-based QAOA on 3-regular MaxCut instances from 4 to 26 nodes, especially with CVaR fitness, and demonstrates distributed two-QPU experiments: https://research.ibm.com/publications/evolving-a-multi-population-evolutionary-qaoa-on-distributed-qpus

These are external research inputs, not evidence that UQPU already has advantage. Batch 019 should compare at least one improved initialization/optimizer strategy against the current p=1 ER6 baseline under an equal evaluation/shot budget.

## Evidence boundary

`FakeKingston` is a saved backend snapshot. Aer noise simulation is approximate. No live calibration, queue time, billable QPU time, mitigation/QEC cost, network cost, facility energy, GPU baseline or real-QPU output was measured. Therefore no quantum advantage, >=100x result or INV-025/026 100M-unit result is demonstrated.

# Quantum Oracle Sketching Research Watch — 2026-09-10

**Owner:** Lane H with A/C/F review  
**Status:** HIGH_VALUE_ADVERSARIAL_REVIEW_REQUIRED  
**Project evidence class:** EXTERNAL_PREPRINT + EXTERNAL_CODE + EXTERNAL_CRITIQUE  
**REAL_QPU project evidence:** No  
**UQPU advantage claim:** Not promoted

## Primary result under review

Zhao, Zlokapa, Neven, Babbush, Preskill, McClean and Huang, **"Exponential quantum advantage in processing massive classical data"**, arXiv:2604.07639 (submitted 8 April 2026), introduces Quantum Oracle Sketching (QOS).

Primary sources:
- https://arxiv.org/abs/2604.07639
- https://research.google/pubs/exponential-quantum-advantage-in-processing-massive-classical-data/
- https://github.com/haimengzhao/quantum-oracle-sketching

The paper states that a polylogarithmic-size quantum computer can perform selected large-scale classification and dimension-reduction tasks by consuming random classical samples on the fly. The reported real-data demonstrations show four-to-six orders of magnitude machine-size reduction with fewer than 60 logical qubits.

The official repository provides JAX implementations, QSVT utilities, synthetic benchmarks and real-dataset experiments for IMDb, 20 Newsgroups, PBMC68k and Dorothea.

## Why UQPU should study it

QOS attacks a central UQPU bottleneck from a different direction: instead of emulating GPU/NPU matrix instructions, it attempts to avoid storing/materializing the full classical data object needed by a learning task.

This could matter to Lane A/C because UQPU Functional Replacement allows semantic reformulation. A valid compact-data-access primitive could potentially reduce RAM/VRAM/data-movement pressure for selected workload contracts.

However the following quantities are not interchangeable:

`machine-size advantage != runtime advantage != energy advantage != cost advantage != GPU/NPU replacement ratio`.

A logical-qubit count also cannot be used as a physical phone-class footprint without fault-tolerance, control, readout, cooling, host memory and classical processing being counted.

## Adversarial evidence discovered

An independent public research repository by Carmelo Vellón Gascón publishes a version-specific mathematical audit of `arXiv:2604.07639v1`:

- https://github.com/gatephys/quantum-oracle-sketching
- version-specific archival material is linked there through Zenodo.

The audit claims an explicit finite counterexample to the sufficient threshold printed in Theorem D.16 / Eq. D.99 of the source v1 and also discusses interface/composition obligations. Importantly, the audit itself states that it does **not** claim QOS is impossible and does not challenge every result or the entire classical lower-bound program.

The UQPU project does not treat either the source preprint's strongest interpretation or the independent audit as final adjudication merely because it is published. The correct action is reproduction and theorem/interface checking.

## Required UQPU review contract

Before QOS can influence a UQPU architecture or economic claim, freeze:

1. exact source-paper version and theorem statement;
2. dataset/task and accepted-output contract;
3. classical machine-size model and strongest admissible classical comparator;
4. sample-access assumptions and independence/correlation model;
5. oracle construction and repeated-use/composition assumptions;
6. QSVT/block-encoding precision requirements;
7. logical qubits, logical depth, repetitions and error budget;
8. fault-tolerance/physical-qubit resource estimate where required;
9. classical preprocessing, host memory, data ingress and output reconstruction;
10. wall time, energy and total cost per accepted useful result.

## First reproduction target

Start with the smallest Boolean phase-oracle construction or another minimal official-code fixture that can be reproduced deterministically in simulation. Record source commit, seed, dimensions, sample count, oracle approximation error and all classical memory used.

Then separately reproduce the specific mathematical condition disputed by the independent audit. If the counterexample reproduces, label the affected v1 theorem condition `DISPUTED/FAILED_AS_PRINTED` only for that exact version/statement; do not generalize the failure to QOS as a whole.

If it does not reproduce, publish the discrepancy, implementation and assumptions rather than silently selecting the preferred conclusion.

## Promotion rule

QOS remains `HIGH_VALUE_ADVERSARIAL_REVIEW_REQUIRED` until the project has reproducible internal evidence. Even a successful simulator reproduction does not establish real-QPU, physical-memory, energy, cost or NPU/GPU advantage.

No >=100x, >=100,000,000x or Data-Center-to-One-Phone conclusion follows from this literature watch.

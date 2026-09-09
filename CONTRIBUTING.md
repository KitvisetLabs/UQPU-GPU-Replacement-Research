# Contributing to UQPU

Thank you for helping develop the **Universal Quantum Processing Unit (UQPU)** research program.

UQPU is an open research effort led by **Kanutsanan Pongpanna**, with **OpenAI GPT-5.6 Sol** as an AI research collaborator. The project investigates whether a quantum-first processor can eventually cover the full functional workload domain of GPUs while using fundamentally different internal computation.

## Everyone is welcome to contribute

You do not need direct write access to participate.

Standard contribution workflow:

1. Fork this repository.
2. Create a branch for your research, experiment, documentation, benchmark, or implementation.
3. Make your changes with evidence and reproducible assumptions.
4. Open a Pull Request.
5. Explain what problem is being addressed, methodology, assumptions, results, limitations, and how to reproduce the work.
6. Maintainers and community members can review the proposal before it is merged.

## High-priority contribution areas

- quantum algorithms for GPU workload replacement
- semantic compiler and mathematical IR
- reversible deterministic fallback
- quantum AI training/inference
- quantum rendering, ray tracing and path tracing
- scientific/HPC algorithms
- signal, image and video processing
- quantum memory and classical/quantum I/O
- QEC-aware architecture
- resource estimation
- cost modeling
- benchmark design
- hardware architecture
- photonic, analog and continuous-variable approaches
- GPU baseline measurements
- theoretical impossibility/boundary results

Negative results are valuable. A rigorous demonstration that a proposed mapping cannot beat a GPU is a useful research contribution.

## Core research constraints

A proposed UQPU path should ultimately aim for:

- no GPU dependency in the validated execution path;
- application-level functional equivalence;
- end-to-end accounting of state preparation, execution, QEC, measurement and output;
- transparent assumptions;
- reproducible benchmarks;
- honest classification of unresolved or non-advantageous workloads.

## Economic objective

The minimum economic-supremacy research target is **100× lower total cost per useful completed task** than a competitive GPU baseline.

The project also investigates a workload-specific **100,000,000× moonshot target** where quantum algorithms and hardware economics could theoretically permit it.

These are research targets, not guaranteed outcomes.

See `docs/COST_SUPREMACY.md`.

## Pull Request expectations

A strong PR should include:

- problem statement
- workload category
- proposed method
- mathematical formulation
- quantum/classical assumptions
- input/state-preparation model
- output/measurement model
- error/QEC assumptions where relevant
- resource estimate
- comparison baseline
- reproducibility instructions
- limitations
- references

## Result labels

Use the project's result vocabulary:

- `FUNCTIONALLY_SUPPORTED`
- `COMPETITIVELY_SUPPORTED`
- `QUANTUM_ADVANTAGE_CANDIDATE`
- `NO_ADVANTAGE_FOUND`
- `UNRESOLVED`

## Research integrity

Do not present projected quantum advantage as experimentally demonstrated advantage.

Clearly distinguish:

- theorem
- simulation
- resource estimate
- hardware experiment
- hypothesis
- speculation

Do not hide state-preparation, QEC, measurement, output reconstruction, energy, cooling or hardware amortization costs.

## Getting started

Read:

1. `README.md`
2. `GOALS.md`
3. `PROCESS.md`
4. `docs/PAPER.md`
5. `docs/GPU_FUNCTIONAL_COVERAGE.md`
6. `docs/COST_SUPREMACY.md`
7. `ROADMAP.md`

Then choose a research problem and open an Issue or Pull Request.

Welcome to the UQPU open research community.

# Literature watch — root-sparsity scaling for Hamiltonian simulation, ODEs and linear systems

**Date checked:** 2026-10-29  
**Primary owner:** Lane A — quantum programming, workloads and algorithm/resource contracts  
**Interfaces:** B provider-neutral execution; C state, memory and data movement; F benchmark/evidence/economics; H publication  
**Evidence class:** OFFICIAL ARXIV PREPRINT / MATHEMATICAL QUERY-COMPLEXITY CLAIM / NOT REPRODUCED BY UQPU  
**Stable IDs:** LIT-2026-10-02-ROOT-SPARSITY; RG-A-ROOT-SPARSITY-REPRO-001

## Source and dated status

Dominic W. Berry, Abhishek Rawat, Sophia Simon and Guang Hao Low, “Root-sparsity scaling for Hamiltonian simulation, differential equations and linear-system solvers,” official arXiv preprint submitted 2026-10-02: https://arxiv.org/abs/2610.02939.

## Genuine novelty

For an (s)-sparse Hermitian matrix with row/column Euclidean norms bounded by η, and τ = η|t|, the authors give a sparse-oracle query expression for Hamiltonian evolution of the form

`O(√s τ + √(s τ log(1/ε)) + log(1/ε))`.

The paper also gives a nearly matching joint lower bound, extends the method to specified dissipative linear ODEs and linear systems, and describes gate-efficient implementations under additional entry-decoding, arithmetic and source-preparation assumptions. This makes sparsity, evolution time, precision and access model explicit in one analysis rather than hiding them in a single headline multiplier.

## Limitations and evidence boundary

- This is a mathematical query-complexity result in specified sparse-access models, not an empirical runtime or physical speed/energy measurement.
- The expression is asymptotic; hidden constants and implementation overhead are not a measured gate count.
- Time-dependent claims require coherent time-indexed sparse access and certified discretisation; gate-efficient implementations require efficient entry decoding, reversible arithmetic and source preparation.
- Oracle construction, state preparation, compilation, memory, output reconstruction, retries and classical host work can dominate a practical workload.
- No UQPU theorem reproduction, real-QPU result, new physical law or mission-level advantage is claimed.

## Exact UQPU relevance

**Lane A / FND-002 and FND-004:** treat the result as a candidate complexity contract only when the workload can honestly supply the required sparse oracle and norm bounds. Keep it distinct from the existing coefficient-tail proxy for composite qDRIFT; the access models and formulas are not interchangeable.

**Lane B:** preserve provider-neutral lowering; no SDK or hardware target was run.

**Lane C:** account for sparse-entry encoding, oracle/data access, input-state preparation, output information, host/device memory and transfers. Query count is not readable memory capacity.

**Lanes D/G:** only after a target-specific circuit and physical implementation are defined can query scaling be mapped to gates, routing, fabrication, yield or packaging.

**Lane F:** a cost comparison needs a matched accepted-output predicate, target-specific price, full host/device accounting and measured resource use. This paper alone cannot support an economic advantage.

**Lanes E/H:** no direct bio-oil, Pangola-carbon, fusion-electricity or financing-rate evidence follows. Preserve the Kanusanan Pongpanna Model and six-language strategic references.

## Proposed falsifiable follow-up

1. Freeze a small, explicitly sparse Hermitian matrix family and publish its matrix-entry oracle plus row/column norm certificates.
2. Compare exact matrix-exponential references with at least one sparse-access algorithm over held-out sparsity profiles, times and target errors.
3. Record oracle calls separately from state preparation, synthesis, host work, memory/I/O, reconstruction and verification.
4. Search for counterexamples to the claimed scaling only inside the stated assumptions; report failed or infeasible cases.
5. Require independent reproduction before promoting beyond MODEL_ONLY/SIMULATION.

The immediate code addition is only an asymptotic expression evaluator with strict input checks. It does not prove the theorem or instantiate a valid oracle.

# Research gap — RG-QROM-SPARSE-001: sparse coherent data-access cost

**Opened:** 2026-10-27  
**Primary owner:** Lane C — memory/state/data movement, with Lane A compiler ownership and Lane F evidence integration  
**Status:** OPEN — external theorem identified; no UQPU workload has yet been mapped to the theorem's assumptions.  
**Related:** INV-011/025/026/027, INV-029, INV-034/035, FND-002, EQN-001–006.

## Objective

Determine when sparse quantum read-only-memory, state preparation or block-encoding methods reduce the end-to-end cost of a declared workload after including the address promise, table storage/update, classical preprocessing, circuit resources, host compute, data movement and output requirements.

## Current evidence

Li et al., arXiv:2607.28260v2 (revised 2026-10-01), prove asymptotically tight T-count bounds for exact sparse QROM in a fixed Clifford+T circuit model and derive matching bounds for sparse state preparation and sparse block encoding. Their lower bounds cover the paper's adaptive Clifford+T model with mid-circuit measurements and classically controlled operations.

This is external mathematical evidence. The theorem is not an implementation result, physical memory measurement, wall-clock prediction or cost-per-task measurement. It does not establish a universal memory-replacement result.

## Blocking unknowns

- No current UQPU workload has a frozen n/m/s table manifest with verified sparse-address semantics.
- No matched dense-versus-sparse QROM implementation comparison is recorded in this gap.
- T-count alone omits depth, ancillas, routing, magic-state production, preprocessing, classical storage, data movement, energy and provider billing.
- A cheaper promised-address implementation is invalid if the application can query addresses outside the declared support.
- The project's FND-002 output-information bound and FND-001 thermodynamic-gap accounting remain separate; this result does not replace them.

## Unlock criteria

1. Freeze the table source/hash, address width n, data width m, support size s, approximation error, address-promise semantics and output contract.
2. Reproduce small exact instances against a classical oracle and compare dense/direct and sparse-QROM methods on held-out sparsity patterns.
3. Record T-count, depth, ancillas, preprocessing, storage, memory, transfer, output reconstruction and uncertainty.
4. Integrate the result into a workload-level cost model with a clear MODEL_ONLY or SIMULATION_ONLY label until validated end-to-end measurements exist.
5. Retain a no-promise fallback and fail closed when the input contract does not guarantee sparse support.

## Sync debt

This dated gap is intentionally not appended to the large RESEARCH_GAPS.md from a partial snapshot. Preserve it until safe full-history reconciliation can update the aggregate backlog without truncation.

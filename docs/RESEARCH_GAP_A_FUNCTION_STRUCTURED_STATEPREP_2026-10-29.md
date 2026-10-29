# Research gap RG-A-FUNCTION-STATEPREP-001 — function-structured amplitude preparation

**Opened:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** Lane C state/data movement; Lane F evidence and cost; Lane B provider portability; Lanes D/G device/manufacturing; Lane H publication  
**Status:** OPEN / LITERATURE-ONLY / INDEPENDENT REPRODUCTION REQUIRED  
**Source:** Guseynov and Liu, *Physical Review A* 113, 012604 (2026), DOI 10.1103/plc3-2jyx.  
**Detailed watch:** docs/literature_watch/2026-10-29-piecewise-function-state-preparation.md

## Objective

Determine which UQPU workloads have amplitudes that can be represented by the paper's polynomial or piecewise-polynomial model, and whether its explicit circuit provides a reproducible end-to-end benefit after coefficient generation, approximation error, state preparation, output reconstruction and classical alternatives are counted.

## Current evidence

The publisher abstract reports O(n log n) scaling in qubit count, linear scaling with polynomial degree, examples up to degree 10^4 and linear scaling with the number of piecewise-polynomial parts. The method requires its stated polynomial parity/boundedness conditions and efficient approximation of the target function. UQPU has not independently reproduced the circuits or resource tables.

This is a distinct input model from sparse-state preparation and sparse-QROM. Do not combine their asymptotic expressions or treat function-structured state preparation as a solution for arbitrary state vectors.

## Blockers and acceptance gate

- Pin the exact source version and circuit/resource tables.
- Freeze target functions, coefficient representation, degree, piece count, localization and approximation tolerance.
- Independently compare small cases with a classical state-vector reference.
- Test held-out function families and negative controls outside the efficient-approximation regime.
- Record fidelity/error, gate metrics, depth, ancillas, preprocessing, coefficient bytes, data transfer, measurement/reconstruction and total cost per accepted useful task.
- Compare with the best function-aware, sparse-state or classical method under matched useful-output semantics.

## Nonclaims

No arbitrary-state preparation result, lower-bound bypass, readable-memory equivalence, real-QPU advantage, energy/cost reduction, new physical law or mission-level UQPU result is established.

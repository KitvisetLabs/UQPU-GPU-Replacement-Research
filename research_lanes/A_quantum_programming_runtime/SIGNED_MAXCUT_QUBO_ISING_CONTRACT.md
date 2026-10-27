# Lane A contract — signed Max-Cut objective lowering

**Owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** B provider lowering; C output/state/data movement; F reference and economic accounting  
**Evidence class:** SOFTWARE_CONTRACT_ONLY  
**Date:** 2026-10-28

## Frozen semantic contract

For a simple undirected weighted graph with vertices numbered 0 through n-1 and real signed edge weights w_uv, the maximization objective is

C(x) = sum over edges (u,v) of w_uv (x_u XOR x_v), with each x_v in {0,1}.

A negative weight remains negative: cutting that edge subtracts its magnitude from the objective. The compiler must not silently replace signed weights with positive preferences unless it also preserves the exact additive constant and accepted objective semantics.

With binary variables, the equivalent QUBO is

C(x) = sum_v a_v x_v + sum_edges b_uv x_u x_v,
a_v = sum of incident edge weights,
b_uv = -2 w_uv.

With Ising spins s_v = 1 - 2 x_v, the equivalent score is

C(s) = 0.5 sum_edges w_uv - 0.5 sum_edges w_uv s_u s_v.

The constant term is part of the objective contract even when an optimizer can ignore it for argmax selection. Reports of objective values, gaps, certificates and accepted-task quality must use one consistent convention.

## Implemented gate

The pure-Python lowering in software/uqpu-prototype/uqpu/signed_maxcut_objective.py normalizes undirected edge order, rejects duplicate/self-loop/out-of-range edges and non-finite or boolean weights, and exposes direct, QUBO and Ising scoring under one contract.

The unit tests exhaustively compare all bit strings for four fixtures and all 27 signed-weight patterns in a triangle. They require exact preservation of objective values and the complete set of maximizers within a declared floating-point tolerance. They also check canonical edge order and fail-closed input validation.

## Evidence boundary and next gate

This is an algebraic/classical reference only. It is not a QAOA implementation, circuit synthesis, SDK validation, simulator result, provider execution, cost estimate or quantum-advantage claim. The next gate is to bind this exact objective hash to a provider-neutral lowering, independently reconstruct the Hamiltonian/sign convention in at least one SDK, and compare accepted bitstring quality against an exhaustive reference on tiny instances before target-aware simulation.

Any later performance comparison must freeze the graph/weight hash, objective convention, acceptance threshold, shot/optimizer budget, target, calibration and price provenance. Count state preparation, decoding/reconstruction, host compute, memory/I/O, retries, billable usage, energy where measurable and total cost per accepted useful task. Paid QPU execution remains disabled absent explicit user consent, credentials and a bounded budget.

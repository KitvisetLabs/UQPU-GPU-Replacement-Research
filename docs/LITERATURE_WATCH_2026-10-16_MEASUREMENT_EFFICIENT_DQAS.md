# Literature Watch — Measurement-Efficient Differentiable Quantum Architecture Search

**Accessed:** 2026-10-16  
**Source:** Theißinger, Gerlach and Bauckhage, [arXiv:2610.10351](https://arxiv.org/abs/2610.10351), submitted 2026-10-07  
**Evidence class:** `THIRD_PARTY_PREPRINT / CONFERENCE_ACCEPTED`  
**Project promotion:** none; this is not UQPU execution evidence.

## Material delta

The paper derives a measurement-reduction method for differentiable quantum architecture search on combinatorial optimization and reports about 39–41% fewer requested gradient measurements on 3-SAT and MaxCut with negligible classical post-processing overhead. The result is relevant to Lane A/F because it preserves the optimization objective while reducing one resource component.

## Evidence limits

The reported percentage is not imported as a UQPU speed, energy or cost result. Requested gradient measurements are only one part of total accepted-task cost. Circuit preparation, compilation, queueing, shots actually executed, retries, readout, reconstruction, host optimization, data movement, energy and billing remain workload/provider dependent. The paper does not make Cycle 008's dense QSVT fixture scalable and does not supply provider-matched economics for it.

## Concrete decision

Future architecture-search candidates must record `requested_gradient_measurements`, `executed_shots`, `objective_identity`, `accepted_output_quality`, `host_postprocessing`, `provider_bill` and total cost/useful accepted task separately. A measurement-saving claim passes only under an identical objective and quality threshold, and cannot be multiplied by unrelated provider pricing or success probability.

## Falsifiable follow-up

Freeze one MaxCut architecture-search fixture and compare the published estimator with the existing method under identical seeds, candidate space, optimizer budget and quality threshold. Reject the route if requested-measurement savings disappear in executed shots or if total cost per accepted solution fails to improve. Until reproduced, label the result `LITERATURE_ONLY`.

## Official SDK check

IBM Quantum documentation for Qiskit 2.5.2 confirms that `UnitaryGate` accepts a unitary matrix and that unitary synthesis can target declared basis gates. It also distinguishes loose basis-gate synthesis from a real backend `Target`; the latter carries supported operations and target constraints. Cycle 008 therefore records its `rz/sx/x/cx` decomposition as generic SDK synthesis, not provider-target transpilation.

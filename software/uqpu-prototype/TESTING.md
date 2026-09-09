# Testing and Verification

## Development loop

```text
design -> implement -> unit test -> inspect result -> refine model
       -> regression test -> commit -> CI -> next iteration
```

## Verification history

### v0.2
- 9 local tests passed.
- CLI smoke test passed.
- Added MODEL_ONLY evidence labeling.

### v0.3
New verification suite adds 11 tests covering:

- quantum hardware-profile validation
- rejection of physical error rates above the configured QEC threshold
- GPU hardware-profile economics
- surface-code distance parity and lower bound
- monotonic code-distance behavior as error targets tighten
- total physical-qubit accounting
- GPU cost increasing with runtime
- sensitivity sweep behavior
- 100× target calculation
- 100,000,000× moonshot target calculation
- target-ladder ordering

Local v0.3 module result:

```text
Ran 11 tests
OK
```

The repository now contains 20 unit tests total (9 from v0.2 plus 11 introduced in v0.3). GitHub Actions remains the integration-level verifier across Python 3.10, 3.11 and 3.12.

## Scientific verification rule

Passing software tests demonstrates software consistency only. It does **not** validate the physical assumptions of the models.

Verification maturity ladder:

1. unit tests
2. property/invariant tests
3. integration/CI
4. benchmark reproducibility
5. literature-calibrated resource models
6. simulator cross-checks
7. QPU-provider experiments
8. measured GPU baselines
9. end-to-end economic validation


## Batch 012 (2026-09-09)
Current local suite: **142 tests, 141 passed, one optional OR-Tools availability test skipped**. Ten new tests independently verify QUBO/Ising energy semantics, two-layer QAOA state evolution, global phase, normalization, sampling, provider inspection and allocation limits. The historical counts above describe earlier releases.

Reproduce the experiment with `PYTHONPATH=. python examples/run_qaoa_verification.py --output /tmp/qaoa-verification.json`. This runs ideal CPU simulation, not a QPU benchmark.


## Batch 013 (2026-09-09)
SDK environment: **145 tests, 144 passed, one OR-Tools skip**. Core environment: **145 tests, 141 passed, four optional skips**. Three new SDK tests cover reordered measurement, rejection of unsupported measurement patterns and bounded state allocation. The dedicated CI job parses the committed Batch 012 payloads, compares independent probabilities and tests synthetic routing. See `verification-optional-requirements.txt` and `examples/run_qiskit_crosscheck.py`.

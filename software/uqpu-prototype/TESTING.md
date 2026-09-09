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

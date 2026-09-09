# Testing and Verification

## Development loop

The UQPU prototype follows:

```text
design -> implement -> unit test -> inspect result -> refine model
       -> regression test -> commit -> CI -> next iteration
```

## Local verification completed for v0.2

Environment used during development: Python 3.x standard library only.

Command:

```bash
python -m unittest discover -s tests -v
```

Result:

```text
Ran 9 tests
OK
```

Verified areas:

- IR validation
- invalid I/O rejection
- exact-contract fallback behavior
- quantum-native candidate discovery
- positive cost accounting
- cost-advantage calculation
- cost-tier boundaries
- MODEL_ONLY evidence labeling
- JSON workload parsing

CLI smoke test:

```bash
python -m uqpu.cli compile examples/search_workload.json
```

Expected behavior:

- selects a contract-compatible backend
- emits a resource/cost estimate
- marks evidence as MODEL_ONLY
- exposes confidence
- does not claim hardware-demonstrated advantage

## Continuous integration

GitHub Actions runs tests on Python 3.10, 3.11 and 3.12 whenever prototype code changes or a Pull Request modifies it.

## Scientific verification rule

Passing software tests only demonstrates **software consistency**. It does not validate the physical assumptions in resource models.

Future verification layers:

1. unit tests
2. property/invariant tests
3. benchmark reproducibility
4. literature-calibrated resource models
5. simulator cross-checks
6. QPU-provider experiments
7. GPU baseline measurements
8. end-to-end economic validation

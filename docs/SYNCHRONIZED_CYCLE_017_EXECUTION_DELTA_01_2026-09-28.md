# Synchronized Cycle 017 — Execution Delta 01

| Field | Value |
|---|---|
| Date | 2026-09-28 |
| Branch | `research/cycle-017-delta-01-2026-09-28` |
| Base | Verified Cycle 016 closeout `4824f7f034411dbbf9eeca6b41590f902ac6fca6` |
| Code/evidence SHA | `f524ba90c8ab30e752408d6ed227189eb9d2e4fb` |
| State | Cycle 017 closed; exact-SHA GitHub Actions passed 8/8; external gates remain open |

The active synchronous process is [`docs/PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md`](PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md). Cycle 017 began from Cycle 016 closeout on its own research branch. The local executable acceptance artifact is [`benchmarks/results/cycle017-delta01-executable-acceptance.json`](../benchmarks/results/cycle017-delta01-executable-acceptance.json), SHA-256 `9f1010212a9fdc9aebd9afc10f888c37131f1b86825d3c615a5522c5e2af1e44`; module, tests, preregistration and UMRL source hashes are recorded.

## Lane deltas

| Lane | Result | Evidence class | Remaining gate |
|---|---|---|---|
| A | A two-edge weight perturbation changes the exact optimum from 60 to 63 while both 10-node runs enumerate 1,024 states and match the bounded comparator. Scaling remains null. | Local exact classical fixture | Matched QPU/GPU workload, independent baseline and accepted-output contract. |
| B | Receipt-v4 canonical fixture bytes bind request and key identity. Fixture-key rotation/revocation and request/key mutations reject; job, invoice and provider claim remain null. | Synthetic HMAC authentication fixture | External authorization, provider signing key, execution and billing evidence. |
| C | Unsafe target paths reject. A valid target uses the same device for parent/stage; concurrent writers expose only complete payloads. Durability remains process-only. | Same-filesystem process fixture | Kernel/filesystem crash, cache, flush and power-loss durability. |
| D | ZIP64 local header, central entry, disk-relative offset and 64-bit data descriptor cross-bind; payload remains unread. | Synthetic ZIP64 cross-bind | Real producer archives, all record variants and payload provenance. |
| E | Three-event custody chain passes only with a complete terminal hash; truncation and duplicate sequence reject. Physical sample claim remains null. | Synthetic custody negative control | Operational issuers, independent review and physical sample. |
| F | Two-component model compares independent and shared covariance; invalid covariance and zero-output denominator return null. | Model only | Sourced lifecycle data, measured covariance and accepted-output measurement; no commercial interpretation. |
| G | Three-measurand `m/s/kg` covariance block is symmetric and PSD with all pairwise product dimensions; calibration remains null. | Synthetic typed covariance | Measured covariance and traceable calibration. |
| H | Declared center and adverse ranking alternatives yield stability range `[0, 1/3]`; capital remains null. | Illustrative scenario grid | Owner-approved priorities, sourced distributions and outcome model. |
| FND/EQN | Exact rational division gives `[1/2, 2] m/s`; multiplying by `[2, 3] s` yields `[1, 6] m`, preserving UMRL source and `RealModel/Model` sort. | Source-typed rational model | Independent derivation, more registered units and falsifiers; no physical-law claim. |
| SCM | Fiction-only fresh transcript passes; replay, expiry, revocation, scope and response mutations reject. Empirical coupling remains null. | Fiction only | No empirical promotion; future studies remain separately gated. |
| AI-COST | Version-seven lineage links to v6/v5/v4 and binds source, config, split and metric hashes. Candidate result and functional equivalence remain null. | Synthetic data lineage | Frozen functional-equivalence contract and measured quality/runtime/energy/cost. |
| QOS/QSVT | Second six-bit operator is linked to Cycle 014 v4, reconstructed across 64 basis states with integer residual 0; resources are 6 qubits/bits and depth/gates 3/3. Hardware remains null. | ER6 synthetic reconstruction | Independent reconstruction, generalized proof and physical receipt. |

## Validation and evidence

- Cycle 017 focused tests: **13/13 passed**.
- Available Cycle 012–017 regression suite in the validation workspace: **84/84 passed**.
- `py_compile`, executable acceptance runner and JSON parsing: passed.
- GitHub Actions [run 36452385967](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/36452385967) on exact code/evidence SHA `f524ba90c8ab30e752408d6ed227189eb9d2e4fb`: **8/8 jobs passed** — Python 3.10, 3.11, 3.12, Qiskit verification, QSP phase synthesis, QSP reconstruction v0.40, reference benchmark and target snapshot noise.
- `main` was not modified or merged.

Primary references are PKWARE APPNOTE v6.3.10 FINAL (2022-11-01, §§4.3.7, 4.3.9, 4.3.12–4.3.16), Python `os.replace`/`tempfile.mkstemp` documentation, NIST SP 330 Section 2, and UQPU UMRL-031 at source revision `4824f7f034411dbbf9eeca6b41590f902ac6fca6`. They constrain parser and typed-interface design; they do not convert fixtures into external evidence. All receipt, custody, covariance, ranking, AI and QOS data remain synthetic/model-only; SCM remains fiction-only. No hardware performance, provider execution, calibrated measurement, commercial economics, new physical law, AI equivalence, capital authorization or empirical spiritual communication is claimed.

All twelve lanes remain `BLOCKED_WITH_PROGRESS`; no external gate is closed. Continue with Cycle 018 from the exact Cycle 017 closeout branch head.

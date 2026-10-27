# Eight-Lane integration — 2026-10-27 — partial-information ergotropy certificate

**Cycle artifact:** Batch 078  
**Start head:** `20dd5cab2272e204465889d3f77c377a41fa8cd9`  
**Evidence:** PEER_REVIEWED_THEORY + SOFTWARE_CONTRACT; full SDP reproduction OPEN  
**Canonical gap:** `docs/RESEARCH_GAP_FND001_ERGOTROPY_PARTIAL_INFORMATION_2026-10-27.md`

## Integration outcome

The new primary-source watch covers Pagliaro et al., *Physical Review Letters* 137, 130401, DOI 10.1103/pl26-g6vy. Their method certifies a lower bound on ergotropy from partial expectation-value data, assuming a known Hamiltonian, and extends the certificate to finite shot statistics. The project implements only the confidence-radius component:
`epsilon_i = sqrt(2 * ln(2K/delta) / N_i)`.
No SDP, ergotropy estimate, physical energy measurement, or quantum job was run by UQPU.

## Cross-lane dependency map

- **A:** strict finite-shot confidence-radius function and tests; next implement a small-system certificate reproduction only after equations and solver dependencies are pinned.
- **B:** no-submit provider-neutral policy unchanged.
- **C:** count all measurement shots and reconstruction/I/O; no Hilbert-space-to-classical-storage inference.
- **D:** any future hardware mapping needs calibrated Hamiltonian/observable definitions and target-specific measurement costs.
- **E:** no energy/material/fuel/fusion claim.
- **F:** an ergotropy lower bound is a resource certificate, not net device energy or accepted-task economics. Keep boundary-complete energy accounting separate.
- **G:** no fabrication or factory result; maintain D/G co-design.
- **H:** dated primary-source watch published; six-language master-plan references remain preserved as strategic context.

## Validation and non-claims

The helper rejects empty/noninteger/nonpositive shot counts and delta outside (0,1). Tests cover the formula, monotonicity and invalid inputs. Exact-head hosted CI is the required validation gate. No local test execution is claimed.

No new law of nature, quantum advantage, physical memory replacement, Pangola material substitution, accepted bio-oil, fusion electricity, WACC reduction, or Data-Center-to-One-Phone result is established. No paid QPU job was submitted.

## Next highest-value gate

After exact-head CI passes, pin the source and reconstruct the two-stage SDP. For small known states, compare the certificate against exact spectral ergotropy; include cases with insufficient measurements, noisy finite shots, noncommuting observables and solver failure. Check certificate validity and empirical confidence coverage before any real-device experiment. Record all measurement and control costs separately.

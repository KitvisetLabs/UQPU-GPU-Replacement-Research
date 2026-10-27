# Literature watch — 2026-10-27: learning to erase quantum states

**Primary source:** Haimeng Zhao, Yuzhen Zhang and John Preskill, “Learning to erase quantum states: thermodynamic implications of quantum learning theory,” npj Quantum Information 12, Article 137 (2026).  
**Publication date:** 2026-05-27; version of record: 2026-08-20.  
**DOI / publisher record:** https://doi.org/10.1038/s41534-026-01273-4  
**Evidence class:** PEER-REVIEWED THEORETICAL RESULT; no UQPU reproduction or device-energy measurement.  
**Primary owner:** Lane H — literature publication.  
**Implementation/evaluation owners:** Lane F — thermodynamic accounting and evidence; Lane A — reproducible formal/model tooling if selected.  
**Feeds:** FND-001, FND-002, FND-006, EQN-001–006, INV-034/035; lanes A/C/F/H.

## Genuine result

The authors construct a reversible learning-to-erase protocol for a known class of distinguishable quantum states when learning algorithms output state-preparation circuit descriptions. For efficiently learnable structured state classes, the protocol can attain the information-theoretic Landauer work cost with efficient computation. They also prove a computational no-go result: under stated cryptographic assumptions, some state classes cannot reach the optimal work cost using efficient erasure protocols. Thus the information-theoretic minimum can depend on the state-class description while computationally bounded agents face a larger cost.

This is a precise bridge between state learnability, circuit complexity and thermodynamic work—not a claim that learning has zero wall-plug energy in a physical device. The paper's idealized accounting isolates logical irreversibility and explicitly leaves implementation costs such as error correction and device maintenance for future work.

## Assumptions and limitations

- The theorem is scoped to a defined ensemble/class of distinguishable states and learning algorithms that output circuit descriptions; it is not a universal erasure procedure for arbitrary unknown states.
- The main protocol assumes the relevant state-preparation operations and reversible learning construction are available; sample complexity, workspace/ancillas and runtime remain resources that must be accounted for.
- Several results use a trivial Hamiltonian. Nontrivial internal-energy changes and real device dynamics require separate accounting.
- The computational no-go relies on stated cryptographic assumptions. Those assumptions must be recorded, not treated as empirical observations.
- The article reports no newly generated or analyzed experimental dataset. UQPU has not independently rebuilt its proof or measured the protocol.

## Exact UQPU relevance

- **FND-001:** distinguish logical work/entropy accounting from wall-plug energy, refrigeration, controls, error correction and maintenance. Track active memory, retained state, uncomputation and the cost of recycling memory.
- **FND-002:** state-class information and classical circuit descriptions may lower an information-theoretic erasure cost, but this does not make a Hilbert-space dimension equal to readable classical storage.
- **Lane A:** a future prototype may test reversible learning/uncomputation on a small, fully specified state family; include training/sample complexity, circuit-description bytes, classical runtime, ancilla restoration and failure probability.
- **Lane C:** report physical workspace and readable memory separately from quantum state dimension or compact classical description.
- **Lane F / FIN-001:** only after reproducible resource and energy data exist should the method affect a cost-per-accepted-task or time-to-evidence model. This paper alone changes no financed principal, interest expense or WACC.
- **INV-034/035:** the result is a theorem under stated assumptions, not a new physical law or a license to bypass Landauer accounting.

## Falsifiable follow-up

1. Pin the version-of-record article and supplementary information; independently extract the state-class assumptions, distinguishability threshold, sample complexity, work expression and cryptographic hypothesis.
2. Choose a finite, efficiently describable state family with known preparation circuits. Rebuild the learning and reversible-uncomputation steps independently, including ancilla reset and failure branches.
3. Compare predicted logical work against the information-theoretic lower bound and a deliberately under-informed baseline. Separately log circuit gates/depth, workspace, copies N, sample count, circuit-description bytes and classical runtime.
4. Search counterexamples at the limits of the state distinguishability and efficiency assumptions. Test a cryptographic-hardness case only as a theorem/model exercise with the assumption explicitly marked.
5. Any lab follow-up must measure boundary-complete work/energy and report controls, calibration, uncertainty, device overhead and replication. Do not infer wall-plug energy from the theorem's logical work expression.

**Decision rule:** reject any claimed benefit that depends on hidden state-class knowledge, omitted learning/workspace costs, un-restored ancillas, or an unacknowledged cryptographic assumption. Keep information-theoretic work, efficient-protocol complexity and measured physical energy as distinct quantities.

## Non-claims

This paper does not establish a UQPU energy advantage, a better Landauer limit, quantum speedup, readable-memory equivalence, lower project financing cost, a new physical law, or Data-Center-to-One-Phone compression. It does not supply an empirical UQPU result.

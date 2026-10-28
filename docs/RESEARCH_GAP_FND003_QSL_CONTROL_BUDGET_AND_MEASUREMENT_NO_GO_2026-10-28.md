# Research gap — gate-specific QSL, optimal-control budget and measurement-only no-go

**Gap ID:** RG-FND003-QSL-CONTROL-BUDGET-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — workload/runtime comparison contract  
**Cross-lane owners:** B (target identity), C (state/memory/I/O), D/G (Hamiltonian/control hardware), E (thermodynamic boundary), F (evidence/economics), H (literature)  
**Status:** OPEN / LITERATURE_ONLY / RECONSTRUCTION_NOT_RUN  
**Related:** FND-001, FND-003, FND-004, FND-006, EQN-001–EQN-006, INV-029–035  
**Watch:** [quantum time-optimal control and thermodynamic limits](literature_watch/2026-10-28-quantum-time-optimal-control-and-thermodynamic-limits.md)

## Questions

1. Can a gate-specific unitary QSL and a time-optimal-control solution be compared under the same Hamiltonian/control constraints to give a useful necessary-condition check for UQPU scheduling?
2. Does any proposed measurement-driven thermodynamic operation remain advantageous when the exact theorem assumptions and all feedback, thermal-contact, acquisition, processing, reset and controller resources are counted?

## Source-reported leads and scope

- Stepanenko et al., PRA accepted 2026-10-21, DOI 10.1103/rsjw-pk53: quantum brachistochrone/Lax-pair approach for a specified nearest-neighbor qubit-lattice control budget.
- Nelson and Barnes, PRA accepted 2026-10-15, DOI 10.1103/28zn-ch8y: gate-specific unitary speed limit under bounded Hamiltonian spectral width. The theorem has not been independently reconstructed in this project.
- Koshihara and Yuasa, PRA accepted 2026-10-26, DOI 10.1103/4kmf-nzsm: scoped no-go for steady-cycle work extraction from bare measurements without feedback or thermal contact.
- Ji, Gour and Wilde, PRL accepted 2026-10-06, DOI 10.1103/x67n-33gr: thermodynamic bounds with quantum side information and explicit accounting for acquisition, processing and reset.
- Zhan et al., PRL published 2026-10-22, DOI 10.1103/z9t9-mwgv: reported single-qubit optical simulation of a strong Mpemba effect under a Davies-map model.

These are external sources. UQPU has not reconstructed their proofs, reproduced the experiment, run a matched device test or measured end-to-end task energy. The no-go result is restricted to its premises and is not a universal prohibition on feedback-driven quantum engines.

## Required reconstruction

1. Pin the exact source version, theorem statement, assumptions, Hamiltonian and control budget.
2. Check dimensions, boundary conditions, allowed control functions, drift, spectral-width/norm convention, gate equivalence including global phase, fidelity/error threshold and finite-size scaling.
3. Independently solve small systems using two methods and compare with a trusted reference; keep optimal-control objective, QSL lower bound and observed time as separate quantities.
4. For measurement thermodynamics, bind the finite-dimensional state space, measurement class, steady-cycle premise, feedback prohibition and absence of thermal contact. Search counterexamples only within all stated premises.
5. If any premise is relaxed, declare the changed assumption and charge every introduced resource: preparation, controller, feedback, bath, measurement, information processing, reset, wall-plug energy and cooling.
6. Use held-out sizes/parameters and preserve failed or undecided cases. A bound or simulation cannot be promoted to an accepted-task performance result.

## Closure rule

Close only after independent theorem reconstruction and counterexample search. Any claim about device performance requires a matched hardware/control experiment and accepted-useful-task accounting. No current source supports a UQPU speedup, lower total energy, cost/task advantage, new physical law or mission-level success.

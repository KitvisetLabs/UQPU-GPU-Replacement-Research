# Unified Typed Mathematical Goal Framework — Cycle 013 Checkpoint

Date: 2026-09-28
Branch: research/cycle-013-delta-01-2026-09-28
Status: FORMALIZATION CHECKPOINT / NOT A SCIENTIFIC RESULT

This note defines a common mathematical interface for the research portfolio. It makes goals explicit and machine-auditable; it does not establish that any target is feasible or achieved. Every claim remains typed as a definition, assumption, model, simulation, measurement, or independently replicated result.

## 1. A goal is a typed contract

Represent goal i by

G_i = (D_i, X_i, Y_i, U_i, C_i, Theta_i, E_i, F_i, Pi_i),

where D_i is the domain, X_i the admissible inputs and states, Y_i the accepted output, U_i the units and dimensional signature, C_i the constraints, Theta_i the uncertain parameters, E_i the evidence class, F_i the preregistered falsifier, and Pi_i the provenance record.

A goal is evaluable only if it is well-typed:

WellTyped(G_i) = Complete(G_i) AND DimensionalConsistent(G_i) AND Observable(Y_i) AND Falsifiable(F_i) AND ProvenanceBound(Pi_i).

Missing information is represented as bottom (unknown/not measured), never silently imputed as zero or success.

## 2. Feasibility, performance, and evidence are separate predicates

For design z, environment omega, and outcome y, define

Pass_i(z, omega) = 1{ y(z, omega) in Y_i AND C_i(z, omega) }.

Under uncertainty distribution P_i, a probabilistic requirement is

Pr_{omega~P_i}[Pass_i(z, omega)=1] >= 1-alpha_i.

The probability statement is meaningful only when P_i, sampling design, uncertainty treatment, and evidence class are specified. A model-derived probability remains model evidence.

For a portfolio optimization, use a constrained objective:

z_i* in argmin_{z in Z_i} J_i(z)
subject to Pass_i(z, omega) meeting the declared gate.

Cost per accepted output is

J_i(z) = (C_build + C_run + C_energy + C_cooling + C_data + C_error + C_maintenance + C_finance) / N_accepted,

with J_i = bottom when N_accepted=0 or any required cost term is unknown. This prevents a cheap but incorrect, incomplete, or unreproducible output from appearing advantageous.

## 3. Cross-lane composition

A dependency edge i to j transfers a typed interface, not an evidence grade:

I_ij = (variables, units, assumptions, provenance, uncertainty).

Composition is admissible only if units and assumptions match and source hashes are retained:

Compose(G_i,G_j) = G_ij if Compatible(I_ij)=1, otherwise bottom.

The evidence state of a composed claim is bounded by its weakest required dependency:

e(G_ij) <= meet over k in deps(i,j) of e(G_k).

Thus shared code or a mathematical analogy cannot promote one lane's result into another lane's empirical evidence.

## 4. Discovery gate for candidate equations

For a candidate law M_theta and observations D, record the candidate, units, symmetries, conservation constraints, causal scope, null model, held-out predictions, and failure rule. A candidate becomes a project-verified discovery only after all declared gates pass:

Discovery(M_theta) = T AND S AND K AND P AND H AND R,

where T is dimensional/type consistency, S symmetry review, K conservation/causality review where applicable, P preregistered falsifiable predictions, H held-out test success, and R independent reproduction. This is a governance definition, not a theorem that successful candidates are true.

## 5. SCM fiction/empirical type firewall

Let Fic denote propositions true only inside the Lokathibodi fictional canon and Emp denote claims about the physical world. The fictional mind/mental-factor ontology, Abhidhamma-inspired state transitions, occult control, inter-realm channel, portal, and economy are typed in Fic.

There is deliberately no implicit cast: Fic does not imply Emp.

A candidate empirical statement must instead pass an explicit evidence constructor:

EmpiricalClaim(q) = Operationalize(q) AND BlindAndNullControlled(q) AND OrdinaryCausesTested(q) AND SourceInformationRecovered(q) AND IndependentReplication(q).

Until those predicates are evidenced, empirical coupling is bottom. This framework permits rich fictional mechanics while preventing narrative consistency, simulated signals, quantum terminology, or unusual sensor output from being reported as spiritual communication.

## 6. Portfolio coverage and synchronized progress

Let the required lane set be

L = {A, B, C, D, E, F, G, H, FND/EQN, SCM, AI-COST, QOS/QSVT}.

For cycle t, completeness is

CompleteCycle(t) = AND over lane l in L of [DeltaRecorded(l,t) AND ArtifactOrReason(l,t) AND GateState(l,t)].

A blocked lane can meet the progress contract through a bounded blocker-reduction artifact, negative result, or explicit next external dependency. Completion means portfolio accounting is complete; it does not mean every lane's scientific target passed.

## 7. Initial goal registry fields

Every machine-readable goal record should include:
- stable goal ID and lane;
- typed domain and target quantity;
- operational observable and acceptance interval;
- units/dimensions;
- baseline and comparison functional unit;
- constraints and uncertain inputs;
- evidence class and source hashes;
- falsifier and held-out test;
- status: DEFINED, MODEL_ONLY, SYNTHETIC, MEASURED, REPLICATED, or BLOCKED;
- downstream consumers and explicit non-claims.

## 8. Scope and next work

This checkpoint supplies the shared mathematical vocabulary and typed invariants. Cycle 013 still requires its handoff's twelve bounded lane deltas, executable fixtures, focused/full tests, exact-SHA Actions verification, and separate closeout. No cycle work is claimed complete by this note. No GPU/QPU replacement, physical-law discovery, spiritual communication, hardware advantage, or economic target is claimed.

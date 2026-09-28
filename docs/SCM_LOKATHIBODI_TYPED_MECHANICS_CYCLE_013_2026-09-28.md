# SCM Lokathibodi Typed Mechanics — Cycle 013 Formalization

Date: 2026-09-28
Branch: research/cycle-013-delta-01-2026-09-28
Status: FICTIONAL MECHANICS SPECIFICATION / EMPIRICAL COUPLING NULL

## 1. Type boundary

This document defines a mathematical system for the Lokathibodi fictional canon. Its symbols denote fictional entities and rules. No function below is a demonstrated physical mechanism.

Use two disjoint proposition types:
- Fic: statements evaluated under the canon's rules.
- Emp: statements about the physical world.

There is no implicit coercion Fic -> Emp. A fictional rule can motivate a separately preregistered empirical hypothesis, but does not supply its evidence.

## 2. Fictional state space

At discrete story-time t, define the fictional state

x_t = (r_t, c_t, f_t, i_t, a_t, k_t, q_t),

where:
- r_t in R is the realm/location node;
- c_t in C is the fictional citta-class label;
- f_t in [0,1]^p is a vector of normalized cetasika-like fictional factors;
- i_t in I is intention/command content;
- a_t in A is attention/awareness allocation;
- k_t in K is consent state and its scope/expiry;
- q_t in Q is channel/resource state.

The factor vector is a modeling convenience for this canon, not a claim that Buddhist Abhidhamma assigns numerical magnitudes to mental factors. Canon-specific taxonomies and transition rules must be declared in a versioned registry.

A valid state belongs to the constraint set X_Fic:

x_t in X_Fic iff 0 <= f_{t,j} <= 1 for every j, labels are registered, realm edges are permitted, and the consent record is well formed.

## 3. Transition and control law

A fictional transition is a typed stochastic kernel

P_Fic(x_{t+1} | x_t, u_t, e_t; theta),

where u_t is an attempted control, e_t is fictional context, and theta is a versioned set of canon parameters. The transition must preserve the registered state constraints:

P_Fic(x_{t+1} in X_Fic | x_t in X_Fic, u_t, e_t; theta) = 1.

An illustrative factor update is

f_{t+1} = clip_[0,1]( A_theta f_t + B_theta phi(i_t,a_t,e_t) + epsilon_t ),

where A_theta and B_theta are fictional transition parameters and epsilon_t is a declared story-world disturbance. This equation is only a compact authoring device; parameter values and factor causality are canon decisions, not measured quantities.

The control law is

u_t^* = argmax_{u in U_Fic(x_t)} V_Fic(x_t,u),

subject to the safety gate below. V_Fic is a narrative utility (for example, coherence or intended consequence), never a real-world welfare or efficacy estimate.

## 4. Consent, scope, expiry, and replay safety

Represent a consent grant as

g = (subject, controller, scope, t_start, t_expiry, nonce, status).

A control is admissible only if

Allow_Fic(u_t,g,t) =
1{status=ACTIVE}
1{t_start <= t < t_expiry}
1{target(u_t) in scope}
1{controller(u_t)=controller(g)}
1{nonce(u_t) not in UsedNonces}.

If Allow_Fic=0, the transition must leave protected state components unchanged:

(1-Allow_Fic) * ||x'_{protected}-x_{protected}|| = 0.

Revocation changes status to REVOKED and invalidates outstanding commands. Regrant requires a fresh nonce and a new grant record; the old grant is never reactivated. This defines a fictional safety invariant and can be checked in software without asserting a real mind-control capability.

## 5. Communication channel and information criterion

For fictional source message M, realm/channel state Q, and received symbol sequence Y, model

Y = Channel_Fic(M,Q,N),

with conditional distribution p_Fic(y|m,q). A successful story-world communication event requires:
1. a registered sender and receiver;
2. active, scoped consent at both endpoints where the canon requires it;
3. valid challenge/response binding to fresh nonces;
4. decoding to a message in the declared alphabet;
5. a declared error budget and resource debit.

A fictional channel may use the information measure

I_Fic(M;Y | Q) = sum_{m,y,q} p(m,y,q) log2( p(m,y|q) / (p(m|q)p(y|q)) ).

For a fictional transfer to carry at most B bits, require I_Fic(M;Y|Q) <= B under the story's declared channel model. A simulated value of I_Fic is not evidence of cross-realm information transfer.

Authentication can be represented abstractly by Verify_Fic(pk, transcript, signature)=true, with transcript binding the session nonce, message hash, scope, and expiry. This is an identity/provenance rule inside the fiction; a cryptographic signature authenticates a key holder, not a spiritual source.

## 6. Realm graph and portal resource accounting

Let the fictional realm topology be a directed graph G_Fic=(R,E). A portal edge e=(r_i,r_j) is available only when its fictional preconditions hold. For transfer z, track a declared resource vector

b_t = (energy, mass, information, coherence, risk).

A canon may choose an exact conservation rule or a bounded exchange rule. A generic balance equation is

b_{t+1} = b_t + input_t - output_t + exchange_t,

with a registered invariant L b_t = constant for each conserved projection L. Any exception must be explicit in the canon as a named source/sink; unexplained creation is a continuity error within this model.

The economics extension can then be written as

Cost_Fic(z) = sum_j price_j * resource_used_j + risk_penalty(z),

subject to portal capacity, consent, and conservation constraints. Prices and risk weights are worldbuilding parameters, not estimates of actual inter-realm markets.

## 7. Canon validation properties

A software validator for this fictional system may test:
- all state labels and realm edges are registered;
- factor values remain within their declared ranges;
- expired, revoked, out-of-scope, or replayed commands fail closed;
- regrant uses a new grant and nonce;
- channel transcript binds sender, receiver, message, scope, and session nonce;
- resource balance satisfies registered invariants;
- every narrative outcome records its model version and assumptions.

Passing these tests establishes internal rule consistency only.

## 8. Empirical firewall and candidate test path

An empirical candidate q would need a distinct record with operational sensor variables, ordinary-source controls, preregistered blinding, held-out decoding, a source-dependent information test, calibrated false-positive rate, independent sites, and an explicit stopping rule:

EmpClaim(q) = Operational(q) AND Blinded(q) AND NullControlled(q)
AND OrdinaryCausesExcluded(q) AND SourceInformationRecovered(q)
AND IndependentReplication(q).

Until each required predicate has external evidence, EmpClaim(q)=unknown, not true. Current empirical coupling for the fictional mechanics above remains null.

## 9. Scope

This is a formal worldbuilding mechanics proposal. It introduces no evidence for spirits, post-mortem consciousness, telepathy, spiritual control, portals, or physical cross-realm communication. Canonical names, categories, and causal rules should be reconciled with the project's five-volume source text before being treated as canon.

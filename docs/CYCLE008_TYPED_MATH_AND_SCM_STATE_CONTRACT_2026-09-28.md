# Cycle 008 typed mathematics and SCM state contract

**Status:** Active-cycle research checkpoint
**Scope:** UMRL-031 and SCM-MATH-020–023
**Evidence class:** Formal schema, exact-rational checks, and synthetic fixtures
**Machine registry:** benchmarks/experiments/cycle008-delta01-typed-math-scm-registry.json
**Executable checker:** software/uqpu-prototype/uqpu/cycle008_delta01.py

## 1. Typed project quantities

Every declaration in this checkpoint carries a quantity kind, unit code,
dimension vector, domain sort, and evidence type. The checker accepts only
exact rational dimension exponents and compares each real-model unit vector
with its registered vector. It does not infer units from a name or prose.

The expression checker covers:

$$
[T_{\mathrm{acc}}]=[\text{accepted count}]/[\text{elapsed time}],
\tag{008-MATH-1}
$$

$$
[c_{\mathrm{fuel}}]
= [C_{\mathrm{total}}]\big/([m_{\mathrm{accepted}}][H_{\mathrm{LHV}}])
=\mathrm{USD/J},
\tag{008-MATH-2}
$$

and

$$
[P_{\mathrm{net}}]
=[\eta P_{\mathrm{fusion}}]
=[P_{\mathrm{recirculating}}]
=[P_{\mathrm{auxiliary}}]
=\mathrm W.
\tag{008-MATH-3}
$$

The second equation is a useful dimensional counterexample: since
$[H_{\mathrm{LHV}}]=\mathrm{J/kg}$, the canonical SI dimension vector for
$\mathrm{USD/J}$ includes mass exponent $-1$. A unit declaration omitting
that exponent fails the checker. The result verifies the declared algebra,
not any measured fuel, cost, or fusion performance.

## 2. Domain and evidence no-cast rule

UMRL-031 attaches sort $\sigma$ and evidence type $\tau$ to each declared
quantity:

$$
q=(v,k,u,\mathbf d,\sigma,\tau,\pi),
\qquad \Gamma\vdash q:\tau@\sigma.
\tag{UMRL-031}
$$

The typing rules preserve declared domains under ordinary composition. A
fictional value cannot become an empirical value unless a cross-sort map is
explicitly declared and independently validated. The checker rejects missing
or unvalidated maps. It intentionally includes no positive bridge fixture.

This rule is a governance property of the formal language, not a claim about
the impossibility or existence of spiritual phenomena.

## 3. Fictional mind and communication types

The SCM addendum extends the v0.1 canon without changing the status of its
doctrinal references:

$$
\chi_t:\operatorname{CanonMindState}[v_c],\quad
\mathbf z_t:\operatorname{MentalFactorVector}[v_c],\quad
r_t:\operatorname{RealmLabel}[v_c].
\tag{SCM-MATH-020}
$$

Each state has a canon version. The state and mental-factor vector are
fictional ontology objects, not measured neural, field, or metaphysical
coordinates.

Atthan Control permits a fictional action only when the consent grant matches
the subject, action, purpose, and resource; is live and unrevoked; has a fresh
nonce; preserves agency; passes the safety predicate; and leaves an audit
record:

$$
\operatorname{Permit}(u\mid g)
=\mathbf1[
\operatorname{ScopeMatch}\land
t_{\mathrm{issued}}\le t<t_{\mathrm{expiry}}\land
\neg\operatorname{Revoked}\land
\operatorname{FreshNonce}\land
\operatorname{Agency}\land
\operatorname{Safe}\land
\operatorname{Audited}].
\tag{SCM-MATH-021}
$$

The synthetic negative corpus rejects scope mismatch, expiry, revocation,
inactive agency, and failed safety. Consent is revocable and does not transfer
between subjects or purposes.

The inter-realm communication object remains a fictional channel:

$$
x_t:\operatorname{Symbol}[v_c],\qquad
y_t\sim W_F(\cdot\mid x_t,z_t),\qquad
\hat x_t=D_F(y_t,k_t),
$$

$$
\operatorname{Accept}_F
=\operatorname{Auth}\land\operatorname{Fresh}\land
\operatorname{Consent}\land
\bigl[\operatorname{Score}_F(x_t,\hat x_t)\ge\theta_F\bigr].
\tag{SCM-MATH-023}
$$

That formalizes what counts as successful communication inside the story:
authenticated, fresh, consented, and scored against a frozen fictional
criterion. It supplies no empirical spiritual-communication result.

## 4. Fictional conservation and five-volume rules

For a fictional portal ledger, every entry must use one canon quantity, one
canon unit, and one canon version:

$$
\operatorname{CanonBalance}(Q)
=\mathbf1\!\left[
\left|\sum_i\Delta Q_i\right|\le\epsilon_Q
\land\operatorname{SameCanonQuantity}
\land\operatorname{SameCanonUnit}
\land\operatorname{SameVersion}
\right].
\tag{SCM-MATH-022}
$$

The synthetic corpus tests exact rational balance, residual overflow, unit
mismatch, and non-rational numeric inputs. A passing ledger means only internal
story consistency; it does not revise physical conservation laws.

All five volumes receive a machine-checked domain sort and non-cast boundary.
Each also has one local invariant: versioned Abhidhamma-inspired taxonomy,
consent-scoped control, authenticated challenge-response, anti-replay and
noncoercion, or double-entry settlement with consent. These are consistency
requirements for the fictional system, not claims of doctrinal completeness.

## 5. Current boundary and next work

The artifact covers three selected real-model dimensional equations, 15
typed quantities, four added SCM equations, five volume contracts, one valid
synthetic consent case, five consent negatives, one balanced story ledger,
four conservation negatives, and one rejected unvalidated bridge.

The audit does not yet classify all 134 UMRL declarations, prove physical
models, validate a real consent system, or demonstrate an SCM channel. The
Cycle 008 executable-acceptance artifact links a bounded test to each of the
12 lanes, while every lane's external evidence gate remains open. Cycle 008
remains active until the exact published code/evidence SHA passes CI and the
closeout record is published.

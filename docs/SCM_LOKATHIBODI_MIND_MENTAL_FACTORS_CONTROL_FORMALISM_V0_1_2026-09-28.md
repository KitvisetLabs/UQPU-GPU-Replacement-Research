# SCM / คำภีร์โลกาธิบดี — จิต เจตสิก อภิธรรม และอาถรรพ์คอนโทรล: Mathematical Formalism v0.1

**Date:** 2026-09-28  
**Status:** FICTIONAL MATHEMATICAL SYSTEM / RESEARCH-TO-FICTION BRIDGE / NO DEMONSTRATED SPIRITUAL CHANNEL  
**Machine-readable registry:** `benchmarks/experiments/cycle006-delta01-scm-lokathibodi-math-registry.json`

## 1. Scope and respectful boundary

This document gives *คำภีร์โลกาธิบดี* a rigorous mathematical language for
mind (`จิต`), mental factors (`เจตสิก`), Abhidhamma-inspired classification
(`อภิธรรม`), the fictional `อาถรรพ์คอนโทรล` system, and Spiritual
Communication Mechanics (SCM).

It is deliberately a **two-layer formalism**:

1. a canon/fiction layer in which states, realms, coupling, devices, and
   technology can be defined consistently and explored without arbitrary magic;
2. a real-world empirical layer in which sensors, controls, information,
   statistics, consent, and replication determine what may be claimed.

Mathematical notation does not establish that doctrinal categories are physical
state variables, that consciousness survives death, that realms are measured
locations, or that spiritual communication/control exists.  The formalization
also does not claim to replace or exhaust Buddhist doctrine.  Canonical Buddhist
taxonomies can be inserted as versioned reference tables later; v0.1 avoids
inventing a doctrinal count or equivalence.

## 2. Two-sorted universe: meaning without evidence leakage

Use two distinct sorts:

$$
\mathfrak R=(\mathcal X_R,\mathcal Y_R,\mathcal I_R)
\quad\text{and}\quad
\mathfrak F=(\mathcal X_F,\mathcal Y_F,\mathcal I_F),
\tag{SCM-MATH-001}
$$

where $\mathfrak R$ contains real measurements and $\mathfrak F$ contains
fictional/canonical states.  A story interpretation map
$J:\mathcal X_R\to\mathcal X_F$ is permitted.  A physical bridge
$B:\mathcal X_F\to\mathcal Y_R$ is **not** presumed; it remains null until a
discriminating experiment validates it.

The typing rule is

$$
J(r):\mathsf{FICTION\_INTERPRETATION}
\not\Rightarrow
B(f):\mathsf{PHYSICAL\_MEASUREMENT}.
\tag{SCM-MATH-002}
$$

This firewall lets the novels use rich spiritual meaning while preventing an
in-world fact from becoming a real-world claim.

## 3. Mind-event state (`จิต–เจตสิก`)

Represent one canon mind event as

$$
\chi_t=(c_t,\mathbf z_t,a_t,v_t,q_t,\iota_t).
\tag{SCM-MATH-003}
$$

The coordinates are:

- $c_t\in\mathcal C$: a versioned **citta/mind-event category**;
- $\mathbf z_t\in[0,1]^m$: activation or narrative salience of $m$ registered
  **cetasika/mental-factor categories**;
- $a_t\in\mathcal A$: the object/content attended to;
- $v_t\in\mathcal V$: cognitive-process or scene-process position;
- $q_t\in\mathcal Q$: qualitative ethical/affective/canonical tags;
- $\iota_t$: identity/session reference, never assumed identical to a soul or
  metaphysical self.

If the canon uses presence/absence rather than degree, set
$\mathbf z_t\in\{0,1\}^m$.  Compatibility is a constraint system:

$$
A\mathbf z_t\le\mathbf b,
\qquad
E\mathbf z_t=\mathbf d(c_t),
\qquad
\mathbf z_t\in\mathcal Z_{\mathrm{canon}}.
\tag{SCM-MATH-004}
$$

$A$ encodes incompatible combinations, $E$ encodes required co-occurrences,
and $\mathcal Z_{\mathrm{canon}}$ is a versioned canon table.  This gives the
author a consistency checker.  It does not assert that a real mind is literally
a finite vector.

## 4. Dynamics of mind and mental factors

The most general discrete transition is a controlled stochastic kernel:

$$
p(\chi_{t+1}\mid\chi_{0:t},u_t,o_t,r_t,\theta_F),
\tag{SCM-MATH-005}
$$

where $u_t$ is a permitted control/input, $o_t$ a perceived object,
$r_t$ a canon realm label, and $\theta_F$ fictional law parameters.  A Markov
version uses only $\chi_t$.  A deterministic story rule is the special case in
which this distribution is concentrated at one state.

Useful derived quantities include:

$$
H(\chi_t)=-\sum_xp_t(x)\log p_t(x),
\qquad
I(\chi_{t+1};u_t\mid\chi_t),
\tag{SCM-MATH-006}
$$

which measure uncertainty and control-relevant information inside the model,
not spiritual energy or moral worth.

## 5. Realm ontology as a graph, not a measured map

Let the canon's realm/classification system be

$$
\mathcal G_R=(\mathcal R,\mathcal E_R,\ell,\kappa),
\tag{SCM-MATH-007}
$$

where $\mathcal R$ is a finite versioned set of realm labels,
$\mathcal E_R$ allowed narrative transitions, $\ell(e)$ a transition cost or
story difficulty, and $\kappa(e)$ a rule/condition.  The graph distance

$$
d_R(r_i,r_j)=\min_{\pi:i\leadsto j}\sum_{e\in\pi}\ell(e)
\tag{SCM-MATH-008}
$$

is a narrative/control distance.  It is not meters, spacetime separation,
frequency, or energy unless the story later defines and conserves those units.

## 6. `อาถรรพ์คอนโทรล` as a fictional safe controller

Define the controller as a partially observed system

$$
\mathcal{AC}=(\mathcal X_F,\mathcal U_{\mathrm{consent}},
\mathcal Y,\mathcal T,\mathcal O,\mathcal S,\mathcal L),
\tag{SCM-MATH-009}
$$

with hidden canon state $\mathcal X_F$, consent-bounded controls
$\mathcal U_{\mathrm{consent}}$, observations $\mathcal Y$, transition kernel
$\mathcal T$, observation map $\mathcal O$, safety predicate $\mathcal S$, and
loss/objective $\mathcal L$.

The fictional controller chooses

$$
\pi^*=\arg\min_{\pi:\,u_t\in\mathcal U_{\mathrm{consent}}}
\mathbb E_\pi\!\left[
\sum_{t=0}^{T}\mathcal L(\chi_t,u_t)
+\lambda\,\mathbf1[\neg\mathcal S(\chi_t,u_t)]
\right],
\tag{SCM-MATH-010}
$$

with $\lambda$ treated as an effectively infinite fail-closed penalty for
non-consensual, coercive, unsafe, or unauthorized transitions.  For real people,
the system may control only ordinary interfaces and experimental stimuli under
approved consent; it has no validated ability to control mind, spirit, karma,
or realm.

The canon device stack is:

```text
canon ontology + state estimator
-> mental-factor compatibility engine
-> consent/authority gate
-> realm-route planner
-> SCM channel/authentication layer
-> semantic renderer
-> immutable provenance and safety log
```

## 7. Observation model and the real-world null

For physical sensors,

$$
Y(t)=H_{\mathrm{env}}[X_{\mathrm{env}}(t)]
+H_{\mathrm{human}}[X_{\mathrm{human}}(t)]
+H_{\mathrm{inst}}[X_{\mathrm{inst}}(t)]
+N(t)+g_{SR}H_{SR}[S(t)].
\tag{SCM-MATH-011}
$$

The first four terms are ordinary.  $g_{SR}H_{SR}$ is an explicit fictional or
hypothesis term.  Present real-world analysis starts at

$$
H_0:g_{SR}=0.
\tag{SCM-MATH-012}
$$

If a residual survives, ordinary model misspecification, leakage, calibration,
selection effects, and fraud remain competing explanations.  A residual is not
automatically a spirit, realm, or message.

The causal graph must compare at least:

```text
environment -> sensor <- instrument drift
operator expectation -> selection -> reported pattern
target metadata -> leakage -> decoder output
fictional source hypothesis -> candidate coupling -> sensor
```

A source effect is identifiable only if the protocol blocks or measures the
ordinary backdoor paths.

## 8. From anomaly to authenticated communication

Let $X$ be an unpredictable committed challenge, $Y$ the frozen decoded
response, and $Z$ all measured ordinary side information.  The residual channel
capacity is

$$
C_{SR}=\sup_{p(x)}I(X;Y\mid Z).
\tag{SCM-MATH-013}
$$

For a $K_i$-symbol trial with acceptance indicator $a_i$ and duration $T$,
verified information rate is

$$
R_v=\frac1T\sum_i a_i\log_2K_i,
\tag{SCM-MATH-014}
$$

reported together with symbol error, erasure, latency, jitter, false-positive
rate, leakage audit, and independent-site stability.  A useful fictional SCM-3
terminal requires a positive lower confidence bound on $R_v$ after all controls,
not merely an unusual waveform.

## 9. Protocol identity versus metaphysical identity

For identity hypothesis $H_j$ and independent preregistered challenges,

$$
\log BF_{j0}^{(n)}=
\sum_{i=1}^{n}
\log\frac{p(y_i\mid x_i,H_j,Z_i)}{p(y_i\mid x_i,H_0,Z_i)}.
\tag{SCM-MATH-015}
$$

Protocol authentication additionally requires nonce uniqueness, commitment
order, anti-replay, source-specific prospective information, and continuity
across sessions.  Even a large Bayes factor would support only the stated
protocol model under its assumptions; it would not solve the philosophical
identity of a person, self, mind-stream, or soul.

## 10. Imaging and reconstructed experience

SCM-2/SCM-3C reconstruction is an inverse problem:

$$
\hat s=\arg\min_s
\left\|y-Hs\right\|_{\Sigma^{-1}}^2+\lambda\mathcal R(s),
\tag{SCM-MATH-016}
$$

where $H$ is frozen before reveal, $\Sigma$ is noise covariance, and
$\mathcal R$ is an explicit regularizer.  Raw data, reconstruction, confidence,
and alternative reconstructions remain separate.  The renderer may never
overwrite raw evidence; hallucination and pareidolia benchmarks are mandatory.

## 11. Communication is not transport

An SCM-3 channel does not imply SCM-4 transport.  Any fictional portal must
specify a state map

$$
\mathcal P:(r_A,s_A)\mapsto(r_B,s_B,b),
\tag{SCM-MATH-017}
$$

including bridge state $b$, reversibility or erasure, failure modes, and identity
semantics.  For every quantity $Q$ declared conserved by the in-world theory,

$$
\Delta Q_A+\Delta Q_B+\Delta Q_{\mathrm{bridge}}=0
\quad\text{within }U_Q.
\tag{SCM-MATH-018}
$$

Mass, energy, momentum, charge, angular momentum, entropy/information, and causal
order are separate ledgers.  If the new fictional law changes one, it must state
which incumbent assumption changes and predict an observable difference.

## 12. Inter-realm information economy

Before matter transport, SCM-5 can exchange authenticated information/services.
For transaction $k$,

$$
\sum_a\operatorname{debit}_{ka}
=\sum_a\operatorname{credit}_{ka},
\qquad
\operatorname{settle}_k=
\operatorname{Auth}_k\land\operatorname{Consent}_k
\land\operatorname{NoReplay}_k\land\operatorname{CapacityAvailable}_k.
\tag{SCM-MATH-019}
$$

Physical commodity transfer is a different contract and also requires
SCM-MATH-018.  Information about gold, a claim on gold, and atoms of gold are
three different asset types.

## 13. Device and canon ladder

| Stage | Mathematical closure required | Canon use |
|---|---|---|
| SCM-1 anomaly detector | SCM-MATH-011/012 plus calibrated null distribution | finds unresolved residuals, never labels a spirit automatically |
| SCM-2 imager | SCM-MATH-016 plus independent sensors/sites | reconstructs with visible uncertainty and alternatives |
| SCM-3 communicator | SCM-MATH-013–015 plus bidirectional challenge-response | authenticated symbols → text → audio → video-like reconstruction |
| SCM-4 portal | SCM-MATH-017/018 plus explicit causal/state law | information success cannot skip transport gates |
| SCM-5 economy | SCM-MATH-019 plus identity, consent, scarcity, governance | information services first; matter only after conservation-accounted transport |
| อาถรรพ์คอนโทรล | SCM-MATH-003–010 plus safety/authority | internally consistent state navigation and device control in the fiction |

## 14. Five-volume mathematical arc

1. **ปฐมกลศาสตร์แห่งจิตและสภาวธรรม** — introduce
   SCM-MATH-001–006: what a state, observation, uncertainty, and mental-factor
   constraint mean; the first detector fails productively.
2. **บัญชาสวรรค์และกำเนิดอาถรรพ์คอนโทรล** — introduce
   SCM-MATH-007–012: realm graph, controller, safety, physical nulls, and a
   residual that remains unresolved.
3. **มายาการสัทธรรมปฏิรูปและระบบสร้างพญามาร** — introduce
   SCM-MATH-013–016: information capacity, cryptographic authentication,
   adversarial AI, deepfakes, spoofing, and reconstruction error.
4. **เปลวเพลิงกลียุคและสงครามชิงโลกธรรม** — scale to a networked multi-agent
   control problem with governance, consent, weaponization, and false authority;
   no institution may act on an unauthenticated message.
5. **รุ่งอรุณสุวรรณภูมิและยุคศิวิไลซ์** — allow the in-world SCM-3 threshold to
   pass only after independent replication; develop SCM-MATH-017–019 for portal
   and economic research while preserving conservation and identity conflicts.

## 15. Useful real-world by-products

The program can produce useful work even if no spiritual channel exists:

- robust multimodal anomaly detection and sensor calibration;
- blind human/AI decoding and pareidolia/hallucination benchmarks;
- conditional-information and leakage analysis;
- cryptographic commitment, challenge-response, and anti-replay protocols;
- provenance-preserving reconstruction and uncertainty visualization;
- consent-bounded human–computer control design;
- POMDP/state-estimation tools and narrative consistency checking;
- causal graphs, null libraries, adversarial tests, and independent-replication
  packages;
- conservation-aware fictional worldbuilding and double-entry economic design.

Negative results, broken equations, nulls, ambiguity bounds, and counterexamples
remain in the ledger because they strengthen both the research method and the
fiction.

## 16. Open gates

- No empirical mapping from `จิต`, `เจตสิก`, an Abhidhamma category, or a canon
  realm to a physical coordinate or sensor observable has been validated.
- No real $g_{SR}\ne0$, $C_{SR}>0$, authenticated cross-realm identity,
  spiritual control surface, portal, or inter-realm economy has been measured.
- Human or biological experimentation requires separate ethics approval,
  consent, safety review, privacy governance, and independent oversight; none is
  authorized by this formalism.
- The next safe technical step is machine validation of the ontology, equation
  references, type firewall, device-stage dependencies, and canon traceability.


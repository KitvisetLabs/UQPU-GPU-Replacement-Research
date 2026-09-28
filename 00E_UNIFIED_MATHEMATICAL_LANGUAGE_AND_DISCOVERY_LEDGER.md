# UQPU Unified Mathematical Language and Discovery Ledger

**Status:** Permanent project-wide mathematical interface / evidence-gated  
**Version:** UQPU-UMRL 0.2
**Established:** 2026-09-28  
**Primary invariant:** INV-037  
**Related:** INV-004, INV-007, INV-025–INV-036

## 1. Purpose and claim boundary

Every UQPU research objective must be expressible as a mathematical object with
defined variables, units or types, domain, assumptions, uncertainty, decision
predicate, falsifier, evidence requirement, and explicit non-claims.  Natural
language remains necessary, but it may not be the only specification of a goal.

UQPU-UMRL is a new **project-specific formal language and accounting calculus**.
It is not a newly discovered law of nature, proof that the North Star is
feasible, measured hardware performance, or commercial evidence.  Its purpose
is to make every target falsifiable and to expose missing terms rather than hide
them in prose.

The machine-readable Cycle 006 registry is:
`benchmarks/experiments/cycle006-delta01-unified-math-goal-registry.json`.

## 2. Typed objects

Let:

- $x\in\mathcal X$ be a candidate algorithm, system, device, material,
  process, plant, financing structure, or theory;
- $w\in\mathcal W$ be a frozen useful-service or experiment contract;
- $\omega\in\Omega$ be an operating condition or uncertainty realization;
- $p\in\mathcal P(t)$ be a provider available at date $t$;
- $g\in\mathcal G$ be a canonical project goal;
- $D$ be observations with provenance;
- $\Gamma$ be the evidence context attached to a claim;
- $\tau$ be an evidence type, not a scalar confidence score.

The evidence judgement is

$$
\Gamma\vdash c:\tau,
\qquad
\tau\in\{\mathsf{DEFINITION},\mathsf{THEORY},\mathsf{MODEL},
\mathsf{SIMULATION},\mathsf{LOCAL\_MEASUREMENT},
\mathsf{PROVIDER\_MEASUREMENT},\mathsf{PHYSICAL\_EXPERIMENT},
\mathsf{COMMERCIAL\_OBSERVATION}\}.
\tag{UMRL-001}
$$

There is no implicit cast between evidence types.  A simulation cannot be used
where a physical experiment is required, a tariff cannot become a bill, and a
roadmap cannot become measured economics.

## 3. Full-system dependency closure

The least fixed-point dependency closure prevents hidden infrastructure:

$$
\operatorname{cl}(x)
=\mu Z\left(\{x\}\cup\bigcup_{z\in Z}\operatorname{dep}(z)\right).
\tag{UMRL-002}
$$

Cost, energy, mass, volume, latency, labor, control electronics, host compute,
memory, storage, networking, cryogenics, cooling, state preparation, error
mitigation/QEC, repetitions, decoding, reconstruction, maintenance, and
financing are summed over $\operatorname{cl}(x)$.  A phone that depends on a
remote data center therefore has that data center in its closure.

For any extensive resource $r$,

$$
R_r(x;\omega)=\sum_{z\in\operatorname{cl}(x)}R_r(z;\omega),
\tag{UMRL-003}
$$

with overlap removed by stable resource identifiers.

## 4. Functional equivalence and accepted outputs

For each contract $w$, let $y_{wk}$ be observed metric $k$, $b_{wk}$ its
required boundary, $s_{wk}=+1$ when larger is better and $s_{wk}=-1$ when
smaller is better, and $u_{wk}>0$ its normalization scale.  The robust margin is

$$
m_w(x)=\inf_{\omega\in\mathcal U_{w,1-\alpha}}
\min_{k\in K_w}\frac{s_{wk}\,[y_{wk}(x,\omega)-b_{wk}]}{u_{wk}}.
\tag{UMRL-004}
$$

Categorical semantics, exact hashes, and required identities are Boolean
conjuncts rather than numeric ratios.  Functional acceptance is

$$
A_w(x)=\mathbf 1\!\left[m_w(x)\ge0\right]
\prod_{q\in Q_w}\mathbf 1[q(x)=\mathrm{true}].
\tag{UMRL-005}
$$

For attempted outputs $o_i$,

$$
N_{\mathrm{acc}}(x,w)=\sum_i\mathbf 1[A_w(o_i)=1].
\tag{UMRL-006}
$$

Throughput, cost, and energy use accepted outputs, never raw shots or attempted
jobs, as the denominator:

$$
T_{\mathrm{acc}}=\frac{N_{\mathrm{acc}}}{\Delta t},\qquad
c_{\mathrm{acc}}=\frac{C_{\mathrm{life}}}{N_{\mathrm{acc}}},\qquad
e_{\mathrm{acc}}=\frac{E_{\mathrm{life}}}{N_{\mathrm{acc}}}.
\tag{UMRL-007}
$$

If $N_{\mathrm{acc}}=0$ or any required lifecycle term is unknown, the
corresponding ratio is null, not infinity, zero, or an estimate silently filled
from another source.

## 5. Replacement and economic targets

Let $v_{jk}$ be capability $k$ of one competitive conventional subsystem unit
$j$, under the same $w$, horizon, and quality gate.  The accepted equivalent
unit count is

$$
N^{\mathrm{eq}}_{j,w}(x)=A_w(x)
\min_{k\in K_{j,w}}
\frac{v_k(x)}{v_{jk}},
\tag{UMRL-008}
$$

where every ratio is oriented so larger is better (for example, reciprocal
latency).  Missing capacity, bandwidth, persistence, durability, or access
semantics makes the value null.  The $10^8$-unit moonshot requires one
physically closed UQPU system and
$N^{\mathrm{eq}}_{j,w}\ge10^8$ for the explicitly named subsystem and workload;
it cannot be inferred from qubit dimension, TOPS, or asymptotic complexity.

Economic advantage is

$$
G_C(x,w)=
\frac{c_{\mathrm{acc}}(\mathrm{competitive\ reference},w)}
     {c_{\mathrm{acc}}(x,w)}.
\tag{UMRL-009}
$$

The primary and moonshot predicates are respectively $G_C\ge10^2$ and
$G_C\ge10^8$, after matched output and complete lifecycle accounting.

## 6. Data-center-to-phone closure

Let $\mathcal W_\star$ be the frozen target service portfolio and let
$V_\max,M_\max,P_\max,P^{\mathrm{thermal}}_\max$ be declared phone-class
volume, mass, price, and thermal/power boundaries.  The North-Star predicate is

$$
\begin{aligned}
\operatorname{PhoneReady}(x)=
&\left[\bigwedge_{w\in\mathcal W_\star} A_w(x)=1\right]
\land [\operatorname{essential}(\operatorname{cl}(x))\subseteq x]\\
&\land[V(x)\le V_\max]\land[M(x)\le M_\max]
\land[P_{\mathrm{device}}(x)\le P_\max]\\
&\land[P_{\mathrm{thermal}}(x)\le P^{\mathrm{thermal}}_\max]
\land[\operatorname{Reliability}(x)\ge R_\min].
\end{aligned}
\tag{UMRL-010}
$$

The user-defined US$10T–US$100T envelope is an ambition-scale input used to
construct $\mathcal W_\star$; dollars are not treated as a unit of computation.
The numeric phone boundaries remain target parameters until frozen by a
separate contract.

## 7. Cloud portability and software execution

For provider $p$, define ordered maturity indicators: discoverable $d_p$,
compilable $c_p$, dry-run validated $r_p$, simulator validated $s_p$, and
real-QPU/receipt validated $h_p$.  The date-stamped vector

$$
\Pi(t)=\frac1{|\mathcal P(t)|}
\sum_{p\in\mathcal P(t)}(d_p,c_p,r_p,s_p,h_p)
\tag{UMRL-011}
$$

must be reported componentwise.  Its components must not be averaged into a
claim that discovery or simulation equals hardware execution.

The provider-neutral correctness condition is the commuting relation

$$
d_w\!\left(
\operatorname{Normalize}_p(\operatorname{Execute}_p(
\operatorname{Lower}_p(\operatorname{Compile}(w)))),
\operatorname{Reference}(w)
\right)\le\varepsilon_w.
\tag{UMRL-012}
$$

## 8. Memory, state, storage, and information

Literal state equality is not required if application-visible behavior
commutes:

$$
d_w\!\left(O_w\circ F_x(u),O_w\circ F_{\mathrm{ref}}(u)\right)
\le\varepsilon_w\quad\forall u\in\mathcal U_w.
\tag{UMRL-013}
$$

Capacity, bandwidth, latency, random access, retention, persistence, durability,
recovery, and read/write semantics remain separate coordinates.  When a task
must emit one of $|\mathcal Y|$ distinguishable classical outputs, the noiseless
output lower bound is

$$
B_{\mathrm{out}}\ge\left\lceil\log_2|\mathcal Y|\right\rceil,
\tag{UMRL-014}
$$

with noisy channels requiring the appropriate information-theoretic correction.
Amplitudes that cannot be read under the contract are not counted as classical
RAM or storage.

## 9. Quantum algorithms and QOS/QSVT

A complete algorithmic error budget is additive only when a proved composition
bound supports it; the default upper-bound ledger is

$$
\epsilon_{\mathrm{total}}
\le\epsilon_{\mathrm{model}}+\epsilon_{\mathrm{algorithm}}
+\epsilon_{\mathrm{synthesis}}+\epsilon_{\mathrm{input}}
+\epsilon_{\mathrm{implementation}}+\epsilon_{\mathrm{sampling}}.
\tag{UMRL-015}
$$

For a QSVT polynomial candidate $P_d$ on domain $\mathcal D\subseteq[-1,1]$,

$$
\sup_{x\in[-1,1]}|P_d(x)|\le1,
\qquad
\sup_{x\in\mathcal D}|P_d(x)-f(x)|\le\epsilon,
\tag{UMRL-016}
$$

followed by phase synthesis, independent reconstruction, resource accounting,
and hardware evidence.  Polynomial existence alone is not a provider execution.

## 10. Device, material, and factory chain

Let $r_D$ be device requirements, $m_E$ measured material properties, $z_G$
process settings, and $q(m_E,z_G)$ resulting device metrics.  Qualification and
yield are

$$
Q_D=\mathbf1[q(m_E,z_G)\succeq r_D],
\qquad
Y_G=\Pr\{q(m_E,z_G)\succeq r_D\},
\tag{UMRL-017}
$$

with uncertainty, lot identity, custody, calibration validity, and matched
controls included.  Approximate qualified-device cost is

$$
C_{\mathrm{qualified}}=
\frac{C_{\mathrm{wafer}}+C_{\mathrm{process}}+C_{\mathrm{test}}
+C_{\mathrm{packaging}}+C_{\mathrm{scrap}}}{N_{\mathrm{sites}}Y_G}.
\tag{UMRL-018}
$$

No value is published when $Y_G$ is unmeasured or the numerator is incomplete.

## 11. Pangola/biomass material substitution

For required incumbent function vector $f^\star$ and candidate measured vector
$f_c$, qualification uses the same robust-margin calculus as UMRL-004.  Critical
material reduction is reported element by element:

$$
\Delta M_a=M_{a,\mathrm{reference}}-M_{a,\mathrm{candidate}},
\qquad a\in\{\mathrm{Au,Cu,Ag,Li,Co,Ni,REE},\ldots\}.
\tag{UMRL-019}
$$

Mass balance requires

$$
\sum_i m_i^{\mathrm{in}}
=\sum_j m_j^{\mathrm{product}}
+\sum_k m_k^{\mathrm{waste/emission}}+m_{\mathrm{inventory\ change}}.
\tag{UMRL-020}
$$

Biomass carbon can substitute a function, reduce loading, enable recovery, or
support redesign; UMRL-020 forbids treating it as ordinary chemical creation of
unfed metal or rare-earth atoms.

## 12. Bio-oil and accepted liquid-energy service

For saleable fuel or accepted refinery intermediate,

$$
c_{\mathrm{fuel}}=
\frac{C_{\mathrm{feed}}+C_{\mathrm{pre}}+C_{\mathrm{conversion}}
+C_{\mathrm{upgrade}}+C_{\mathrm{H_2/catalyst}}+C_{\mathrm{utility}}
+C_{\mathrm{capital}}+C_{\mathrm{logistics}}+C_{\mathrm{finance}}
-C_{\mathrm{nonduplicated\ coproduct}}}
{m_{\mathrm{accepted}}H_{\mathrm{LHV}}}.
\tag{UMRL-021}
$$

The denominator is accepted delivered energy, not crude liquid volume.

## 13. Fusion electricity

Net power and discounted delivered-electricity cost are

$$
P_{\mathrm{net}}=\eta_{\mathrm{conversion}}P_{\mathrm{fusion}}
-P_{\mathrm{recirculating}}-P_{\mathrm{auxiliary}},
\tag{UMRL-022}
$$

$$
\operatorname{LCOE}_{\mathrm{net}}=
\frac{\sum_t(C_{\mathrm{CAPEX},t}+C_{\mathrm{OPEX},t}
+C_{\mathrm{fuel},t}+C_{\mathrm{replacement},t}
+C_{\mathrm{decommission},t})/(1+r)^t}
{\sum_t E_{\mathrm{net,delivered},t}/(1+r)^t}.
\tag{UMRL-023}
$$

Ignition, plasma gain, or gross heat cannot satisfy UMRL-023 by themselves.

## 14. Finance and interest compression

For debt balance $D(t)$ and contractual rate $r(t)$,

$$
I_{\mathrm{absolute}}=\int_0^T r(t)D(t)\,dt+F_{\mathrm{fees}}.
\tag{UMRL-024}
$$

Reducing principal or duration lowers this integral with fixed terms.  A claim
that the rate or WACC itself falls requires a separately observed risk/market
model; it is never inferred from cheaper technology alone.

## 15. SCM measurement and information boundary

The detailed `จิต–เจตสิก–อภิธรรม`, `อาถรรพ์คอนโทรล`, realm graph,
SCM-1–5, portal, and inter-realm economic formalism is maintained in
`docs/SCM_LOKATHIBODI_MIND_MENTAL_FACTORS_CONTROL_FORMALISM_V0_1_2026-09-28.md`
and its machine-readable Cycle 006 registry.  Those objects use the
`SCM-MATH-001`–`SCM-MATH-019` namespace and remain explicitly fictional or
protocol-level unless their individual empirical gates pass.

For preregistered source label $S$, blinded observation $Y$, and controls $X$,
the empirical null is

$$
H_0:I(S;Y\mid X)=0,
\qquad
H_1:I(S;Y\mid X)>0,
\tag{UMRL-025}
$$

evaluated with frozen scoring, leakage controls, multiplicity control,
adversarial nulls, and independent replication.  Rejecting a local null would
not by itself identify a spiritual, paranormal, biological, or cross-realm
cause.  Fictional/canonical use is typed separately from empirical evidence.

## 16. AI training/service cost

AI replacement first requires a frozen model/task/data/quality contract.  The
same UMRL-007 and UMRL-009 ratios then apply to training or service outputs.  If
only fraction $f$ of baseline cost can receive acceleration $a$, the optimistic
cost reduction is bounded by

$$
G_{\mathrm{total}}\le
\frac{1}{(1-f)+f/a},
\tag{UMRL-026}
$$

before adding any new orchestration, state-preparation, QEC, sampling, or
reconstruction costs.

## 17. New-equation hypothesis contract

Each quantitative declaration is an explicit tuple of value, kind, unit,
dimension vector, domain sort, evidence type, and provenance:

$$
q=(v,k,u,\mathbf d,\sigma,\tau,\pi),
\qquad
\Gamma\vdash q:\tau@\sigma.
\tag{UMRL-031}
$$

Real numeric quantities require a registered unit and exact rational
dimension vector; fictional canon quantities use canon-scoped types and do
not receive SI dimensions by resemblance. Functions preserve their declared
sort. A cross-sort map must be explicitly declared and independently
validated; there is no implicit cast. This is a property of the project's
formal interface, not a physical law. The bounded Cycle 008 checker audits
three selected real-model equations and the SCM additions while leaving the
remaining registry variables unclassified. The Cycle 006 registry remains a
frozen UMRL-0.1 snapshot.

A candidate equation is the typed object

$$
h=(F,\Theta,\mathcal D,\mathcal A,\mathcal C,\mathcal L,
\mathcal O,\mathcal F,\Pi),
\tag{UMRL-027}
$$

where $F$ is the symbolic object, $\Theta$ parameters, $\mathcal D$ domain,
$\mathcal A$ assumptions, $\mathcal C$ dimensional/symmetry/conservation/
causality constraints, $\mathcal L$ limiting cases, $\mathcal O$ discriminating
observables, $\mathcal F$ falsifiers, and $\Pi$ provenance.  Promotion requires

$$
\operatorname{Promote}(h)=
\bigwedge_{q\in\{\mathrm{dimensions,symmetry,conservation,causality,limits,
heldout,counterexample,independence}\}}\operatorname{Pass}_q(h).
\tag{UMRL-028}
$$

This is a conjunction: elegance or fit cannot compensate for a failed physical
constraint.  A failed candidate remains in the discovery ledger with its
counterexample and validity boundary.

## 18. Research prioritization without capital authorization

For a bounded protocol $\pi$, its expected information gain is

$$
\operatorname{EIG}(\pi)=
H[p(\theta\mid D)]-
\mathbb E_{Y_\pi}\!\left[H[p(\theta\mid D,Y_\pi)]\right].
\tag{UMRL-029}
$$

A research queue may rank reproducible, already-authorized protocols by
$\operatorname{EIG}$, blocker reduction, cost, time, and risk.  This ranking is
not a funding, purchase, fabrication, provider-job, or human-study authorization.

## 19. UQPU Mission Closure Equation

Every goal $g$ has a robust margin $\Delta_g$, an evidence predicate $E_g$, a
provenance predicate $P_g$, and a non-claim boundary $N_g$.  The project-specific
mission closure equation is

$$
\boxed{
\operatorname{UMCE}(x,\Gamma)=
\bigwedge_{g\in\mathcal G}
\left[
\inf_{\omega\in\mathcal U_{g,1-\alpha_g}}
\Delta_g(x,\omega)\ge0
\right]
\land E_g(\Gamma)\land P_g(\Gamma)\land N_g(\Gamma)
}
\tag{UMRL-030}
$$

UMCE uses logical conjunction rather than a weighted sum.  Superior cost cannot
cancel failed safety, missing function, inadequate output quality, hidden
infrastructure, or the wrong evidence type.  Before all terms are measured and
pass, UMCE is **open**, not false proof of impossibility and not evidence of
success.

## 20. Twelve-lane interface

| Lane | Primary mathematical objects |
|---|---|
| A | UMRL-004–009, 012, 015, 031 |
| B | UMRL-001–003, 011–012, 031 |
| C | UMRL-002–008, 013–014, 031 |
| D | UMRL-004–005, 017, 031 |
| E | UMRL-003–005, 019–023, 031 |
| F | UMRL-003, 006–009, 021, 023–024, 031 |
| G | UMRL-002–003, 017–018, 031 |
| H | UMRL-009–010, 024, 029–031 |
| FND/EQN | UMRL-001, 027–031 |
| SCM | UMRL-001, 025, 028, 031 |
| AI-COST | UMRL-004–009, 026, 031 |
| QOS/QSVT | UMRL-004–005, 015–016, 031 |

## 21. Continuous discovery ledger

Every synchronized cycle must record useful intermediate mathematics even when
the main target remains blocked.  Valid entries include:

- a definition that removes ambiguity;
- an invariant, lemma, proof obligation, or certified bound;
- a counterexample or impossibility result;
- a dimensional, symmetry, conservation, or limiting-case rejection;
- an uncertainty reduction or identifiability result;
- a null result or failed equation candidate;
- a new observable, falsifier, benchmark, or experiment design;
- a cross-lane interface mapping an equation to measurable fields.

Each entry records `equation_id`, version, owner lane, status, assumptions,
variables/units, provenance, evidence type, tests, uncertainty, falsifier,
downstream goal links, and non-claims.  History is retained; a superseded or
falsified equation is never silently deleted.

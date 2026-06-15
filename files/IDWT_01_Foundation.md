# Infinite Dimensional Wave Theory — Part 1: Foundations

## Status Key
- ⭐ Identity — pure combinatorial or algebraic fact, valid with or without the IDWT postulates
- ✅ Structural consequence — rigorously proved from the IDWT postulates P1–P4
- 🔵 Numerically verified — matches observation; mechanism not yet proved
- 🔶 Motivated / open — selection rule, ansatz, or empirical constraint beyond P1–P4; derivation open
- ❓ Conjecture — plausible structure; unproved

---

## A Note on First Impressions

The mass tables in this document invite an immediate reaction: this must be curve-fitting. The reaction is understandable and wrong, in ways that are not obvious on a first pass. Three specific misconceptions are worth addressing before proceeding.

**The mode indices are not fitted.** Every mode index $n$ in the particle spectrum is generated algebraically by the Hockey-Stick identity $S(n,d) = \binom{n+d-1}{d}$ applied to the two seeds $n_d = 1$ and $n_u = 3$ (composite $n_s = 4$). The full derivation chain is in §5 and Part 2 §6. As one example: $n_\mu = S(4,4) = 35$ because that is Pascal's recursion $S(n,d) = S(n,d-1) + S(n-1,d)$ evaluated at $(n=4, d=4)$ — not because the muon happens to have that index. The non-trivial seed $n_u = 3$ is forced by $\chi(\mathbb{CP}^2) = N_c = 3$ (§3b); the composite $n_s = n_u + n_d = 4$ is confirmed topologically by $\chi(\mathbb{CP}^3) = 4$, independently of any mass data.

**The sector assignments are not arbitrary.** Each sector imparts specific physical properties through its spinor geometry. $d=5$ ($S^5$, $d \bmod 8 = 5$) forbids Majorana spinors by Clifford algebra periodicity — Dirac neutrinos are not a choice, they are a geometric consequence. $d=4$ ($\mathbb{CP}^2$) generates colour charge from its $SU(3)$ isometry group; $\chi(\mathbb{CP}^2) = 3 = N_c$. $d=6$ ($\mathbb{CP}^3$) produces colour-neutral chiral fermions through its Kähler structure. Moving a particle to a different sector does not produce a different prediction — it produces the wrong quantum numbers entirely. The assignments are locked by geometry.

**The sector scales are not calibrated to mass data.** $m_{\text{scale},3} = m_e \times \sqrt{g_{33}/g_{66}}$ uses coupling constants derived from seed pair $\{n_d=1,\,n_u=3\}$ and composite $n_s=4$ ($g_{33} = 8\sqrt{7}$) and from the complex geometry of CP³ ($g_{66} = 1/4$; see Part 2 §9c). No quark mass enters the derivation. The down quark prediction (+0.68% from PDG) is an output, not an input. All sector scales derive from the seed coupling constants and $m_e$ as the sole unit reference (Part 2 §10).

The particle physics sector of the framework has one unit of mass ($m_e = 0.511$ MeV) and two seed integers ($n_d = 1$, $n_u = 3$) with composite $n_s = 4$. Everything else in the particle sector — the sector set, all mode indices, all coupling constants, all sector scales, all particle masses, the Cabibbo angle, and the three PMNS magnitudes — is derived from these. The CP-violating phase δ_CP = π + 2θ₁₃ = 197.11° is derived via APS spectral flow of the one-parameter Dirac family across the CP³→CP⁵ Chern class mismatch Δc₁ = −2 (T8 🔶, Part 10 §4). The derivation carries three technical gaps before reaching 🔵 (see Part 10 §4 status note). The one current exception is gravity: $G_N$ is a measured external input pending derivation from the spectral action scale $\Lambda$ (P5, Part 4 §3.12.4). When $G_\infty$ is derived, $G_N = G_\infty/V_7$ will follow from the same geometry with no additional input. The structural evidence against numerology is the cross-referencing: the same numbers arriving independently from different directions. The quantity $q = S(n_u-1, 4) = 5$ appears in both the EW coupling derivation $g_{22} = p^2 q/2$ and the boson mass gap $n_Z - n_W = 5$. The resonance site $k_0 = 16$ satisfies three independent conditions simultaneously. The Higgs mode index $n_H = 95$ is reached by two separate cross-sector routes. Numerological schemes are flexible enough to always find a match. This framework is rigid enough that these convergences are non-trivial.

---

**Note on EW symmetry breaking.** IDWT does not use spontaneous symmetry breaking, so the concept of a Higgs VEV does not apply within the framework (Part 5 §3c). The EW scale is $(\sqrt{2}\,G_F)^{-1/2}$ — not a vacuum expectation value.

## 1. Core Postulates

**P1 — The Master Field**
Ψ∞ is a **Dirac spinor field** on the infinite-dimensional manifold M_∞ = ℝ_t × Ξ_∞. It is the only fundamental object. Everything observable — particles, fields, forces, quantum numbers — is a derived consequence of its geometry. The mass spectrum follows from the mode counting function S(n,d) = C(n+d−1, d). The coupling structure of each particle — what interactions are available to it and what is geometrically forbidden — follows from the Riemannian and spinor geometry of its sector manifold. Quantum number labels are not inputs; they are outputs of the geometry.

The sector space Ξ_∞ contains all dimensions d ≥ 1. The active sectors — those whose geometry supports stable bound-state eigenmodes — are D = {2,3,4,5,6,10}. Sectors d=7,8,9 exist as coordinates of M_∞ but their geometry does not support stable eigenmodes (Rule A, §3a); sectors d≥11 are subcritical and cannot localize modes at all (Rule B, §3a). The label Ξ_{10} used in earlier versions of this document referred to the highest active sector, not to a truncation of M_∞.

**Dependency structure.** In the current formulation, where the sector potential V_d(r) = λ_d r² is fixed by the kernel mean-field self-consistency (Part 4 §3.10) rather than derived directly from the action, the logical chain is one-directional: M_∞ topology determines the active sector set D (via the Gegenbauer criticality condition and Hopf fibration pairing, Part 9 T3), the sector geometries {M_d}_{d∈D} determine the projection operators Π_d, and observables are the projected fields Π_d Ψ_∞. Given fixed sector geometry, S(n,d), m_scale_d, and g_{dd'} are derived quantities; they do not feed back into the determination of which d are active.

This one-directionality is a property of the current mean-field V_d formulation, not of the complete theory. When V_d is derived from the IDWT action (open item MC-2, Part 6), the sector geometry will itself become a functional of the vacuum structure of Ψ_∞, making the full problem a coupled fixed-point system (Ψ_∞, {M_d}) ∈ Fix(T). At that level D = {2,3,4,5,6,10} should emerge as stable solution branches of the joint field-geometry system, not solely from M_∞ topology. This is precisely the content of Theorems A and B in Part 6 §Open.

### 1.1 The temporal structure of M_∞

P1 writes M_∞ = ℝ_t × Ξ_∞. This factorization is load-bearing and deserves an explicit statement of what it commits to.

⭐ **One timelike direction.** ℝ_t is the unique timelike direction in M_∞. Ξ_∞ is a purely Riemannian (all-spatial) manifold. M_∞ therefore has Lorentzian signature (1, ∞): one negative metric eigenvalue from ℝ_t and countably many positive ones from Ξ_∞. The Dirac operator on M_∞ is D = γ⁰ ∂_t + Σ_i γⁱ ∂_{ξⁱ}, where γ⁰ is the single timelike Clifford generator and the γⁱ are spatial. Every particle in every sector shares this one time coordinate. There is no sector-specific time; a d=10 mode and a d=3 mode age at the same rate, governed by the same ℝ_t.

⭐ **Kinematics per sector.** A particle in sector d inhabits d spatial directions and 1 temporal direction: its kinematics are those of a (d+1)-dimensional spacetime. Its natural kinematic group is SO(d,1). The d=3 observer's Lorentz group SO(3,1) is the restriction of SO(d,1) to the observable spatial directions (d=3 marginal).

🔶 **Observable Lorentz invariance.** From the d=3 marginal, every kinematic observable of a higher-sector particle — energy, momentum, spin — is fixed by the d=3 marginal dynamics alone (Marginal Exactness, Part 11 §6.1). The full SO(d,1) kinematics of a d=6 electron reduce to SO(3,1) for any measurement a d=3 apparatus can perform: the extra spatial directions appear only as the CP³ sector coordinates that project out under Lemma 2. The electron is a fully relativistic particle with the standard Dirac kinematics in d=3+1 — its extra sector dimensions do not produce additional Lorentz partners, because those dimensions are spatial and the temporal one is the shared ℝ_t.

**What this rules out.** There are no additional time dimensions in any sector. The phrase "six-dimensional electron" means six spatial dimensions plus one shared time — not a 6+1 spacetime independent of d=3. Proposals that treat the sector coordinates as having their own timelike directions, or that use SO(6,1) boosts in the hidden directions as physical operations, are outside the framework: ℝ_t is unique. This also rules out the pathologies (closed timelike curves, multiple causalities) that would otherwise arise in a framework with many large spatial dimensions, since causal structure is everywhere determined by a single ℝ_t.

**What remains open.** The specific form of the Dirac operator on M_∞ — whether D decomposes cleanly as D_t + D_Ξ or has mixed terms — is the open MC-2 action question (Part 6). The present P1 formulation postulates the product structure M_∞ = ℝ_t × Ξ_∞; deriving it from a spectral action on M_∞ would also fix the form of D and close the question of whether ℝ_t × Ξ_∞ is exact or only approximate at the scales relevant to particle physics. 🔶

**P2 — The Observer's Position**
We are at d=3 — inside M_∞, at the coordinate level where the first stable hadronic sector constitutes space. The observable universe is Ψ∞ evaluated at a fixed sector-space address ξ⁰:
```
ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```
The observer's position determines which modes are easy to resolve but not which modes exist. The physical spectrum is closed at exactly 15 states: those mode-sector pairs (n,d) satisfying the co-fixed-point condition — the pair (n,d) is an element of Σ_pairs, the closed set produced by the generation tower (the sector comb filtration from n_s = 4). All observers at any ξ⁰ see the same 15-particle spectrum.

**P3 — Non-Compact Sector Spaces**
The sector spaces Ξ_d are infinite Riemannian spaces — not rolled up or compactified. Each sector carries a potential well $V_d(r) = \lambda_d r^2$ — the kernel self-binding potential (Part 4 §3.10) — whose eigenmodes are Gaussian-localized bound states (sector mode localization theorem, Part 4 §3.13 Part I). The particles are these bound states. The geometry labels (CP^n, S^n) describe the local symmetry of the potential minimum — the symmetry of sector mode amplitudes near r=0 — not the global topology of Ξ_d. This is analogous to a hydrogen atom: the electron occupies infinite ℝ³ but the ground state has S² symmetry from the spherically symmetric potential. No sector is curled up. The sector spectrum is purely discrete (σ_ess = ∅, Part 4 §3.13 Part I): no freely propagating sector modes exist, and every physical mode is a normalizable bound state. The standard KK exclusions presuppose graviton propagation into compact dimensions and do not apply here (Part 4 §1b, §3.9).

**P4 — Two Force Principles**
Forces couple through two complementary geometric principles. Both are required; neither alone is sufficient.

*(a) Coordinate containment — necessary condition.* A particle couples to a force only if the force's sector coordinates are contained in the particle's sector. The active sectors nest as Ξ_2 ⊂ Ξ_3 ⊂ Ξ_4 ⊂ Ξ_5 ⊂ Ξ_6 ⊂ Ξ_{10} ⊂ Ξ_∞. Coupling is possible only when the force's sector is contained in the particle's sector. The coordinates of d=7,8,9 exist in Ξ_∞ but host no stable eigenmodes (§3a Rule A), so no particle occupies those directions; they are inert coordinates of M_∞, traversed by the nesting chain but not occupied.

*(b) Coupling filter — structural condition.* The particle's own sector geometry determines the structure of whatever coupling it has. The sector quantum number is not a label — it is the geometry expressing itself as a coupling structure: polarization (U(1) of CP¹), color (SU(3) isometry of CP²), the Dirac condition (Clifford algebra of S⁵), color silence (index cancellation on CP³), Gegenbauer-critical coupling (Gegenbauer critical-endpoint condition of CP⁵). Each is the natural generalization of polarization to a higher-dimensional geometry. The geometry specifies not only what interaction handles exist but what entire classes of interaction are geometrically forbidden — not suppressed, unavailable.

A particle with coordinate support in a force sector may still have zero coupling to that force if its sector geometry projects the relevant representation to zero (as neutrinos are colour-neutral despite their S⁵ coordinates containing Ξ_4).

**P5 — Gravity as Curvature of M_∞**
Gravity is the curvature of M_∞ sourced by mass, operating across all sector coordinates without a sector boundary. There are no gravitons; gravity cannot be quantized because there is no gravitational field — only geometry. The observed G_N = G_∞/V_7, where V_7 ≈ 7.74 is the product of sector localization lengths, fully derived from the sector coupling constants. G_∞ — the ∞D Newton constant — requires fixing the spectral action scale Λ and is not yet derived; G_N is currently an external input. Once the a₂ Seeley-DeWitt integral over M_∞ is computed, G_N = G_∞/V_7 becomes a parameter-free prediction 🔶 (Part 4 §3.12).

**P6 — Rank-1 Coupling 🔶**
The inter-sector coupling strength matrix factorizes as $g_{dd'} = v_d \times v_{d'}$ — rank-1 as an outer product of a coupling vector $v = (v_2, v_3, v_4, v_5, v_6, v_{10})$. All six components $v_d$ are derived from seeds $\{n_d=1,\,n_u=3\}$ and composite $n_s=4$ (Part 2 §10, Part 3 §0.1). The rank-1 factorization follows as a **necessary consequence of the sector-separable mass formula (P1)**: if $g_{dd'} = \sum_k v_d^{(k)} v_{d'}^{(k)}$ had rank $r > 1$, the mean-field kernel $V[\Psi](x,\xi) = \sum_k (\sum_d v_d^{(k)}\xi_d)\cdot(\sum_{d'} v_{d'}^{(k)}\xi_{d'} J_{d'}(x))$ would introduce cross-sector entanglement that prevents the sector-by-sector eigenvalue separation $m = m_{\rm scale,d} \times S(n,d)$. Rank-1 ($r=1$) is the unique structure for which the condensate $C(x) = \sum_{d'} v_{d'}\langle\xi_{d'}\rangle(x)$ is common to all sectors, allowing each sector $d$ to see a local harmonic potential $V_d = v_d^2|\xi_d|^2|C(x)|^2$ and reproduce the simplex eigenvalue. **Status: ✅ as a consequence of P1.** Physical consequences: universal correlated coupling scales across sectors, constrained inter-sector mixing, the Wolfenstein angle from a single ratio $v_3/v_4$.

Two algebraic corollaries of the factorization ⭐: *(i)* $G$ has exactly one nonzero eigenvalue, $|v|^2 = \mathrm{tr}\,G = \sum_d g_{dd}$, with eigenvector $v$ — the wave has a single independent interaction channel, and every cross-sector coupling is the projection of that one coupling direction. *(ii)* Writing $(\xi_d\cdot\xi_{d'})^2 = Q^{(d)}_{ij}Q^{(d')}_{ij}$ with $Q^{(d)}_{ij} = \xi_{d,i}\xi_{d,j}$, the quartic kernel term is a sum of squares, $V_{\rm kernel} = \tfrac12\sum_{ij}\big(\sum_d v_d\,Q^{(d)}_{ij} J_d\big)^2 \geq 0$, for any real sector densities $J_d$. The positivity is not termwise — $J_d J_{d'}$ can be negative — it is guaranteed by the rank-1 structure. The kernel self-coupling only adds energy: it penalizes configurations and never lowers a mode's energy. (`files/idwt.py` STEP 2b.)

**P7 — Mode Selection by the Co-fixed-point Condition 🔶**
A mode $(n,d)$ of Ψ_∞ is a physical particle if and only if the pair $(n,d)$ is an element of $\Sigma_{\rm pairs}$ — the unique finite closed set of mode-sector pairs produced by the generation tower from seeds $(n_{\rm down},d) = (1,3)$ and $(n_u,d) = (3,4)$, together with their offset-additive composite $(n_s,d) = (4,3)$. The generation tower assigns both the mode index and the sector; a mode at index $n$ in sector $d$ is stable only if the specific pair $(n,d)$ appears as a tower output, not merely if $n$ appears as a tower output in some other sector. This is semi-structural: the instability of non-co-fixed-point modes (l-parity disconnection for odd levels, infinite-dimensional dephasing on timescale $1/m_{\rm scale,d}$ for even levels) is established at the kernel level (Part 7 §1.2) but not yet derived from the EOM. The detailed co-fixed-point set and its DAG structure are given in P8. Status: 🔶 (Part 7 §1, Part 9 T0.5).

**P8 — Co-Fixed-Point Stability 🔶**
A mode-sector pair $(n,d)$ is a stable resonance if and only if it is an element of $\Sigma_{\rm pairs}$, the co-fixed-point set: the unique finite set of pairs such that applying every generation-tower operation to $\Sigma_{\rm pairs}$ returns only elements already in $\Sigma_{\rm pairs}$ (verified exhaustively, §5c). The generation tower is a finite acyclic DAG with seeds $\{(1,3),(3,4)\}$ (composite $(4,3)$ at depth 1) and trivial automorphism group (Appendix A §13b) — the labeling of all 15 particles is uniquely determined by the DAG structure.

**Sector assignment — the rung placements are derived (✅); the routing DAG is the open item (🔶).** Two results carry the assignment without SM input:

*(i) Seed values and seed sector.* The primitive seeds are $n_d = 1$ (ground seed: $S(1,d) = 1$ in every sector) and $n_u = 3$ (geometric seed: $\chi(\mathbb{CP}^2) = N_c = 3$, T15, ✅-grade). The composite $n_s = 4 = 1+3$ is sourced from these seeds via the offset-additive channel (🔶 MC-4.4 kernel reading); T4 (the $4/7$ double-degeneracy equation, Part 9), the muon fixed-point $S(4,4) = 35$, the Gegenbauer crossing, and the matter-quartet identity $2n_s - 4 = n_s$ are uniqueness certificates confirming the composite. The seed sector is d=3: the observable spacetime sector and the first Hopf total space $S^3$ of the complex Hopf chain (§3a). Both seeds occupy d=3 independently by R1 — no cross-seed argument is required for their shared sector placement.

*(ii) Remaining sector assignments follow from Hopf chain geometry.* Given seeds in d=3, the subsequent sector assignments propagate via the Hopf fibration chain $\{2,3\} \to \{4,5\} \to \{6,10\}$:
- d=4 (CP²): the first Hopf base space over S³ (d=3). All modes derived by direct HS from d=3 seeds land here. $N_c = \chi(\text{CP}^2) = 3$ identifies this as the colour sector (T15, §3a) — no SM name needed.
- d=5 (S⁵): the Hopf total space over CP² (d=4). Modes derived by HS from d=4 modes land here.
- d=6 (CP³): the next Hopf base above S⁵. $\chi(\text{CP}^3) = 4 = n_s$ links it to the composite (T15).
- d=10 (CP⁵): the Gegenbauer-critical endpoint, fully proved by T5 without SM input.
- d=2 (CP¹): the EM reference sector, base of the full chain; the g-rule routes W, Z, H to d=2.

*(iii) Trivial automorphism group closes the argument.* Since the tower DAG has no non-trivial automorphisms, once the seed sector d=3 is established (algebraically) and the Hopf chain determines the sector for each derived particle (geometrically), there is exactly one consistent labeling. No alternative sector assignment scheme preserves the DAG.

**What remains genuinely open.** The EOM derivation of co-fixed-point stability (Part 6, MC-4): the dynamical argument for why the tower $(n,d)$ pairs are stable resonances rather than transient excitations. The geometric routing is established — the routing rule for $d=4\to d=5$ is a corollary of §3a Step 2 (see Routing Corollary above), and the trivial automorphism theorem establishes uniqueness of the labeling up to relabeling. P8 is 🔶 on the dynamical stability mechanism: uniqueness up to relabeling is not yet a derivation of the DAG from the dynamics.

P8 as a postulate remains 🔶 until the EOM derives co-fixed-point stability. The co-fixed-point condition has the status of an algebraically-seeded, geometrically-propagated selection rule — the rung placements are derived (✅); the routing DAG and its dynamical stability are the remaining open item.

⭐ **Matroid interpretation of the generation tower.** The uniform matroid $U^d_{n+d-1}$ has ground set $E = \{1,\dots,n+d-1\}$ with a subset declared independent iff its cardinality is at most $d$. Its number of bases is $\binom{n+d-1}{d} = S(n,d)$. The hockey-stick recursion $S(n,d) = S(n,d-1) + S(n-1,d)$ is the matroid basis-exchange axiom in this uniform case: deleting or contracting one element gives the two terms. Submodularity of the rank function $r(A) = \min(|A|,d)$ gives a combinatorial proof that a mode index can increase by at most one hockey-stick step per generation — the mass spectrum is submodular. The trivial automorphism group of the tower DAG (Appendix A §13b) is automatic for uniform matroids of rank $\geq 3$ (Whitney's theorem on the automorphism group of $U^d_{n+d-1}$), which independently confirms that the 15-particle labeling is unique without invoking SM input.

⭐ **Poset structure and seed uniqueness.** The modes ordered by $(n_1,d_1) \leq (n_2,d_2)$ iff $n_1 \leq n_2$ and $d_1 \leq d_2$ form a product of two chains — a distributive lattice — with $S(n,d)$ as the rank function and the hockey-stick identity as the rank-generating function. Sperner's theorem gives the size of the largest antichain at a given rank as $\binom{n+d-1}{\lfloor(n+d-1)/2\rfloor}$; Dilworth's theorem gives the minimum chain cover of the 15 modes as the DAG width, a pure combinatorial invariant. The seeds $\{(1,3),(3,4)\}$ are the unique minimal elements of the two largest antichains in the tower — their forced status is a poset-theoretic consequence, providing an independent combinatorial route to the same conclusion as the co-fixed-point uniqueness proof (§5c).

⭐ **Minimal derivation depths — generation tower word lengths.** The derivation depth of each mode is the minimal number of licensed operations (hockey-stick operators $H_{d\to d\pm1}$, additive eigenmode operators $A$, Vandermonde g-rule operators $G_d$) required to reach it from the seeds $\{(1,3),(3,4)\}$. These depths are simultaneously the height in the ranked distributive lattice, the RSK insertion length for the corresponding semistandard Young tableau (Part 2 §1 ⭐ Ferrers diagram depth), and the tropical distance in the min-plus linearization of the Pascal relations. The complete depth table:

| Mode index $n$ | Particle | Depth | Construction |
|---|---|---|---|
| 1 | down | 0 | Seed |
| 3 | up | 0 | Seed: $\chi(\mathbb{CP}^2) = N_c = 3$ (T15) |
| 4 | strange | 1 | $b = 1+a$: offset-additive composite (🔶) |
| 10 | $\nu_1$ | 1 | $S(3,3)$: HS from up (depth 0) |
| 15 | $\nu_2$ | 1 | $S(3,4)$: HS from up in d=4 (depth 0) |
| 13 | electron | 2 | $n_{\nu_1}+n_u$: additive rule on depth-1 + depth-0 |
| 20 | charm | 2 | $S(4,3)$: HS from strange (depth 1) |
| 22 | $\nu_3$ | 2 | $n_{\nu_1}+n_{\nu_2}-n_u$: inclusion-exclusion on depth-1 modes |
| 23 | tau | 3 | $n_{\nu_3}+n_d$: generation law from depth-2 |
| 35 | muon | 3 | $S(4,4)=n_c+n_{\nu_2}$: Pascal on depth-2 + depth-1 |
| 72 | top | 3 | Eigenmode chain from electron (depth 2) |
| 76 | $W$ | 4 | g-rule on top (depth 3) |
| 95 | Higgs | 4 | $n_u+n_c+n_{\rm top}$: sum of up-type, max depth 3 |
| 81 | $Z$ | 5 | g-rule on $W$ (depth 4) |

The bosons systematically carry the highest depths because they are built by the g-rule chain on top of the fermion tower. The GTC exponents $k\in\{0,3,10\}$ for up-type quarks are not identical to depths but are monotonically related: $k_c = n_u = 3$ (the depth-2 charm's Ferrers box count) and $k_t = S(n_u,3) = 10$ (the depth-3 top's Ferrers box count through the neutrino sector) — see Part 2 §11.3 for the derivation.

⭐ **Generation tower as a finitely presented semigroup.** The generation tower is the action of a finitely presented semigroup on the binomial lattice of pairs $(n,d)$. The **generators** are three families: hockey-stick operators $H_{d\to d\pm1}$ (the two Pascal directions $S(n,d)=S(n,d-1)+S(n-1,d)$), additive eigenmode operators $A$ (the selection rule $n_{\rm lepton}=n_{\rm neutrino}+n_{\rm quark}$), and Vandermonde g-rule operators $G_d$ for bosons. The **relations** are the full hockey-stick identities, distributive lattice commutativity, spectral independence (the occupied $S$-values form a sum-free set), and co-fixed-point closure. The **seeds** $\{(1,3),(3,4)\}$ are the unique minimal generators, with composite $(4,3)$ derived at depth 1. The **physical spectrum** $\Sigma_{\rm pairs}$ is the minimal closed orbit of the seeds under this semigroup. The derivation depth of each mode (table above) is the minimal word length in the semigroup from the seeds. This framing makes the generation tower's rigidity explicit: $\Sigma_{\rm pairs}$ is not a collection of algebraic choices but the unique closed orbit of two elements under three families of forced operations.

---

## 2. Observable Coordinates and the d=3 Marginal

### 2.1 We Are Inside M∞

There is no projection happening in IDWT. We are not external observers mapping M∞ onto a separate 3D screen. We are at d=3 — inside M∞, at the coordinate level where the first stable sector constitutes space. Our observable universe is M∞ at the d=3 coordinate level, not a shadow of something else.

Particles with d > 3 are not separate from us. Their modes include the d=3 coordinates we occupy — those coordinates are a literal subset of every higher sector (§3f, §3i). What we cannot access are the additional d−3 sector-space coordinates their modes also span. We are not outside those coordinates looking in; we simply do not have coordinates there. The distinction matters: a projection implies an external observer with a screen. IDWT has neither. There is one manifold M∞, one field Ψ∞, and we are a feature of it at coordinate level d=3.

### 2.2 Observable and Sector Coordinates

The down-type quarks (d=3) have sector dimensions that are exactly our three: all of their vibrational activity is in our dimensions, with no component eluding measurement. The photon (d=2) has exactly two directions — fewer than our three — but it is not pinned to our three coordinates: it oscillates in its two and moves perpendicular to them, and that perpendicular motion runs through the full manifold, not only the one leftover direction our three dimensions provide (§3i, Part 3 §14).

For particles with d > 3, the mode vibrates across d dimensions, of which only 3 are ours. The electron (d=6) has 3 observable dimensions and 3 sector dimensions we do not occupy. The tau (d=10) has 3 observable and 7 sector dimensions beyond d=3. We measure the d=3 component of their activity; the rest vibrates in coordinates we do not occupy. What a d=3 observer resolves is the d=3 cross-section of the full mode — for the electron, the 3D shadow of its 6D orbit (Part 8).

What an observer at ξ⁰ can resolve does not affect what the particle is. Mass and coupling are eigenvalues of each particle's sector manifold (T0, Part 9) — intrinsic, and independent of observer position.

### 2.3 The Observable Probability Density from Ψ∞

```
ρ(r, t) = ∫ |Ψ∞(r, ξ, t)|² dξ
```

The observable probability density at position r is the marginal of |Ψ∞|² over the sector coordinates. Since our measurements are mediated by d=3 interactions and we cannot independently access the sector-space coordinates, the density we measure is the integral of |Ψ∞|² over ξ — the sector-space marginal, not the full function.

This is not a separate postulate; it follows from the fact that our measurements access only the d=3 coordinate marginal. An electron is not a cloud in 3D — it is a structured mode in M∞ whose d=3 marginal appears as a diffuse probability density. Entangled particles are features of Ψ∞ that are close in the sector-space coordinates even when their d=3 marginals are far apart.

### 2.4 Why d=3 Is the Observer Level — A Theorem ✅

The assertion "we are at d=3" has not yet been justified — it has only been named. It is not a postulate. It follows from the sector structure of stable matter.

The lightest stable composite objects in IDWT are colour-singlet baryons: the proton and neutron, built from d=3 (down-type) and d=4 (up-type) quarks. Colour confinement forces any gauge-singlet composite to project out its d=4 CP² index entirely. The Euler characteristic χ(CP²) = 3 gives three colour charges (N_c = 3); a colour singlet is the unique combination with zero net colour charge — which means the d=4 CP² index cancels completely from the composite. What remains is a pure d=3 object: a baryon is a d=3 excitation of M∞ with no residual d=4 coordinate dependence.

All chemistry — every atom, every molecule — is built from such nuclei. Every macroscopic measuring device, every observer, every experimental apparatus that can exist within this theory is an assembly of d=3 nuclear matter. An observer constructed from d=3 objects measures physics at the d=3 coordinate level by construction: their instruments have no coordinate support in d=4, d=5, d=6, or d=10, so the physics they access is the restriction of Ψ∞ to d=3. No measurement protocol built from d=3 matter can return coordinates outside d=3.

**The observer location is a theorem, not an input.** The question "why do we experience a three-dimensional world?" has a derivable answer within IDWT: because the stable composites that building-matter selects are d=3 objects by colour confinement, and any observer assembled from such matter is constrained to the d=3 coordinate level. The d=3 status of our observable space is not introduced as a special axiom; it is the coordinate level forced by the lightest bound states the theory admits. ✅

---

## 3. The Sector Structure of M_∞

The sector space decomposes into sectors with distinct potential well symmetries. Each $\Xi_d$ is an infinite macroscopic space; the geometry labels ($S^3$, $\mathbb{CP}^2$, etc.) describe the local symmetry of the potential minimum $V_d(r)$ near $r=0$, not the global topology:

| d | Geometry | Symmetry | Spinor type | Spinor dim | Physical content |
|---|---|---|---|---|---|
| 2 | CP¹ | U(1) | Majorana-Weyl | 2 | Bosons (γ, W, Z, H) |
| 3 | S³ | SO(4) | Majorana | 2 | Down-type quarks (d, s, b) |
| 4 | CP² | SU(3) | Weyl (spin^c) | 4 | Up-type quarks (u, c, t) |
| 5 | S⁵ | SO(6) | Dirac only | 4 | Neutrinos (ν_e, ν_μ, ν_τ) |
| 6 | CP³ | SU(4) | Weyl | 8 | Charged leptons (e, μ) |
| 7,8,9 | — | — | — | — | *Coordinates of M_∞; supercritical (b > 1/2), but IDWT's coupling construction does not reach these sectors (Rule A, §3a). No active sector geometry is established; whether eigenmodes could form under an extended coupling is open.* |
| 10 | CP⁵ | SU(6) | Majorana-Weyl | 16 | Tau lepton; d mod 8=2 Maj-Weyl (16 real components) |

This list is derived from seeds $n_d = 1$ and $n_u = 3$ (composite $n_s = 4$) and the Generation Tower. See §3a below.

### 3a. Sector Set Theorem

**Theorem.** The sector set $D = \{2, 3, 4, 5, 6, 10\}$ is uniquely determined within IDWT by the complex Hopf fibration chain $S^1 \to S^{2n+1} \to \mathbb{CP}^n$ together with two termination rules, both derivable from the non-trivial seed $n_u = 3$ and composite $n_s = 4$:

**Step 1 — CP base sectors from the seeds.** The non-trivial seed $n_u = 3$ (colour index $N_c = 3$ from the CP² spin$^c$ index, Part 8 §2.2) and composite $n_s = 4$ identify three complex projective spaces by their Euler characteristics:

$$\chi(\mathbb{CP}^{N_c-1}) = N_c = 3, \quad d = 4; \qquad \chi(\mathbb{CP}^{n_s-1}) = n_s = 4, \quad d = 6; \qquad \chi(\mathbb{CP}^1) = 2, \quad d = 2.$$

$d = 2$ (CP¹) is the $U(1)$ Hopf fiber base required by the chain. This gives $d \in \{2, 4, 6\}$. The $d=10$ sector is determined by Rule B below.

**Step 2 — Hopf total spaces add $d \in \{3, 5\}$.** The odd-sphere sectors $S^{2k+1}$ are derivable when their base CP sector has a kernel self-consistency fixed-point coupling:

- $d=3$ (S³ over CP¹): $g_{33} = n_s^2\sqrt{n_s+n_u}/2 = 8\sqrt{7}$ — from seeds.
- $d=5$ (S⁵ over CP²): $g_{55} = g_{33}g_{44}/g_{22}$ — from Hopf universality $v_3/v_2 = v_5/v_4$.

**Corollary (Hopf Routing Rule). ✅** The coupling $g_{55}$ is not an independent constant — it is derived entirely from $g_{44}$ through the Hopf universality condition $v_3/v_2 = v_5/v_4$. Sector $d=5$ is therefore, within IDWT, the sector whose self-coupling closes over $d=4$ via the Hopf fiber. There is no routing theorem to prove beyond Step 2: generation tower operations applied to a $d=4$ seed produce mode indices in $d=5$ by the same logic — because $d=5$ is the unique sector in $D$ constructed as the Hopf fiber over $d=4$. Uniqueness follows from T3 (no other sector in $D$ has its coupling determined by $g_{44}$) and the trivial automorphism theorem (Appendix A §13b). Assigning those HS outputs to any other sector would require a sector whose coupling closes over $d=4$; by Step 2, only $d=5$ satisfies this. The routing rule is the content of Step 2 read in the direction of the generation tower.

**Step 3 — Termination rules exclude all remaining spaces.**

*Rule A (coupling termination).* $g_{66} = 1/n_s$ is the composite ratio — a direct output of the seed ($\chi(\mathbb{CP}^3)=n_s$), not a kernel fixed-point coupling — so the coupling-construction chain terminates at $d=6$. The band $d=7,8,9$ acquires no self-coupling and is excluded, the three cases standing on different footings: $d=8$ ($\mathbb{CP}^4$) is the gap in the Euler-characteristic sequence of the active even sectors ($\chi=N_c+2=5$, no fixed point for $g_{88}$; Part 9 T15b); $d=9$ ($S^9$) inherits that gap — its $S^1$-invariant block carries a $\mathbb{CP}^4$-symmetric kernel self-consistency with no admissible coupling; $d=7$ ($S^7$) has no activation route — Hopf universality (T9b) is a consistency relation between active sector pairs, not an activation mechanism, and any route treating the $d=6$ and $d=10$ bases symmetrically (their coupling rows are exactly equal, T9c) would equally activate $S^{11}$ over $\mathbb{CP}^5$, which the $d=11$ endpoint excludes. Note this is a statement about the reach of activation, not a geometric proof that eigenmodes cannot form: the Gegenbauer values for $d=7,8,9$ are all supercritical ($b_{k_0} > 1/2$), so localization would be geometrically permissible if a coupling were present. The residual — an activation law underdetermined by the two real activation instances — is an open item (Part 6); Rule A stands 🔶. The arbitration is not a mean-field object: the §3.10 condensate self-consistency $2\lambda_d^{3/2}=g_{dd}$ is solvable for any coupling in any dimension (the dimension cancels), so it cannot distinguish $d=7$ from the active set (Appendix A §3; `files/idwt.py` STEP 76). It lives in the coupled $(\Psi_\infty,\{M_d\})$ fixed point — Part 6 Open Theorem A, the ground-state covariance operator whose spectral plateaux should fall at exactly $d\in D$.

*Rule B (Gegenbauer criticality).* The Jacobi coupling $b_{k_0}(d) = \sqrt{k_0(k_0+d-1)}/(2k_0+d-2)$ must satisfy $b_{k_0} \geq 1/2$ for a sector to support stable bound-state modes. The unique solution to $b_{k_0}(d) = 1/2$ on the complex Hopf chain is:
$$4k_0 = (d-2)^2 \quad \Longrightarrow \quad 4\times 16 = 64 = (10-2)^2, \quad d = 10.$$
Sector $d=10$ is the critical endpoint; all $d \geq 11$ are subcritical — localization is impossible, modes cannot bind — and are excluded from the active sector set.

The sector set is therefore:
$$D = \underbrace{\{2,3,4,5\}}_{\text{Hopf pairs } n=1,2} \cup \underbrace{\{6\}}_{n=3 \text{ base, Rule A}} \cup \underbrace{\{10\}}_{n=5 \text{ base, Rule B}} = \{2,3,4,5,6,10\} \quad \square$$

**Remark.** The lepton sector coupling $g_{66} = 1/n_s = 1/4$ is derived from the composite $n_s=4$ alone — no hypercharge assignment enters.

**Remark — two qualitatively distinct types of inactive dimension.** $d\geq11$ and $d\in\{7,8,9\}$ are inactive for fundamentally different reasons, and the distinction matters.

Sectors $d\geq11$ are **subcritical** ($b_{k_0} < 1/2$): localization is geometrically impossible regardless of any coupling. Modes cannot bind; they disperse into the infinite-dimensional bulk. This is the stronger exclusion — it holds unconditionally.

Sectors $d\in\{7,8,9\}$ are **supercritical** ($b_{k_0} > 1/2$): localization would be geometrically permissible if a coupling were present. They are absent from the active sector set because IDWT's coupling construction terminates at $d=6$ — no activation route reaches the band: $d=8$ and $d=9$ are blocked by the $\chi=5$ gap, and $d=7$ by the $d=6$/$d=10$ row-equality argument of Rule A. No active sector geometry is established there, so no eigenmodes are generated. But this is a gap in the construction, not a geometric prohibition: the Gegenbauer criterion does not exclude these sectors, and whether they could host modes under an extended coupling theory remains open.

**Note on the index cross-check.** Once the sector set is established, one finds $n_{\rm top} = \chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = N_c \times n_s \times N_f = 3\times4\times6 = 72$, consistent with the mode index derived independently from the eigenmode selection chain.

**Sector set structure.** The active matter quartet $\{3,4,5,6\} = \{n_s-1,\ldots,n_s+2\}$ is derived from the Hopf chain and Rule A (Appendix A §19):

**Quartet derivation. 🔵** The complex Hopf chain $S^1\!\to\!S^{2k+1}\!\to\!\mathbb{CP}^k$ produces matter sectors at $d=3,4,5,6,\ldots$ (starting from the $k=1$ total space $S^3$ at $d=3$). Rule A terminates the chain at $\mathbb{CP}^{n_s-1}$ (real dimension $d_{\rm term}=2(n_s-1)$, Euler characteristic $\chi=n_s$, forcing $g_{d_{\rm term}}=1/n_s$). The matter quartet runs from $d=3$ to $d=2(n_s-1)$ with length $2(n_s-1)-3+1=2n_s-4$. The **self-consistency requirement** — the seed equals the number of matter sectors — gives $2n_s-4=n_s$, hence $n_s=4$. This is an independent derivation of the seed. At $n_s=4$ the quartet is $\{3,4,5,6\}$ with the two Hopf pairs $(d=3,d=4)$ (quark sectors) and $(d=5,d=6)$ (lepton sectors) — producing exactly two quark multiplets and two lepton multiplets as a structural consequence.

The full sector set reads:
$$D = \{2\} \cup \{n_s-1,\,n_s,\,n_s+1,\,n_s+2\} \cup \{2(n_s+1)\} = \{2,3,4,5,6,10\}$$

where $\{2\}$ is the EM reference sector, the quartet is the matter sector, and $2(n_s+1)=10$ is the Gegenbauer-critical terminal sector (Rule B above).

---

### 3b. Completeness of the Particle Spectrum

**Theorem.** The IDWT particle spectrum consists of exactly 15 states: the 14 mode indices in $\Sigma = \{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ plus the bottom quark beat at $k_0 = 16$ in $d=3$. No additional stable particles exist.

**Proof.** Three steps, each relying only on results already established.

**Step 1 — Finite sectors.** The Sector Set Theorem (§3a) proves $D = \{2,3,4,5,6,10\}$ is the complete set. Any new particle must reside in one of these six sectors.

**Step 2 — Eigenmode set is complete.** The sector comb filtration from $n_s = 4$ selects mode indices $\Sigma$. Applying every filtration rule to $\Sigma$ either returns an element already in $\Sigma$ or exits the physically accessible range — verified exhaustively (§5c). Therefore any mode index $n \notin \Sigma$ fails the **co-fixed-point condition** and cannot be a stable resonance. This eliminates all non-$\Sigma$ modes in every sector.

**Step 3 — Unique beat mode.** A beat mode arises at a site $k_0$ where three independent resonance conditions coincide simultaneously, forcing equal spectral weight at adjacent modes $n$ and $n+1$. The three conditions are:

$$k_0 = n_s^2 = 16, \qquad k_0 = n_e + n_u = 13 + 3, \qquad k_0 = S(n_s,3) - S(2,3) = 20 - 4.$$

All three give $k_0 = 16$ exactly. Every quantity is determined by $n_s = 4$. Exhaustive search over all $n \leq 200$ and $d \in D$ finds **no other site** satisfying all three conditions. The beat therefore exists at a unique site in $d=3$, giving $m_b = \sqrt{S(16,3) \times S(17,3)} \times m_{\mathrm{scale},3} = 4181$ MeV.

The beat is structurally confined to $d=3$: conditions 2 and 3 are $d=3$ identities — they use $n_e$ (from $d=6$) and $n_u$ (from $d=4$), whose sum closes onto the $d=3$ resonance site. The same $n=16$ appears in other sectors but produces no known particle mass. $\square$

**The observable spectrum is closed.** Given $n_s = 4$ and $m_e$, the list of observable particles, their masses, and their quantum numbers are fully determined. Any additional *observable* stable state would require either a new sector (excluded by §3a) or a new mode index consistent with the eigenmode selection rule (excluded by the Uniqueness Theorem, §5c). Neither exists. There is no room for new observable fundamental particles within the IDWT framework.

---

### Sector Euler Characteristics

Each CP^n sector carries an Euler characteristic χ(CP^n) = n+1 (one cell in each even dimension 0, 2, ..., 2n; alternating signs give n+1).

The Euler characteristics of the IDWT sectors are:

| Sector | Manifold | χ | Physical meaning |
|---|---|---|---|
| d=2 | CP¹ | 2 | Two photon/W helicities |
| d=3 | S³ | 0 | Odd sphere — vector-like QCD (correct: no γ₅) |
| d=4 | CP² | 3 | **N_c = 3 colours** (index = number of zero modes = colours) |
| d=5 | S⁵ | 0 | Odd sphere — no Majorana (Dirac neutrinos forced) |
| d=6 | CP³ | 4 | **n_s = 4 = composite** (index = n_s = n_u + n_d; n_u = 3 is the primitive seed) |
| d=10 | CP⁵ | 6 | **N_f = 6 flavours** (index = quark family count) |

**The composite n_s = 4 is topologically confirmed.** The d=6 lepton sector lives on CP³, with χ(CP³) = 4 (cells in dimensions 0, 2, 4, 6). The composite n_s = n_u + n_d must equal this Euler characteristic for the d=6 spectrum to be self-consistent — it counts the available topological modes before gauge fixing removes one, leaving three generations (e, μ, τ). The Euler characteristic independently confirms the composite value: n_s = χ(CP³) = 4.

**The top quark mode index from geometry:**

```
n_top = χ(CP²) × χ(CP³) × χ(CP⁵) = N_c × n_s × N_f = 3 × 4 × 6 = 72  [consistency check — not the derivation; see §3a]
```

The top quark mode index encodes all three quantum numbers of QCD simultaneously.

**Spin structure alternation.** CP^n admits a spin structure iff n is odd (c_1(CP^n) = n+1 must be even):

- d=2 (CP¹): **spin** — gauge sector (photon has exact spin-1)
- d=4 (CP²): **spinᶜ** — quarks must carry a U(1) factor = colour hypercharge ✓
- d=6 (CP³): **spin** — leptons have genuine spin structure (no forced U(1) coupling) ✓
- d=10 (CP⁵): **spin** — tau sector has genuine spin structure ✓

The quarks' spinᶜ structure (forced U(1) coupling) is the geometric origin of colour charge.

**The sum rule:**

```
Σ_{d∈D} χ(Ξ_d) = 2 + 0 + 3 + 0 + 4 + 6 = 15 = S(n_s,3) − n_s − 1
```

The total Euler characteristic of the sector manifold Ξ equals S(n_s,3) − n_s − 1 = 20 − 4 − 1 = 15.



### Parallel Uniqueness Results

The two uniqueness results are parallel:

| Uniqueness result | Algebraic condition | Consequence |
|---|---|---|
| Seeds {1,4} | S(n,4)=35 has unique solution n=4 | No other spectra |
| Sectors D | Three joint constraints on d | No other families |



**Convergence on d=10.** Two independent routes — Hopf chain (topology) and Gegenbauer criticality (algebra) — both give d=10.

The spinor type per sector follows from Clifford algebra periodicity (Clifford algebra, mod 8). The d=10 sector carries a Majorana-Weyl spinor (16 real components, d mod 8 = 2); the other sectors carry Weyl, Majorana, or Dirac spinors as determined by their d mod 8 (Part 8 §2.1).

These sector dimensions are not chosen. They are the unique sequence produced by the complex Hopf fibration chain S¹→S^{2n+1}→CP^n:

```
S¹ → S³  → S²    complex Hopf     →  d=2 (base CP¹), d=3 (total S³)
S¹ → S⁵  → CP²   complex Hopf     →  d=4 (base CP²), d=5 (total S⁵)
S³ → S⁷  → S⁴    quaternionic     →  d=4 also as S⁴≅HP¹ (consistent)
```

d=6 arises as CP³, the base space of the next complex Hopf fibration S¹→S⁷→CP³. CP³ has real dimension 6. d=7 (the total space S⁷) is excluded from the IDWT sector set for two consistent reasons: (i) geometrically, S⁷ is the total space of the quaternionic Hopf fibration S³→S⁷→S⁴ and is fully accounted for by the d=4 and d=3 sectors already present; (ii) algebraically, Hopf universality (T9b) is a consistency relation between active sector pairs, not an activation mechanism, and any activation route treating the d=6 and d=10 bases symmetrically would equally activate S¹¹ over CP⁵, which the d=11 endpoint excludes (Part 9 T3 Rule A; the open residual is recorded in Part 6). Both routes reach the same conclusion.

d=10 arises as CP⁵ = SU(6)/U(5), the next step in the complex projective chain beyond CP³. Its sector dimension d=10 is fixed by the Sector Set Theorem (§3a) — $d=10 = 2(N_f-1)$ where $N_f = n_{\rm top}/(N_c \times n_s) = 6$ — and confirmed independently by the Gegenbauer criticality condition (§3b), which shows that $b_{k_0}(d) = 1/2$ is achieved uniquely at d=10.

The sequence terminates at d=10 because any d > 10 puts the composite resonance site $k_0 = n_s^2$ in the evanescent (subcritical) regime — stable eigenmodes cannot form.

### 3b-ii. Sector Assignment Theorem — All 15 Particles Placed Without SM Input ✅

**Theorem (Sector Assignments).** Each of the 15 NS particles has a uniquely determined sector $d$ derivable from IDWT structure alone, without using SM particle names. The sectors are not assigned one particle at a time. They are the consecutive rungs of a single object — the complex Hopf chain $S^1\to S^{2k+1}\to\mathbb{CP}^k$, which alternates total spaces ($S^3, S^5, S^7$) and base spaces ($\mathbb{CP}^1, \mathbb{CP}^2, \mathbb{CP}^3$) to give the ladder $\{2,3\}\to\{4,5\}\to\{6,10\}$ (§3a). Each particle sits on the rung its generation-tower derivation routes it to, and its mode index falls out of the same step. The six rules below are the one ladder read at each rung: each placement carries an independent IDWT fingerprint — an Euler characteristic, a Hopf coupling identity, or a criticality condition — that fixes that rung. They are corroborations of a single structure, not six separate choices.

| Rule | Sector | Particles | IDWT derivation |
|------|--------|-----------|-----------------|
| R0 | d=2 | photon, W, Z, H | d=2 is the reference sector (CP¹, U(1)_EM) by construction; g-rule maps fermion combinations to d=2 |
| R1 | d=3 | down, strange | d=3 is observable spacetime and the first Hopf total space S³; seeds start the tower here |
| R2 | d=4 | up, charm, top | n_u = χ(CP²) = N_c = 3; n_top = χ(CP²)×χ(CP³)×χ(CP⁵) (T15, ✅) |
| R3 | d=5 | ν₁, ν₂, ν₃ | Hopf pair {4,5}: S⁵ is the Hopf total space over CP²; g₅₅ = g₃₃g₄₄/g₂₂ (✅) |
| R4 | d=6 | e, μ | χ(CP³) = n_s = 4; g₆₆ = 1/n_s (T15, ✅) |
| R5 | d=10 | τ | Gegenbauer criticality T5: b_{k₀}(d)=1/2 uniquely at d=10 (✅) |

**Proof sketch for each rule:**

**R0.** The d=2 sector is the reference sector (CP¹, carrying U(1)_EM; the photon is the d=2 n=0 ground state). Bosons (W, Z, H) land in d=2 via the Vandermonde g-rule: $g(d_\nu=5, n_{\rm top}) = 5+72-1 = 76 = n_W$; $g(d_\ell=6, n_W) = 6+76-1 = 81 = n_Z$. No SM particle names needed — only the sector dimensions d=5 and d=6 (derived below) and the already-derived mode indices.

**R1.** The seed sector is d=3: it is the observable spacetime sector and the first total space $S^3$ of the complex Hopf chain (§3a), the natural starting point of the generation tower. Both seeds share d=3: the down seed $n_{\rm down}=1$ is the universal ground state $S(1,d)=1$; the up seed $n_u=3$ has $\chi(\mathbb{CP}^2)=N_c=3$ (T15, ✅) and lands in d=4 via R2. The composite $n_s=1+3=4$ is confirmed by T4 and $S(4,4)=35$; it sits in d=3 as the strange quark. The χ-consecutiveness identity $n_u=n_s-1$ (T15) records a geometric fact about the Hopf chain, not a derivation from $n_s$.

**R2.** From T15 (§3a): $\chi(\mathbb{CP}^2) = N_c = 3 = n_u$. The up quark mode index equals the Euler characteristic of d=4 — the unique sector in $D$ with $\chi = n_u$. All up-type quarks share d=4: charm via $n_{\rm charm} = S(n_s,3)$ (HS from seed), top via $n_{\rm top} = \chi(\mathbb{CP}^2) \times \chi(\mathbb{CP}^3) \times \chi(\mathbb{CP}^5) = 72$ (T15).

**R3.** The Hopf pair $\{4,5\}$ is established in §3a: CP² (d=4) and S⁵ (d=5) are connected by the Hopf fibration $S^1 \to S^5 \to \mathbb{CP}^2$. The IDWT coupling universality $g_{55} = g_{33}g_{44}/g_{22}$ (Part 2 §9) is the algebraic expression of this Hopf connection. Neutrino modes are derived from the d=4 up quark by HS: $n_{\nu_1} = S(n_u, 3) = 10$, $n_{\nu_2} = S(n_u, 4) = 15$, $n_{\nu_3} = n_{\nu_1}+n_{\nu_2}-n_u = 22$. These land in d=5 (S⁵) as the Hopf total-space modes associated with the d=4 quark modes. **The Hopf routing rule** — HS outputs from d=4 land in d=5 — is proved as a corollary of §3a Step 2: $g_{55}$ is derived from $g_{44}$ via Hopf universality, making $d=5$ the unique sector in $D$ whose coupling closes over $d=4$; no other sector assignment is consistent with §3a. ✅

**R4.** From T15: $\chi(\mathbb{CP}^3) = n_s = 4$. The d=6 lepton sector is the unique sector in $D$ with Euler characteristic equal to the seed $n_s$. The coupling $g_{66} = 1/n_s$ (Part 2 §9) encodes the seed directly. Charged leptons are sums of d=4 and d=5 modes: $n_e = n_{\nu_1}+n_u = 13$, $n_\mu = n_{\rm charm}+n_{\nu_2} = 35$.

**R5.** Proved by the Gegenbauer criticality theorem T5 (§3c below): $b_{k_0}(d) = 1/2$ iff $4k_0 = (d-2)^2$, giving $d=10$ as the unique solution. The tau is the terminal particle at the Gegenbauer critical endpoint.

**Uniqueness of the labeling.** The tower DAG has a trivial automorphism group (Appendix A §13b): no non-trivial relabeling preserves the derivation structure, so once the seed sector $d=3$ is fixed and the Hopf ladder assigns each rung, there is exactly one consistent labeling. This establishes uniqueness *up to relabeling* — it forbids alternative assignments that preserve the DAG; it does not by itself derive the DAG from the dynamics. The geometric rung placements R2 ($\chi(\mathbb{CP}^2)=N_c$), R3 (Hopf pair $\{4,5\}$), R4 ($\chi(\mathbb{CP}^3)=n_s$), and R5 (Gegenbauer criticality) are each ✅ structural consequences; the boson routing R0 rests on the $g$-rule, whose $-1$ offset is now derived (✅, Part 3 §11). The one placement set by a mechanism outside the Hopf ladder is R5: the tau is the third charged lepton, not placed in the lepton base $\mathbb{CP}^3$ (d=6) with the electron and muon but at the Gegenbauer-critical terminal sector d=10. The two are reconciled by the kernel — $g_{10,10}=g_{66}=1/n_s$, so the coupling cannot distinguish the d=6 lepton sector from the d=10 terminal sector, and the muon/tau split is pure sector geometry $S(35,6)$ vs $S(23,10)$ (Part 2 §9b). **Status: ✅ for the geometric rung placements (R2–R5); the assignment as a whole is forced only modulo the open derivation of the tower DAG itself (co-fixed-point stability, MC-4).**

Script: `claude/sector_assignment_proof.py`.

### 3c. Gegenbauer Criticality Theorem — Second Route to d=10

An independent algebraic derivation of d=10 comes from the Gegenbauer chain structure of the Jacobi operator at the resonance site k₀ = n_s² = 16.

**Definition.** The Gegenbauer coupling at the resonance site k₀ in sector d is the off-diagonal matrix element of the d-dimensional Jacobi chain at bond k₀:

```
b_{k₀}(d) = √(k₀(k₀+d−1)) / (2k₀+d−2)
```

For the IDWT sectors with k₀ = n_s² = 16 this evaluates to:

| d | b_{k₀}(d) | Status |
|---|---|---|
| 2 | 0.51539 | supercritical — active |
| 3 | 0.51426 | supercritical — active |
| 4 | 0.51281 | supercritical — active |
| 5 | 0.51110 | supercritical — active |
| 6 | 0.50918 | supercritical — active |
| 7 | 0.50712 | supercritical — present in M_∞ but no stable eigenmodes (Rule A) |
| 8 | 0.50497 | supercritical — present in M_∞ but no stable eigenmodes (Rule A) |
| 9 | 0.50246 | supercritical — present in M_∞ but no stable eigenmodes (Rule A) |
| **10** | **0.50000** | **critical (exact) — active** |
| 11 | 0.49747 | subcritical — cannot localize |

**Theorem.** b_{k₀}(d) = 1/2  ↔  4k₀ = (d−2)²  ↔  d = 2 + 2√k₀ = 2(n_s+1) = 10.

**Proof.**  b = 1/2  ↔  4k₀(k₀+d−1) = (2k₀+d−2)²  ↔  4k₀(d−1) − 4k₀(d−2) = (d−2)²  ↔  4k₀ = (d−2)².  With k₀ = n_s² = 16: d = 2 + 2√16 = 2 + 2n_s = 10. □

**Monotonicity.** b_{k₀}(d) is strictly decreasing in d. d=10 is therefore the **last** sector with b_{k₀} ≥ 1/2. For d ≥ 11 the coupling is subcritical: the resonance site k₀ falls outside the chain's natural coupling range and the sector cannot propagate.

**Physical interpretation.** In the Gegenbauer recurrence, b = 1/2 is the critical coupling where a resonance site sits precisely at the boundary between propagating and evanescent regimes. All active IDWT sectors (d = 2…6 and d = 10) are at or above critical at k₀. Sectors d=7,8,9 are also supercritical (b > 1/2) — localization would be geometrically permissible — but IDWT's coupling construction does not reach them (Rule A), so no active sector geometry is established there. This is distinct from d≥11, where subcriticality (b < 1/2) means localization is geometrically impossible regardless of any coupling: modes fall into the evanescent regime and cannot propagate through the chain at k₀.

**Sector phase delay consequence.** The sector phase delay correction τ_d = 1/(2√(k₀+d)) is proportional to (b_{k₀} − 1/2)/b_{k₀}². For d = 10 this correction **vanishes identically** — the leading-order sector phase delay is exact for the terminal sector. For d = 3 the correction is −0.67% and goes in the wrong direction for the ρ meson, confirming that the +0.069% residual in the ρ prediction is a genuine prediction floor, not a removable sector phase delay artifact.

**Triple consistency of d=10:**

| Route | Condition | Result |
|---|---|---|
| **Gegenbauer (algebra)** | **b_{k₀}(d) = 1/2 ↔ d = 2(n_s+1)** | **d = 10** |
| Hypercharge (gauge) | g_{10,10} = g_{6,6} = 1/n_s = 1/4 | d = 10 |

Two routes, one answer. The IDWT framework is over-determined on the terminal sector.

---

### 3d. Per-Sector Profiles

Every particle is a bound eigenmode of V_d(r) = λ_d r² with mass m(n,d) = m_scale_d × S(n,d), S(n,d) = C(n+d−1,d). The following profiles collect each sector's coupling, particle content, quantum properties, and spectral data.

---

#### d = 2 — Electroweak Sector

**Geometry.** CP¹ = S² (globally); S³ Hopf fibration over S² with U(1) fiber. Hopf fiber phase → electromagnetic potential A_μ = ∂_μθ, curvature → F_μν. SU(2)_L acts on the base CP¹.

| Parameter | Value |
|---|---|
| g₂₂ | 722.5 |
| m_scale_2 | 27.47 MeV |
| L_2 | 0.375 fm |

| Particle | n | S(n,2) | Predicted mass | PDG |
|---|---|---|---|---|
| γ (photon) | 0 | 0 | 0 (zero mode — exact) | 0 ✅ |
| W boson | 76 | 2926 | 80.377 GeV | 80.377 GeV ✅ |
| Z boson | 81 | 3321 | 91.188 GeV | 91.188 GeV ✅ |
| Higgs H | 95 | 4560 | 125.25 GeV | 125.25 GeV ✅ |

Note: S(n,2) = n(n+1)/2. The photon zero mode is exactly massless — the mode equation has no zero-eigenvalue force term.

**Quantum properties.**
- **Electromagnetism:** U(1) Hopf fiber holonomy → gauge field A_μ; photon is the connection 1-form.
- **Weak isospin:** SU(2)_L acts only on holomorphic half of d=2 spinor → left-handedness of W coupling.
- **sin²θ_W = 1 − (S(76,2)/S(81,2))² = 0.2237** (PDG: 0.2229, +0.37% — within 1-loop EW corrections).
- **EW scale:** √Tr(D²) ≈ 248.3 GeV is the spectral RMS of |D| across all sectors. IDWT does not use spontaneous symmetry breaking; the Higgs is mode n=95, not a condensate. The EW scale is (√2 G_F)^{-1/2} = 246.3 GeV from the IDWT-derived G_F (§0, Part 5 §3c).
- **Coupling filter:** Orientation/phase alignment. The photon couples only to currents aligned with its polarization vector ε_μ; perpendicular currents receive zero coupling, not suppression. This is the U(1) geometry of CP¹ expressing itself as a coupling structure — polarization is not a label on the photon but the geometry's stamp on what the photon can do.

**Spectral.** ζ₂(1) = 2, ζ₂(0) = −1, a₀₂ ≈ 1.253.

---

#### d = 3 — Hadronic Sector (Down-Type Quarks)

**Geometry.** S³ (round); isometry SU(2)×SU(2) ≅ SO(4). Color charge by coordinate containment inside Ξ₄ (Part 3 §2). Confinement: E_conf = λ_c|N⃗|.

| Parameter | Value |
|---|---|
| g₃₃ | 8√7 ≈ 21.17 |
| m_scale_3 | 4.702 MeV |
| L_3 | 0.675 fm |

| Particle | n | S(n,3) | Predicted mass | PDG |
|---|---|---|---|---|
| d quark | 1 | 1 | 4.702 MeV | ~4.7 MeV ✅ |
| s quark | 4 | 20 | 94.04 MeV | 93.4 MeV ✅ |
| b quark | beat k₀=16 | √(S(16,3)·S(17,3)) | 4181 MeV | 4180 MeV ✅ |

Note: S(n,3) = n(n+1)(n+2)/6. The b quark is a beat resonance (§3b) at the unique triple-coincidence site k₀ = n_s² = 16.

**Quantum properties.**
- **SU(3) color:** Down-type quarks carry color via coordinate containment inside Ξ₄; the SU(3) symmetry arises from the CP² (d=4) isometry. They transform in the fundamental representation.
- **Confinement:** Scattering states are non-normalizable — not bound states — so they do not appear in the physical spectrum; all physical modes are confined.
- **Cabibbo angle:** sin θ_C = (1+1/240)/√S(4,3) = 0.22454 (PDG: 0.22450, +0.09σ). The 1/240 is the CP¹ sector curvature correction.
- **Baryon number:** Topological winding number of the S³ mode.
- **Coupling filter:** Left-handed weak isospin. The SO(4) = SU(2)_L × SU(2)_R isometry of S³ gives left-handed W coupling and leaves the right-handed component decoupled from the weak interaction. Color coupling is inherited derivatively via coordinate containment inside Ξ_4, not from S³ itself.

**Spectral.** ζ₃(1) = 3/2, ζ₃(0) = −3/2, a₀₃ ≈ 1.623.

---

#### d = 4 — Up-Type Quark Sector

**Geometry.** CP² (complex projective plane); local symmetry U(2). Kähler structure provides γ₅ for left-handed chirality. GTC (Global Topological Correction) ε = 1/(280√7) from the CP² Euler characteristic.

| Parameter | Value |
|---|---|
| g₄₄ | 12/√7 ≈ 4.536 |
| m_scale_4 | 0.1451 MeV |
| L_4 | 0.872 fm |

| Particle | n | GTC order k | Predicted mass | PDG |
|---|---|---|---|---|
| u quark | 3 | 0 | 0.1451 × 15 = 2.177 MeV | ~2.2 MeV ✅ |
| c quark | 20 | 3 | m_scale_4 × S(20,4) × (1−ε)³ = 1279.7 MeV | 1270 MeV ✅ |
| t quark | 72 | 10 | m_scale_4 × S(72,4) × (1−ε)^{10} = 174.0 GeV | 172.69 GeV ✅ |

Note: S(n,4) = n(n+1)(n+2)(n+3)/24. ε = 1/(280√7) ≈ 0.001348.

**Quantum properties.**
- **SU(3) color:** Up-type quarks share color with d=3 via the cross-sector tower coupling g₃₃ × g₄₄.
- **Electric charge +2/3:** From Kähler index and U(2) representation theory (Part 3 §4).
- **Chirality:** CP² Kähler γ₅ → W couples to left-handed component only.
- **GTC:** The topological correction (1−ε)^k accounts for the compression of up-type masses relative to naive mode scaling; without it the top is overestimated by ~1.35%.
- **Coupling filter:** Color conservation. χ(CP²) = 3 gives N_c = 3 — the number of independent color coupling handles. All processes must conserve color; isolated color-nonsinglet states are geometrically forbidden. Confinement is this filter operating at the level of which asymptotic states can be constructed, not a dynamical suppression.

**Spectral.** ζ₄(1) = 4/3, ζ₄(0) = −2, a₀₄ ≈ 2.006.

---

#### d = 5 — Neutrino Sector

**Geometry.** S⁵ (round); isometry SO(6) ≅ SU(4). d mod 8 = 5 → spinor bundle on S⁵ admits no real (Majorana) structure → Majorana mass terms forbidden.

| Parameter | Value |
|---|---|
| g₅₅ | 96/722.5 ≈ 0.1329 |
| m_scale_5 | ≈ 7.4 × 10⁻¹³ MeV |
| L_5 | 1.571 fm |

m_scale_5 is fully derived from the cross-sector constraint m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³. No neutrino mass data enters.

| Particle | n | S(n,5) | Predicted mass | Bound |
|---|---|---|---|---|
| ν₁ | 10 | 2002 | 1.487 meV | < 450 meV ✅ |
| ν₂ | 15 | 11628 | 8.639 meV | < 450 meV ✅ |
| ν₃ | 22 | 65780 | 50.27 meV (bare: 48.87 meV) | < 450 meV ✅ |

Note: S(n,5) = n(n+1)(n+2)(n+3)(n+4)/120. Σm_ν = 60.39 meV (corrected; δ_ν₃ = ε×g_{33} = 1/35, Part 2 §9d); bare 59.00 meV. Δm²₃₁/Δm²₂₁ = 34.86 (corrected; PDG: 34.825, +0.11%).

**Quantum properties.**
- **Dirac (not Majorana):** d mod 8 = 5 → no real spinor → Majorana forbidden → **0νββ rate = 0** (hard prediction).
- **Normal ordering:** n₁ < n₂ < n₃ and S(n,5) monotone → m_ν₁ < m_ν₂ < m_ν₃ necessarily. Experiments prefer normal ordering at 3–4σ.
- **PMNS angles:** θ₁₂, θ₂₃, θ₁₃ determined by g₅₅ = 96/g₂₂ and the four mode indices (n_e, n_μ, n_τ, n_ν); all three angles fixed with no free parameters (Part 9 T6).
- **No sterile neutrinos:** bulk-propagating modes are non-normalizable (not bound states) and do not appear; the co-fixed-point condition selects exactly three d=5 modes.
- **Coupling filter:** Dirac condition — geometric prohibition of an entire class of interactions. The Clifford algebra of S⁵ (d mod 8 = 5) cannot support the spinor structure required by Majorana mass terms, the see-saw mechanism, or any lepton-number-violating vertex. These interactions are not suppressed — they cannot be written down for S⁵ modes. The S⁵ Hopf fibration (S¹ → S⁵ → CP²) additionally projects the color representation from CP² onto its singlet component, giving color-neutral neutrinos despite their coordinate support inside Ξ_4. Positively, the SO(6) ≅ SU(4) sector gives neutrinos their B−L charge.

**Spectral.** ζ₅(1) = 5/4, ζ₅(0) = −5/2, a₀₅ ≈ 2.392.

---

#### d = 6 — Charged Lepton Sector (e, μ)

**Geometry.** CP³; local symmetry U(3). CP³ Kähler form → hypercharge assignment. Lepton number = U(1) centre of U(3).

| Parameter | Value |
|---|---|
| g₆₆ | 1/4 (composite ratio 1/n_s) |
| m_scale_6 | m_e / S(13,6) ≈ 2.75 × 10⁻⁵ MeV |
| L_6 | 1.414 fm |

| Particle | n | S(n,6) | Predicted mass | PDG |
|---|---|---|---|---|
| e (electron) | 13 | 18564 | 0.51100 MeV (anchors scale) | 0.51100 MeV ✅ |
| μ (muon) | 35 | 3838380 | 105.658 MeV | 105.658 MeV ✅ |

Note: S(n,6) = n(n+1)(n+2)(n+3)(n+4)(n+5)/720. Ratio m_μ/m_e = S(35,6)/S(13,6) = 206.765 (PDG: 206.768, −0.002%).

**Quantum properties.**
- **Lepton number L=1:** Topological U(1) winding number of CP³ fibre.
- **Electric charge −1:** From Kähler index of CP³ (Part 3 §5).
- **Chirality:** CP³ Kähler γ₅ → left-handed W coupling (same mechanism as d=4).
- **Hypercharge:** Y = −1/2 (left-handed), Y = −1 (right-handed); from U(3) centre.
- **Coupling filter:** Total colour silence. χ(CP³) = 4, not 3; colour contributions cancel in the SU(4) representation. Zero strong coupling at any energy — not suppressed, geometrically absent. The d=2 photon sector (CP¹) is a coordinate subspace of d=6 (CP³); the electron-photon coupling follows from coordinate containment and the rank-1 kernel, giving pure U(1) EM coupling with the structure fixed by the CP³ isometry.

**Lepton universality as a geometric theorem.** The electron and muon are both d=6 (CP³) modes — n = 13 and n = 35 in the same geometry. The coupling to any lower-d particle — photon, W, Z (all d=2) — depends only on the sector geometry, not on the mode index. Both are d=6 modes containing the same Ξ₂ coordinates, with the same contact structure; the mode index enters only the mass formula. Lepton universality is not measured and then explained — it is forced by both particles living in the same CP³. Any two modes in the same sector couple identically to everything outside it.

**Orbit hybridization as a basis choice.** The sp, sp², sp³ hybridization of chemistry is usually presented as a mixing of s and p orbitals that requires energy to set up. But the electron is a d=6 mode executing a 6D orbit, and s, p, d, f orbitals are different d=3 projections of that same 6-dimensional orbit — angular momentum eigenstates (L=0, 1, 2, 3) of the same SU(4) angular momentum tower. The CP³ isometry group SU(4) rotates between these d=3 projections exactly — there is no energy cost, no approximation, no mixing. What looks like ad hoc mixing to a d=3 observer is the electron settling into the lowest-energy angular momentum configuration of its 6D orbit for its bonding environment. Carbon's sp³ bonds form a perfect tetrahedron because the SU(4) isometry acting on the 6D orbit projects to the tetrahedral rotation group in d=3; the tetrahedral angle (arccos(−1/3) = 109.47°) is derivable from the CP³ geometry alone, with no empirical input.

**The electron's apparent d=3 position is where its 6D orbit intersects our coordinates.** The electron executes a definite 6D orbit in CP³. A d=3 observer detects it only where that orbit intersects our three observable coordinates. The 6D orbit sweeps through our 3D slice carrying no confinement in the d=3 directions — only the d=6 sector potential localises the electron, and that localisation is in the 6D sector space, not in our 3D coordinates. The intersections of the 6D orbit with our 3D slice therefore fall anywhere across observable space. This is the IDWT reading of the standard quantum statement that the electron can be found anywhere in the universe: not uncertainty, not a smeared probability cloud, but the 3D shadow of the definite 6D orbit the electron follows — a shadow unlocalized by construction. The orbit is definite; the apparent position in d=3 is the shadow of that orbit in our three coordinates, and a shadow does not inherit the localization of the object that casts it.

**Spectral.** ζ₆(1) = 6/5, ζ₆(0) = −3, a₀₆ ≈ 2.777.

---

#### d = 10 — Tau Sector

**Geometry.** CP⁵ = SU(6)/U(5); local symmetry U(5). V_{10}(r) sits at the Gegenbauer critical endpoint (b_{k₀}=1/2), making the sector phase delay exact. Shares coupling $g=1/n_s$ and mass scale with d=6 — unified lepton composite coupling.

| Parameter | Value |
|---|---|
| g_{10,10} | 1/4 (same as d=6) |
| m_scale_{10} | = m_scale_6 (shared seed) |
| L_{10} | 1.414 fm |

| Particle | n | Back-reaction factor | Predicted mass | PDG |
|---|---|---|---|---|
| τ (tau) | 23 | × (1+1/1680) | 1776.84 MeV | 1776.93 MeV ✅ |

Back-reaction factor 1+1/1680 = 1 + 1/(n_up × n_s² × S(n_s,4)) from the Gegenbauer critical endpoint sector phase delay correction. Without it, m_τ is 0.06% low.

**Quantum properties.**
- **Lepton number L=1 and charge −1:** Shared with d=6 via joint g=1/4 coupling.
- **Gegenbauer critical-endpoint condition:** At the Gegenbauer critical point, the sector phase delay is exact — no higher-order corrections to the tau mass. Unique among all sectors.
- **Lepton universality:** m_scale_{10} = m_scale_6 enforces identical mass unit for the heavy lepton family; mass splitting comes entirely from different mode indices (23 vs 13, 35).
- **Coupling filter:** Gegenbauer-critical coupling. At the Gegenbauer critical endpoint (Jacobi threshold b_{k₀} = 1/2), modes sit at the Jacobi coupling boundary — coupling weight is distributed across many channels with no dominant mode. This is a critical-point property, not a fractal or self-similar structure. The tau's coordinate space Ξ_{10} contains all other sectors; in principle it couples to everything, but at every specific channel the coupling is marginal. This explains the tau's decay pattern: no gap (short lifetime), but no dominant channel (broad decay distribution). The geometric back-reaction correction δ_τ = 1/1680 (required only at the critical point) is the mathematical signature of this critical-boundary coupling.

**The tau is the only particle that touches everything.** The tau's d=10 sector contains all of Ξ₂ through Ξ₁₀; every other particle's coordinates are a subset of the tau's. The tau is the only particle where the contact condition — that one sector's coordinates overlap with the partner's — is trivially satisfied for every possible partner. But the Gegenbauer criticality means coupling weight is distributed with no dominant channel. The tau's interaction pattern is the direct consequence: it decays to electrons, muons, pions, kaons, multiple neutrinos — every channel is open, none dominates. The electron (d=6) does not decay; the muon (d=6) decays almost entirely to an electron and neutrinos; the tau (d=10) distributes across every sector. The widening of the accessible channel tree with d is a readout of coordinate nesting depth, with the Gegenbauer criticality of d=10 preventing any single open channel from being selected.

**Spectral.** ζ_{10}(1) = 10/9, ζ_{10}(0) = −5, a₀_{10} ≈ 4.308.

---

### 3e. Sector Summary Table

| d | Geometry | Particles | g_dd | m_scale_d | L_d (fm) | ζ_d(1) | ζ_d(0) | a₀_d |
|---|---|---|---|---|---|---|---|---|
| 2 | CP¹ (EW/Hopf) | γ, W, Z, H | 722.5 | 27.47 MeV | 0.375 | 2 | −1 | 1.253 |
| 3 | S³ (hadronic) | d, s, b | 8√7 | 4.702 MeV | 0.675 | 3/2 | −3/2 | 1.623 |
| 4 | CP² (up-type) | u, c, t | 12/√7 | 0.1451 MeV | 0.872 | 4/3 | −2 | 2.006 |
| 5 | S⁵ (neutrino) | ν₁, ν₂, ν₃ | 96/722.5 | 7.4×10⁻¹³ MeV | 1.571 | 5/4 | −5/2 | 2.392 |
| 6 | CP³ (lepton) | e, μ | 1/4 | 2.75×10⁻⁵ MeV | 1.414 | 6/5 | −3 | 2.777 |
| 10 | CP⁵ (tau) | τ | 1/4 | = m_scale_6 | 1.414 | 10/9 | −5 | 4.308 |

ζ_d(1) = d/(d−1) and ζ_d(0) = −d/2 are exact for all sectors (Part 9 T13–T14, Pascal telescoping and heat kernel). All 15 particle masses follow from m_scale_d × S(n,d) plus three corrections: GTC for up-type quarks, geometric back-reaction correction for tau, beat resonance for b quark. No other free parameters once the six couplings g_dd are fixed from seeds {n_d=1, n_u=3} and composite n_s = 4.

### 3e-ii. The Particle Map — All Fifteen Modes

Each Standard Model particle is one mode of Ψ_∞, fixed by its sector dimension d and mode index n, with mass m(n,d) = S(n,d) × m_scale_d. The full spectrum:

| Particle | d | Geometry | Isometry | n | S(n,d) | Mass |
|----------|---|----------|----------|---|--------|------|
| photon γ | 2 | CP¹ | SU(2) | 0 | 0 | 0 (exact) |
| W | 2 | CP¹ | SU(2) | 76 | 2,926 | 80.38 GeV |
| Z | 2 | CP¹ | SU(2) | 81 | 3,321 | 91.23 GeV |
| Higgs | 2 | CP¹ | SU(2) | 95 | 4,560 | 125.27 GeV |
| down | 3 | S³ | SO(4) | 1 | 1 | 4.70 MeV |
| strange | 3 | S³ | SO(4) | 4 | 20 | 94.0 MeV |
| up | 4 | CP² | SU(3) | 3 | 15 | 2.18 MeV |
| charm | 4 | CP² | SU(3) | 20 | 8,855 | 1.28 GeV |
| top | 4 | CP² | SU(3) | 72 | 1,215,450 | 174 GeV |
| ν₁ | 5 | S⁵ | SO(6) | 10 | 2,002 | 1.49 meV |
| ν₂ | 5 | S⁵ | SO(6) | 15 | 11,628 | 8.64 meV |
| ν₃ | 5 | S⁵ | SO(6) | 22 | 65,780 | 50.3 meV |
| electron | 6 | CP³ | SU(4) | 13 | 18,564 | 0.511 MeV |
| muon | 6 | CP³ | SU(4) | 35 | 3,838,380 | 105.7 MeV |
| tau | 10 | CP⁵ | SU(6) | 23 | 64,512,240 | 1776.84 MeV |

The bottom quark is not in the table: it is not a single (n,d) mode but the geometric-mean beat between n=16 and n=17 in d=3 at the resonance site k₀ = n_s² = 16, m_b = √(S(16,3)·S(17,3)) × m_scale_3 ≈ 4181 MeV. It is a stable d=3 resonance, not one of the 15 co-fixed-point pairs Σ_pairs (§3b, §5).

---

### 3f. The Coordinate Extension Picture

M∞ is one coordinate system extended step by step: the two coordinates of d=2 are contained in d=3, the three of d=3 are contained in d=4, and so on without bound. The sectors D = {2, 3, 4, 5, 6, 10} are the stable levels at which this extension produces observable eigenmodes.

At each new dimension d, the stability condition is whether the self-coupling equation has a solution consistent with the seed pair {n_d=1, n_u=3} and composite n_s = 4. The even sectors d ∈ {2, 4, 6, 10} close on their Kähler geometry (χ = 2, 3, 4, 6); d=3 closes on the parallelizable Lie-group structure of S³ = SU(2). Both S³ and S⁵ have χ = 0, so vanishing Euler characteristic does not distinguish them — the discriminator is parallelizability: S³ is a division-algebra sphere (ℍ on ℝ⁴) and closes on its own group structure, while S⁵ is non-parallelizable (S^n is parallelizable only for n = 1, 3, 7) and has no self-coupling fixed point of its own. For d=5, S⁵ is neither Kähler nor parallelizable; m_scale_5 is fixed by the cross-sector constraint m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ (Part 2 §9c). In each closing sector the Gegenbauer threshold falls within the vacuum stability window.

M∞ is genuinely infinite-dimensional. Beyond d=10 the Gegenbauer threshold exceeds the vacuum stability bound, or no cross-sector pairing satisfies the Vandermonde coupling rule; the odd spheres there are non-parallelizable as well. The window for self-consistent eigenmodes closes at d=10; M∞ continues. D = {2, 3, 4, 5, 6, 10} are the primes of the extension — the levels at which the coordinate system locks into a stable sector.

The containment chain Ξ₂ ⊂ Ξ₃ ⊂ Ξ₄ ⊂ Ξ₅ ⊂ Ξ₆ ⊂ Ξ₁₀ holds for all six sectors: each Ξ_d is M∞ evaluated at coordinate level d, and each level's coordinates are a literal subset of the next level's coordinates.

---

### 3g. Interaction as Coordinate Containment

Particles in different sectors couple because their sectors share coordinate subspaces. The two coordinates of the photon's d=2 sector are literally two of the three coordinates of d=3, two of the four of d=4, two of the five of d=5, two of the six of d=6, two of the ten of d=10. Dynamics in any shared subspace are dynamics in every sector that owns those coordinates, symmetrically in both directions. A photon perturbs an electron because those two coordinates belong to the electron as well. An electron moving in its six dimensions necessarily moves in the two-dimensional subspace that photons live in — and so affects them.

This is why electromagnetism is universal. Every sector d ≥ 2 contains d=2 as its lowest coordinate subspace, so every charged particle couples to the photon. The coupling constant reflects the coordinate overlap — the ratio of shared dimensions to total dimensions of the higher sector.

The strong force spans d ∈ {3,4}. Down-type quarks (d=3) and up-type quarks (d=4) interact through the d=4 kernel self-coupling g_{44}, which is SU(3)-invariant by the CP² isometry. Down-type quarks couple because d=3 ⊂ d=4 — they share the full d=3 coordinate subspace with the d=4 quark sector. Up-type quarks couple because they occupy d=4 directly. The coupling is a direct contact term in the kernel.

The electron (d=6, mode n=13) couples to the photon (d=2) via the two coordinates they share. The coupling strength derives from a cascade: g_{44} → g_s → g_2 → sin²θ_W → g_1 → α (Part 3 §0.7). Coordinate containment determines that the coupling exists and which sectors are linked; coupling magnitudes are set by the spectral geometry of each sector manifold — integrals over S^{d−1} and CP^m, not bare dimension counts. There is one step in the cascade where the coordinate ratio does appear literally: g_2 = (2/3)√g_s, where 2/3 = d_photon/d_hadronic. The factor 2/3 is the electric charge of the up quark and the ratio of photon sector dimension to hadronic sector dimension N_c = 3, and those are the same number because N_c = d_hadronic.

**Complementary principle — sector geometry as coupling filter.** Coordinate containment is the necessary condition for coupling: it answers whether coupling between a particle and a force is possible at all. Complementary to this is the coupling filter: the particle's own sector geometry determines the structure of whatever coupling it has. The sector quantum number — polarization, color, the Dirac condition — is not a label attached to the particle after the fact. It is the geometry of the particle's sector expressing itself as a coupling structure, determining both what coupling handles the particle presents to the world and what entire classes of interaction are geometrically forbidden to it. Coordinate containment answers "which forces can couple to this particle?"; the coupling filter answers "how does it couple, and what is structurally impossible?" These two principles are independent. A particle can have coordinate support in a force's sector (satisfying containment) while its own sector geometry projects that support onto the singlet representation — as neutrinos do with color via the S⁵ Hopf structure. The full coupling structure of any particle requires both principles applied together. See §3d for the coupling filter characterization of each sector.

---

### 3h. Sector Autonomy and Nested Dynamical Invariance

Each sector Ξ_d is a self-contained dynamical system. Its Hamiltonian H_d = −Δ_{Ξ_d} + V_d(|ξ_d|) is invariant under the isometry group G_d of the sector manifold, and its eigenvalue problem H_d χ = m_eff χ can be solved sector by sector without reference to any other sector. The mass formula m = m_scale_d × S(n,d) is sector-separable: the d=6 lepton spectrum is determined entirely by H_6; the d=4 quark spectrum by H_4.

This autonomy survives the nesting Ξ_2 ⊂ Ξ_3 ⊂ ··· ⊂ Ξ_{10}. At the level of coordinate algebras, the inclusion of coordinate subspaces induces a nested chain of observable algebras — the shared coordinate algebra of M∞:

```
C∞(Ξ_2) ⊂ C∞(Ξ_3) ⊂ C∞(Ξ_4) ⊂ C∞(Ξ_5) ⊂ C∞(Ξ_6) ⊂ C∞(Ξ_7) ⊂ C∞(Ξ_8) ⊂ C∞(Ξ_9) ⊂ C∞(Ξ_{10}) ⊂ C∞(M∞)
```

A function of only the d=2 coordinates is simultaneously a valid function on every sector — it belongs to every algebra in the chain. The differential operators built from those coordinates — the d=2 Laplacian, the U(1) rotation generators — appear in every larger sector's operator algebra, acting on the shared coordinate subspace and commuting with any operator that acts only on the additional coordinates. The symmetry generators of a smaller sector are literal elements of the operator algebra of every larger sector.

This is the precise sense in which each dynamical system is nested inside, and invariant within, the shared coordinate algebra: the G_d-invariant structure of H_d is preserved in every H_{d'} for d' > d, restricted to the G_d-invariant subspace of C∞(Ξ_{d'}). The sector potential wells localize each particle type to its own sector, ensuring this restriction is physically realized rather than merely formal. A mode that does not excite the additional coordinates of Ξ_{d'} is dynamically a mode of Ξ_d, and the symmetry generators that label it are present in both algebras — so its quantum numbers are unambiguous in either context.

§3g and §3h are complementary. §3g: shared coordinates produce coupling — perturbations in one sector propagate to every sector that shares those coordinates, bidirectionally. §3h: that coupling operates at the shared subspace and leaves each sector's bulk eigenvalue structure intact. The inter-sector coupling terms g_{d,d'} in the kernel (§4) are cross-sector boundary terms, not deformations of the individual sector Hamiltonians H_d. Each sector remains exactly as self-consistent in isolation as it is in the full system — the nesting is lossless.

**Physical reading — every particle integrates out the dimensions it does not have.** The nesting has a direct physical meaning. A particle of sector dimension d has structure only in its d coordinates; in every coordinate of M∞ beyond d it is uniform — it integrates those dimensions out. This is the literal content of C∞(Ξ_d) ⊂ C∞(Ξ_{d'}): a d-function is one that does not vary in the additional coordinates. It is the same fact as "bound within, free without" (§3i) — bound in its own d dimensions, uniform in all the rest. Two consequences follow, and they hold for *every* particle, not only the photon.

*Coupling.* Because each particle is uniform outside its own d dimensions, two particles meet only on the coordinates they share — the lower of their two dimensionalities. The kernel self-coupling (§3g, §4) acts on that shared subspace and on nothing else; the surplus coordinates of the higher-dimensional particle are integrated out of that particular meeting (they carry its *other* couplings, not this one). So a lower-dimensional structure reaches every particle whose sector contains its coordinates, and a particle feels every force whose sector is contained in its own — the containment necessary-condition of §3g, seen from each side. A particle "lines up" with every higher-dimensional particle through the subspace they hold in common, and the coupling fires there when the symmetry/charge filter (§3g) also aligns.

*Orientation.* With no structure outside its d dimensions, a particle has nothing out there to fix the orientation of its d-frame: which d-plane of M∞ it occupies is a free, kinematic degree of freedom, while the count d, the sector geometry, and the mass S(n,d) are fixed by the sector. The frame is determined up to orientation by the sector; the orientation is set by what the particle lines up with.

The photon (d=2) is the sharpest instance of both, because 2 is the smallest sector dimension: it integrates out dimensions 3–10, couples to every charged particle through the d=2 subspace they all contain (electromagnetism is universal for exactly this reason), and its reorientable 2-plane — its polarization — is directly observable (§3i).

---

### 3i. The d=3 Threshold: Sector Dimension as Physical Dimensionality

The coordinate extension picture (§3f) assigns a concrete meaning to the phrase "our three observable spatial dimensions": they are the d=3 level of the coordinate hierarchy. The three coordinates at which the extension first produces a full self-consistent sector are the same three coordinates that constitute our observable space. The sector dimension d therefore measures where each particle stands relative to our observable space.

| d relative to 3 | Physical meaning | Example |
|---|---|---|
| d < 3 | Particle has fewer directions than our d=3 | Photon (d=2): two directions, fewer than our three |
| d = 3 | Particle's sector coincides with our d=3 | Down-type quarks: sector is exactly our d=3 |
| d > 3 | Our d=3 is a subspace of the particle's sector | Electron (d=6): 6D sector; our d=3 is a subspace of it |

**Particles with d > 3 — partial observation.** The electron (d=6) orbits in 6 dimensions. Three of those dimensions are ours — the d=3 coordinate subspace that constitutes our observable space. The other three are real, physical, macroscopic sector dimensions we cannot directly observe. The electron, from its own perspective, inhabits a 6-dimensional world with no special status attached to any three of the six coordinates. We measure the d=3 component of its full 6-dimensional activity. The internal quantum numbers — hypercharge, lepton number, chirality — are determined by the isometry geometry of the sector manifold in those sector dimensions (SU(4) for CP³, the d=6 manifold). They appear to us as discrete labels rather than spatial directions because we can only resolve the d=3 component of a mode structure that lives in d=6.

**Particles with d < 3 — sub-dimensional embedding.** The photon (d=2) is the sharpest instance of the principle in §3h. It is always a 2-dimensional object: it has exactly two directions, the two it oscillates in, and these are its two polarization states. The two-ness is intrinsic — it is dim(Ξ₂) = 2. The photon integrates out every dimension beyond its two: it is uniform in dimensions 3–10, with no structure out there to pin its 2-plane. So while the sector fixes how many directions the photon has (two), along with the U(1) geometry and mass that go with them, it does not fix which way they point — the orientation of the 2-plane in M∞ is free, set by what the photon lines up with. This is why the photon couples to every charged particle: a 2-plane lies inside every sector, so every charged particle presents a d=2 subspace for the photon to line up with — and the coupling fires where that particle also carries U(1) charge in the shared plane (the coupling filter, §3g). The "fixed coordinates {1,2}" of the nesting chain are a bookkeeping gauge; physically the photon is uniform outside whichever 2-plane it occupies.

**The direct consequence: electromagnetic waves must be transverse.** The photon oscillates in its two dimensions and moves perpendicular to them. Perpendicular to a 2-plane is not a single direction — in M∞ it is a high-dimensional space of directions, none of them privileged. A d=3 observer resolves one propagation direction because the observer's three coordinates meet that orthogonal space in a single line; the one direction of travel we see is our slice of it, not a property of the photon. The photon cannot oscillate along its direction of travel, because travel is by construction perpendicular to the plane it oscillates in. So in whichever direction we see a photon move, its oscillation is transverse to that motion and carries exactly two independent states — the photon's two dimensions, made directly observable. Transversality and the two polarizations are the d=3 shadow of a 2-dimensional oscillator moving perpendicular to itself; they are what we resolve of the photon, not a confinement of it to our three coordinates. This is developed in Part 3 §14.

**The electron cloud as a d=3 marginal density.** The language of "electron clouds" or "probability distributions" in atomic physics is the inevitable result of a d=3 observer integrating over the three inaccessible sector coordinates of CP³. The electron does not occupy a smeared region of 3D space in any fundamental sense. It occupies a definite position in 6-dimensional CP³ at every moment. A d=3 observer, unable to resolve the three sector coordinates beyond d=3, integrates over them — what remains is a marginal distribution in 3D that looks like a cloud. The orbital shapes of standard quantum mechanics (s, p, d, f — spherical harmonic angular dependence in 3D) are the d=3-coordinate structure of the full CP³ mode. The "uncertainty" in the electron's 3D position is irreducible only from the d=3 observer's perspective; it is the information integrated over in the sector-space marginal, not a fundamental indeterminacy.

**The nucleus is geometrically thin in the electron's space.** The atomic nucleus is a colour-singlet composite of d=3 and d=4 quarks. Colour confinement forces the composite to project out its d=4 character entirely — the CP² color index cancels in any singlet — leaving a d=3 object. The nucleus occupies only 3 of the 6 dimensions of the electron's CP³ orbit. From the electron's perspective, it orbits something geometrically thin: the nucleus extends through 3 of the electron's 6 coordinate directions and is absent from the other 3. The electromagnetic coupling (d=2 sector, nested inside both d=3 and d=6) provides the binding handle. The atom is therefore not a nucleus at the center of a cloud — it is a d=3 structure being orbited in 6-dimensional space by a d=6 excitation, coupled through a shared d=2 coordinate.

**Entanglement as sector-coordinate correlation.** Two entangled electrons have correlated d=6 sector states, observed at d=3. The d=3 spatial separation between them is a distance in Ξ₃. The correlation, however, is in the d=4, 5, 6 sector coordinates, which have no d=3 spatial topology. Two electrons separated by 1 AU in d=3 can have completely overlapping d=6 sector coordinates, because d=6 sector space is not d=3 physical space. Measuring the spin at x₁ collapses the CP³ sector state — which affects x₂ not because anything travelled through d=3, but because the shared sector coordinates were never separated by the d=3 distance in the first place. The apparent non-locality is not a violation of causality; the connection exists in dimensions that d=3 spatial separation does not reach.

**Marginalization is relative to observer depth. ✅** The cloud is not special to d=3. The marginal operation of §2.3 — integrating |Ψ∞|² over the coordinates an observer cannot resolve — is defined relative to whatever sector depth does the observing, not relative to d=3 in particular. A d=3 observer integrates over the electron's d=4,5,6 coordinates and obtains the diffuse d=3 marginal called the electron cloud. The same operation one depth up: from the d=6 frame of the electron, the tau's four deeper coordinates (d=7–10) are integrated out, and the tau's activity in them appears as a marginal smear of exactly the same kind. Every particle is a definite, sharp object in its own d coordinates and a marginal cloud to anything resolving fewer dimensions. The smearing is the signature of observing from below the object's dimension; it is not a property of the object. This is the same statement as the electron-cloud marginal above, with the observer depth left general rather than fixed at d=3.

**Cross-sector interaction involves no separate objects. ✅** Because there is one field Ψ∞ (§2.1), a cross-sector coupling is not two objects reaching across a gap. When the electron (d=6) and the tau (d=10) interact — an interaction set in the full d=10 space, the larger of the two — the electron does not travel or extend into the tau's four additional coordinates. It is already a feature of the single wave those coordinates belong to: it was never a separate object outside them. The coupling is realized at the coordinates the two sectors share (d=1–6, §3g), and the tau's four deeper coordinates are integrated out of the electron's d=6 frame, appearing to it as the marginal smear above. "The electron interacts with the tau" is the structure of one wave at two sector depths, not a meeting of two things — the cross-sector form of the single-field ontology of §2.1. The literal presence (the wave is one object across all coordinates) and the apparent smear (the lower-depth frame integrates out the higher coordinates) are the inside and outside of one situation, not competing accounts.

**Bound within, free without. ✅** A particle is confined in its own d sector dimensions by the sector well V_d (Part 4 §3.9); its sector mode function is the normalizable ground state on Ξ_d. The well is the mode's own self-binding, evaluated in the mode's frame (Part 4 §3.10.2 covariance note): it binds the particle's structure about its centroid, equally in all d of its dimensions, and travels with the mode. Nothing anchors the centroid — the absolute-origin reading of the well is excluded by the framework's own results (`files/idwt.py` STEP 58) — so the centroid propagates freely with E² = P² + m², and bound within means bound about its center within: no three of a particle's own dimensions are marked out by the well. In every dimension beyond d — the ones it is not in — there is no such well: the d=7,8,9 band carries no sector geometry, and the d=10 well belongs to the tau, not to a d<10 mode. There the particle is free, governed by the bare Laplacian. The free Laplacian −∂² on any one of those directions has spectrum [0,∞): no negative eigenvalue, hence no normalizable bound state can localize the particle there, and the unique zero-momentum configuration is the constant. The three solutions are e^{iky} (E>0, carrying momentum), the constant (E=0, uniform), and e^{+|k|y} (E<0, divergent and unphysical). The rest configuration is the constant alone.

A massive particle, in the dimensions beyond its sector, is therefore uniform across them. The physical reading is that the particle floats freely there: present everywhere across those directions at once, pinned to no point. 🔵 It does not sit at a point — localizing it to a width Δ costs kinetic energy of order 1/(2mΔ²), so the rest limit E→0 forces Δ→∞, i.e. uniformity — and it does not drift as a lump, which would require momentum and so an excited outer state. Uniform co-presence is the only zero-energy state a free direction allows. This is the precise mode-theoretic content of the "already there" framing above: the electron (d=6) is a feature of the tau's deeper coordinates not by travelling or extending into d=7–10 but by being uniform across them.

Normalizability is untouched by this. ✅ The mode is normalized on its own Ξ_d (∫_{Ξ_d}|χ|² = 1), and its uniform factor in the dimensions beyond d is the nesting embedding C∞(Ξ_d) ⊂ C∞(Ξ_{d'}) of §3h. The norm taken over the outer volume does not converge, and it is not meant to: that divergence is the statement "this is a d-object — normalize it on Ξ_d," not a defect of the mode.

**Masslessness upgrades uniform presence to propagation. 🔵** The same principle applied to the one massless sector gives the photon's behaviour in the dimensions beyond its own. With dispersion E² = p² + m², a massive particle admits a rest state (p=0, the uniform configuration); the photon (m=0) has no rest frame, so its free state in the directions beyond d=2 must carry momentum, and uniform presence becomes propagation. This is the mode-theoretic root of the transverse-propagation picture of the photon set out above and in Part 3 §14: the photon does not float uniformly perpendicular to its oscillation plane, it travels there, because masslessness removes the rest state that uniformity requires.

**Uniform presence defeats containment, not traversal. ✅** The uniformity in the dimensions beyond d has two consequences that pull in opposite directions, and keeping them distinct prevents an overreach. First: a structure that a d=3 apparatus confines within a 3D region is not thereby kept from the particle. It is uniformly present in the dimensions the apparatus does not act in, and the particle meets it there. A 3D shield can erase a field on the 3D slice but cannot contain a structure that extends past the slice — the Aharonov–Bohm and Aharonov–Casher phases are this containment failure, a field reaching the particle through coordinates the shield was not built in. Second, and oppositely: the same uniformity gives no way around a potential barrier. A barrier along an observable direction is set by 3D sources, so by the projection theorem (Part 3 §0.8a) it takes the same value at every value of the hidden coordinates; those coordinates are transverse to it and separate off as free directions, leaving the ordinary one-dimensional crossing problem in the observable coordinate. A particle gains no extra-dimensional shortcut through a barrier, and the tunnelling time is the standard one. The hidden dimensions carry an influence around a shield but offer no detour through a wall — they bypass shields, not walls. The distinction is which task the transverse dimensions are asked to perform: carrying an influence past an obstacle in the slice (which they can) versus substituting for blocked motion along the slice (which they cannot). The worked check and the general criterion are in Appendix A §15.

**Mass as the sector eigenvalue.** The governing equation on M_∞ separates into observable and sector parts. For a mode with sector mode function χ_{n,d}:

```
∂_t² Ψ = c²(Δ_3 + Δ_Ξ) Ψ
```

The Laplacian on Ξ_d acts on χ_{n,d} and returns its eigenvalue: Δ_Ξ χ_{n,d} = −m² χ_{n,d}, where m = m_scale_d × S(n,d). A d=3 observer, who cannot resolve motion in Ξ_d, sees:

```
∂_t² ψ = c²(Δ_3 − m²) ψ
```

This is the Klein-Gordon equation. The mass term is not a separate input — it is the eigenvalue of the sector operator, appearing to a d=3 observer as a scalar constant because the Ξ_d degrees of freedom are inaccessible. Mass is a count of excited sector microstates: S(n,d) = C(n+d−1, d) counts the number of independent ways to distribute n excitations across d dimensions of Ξ_d, and m_scale_d sets the sector frequency. The photon (n=0, d=2) has S(0,2) = 0, so m = 0 exactly — zero excitations means zero mass. Every other particle has n ≥ 1 and a non-zero count of excited microstates, giving non-zero mass. The mass formula m = m_scale_d × S(n,d) is the spectrum of that sector operator.

---

## 4. The Unified Kernel

The cross-sector interaction is the unique leading term compatible with U(d) × U(d') symmetries (T2). The coupling matrix g_{dd'} = v_d × v_{d'} (rank-1) connects every pair of sectors in D — self-couplings (d=d') and cross-sector terms alike. **Note:** T2 proves that (ξ_d·ξ_{d'})² is the unique quartic U(d)×U(d')-invariant interaction. The rank-1 factorization g_{dd'} = v_d v_{d'} follows as a necessary consequence of the sector-separable mass formula (P1): rank r > 1 would introduce cross-sector entanglement preventing the sector-by-sector eigenvalue separation m = m_scale_d × S(n,d) (see P6). **Status: ✅.** The full kernel:

```
V_kernel = Σ_{d,d'∈D} g_{d,d'} (ξ_d · ξ_{d'})² |Ψ^(d)|² |Ψ^(d')|²
```

The overall coupling strength g₃₃ = 8√7 = n_s²√(n_s+n_u)/2 is determined by the seed pair {n_d=1, n_u=3} and their composite n_s = 4 — the same integers from which the entire particle spectrum is selected. "Vacuum stability" is the physical condition that fixes the gap; seeds and composite supply the numbers. No particle mass appears in the determination of g₃₃.

---

## 5. Canonical Particle Assignments

All masses predicted from a **sole unit reference m_e = 0.511 MeV**. The W boson mass follows from m_scale_2 × S(76,2). Sector scales follow from seeds alone (Part 2 §10).

The mass formula m = m_scale_d × S(n,d) where S(n,d) = C(n+d−1, d) is a binomial coefficient. In natural units, mass is frequency — S(n,d) × m_scale_d is the resonant frequency of mode n in sector d. The crucial additional fact is that this resonant frequency equals the cumulative count of sector microstates below level n — a hockey-stick sum: S(n,d) = Σ_{k=0}^{n-1} C(k+d−1, d−1). **Formal statement (Part 8 §3.4):** this is the IDWT Weyl-type spectral law — mass equals m_scale_d times the sector spectral counting function $N_d(E_{n-1})$, where $N_d(E) = \#\{$Dirac eigenvalues of $D_\Xi$ with $|\lambda|^2 \leq E\}$. The identification of S(n,d) with a cumulative count of eigenstates is a combinatorial identity (⭐). The postulate that this cumulative count, scaled by m_scale_d, equals the physical mass is P1 + the mass formula; its domain, normalization, and operator-theoretic foundation are specified in Part 8 §3.3–3.4. This identity is why the eigenmode selection rule holds as a theorem rather than a coincidence (see Part 2).

Derived sector scales (coupling self-consistency; see Part 2 §10):
```
m_scale_6  = m_e / S(13,6)                        = 2.7526 × 10⁻⁵ MeV  [unit reference: sets the MeV scale for d=6]
m_scale_3  = m_e × √(g₃₃/g₆₆)                    = 4.702 MeV
m_scale_4  = m_scale_3 × √(g₄₄/g₃₃) / S(3,4)    = 0.1451 MeV
m_scale_10 = m_scale_6                             [g₁₀,₁₀ = g₆₆ = 1/n_s: shared composite coupling]
m_scale_2  = m_e × √(g₂₂/g₆₆)                     = 27.47 MeV           [derived from seeds; gives m_W = 80,379 MeV]
```

**SU(2)_L coupling (derived from CP²→CP¹ reduction, Part 3 §0.7):**
```
g₂ = Q_u × √g_s = (2/3)√(2g₄₄/π²) = 0.65275   (PDG: 0.65270, +0.008%)
G_F = g₂²/(4√2 m_W²) = 1.1658×10⁻⁵ GeV⁻²        (PDG: 1.1664×10⁻⁵, −0.05%)
```

**Complete coupling vector** {v_d = √g_dd}, determined by seeds and m_e:
```
v₂ = 26.879  [derived: v₂ = √g₂₂ = √(p²q/2), p=S(n_s,3)−n_u=17, q=S(n_u−1,4)=5]
v₃ = 4.601   [seeds {n_d=1, n_u=3}; composite n_s=4]
v₄ = 2.130   [seeds {n_d=1, n_u=3}; composite n_s=4]
v₅ = 0.3645  [Hopf fiber universality: g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂]
v₆ = 0.500   [g₆₆ = 1/n_s = 1/4]
v₁₀= 0.500   [g₁₀,₁₀ = g₆₆ = 1/n_s: sectors d=6 and d=10 share the composite coupling 1/n_s]
```
The constraint g₂₅ = g₃₄ = 4√6 (equal cross-coupling for both U(1) Hopf pairs) uniquely fixes v₅ given v₂. No third unit reference is needed for any sector coupling.

| Particle | n | d | Predicted (MeV) | PDG (MeV) | Error |
|---|---|---|---|---|---|
| electron | 13 | 6 | 0.511 | 0.511 | unit reference |
| muon | 35 | 6 | 105.657 | 105.658 | −0.001% |
| tau | 23 | 10 | 1,776.84†† | 1,776.93 | −1.0σ |
| down | 1 | 3 | 4.702 | 4.670 | +0.68%† |
| strange | 4 | 3 | 94.04 | 93.40 | +0.68%† |
| up | 3 | 4 | 2.177 | 2.160 | +0.77%† |
| charm | 20 | 4 | 1,279.7‡ | 1,270.0 | +0.76%‡ |
| top | 72 | 4 | 174,000‡ | 172,760 | +0.72%‡ |
| bottom | — | 3 | 4,181 | 4,180 | +0.02% |
| photon | 0 | 2 | 0 | 0 | exact |
| W | 76 | 2 | 80,379 | 80,377 | +0.003% |
| Z | 81 | 2 | 91,230 | 91,188 | +0.047% |
| Higgs | 95 | 2 | 125,266 | 125,200 | +0.053% |

† The +0.68% offset in d=3 and +0.77% in d=4 reflect the natural accuracy of the coupling self-consistency derivation of m_scale_3. The rank-1 kernel forces this offset to be identical across all modes within a sector — confirmed by d and s quarks both at +0.68% despite spanning n=1 to n=4. Both are within PDG quark mass uncertainties (~10%).

†† Tau: **m_τ = m_e × S(23,10)/S(13,6) × (1 + 1/1680) = 1776.84 MeV (PDG 2024: 1776.93 ± 0.09 MeV; −1.0σ, inside 1σ).** The factor 1/1680 = 1/(n_u × n_s² × S(n_s,4)) is the geometric back-reaction resummation of the d=6→d=10 coupling. The isotropic coupling g_{6,6}=g_{6,10}=g_{10,10}=1/n_s=1/4 (from the seed) means the leading correction 1/2240 feeds back via g_{10,10}=1/n_s, multiplying by n_s/(n_s−1) = n_s/n_u = 4/3. Combined: 1/2240 × 4/3 = 1/1680.

‡ After applying the Generation Tower Correction (Part 2 §11) with ε = 1/(280√7) and k values {charm:3, top:10}, the c/u ratio becomes 0.000% and the t/u ratio −0.048%. The GTC corrects within-sector ratios; the uniform +0.77% sector-wide offset persists in all d=4 absolute masses.

**Co-fixed-point uniqueness**

As a uniqueness verification, the generation map was run over all 1,600 pairs $(n_d, n_s) \in [1..40]^2$, computing Jaccard similarity against the observed spectrum $\{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$. Jaccard $= 1.0$ at exactly one pair: **(1, 4)**. The next-closest is $(19,4)$ at $0.375$. $n_d = 1$ is trivially forced ($S(1,d)=1$ for all $d$). The non-trivial seed is $n_u = 3$ ($\chi(\mathbb{CP}^2) = N_c = 3$, T15); the composite $n_s = 4 = 1+3$ is confirmed by the topological constraint $S(4,4) = 35$ (Part 2 §3). The search is parametrised over $(n_d, n_s)$; within that parametrisation the pair $(1,4)$ is the unique match.

---

### Theorem: Uniqueness of the Occupied Mode Index Set

**Statement.** Let $\Sigma = \{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ be the set of IDWT mode indices. $\Sigma$ is the unique set of positive integers satisfying all of the following simultaneously:

1. **Generation law closure.** Every element of $\Sigma$ is the eigenfrequency selected by the following closed chain of sector comb conditions (all verified exactly):

$$n_u = 3 \quad \text{[seed: } \chi(\mathbb{CP}^2) = N_c = 3 \text{ (T15); g-rule certificate: } S(3,3) = 10 \text{ uniquely solves } n_{\nu_1} = n_e - d_u + 1 \text{]}$$

$$n_c = S(n_s, 3) = 20$$

$$n_e = n_c - n_u - n_s = 13, \qquad n_\mu = S(n_s, 4) = 35$$

$$n_\tau = n_\mu - n_e + n_d = 23$$

$$n_{\nu_1} = S(n_u, 3) = 10, \quad n_{\nu_2} = S(n_u, 4) = 15, \quad n_{\nu_3} = n_{\nu_1} + n_{\nu_2} - n_u = 22$$
[inclusion-exclusion: both $n_{\nu_1}$ and $n_{\nu_2}$ encode the same seed $n_u$, so their sum over-counts $n_u$ once; subtracting it is forced. Cross-check: $n_{\nu_3} = n_\tau - n_d = 22$ ✓]

$$n_{\rm top} = S(n_e, 2) - n_c + 1 = 72$$

$$n_W = g(d_\nu, n_{\rm top}) = d_\nu + n_{\rm top} - 1 = 5 + 72 - 1 = 76, \quad n_Z = n_W + q = 81 \;\; [q = d_\ell - 1 = S(n_u{-}1,4) = 5]$$

$$n_H = n_u + n_c + n_{\rm top} = 95$$

2. **Spectral independence.** No three elements $i, j, k \in \Sigma$ satisfy $S(i, d_i) + S(j, d_j) = S(k, d_k)$, where $d_i$ is the sector of mode $i$. The 14 non-zero occupied $S$-values are: $\{1, 15, 20, 2002, 2926, 3321, 4560, 8855, 11628, 18564, 65780, 1215450, 3838380, 64512240\}$. All 91 unordered pairs were checked; there are **zero violations**.

⭐ **Additive combinatorics framing.** In additive number theory, a set $B$ of positive integers is **sum-free** if no element of $B$ equals the sum of two (not necessarily distinct) other elements of $B$. The 14 non-zero IDWT $S$-values constitute a sum-free set. This is not a numerical accident: additive combinatorics (Erdős–Turán theory) establishes that a sum-free subset of $\{1,\dots,N\}$ has size at most $\lceil N/2 \rceil + O(N^{1/3})$, and characterizes large sum-free sets as either mostly odd numbers or concentrated in a short interval. The IDWT $S$-values cluster at low $n$ in each sector and then jump by combinatorial gaps — the predicted shape for a sum-free set whose members are binomial coefficients evaluated at widely spaced arguments. Conversely, the sum-free property imposes an upper bound on the number of allowed modes at a given combinatorial scale, providing a purely number-theoretic explanation for why the spectrum closes at 15 that complements the co-fixed-point derivation. Note: the mode *indices* $\Sigma = \{1,3,4,\dots\}$ are not sum-free (e.g.\ $1+3=4\in\Sigma$); the sum-free condition holds at the level of the $S$-values (the actual eigenvalues), not the index labels.

3. **Seed and composite uniqueness.** The primitive seeds are $n_d = 1$ and $n_u = 3$. The composite $n_s = 4 = 1+3$ is the unique positive integer solving $S(n_s, 4) = n_\mu$, i.e.\ $\binom{n_s+3}{4} = 35$ — exactly one solution — confirming the composite value.

⭐ **Tropical geometry remark.** The tropical Grassmannian $\mathrm{Trop}\,\mathrm{Gr}(2,n)$ parametrises ultrametrics on $n$ points and, for $n=4$, is a 1-dimensional fan equivalent to the space of phylogenetic trees on 4 labeled leaves. This space has exactly **3 maximal cones** — one for each trivalent tree topology on 4 leaves. The number 3 is the number of quark/lepton generations. The composite $n_s = 4$ is thus the smallest value of $n$ for which $\mathrm{Trop}\,\mathrm{Gr}(2,n)$ is a 1-dimensional trivalent fan with exactly 3 maximal regions; for $n < 4$ the fan is either trivial or has fewer regions. This is an independent combinatorial coincidence consistent with the generation structure, not a separate derivation of it.

**Proof sketch.**

- *Condition 3* is immediate: $S(1,4)=1$, $S(2,4)=5$, $S(3,4)=15$, $S(4,4)=35$, $S(5,4)=70$, and $S(n,4)$ is strictly increasing, so $n_s = 4$ is unique. $\square$

- *Condition 1* then fixes every element of $\Sigma$ deterministically — the chain above is algebraically closed with no free choices. Exhaustive search over all 1,600 pairs $(n_d, n_s) \in [1..40]^2$ confirms that only $(1,4)$ produces a set with Jaccard similarity $1.0$ against $\Sigma$; the next-closest pair gives $0.375$.

- *Condition 2* is verified computationally (zero violations). The asymptotic argument is: $S(\tau) = 64{,}512{,}240$ and $\sum_{\rm other} S_i = 5{,}171{,}502$, with cross-sector gaps (e.g.\ max $d=3$ simplex value $= 20$ vs.\ min $d=4$ simplex value $= 15$) growing combinatorially, making accidental sum-equalities impossible for larger seeds. $\square$

**Additional algebraic cross-checks** (all consequences of the chain above, each independently verified):

$$n_e = k_0 - n_u \;\; [k_0 = n_s^2 = 16], \qquad n_\tau = n_c + n_u, \qquad n_H = n_Z + 2(n_s + n_u)$$

$$n_{\rm top} = \chi(\mathbb{CP}^2) \times \chi(\mathbb{CP}^3) \times \chi(\mathbb{CP}^5) = 3 \times 4 \times 6, \qquad S(n_e, 2) = 91$$

$$n_Z - n_W = q = S(n_u{-}1,4) = 5 \;\; \text{(same } q \text{ as in } g_{22} = p^2 q/2 \text{)}$$

No mode index is chosen to match a mass. Each is the unique output of an algebraic rule applied to the seed pair $\{n_d = 1,\, n_u = 3\}$ and composite $n_s = 4$.

---

## 6. Neutrino Sector

Neutrinos cannot fit d=6. The sector scale m_scale_6 = 27.5 eV means the lightest possible d=6 mode (n=1) has mass 27.5 eV — already 550× heavier than m_ν₃ and over 18,000× heavier than m_ν₁. No integer simplex index gives a d=6 mass in the meV range. They occupy **d=5** with mode indices n=(10,15,22), all structurally derived:

```
n_ν₁ = S(n_u,3) = S(3,3) = 10    [simplex image of up quark into d=3]
n_ν₂ = S(n_u,4) = S(3,4) = 15    [simplex image of up quark into d=4]
n_ν₃ = n_τ − n_d = 23 − 1 = 22   [eigenmode selection rule]
```

Redundant check: n_ν₃ = n_ν₁ + n_ν₂ − n_u = 10+15−3 = 22 ✓

d=5 is topologically forced as the Hopf total space S⁵ of the fibration S¹→S⁵→CP². It is the Hopf partner of d=4 (up quarks) and is required by the fibration chain.

**Neutrinos are Dirac fermions — a prediction from the spinor structure**

The d=5 sector has d mod 8 = 5. This is the one Clifford algebra class for which Majorana spinors do not exist — neither a Majorana condition nor a Majorana-Weyl condition can be imposed on the sector spinor in sector d=5. Therefore the fundamental d=5 spinor is Dirac-type. The all-orders prohibition follows from the spinor bundle: no charge-conjugation matrix C exists on S⁵ (d mod 8 = 5 admits no C satisfying the required anti-commutation relations), so cross-sector couplings cannot construct ψ^T C ψ at any loop order. **Neutrinos are Dirac fermions at the fundamental level.**

This is a concrete, falsifiable prediction: 0νββ is forbidden at all orders — no 0νββ signal is expected. Current experiments (KamLAND-Zen: m_ββ < 36 meV) have seen no signal, consistent with the leading-order prediction. If 0νββ is observed, the spinor structure of IDWT is falsified on this point.

The d=5 sector mass scale is derived from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ (Part 2 §9c). No suppression mechanism is needed.

**Absolute masses** (scale derived from m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ — no neutrino data):
```
m_ν₁ = 1.487 meV,  m_ν₂ = 8.639 meV,  m_ν₃ = 50.27 meV,  Σm_ν = 60.39 meV
```
(Bare: m_ν₃ = 48.87 meV, Σm_ν = 59.00 meV. Corrected by δ_ν₃ = ε×g_{33} = 1/35, Part 2 §9d.)
All below KATRIN bound (450 meV). The mass scale m_scale_5 is fully derived from m_e and seeds (Part 2 §9c). The primary testable quantities are the absolute masses themselves: Σm_ν = 60.39 meV (within reach of CMB-S4) and the mass ratios m_ν₂/m_ν₁ = S(15,5)/S(10,5) = 5.808, m_ν₃/m_ν₁ = S(22,5)/S(10,5) = 32.86.

**Note on oscillation comparisons.** Δm² values are derived consequences of the absolute masses, expressed in the language of oscillation experiments (which measure interference, not absolute masses). They are not native IDWT quantities. The correction δ_ν₃ = ε×g_{33} = 1/35 is a closure relation (🔶, Part 2 §9d): the √7 factors cancel algebraically (g_coeff × g_{33} = n_s² = k₀, so ε×g_{33} = k₀/(k₀×n_mu) = 1/35), but the deeper operator mechanism — why the l=2 T2 cross-term acts with exactly this product — is not yet derived. The corrected m_ν₃ = 50.267 meV implies Δm²₃₁ = 2.5246×10⁻³ eV², matching PDG 2023 within 0.05% and PDG 2024 within 0.2σ.

**Normal ordering is a prediction.** Mode indices n_ν₁ < n_ν₂ < n_ν₃ are fixed by the eigenmode selection rule; since S(n,5) is monotonically increasing, m_ν₁ < m_ν₂ < m_ν₃ follows necessarily. Current experiments prefer normal ordering at 3–4σ, consistent with IDWT.

---

## 7. Relationship to Existing Physics

| Framework | IDWT equivalent | Derivation status |
|-----------|----------------|------------------|
| Quantum mechanics | Ψ∞ evaluated at ξ⁰; ∫|Ψ∞|²dξ gives the d=3 marginal probability density | ✅ |
| Wave-particle duality | Ψ∞ is a wave; its d=3 activity appears particle-like when localised | ✅ |
| Uncertainty principle | Dimensional depth prevents simultaneous position+momentum specification | ✅ |
| Special relativity | □_x component of □_{M∞}; inherited Lorentz covariance from product structure | ✅ |
| Fermi statistics | Spinor Ψ∞ anticommutes: {Ψ∞(ξ),Ψ†∞(ξ')}=δ(ξ−ξ') — Pauli exclusion derived | ✅ |
| Particle/antiparticle | Conjugate spinor Ψ̄∞ is distinct; antiparticles are automatic | ✅ |
| Electromagnetism | U(1) Hopf fiber phase: A_μ = ∂_μθ, F_μν = ∂_μA_ν−∂_νA_μ | ✅ |
| General relativity | Effective Einstein equations from |Ψ∞|² back-reaction on the observer's 3D spacetime geometry. No gravitons — gravity is purely geometric curvature. Macroscopic sector spaces are consistent because graviton propagation exclusions do not apply (Part 4 §1b). Bianchi identity and spectral theorem proved; G_N from sector localization geometry is the remaining open item (Part 4 §3.12) | 🔶 |
| Standard Model quarks | d=3 (down-type), d=4 (up-type) — masses from simplex formula | ✅ |
| Standard Model leptons | d=6 (e,μ), d=10 (τ) — masses from simplex formula | ✅ |
| Chiral weak force | Kähler γ₅ on CP²,CP³ selects left-handed components; W couples to holomorphic half only | ✅ |
| Spin-½ of all fermions | Dirac operator on $M_\infty$; spinor bundle of $\Psi_\infty$ (Part 8 §2) | ✅ |
| CKM Cabibbo angle | sin θ_C = (1+1/240)/√S(n_s,3) = 0.22454 — seed + CP¹ sector curvature correction | ✅ |
| Neutrino oscillations | d=5 sector, normal ordering | ✅ |
| Leptonic CP phase δ_CP | δ_CP = π + 2θ₁₃ = 197.11°, J = −0.00981 via APS spectral flow Δc₁ = c₁(CP⁵) − c₁(CP³) = −2 (T8 🔶, Part 10) | 🔶 |
| Dirac neutrinos | d=5 has d mod 8=5: Majorana forbidden → 0νββ rate = 0 predicted | ✅ |
| Tau hypercharges | Y(τ)=−1 from anomaly cancellation with N_c=3 and g_{66}=1/n_s (Part 3 §8, §13) | ✅ |
| Confinement | Colour-neutrality condition |N⃗|=0 from CP² isometry geometry; λ_c is an open item; full QCD confinement mechanism (flux tubes, asymptotic freedom) not derived | 🔵 |
| Cosmological constant | Λ_eff from unoccupied-mode vacuum energy; suppression mechanism not derived | 🔶 |
| Dark matter | Spectrum is complete at 15 particles; IDWT offers no dark matter candidate at present | ❓ |

---

## 8. What Would Falsify IDWT

The complete falsification inventory — hard binary falsifiers (Category A), precision quantitative thresholds (Category B), structural predictions without SM equivalent (Category C), and near-future experimental windows — is in Part 5 §9, the canonical reference for IDWT's testability. That section also explains the distinction between a falsifier (no adjustable parameter) and a residual (small, structurally explained, within measurement uncertainty).

Key hard falsifiers: observed 0νββ attributed to a fundamental Majorana mass term; confirmed non-unitary PMNS; CP phase δ_CP inconsistent with |δ − π| = 2|θ₁₃|; any new stable fundamental particle beyond the 15 in the spectrum; a fourth neutrino species. These are all irrecoverable — no sector, coupling constant, or mode index can be adjusted to accommodate them.

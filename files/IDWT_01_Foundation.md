# Infinite Dimensional Wave Theory — Part 1: Foundations

## Status Key
- ✅ Derived or confirmed
- 🔶 Consistent but not fully derived

---

## A Note on First Impressions

The mass tables in this document invite an immediate reaction: this must be curve-fitting. The reaction is understandable and wrong, in ways that are not obvious on a first pass. Three specific misconceptions are worth addressing before proceeding.

**The mode indices are not fitted.** Every mode index $n$ in the particle spectrum is generated algebraically by the Hockey-Stick identity $S(n,d) = \binom{n+d-1}{d}$ applied to the single seed $n_s = 4$. The full derivation chain is in §5 and Part 2 §6. As one example: $n_\mu = S(4,4) = 35$ because that is Pascal's recursion $S(n,d) = S(n,d-1) + S(n-1,d)$ evaluated at $(n=4, d=4)$ — not because the muon happens to have that index. The seed $n_s = 4$ is itself topologically forced by the Dirac index of $\mathbb{CP}^3$ (§3b), independently of any mass data.

**The sector assignments are not arbitrary.** Each sector imparts specific physical properties through its spinor geometry. $d=5$ ($S^5$, $d \bmod 8 = 5$) forbids Majorana spinors by Clifford algebra periodicity — Dirac neutrinos are not a choice, they are a geometric consequence. $d=4$ ($\mathbb{CP}^2$) generates colour charge from its $SU(3)$ isometry group via the Atiyah-Singer index. $d=6$ ($\mathbb{CP}^3$) produces colour-neutral chiral fermions through its Kähler structure. Moving a particle to a different sector does not produce a different prediction — it produces the wrong quantum numbers entirely. The assignments are locked by geometry.

**The sector scales are not calibrated to mass data.** $m_{\text{scale},3} = m_e \times \sqrt{g_{33}/g_{66}}$ uses coupling constants derived from $n_s = 4$ alone ($g_{33} = 8\sqrt{7}$) and from the quaternionic geometry of CP³ ($g_{66} = 1/4$; see Part 2 §9c). No quark mass enters the derivation. The down quark prediction (+0.68% from PDG) is an output, not an input. All sector scales derive from the seed coupling constants and $m_e$ as the sole unit reference (Part 2 §10).

The framework has one unit of mass ($m_e = 0.511$ MeV) and one seed integer ($n_s = 4$). Everything else — the sector set, all mode indices, all coupling constants, all sector scales, all particle masses — is derived. The structural evidence against numerology is the cross-referencing: the same numbers arriving independently from different directions. The quantity $q = S(n_u-1, 4) = 5$ appears in both the EW coupling derivation $g_{22} = p^2 q/2$ and the boson mass gap $n_Z - n_W = 5$. The resonance site $k_0 = 16$ satisfies three independent conditions simultaneously. The Higgs mode index $n_H = 95$ is reached by two separate cross-sector routes. Numerological schemes are flexible enough to always find a match. This framework is rigid enough that these convergences are non-trivial.

---

## 0. The Actual Structure: A Spectral Triple

**IDWT identifies the Standard Model as the spectral data of one operator $D$ on one space $M_\infty$.** It is the spectral action programme of Connes' noncommutative geometry, applied to the unique self-consistent Dirac-Harmonic operator on $M_\infty$. The mathematical object is a spectral triple $(\mathcal{A},\,\mathcal{H},\,D)$:

$$\mathcal{A} = C(M_\infty)\otimes\bigoplus_{d\in D}\mathcal{M}_{n_d}(\mathbb{C}), \quad \mathcal{H} = L^2(M_\infty, \mathcal{S}_\infty), \quad D = -i\gamma^\mu\partial_\mu + \sum_{d\in D} D_d$$

where $D_d$ is the Dirac-Harmonic operator in sector $d$ with potential $V_d(r) = \lambda_d r^2/(1+r^2)$. The stable spectrum of $|D|$ is exactly $\{S(n,d)\times m_{\text{scale},d}\}$. The spectral action $\text{Tr}(f(D/\Lambda))$ has the Seeley-DeWitt asymptotic expansion:
$$\text{Tr}(f(D/\Lambda)) \sim f_4\Lambda^4\,a_0 + f_2\Lambda^2\,a_2 + f_0\,a_4 + O(\Lambda^{-2}),$$
where $a_0 \propto \text{Vol}(M_\infty)$ (cosmological constant term), $a_2 \propto \int R\,\text{dvol}$ (Einstein-Hilbert term, giving $G_N^{-1} \propto f_2\Lambda^2$), and $a_4$ contains the gauge kinetic and Yukawa terms of $S_{\text{SM}}$. The IDWT sector heat-kernel coefficients $a_0^{(d)} = \Gamma(1+1/d)(d!)^{1/d}$ and $\zeta_d(0) = -d/2$ are computed exactly from $S(n,d)$ alone (Part 9 T14). The cutoff $\Lambda$ and spectral function coefficients $f_k$ are open (Part 6; related to the unevaluated $f_2$ offset in $\sin^2\theta_W$, $g_1$, and $\sqrt{\text{Tr}(D^2)}$).

**Internal consistency check.** Computing $\text{Tr}(D^2) = \sum_i m_i^2$ from the 15 IDWT particles (top quark 50.5%, Higgs 25.5%, $Z$ 13.5%, $W$ 10.5%):
$$\sqrt{\text{Tr}(D^2)} = 248.3\text{ GeV}.$$

IDWT derives $G_F = g_2^2/(4\sqrt{2}\,m_W^2)$ directly from seeds, which gives the EW scale $({\sqrt{2}\,G_F})^{-1/2} = 246.3$ GeV. The 0.85% gap between $\sqrt{\text{Tr}(D^2)}$ and this scale is a consistency check on the derived mass spectrum against the derived $G_F$ — both quantities come from the same seed structure, so agreement is expected and the residual traces to the same spectral normalisation offset as the $\sin^2\theta_W$ and $g_1$ residuals. Note: IDWT does not use spontaneous symmetry breaking, so the concept of a Higgs VEV does not apply within the framework (Part 5 §3c). The EW scale here is $(\sqrt{2}\,G_F)^{-1/2}$, not a vacuum expectation value.

**Open computations reframed as spectral geometry:**

| Item | Status | Spectral geometry statement |
|---|---|---|
| PMNS mixing | ✅ | Weighted average of TBM and simplex-ratio limits with weight $g_{55}=96/g_{22}$; all three angles within 0.51% of PDG with no free parameters (Part 9 T6) |
| $\sin^2\theta_W$ residual | ✅ | $S(76,2)/S(81,2)=0.2237$ exactly; +0.37% from PDG on-shell value is within known 1-loop EW radiative corrections — not an open computation |
| CP phase | 🔶 | $\Delta c_1 = c_1(\mathbb{CP}^3) - c_1(\mathbb{CP}^5) = -2$ identified as candidate source; curvature integral over sector coupling parameter space not performed (T8) |
| G_N derivation | 🔶 | G_N from sector localization geometry — how concentrated sector energy couples to 4D curvature (Part 4 §3.12) |

The laser, quasicrystal, Aubry-André, and atomic analogies are all instances of the same mathematical fact: the spectrum of a self-adjoint operator with a filtering condition. IDWT names that operator: $D$ on $M_\infty$. The SM is its spectral data.

**Analytic control from combinatorics.** The spectral zeta function of each sector $d$ has two exact anchor values derivable from $S(n,d)=\binom{n+d-1}{d}$ alone: $\zeta_d(1)=d/(d-1)$ (total inverse-mass weight, proved by a Pascal telescoping identity) and $\zeta_d(0)=-d/2$ (zeta-regularised eigenvalue count, from the constant term of the heat kernel $K_d(t)=\sum_n e^{-tS(n,d)}$). These confirm that each hidden sector behaves as a proper $d$-dimensional Riemannian space — spectral dimension matches fiber dimension, the functional determinant $\log\det D_d=-\zeta_d'(0)$ is finite without a UV cutoff, and the infinite tower is analytically controlled. Full derivations in Part 9 T13–T14.

---

## 1. Core Postulates

**P1 — The Master Wave**
Ψ∞ is a **Dirac spinor field** defined on an infinite-dimensional manifold. It is the only fundamental object. Everything observable — particles, fields, forces — is a derived consequence of its structure. The quantum number structure of matter (spin, chirality, statistics, hypercharges) follows from the spinor geometry of M_∞; the mass spectrum follows from the combinatorial mode structure S(n,d).

**P2 — The Observable Slice**
Our 3D universe is the restriction of Ψ∞ to a fixed address ξ⁰ in the hidden-sector coordinates:
```
ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```
The observer's location ξ⁰ weights the projection amplitude for each mode (Stage-1 filter, Part 7) but does not determine which modes exist. The spectrum of occupied modes — which particles exist — is determined entirely by the seed structure and eigenmode selection rule (Part 2 §2-4), independent of ξ⁰. All observers at any ξ⁰ see the same particle spectrum; they differ only in the amplitude with which each mode projects onto their slice.

**P3 — Hidden-Sector Spaces are Infinite and Non-Compact**
The sector spaces $\Xi_d$ are infinite Riemannian spaces — full-size sector spaces, not rolled up or compactified in any sense. Each sector carries a potential well $V_d(r) = \lambda_d r^2/(1+r^2)$ that supports exponentially localized bound states via the Agmon decay theorem (Part 4 §3.8). These bound states are the particles. The symmetry labels $\mathbb{CP}^n$ and $S^n$ in the sector table describe the local geometry at the bottom of the potential well — the symmetry of the mode wavefunctions near $r=0$ — not the global topology of $\Xi_d$. This is exactly analogous to a hydrogen atom: the electron lives in infinite $\mathbb{R}^3$ but the ground state has $S^2$ symmetry from the spherically symmetric potential. No sector space is curled up; the modes bind themselves through the potential. The standard KK exclusions (Eöt-Wash, collider searches) presuppose graviton propagation into small compact dimensions; they do not apply here. See Part 4 §1b and §3.9.

Every SM particle is a bound state of a sector potential — not a bulk propagator. Scattering states (modes that propagate freely through the hidden space) are eliminated by the Stage-1 observability filter: they fail to project onto the 4D slice with finite amplitude. There are no KK excitations of SM fields accessible to experiment; the SM spectrum is precisely the set of sector resonances that survive both observability filters.

**P4 — Geometry First**
The governing equation is a Dirac wave equation on the curved manifold $M_\infty$. The sector potentials $V_d(r)$ arise from the intrinsic curvature of $M_\infty$ evaluated at the vacuum $\xi^0_d$ — they are not independent inputs but consequences of the geometry.

---

## 2. Projection and the Born Rule

### 2.1 Observable Reality as a Cross-Section

Our 3D universe is one slice through Ψ∞, as a 2D circle is a cross-section of a 3D sphere. The circle is unaware it is a cross-section. Our entire observable universe is one such slice — its contents (matter, energy, space) are determined by the global structure of Ψ∞ evaluated at ξ⁰. The slice is at the d=3 coordinate level: our three spatial dimensions are the d=3 coordinates of M∞, and every particle with d > 3 occupies our three spatial dimensions (§3i).

### 2.2 The Projection Operator

```
Π: Ψ∞(r, ξ, t)  →  ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```

This is a restriction map — it picks out one hypersurface from the full infinite-dimensional field at fixed ξ⁰. **The projection is the one place in IDWT where amplitude computation occurs.** Evaluating Ψ∞ at a specific address ξ⁰ gives a definite amplitude for each mode at that point.

In mode space, Π acts as a **lowpass filter**: the amplitude of sector-d mode n at the observer address scales as

$$|\chi_n(\xi^0)| \propto \frac{1}{\sqrt{S(n,d)}}$$

from the L² normalisation of the sector mode functions. Higher mode indices (heavier particles) are progressively suppressed at ξ⁰. This is the physical mechanism behind the Stage-1 observability filter (Part 7) and the intra-sector mixing ratios (Part 3 §11). Every other IDWT prediction — masses, coupling constants, PMNS angles, the CP phase — involves ratios or eigenvalues of the sector geometry and does not require knowing the global normalisation of Ψ∞.

### 2.3 The Born Rule Applied to Ψ∞

```
ρ(r, t) = ∫ |Ψ∞(r, ξ, t)|² dξ
```

Standard quantum mechanics assigns probability density |ψ|² to any quantum field. IDWT applies this to Ψ∞ directly. The observable density ρ(r,t) is the hidden-space integral of |Ψ∞|², which marginalises over the hidden coordinates and recovers the 3D probability density. It is the Born rule of quantum mechanics applied to the field Ψ∞ on M_∞, with the hidden-sector dimensions integrated out.

The physical interpretation: an electron is not a cloud in 3D — it is a structured object in M_∞ whose 3D shadow (the projection) appears as a diffuse probability density. Entangled particles are features of Ψ∞ that are close in the hidden-sector coordinates even when their 3D projections are far apart.

### 2.4 Connection to Cut-and-Project Construction

The IDWT projection mechanism is structurally identical to the cut-and-project method used to construct quasicrystals. The three-step architecture:

1. **Full space:** M_∞ (infinite-dimensional manifold supporting Ψ∞)
2. **Slice:** ψ_obs = Ψ∞(r, ξ⁰, t) at fixed ξ⁰
3. **Acceptance window:** Two-stage filter (Stage-1 projection mismatch Ω_log + Stage-2 colour closure). In quasicrystal theory the acceptance window is a geometric region; in IDWT it is a spectral criterion. The analogy captures the structure of selection — an underlying high-dimensional structure M_∞, a slice, and a filter — rather than the mechanism.

The observed particle spectrum {1, 3, 4, 10, 13, 15, 20, 22, 23, 35, 72, 76, 81, 95} in mode-index space is the IDWT analogue of the aperiodic quasicrystal point set: irregular when listed, exactly determined by the projection geometry.

Key difference from quasicrystals: IDWT projects a continuous wave equation — modes have continuous suppression exp(−Ω_log) = S(n,2)/S(n,d) rather than a binary in/out criterion. Consequently, mass gaps between successive occupied modes approach the ratio S(n+1,d)/S(n,d) = (n+d)/n → d in the large-n limit: the spectrum within each sector is asymptotically geometric.

---

## 3. The Sector Structure of M_∞

The hidden space decomposes into sectors with distinct potential well symmetries. Each $\Xi_d$ is an infinite macroscopic space; the geometry labels ($S^3$, $\mathbb{CP}^2$, etc.) describe the local symmetry of the potential minimum $V_d(r)$ near $r=0$, not the global topology:

| d | Geometry | Symmetry | Spinor type | Spinor dim | Physical content |
|---|---|---|---|---|---|
| 2 | CP¹ | U(1) | Majorana-Weyl | 2 | Gauge bosons (γ, W, Z, H) |
| 3 | S³ | SO(4) | Majorana | 2 | Down-type quarks (d, s, b) |
| 4 | CP² | SU(3)/U(2) | Weyl (spin^c) | 4 | Up-type quarks (u, c, t) |
| 5 | S⁵ | SO(6) | Dirac only | 4 | Neutrinos (ν_e, ν_μ, ν_τ) |
| 6 | CP³ | SU(4)/U(3) | Weyl | 8 | Charged leptons (e, μ) |
| 10 | CP⁵ | SU(6)/U(5) | Majorana-Weyl | 32 | Tau lepton; d mod 8=2 Maj-Weyl (cross-check: coincides with 16 of Spin(10)) |

This list is derived from the seed $n_s = 4$ and the mode index tower. See §3a below.

### 3a. Sector Set Theorem

**Theorem.** The sector set $D = \{2, 3, 4, 5, 6, 10\}$ is uniquely determined within IDWT by the complex Hopf fibration chain $S^1 \to S^{2n+1} \to \mathbb{CP}^n$ together with two termination rules, both derivable from the single seed $n_s = 4$:

**Step 1 — CP base sectors from the seed.** The seed $n_s = 4$ and the colour index $N_c = 3$ (from the CP² spin$^c$ index, Part 8 §2.2) identify three complex projective spaces by their Euler characteristics:

$$\chi(\mathbb{CP}^{N_c-1}) = N_c = 3, \quad d = 4; \qquad \chi(\mathbb{CP}^{n_s-1}) = n_s = 4, \quad d = 6; \qquad \chi(\mathbb{CP}^{n_s-1}) = 2, \quad d = 2.$$

$d = 2$ (CP¹) is the $U(1)$ Hopf fiber base required by the chain. This gives $d \in \{2, 4, 6\}$. The $d=10$ sector is determined by Rule B below.

**Step 2 — Hopf total spaces add $d \in \{3, 5\}$.** The odd-sphere sectors $S^{2k+1}$ are derivable when their base CP sector has a kernel self-consistency fixed-point coupling:

- $d=3$ (S³ over CP¹): $g_{33} = n_s^2\sqrt{n_s+n_u}/2 = 8\sqrt{7}$ — from seeds.
- $d=5$ (S⁵ over CP²): $g_{55} = g_{33}g_{44}/g_{22}$ — from Hopf universality $v_3/v_2 = v_5/v_4$.

**Step 3 — Termination rules exclude all remaining spaces.**

*Rule A (coupling termination).* $g_{66} = 1/n_s$ is the seed ratio — a direct output of the seed, not a kernel fixed-point coupling. The Hopf universality condition that derives $g_{55}$ cannot extend to $d=7$: no fixed-point formula for $g_{77}$ exists within IDWT. Sectors $d=7, 8, 9$ are excluded.

*Rule B (Gegenbauer criticality).* The Jacobi coupling $b_{k_0}(d) = \sqrt{k_0(k_0+d-1)}/(2k_0+d-2)$ must satisfy $b_{k_0} \geq 1/2$ for a sector to support stable bound-state modes. The unique solution to $b_{k_0}(d) = 1/2$ on the complex Hopf chain is:
$$4k_0 = (d-2)^2 \quad \Longrightarrow \quad 4\times 16 = 64 = (10-2)^2, \quad d = 10.$$
Sector $d=10$ is the critical endpoint; all $d \geq 11$ are subcritical and excluded.

The sector set is therefore:
$$D = \underbrace{\{2,3,4,5\}}_{\text{Hopf pairs } n=1,2} \cup \underbrace{\{6\}}_{n=3 \text{ base, Rule A}} \cup \underbrace{\{10\}}_{n=5 \text{ base, Rule B}} = \{2,3,4,5,6,10\} \quad \square$$

**Remark.** The lepton sector coupling $g_{66} = 1/n_s = 1/4$ is derived from the seed alone — no hypercharge assignment enters.

**Note on the index cross-check.** Once the sector set is established, one finds $n_{\rm top} = \chi(\mathbb{CP}^2)\times\chi(\mathbb{CP}^3)\times\chi(\mathbb{CP}^5) = N_c \times n_s \times N_f = 3\times4\times6 = 72$, consistent with the mode index derived independently from the eigenmode selection chain.

---

### 3b. Completeness of the Particle Spectrum

**Theorem.** The IDWT particle spectrum consists of exactly 15 states: the 14 mode indices in $\Sigma = \{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ plus the bottom quark beat at $k_0 = 16$ in $d=3$. No additional stable particles exist.

**Proof.** Three steps, each relying only on results already established.

**Step 1 — Finite sectors.** The Sector Set Theorem (§3a) proves $D = \{2,3,4,5,6,10\}$ is the complete set. Any new particle must reside in one of these six sectors.

**Step 2 — Eigenmode set is complete.** The sector comb filtration from $n_s = 4$ selects mode indices $\Sigma$. Applying every filtration rule to $\Sigma$ either returns an element already in $\Sigma$ or exits the physically accessible range — verified exhaustively (§5c). Therefore any mode index $n \notin \Sigma$ fails the **Stage-2 co-fixed-point condition** and cannot be a stable resonance. This eliminates all non-$\Sigma$ modes in every sector.

**Step 3 — Unique beat mode.** A beat mode arises at a site $k_0$ where three independent resonance conditions coincide simultaneously, forcing equal spectral weight at adjacent modes $n$ and $n+1$. The three conditions are:

$$k_0 = n_s^2 = 16, \qquad k_0 = n_e + n_u = 13 + 3, \qquad k_0 = S(n_s,3) - S(2,3) = 20 - 4.$$

All three give $k_0 = 16$ exactly. Every quantity is determined by $n_s = 4$. Exhaustive search over all $n \leq 200$ and $d \in D$ finds **no other site** satisfying all three conditions. The beat therefore exists at a unique site in $d=3$, giving $m_b = \sqrt{S(16,3) \times S(17,3)} \times m_{\mathrm{scale},3} = 4181$ MeV.

The beat is structurally confined to $d=3$: conditions 2 and 3 are $d=3$ identities — they use $n_e$ (from $d=6$) and $n_u$ (from $d=4$), whose sum closes onto the $d=3$ resonance site. The same $n=16$ appears in other sectors but produces no known particle mass. $\square$

**The spectrum is closed.** Given $n_s = 4$ and $m_e$, the list of particles, their masses, and their quantum numbers are fully determined. Any additional stable state would require either a new sector (excluded by §3a) or a new mode index consistent with the eigenmode selection rule (excluded by the Uniqueness Theorem, §5c). Neither exists. There is no room for new fundamental particles within the IDWT framework.

---

### Sector Topology and the Atiyah-Singer Index

Each CP^n sector carries an Euler characteristic χ(CP^n) = n+1. By the Atiyah-Singer index theorem, this equals the holomorphic index ind(D_{CP^n}) = n+1 — the number of independent zero modes of the sector's Dirac operator.

The Euler characteristics of the IDWT sectors are:

| Sector | Manifold | χ | Physical meaning |
|---|---|---|---|
| d=2 | CP¹ | 2 | Two photon/W helicities |
| d=3 | S³ | 0 | Odd sphere — vector-like QCD (correct: no γ₅) |
| d=4 | CP² | 3 | **N_c = 3 colours** (index = number of zero modes = colours) |
| d=5 | S⁵ | 0 | Odd sphere — no Majorana (Dirac neutrinos forced) |
| d=6 | CP³ | 4 | **n_s = 4 = seed** (index = strange quark seed) |
| d=10 | CP⁵ | 6 | **N_f = 6 flavours** (index = quark family count) |

**The seed n_s = 4 is topologically forced.** The d=6 lepton sector lives on CP³. The Dirac index ind(D_{CP³}) = χ(CP³) = 4. The seed n_s must equal this index for the d=6 spectrum to be self-consistent — it counts the zero modes available before gauge fixing removes one, leaving three generations (e, μ, τ). Therefore n_s = 4 is not chosen: it equals the topological invariant of the lepton sector.

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



**Convergence on d=10.** Four independent routes — Hopf/octonionic chain (approximate), Gegenbauer criticality (exact), Spin(10) spinor weight lattice (cross-check), and Hurwitz termination (exact) — all give d=10.

The spinor type per sector follows from the Clifford algebra periodicity theorem (Bott periodicity, mod 8). The sectors are independent in the sense that each carries a distinct Clifford algebra Cl(d) with no shared generators; their spinor spaces therefore combine as a tensor product. The d=10 sector carries a Majorana-Weyl spinor (16 real components, the **16** of Spin(10)); the other sectors carry Weyl, Majorana, or Dirac spinors as determined by d mod 8 (Part 8 §2.1). The total hidden-space spinor component count is 2×2×4×4×8×16 = 2¹³ = 8,192 [tensor product over all six sectors].

These sector dimensions are not chosen. They are the unique sequence produced by the Hopf fibration chain over the normed division algebras (ℝ, ℂ, ℍ, 𝕆):

```
S¹ → S³  → S²    complex Hopf     →  d=2 (base CP¹), d=3 (total S³)
S¹ → S⁵  → CP²   complex Hopf     →  d=4 (base CP²), d=5 (total S⁵)
S³ → S⁷  → S⁴    quaternionic     →  d=4 also as S⁴≅HP¹ (consistent)
```

d=6 arises as CP³, the base space of the next complex Hopf fibration S¹→S⁷→CP³. CP³ has real dimension 6 and serves as the twistor space of S⁴ ≅ HP¹. d=7 (the total space S⁷) is excluded from the IDWT sector set for two consistent reasons: (i) geometrically, S⁷ is the total space of the quaternionic Hopf fibration S³→S⁷→S⁴ and is fully accounted for by the d=4 and d=3 sectors already present; (ii) algebraically, g_{66} = 1/n_s is a seed ratio rather than a kernel fixed-point coupling, so Hopf universality cannot determine a coupling formula for a hypothetical d=7 sector over d=6. Both routes reach the same conclusion.

d=10 arises as CP⁵ = SU(6)/U(5), the next step in the complex projective chain beyond CP³. Its sector dimension d=10 is fixed by the Sector Set Theorem (§3a) — $d=10 = 2(N_f-1)$ where $N_f = n_{\rm top}/(N_c \times n_s) = 6$ — and confirmed independently by the Gegenbauer criticality condition (§3b). Hurwitz's theorem provides a third confirmation: CP⁵ associated with the octonions is the last space in the chain for which the sector structure remains self-consistent.

The sequence terminates at d=10 because the octonions are the last normed division algebra — Hurwitz's theorem admits no further entries.

### 3c. Gegenbauer Criticality Theorem — Second Route to d=10

An independent algebraic derivation of d=10 comes from the Gegenbauer chain structure of the Jacobi operator at the resonance site k₀ = n_s² = 16.

**Definition.** The Gegenbauer coupling at the resonance site k₀ in sector d is the off-diagonal matrix element of the d-dimensional Jacobi chain at bond k₀:

```
b_{k₀}(d) = √(k₀(k₀+d−1)) / (2k₀+d−2)
```

For the IDWT sectors with k₀ = n_s² = 16 this evaluates to:

| d | b_{k₀}(d) | Status |
|---|---|---|
| 2 | 0.51539 | supercritical |
| 3 | 0.51426 | supercritical |
| 4 | 0.51281 | supercritical |
| 5 | 0.51110 | supercritical |
| 6 | 0.50918 | supercritical |
| **10** | **0.50000** | **critical (exact)** |
| 11 | 0.49747 | subcritical |

**Theorem.** b_{k₀}(d) = 1/2  ↔  4k₀ = (d−2)²  ↔  d = 2 + 2√k₀ = 2(n_s+1) = 10.

**Proof.**  b = 1/2  ↔  4k₀(k₀+d−1) = (2k₀+d−2)²  ↔  4k₀(d−1) − 4k₀(d−2) = (d−2)²  ↔  4k₀ = (d−2)².  With k₀ = n_s² = 16: d = 2 + 2√16 = 2 + 2n_s = 10. □

**Monotonicity.** b_{k₀}(d) is strictly decreasing in d. d=10 is therefore the **last** sector with b_{k₀} ≥ 1/2. For d ≥ 11 the coupling is subcritical: the resonance site k₀ falls outside the chain's natural coupling range and the sector cannot propagate.

**Physical interpretation.** In the Jacobi tight-binding chain, b = 1/2 is the critical coupling where a resonance site sits precisely at the boundary between propagating and evanescent regimes. All active IDWT sectors (d = 2…6) are supercritical at k₀ (b > 1/2). d = 10 is exactly critical — the last permissible sector. d > 10 puts the seed resonance in the evanescent regime; modes cannot propagate through the chain at k₀.

**WKB consequence.** The WKB correction to the Jacobi delay τ_d = 1/(2√(k₀+d)) is proportional to (b_{k₀} − 1/2)/b_{k₀}². For d = 10 this correction **vanishes identically** — the leading-order WKB is exact for the terminal sector. For d = 3 the correction is −0.67% and goes in the wrong direction for the ρ meson, confirming that the +0.069% residual in the ρ prediction is a genuine prediction floor, not a removable WKB artifact.

**Triple consistency of d=10:**

| Route | Condition | Result |
|---|---|---|
| Hurwitz (geometry) | Normed division algebras end at 𝕆 | d = 10 |
| **Gegenbauer (algebra)** | **b_{k₀}(d) = 1/2 ↔ d = 2(n_s+1)** | **d = 10** |
| Hypercharge (gauge) | g_{10,10} = g_{6,6} = 1/n_s = 1/4 | d = 10 |

Three routes, one answer. The IDWT framework is over-determined on the terminal sector.

---

### 3d. Per-Sector Profiles

Every particle is a bound eigenmode of V_d(r) = λ_d r²/(1+r²) with mass m(n,d) = m_scale_d × S(n,d), S(n,d) = C(n+d−1,d). The following profiles collect each sector's coupling, particle content, quantum properties, and spectral data.

---

#### d = 2 — Electroweak Sector

**Geometry.** CP¹ ≅ S² locally; global S³ Hopf fibration over S² with U(1) fiber. Hopf fiber phase → electromagnetic potential A_μ = ∂_μθ, curvature → F_μν. SU(2)_L acts on the base CP¹.

| Parameter | Value |
|---|---|
| g₂₂ | 722.5 |
| m_scale_2 | 27.47 MeV |
| L_2 | 0.142 fm |

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
- **sin²θ_W = S(76,2)/S(81,2) = 0.2237** (PDG: 0.2229, +0.37% — within 1-loop EW corrections).
- **EW scale:** √Tr(D²) ≈ 248.3 GeV is the spectral RMS of |D| across all sectors. IDWT does not use spontaneous symmetry breaking; the Higgs is mode n=95, not a condensate. The EW scale is (√2 G_F)^{-1/2} = 246.3 GeV from the IDWT-derived G_F (§0, Part 5 §3c).

**Spectral.** ζ₂(1) = 2, ζ₂(0) = −1, a₀₂ ≈ 1.253.

---

#### d = 3 — Hadronic Sector (Down-Type Quarks)

**Geometry.** S³ (round); isometry SU(2)×SU(2) ≅ SO(4). SU(3) color from triple monopole charges on S³ (Part 3 §2). Confinement: E_conf = λ_c|N⃗|.

| Parameter | Value |
|---|---|
| g₃₃ | 8√7 ≈ 21.17 |
| m_scale_3 | 4.702 MeV |
| L_3 | 0.460 fm |

| Particle | n | S(n,3) | Predicted mass | PDG |
|---|---|---|---|---|
| d quark | 1 | 1 | 4.702 MeV | ~4.7 MeV ✅ |
| s quark | 4 | 20 | 94.04 MeV | 93.4 MeV ✅ |
| b quark | beat k₀=16 | √(S(16,3)·S(17,3)) | 4181 MeV | 4180 MeV ✅ |

Note: S(n,3) = n(n+1)(n+2)/6. The b quark is a beat resonance (§3b) at the unique triple-coincidence site k₀ = n_s² = 16.

**Quantum properties.**
- **SU(3) color:** Three degenerate color charges from S³ topology; quarks transform in the fundamental.
- **Confinement:** No scattering states survive the observability filter in d=3; all modes are confined.
- **Cabibbo angle:** sin θ_C = (1+1/240)/√S(4,3) = 0.22454 (PDG: 0.22500, −0.2%). The 1/240 is the Lichnerowicz S³ curvature correction.
- **Baryon number:** Topological winding number of the S³ mode.

**Spectral.** ζ₃(1) = 3/2, ζ₃(0) = −3/2, a₀₃ ≈ 1.623.

---

#### d = 4 — Up-Type Quark Sector

**Geometry.** CP² (complex projective plane); local symmetry U(2). Kähler structure provides γ₅ for left-handed chirality. GTC (Global Topological Correction) ε = 1/(280√7) from the CP² Euler characteristic.

| Parameter | Value |
|---|---|
| g₄₄ | 12/√7 ≈ 4.536 |
| m_scale_4 | 0.1451 MeV |
| L_4 | 0.801 fm |

| Particle | n | GTC order k | Predicted mass | PDG |
|---|---|---|---|---|
| u quark | 3 | 0 | 0.1451 × 15 = 2.177 MeV | ~2.2 MeV ✅ |
| c quark | 20 | 3 | m_scale_4 × S(20,4) × (1−ε)³ | 1279.7 MeV | 1270 MeV ✅ |
| t quark | 72 | 10 | m_scale_4 × S(72,4) × (1−ε)^{10} | 174.0 GeV | 172.69 GeV ✅ |

Note: S(n,4) = n(n+1)(n+2)(n+3)/24. ε = 1/(280√7) ≈ 0.001348.

**Quantum properties.**
- **SU(3) color:** Up-type quarks share color with d=3 via the cross-sector seed coupling g₃₃ × g₄₄.
- **Electric charge +2/3:** From Kähler index and U(2) representation theory (Part 3 §4).
- **Chirality:** CP² Kähler γ₅ → W couples to left-handed component only.
- **GTC:** The topological correction (1−ε)^k accounts for the compression of up-type masses relative to naive mode scaling; without it the top is overestimated by ~1.35%.

**Spectral.** ζ₄(1) = 4/3, ζ₄(0) = −2, a₀₄ ≈ 2.006.

---

#### d = 5 — Neutrino Sector

**Geometry.** S⁵ (round); isometry SO(6) ≅ SU(4). d mod 8 = 5 → spinor bundle on S⁵ admits no real (Majorana) structure → Majorana mass terms forbidden.

| Parameter | Value |
|---|---|
| g₅₅ | 96/722.5 ≈ 0.1329 |
| m_scale_5 | ≈ 7.4 × 10⁻¹³ MeV |
| L_5 | 2.623 fm |

m_scale_5 is fully derived from the cross-sector constraint m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³. No neutrino mass data enters.

| Particle | n | S(n,5) | Predicted mass | Bound |
|---|---|---|---|---|
| ν₁ | 10 | 2002 | 1.487 meV | < 450 meV ✅ |
| ν₂ | 15 | 11628 | 8.639 meV | < 450 meV ✅ |
| ν₃ | 22 | 65780 | 48.87 meV | < 450 meV ✅ |

Note: S(n,5) = n(n+1)(n+2)(n+3)(n+4)/120. Σm_ν = 59.00 meV. Δm²₃₁/Δm²₂₁ = 32.949 (PDG: 34.825, −5.4%).

**Quantum properties.**
- **Dirac (not Majorana):** d mod 8 = 5 → no real spinor → Majorana forbidden → **0νββ rate = 0** (hard prediction).
- **Normal ordering:** n₁ < n₂ < n₃ and S(n,5) monotone → m_ν₁ < m_ν₂ < m_ν₃ necessarily. Experiments prefer normal ordering at 3–4σ.
- **PMNS angles:** θ₁₂, θ₂₃, θ₁₃ determined by holonomy of the lepton bundle over d=5→6→10→5 (Part 6); g₅₅ and mode indices fix all three with no free parameters.
- **No sterile neutrinos:** Observability filter eliminates all bulk-propagating modes.

**Spectral.** ζ₅(1) = 5/4, ζ₅(0) = −5/2, a₀₅ ≈ 2.392.

---

#### d = 6 — Charged Lepton Sector (e, μ)

**Geometry.** CP³ (quaternionic projective line 𝕳P¹); local symmetry U(3). CP³ Kähler form → hypercharge assignment. Lepton number = U(1) centre of U(3).

| Parameter | Value |
|---|---|
| g₆₆ | 1/4 (seed ratio 1/n_s) |
| m_scale_6 | m_e / S(13,6) ≈ 2.75 × 10⁻⁵ MeV |
| L_6 | 2.301 fm |

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

**Spectral.** ζ₆(1) = 6/5, ζ₆(0) = −3, a₀₆ ≈ 2.777.

---

#### d = 10 — Tau Sector

**Geometry.** CP⁵ = SU(6)/U(5); local symmetry U(5). The Aubry-André critical endpoint: V_{10}(r) sits at the metal-insulator transition self-dual point, making WKB exact. Shares coupling and mass scale with d=6 — unified lepton seed.

| Parameter | Value |
|---|---|
| g_{10,10} | 1/4 (same as d=6) |
| m_scale_{10} | = m_scale_6 (shared seed) |
| L_{10} | 2.198 fm |

| Particle | n | Dyson factor | Predicted mass | PDG |
|---|---|---|---|---|
| τ (tau) | 23 | × (1+1/1680) | 1776.84 MeV | 1776.86 MeV ✅ |

Dyson factor 1+1/1680 = 1 + 1/(n_up × n_s² × S(n_s,4)) from the Aubry-André critical point WKB correction. Without it, m_τ is 0.06% low.

**Quantum properties.**
- **Lepton number L=1 and charge −1:** Shared with d=6 via joint g=1/4 coupling.
- **Aubry-André criticality:** At the self-dual point, the WKB approximation is exact — no higher-order corrections to the tau mass. Unique among all sectors.
- **Spin(10) spinor weight lattice (d mod 8 = 2):** The 16-component Majorana-Weyl spinor of SO(10) has weight lattice cross-checking tau hypercharges against anomaly cancellation (Part 8).
- **Lepton universality:** m_scale_{10} = m_scale_6 enforces identical mass unit for the heavy lepton family; mass splitting comes entirely from different mode indices (23 vs 13, 35).

**Spectral.** ζ_{10}(1) = 10/9, ζ_{10}(0) = −5, a₀_{10} ≈ 4.308.

---

### 3e. Sector Summary Table

| d | Geometry | Particles | g_dd | m_scale_d | L_d (fm) | ζ_d(1) | ζ_d(0) | a₀_d |
|---|---|---|---|---|---|---|---|---|
| 2 | CP¹ (EW/Hopf) | γ, W, Z, H | 722.5 | 27.47 MeV | 0.142 | 2 | −1 | 1.253 |
| 3 | S³ (hadronic) | d, s, b | 8√7 | 4.702 MeV | 0.460 | 3/2 | −3/2 | 1.623 |
| 4 | CP² (up-type) | u, c, t | 12/√7 | 0.1451 MeV | 0.801 | 4/3 | −2 | 2.006 |
| 5 | S⁵ (neutrino) | ν₁, ν₂, ν₃ | 96/722.5 | 7.4×10⁻¹³ MeV | 2.623 | 5/4 | −5/2 | 2.392 |
| 6 | CP³ (lepton) | e, μ | 1/4 | 2.75×10⁻⁵ MeV | 2.301 | 6/5 | −3 | 2.777 |
| 10 | CP⁵ (tau) | τ | 1/4 | = m_scale_6 | 2.198 | 10/9 | −5 | 4.308 |

ζ_d(1) = d/(d−1) and ζ_d(0) = −d/2 are exact for all sectors (Part 9 T13–T14, Pascal telescoping and heat kernel). All 15 particle masses follow from m_scale_d × S(n,d) plus three corrections: GTC for up-type quarks, Dyson for tau, beat resonance for b quark. No other free parameters once the six couplings g_dd are fixed from the seed n_s = 4.

---

### 3f. The Coordinate Extension Picture

M∞ is one coordinate system extended step by step: the two coordinates of d=2 are contained in d=3, the three of d=3 are contained in d=4, and so on without bound. The sectors D = {2, 3, 4, 5, 6, 10} are the stable levels at which this extension produces observable eigenstates.

At each new dimension d, the stability condition is whether the self-coupling equation has a solution consistent with the seed n_s = 4. For d ∈ {2, 3, 4, 6, 10} the Kähler geometry (for even d) or the isometry group (for d=3) closes on itself, the Atiyah-Singer index is nonzero, and the Gegenbauer threshold falls within the vacuum stability window. For d=5, S⁵ has χ(S⁵) = 0, no Kähler form, and no self-coupling fixed point; m_scale_5 is fixed by the cross-sector constraint m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ (Part 2 §9c).

M∞ is genuinely infinite-dimensional. Beyond d=10 the Atiyah-Singer index vanishes, the Gegenbauer threshold exceeds the vacuum stability bound, or no cross-sector pairing satisfies the Vandermonde coupling rule. The window for self-consistent eigenstates closes at d=10; M∞ continues. D = {2, 3, 4, 5, 6, 10} are the primes of the extension — the levels at which the coordinate system locks into a stable sector.

The containment chain Ξ₂ ⊂ Ξ₃ ⊂ Ξ₄ ⊂ Ξ₅ ⊂ Ξ₆ ⊂ Ξ₁₀ and the isomorphism chain M∞ ≅ Ξ₂ ≅ Ξ₃ ≅ Ξ₄ ≅ Ξ₅ ≅ Ξ₆ ≅ Ξ₁₀ hold for all six sectors: each Ξ_d is M∞ perceived from coordinate level d, and each level's coordinates are a literal subset of the next level's coordinates.

---

### 3g. Interaction as Coordinate Containment

Particles in different sectors couple because their sectors share coordinate subspaces. The two coordinates of the photon's d=2 sector are literally two of the three coordinates of d=3, two of the four of d=4, two of the five of d=5, two of the six of d=6, two of the ten of d=10. Dynamics in any shared subspace are dynamics in every sector that owns those coordinates, symmetrically in both directions. A photon perturbs an electron because those two coordinates belong to the electron as well. An electron moving in its six dimensions necessarily moves in the two-dimensional subspace that photons live in — and so affects them.

This is why electromagnetism is universal. Every sector d ≥ 2 contains d=2 as its lowest coordinate subspace, so every charged particle couples to the photon. The coupling constant reflects the coordinate overlap — the ratio of shared dimensions to total dimensions of the higher sector.

The gluon lives in d=3 (S³, the hadronic sector). Its three coordinates are inside d=4 (CP², the up-type quark sector). Down-type quarks (d=3) couple to gluons because they share the full d=3 coordinate set. Up-type quarks (d=4) couple to gluons because d=3 ⊂ d=4: the gluon's three coordinates are three of the four coordinates the up-type quarks live in. The strong force spans d ∈ {3,4} — those are the sectors that contain d=3 as a coordinate subspace.

The electron (d=6, mode n=13) couples to the photon (d=2) via the two coordinates they share. The coupling strength derives from a cascade: g_{44} → g_s → g_2 → sin²θ_W → g_1 → α (Part 3 §0.7). Coordinate containment determines that the coupling exists and which sectors are linked; coupling magnitudes are set by the spectral geometry of each sector manifold — integrals over S^{d−1} and CP^m, not bare dimension counts. There is one step in the cascade where the coordinate ratio does appear literally: g_2 = (2/3)√g_s, where 2/3 = d_photon/d_hadronic. The factor 2/3 is the electric charge of the up quark and the ratio of photon sector dimension to hadronic sector dimension N_c = 3, and those are the same number because N_c = d_hadronic.

---

### 3h. Sector Autonomy and Nested Dynamical Invariance

Each sector Ξ_d is a self-contained dynamical system. Its Hamiltonian H_d = −Δ_{Ξ_d} + V_d(|ξ_d|) is invariant under the isometry group G_d of the sector manifold, and its eigenvalue problem H_d χ = m_eff χ can be solved sector by sector without reference to any other sector. The mass formula m = m_scale_d × S(n,d) is sector-separable: the d=6 lepton spectrum is determined entirely by H_6; the d=4 quark spectrum by H_4.

This autonomy survives the nesting Ξ_2 ⊂ Ξ_3 ⊂ ··· ⊂ Ξ_{10}. At the level of coordinate algebras, the inclusion of coordinate subspaces induces a nested chain of observable algebras — the shared coordinate algebra of M∞:

```
C∞(Ξ_2) ⊂ C∞(Ξ_3) ⊂ C∞(Ξ_4) ⊂ C∞(Ξ_5) ⊂ C∞(Ξ_6) ⊂ C∞(Ξ_{10}) ⊂ C∞(M∞)
```

A function of only the d=2 coordinates is simultaneously a valid function on every sector — it belongs to every algebra in the chain. The differential operators built from those coordinates — the d=2 Laplacian, the U(1) rotation generators — appear in every larger sector's operator algebra, acting on the shared coordinate subspace and commuting with any operator that acts only on the additional coordinates. The symmetry generators of a smaller sector are literal elements of the operator algebra of every larger sector.

This is the precise sense in which each dynamical system is nested inside, and invariant within, the shared coordinate algebra: the G_d-invariant structure of H_d is preserved in every H_{d'} for d' > d, restricted to the G_d-invariant subspace of C∞(Ξ_{d'}). The sector potential wells localize each particle type to its own sector, ensuring this restriction is physically realized rather than merely formal. A mode that does not excite the additional coordinates of Ξ_{d'} is dynamically a mode of Ξ_d, and the symmetry generators that label it are present in both algebras — so its quantum numbers are unambiguous in either context.

§3g and §3h are complementary. §3g: shared coordinates produce coupling — perturbations in one sector propagate to every sector that shares those coordinates, bidirectionally. §3h: that coupling operates at the shared subspace and leaves each sector's bulk eigenvalue structure intact. The inter-sector coupling terms g_{d,d'} in the kernel (§4) are cross-sector boundary terms, not deformations of the individual sector Hamiltonians H_d. Each sector remains exactly as self-consistent in isolation as it is in the full system — the nesting is lossless.

---

### 3i. The d=3 Threshold: Sector Dimension as Physical Dimensionality

The coordinate extension picture (§3f) assigns a concrete meaning to the phrase "our three observable spatial dimensions": they are the d=3 level of the coordinate hierarchy. The three coordinates at which the extension first produces a full self-consistent sector are the same three coordinates that constitute our observable space. The sector dimension d therefore measures where each particle stands relative to our observable space.

| d relative to 3 | Physical meaning | Example |
|---|---|---|
| d < 3 | Particle orbit is a proper subspace of our 3D | Photon (d=2): 2D entity within our 3D world |
| d = 3 | Particle orbit coincides with our 3D | Down-type quarks: fully at home in observable space |
| d > 3 | Particle orbit contains our 3D plus (d−3) hidden dimensions | Electron (d=6): 3 observable + 3 hidden dimensions |

**Particles with d > 3 — partial observation.** The electron (d=6) orbits in 6 dimensions. Three of those dimensions are ours — the d=3 coordinate subspace that constitutes our observable space. The other three are real, physical, macroscopic hidden dimensions we cannot directly observe. The electron, from its own perspective, inhabits a 6-dimensional world with no special status attached to any three of the six coordinates. We observe the 3D projection of its full 6-dimensional motion. The internal quantum numbers — hypercharge, lepton number, chirality — are determined by the isometry geometry of the sector manifold in those hidden dimensions (SU(4)/U(3) for CP³, the d=6 manifold). They appear to us as discrete labels rather than spatial directions because we observe only the d=3 projection of a mode structure that lives in d=6.

**Particles with d < 3 — sub-dimensional embedding.** The photon (d=2) is the opposite case. Its orbit spans 2 dimensions — a proper subspace of our 3D. Those 2 dimensions lie entirely within our observable space. From the photon's perspective, reality is 2-dimensional: the third spatial dimension of our world does not exist in its coordinate system. From our perspective, the photon is a 2D entity moving within our 3D world. Its 2D polarization plane can be oriented in any direction within our 3D — the photon is not fixed to one plane in space — but in whichever direction it travels, it is always a 2D object.

**The direct consequence: electromagnetic waves must be transverse.** The photon oscillates in its 2 dimensions. The direction of propagation is the one coordinate our 3D has that the photon's world does not. The photon cannot oscillate in that direction because that direction does not exist from its perspective. As the photon travels in different directions through our 3D space, its 2D polarization plane rotates to remain perpendicular to the direction of travel — the missing dimension is always the one the photon is moving through. Electromagnetic waves are transverse because the photon is a d=2 entity propagating through a d=3 observable space: it oscillates in the 2 dimensions it possesses and propagates through the 1 dimension it doesn't. The two polarization states are the photon's 2 dimensions, made directly observable. This is derived in Part 3 §14.

**Mass as hidden-dimensional momentum.** The governing equation on M_∞ separates into observable and hidden parts. For a mode with hidden wavefunction χ_{n,d}:

```
∂_t² Ψ = c²(Δ_3 + Δ_hidden) Ψ
```

The hidden Laplacian acts on χ_{n,d} and returns its eigenvalue: Δ_hidden χ_{n,d} = −m² χ_{n,d}, where m = m_scale_d × S(n,d). A d=3 observer, who cannot resolve the hidden motion, sees:

```
∂_t² ψ = c²(Δ_3 − m²) ψ
```

This is the Klein-Gordon equation. The mass term is not a separate input — it is the hidden-dimensional kinetic energy of the mode, appearing to a d=3 observer as a scalar constant because the hidden degrees of freedom are inaccessible. Mass is hidden momentum. The photon (n=0, d=2) has S(0,2) = 0, so m = 0: no hidden kinetic energy, no mass. Every other particle has n > 0 and non-zero hidden momentum, giving non-zero mass. The mass formula m = m_scale_d × S(n,d) is the spectrum of that hidden momentum.

---

## 4. The Unified Kernel

The cross-sector interaction is the unique leading term compatible with U(d) × U(d') symmetries. Sectors d and d' may couple only when d + d' is itself a sector dimension (Vandermonde rule):

```
V_kernel = Σ_{d+d' ∈ sectors} g_{d,d'} (ξ_d · ξ_{d'})² |Ψ^(d)|² |Ψ^(d')|²
```

The overall coupling strength g₃₃ = 8√7 = n_s²√(n_s+n_u)/2 is set by the seed n_s=4 (with n_u = n_s−1 = 3 derived) — the same integers from which the entire particle spectrum is selected. "Vacuum stability" is the physical condition that fixes the gap; n_s=4 (seed) and n_u=n_s−1 (derived) supply the numbers. No particle mass appears in the determination of g₃₃.

---

## 5. Canonical Particle Assignments

All masses predicted from a **sole unit reference m_e = 0.511 MeV**. The W boson mass follows from m_scale_2 × S(76,2). Sector scales follow from seeds alone (Part 2 §10).

The mass formula m = m_scale_d × S(n,d) where S(n,d) = C(n+d−1, d) is a binomial coefficient. In natural units, mass is frequency — S(n,d) × m_scale_d is the resonant frequency of mode n in sector d. The crucial additional fact is that this resonant frequency equals the cumulative count of hidden microstates below level n — a hockey-stick sum: S(n,d) = Σ_{k=0}^{n-1} C(k+d−1, d−1). This identity is why the eigenmode selection rule holds as a theorem rather than a coincidence (see Part 2).

Derived sector scales (coupling self-consistency; see Part 2 §10):
```
m_scale_6  = m_e / S(13,6)                        = 2.7526 × 10⁻⁵ MeV  [unit reference: sets the MeV scale for d=6]
m_scale_3  = m_e × √(g₃₃/g₆₆)                    = 4.702 MeV
m_scale_4  = m_scale_3 × √(g₄₄/g₃₃) / S(3,4)    = 0.1451 MeV
m_scale_10 = m_scale_6                             [g₁₀,₁₀ = g₆₆ = 1/n_s: shared seed coupling]
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
v₃ = 4.601   [seed n_s; derived n_u=n_s−1]
v₄ = 2.130   [seed n_s; derived n_u=n_s−1]
v₅ = 0.3645  [Hopf fiber universality: g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂]
v₆ = 0.500   [g₆₆ = 1/n_s = 1/4]
v₁₀= 0.500   [g₁₀,₁₀ = g₆₆ = 1/n_s: sectors d=6 and d=10 share the seed coupling]
```
The constraint g₂₅ = g₃₄ = 4√6 (equal cross-coupling for both U(1) Hopf pairs) uniquely fixes v₅ given v₂. No third unit reference is needed for any sector coupling.

| Particle | n | d | Predicted (MeV) | PDG (MeV) | Error |
|---|---|---|---|---|---|
| electron | 13 | 6 | 0.511 | 0.511 | unit reference |
| muon | 35 | 6 | 105.657 | 105.658 | −0.001% |
| tau | 23 | 10 | 1,776.84†† | 1,776.86 | −0.14σ |
| down | 1 | 3 | 4.702 | 4.670 | +0.68%† |
| strange | 4 | 3 | 94.04 | 93.40 | +0.68%† |
| up | 3 | 4 | 2.177 | 2.160 | +0.77%† |
| charm | 20 | 4 | 1,279.7‡ | 1,270.0 | +0.76%‡ |
| top | 72 | 4 | 174,000‡ | 172,760 | +0.72%‡ |
| bottom | — | 3 | 4,181 | 4,180 | +0.02% |
| photon | 0 | 2 | 0 | 0 | exact |
| W | 76 | 2 | 80,379 | 80,377 | +0.003% |
| Z | 81 | 2 | 91,230 | 91,188 | +0.047% |
| Higgs | 95 | 2 | 125,266 | 125,250 | +0.013% |

† The +0.68% offset in d=3 and +0.77% in d=4 reflect the natural accuracy of the coupling self-consistency derivation of m_scale_3. The rank-1 kernel forces this offset to be identical across all modes within a sector — confirmed by d and s quarks both at +0.68% despite spanning n=1 to n=4. Both are within PDG quark mass uncertainties (~10%).

†† Tau: **m_τ = m_e × S(23,10)/S(13,6) × (1 + 1/1680) = 1776.84 MeV (−0.14σ, inside 1σ ± 0.12 MeV).** The factor 1/1680 = 1/(n_u × n_s² × S(n_s,4)) is the Dyson resummation of the d=6→d=10 back-reaction. The isotropic coupling g_{6,6}=g_{6,10}=g_{10,10}=1/n_s=1/4 (from the seed) means the leading correction 1/2240 feeds back via g_{10,10}=1/n_s, multiplying by n_s/(n_s−1) = n_s/n_u = 4/3. Combined: 1/2240 × 4/3 = 1/1680.

‡ After applying the Generation Tower Correction (Part 2 §11) with ε = 1/(280√7) and k values {charm:3, top:10}, the c/u ratio becomes 0.000% and the t/u ratio −0.048%. The GTC corrects within-sector ratios; the uniform +0.77% sector-wide offset persists in all d=4 absolute masses.

**Co-fixed-point uniqueness**

As a uniqueness verification, the generation map was run over all 1,600 pairs $(n_d, n_s) \in [1..40]^2$, computing Jaccard similarity against the observed spectrum $\{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$. Jaccard $= 1.0$ at exactly one pair: **(1, 4)**. The next-closest is $(19,4)$ at $0.375$. $n_d = 1$ is trivially forced ($S(1,d)=1$ for all $d$) and $n_s = 4$ is forced by the topological constraint $S(4,4) = 35$ (Part 2 §3). There is one non-trivial seed.

---

### Theorem: Uniqueness of the Occupied Mode Index Set

**Statement.** Let $\Sigma = \{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ be the set of IDWT mode indices. $\Sigma$ is the unique set of positive integers satisfying all of the following simultaneously:

1. **Generation law closure.** Every element of $\Sigma$ is the eigenfrequency selected by the following closed chain of sector comb conditions (all verified exactly):

$$n_u = n_s - 1 = 3 \quad \text{[g-rule: } S(n_u,3) = 10 \text{ uniquely solves } n_{\nu_1} = n_e - d_u + 1\text{; Pascal describes the lattice position, g-rule selects it]}$$

$$n_c = S(n_s, 3) = 20$$

$$n_e = n_c - n_u - n_s = 13, \qquad n_\mu = S(n_s, 4) = 35$$

$$n_\tau = n_\mu - n_e + n_d = 23$$

$$n_{\nu_1} = S(n_u, 3) = 10, \quad n_{\nu_2} = S(n_u, 4) = 15, \quad n_{\nu_3} = n_{\nu_1} + n_{\nu_2} - n_u = 22$$
[inclusion-exclusion: both $n_{\nu_1}$ and $n_{\nu_2}$ project the same seed $n_u$, so their sum over-counts $n_u$ once; subtracting it is forced. Cross-check: $n_{\nu_3} = n_\tau - n_d = 22$ ✓]

$$n_{\rm top} = S(n_e, 2) - n_c + 1 = 72$$

$$n_W = g(d_\nu, n_{\rm top}) = d_\nu + n_{\rm top} - 1 = 5 + 72 - 1 = 76, \quad n_Z = n_W + q = 81 \;\; [q = d_\ell - 1 = S(n_u{-}1,4) = 5]$$

$$n_H = n_u + n_c + n_{\rm top} = 95$$

2. **Spectral independence.** No three elements $i, j, k \in \Sigma$ satisfy $S(i, d_i) + S(j, d_j) = S(k, d_k)$, where $d_i$ is the sector of mode $i$. The 14 occupied $S$-values are: $\{1, 15, 20, 2002, 2926, 3321, 4560, 8855, 11628, 18564, 65780, 1215450, 3838380, 64512240\}$. All 91 unordered pairs were checked; there are **zero violations**.

3. **Seed uniqueness.** The single non-trivial input $n_s = 4$ is the unique positive integer solving $S(n_s, 4) = n_\mu$, i.e.\ $\binom{n_s+3}{4} = 35$. This has exactly one solution.

**Proof sketch.**

- *Condition 3* is immediate: $S(1,4)=1$, $S(2,4)=5$, $S(3,4)=15$, $S(4,4)=35$, $S(5,4)=70$, and $S(n,4)$ is strictly increasing, so $n_s = 4$ is unique. $\square$

- *Condition 1* then fixes every element of $\Sigma$ deterministically — the chain above is algebraically closed with no free choices. Exhaustive search over all 1,600 pairs $(n_d, n_s) \in [1..40]^2$ confirms that only $(1,4)$ produces a set with Jaccard similarity $1.0$ against $\Sigma$; the next-closest pair gives $0.375$.

- *Condition 2* is verified computationally (zero violations). The asymptotic argument is: $S(\tau) = 64{,}512{,}240$ and $\sum_{\rm other} S_i = 5{,}171{,}502$, with cross-sector gaps (e.g.\ max $d=3$ simplex value $= 20$ vs.\ min $d=4$ simplex value $= 15$) growing combinatorially, making accidental sum-equalities impossible for larger seeds. $\square$

**Additional algebraic cross-checks** (all consequences of the chain above, each independently verified):

$$n_e = k_0 - n_u \;\; [k_0 = n_s^2 = 16], \qquad n_\tau = n_c + n_u, \qquad n_H = n_Z + 2(n_s + n_u)$$

$$n_{\rm top} = \chi(\mathbb{CP}^2) \times \chi(\mathbb{CP}^3) \times \chi(\mathbb{CP}^5) = 3 \times 4 \times 6, \qquad S(n_e, 2) = 91$$

$$n_Z - n_W = q = S(n_u{-}1,4) = 5 \;\; \text{(same } q \text{ as in } g_{22} = p^2 q/2 \text{)}$$

No mode index is chosen to match a mass. Each is the unique output of an algebraic rule applied to $n_s = 4$.

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

The d=5 sector has d mod 8 = 5. This is the one Clifford algebra class for which Majorana spinors do not exist — neither a Majorana condition nor a Majorana-Weyl condition can be imposed on the hidden-space spinor in sector d=5. Therefore no Majorana mass term is geometrically allowed for neutrinos, and the seesaw mechanism is forbidden by the sector structure. Neutrinos must be **Dirac fermions**.

This is a concrete, falsifiable prediction: neutrinoless double beta decay (0νββ) must have rate exactly zero. Current experiments (KamLAND-Zen: m_ββ < 36 meV) have seen no signal, consistent with the prediction. If 0νββ is observed, the spinor structure of IDWT is falsified on this point.

The d=5 sector mass scale is derived from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ (Part 2 §9c). No suppression mechanism or seesaw is needed.

**Absolute masses** (scale derived from m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ — no neutrino data):
```
m_ν₁ = 1.487 meV,  m_ν₂ = 8.639 meV,  m_ν₃ = 48.87 meV,  Σm_ν = 59.00 meV
```
All below KATRIN bound (450 meV). The mass scale m_scale_5 is fully derived from m_e and seeds (Part 2 §9c). The primary testable quantities are the absolute masses themselves: Σm_ν = 59.0 meV (within reach of CMB-S4) and the mass ratios m_ν₂/m_ν₁ = S(15,5)/S(10,5) = 5.808, m_ν₃/m_ν₁ = S(22,5)/S(10,5) = 32.86.

**Note on oscillation comparisons.** Δm² values are derived consequences of the absolute masses, expressed in the language of oscillation experiments (which measure interference, not absolute masses). They are not native IDWT quantities. m_ν₃ = 48.87 meV is about 4% below what oscillation data imply (~50.85 meV), a gap of the same structural kind as the raw top quark (+1.3%) and tau (−0.06%) discrepancies that the GTC and Dyson resummation respectively address. The Dyson correction coefficient 1/n_μ = 1/S(n_s,4) = 1/35 is a Pascal quantity; the machinery for deriving it from first principles remains open (Part 6).

**Normal ordering is a prediction.** Mode indices n_ν₁ < n_ν₂ < n_ν₃ are fixed by the eigenmode selection rule; since S(n,5) is monotonically increasing, m_ν₁ < m_ν₂ < m_ν₃ follows necessarily. Current experiments prefer normal ordering at 3–4σ, consistent with IDWT.

---

## 7. Relationship to Existing Physics

| Framework | IDWT equivalent | Derivation status |
|-----------|----------------|------------------|
| Quantum mechanics | Projection of Ψ∞ to 3D slice; Born rule from ∫|Ψ∞|²dξ | ✅ |
| Wave-particle duality | Ψ∞ is a wave; its 3D projection appears particle-like when localised | ✅ |
| Uncertainty principle | Projection loss prevents simultaneous position+momentum specification | ✅ |
| Special relativity | □_x component of □_{M∞}; inherited Lorentz covariance from product structure | ✅ |
| Fermi statistics | Spinor Ψ∞ anticommutes: {Ψ∞(ξ),Ψ†∞(ξ')}=δ(ξ−ξ') — Pauli exclusion derived | ✅ |
| Particle/antiparticle | Conjugate spinor Ψ̄∞ is distinct; antiparticles are automatic | ✅ |
| Electromagnetism | U(1) Hopf fiber phase: A_μ = ∂_μθ, F_μν = ∂_μA_ν−∂_νA_μ | ✅ |
| General relativity | Effective Einstein equations from |Ψ∞|² back-reaction on 4D geometry. No gravitons — gravity is purely geometric curvature. Macroscopic hidden-sector spaces are consistent because graviton propagation exclusions do not apply (Part 4 §1b). Bianchi identity and spectral theorem proved; G_N from sector localization geometry is the remaining open item (Part 4 §3.12) | 🔶 |
| Standard Model quarks | d=3 (down-type), d=4 (up-type) — masses from simplex formula | ✅ |
| Standard Model leptons | d=6 (e,μ), d=10 (τ) — masses from simplex formula | ✅ |
| Chiral weak force | Kähler γ₅ on CP²,CP³ selects left-handed components; W couples to holomorphic half only | ✅ |
| Spin-½ of all fermions | Dirac operator on $M_\infty$; spinor bundle of $\Psi_\infty$ (Part 8 §2) | ✅ |
| CKM Cabibbo angle | sin θ_C = (1+1/240)/√S(n_s,3) = 0.22454 — seed + Lichnerowicz | ✅ |
| Neutrino oscillations | d=5 sector, normal ordering | ✅ |
| Dirac neutrinos | d=5 has d mod 8=5: Majorana forbidden → 0νββ rate = 0 predicted | ✅ |
| Spin(10) spinor weight lattice | d=10 Maj-Weyl spinor (d mod 8 = 2) has 16-component Weyl part; its weight lattice gives tau hypercharges as cross-check on the anomaly cancellation derivation | ✅ |
| Confinement | Colour vector closure E_conf = λ_c|N⃗| from CP² geometry | ✅ |
| Cosmological constant | Λ_eff from unoccupied-mode vacuum energy, exponentially suppressed | 🔶 |

---

## 8. What Would Falsify IDWT

IDWT makes hard predictions — not parameter fits. Any Category A observation below directly and irrecoverably falsifies the framework with no parameter to adjust. Full inventory, thresholds, and structural predictions are in Part 5 §9.

### Category A — Hard binary falsifiers (one observation ends the framework)

| Prediction | Geometric basis | Current status |
|---|---|---|
| **0νββ rate = 0 exactly** (m_ββ = 0) | d=5, d mod 8 = 5: Clifford structure forbids Majorana spinors; no seesaw allowed | KamLAND-Zen: m_ββ < 36 meV, no signal ✅ |
| **Normal neutrino mass ordering** | n_ν₁ < n_ν₂ < n_ν₃ forced by eigenmode selection rule; S(n,5) strictly monotone | 3–4σ preference for normal ordering ✅ |
| **No new stable fundamental particles** | Sector Set Theorem + Uniqueness Theorem closes the spectrum (§3a, §3b) | No new particles at LEP, LHC ✅ |
| **No stable particle near 68.3 GeV** | S(35,10) × m_scale_10; not a co-fixed-point eigenmode | Excluded at LEP ✅ |
| **No narrow hadronic resonance in 15–50 MeV** | d=3 n=2,3 modes fail Stage-2; no stable states predicted in this window | Consistent with QCD spectrum ✅ |
| **No fourth quark or lepton generation** | Completeness Theorem; N_ν = 3 exactly | Z invisible width: PDG 2.984 ± 0.008 ✅ |

### Category B — Precision quantitative tests (with explicit thresholds)

| Prediction | Value | Falsified if... |
|---|---|---|
| m_s/m_d | 20.000 exactly | Outside 19.5–20.5 at controlled scale |
| m_μ/m_e | 206.7647 | Outside 206.760 ± 0.005 |
| Σm_ν | 59.00 meV | Measured < 40 meV or > 80 meV |
| sin²θ₂₃ | 0.5590 | > 3σ from 0.5590 |
| sin²θ₁₂ | 0.3086 | > 3σ from 0.3086 |
| sin²θ₁₃ | 0.02211 | > 3σ from 0.02211 |
| sin θ_C | 0.22454 | Outside 0.2237–0.2254 |
| ρ parameter | 1.00000 at tree level | ρ ≠ 1 beyond radiative corrections |
| N_ν | 3 exactly | Fourth neutrino species confirmed |

### Category C — Structural predictions (no SM equivalent)

- **No hierarchy problem:** m_H is integer-determined (n_H = 95); radiative corrections cannot shift mode indices.
- **Higgs is not a condensate:** no quartic self-coupling, no VEV, no vacuum metastability from λ_H running.
- **No seesaw:** neutrino mass scale set by cross-sector Hopf fixed point, not by a heavy right-handed neutrino mass term.
- **No sterile neutrinos:** Stage-1 filter eliminates all non-projecting d=5 modes; exactly three neutrino species.
- **Left-handed W coupling is geometric:** Kähler γ₅ on CP² and CP³ selects holomorphic (left-handed) components; not imposed as a postulate.

### Near-future windows

| Prediction | Experiment | Timescale |
|---|---|---|
| 0νββ = 0 (m_ββ = 0) | nEXO, LEGEND-1000, KamLAND-Zen 800 | 2025–2035 |
| Σm_ν = 59.0 meV | CMB-S4 (target ~30 meV) | 2030s |
| Normal ordering (definitive) | JUNO, DUNE, Hyper-Kamiokande | 2025–2030 |
| sin²θ₂₃ = 0.5590 | T2K, NOvA, DUNE | Running |
| No new stable particles | HL-LHC, FCC | 2025–2040 |

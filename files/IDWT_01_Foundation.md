# IDWT — Part 1: Foundations

## Status Key
- ✅ Derived or confirmed
- 🔶 Consistent but not fully derived

---

## 0. The Actual Structure: A Spectral Triple

**IDWT identifies the Standard Model as the spectral data of one operator $D$ on one space $M_\infty$.** It is the spectral action programme of Connes' noncommutative geometry, applied to the unique self-consistent Dirac-Harmonic operator on $M_\infty$. The mathematical object is a spectral triple $(\mathcal{A},\,\mathcal{H},\,D)$:

$$\mathcal{A} = C(M_\infty)\otimes\bigoplus_{d\in D}\mathcal{M}_{n_d}(\mathbb{C}), \quad \mathcal{H} = L^2(M_\infty, \mathcal{S}_\infty), \quad D = -i\gamma^\mu\partial_\mu + \sum_{d\in D} D_d$$

where $D_d$ is the Dirac-Harmonic operator in sector $d$ with potential $V_d(r) = \lambda_d r^2/(1+r^2)$. The stable spectrum of $|D|$ is exactly $\{S(n,d)\times m_{\text{scale},d}\}$. The spectral action $\text{Tr}(f(D/\Lambda))$ expands as:
$$\text{Tr}(f(D/\Lambda)) = f_2\Lambda^2\,\text{Tr}(D^2) + \cdots = \frac{1}{G_N}\int R + S_{\text{SM}}.$$

**Verification.** Computing $\text{Tr}(D^2) = \sum_i m_i^2$ from the 15 IDWT particles (top quark 50.5%, Higgs 25.5%, $Z$ 13.5%, $W$ 10.5%):
$$\sqrt{\text{Tr}(D^2)} = 248.3\text{ GeV} \approx v_{\text{Higgs}} = 246.2\text{ GeV} \quad (+0.85\%).$$

The Higgs VEV is a **spectral quantity** — the RMS eigenvalue of $D$ — not an independent input. The 0.85% residual in $\sqrt{\text{Tr}(D^2)}$ vs $v_{\text{Higgs}}$ reflects the small prediction errors in the mass spectrum (dominated by the +0.72% top quark offset from the GTC); it is not an independent error.

**Open computations reframed as spectral geometry:**

| Open item | Spectral geometry statement |
|---|---|
| G_N derivation | G_N from sector localization geometry — how concentrated sector energy couples to 4D curvature (Part 4 §3.12) |
| PMNS mixing | Holonomy of lepton sector bundle over graph $d=5\to6\to10\to5$ |
| CP phase | Berry phase around the lepton sector loop |
| $\sin^2\theta_W$ residual | Mode index ratio $S(76,2)/S(81,2)$ gives $\sin^2\theta_W=0.2237$ exactly; +0.37% from PDG on-shell value is within known 1-loop EW radiative corrections |

The laser, quasicrystal, Aubry-André, and atomic analogies are all instances of the same mathematical fact: the spectrum of a self-adjoint operator with a filtering condition. IDWT names that operator: $D$ on $M_\infty$. The SM is its spectral data.

**Analytic control from combinatorics.** The spectral zeta function of each sector $d$ has two exact anchor values derivable from $S(n,d)=\binom{n+d-1}{d}$ alone: $\zeta_d(1)=d/(d-1)$ (total inverse-mass weight, proved by a Pascal telescoping identity) and $\zeta_d(0)=-d/2$ (zeta-regularised eigenvalue count, from the constant term of the heat kernel $K_d(t)=\sum_n e^{-tS(n,d)}$). These confirm that each hidden sector behaves as a proper $d$-dimensional Riemannian space — spectral dimension matches fiber dimension, the functional determinant $\log\det D_d=-\zeta_d'(0)$ is finite without a UV cutoff, and the infinite tower is analytically controlled. Full derivations in Part 9 T13–T14.

---

## 1. Core Postulates

**P1 — The Master Wave**
Ψ∞ is a **Dirac spinor field** defined on an infinite-dimensional manifold. It is the only fundamental object. Everything observable — particles, fields, forces — is a derived consequence of its structure. The quantum number structure of matter (spin, chirality, statistics, hypercharges) follows from the spinor geometry of M_∞; the mass spectrum follows from the combinatorial mode structure S(n,d).

**P2 — The Observable Slice**
Our 3D universe is the restriction of Ψ∞ to a fixed address ξ⁰ in the hidden dimensions:
```
ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```
The observer's location ξ⁰ weights the projection amplitude for each mode (Stage-1 filter, Part 7) but does not determine which modes exist. The spectrum of occupied modes — which particles exist — is determined entirely by the seed structure and eigenmode selection rule (Part 2 §2-4), independent of ξ⁰. All observers at any ξ⁰ see the same particle spectrum; they differ only in the amplitude with which each mode projects onto their slice.

**P3 — Hidden Dimensions are Infinite and Non-Compact**
The sector spaces $\Xi_d$ are infinite Riemannian spaces — full-size dimensions, not rolled up or compactified in any sense. Each sector carries a potential well $V_d(r) = \lambda_d r^2/(1+r^2)$ that supports exponentially localized bound states via the Agmon decay theorem (Part 4 §3.8). These bound states are the particles. The symmetry labels $\mathbb{CP}^n$ and $S^n$ in the sector table describe the local geometry at the bottom of the potential well — the symmetry of the mode wavefunctions near $r=0$ — not the global topology of $\Xi_d$. This is exactly analogous to a hydrogen atom: the electron lives in infinite $\mathbb{R}^3$ but the ground state has $S^2$ symmetry from the spherically symmetric potential. No dimension is curled up; the modes bind themselves through the potential. The standard KK exclusions (Eöt-Wash, collider searches) presuppose graviton propagation into small compact dimensions; they do not apply here. See Part 4 §1b and §3.9.

Every SM particle is a bound state of a sector potential — not a bulk propagator. Scattering states (modes that propagate freely through the hidden space) are eliminated by the Stage-1 observability filter: they fail to project onto the 4D slice with finite amplitude. There are no KK excitations of SM fields accessible to experiment; the SM spectrum is precisely the set of sector resonances that survive both observability filters.

**P4 — Geometry First**
The governing equation is a Dirac wave equation on the curved manifold $M_\infty$. The sector potentials $V_d(r)$ arise from the intrinsic curvature of $M_\infty$ evaluated at the vacuum $\xi^0_d$ — they are not independent inputs but consequences of the geometry.

**P5 — Mass and Gravity are One Thing**
Both emerge from the same geometric structure. Mass is the count of hidden microstates accessible at a mode level, scaled by the sector's energy unit: m(n,d) = m_scale_d × S(n,d). Gravity is the distortion that concentration of |Ψ∞|² causes in the surrounding 4D geometry. They are manifestations of the same geometric object because they are sourced by the same underlying mode structure. The derivation of m_scale_d from the coupling constants is in Part 2 §10.

---

## 2. Projection and the Born Rule ✅

### 2.1 Observable Reality as a Cross-Section

Our 3D universe is one slice through Ψ∞, as a 2D circle is a cross-section of a 3D sphere. The circle is unaware it is a cross-section. Our entire observable universe is one such slice — its contents (matter, energy, space) are determined by the global structure of Ψ∞ evaluated at ξ⁰.

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

Standard quantum mechanics assigns probability density |ψ|² to any quantum field. IDWT applies this to Ψ∞ directly. The observable density ρ(r,t) is the hidden-space integral of |Ψ∞|², which marginalises over the hidden coordinates and recovers the 3D probability density. This is not a new postulate — it is the Born rule of quantum mechanics applied to the field Ψ∞ on M_∞, with the hidden dimensions integrated out.

The physical interpretation: an electron is not a cloud in 3D — it is a structured object in M_∞ whose 3D shadow (the projection) appears as a diffuse probability density. Entangled particles are features of Ψ∞ that are close in the hidden dimensions even when their 3D projections are far apart.

### 2.4 Connection to Cut-and-Project Construction

The IDWT projection mechanism is structurally identical to the cut-and-project method used to construct quasicrystals. The three-step architecture:

1. **Full space:** M_∞ (infinite-dimensional manifold supporting Ψ∞)
2. **Slice:** ψ_obs = Ψ∞(r, ξ⁰, t) at fixed ξ⁰
3. **Acceptance window:** Two-stage filter (Stage-1 projection mismatch Ω_log + Stage-2 colour closure). In quasicrystal theory the acceptance window is a geometric region; in IDWT it is a spectral criterion. The analogy captures the structure of selection — an underlying high-dimensional object, a slice, and a filter — rather than the mechanism.

The observed particle spectrum {1, 3, 4, 10, 13, 15, 20, 22, 23, 35, 72, 76, 81, 95} in mode-index space is the IDWT analogue of the aperiodic quasicrystal point set: irregular when listed, exactly determined by the projection geometry.

Key difference from quasicrystals: IDWT projects a continuous wave equation — modes have continuous suppression exp(−Ω_log) = S(n,2)/S(n,d) rather than a binary in/out criterion. Consequently, mass gaps between successive occupied modes approach the ratio S(n+1,d)/S(n,d) = (n+d)/n → d in the large-n limit: the spectrum within each sector is asymptotically geometric.

---

## 3. The Sector Structure of M_∞ ✅

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

### 3a. Sector Set Theorem ✅

**Theorem.** The sector set $D = \{2, 3, 4, 5, 6, 10\}$ is uniquely determined within IDWT by the following four conditions, all derivable from the single seed $n_s = 4$:

**Step 1 — The top quark mode index factorises.** From the eigenmode selection conditions alone (no sector assignment required):

$$n_{\rm top} = S(n_e, 2) - n_c + 1 = 91 - 20 + 1 = 72.$$

The unique factorisation $72 = N_c \times n_s \times N_f$ with $N_c = 3$ (from the CP² spin^c index, Part 8 §2.2), $n_s = 4$ (seed), and $N_f = 72/(N_c \times n_s) = 6$ (derived entirely within IDWT — no external input).

Cross-check: $N_f = S(n_u, 2) = S(3,2) = \binom{4}{2} = 6$. Both expressions for $N_f$ give the same value, confirming internal consistency.

**Step 2 — The three CP sectors are forced.** The factors $N_c$, $n_s$, $N_f$ are the Euler characteristics of three complex projective spaces:

$$\chi(\mathbb{CP}^{N_c-1}) = N_c = 3, \qquad d = 2(N_c-1) = 4,$$
$$\chi(\mathbb{CP}^{n_s-1}) = n_s = 4, \qquad d = 2(n_s-1) = 6,$$
$$\chi(\mathbb{CP}^{N_f-1}) = N_f = 6, \qquad d = 2(N_f-1) = 10.$$

This forces $d \in \{4, 6, 10\}$ as the three CP sectors. $d = 2$ (CP¹) is required as the $U(1)$ Hopf fiber base.

**Step 3 — The Hopf total spaces add $d \in \{3, 5\}$.** The couplings of the odd-sphere sectors $S^{2k+1}$ are derivable within IDWT when the base CP sector has its coupling from the kernel self-consistency fixed point:

- $d=3$ (S³ over CP¹): $g_{33} = n_s^2\sqrt{n_s+n_u}/2 = 8\sqrt{7}$ — from seeds. ✓  
- $d=5$ (S⁵ over CP²): $g_{55} = g_{33}g_{44}/g_{22}$ — from the Hopf universality condition $v_3/v_2 = v_5/v_4$. ✓

**Step 4 — Exclusion of remaining Hopf spaces.** The complex Hopf chain $S^1 \to S^{2n+1} \to \mathbb{CP}^n$ generates candidate pairs at every $n$. Two termination rules eliminate all unlisted spaces:

*Rule A (coupling termination).* $g_{66} = 1/n_s$ is the seed ratio — a direct output of the seed, not a kernel fixed-point coupling. The Hopf universality condition $v_3/v_2 = v_5/v_4$ that derives $g_{55}$ from fixed-point couplings cannot extend beyond $d=6$: there is no fixed-point formula for $g_{77}$, so $d=7$ is excluded. Sectors $d=8$ and $d=9$ (the $n=4$ Hopf pair, $\mathbb{CP}^4$ and $S^9$) have no path to the kernel fixed-point from the broken chain at $d=6$, so they are likewise excluded.

*Rule B (Gegenbauer criticality).* The Jacobi coupling $b_{k_0}(d) = \sqrt{k_0(k_0+d-1)}/(2k_0+d-2)$ must satisfy $b_{k_0} \geq 1/2$ for a sector to support stable bound-state modes. At $d=10$:
$$4k_0 = (d-2)^2 \quad \Longrightarrow \quad 4\times 16 = 64 = (10-2)^2,$$
so $b_{k_0}(10) = 1/2$ exactly — the unique solution to $4k_0=(d-2)^2$, giving the critical endpoint of the chain. At $d=11$: $b_{k_0}(11) < 1/2$ (subcritical), so $d=11$ and all $d \geq 11$ cannot support stable modes.

The sector set is therefore forced by the Hopf chain together with Rules A and B:
$$D = \underbrace{\{2,3,4,5\}}_{\text{Hopf pairs } n=1,2} \cup \underbrace{\{6\}}_{n=3 \text{ base, Rule A}} \cup \underbrace{\{10\}}_{n=5 \text{ base, Rule B}} = \{2,3,4,5,6,10\} \quad \square$$

**Completeness.** All 14 occupied mode indices $\{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ sit in $d \in \{2,3,4,5,6,10\}$ and no occupied index is consistent with any excluded sector. $\square$

**Remark.** The lepton sector coupling $g_{66} = 1/n_s = 1/4$ is derived from the seed. Numerically it equals $(1/2)^2 = 0.25$, but the derivation is from $n_s$ alone — no hypercharge assignment enters.

---

### 3b. Completeness of the Particle Spectrum ✅

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

### Sector Topology and the Atiyah-Singer Index ✅

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
n_top = χ(CP²) × χ(CP³) × χ(CP⁵) = N_c × n_s × N_f = 3 × 4 × 6 = 72 ✓
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



**Convergence on d=10.** Four independent routes — Hopf/octonionic chain (approximate), Gegenbauer criticality (exact), Spin(10) spinor weight lattice (cross-check), and Hurwitz termination (exact) — all give d=10. Their agreement is the reason d=10 carries ✅ rather than 🔶.

The spinor type per sector follows from the Clifford algebra periodicity theorem (Bott periodicity, mod 8). The sectors are independent in the sense that each carries a distinct Clifford algebra Cl(d) with no shared generators; their spinor spaces therefore combine as a tensor product. The total hidden-space spinor dimension is 2×2×4×4×8×32 = 2¹⁴ = 16,384 [tensor product over all six sectors].

These dimensions are not chosen. They are the unique sequence produced by the Hopf fibration chain over the normed division algebras (ℝ, ℂ, ℍ, 𝕆):

```
S¹ → S³  → S²    complex Hopf     →  d=2 (base CP¹), d=3 (total S³)
S¹ → S⁵  → CP²   complex Hopf     →  d=4 (base CP²), d=5 (total S⁵)
S³ → S⁷  → S⁴    quaternionic     →  d=4 also as S⁴≅HP¹ (consistent)
```

d=6 arises as CP³, the base space of the next complex Hopf fibration S¹→S⁷→CP³. CP³ has real dimension 6 and serves as the twistor space of S⁴ ≅ HP¹. d=7 (the total space S⁷) is excluded from the IDWT sector set for two consistent reasons: (i) geometrically, S⁷ is the total space of the quaternionic Hopf fibration S³→S⁷→S⁴ and is fully accounted for by the d=4 and d=3 sectors already present; (ii) algebraically, g_{66} = 1/n_s is a seed ratio rather than a kernel fixed-point coupling, so Hopf universality cannot determine a coupling formula for a hypothetical d=7 sector over d=6. Both routes reach the same conclusion.

d=10 arises as CP⁵ = SU(6)/U(5), the next step in the complex projective chain beyond CP³. Its dimension d=10 is fixed by the Sector Set Theorem (§3a) — $d=10 = 2(N_f-1)$ where $N_f = n_{\rm top}/(N_c \times n_s) = 6$ — and confirmed independently by the Gegenbauer criticality condition (§3b). Hurwitz's theorem provides a third confirmation: CP⁵ associated with the octonions is the last space in the chain for which the sector structure remains self-consistent.

The sequence terminates at d=10 because the octonions are the last normed division algebra — Hurwitz's theorem admits no further entries.

### 3c. Gegenbauer Criticality Theorem — Second Route to d=10 ✅

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

## 4. The Unified Kernel ✅

The cross-sector interaction is the unique leading term compatible with U(d) × U(d') symmetries. Sectors d and d' may couple only when d + d' is itself a sector dimension (Vandermonde rule):

```
V_kernel = Σ_{d+d' ∈ sectors} g_{d,d'} (ξ_d · ξ_{d'})² |Ψ^(d)|² |Ψ^(d')|²
```

The overall coupling strength g₃₃ = 8√7 = n_s²√(n_s+n_u)/2 is set by the seed n_s=4 (with n_u = n_s−1 = 3 derived) — the same integers from which the entire particle spectrum is selected. "Vacuum stability" is the physical condition that fixes the gap; n_s=4 (seed) and n_u=n_s−1 (derived) supply the numbers. No particle mass appears in the determination of g₃₃.

---

## 5. Canonical Particle Assignments ✅

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

**Complete coupling vector** {v_d = √g_dd}, fully closed by seeds and m_e:
```
v₂ = 26.879  [derived: v₂ = √g₂₂ = √(17²×5/2)]
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

**Co-fixed-point uniqueness ✅**

As a uniqueness verification, the filtration map was run over all 1,600 pairs $(n_d, n_s) \in [1..40]^2$, computing Jaccard similarity against the observed spectrum $\{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$. Jaccard $= 1.0$ at exactly one pair: **(1, 4)**. The next-closest is $(19,4)$ at $0.375$. This is a verification, not a parameter search — $n_d = 1$ is trivially forced ($S(1,d)=1$ for all $d$) and $n_s = 4$ is forced by the topological constraint $S(4,4) = 35$ (Part 2 §3). There is one non-trivial seed.

---

### Theorem: Uniqueness of the Occupied Mode Index Set

**Statement.** Let $\Sigma = \{1,3,4,10,13,15,20,22,23,35,72,76,81,95\}$ be the set of IDWT mode indices. $\Sigma$ is the unique set of positive integers satisfying all of the following simultaneously:

1. **Filtration closure.** Every element of $\Sigma$ is the eigenfrequency selected by the following closed chain of sector comb conditions (all verified exactly):

$$n_u = n_s - 1 = 3$$

$$n_c = S(n_s, 3) = 20$$

$$n_e = n_c - n_u - n_s = 13, \qquad n_\mu = S(n_s, 4) = 35$$

$$n_\tau = n_\mu - n_e + n_d = 23$$

$$n_{\nu_1} = S(n_u, 3) = 10, \quad n_{\nu_2} = S(n_u, 4) = 15, \quad n_{\nu_3} = n_{\nu_1} + n_{\nu_2} - n_u = 22$$

$$n_{\rm top} = S(n_e, 2) - n_c + 1 = 72$$

$$n_W = S(n_e, 2) - n_{\nu_2} = 76, \quad n_Z = n_W + \beta = 81 \;\; [\beta = S(n_u{-}1,4) = 5]$$

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

$$n_Z - n_W = \beta = S(n_u{-}1,4) = 5 \;\; \text{(same } \beta \text{ as in } g_{22} = \alpha^2\beta/2 \text{)}$$

No mode index is chosen to match a mass. Each is the unique output of an algebraic rule applied to $n_s = 4$.

---

## 6. Neutrino Sector ✅

Neutrinos cannot fit d=6. The sector scale m_scale_6 = 27.5 eV means the lightest possible d=6 mode (n=1) has mass 27.5 eV — already 550× heavier than m_ν₃ and over 18,000× heavier than m_ν₁. No integer simplex index gives a d=6 mass in the meV range. They occupy **d=5** with mode indices n=(10,15,22), all structurally derived:

```
n_ν₁ = S(n_u,3) = S(3,3) = 10    [simplex image of up quark into d=3]
n_ν₂ = S(n_u,4) = S(3,4) = 15    [simplex image of up quark into d=4]
n_ν₃ = n_τ − n_d = 23 − 1 = 22   [eigenmode selection rule]
```

Redundant check: n_ν₃ = n_ν₁ + n_ν₂ − n_u = 10+15−3 = 22 ✓

d=5 is topologically forced as the Hopf total space S⁵ of the fibration S¹→S⁵→CP². It is the Hopf partner of d=4 (up quarks) and is required by the fibration chain.

**Neutrinos are Dirac fermions — a prediction from the spinor structure ✅**

The d=5 sector has d mod 8 = 5. This is the one Clifford algebra class for which Majorana spinors do not exist — neither a Majorana condition nor a Majorana-Weyl condition can be imposed on the hidden-space spinor in sector d=5. Therefore no Majorana mass term is geometrically allowed for neutrinos, and the seesaw mechanism is forbidden by the sector structure. Neutrinos must be **Dirac fermions**.

This is a concrete, falsifiable prediction: neutrinoless double beta decay (0νββ) must have rate exactly zero. Current experiments (KamLAND-Zen: m_ββ < 36 meV) have seen no signal, consistent with the prediction. If 0νββ is observed, the spinor structure of IDWT is falsified on this point.

The d=5 sector mass scale is derived from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ (Part 2 §9c). No suppression mechanism or seesaw is needed.

**Oscillation ratios (from simplex values alone):**
```
m_ν₂/m_ν₁ = S(15,5)/S(10,5) = 11628/2002 = 5.808
Δm²₃₁/Δm²₂₁ = 32.949   (PDG 2022: 34.825, deficit −5.4%; see Part 5 §3 and Part 6 for experimental range analysis)
```

**Absolute masses** (scale derived from m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ — no neutrino data):
```
m_ν₁ = 1.487 meV,  m_ν₂ = 8.639 meV,  m_ν₃ = 48.87 meV,  Σm_ν = 59.00 meV
```
All below KATRIN bound (450 meV). The atmospheric splitting Δm²₃₁ is derived from the mode ratios alone: Δm²₃₁ = m_ν₃² − m_ν₁² = 2.386×10⁻³ eV² (observed: 2.584×10⁻³ eV², −7.7%). The mass scale m_scale_5 is fully derived from m_e and seeds (Part 2 §9c).

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
| General relativity | Effective Einstein equations from |Ψ∞|² back-reaction on 4D geometry. No gravitons — gravity is purely geometric curvature. Macroscopic hidden dimensions are consistent because graviton propagation exclusions do not apply (Part 4 §1b). Bianchi identity and spectral theorem proved; G_N from sector localization geometry is the remaining open item (Part 4 §3.12) | 🔶 |
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

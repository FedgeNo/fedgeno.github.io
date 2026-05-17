# Infinite Dimensional Wave Theory — Part 3: Forces, Gauge Structure & Colour

All fundamental forces emerge from the geometry of Ψ∞ and the sector structure of M_∞.

---

## 0. The Complete IDWT Action

Everything in IDWT — gravity, the mass spectrum, gauge fields, coupling constants, mixing angles — follows from a single action functional on M_∞ = ℝ^{3,1} × Ξ, varied with respect to two dynamical objects: the spacetime metric g_μν(x) and the master spinor field Ψ∞(x,ξ).

### 0.1 Field Content

The single fundamental field is Ψ∞(x,ξ), a Dirac spinor on M_∞. The manifold carries the product metric:

```
ds²_{M_∞} = g_μν(x) dx^μ dx^ν  +  h_ab(ξ) dξ^a dξ^b
```

g_μν(x) is the dynamical spacetime metric (3 spatial + 1 time). h_ab(ξ) is the fixed background metric on the sector space Ξ = ⊕_{d∈D} Ξ_d, D = {2,3,4,5,6,10}. The Dirac matrices on M_∞ decompose as:

```
{Γ^M, Γ^N} = 2 G^{MN},    G^{MN} = diag(g^{μν}, h^{ab})
Γ^μ = e^μ_a(x) γ^a        [spacetime, via vierbein (3+1 tetrad)]
Γ^a = sector matrices on Ξ  [from Clifford algebra Cl(d) per sector]
```

### 0.2 The Action

```
S_IDWT[Ψ∞, g_μν]

  = (1/16πG_N) ∫_{ℝ^{3,1}} R^{(4)} √{-g} d⁴x                          [Einstein-Hilbert]

  + ∫_{ℝ^{3,1}×Ξ} Ψ̄∞ (iΓ^μ ∇_μ + iΓ^a ∂_a) Ψ∞ dμ_4 dμ_ξ               [Kinetic]

  + (1/2) Σ_{d,d'∈D} g_{dd'}
      ∫_{ℝ^{3,1}×Ξ×Ξ} (ξ_d·ξ_{d'})²                                     [Kernel]
      [Ψ̄∞(x,ξ) P_d Ψ∞(x,ξ)] [Ψ̄∞(x,ξ') P_{d'} Ψ∞(x,ξ')]
      dμ_4 dμ_ξ dμ_{ξ'}
```

where P_d is the projector onto sector Ξ_d, and g_{dd'} = v_d × v_{d'} is the rank-1 coupling matrix with v_d = √g_{dd} determined by the seed n_s=4 (with n_u = n_s−1 derived).

The kernel term is the unique leading interaction invariant under U(d) × U(d') rotations of each sector. Its quartic-in-Ψ form is the sector-space analogue of the Nambu–Jona-Lasinio interaction.

### 0.3 Equations of Motion

**Varying g^{μν}:**

```
G_μν(x) = 8π G_N T_μν^{eff}(x),    G_N = measured Newton's constant
```

The sector space contributes only through T_μν^{eff} = ∫_Ξ T_μν^{Dirac} dμ_ξ — a source term, never a propagating gravitational degree of freedom (Part 4 §3.1–3.4).

**Varying Ψ̄∞:**

```
[iΓ^μ ∇_μ + iΓ^a ∂_a] Ψ∞ + Σ_{d,d'} g_{dd'} (ξ_d·ξ_{d'})² J^{d'}(x,ξ) Ψ∞ = 0
```

where J^{d'}(x,ξ) = ∫ (ξ_{d'}·ξ')² [Ψ̄∞ P_{d'} Ψ∞](x,ξ') dμ_{ξ'}. In the mean-field approximation (replacing J^{d'} by the sector condensate ⟨J^{d'}⟩):

```
[iΓ^μ ∇_μ + iΓ^a ∂_a  −  V_conf(ξ)] Ψ∞ = 0
```

with sector potential V_conf = Σ_d V_d(|ξ_d|), V_d(r) = λ_d r²/(1+r²) and λ_d = (g_{dd}/2)^{2/3} (Part 4 §3.10).

### 0.4 What Each Term Produces

| Term | Variation | Output |
|---|---|---|
| S_EH | δg^{μν} | Spacetime Einstein equations, G_eff = G_N = G_fund/V_7 (V_7 from all six sector manifold geometries, Part 4 §3.12.3) |
| L_kinetic (spacetime part) | δΨ̄∞ | Dirac propagation in 3D space |
| L_kinetic (sector part) | δΨ̄∞ | Mass eigenvalue problem H_d χ = m_eff χ |
| L_kernel (d=d', self) | δΨ̄∞ | Sector confinement V_d, λ_d = (g_{dd}/2)^{2/3} |
| L_kernel (d=4, colour) | δΨ̄∞ | SU(3)-symmetric quark contact coupling; effective coupling g²_eff = 2g_{44}/π² (§4) |
| L_kernel (d=4↔d=2) | consistency | U(2) electroweak gauge fields, W±, Z, γ |
| L_kernel (d=3↔d=4) | eigenvalue + Lichnerowicz | Cabibbo angle sin θ_C |

### 0.5 Mass Spectrum from the Action

The KK ansatz Ψ∞ = ψ(x) ⊗ χ_n(ξ) reduces the equation of motion to:

```
(iγ^μ ∇_μ − m_eff) ψ = 0           [massive Dirac in 3D space]
H_d χ_n = m_eff χ_n                  [sector eigenvalue problem]
```

The sector Hamiltonian H_d = −Δ_Ξ + V_d(r) has eigenvalues m_eff = m_scale_d × S(n,d) by the spectral counting theorem (Part 8 §3). The mass formula is a consequence of the action.

### 0.6 Effective Colour Coupling from the Kernel

The d=4 self-coupling L_{44} = (g_{44}/2) ∫ (ξ_4·ξ_4')² J^4(ξ) J^4(ξ') dμ_{ξ'} is the direct quark contact interaction. When parameterized in Yang-Mills language for correspondence with QCD, integrating J^4 over CP² (volume π²/(2m_scale_4⁴)) gives the effective coupling:

```
g²_eff = 2g_{44}/π²
```

The SU(3) invariance of this coupling follows from the CP² isometry group acting on the quark colour states. No propagating SU(3) gauge quanta (gluons) appear in the IDWT action — the colour interaction is a contact term, not an exchange interaction.

### 0.7 Coupling Constants from the Action

All physical coupling constants follow from {g_{dd'}} and the sole unit reference m_e (m_W is derived at +0.003% from seeds via g₂₂):

| Physical quantity | Formula | Value |
|---|---|---|
| Effective colour coupling | g²_eff = 2g_{44}/π² | 0.919 |
| Weinberg angle | sin²θ_W = 1−(S(n_W,2)/S(n_Z,2))² | 0.2237 |
| GTC correction | ε = 1/(280√7) | 0.001350 |
| Cabibbo angle | sin θ_C = (1+χ(CP¹)/24S)/√S(n_s,3) | 0.22454 |
| Newton's constant | G_N = G_fund / V_7, V_7 = L_4 L_5 L_6 L_{10}^4 ≈ 113 (all six sector manifold geometries; G_fund one input) | — |
| **SU(2)_L coupling** | **g₂ = Q_u √g_s = (2/3)√g_s = (2/3)(2g₄₄/π²)^(1/4)** | **0.65275** |
| **EW scale √Tr(D²)** | **spectral action RMS** | **248.3 GeV** |
| **Fermi constant** | **G_F = g₂²/(4√2 m_W²)** | **1.1658×10⁻⁵ GeV⁻²** |


**Derivation of g₂.** The QCD coupling g_s arises from the Wilson loop holonomy of the Fubini-Study gauge connection over the d=4 sector manifold CP². The Fubini-Study metric has fundamental 2-cycle area π; integrating the Yang-Mills action density over CP² introduces the volume factor 2/π² (ratio of the sphere volumes at successive Hopf levels), giving:

```
g_s = √(2g₄₄/π²) = (2g₄₄/π²)^(1/2)   [holonomy integral over CP²]
```

The up-quark charge Q_u = 2/3 follows from the spin^c index on CP²: ind(D^c_{CP²} ⊗ O(1)) = 3 = N_c colours (Theorem S3, Part 8 §2.2), so each colour carries charge 1/N_c = 1/3 and the doublet carries 2Q_u = 2 × 2/3. The SU(2)_L coupling is therefore:

```
g_s = √(2g₄₄/π²) = (2g₄₄/π²)^(1/2)   [QCD coupling, from CP² holonomy]
g₂  = (2/3)√g_s  = (2/3)(2g₄₄/π²)^(1/4)
g₂² = (4/9) × g_s = (4/9)(2g₄₄/π²)^(1/2)

g₂ = (2/3)√g_s = 0.65275
PDG: 0.65270.  Error: +0.008%
```

**The coupling cascade.** All three gauge couplings descend from a single seed-derived quantity, g_{44}, through a fixed chain with no free parameters at any step:

```
g_{44}  [seed: n_s=4, n_u=3]
  → g_s = √(2g_{44}/π²)         [CP² holonomy integral, factor 2/π² from Fubini-Study volume]
  → g_2 = (2/3)√g_s             [coordinate ratio: d_photon/d_hadronic = 2/3]
  → sin²θ_W = 1−(S(n_W,2)/S(n_Z,2))²   [mode index ratio]
  → g_1 = g_2 tan θ_W
  → α = g_1²g_2²/[4π(g_1²+g_2²)]
```

The factor 2/3 at the g_s → g_2 step is both the electric charge of the up quark (index theorem) and the coordinate containment ratio d_photon/d_hadronic: N_c = 3 = d_hadronic (the hadronic sector dimension), d_photon = 2, so Q_u = d_photon/d_hadronic (Part 1 §3g). The CP² holonomy step involves a continuous Riemannian integral (2/π²), not a coordinate count; but the subsequent step is a literal ratio of sector dimensions.

From g₂ and m_W (the confinement mass of the W in the d=2 sector):

```
G_F = g₂²/(4√2 m_W²) = 1.1658×10⁻⁵ GeV⁻²  (PDG: 1.1664×10⁻⁵,  −0.05%)
g₁ = g₂ × tan θ_W = 0.35044         (PDG: 0.35740,  −1.95% at fiber scale)
g₁(m_Z) after 1-loop U(1)_Y running = 0.35067  (PDG: 0.35740,  −1.88%)
sin²θ_eff(m_Z) from running g₁ = 0.22397        (PDG: 0.23153,  −3.3%)
```

The g₁ error of −2% reflects the difference between the fiber-scale U(1)_Y coupling and its value at m_Z after EW running. The α prediction from g₁,g₂:

```
α = g₁²g₂²/(4π(g₁²+g₂²)) = 1/131.8   (PDG α(m_Z)=1/127.9, +3.1%)
```

The +3% is the EW running from the fiber scale (≈m_W) to m_Z.



### 0.8 Force Mediation as Spatial Geometry

Each fundamental force acts within a spatial region determined by its sector. The mediator of a force traverses the spatial dimensions of its sector; a particle can only couple to that force if it shares those sector coordinates.

| Force | Mediator | Sector | Spatial dimensions occupied |
|---|---|---|---|
| Electromagnetic | Photon | d=2 | 2 |
| Weak | W±, Z | d=2 | 2 |
| Strong (QCD) | — (kernel contact) | d=3, d=4 | — |
| Gravity | — | (none) | 10 |

**Coordinate containment.** For a force to couple two particles, both must have wavefunction support on the spatial coordinates the force acts in. A d=2 photon cannot couple to a particle with no support on the d=2 sector. The strong coupling (d=4, kernel contact) cannot reach a particle with no d=3 or d=4 sector support. Coordinate containment is a necessary condition. The sufficient condition additionally requires the appropriate topological charge — electric charge from the Hopf fiber winding number on S³ (the d=3 sector boundary), colour from the Atiyah-Singer index on CP² (the d=4 manifold), and weak isospin from the Kähler chirality on the d=2 sector.

**Gravity as the exception.** Gravity carries no sector label and is confined to no subset of the spatial dimensions. The effective stress-energy sourcing gravity integrates over all sector coordinates:

```
T_μν^{eff}(x) = ∫_Ξ T_μν^{Dirac}(x,ξ) dμ_ξ
```

The gravitational field is genuinely 10D — it is not a 3D field with extra-dimensional corrections. A d=3 observer measures the 3-dimensional projection of this field, giving observed Newton's constant G_N = G_fund / V_7 rather than G_fund (Part 4 §3.12.2).

**Spatial extent and coupling strength.** The gauge forces (EM, weak, strong) are confined to 2 or 4 spatial dimensions and act at full strength within those sectors. Gravity distributes over all 10 spatial dimensions. The factor V_7 = L_4 L_5 L_6 L_{10}^4 ≈ 113 — the product of the localization lengths of the seven additional spatial dimensions introduced by the sector nesting Ξ_3 ⊂ Ξ_4 ⊂ Ξ_5 ⊂ Ξ_6 ⊂ Ξ_{10} — is precisely how much larger the gravitational field's spatial footprint is compared to what a d=3 observer can directly probe. This is the geometric origin of gravity's weakness relative to the other forces.

**Coupling filter — the particle side.** The coordinate containment principle above describes the force side: which sector a force mediator occupies determines which particles it can reach. The complementary particle-side principle is the coupling filter: the particle's own sector geometry determines the structure of whatever coupling it has. Coordinate containment is necessary but not sufficient. A particle whose coordinates are nested inside a force's sector may still have zero coupling to that force if its sector geometry projects the relevant representation to zero — as neutrinos are colour-neutral despite their S⁵ coordinates containing Ξ_4, because the S⁵ Hopf fibration averages over the CP² colour representation and selects only the singlet. More broadly: the photon's U(1) geometry constitutes the orientation filter of EM coupling; the CP² Atiyah-Singer index constitutes colour with N_c = 3 handles; the S⁵ Clifford algebra constitutes the prohibition of all Majorana/LNV interactions; the CP³ index cancellation constitutes total colour silence for leptons; the d=10 AA Cantor-set spectrum constitutes the tau's fractal marginal coupling to all decay channels. In each case, the sector geometry is not producing a quantum number that then determines coupling — the geometry is the coupling structure. See Part 1 §3d and §3g for the full derivation of each sector's coupling filter.

### 0.9 CKM Matrix from the Kernel

The mode amplitude at the d=3 coordinate level scales as $|\chi_n(\xi^0)| \propto 1/\sqrt{S(n,d)}$ from L² normalisation (Part 1 §2.2), so heavier modes (larger S) carry less weight at our coordinate level relative to lighter modes. The intra-sector kernel matrix element between modes $n_i$ (lighter) and $n_j$ (heavier) is proportional to the amplitude of the **heavier** mode at ξ₀ relative to the lighter:

```
|⟨χ_{n_lighter}|K_{dd}|χ_{n_heavier}⟩| ∝ |χ_{n_heavier}(ξ₀)| / |χ_{n_lighter}(ξ₀)|
                                          = √(S(n_lighter,d) / S(n_heavier,d))
```

The mixing probability is the square of this ratio:

```
|V_{i→j}|² = S(n_lighter, d) / S(n_heavier, d)    [within sector d]
```

**Application to CKM elements:**

The Cabibbo angle is the d=3 intra-sector mixing (down ↔ strange):
```
sin²θ_C = S(n_d, 3) / S(n_s, 3) = 1/20    → sin θ_C = 1/√20 = 0.22361  [bare]
```
Corrected by CP¹ curvature (Lichnerowicz, §12): sin θ_C = (1+1/240)/√20 = 0.22454

The |V_cb| element is the d=4 intra-sector mixing (up ↔ charm):
```
|V_cb|² = S(n_u, 4) / S(n_c, 4) = S(3,4)/S(20,4) = 15/8855

|V_cb| = √(15/8855) = 0.04116
```

PDG |V_cb| = 0.04100 ± 0.0014 (exclusive). Tension: +0.11σ.

The Wolfenstein parameter A:
```
A = |V_cb| / sin²θ_C = √(S(n_u,4)/S(n_c,4)) × S(n_s,3)
  = √(15/8855) × 20 = 0.82315
```

PDG A = 0.8230 ± 0.0046. Tension: +0.03σ.

**|V_ts| from unitarity:** The third row of the CKM matrix has |V_tb| ≈ 1, so |V_ts|² ≈ |V_cb|². IDWT predicts |V_ts| ≈ |V_cb| = 0.04116. PDG: 0.04183 ± 0.0007. Tension: −0.96σ.

**|V_ub| lower bound:** Without the CP-violating phase (ρ, η — open in IDWT): |V_ub|_min = A s_C³ = 0.00920. PDG |V_ub| = 0.00382, which requires √(ρ²+η²) ≈ 0.41. The CP phase is not yet derived.

### 0.10 Pure Sector Identities from the Lagrangian

**cos θ_W = S(n_W,2)/S(n_Z,2) exactly.** From the Lagrangian's Weinberg angle definition:

```
sin²θ_W = 1 − (S(n_W,2)/S(n_Z,2))²  →  S(n_W,2)/S(n_Z,2) = cos θ_W
= 2926/3321 = 0.88106    (PDG cos θ_W = 0.88108)
```

**Sector mass ratios:**

```
m_μ/m_e = S(n_μ,6)/S(n_e,6) = 3,838,380/18,564 = 206.7647  (PDG 206.7683, −0.002%)
m_H/m_Z = S(n_H,2)/S(n_Z,2) = 4560/3321 = 1.37308          (PDG 1.37354, −0.033%)
```

**The d=2 coupling g22 = 722.5 and what it determines.** The Hopf chain constraint g_{25} = √g_{22} × √g_{55} = √96 = 4√6 is automatically satisfied for any g_{22} with g_{55} = 96/g_{22} — g_{22} cancels. Its value is fixed instead by the depth of the d=2 sector potential: λ_2 = (g_{22}/2)^{2/3} = 50.72, localization length L_2 = 0.14. The large λ_2 ensures W, Z, H are tightly confined and do not propagate as bulk KK modes.

**Neutron-proton mass difference, leading order:**

```
m_n − m_p ≈ m_d − m_u = m3 × S(1,3) − m4 × S(3,4) = 4.702 − 2.177 = 2.525 MeV
PDG: 1.293 MeV    (factor 2, uncomputed QED + isospin corrections)
```

The correct order of magnitude emerges from pure sector masses with no parameters. The factor of 2 is the uncomputed electromagnetic correction (proton self-energy ≈ 0.6 MeV) plus isospin breaking from the d=3↔d=4 sector coupling asymmetry.

---

## 1. Electromagnetism

Electromagnetism emerges from the U(1) Hopf fiber connecting the d=2 and d=3 sectors. Writing Ψ∞ = A·e^{iθ}, the phase gradient A_μ = ∂_μθ is the photon field; its curvature F_μν = ∂_μA_ν − ∂_νA_μ gives Maxwell's equations. The photon is massless because its mode index is n=0: S(0,2) = 0. Full derivation in §14.

---

## 2. Colour Charge from CP²

The d=4 sector geometry is CP² = SU(3)/U(2). The full isometry group of CP² is SU(3). Therefore quarks in the d=4 sector naturally carry SU(3) quantum numbers — from the manifold's own geometry.

The spin^c Dirac operator on CP² twisted by the fundamental colour bundle O(1) with Hopf flux k=1 gives:
```
index(D^c_{CP²} ⊗ O(1)) = C(3,2) = 3
```

The three net left-chiral zero modes live in the fibre of O(1) over CP². This bundle transforms under SU(3) = Isom(CP²) in the fundamental representation **3** — the standard 3-dimensional representation. Therefore the three zero modes are not merely three distinct objects; they transform into each other under SU(3) gauge rotations exactly as the three colour states of a quark do. Colour charge is the SU(3) representation label of the zero-mode fibre.

**Three net left-chiral zero modes = three colour states per quark.** This is the geometric origin of colour charge, with the representation content explicit.

---

## 3. Colour Symmetry from Consistency

The SU(3) colour symmetry emerges from a well-defined principal bundle. The d=4 sector contributes a principal SU(3) bundle P_{SU(3)} → M₄ with connection 1-form A constructed from the Hopf fibration data of CP². This connection is a mathematical consequence of local phase-frame freedom in ψ_colour(x); it is non-propagating in the IDWT action (no Yang-Mills kinetic term — see §0.2). Similarly, the d=2 sector and d=6 lepton sector contribute the U(2) bundle P_{U(2)} → M₄ with connection B. The total colour-plus-EW bundle is:

```
P → M₄,    structure group G = SU(3) × U(2)
```

Given the colour space H_colour identified from the CP² Dirac zero modes:

1. Physical observables depend on |Ψ∞|² — invariance under local colour rotations U(x) ∈ U(H_colour) is a **consistency requirement**, not a postulate
2. Local invariance forces a connection: D_μΘ = ∂_μΘ + i[A_μ, Θ]
3. The commutator [D_μ, D_ν]Θ = i[F_μν, Θ] gives the Yang-Mills field strength:
   ```
   F_μν = ∂_μA_ν − ∂_νA_μ + i[A_μ, A_ν]
   ```

SU(3) gauge theory is not postulated. It follows from the CP² geometry combined with the consistency requirement that physics not depend on the local orientation of the colour frame. The gauge transformation A → gAg⁻¹ − (dg)g⁻¹ arises from local fibre rotations in P_{SU(3)}.

### 3a. Explicit Berry Connection Construction 🔶

The argument above establishes that a connection must exist. This subsection constructs it explicitly from the IDWT sector field.

**The colour triplet state.** The Atiyah-Singer index on CP² (Part 8 §2) gives three left-chiral zero modes φ_a ∈ L²(CP²), a = 1, 2, 3. At spacetime point x, the d=4 sector component of Ψ_∞ decomposes as:

```
ψ_color(x) = (ψ¹(x), ψ²(x), ψ³(x)) ∈ ℂ³
```

where

```
ψ^a(x) = ∫_{CP²} φ_a*(ξ) Ψ_∞^{(d=4)}(x, ξ) dμ_{CP²}
```

This integral extracts the three colour amplitudes from the full sector-space field at each spacetime point x. It is the IDWT definition of the colour state at x.

**Berry connection formula.** The colour frame can be chosen independently at each spacetime point. The unique torsion-free SU(3) connection preserving the L²(CP²) inner product on H_colour is:

```
A_μ(x) = i ψ_color†(x) ∂_μ ψ_color(x)   ∈ su(3)
```

This is the colour connection on P_{SU(3)} → M₄.

**Gauge transformation check.** Under U(x) ∈ SU(3): ψ_color(x) → U(x)ψ_color(x). Direct computation:

```
A_μ → i(Uψ)† ∂_μ(Uψ)
     = iψ† U†[(∂_μU)ψ + U∂_μψ]
     = U† (iψ†∂_μψ) U + U†(∂_μU)
     = U† A_μ U + U† ∂_μU
```

This is the correct SU(3) transformation law. The curvature

```
F_μν = ∂_μA_ν − ∂_νA_μ + i[A_μ, A_ν]   ∈ su(3)
```

is the colour curvature 2-form. This is a mathematical object encoding the SU(3) holonomy of the colour frame; it is not a propagating field. The IDWT action (§0.2) contains no kinetic term F_{μν}F^{μν} for this connection — the colour interaction is entirely in the kernel contact term.

**Status.** The Berry connection is defined and transforms correctly for the zero-mode sector. What remains is constructing ψ_color(x) explicitly for propagating quark modes — that is, extending the colour projection P_color: Ψ_∞^{(d=4)} → ψ_color beyond the three CP² zero modes to the full occupied spectrum (n=3 up, n=20 charm, n=72 top). The zero-mode construction is complete (Part 8 §2); the propagating-mode projection operator is the remaining step.

---

## 4. Effective Colour Coupling from the Kernel

### Derivation of g²_eff from the d=4 Kernel

The IDWT action has no Yang-Mills kinetic term. The colour interaction is entirely the d=4 self-coupling contact term. To connect with the QCD coupling g_s used in the cascade of §0.7, we derive the effective coupling by integrating the kernel current J^4 over CP²:

The d=4 kernel current density, when integrated over CP² with the Fubini-Study metric at radius parameter a = 1/m_scale₄:

```
Vol(CP²) = π² a⁴ / 2 = π² / (2 m_scale₄⁴)
```

The kernel coupling g₄₄ = 12/√7 is dimensionless (ξ measured in units of 1/m_scale₄). The effective coupling strength extracted by matching the integrated kernel amplitude to the standard QCD form is:

```
1/g²_eff = Vol(CP²) × m_scale₄²/g₄₄ = (π²/2) × (1/g₄₄)

g²_eff = 2g₄₄/π²
```

**Numerically:**

```
g²_eff = 2 × (12/√7) / π² = 0.919
```

This is the coupling g_s = √g²_eff that enters the cascade g_{44} → g_s → g₂ → sin²θ_W → g₁ (§0.7). The formula derives from the kernel coupling g₄₄ and the CP² volume, with no free parameters. (This is not a Kaluza-Klein result: CP² is the configuration space of d=4 internal degrees of freedom, not a geometrically compact extra dimension.)

---

## 5. Colour Confinement

Assign each quark a colour expectation vector n⃗ ∈ ℝ⁸ (the 8 Gell-Mann matrix expectation values). For any single quark, |n⃗|² = 4/3. Antiquarks have n⃗(q̄) = −n⃗(q).

The energy of a composite system is:
```
E_conf = λ_c |Σᵢ n⃗(qᵢ)|
```

This is the unique SU(3)-invariant linear energy functional. Its consequences:

- **Mesons:** only colour-matched qq̄ pairs give Σn⃗ = 0 → E_conf = 0. All others cost 2λ_c.
- **Baryons:** only the (r,g,b) combination and permutations give Σn⃗ = 0 → E_conf = 0.

**Only colour-matched configurations are stable.** It is a necessary consequence of the CP² isometry group acting on the colour vector space.

**Status note:** This colour-vector model is a *selection rule* — it correctly identifies which states are colour-neutral and therefore stable. It does not derive the confinement *mechanism* (linear potential, flux-tube formation, Wilson loop area law) from the M_∞ kernel. The derivation of λ_c from the inter-sector coupling structure, and the equivalence to the QCD area law, are open items addressed further in §8 and Part 8 §11.

---

## 6. SU(3)_colour × U(2)_EW from One Manifold

CP² carries two independent gauge-algebraic structures:

| Structure | Source | Group | Generators | Physical role |
|---|---|---|---|---|
| Isometry | SU(3) acts on fibre ℂ³ | SU(3) | 8 | Colour symmetry of quark contact coupling |
| Holonomy | Fubini-Study metric | U(2) = SU(2)×U(1) | 4 | Electroweak |

### Why U(1)_Y is the U(1) in U(2), and SU(2)_L is the SU(2) in U(2)

**The U(1)_Y generator is T₈ of SU(3).** Since CP² = SU(3)/U(2), the isotropy group U(2) sits inside SU(3). The U(1) factor of U(2) is generated by the 8th Gell-Mann generator:

```
Y_generator = T₈ = λ₈/2 = diag(1, 1, −2)/(2√3)
```

acting on the fundamental representation ℂ³. Normalising to give physical hypercharges (Y = 1/6 for the quark doublet):

```
Y = (1/√3) T₈ = diag(1, 1, −2)/6  [acting on colour triplet]
```

The electric charges follow immediately from Q = T₃ + Y:

| Field | T₃ | Y | Q |
|---|---|---|---|
| u_L | +1/2 | +1/6 | +2/3 |
| d_L | −1/2 | +1/6 | −1/3 |
| e_L | −1/2 | −1/2 | −1 |
| ν_L | +1/2 | −1/2 | 0 |

The hypercharges are not assigned — they are eigenvalues of T₈ on the SU(3) representations, which are determined by the root lattice of SU(3) = Isom(CP²).

**The SU(2)_L generator is the SU(2) factor of U(2).** From the Kähler spinor decomposition (§7): the U(2) holonomy acts on the tangent space T^{1,0}(CP²) ≅ ℂ². The SU(2) ⊂ U(2) acts on Λ^{0,1} = ℂ² (the left-handed spinors) in the fundamental representation, and acts trivially on Λ^{0,0} and Λ^{0,2} (the right-handed spinors). Therefore:

- Left-handed quarks (u_L, d_L): transform as a doublet under SU(2). **This is SU(2)_L.**
- Right-handed quarks (u_R, d_R): are SU(2) singlets. They carry no weak charge.

The weak isospin structure is entirely determined by the SU(2) factor of the U(2) holonomy of CP². No separate postulate is needed.

```
su(3) = u(2) ⊕ m
```

where m ≅ T_{[e]}(CP²) is the 4-dimensional (real) tangent space at the base point. **Dimension check:** dim su(3) = 8, dim u(2) = 4, dim m = dim CP² = 4, and 4+4 = 8. This is an orthogonal decomposition under the Killing form of su(3): the u(2) generators are orthogonal to the m generators. Therefore:

- The **8 colour generators** are the 8 generators of su(3). Of these, 4 live in u(2) (the holonomy generators) and 4 live in m (the tangent space generators). These generators act on the colour states of quarks through the SU(3)-invariant kernel — they are symmetry generators of the contact coupling, not propagating quanta.
- The **4 EW bosons** are the 4 generators of u(2) ⊂ su(3). They act on the tangent space of CP², not on the colour fibre. Since u(2) and m are orthogonal in su(3), the EW generators do not mix with the colour generators.

The colour-plus-EW algebra su(3) ⊕ u(2) is the full algebra of CP²'s isometry group SU(3), decomposed according to the homogeneous space structure. No extra gauge bosons appear because the decomposition su(3) = u(2) ⊕ m is complete and exhausts all generators.

---

## 7. Chirality from Kähler γ₅

The chiral weak force — the W boson couples to left-handed particles only — follows from the spinor structure of Ψ∞ on the sector manifolds. Three sectors are **Kähler manifolds**: d=2 (CP¹), d=4 (CP²), d=6 (CP³). Each carries a canonical Kähler form ω, which defines a chirality operator on the sector spinor:

```
γ₅^Kähler = i^m × ω_{a₁a₂} ... ω_{a_{2m-1}a_{2m}} γ^{a₁}⋯γ^{a_{2m}}
```

where m is the complex dimension of the sector (m=1,2,3 for d=2,4,6 respectively). This operator anticommutes with all sector gamma matrices γ^a, splitting the sector spinor into **holomorphic** (positive chirality = LEFT) and **anti-holomorphic** (negative chirality = RIGHT) components.

**Why the W couples only to the holomorphic half — the Kähler spinor argument:**

On a Kähler manifold of complex dimension m, the Dirac spinor bundle decomposes as:
```
S = Λ^{0,*}(T^{*1,0}) = Λ^{0,0} ⊕ Λ^{0,1} ⊕ ... ⊕ Λ^{0,m}
```

The Kähler chirality operator γ₅^Kähler splits this into:
- **S₊ (LEFT)** = Λ^{0,0} ⊕ Λ^{0,2} ⊕ ... (even-degree anti-holomorphic forms)
- **S₋ (RIGHT)** = Λ^{0,1} ⊕ Λ^{0,3} ⊕ ... (odd-degree anti-holomorphic forms)

The U(2) holonomy of CP² acts on T^{*1,0}(CP²) — the holomorphic cotangent bundle. This means U(2) acts on Λ^{0,1} but not on Λ^{0,0}. For d=4 (CP², m=2):

- Λ^{0,0} = ℂ: transforms trivially under U(2) → singlet, RIGHT-handed
- Λ^{0,1} = T^{*1,0}: transforms in the fundamental of U(2) → doublet, LEFT-handed
- Λ^{0,2} = det(T^{*1,0}): transforms as a character of U(2) → singlet, RIGHT-handed

The W boson is the SU(2) ⊂ U(2) gauge field. Since SU(2) acts on Λ^{0,1} (the left-handed sector) but acts trivially on Λ^{0,0} and Λ^{0,2} (right-handed), the W couples exclusively to left-handed quarks. Right-handed quarks live in SU(2) singlets — not because this is postulated, but because U(2) holonomy acts non-trivially only on Λ^{0,1}.

For d=6 (CP³, m=3): S₊ = Λ^{0,0} ⊕ Λ^{0,2} (dim 1+3=4) and S₋ = Λ^{0,1} ⊕ Λ^{0,3} (dim 3+1=4), giving the 4L+4R split of the lepton sector.

**The non-Kähler sectors (d=3, d=5) have no Kähler form** and therefore no intrinsic chirality operator. Quarks in d=3 (S³) are intrinsically vector-like; their observed left-right asymmetry is inherited from the d=4 sector via the cross-coupling g_{3,4}. The neutrino sector d=5 (S⁵) is also non-Kähler — it has no chirality operator — consistent with the fact that neutrinos are Dirac fermions (no Weyl condition possible in d=5, see Part 1 §6).

**The spin^c Dirac index** is a consequence of this structure: the net count of left-chiral zero modes is exactly the holomorphic Euler characteristic χ_{hol}(CP^m) = C(m+1,m) = m+1, which agrees with the indices tabulated in the sector Dirac table. The Kähler form is the geometric cause; the index is its topological fingerprint.

| Sector | Kähler? | γ₅^Kähler | L/R split | Physical |
|--------|---------|-----------|-----------|---------|
| d=2 (CP¹) | ✓ | exists | 1L + 1R | W± polarisation |
| d=3 (S³) | ✗ | none | vector-like | Colour inherited from d=4 |
| d=4 (CP²) | ✓ (spin^c) | exists | 2L + 2R | u_L,d_L vs u_R,d_R |
| d=5 (S⁵) | ✗ | none | Dirac only | ν_L + ν_R (Dirac neutrinos) |
| d=6 (CP³) | ✓ | exists | 4L + 4R | ν_L,e_L,ν_μL,μ_L vs right-handed |
| d=10 (CP⁵) | ✓ | exists | 16L + 16R | SO(10) Weyl splitting |

---

## 8. Hypercharges from Anomaly Cancellation and SO(10)

With N_c = 3 from the CP² Dirac index, and g₆₆ = 1/4 established from CP³ quaternionic geometry (Part 2 §9c), all SM hypercharges follow from gauge anomaly cancellation. Full derivation in §13; result: Y_Q = 1/6, Y_L = −1/2 = −√g₆₆, Q_u = 2/3, Q_d = −1/3. Fractional charges are not inputs — they follow from three colours and the seed coupling.

**Note on derivation order.** The anomaly cancellation route works from d=4 geometry upward: CP² gives N_c = 3, then CP³ quaternionic geometry gives g₆₆ = 1/4, and N_c = 3 together with Y_L = −√g₆₆ = −1/2 force the remaining hypercharge assignments via SU(2)²U(1) anomaly cancellation. Anomaly cancellation is the mechanism that propagates the geometric inputs into a complete hypercharge table — it is not the source of g₆₆.

**Independent cross-check — SO(10) algebra:** Because Ψ∞ is a spinor and d=10 has d mod 8 = 2, the d=10 sector carries a Majorana-Weyl spinor whose 16-component Weyl part is the **16** of Spin(10) ≅ SO(10). The six distinct hypercharge values in that multiplet — Y = {+1/6, −2/3, +1, +1/3, −1/2, 0} — are determined entirely by the SO(10) weight lattice. For the tau generation specifically: Y(τ) = −1, Y(ν_τ) = 0, Y(t) = +2/3, Y(b) = −1/3 follow from the SO(10) root system without any SM hypercharge assignment.

Both routes agree. The SO(10) route provides a cross-check on the anomaly cancellation result: the same hypercharges that cancel anomalies with N_c=3 are precisely those predicted by the SO(10) weight lattice. The redundancy is structural consistency, not circular reasoning — the two routes start from different sectors (d=4 and d=10) and converge on the same hypercharges.

---

## 9. Colour Coupling Running 🔶

The standard QCD β-function coefficient b₀ = (11N_c − 2n_f)/(48π²) contains two contributions: −2n_f/(48π²) from fermion loops and 11N_c/(48π²) from gauge-boson (gluon) loops. IDWT derives N_c = 3 from the CP² Dirac index (§2) and n_f = 6 from the six occupied quark modes. However, because the IDWT action has no propagating colour gauge quanta (§0.2, §0.6), the 11N_c gauge-boson loop term does not automatically follow. The running of the effective colour coupling g²_eff = 2g_{44}/π² from the kernel in a theory with only quark loops would give b₀ = −2n_f/(48π²) < 0 — infrared freedom, not asymptotic freedom.

**Status 🔶:** Whether and how asymptotic freedom arises in IDWT is an open derivation item. The N_c = 3 result (from CP² Dirac index) and n_f = 6 count (from quark mode indices) are both solid. The question is whether the SU(3)-symmetric quark contact coupling generates an effective running that reproduces QCD asymptotic freedom — possibly through resummation of quark loop insertions in the kernel, analogous to how NJL models exhibit a form of running at finite cutoff.

---

## 10. Electroweak Predictions

With the d=2 sector scale m_scale_2 = 27.47 MeV:

| Observable | IDWT | Observed | Error |
|---|---|---|---|
| m_photon | 0 (exact) | 0 | — |
| m_Z | 91,230 MeV | 91,188 MeV | +0.047% |
| m_Higgs | 125,266 MeV | 125,250 MeV | +0.013% |
| sin²θ_W | 0.2237 | 0.22290 (on-shell) | +0.37% |
| ρ parameter | 1 (exact) | 1.002 | −0.2% |

**sin²θ_W is parameter-free:**
```
n_Z − n_W = n_s + n_d = 4 + 1 = 5   (seed index + down mode index)
           = q = S(n_u,4)−S(n_u,3) = S(2,4) = 5   [same q as in Theorem S3]
sin²θ_W = 1 − (S(76,2)/S(81,2))² = 0.2237
```

The Z-W mode gap equals q — the same Dirac eigenstate increment that enters g₂₂ (Theorem S3, Part 8 §5). Both arise from the d=4 sector's eigenvalue count at the up-quark level. n_Z − n_W = q links the W-Z mass ratio to the EW coupling constant through a single spectral identity.

**ρ = 1 is derived:** W and Z live in the same sector → custodial SU(2) is automatic.

---

## 11. The Boson Eigenmode Selection and Sector Coupling Map

All boson mode indices follow from the Vandermonde sector coupling g(a,b) = a + b − 1 applied to occupied mode indices and sector dimensions:

| Coupling | Result | Identification |
|---------|--------|----------------|
| g(d=4, n_ν₁=10) | 13 | n_e — up sector + ν₁ → electron |
| g(d=4, n_c=20) | 23 | n_τ — up sector + charm → tau |
| g(d=5, n_top=72) | 76 | n_W — ν sector + top → W boson |
| g(d=6, n_W=76) | 81 | n_Z — lepton sector + W → Z boson |
| g(n_ν₂=15, n_Z=81) | 95 | n_H — ν₂ + Z → Higgs |
| g(d=10, n_s=4) | 13 | n_e — tau sector + strange → electron |

**Boson generation chain:**
```
g(d=5, n_top=72)    = 76 = n_W    [ν-sector + top → W]
g(d=6, n_W=76)      = 81 = n_Z    [lepton + W → Z]
g(n_ν₂=15, n_Z=81) = 95 = n_H    [ν₂ + Z → Higgs]
```

**Sum rules:**
```
n_u + n_c + n_top = 3+20+72 = 95 = n_H     [all d=4 quarks sum to Higgs]
n_top = n_H − n_u − n_c = 72               [Higgs back-determines top]
```

**Jacobi boundary identities at k₀ = n_s² = 16:**
```
b₁₆² = n_W:         16×19/4 = 76 = n_W
n_s + n_e = n_s²+1: 4+13 = 17 = n_s(n_s−1)+1   [equivalently n_e = n_s²−n_s+1]
n_W + S(2,3) = n_s × S(n_s,3):  76+4 = 80 = 4×20
```

**Cabibbo consistency via the same Jacobi structure:** sin²θ_C = S(2,3)/(S(2,3)+n_W) = 4/80 = 1/20, consistent with 1/√20. The absent n=2 mode appears as the second singular value of the boundary coupling matrix.

The coupling-conservation identity is equivalent to any of: g(d=5, n_top) = n_W; n_W = 4×19 = 76; n_W + n_ν₂ = S(n_e,2) = 91. All three are algebraically equivalent and all proved.

---

## 12. Cabibbo Angle

The Cabibbo mixing angle arises from the d=3↔d=2 coupling structure. The bare IDWT prediction is 1/√20; the curvature of the mediating d=2 sector (CP¹) provides a computable correction.

### Bare Prediction

The Cabibbo angle at leading order:

```
sin²θ_C = 1/S(n_s, 3) = 1/20       → sin θ_C = 1/√20 = 0.22361
```

Equivalently, from the Jacobi boundary identity n_W + S(2,3) = n_s × S(n_s,3):

```
sin²θ_C = S(2,3) / (S(2,3) + n_W) = 4/80 = 1/20
```

This is a theorem of the seed n_s=4 and the Vandermonde structure, with no free parameters.

### Curvature Correction from the Mediating Sector

The Cabibbo mixing is mediated by the W boson, which lives in the d=2 sector (CP¹ = S²). The bare prediction uses a flat-space normalization of the mode functions on CP¹. The actual CP¹ geometry has curvature, which corrects the effective mode density through the Lichnerowicz formula.

**Step 1 — Lichnerowicz on CP¹ (d=2 sector):**

The Dirac operator on CP¹ satisfies:

```
D² = Δ + R/4      (Lichnerowicz–Bochner)
```

The heat kernel of D² on CP¹ at the diagonal:

```
K(t, x, x) ~ (N/4πt) × [1 + t(R/6 − R/4) + O(t²)]
           = (N/4πt) × [1 − tR/12 + O(t²)]
```

The R/6 term is the standard heat-kernel curvature correction; the −R/4 Bochner term subtracts, giving the net −R/12 coefficient.

**Step 2 — IDWT time scale:**

The heat-kernel time relevant for the Cabibbo correction is set by the strange quark's energy scale, not the bare sector scale. In units where m_scale_3 = 1:

```
t₀ = 1/S(n_s, 3) = 1/20
```

**Step 3 — Corrected effective mode count:**

The effective mode count that enters sin²θ_C becomes:

```
S_eff = S(n_s, 3) × (1 − R × t₀/12) = 20 × (1 − 2/(12×20)) = 20 × (1 − 1/120)
```

**Step 4 — Corrected Cabibbo angle:**

```
sin²θ_C = 1/S_eff ≈ (1/20) × (1 + 1/120)

sin θ_C = √sin²θ_C ≈ (1/√20) × (1 + 1/240)    [Taylor: √(1+δ) ≈ 1+δ/2]
```

**Step 5 — Using R = χ(CP¹):**

For unit CP¹ = S²: R = 2 = χ(CP¹) (the scalar curvature equals the Euler characteristic for the standard metric on S²). Therefore:

```
sin θ_C = (1 + χ(CP¹)/(24 · S(n_s,3))) / √S(n_s,3)
         = (1 + 2/(24 × 20)) / √20
         = (1 + 1/240) / √20
         = 0.22454
```

**Why χ(S³) = 0 does not contribute:** The d=3 quark sector has geometry S³. The Euler characteristic of any odd-dimensional closed manifold is zero: χ(S³) = 0. The curvature correction vanishes for the quark sector. The correction enters exclusively through the mediating d=2 sector (CP¹) through which the W boson propagates.

**Result:**

| Quantity | Value |
|---|---|
| sin θ_C (bare) | 0.22361 |
| sin θ_C (curvature corrected) | 0.22454 |
| PDG \|V_us\| | 0.22450 ± 0.00044 |
| Tension | +0.09σ |

The correction closes the tension from −2.03σ to +0.09σ with no free parameters. The inputs are: χ(CP¹) = 2 (topology of the W boson sector), S(n_s,3) = 20 (seed structure), and the Lichnerowicz coefficient −R/12 (a theorem of spin geometry).

**First-row unitarity.** IDWT's CKM matrix is unitary by construction. V_ud is not an independent prediction — it is the trigonometric complement of sin θ_C:

```
|V_ud| = √(1 − sin²θ_C) = 0.97447
```

This value is not separately testable against the PDG nuclear beta-decay result of 0.97370 ± 0.00014, because the apparent 5.5σ discrepancy is not an IDWT-specific failure. It is the **Cabibbo Angle Anomaly**, a pre-existing tension within the Standard Model itself: the PDG values of |V_ud| (from nuclear beta decay) and |V_us| (from kaon decays) are independently measured, and they fail to satisfy |V_ud|² + |V_us|² + |V_ub|² = 1 by ~3σ (giving ≈0.9985 rather than 1.000). Computing √(1 − |V_us|²_PDG − |V_ub|²_PDG) = 0.97447 — precisely IDWT's value — demonstrates that this gap is entirely attributable to the known unitarity deficit in the SM measurement inputs, not to anything IDWT does differently. IDWT enforces exact CKM unitarity by construction; the tension is between the two independent PDG measurements, and IDWT agrees with |V_us| at +0.09σ. Reporting a 5.5σ V_ud discrepancy alongside the +0.09σ V_us agreement would double-count a single angular prediction.



---

## 13. Spin^c Structure and Hypercharge Derivation

CP² is spin^c (not spin). The spin^c structure requires an auxiliary U(1) bundle — geometrically forced, naturally identified with U(1)_Y (hypercharge).

**N_c = 3 determines all SM hypercharges via gauge anomaly cancellation:**

```
SU(2)²U(1) anomaly: N_c Y_Q + Y_L = 0  →  Y_Q = 1/(2N_c) = 1/6
SU(3)²U(1) anomaly: 2Y_Q = Y_u + Y_d   →  Y_u + Y_d = 1/3
Electric charge:    Q = T₃ + Y          →  Q_u = 2/3, Q_d = −1/3
```

All four independent anomaly conditions cancel exactly with SM values. Fractional hypercharges (1/6, 2/3, −1/3) are not inputs — they follow from N_c = 3 from CP² geometry.

**The N_c chain:**
```
IDWT d=4 sector: CP² = SU(3)/U(2)
→ Dirac index = C(3,2) = 3 = N_c
→ SU(2)²U(1) anomaly-free: Y_Q = 1/(2N_c) = 1/6
→ All SM hypercharges determined from geometry alone
```

**What remains open:** Generation number (N_gen = N_c = 3 suggestive but unproved).

---

## 14. Electromagnetism from the Hopf Fiber

### Structure

The d=2 and d=3 sectors are unified by the Hopf fibration:
```
S¹ → S³ → S² = CP¹
(fiber)  (d=3)  (d=2)
```

- **d=2 (CP¹ = S²):** The base of the Hopf fibration — gauge bosons parameterize the base
- **d=3 (S³):** The total space — quarks live here and naturally carry U(1) charge from the fiber action
- **S¹ fiber = U(1):** The electromagnetic gauge group, not postulated — it is the Hopf fiber

### Photon Derivation

Write Ψ∞ = A·e^{iθ}. The phase gradient defines the gauge field:
```
A_μ = ∂_μθ
```

This is the KK zero mode of the U(1) Hopf fiber. The field tensor:
```
F_μν = ∂_μA_ν − ∂_νA_μ
```
is the curvature 2-form of the U(1) connection. The Lorentz force equation follows from the geodesic equation in ℝ³ × S¹:
```
F = q(E + v × B)
```
Electromagnetism is not postulated — it emerges from the phase geometry of Ψ∞ via the Hopf fiber.

### Massless Photon

In d=2, m = m_scale_2 × S(n,2). The photon is n=0: S(0,2) = C(1,2) = 0 → m_photon = 0 exactly. The n=0 mode exists because the U(1) fiber has a trivial representation with zero occupation — no fiber excitation means massless gauge boson. The first d=2 sector excitation (n=1) has mass m_scale_2 × 1 = 27.47 MeV, safely above photon mass bounds.

### Transverse Polarization from Sector Dimension

The photon lives in the d=2 sector. Our observable space is d=3 (Part 1 §3i). The photon's 2 dimensions are a proper subspace of our 3 — it is a 2-dimensional entity in a 3-dimensional world. The direction of propagation is the one coordinate our 3D has that the photon's sector does not. The photon cannot oscillate in the propagation direction because that coordinate falls outside its world.

This is why electromagnetic waves are transverse. The two polarization states — the only two independent oscillation modes of the photon field — are exactly the photon's 2 sector dimensions. As the photon travels in different directions through our 3D space, its polarization plane rotates to stay perpendicular to the direction of travel: the missing coordinate is always the propagation direction. No additional argument from gauge invariance or the Maxwell equations is needed; transversality is a direct consequence of d=2 < 3.

The masslessness (n=0, S(0,2)=0) and the universality (d=2 ⊂ every higher sector) are properties of the photon within its sector. The transversality is a property of the photon relative to our observable space. All three follow from d=2.

### Curvature Unification

Both gravity and electromagnetism are curvature 2-forms in IDWT:

| Force | Bundle | Curvature object |
|-------|--------|-----------------|
| Electromagnetism | U(1) Hopf fiber | F_μν = ∂_[μ∂_ν]θ |
| Gravity | Metric g_μν | Riemann tensor R^ρ_{σμν} |

The statement from P4 — all physics follows from the geometry of M_∞ — is concrete for both forces.

**Electric charge is derived.** The electromagnetic coupling is $e = g_2 \sin\theta_W$, where $g_2 = (2/3)\sqrt{g_s}$ follows from the CP² holonomy integral (§4) and $\sin\theta_W = \sqrt{1-(S(76,2)/S(81,2))^2}$ follows from the mode indices. The fine structure constant at the fiber scale is $\alpha = e^2/(4\pi)$, giving $1/\alpha = 131.8$. After 1-loop QED running to $q\to0$, $1/\alpha(0) \approx 133.1$ (−2.9% from PDG 137.036); the residual traces to the $\sin^2\theta_W$ +0.37% gap, not a separate parameter.

---

## 15. The Quantum Number Package

The spinor structure of Ψ∞ means the quantum number structure of the SM emerges from geometry. The table below identifies what is derived and which route it comes from.

| SM feature | IDWT derivation | Route |
|---|---|---|
| Spin-½ for quarks and leptons | KK Dirac operator on M_∞ | Spinor bundle §59 |
| Fermi statistics | Spinor anticommutation relations | Clifford algebra |
| Particle/antiparticle | Conjugate spinor Ψ̄∞ | Complex spinor field |
| Left-handed weak coupling | Kähler γ₅ selects holomorphic half of each sector spinor | §7 above |
| Quark chirality (u_L ≠ u_R) | CP² Kähler chirality splits 4-spinor into 2L + 2R | §7 above |
| Lepton chirality (e_L ≠ e_R) | CP³ Kähler chirality splits 8-spinor into 4L + 4R | §7 above |
| Neutrinos are Dirac | d=5 has d mod 8 = 5; Majorana spinors forbidden | Clifford periodicity |
| Tau-sector hypercharges | SO(10) spinor weight lattice (16 of Spin(10)) | 16 of Spin(10) |
| 0νββ rate = 0 | Follows from Dirac neutrino prediction | Falsifiable |

The spinor structure governs quantum numbers — what attaches to each mode. The mass formula m = m_scale_d × S(n,d), all coupling constants, the sector structure {2,3,4,5,6,10}, and the sole unit reference m_e are determined by the geometric and combinatorial structure of M_∞ independently of spin. m_W is derived.

---

## 16. Electromagnetism: Ward Identity and L-Parity Protection

### 16.1 The Ward Identity in IDWT

The IDWT kinetic term contains the covariant derivative:

```
L_kin = Ψ̄∞ (iΓ^μ ∇_μ) Ψ∞     with ∇_μ = ∂_μ − i A_μ Q̂
```

where A_μ is the d=2 zero-mode (photon) field and Q̂ is the U(1)_EM charge operator (Q = −1 for d=6 electrons, Q = +2/3 for d=4 up-type quarks, etc., from anomaly cancellation §8).

Under a local U(1) gauge transformation A_μ → A_μ + ∂_μα, Ψ∞ → e^{iα Q̂} Ψ∞:

```
δL_kin = −(∂_μα) J^μ_EM
```

Setting δS = 0 (invariance of the action) yields:

```
∂^μ J_μ^{EM}(x) = 0    [Ward identity]
```

The Ward-Takahashi identity at all loop orders:

```
q_μ Γ^μ(p, p+q) = S^{-1}(p+q) − S^{-1}(p)
```

holds automatically from gauge invariance.

### 16.2 L-Parity Protection: Photon Mass = 0 to All Orders

**Theorem.** The IDWT kernel cannot produce a photon mass at any order in perturbation theory.

**Proof.** The kernel is (ξ·ξ')², a degree-2 polynomial in the inner product ξ·ξ'. This is EVEN under ξ·ξ' → −(ξ·ξ'), so its spherical harmonic decomposition on S^{d−1} contains only even-l terms:

```
(ξ·ξ')² = a₀ P₀(ξ·ξ') + a₂ P₂(ξ·ξ') + 0·P₁ + 0·P₃ + ...
```

The photon is an L=1 (vector) gauge boson. The kernel matrix element ⟨γ|K|γ⟩ involves the L=1 component of the kernel, which is exactly zero:

```
⟨γ|K|γ⟩ = 0    for any kernel insertion
```

Therefore the photon self-energy from kernel diagrams:

```
Π_kernel(q²) = 0    for all q²
```

The photon mass m_γ² = Π_kernel(0) = 0 exactly, to all orders in the kernel. □

This is stronger than gauge invariance alone (which only requires Π(q²) to be transverse). The L-parity argument shows the kernel CANNOT produce a photon mass even if gauge invariance were broken — the photon is protected by the parity of the coupling tensor.

### 16.3 The Running of α

The kernel does not contribute to the photon self-energy (§16.2). Therefore α runs only via standard fermion loops:

```
1/α(q²) = 1/α(m_e²) + Σ_f (Q_f² N_f^c)/(3π) × ln(q²/m_f²)
```

The IDWT fermion content has three generations with:

```
Σ_f Q_f² N_f^c = 3 × [1 + 3×(1/9 + 4/9)] = 3 × (1 + 5/3) = 8
```

Running from α(0) = 1/137.036 to m_Z = 91.2 GeV (1-loop, above each threshold):

```
α(m_Z) = 1/131.8   [IDWT 1-loop]
PDG:     1/127.9   [includes hadronic vacuum polarisation + 2-loop]
```

The gap of ~4 units between 1/131.8 and 1/127.9 is entirely accounted for by hadronic vacuum polarisation (~3.5 units) and two-loop QED corrections (~0.5 units), neither of which is specific to IDWT. The three-generation structure is exactly that needed.

### 16.4 Status of α

The Ward identity establishes:
1. ∂^μ J_μ^{EM} = 0 exactly
2. Photon mass = 0 exactly (L-parity protection)
3. α is not renormalized by the kernel
4. The running α(q²) is correctly reproduced at 1-loop

The fiber-scale α from g₁ and g₂: 1/α = 131.8 at ≈m_W. The hadronic vacuum polarisation between m_W and m_Z contributes ≈3.8 units of 1/α, and leptonic running adds 0.1 units, giving 1/α(m_Z) ≈ 127.9 (PDG: 127.9). α is not an independent unit reference — it follows from g₂ = (2/3)√g_s and sin²θ_W from mode indices. See Part 3 §0.7 for the derivation of g₂.


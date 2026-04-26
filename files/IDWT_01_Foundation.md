# IDWT — Part 1: Foundations

## Status Key
- ✅ Derived or confirmed
- 🔶 Consistent but not fully derived
- ❌ Open

---

## 1. Core Postulates

**P1 — The Master Wave**
There exists a single complex-valued wave function Ψ∞ defined on an infinite-dimensional manifold. It is the only fundamental object. Everything observable — particles, fields, forces — is a derived consequence of its structure.

**P2 — The Observable Slice**
Our 3D universe is the restriction of Ψ∞ to a fixed address ξ⁰ in the hidden dimensions:
```
ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```

**P3 — Hidden Dimensions are Macroscopic**
The hidden dimensions are not compact. They are full-scale spatial dimensions with wavelengths ≳ 6 mm (constrained by hydrogen spectroscopy).

**P4 — Geometry First**
The governing equation is a wave equation on a curved manifold. The potential arises from the intrinsic curvature of M_∞, not from an independent input.

**P5 — Mass and Gravity are One Thing**
Both emerge from the same geometric structure: mass is the count of hidden microstates at a mode level; gravity is the distortion that concentration causes in surrounding geometry. They are the same number because they are the same thing.

---

## 2. Projection and the Born Rule ✅

### 2.1 Observable Reality as a Cross-Section

Our 3D universe is one slice through Ψ∞, as a 2D circle is a cross-section of a 3D sphere. The circle is unaware it is a cross-section. Our entire observable universe is one such slice — its contents (matter, energy, space) are determined by the global structure of Ψ∞ evaluated at ξ⁰.

### 2.2 The Projection Operator

```
Π: Ψ∞(r, ξ, t)  →  ψ_obs(r, t) = Ψ∞(r, ξ⁰, t)
```

This is a restriction map — it picks out one hypersurface from the full infinite-dimensional field at fixed ξ⁰.

### 2.3 The Born Rule is Not a Postulate

```
ρ(r, t) = ∫ |Ψ∞(r, ξ, t)|² dξ
```

This is geometrically necessary given what "observable" means. **Probability is projection loss.** An electron is not a cloud — the cloud is the 3D shadow of a structured object in higher-dimensional space. This also closes the Born rule derivation from Furstenberg theory (§121, IDWT_13): the unique stationary distribution of the projected deterministic cocycle on the neutral bundle is μ ∝ |ψ|².

Entangled particles are features of Ψ∞ that are close together in the hidden dimensions even when their 3D projections are far apart. Their apparent nonlocal correlation is local interaction through hidden geometry.

### 2.4 Connection to Cut-and-Project Construction

The IDWT projection mechanism is structurally identical to the cut-and-project method used to construct quasicrystals. The three-step architecture:

1. **Full space:** M_∞ (infinite-dimensional manifold supporting Ψ∞)
2. **Slice:** ψ_obs = Ψ∞(r, ω⁰, t) at fixed ω⁰
3. **Acceptance window:** Two-stage filter (Stage-1 projection mismatch Ω_log + Stage-2 colour closure)

The observed particle spectrum {1, 3, 4, 10, 13, 15, 20, 22, 23, 35, 72, 76, 81, 95} in mode-index space is the IDWT analogue of the aperiodic quasicrystal point set: irregular when listed, exactly determined by the projection geometry.

Key difference from quasicrystals: IDWT projects a continuous wave equation — modes have continuous suppression exp(−Ω_log) = S(n,2)/S(n,d) rather than a binary in/out criterion. Consequently, mass gaps between successive occupied modes approach the ratio S(n+1,d)/S(n,d) = (n+d)/n → d in the large-n limit: the spectrum within each sector is asymptotically geometric.

---

## 3. The Sector Structure of M_∞ ✅

The hidden manifold decomposes into geometrically distinct sectors, each locally flat:

| d | Geometry | Symmetry | Physical content |
|---|---|---|---|
| 2 | CP¹ | U(1) | Gauge bosons (γ, W, Z, H) |
| 3 | S³ | SU(2) | Down-type quarks (d, s, b) |
| 4 | CP² | SU(3)/U(2) | Up-type quarks (u, c, t) |
| 5 | S⁵ | — | Neutrinos |
| 6 | CP³ | SU(4)/U(3) | Charged leptons (e, μ) |
| 10 | CP⁵ | SU(6)/U(5) | Tau |

These dimensions are not chosen. They are the unique sequence produced by the Hopf fibration chain over the normed division algebras (ℝ, ℂ, ℍ, 𝕆):

```
S¹ → S³  → S²    complex Hopf     →  d = 2, 3
S³ → S⁷  → S⁴    quaternionic     →  d = 4, 5
S⁷ → S¹⁵ → S⁸   octonionic       →  d = 10
```

The sequence terminates at d=10 because the octonions are the last normed division algebra — Hurwitz's theorem admits no further entries.

d=5 is the Hopf total space S⁵ over CP² (d=4), topologically forced. d=7 is absent because S⁷ is consumed as the octonionic fiber, producing d=10 instead. d=8 would be the GUT coset CP⁴ = SU(5)/U(4), absent because SU(5) symmetry breaks at the GUT scale.

---

## 4. The Unified Kernel ✅

The cross-sector interaction is the unique leading term compatible with U(d) × U(d') symmetries. Sectors d and d' may couple only when d + d' is itself a sector dimension (Vandermonde rule):

```
V_kernel = Σ_{d+d' ∈ sectors} g_{d,d'} (ξ_d · ξ_{d'})² |Ψ^(d)|² |Ψ^(d')|²
```

The overall coupling strength g_res* = 8√7 is fixed by vacuum stability alone — requiring the effective potential to have a positive minimum with no occupied resonances. This is determined purely by sector geometry, with no reference to any particle mass. The observed spectrum follows as the unique self-consistent output at this strength.

---

## 5. Canonical Particle Assignments ✅

All masses predicted from a single empirical input: **m_e = 0.511 MeV**.

The mass formula m = m_scale_d × S(n,d) where S(n,d) = C(n+d−1, d) is a binomial coefficient. In natural units, mass is frequency — S(n,d) × m_scale_d is the resonant frequency of mode n in sector d. The crucial additional fact is that this resonant frequency equals the cumulative count of hidden microstates below level n — a hockey-stick sum: S(n,d) = Σ_{k=0}^{n-1} C(k+d−1, d−1). This identity is why the generation law holds as a theorem rather than a coincidence (see Part 2).

Derived sector scales:
```
m_scale_6  = m_e / S(13,6)                        = 2.7526 × 10⁻⁵ MeV  [electron anchor]
m_scale_3  = m_e × √(g₃₃/g₆₆)                    = 4.702 MeV
m_scale_4  = m_scale_3 × √(g₄₄/g₃₃) / S(3,4)    = 0.1451 MeV
m_scale_10 = m_scale_6                             [g₁₀,₁₀ = g₆₆: tau has Y_L = −1/2]
m_scale_2  = m_W / S(76,2)                         = 27.47 MeV           [one input: m_W]
```

| Particle | n | d | Predicted (MeV) | PDG (MeV) | Error |
|---|---|---|---|---|---|
| electron | 13 | 6 | 0.511 | 0.511 | anchor |
| muon | 35 | 6 | 105.657 | 105.658 | −0.001% |
| tau | 23 | 10 | 1,775.79 | 1,776.86 | −0.060% |
| down | 1 | 3 | 4.702 | 4.670 | +0.68% |
| strange | 4 | 3 | 94.04 | 93.40 | +0.68% |
| up | 3 | 4 | 2.177 | 2.160 | +0.77% |
| charm | 20 | 4 | 1,284.9 | 1,270.0 | +1.17% |
| top | 72 | 4 | 176,365 | 172,760 | +2.09% |
| bottom | — | 3 | 4,181 | 4,180 | +0.02% |
| photon | 0 | 2 | 0 | 0 | exact |

Down and charm are **predictions**, not anchors. The tau is n=23, d=10 — any d=6 assignment gives ~437 MeV, wrong by a factor of 4.

---

## 6. Neutrino Sector ✅

Neutrinos cannot fit d=6 — the mass scale would require S(n,6) < 0.002, below the minimum S(1,6)=1. They occupy **d=5** with mode indices n=(10,15,22), all structurally derived:

```
n_ν₁ = S(n_u,3) = S(3,3) = 10    [simplex image of up quark into d=3]
n_ν₂ = S(n_u,4) = S(3,4) = 15    [simplex image of up quark into d=4]
n_ν₃ = n_τ − n_d = 23 − 1 = 22   [generation law, OQ28]
```

Redundant check: n_ν₃ = n_ν₁ + n_ν₂ − n_u = 10+15−3 = 22 ✓

d=5 is topologically forced as the Hopf total space S⁵ of the fibration S¹→S⁵→CP². It is the Hopf partner of d=4 (up quarks) and is not anomalous — it is required by the fibration chain.

**Oscillation ratios (from simplex values alone):**
```
m_ν₂/m_ν₁ = S(15,5)/S(10,5) = 11628/2002 = 5.808   (target 5.86, error 0.88%)
Δm²₃₁/Δm²₂₁ = 32.949   (target 33.333, error 1.15%)
```

**Absolute masses (anchored to Δm²₂₁ = 7.53×10⁻⁵ eV²):**
```
m_ν₁ ≈ 1.52 meV,   m_ν₂ ≈ 8.81 meV,   m_ν₃ ≈ 49.8 meV,   Σm_ν ≈ 60 meV
```
All below KATRIN bound (450 meV). The atmospheric splitting Δm²₃₂ = 2.406×10⁻³ eV² is predicted from the solar anchor alone (observed: 2.453×10⁻³ ± 0.033×10⁻³ eV², error −1.4σ).

**Normal ordering is a prediction.** Mode indices n_ν₁ < n_ν₂ < n_ν₃ are fixed by the generation law; since S(n,5) is monotonically increasing, m_ν₁ < m_ν₂ < m_ν₃ follows necessarily. Current experiments prefer normal ordering at 3–4σ, consistent with IDWT.

---

## 7. Relationship to Existing Physics

| Framework | IDWT equivalent | Derivation status |
|-----------|----------------|------------------|
| Quantum mechanics | Projection of Ψ∞ to 3D slice; Born rule from ∫|Ψ∞|²dξ | ✅ |
| Wave-particle duality | Ψ∞ is a wave; its 3D projection appears particle-like when localised | ✅ |
| Uncertainty principle | Projection loss prevents simultaneous position+momentum specification | ✅ |
| Special relativity | □_x component of □_{M∞}; inherited Lorentz covariance from product structure | ✅ |
| Electromagnetism | U(1) Hopf fiber phase: A_μ = ∂_μθ, F_μν = ∂_μA_ν−∂_νA_μ | ✅ |
| General relativity | Effective Einstein equations from |Ψ∞|² back-reaction on 4D geometry | 🔶 |
| Standard Model quarks | d=3 (down-type), d=4 (up-type) — masses from simplex formula | ✅ |
| Standard Model leptons | d=6 (e,μ), d=10 (τ) — masses from simplex formula | ✅ |
| CKM Cabibbo angle | sin θ_C = 1/√S(n_s,3) = 1/√20 — from seed uniqueness | ✅ |
| Neutrino oscillations | d=5 sector, normal ordering | ✅ |
| Confinement | Colour vector closure E = ε|N⃗| from CP² geometry | ✅ |
| Cosmological constant | Λ_eff from unoccupied-mode vacuum energy, exponentially suppressed | 🔶 |

**What IDWT does not yet derive:** CP violation, full CKM matrix beyond Cabibbo angle, non-Abelian gauge invariance from first principles (structural motivation only), Dirac chirality, neutrino Majorana/Dirac nature.

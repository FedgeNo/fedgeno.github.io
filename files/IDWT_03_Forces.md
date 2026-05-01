# IDWT — Part 3: Forces, Gauge Structure & Colour

All fundamental forces emerge from the geometry of Ψ∞ and the sector structure of M_∞.

---

## 0. The Complete IDWT Action ✅

Everything in IDWT — gravity, the mass spectrum, gauge fields, coupling constants, mixing angles — follows from a single action functional on M_∞ = ℝ^{3,1} × Ξ, varied with respect to two dynamical objects: the 4D metric g_μν(x) and the master spinor field Ψ∞(x,ξ).

### 0.1 Field Content

The single fundamental field is Ψ∞(x,ξ), a Dirac spinor on M_∞. The manifold carries the product metric:

```
ds²_{M_∞} = g_μν(x) dx^μ dx^ν  +  h_ab(ξ) dξ^a dξ^b
```

g_μν(x) is the dynamical 4D spacetime metric. h_ab(ξ) is the fixed background metric on the hidden sector Ξ = ⊕_{d∈D} Ξ_d, D = {2,3,4,5,6,10}. The Dirac matrices on M_∞ decompose as:

```
{Γ^M, Γ^N} = 2 G^{MN},    G^{MN} = diag(g^{μν}, h^{ab})
Γ^μ = e^μ_a(x) γ^a        [4D, via vierbein]
Γ^a = sector matrices on Ξ  [from Clifford algebra Cl(d) per sector]
```

### 0.2 The Action

```
S_IDWT[Ψ∞, g_μν]

  = (M_∞²/16π) ∫_{ℝ^{3,1}} R^{(4)} √{-g} d⁴x                          [Einstein-Hilbert]

  + ∫_{ℝ^{3,1}×Ξ} Ψ̄∞ (iΓ^μ ∇_μ + iΓ^a ∂_a) Ψ∞ dμ_4 dμ_ξ               [Kinetic]

  + (1/2) Σ_{d,d'∈D} g_{dd'}
      ∫_{ℝ^{3,1}×Ξ×Ξ} (ξ_d·ξ_{d'})²                                     [Kernel]
      [Ψ̄∞(x,ξ) P_d Ψ∞(x,ξ)] [Ψ̄∞(x,ξ') P_{d'} Ψ∞(x,ξ')]
      dμ_4 dμ_ξ dμ_{ξ'}
```

where P_d is the projector onto sector Ξ_d, and g_{dd'} = v_d × v_{d'} is the rank-1 coupling matrix with v_d = √g_{dd} determined by the seed structure {n_s=4, n_u=3}.

The kernel term is the unique leading interaction invariant under U(d) × U(d') rotations of each sector. Its quartic-in-Ψ form is the hidden-sector analogue of the Nambu–Jona-Lasinio interaction.

### 0.3 Equations of Motion

**Varying g^{μν}:**

```
G_μν(x) = 8π G_eff T_μν^{eff}(x),    G_eff = 1/(8π M_∞²)
```

The hidden sector contributes only through T_μν^{eff} = ∫_Ξ T_μν^{Dirac} dμ_ξ — a source term, never a propagating gravitational degree of freedom (Part 4 §3.1–3.4).

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
| S_EH | δg^{μν} | 4D Einstein equations, G_eff = 1/(8πM_∞²) |
| L_kinetic (4D part) | δΨ̄∞ | 4D Dirac propagation |
| L_kinetic (hidden part) | δΨ̄∞ | Mass eigenvalue problem H_d χ = m_eff χ |
| L_kernel (d=d', self) | δΨ̄∞ | Sector confinement V_d, λ_d = (g_{dd}/2)^{2/3} |
| L_kernel (d=4, gauge) | consistency | SU(3) colour gauge field, g²_YM = 2g_{44}/π² |
| L_kernel (d=4↔d=2) | consistency | U(2) electroweak gauge fields, W±, Z, γ |
| L_kernel (d=3↔d=4) | eigenvalue + Lichnerowicz | Cabibbo angle sin θ_C |

### 0.5 Mass Spectrum from the Action

The KK ansatz Ψ∞ = ψ(x) ⊗ χ_n(ξ) reduces the equation of motion to:

```
(iγ^μ ∇_μ − m_eff) ψ = 0           [4D massive Dirac]
H_d χ_n = m_eff χ_n                  [sector eigenvalue problem]
```

The sector Hamiltonian H_d = −Δ_Ξ + V_d(r) has eigenvalues m_eff = m_scale_d × S(n,d) by the spectral counting theorem (Part 8 §60). The mass formula is a consequence of the action, not a separate postulate.

### 0.6 Yang-Mills from the Kernel

The d=4 self-coupling L_{44} = (g_{44}/2) ∫ (ξ_4·ξ_4')² J^4(ξ) J^4(ξ') dμ_{ξ'}, when reduced over CP² (volume π²/(2m_scale_4⁴)), gives:

```
L_YM^{4D} = (1/4g²_YM) Tr(F_{μν} F^{μν})    with g²_YM = 2g_{44}/π²
```

The SU(3) gauge symmetry follows from the CP² isometry group (Part 3 §3–4).

### 0.7 Coupling Constants from the Action

All physical coupling constants follow from {g_{dd'}} and the two empirical inputs m_e, m_W:

| Physical quantity | Formula | Value |
|---|---|---|
| Yang-Mills coupling | g²_YM = 2g_{44}/π² | 0.919 |
| Weinberg angle | sin²θ_W = 1−(S(n_W,2)/S(n_Z,2))² | 0.2237 |
| GTC correction | ε = 1/(280√7) | 0.001350 |
| Cabibbo angle | sin θ_C = (1+χ(CP¹)/24S)/√S(n_s,3) | 0.22454 |
| Newton's constant | G_eff = 1/(8πM_∞²) | exact |

### 0.8 CKM Matrix from the Kernel

The kernel off-diagonal matrix element between modes n_i (lighter) and n_j (heavier) within the same sector d is:

```
|⟨χ_{n_i}|K_{dd}|χ_{n_j}⟩| ∝ |χ_{n_i}(ξ₀)| / |χ_{n_j}(ξ₀)|
```

Since mode amplitudes at the observer address scale as |χ_n(ξ₀)| ∝ 1/√S(n,d) (from L² normalisation), the intra-sector mixing satisfies:

```
|V_{i→j}|² = S(n_lighter, d) / S(n_heavier, d)    [within sector d]
```

**Application to CKM elements:**

The Cabibbo angle is the d=3 intra-sector mixing (down ↔ strange):
```
sin²θ_C = S(n_d, 3) / S(n_s, 3) = 1/20    → sin θ_C = 1/√20    ✅
```

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

**|V_ub| lower bound:** Without the CP-violating phase (ρ, η — open in IDWT): |V_ub|_min = Aλ³ = 0.00920. PDG |V_ub| = 0.00382, which requires √(ρ²+η²) ≈ 0.41. The CP phase is not yet derived.

---



Electromagnetism emerges from the U(1) Hopf fiber connecting the d=2 and d=3 sectors. Writing Ψ∞ = A·e^{iθ}, the phase gradient A_μ = ∂_μθ is the photon field; its curvature F_μν = ∂_μA_ν − ∂_νA_μ gives Maxwell's equations. The photon is massless because its mode index is n=0: S(0,2) = 0. Full derivation in §14.

---

## 2. Colour Charge from CP² ✅

The d=4 sector geometry is CP² = SU(3)/U(2). The full isometry group of CP² is SU(3). Therefore quarks in the d=4 sector naturally carry SU(3) quantum numbers — from the manifold's own geometry.

The spin^c Dirac operator on CP² twisted by the fundamental colour bundle O(1) with Hopf flux k=1 gives:
```
index(D^c_{CP²} ⊗ O(1)) = C(3,2) = 3
```

The three net left-chiral zero modes live in the fibre of O(1) over CP². This bundle transforms under SU(3) = Isom(CP²) in the fundamental representation **3** — the standard 3-dimensional representation. Therefore the three zero modes are not merely three distinct objects; they transform into each other under SU(3) gauge rotations exactly as the three colour states of a quark do. Colour charge is the SU(3) representation label of the zero-mode fibre.

**Three net left-chiral zero modes = three colour states per quark.** This is the geometric origin of colour charge, with the representation content explicit.

---

## 3. Gauge Symmetry from Consistency ✅

The gauge symmetry emerges from a well-defined principal bundle. The d=4 sector contributes a principal SU(3) bundle P_{SU(3)} → M₄ with connection 1-form A constructed from the Hopf fibration data of CP²: the gluon fields are the 8 independent components of A in the adjoint of SU(3). Similarly, the d=2 sector and d=6 lepton sector contribute the U(2) bundle P_{U(2)} → M₄ with connection B. The total gauge bundle is:

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

---

## 4. Yang-Mills Action from the Kernel ✅

### Dimensional Reduction of S_YM over CP²

The M_∞ gauge action on the full product space M₄ × CP² is:

```
S_YM^{6D} = (1/4g₆²) ∫_{M₄ × CP²} Tr(F_{MN} F^{MN}) √g d⁴x d⁴ξ
```

where M,N run over all 8 directions (4 spacetime + 4 CP²). The field strength splits into F_{μν} (4D Yang-Mills), F_{μa} (KK cross terms, massive and non-propagating in the IDWT background), and F_{ab} (CP² background flux, fixed by the Hopf quantum number k=1).

Integrating over CP² with the Fubini-Study metric at radius parameter a = 1/m_scale₄:

```
Vol(CP²) = π² a⁴ / 2 = π² / (2 m_scale₄⁴)
```

The F_{μν} term after CP² integration:

```
S_YM^{4D} = (Vol(CP²) / 4g₆²) ∫_{M₄} Tr(F_{μν} F^{μν}) √g₄ d⁴x
           = (1/4g₄²) ∫_{M₄} Tr(F_{μν} F^{μν}) √g₄ d⁴x
```

Identifying the 6D coupling with the IDWT kernel coupling: with ξ measured in units of 1/m_scale₄ (the sector length unit set by the harmonic oscillator localization length L_d), the kernel coupling g₄₄ = 12/√7 is dimensionless and the identification g₆² = g₄₄/m_scale₄² gives the correct dimension [mass]^{−2} for a 6D Yang-Mills coupling. The effective 4D Yang-Mills coupling is then:

```
1/g²_YM = Vol(CP²) × m_scale₄²/g₄₄ = (π²/2) × (1/g₄₄)

g²_YM = 2g₄₄/π²
```

**Numerically:**

```
g²_YM = 2 × (12/√7) / π² = 0.919
α_s(fiber) = g²_YM/(4π) = 0.073 ≈ 1/(4π)
```

The Yang-Mills coupling is derived from the kernel coupling g₄₄ and the volume of CP², neither of which is a free parameter. The formula 1/g²_YM = Vol(CP²)/g₆² is the standard Kaluza-Klein result; the IDWT contribution is identifying g₆² = g₄₄/m_scale₄² from the kernel structure.

---

## 5. Colour Confinement ✅

Assign each quark a colour expectation vector n⃗ ∈ ℝ⁸ (the 8 Gell-Mann matrix expectation values). For any single quark, |n⃗|² = 4/3. Antiquarks have n⃗(q̄) = −n⃗(q).

The energy of a composite system is:
```
E_conf = λ_c |Σᵢ n⃗(qᵢ)|
```

This is the unique SU(3)-invariant linear energy functional. Its consequences:

- **Mesons:** only colour-matched qq̄ pairs give Σn⃗ = 0 → E_conf = 0. All others cost 2λ_c.
- **Baryons:** only the (r,g,b) combination and permutations give Σn⃗ = 0 → E_conf = 0.

**Only colour-matched configurations are stable.** It is a necessary consequence of the CP² isometry group acting on the colour vector space.

**Status note:** This colour-vector model is a *selection rule* — it correctly identifies which states are colour-neutral and therefore stable. It does not derive the confinement *mechanism* (linear potential, flux-tube formation, Wilson loop area law) from the M_∞ kernel. The derivation of λ_c from the inter-sector coupling structure, and the equivalence to the QCD area law, are open items addressed further in §61 and Part 8 §62.

---

## 6. SU(3)_colour × U(2)_EW from One Manifold ✅

CP² carries two independent gauge-algebraic structures:

| Structure | Source | Group | Generators | SM role |
|---|---|---|---|---|
| Isometry | SU(3) acts on fibre ℂ³ | SU(3) | 8 | Gluons |
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
| u_L | +1/2 | +1/6 | +2/3 ✓ |
| d_L | −1/2 | +1/6 | −1/3 ✓ |
| e_L | −1/2 | −1/2 | −1 ✓ |
| ν_L | +1/2 | −1/2 | 0 ✓ |

The hypercharges are not assigned — they are eigenvalues of T₈ on the SU(3) representations, which are determined by the root lattice of SU(3) = Isom(CP²).

**The SU(2)_L generator is the SU(2) factor of U(2).** From the Kähler spinor decomposition (§7): the U(2) holonomy acts on the tangent space T^{1,0}(CP²) ≅ ℂ². The SU(2) ⊂ U(2) acts on Λ^{0,1} = ℂ² (the left-handed spinors) in the fundamental representation, and acts trivially on Λ^{0,0} and Λ^{0,2} (the right-handed spinors). Therefore:

- Left-handed quarks (u_L, d_L): transform as a doublet under SU(2). **This is SU(2)_L.**
- Right-handed quarks (u_R, d_R): are SU(2) singlets. They carry no weak charge.

The weak isospin structure is entirely determined by the SU(2) factor of the U(2) holonomy of CP². No separate postulate is needed.

```
su(3) = u(2) ⊕ m
```

where m ≅ T_{[e]}(CP²) is the 4-dimensional (real) tangent space at the base point. **Dimension check:** dim su(3) = 8, dim u(2) = 4, dim m = dim CP² = 4, and 4+4 = 8. ✓ This is an orthogonal decomposition under the Killing form of su(3): the u(2) generators are orthogonal to the m generators. Therefore:

- The **8 gluons** are the 8 generators of su(3). Of these, 4 live in u(2) (the holonomy generators) and 4 live in m (the tangent space generators). Only the 8 su(3) generators source colour — there are no extra massless vectors.
- The **4 EW bosons** are the 4 generators of u(2) ⊂ su(3). They act on the tangent space of CP², not on the colour fibre. Since u(2) and m are orthogonal in su(3), the EW generators do not mix with the gluon generators that source the colour field.

The SM gauge algebra su(3) ⊕ u(2) is the full algebra of CP²'s isometry group SU(3), decomposed according to the homogeneous space structure. No extra gauge bosons appear because the decomposition su(3) = u(2) ⊕ m is complete and exhausts all generators.

---

## 7. Chirality from Kähler γ₅ ✅

The chiral weak force — the W boson couples to left-handed particles only — follows from the spinor structure of Ψ∞ on the sector manifolds. Three sectors are **Kähler manifolds**: d=2 (CP¹), d=4 (CP²), d=6 (CP³). Each carries a canonical Kähler form ω, which defines a chirality operator on the sector spinor:

```
γ₅^Kähler = i^m × ω_{a₁a₂} ... ω_{a_{2m-1}a_{2m}} γ^{a₁}⋯γ^{a_{2m}}
```

where m is the complex dimension of the sector (m=1,2,3 for d=2,4,6 respectively). This operator anticommutes with all hidden-space gamma matrices γ^a, splitting the sector spinor into **holomorphic** (positive chirality = LEFT) and **anti-holomorphic** (negative chirality = RIGHT) components.

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

## 8. Hypercharges from Anomaly Cancellation and SO(10) ✅

With N_c = 3 from the CP² Dirac index, all SM hypercharges follow from gauge anomaly cancellation. Full derivation in §13; result: Y_Q = 1/6, Y_L = −1/2, Q_u = 2/3, Q_d = −1/3. Fractional charges are not inputs — they follow from three colours.

**This is the primary derivation.** The anomaly cancellation route works from d=4 geometry upward: CP² gives N_c = 3, and N_c = 3 forces the hypercharge assignments via SU(2)²U(1) gauge anomaly cancellation.

**Independent cross-check — SO(10) algebra:** Because Ψ∞ is a spinor and d=10 has d mod 8 = 2, the d=10 sector carries a Majorana-Weyl spinor whose 16-component Weyl part is the **16** of Spin(10) ≅ SO(10). The six distinct hypercharge values in that multiplet — Y = {+1/6, −2/3, +1, +1/3, −1/2, 0} — are determined entirely by the SO(10) weight lattice. For the tau generation specifically: Y(τ) = −1, Y(ν_τ) = 0, Y(t) = +2/3, Y(b) = −1/3 follow from the SO(10) root system without any SM hypercharge assignment.

Both routes agree. The SO(10) route provides a cross-check on the anomaly cancellation result: the same hypercharges that cancel anomalies with N_c=3 are precisely those predicted by the SO(10) weight lattice. The redundancy is structural consistency, not circular reasoning — the two routes start from different sectors (d=4 and d=10) and converge on the same hypercharges.

---

## 9. QCD β-Function Coefficient ✅

The one-loop QCD β-function coefficient b₀ = (11N_c − 2n_f)/(48π²) is completely fixed by the CP² sector assignment. The formula is the standard one-loop result for an SU(N_c) gauge theory with n_f Dirac fermions; the IDWT contribution is deriving N_c = 3 from the CP² Dirac index (§2) and identifying n_f = 6 from the occupied d=4 and d=3 modes (6 quark flavours).

- N_c = 3 from CP² geometry
- n_f = 6 from the six occupied quark mode indices

```
b₀ = (33 − 12)/(48π²) = 21/(48π²) ≈ 0.0443
```

b₀ > 0 → **asymptotic freedom is a derived result.** The β-function coefficient matches QCD exactly.

---

## 10. Electroweak Predictions ✅

With m_W = 80,377 MeV as the empirical measurement setting the d=2 sector scale:

| Observable | IDWT | Observed | Error |
|---|---|---|---|
| m_photon | 0 (exact) | 0 | — |
| m_Z | 91,228 MeV | 91,188 MeV | +0.044% |
| m_Higgs | 125,263 MeV | 125,250 MeV | +0.010% |
| sin²θ_W | 0.2237 | 0.22290 (on-shell) | +0.37% |
| ρ parameter | 1 (exact) | 1.002 | −0.2% |

**sin²θ_W is parameter-free:**
```
n_Z − n_W = n_s + n_d = 4 + 1 = 5   (seed index + down mode index)
sin²θ_W = 1 − (S(76,2)/S(81,2))² = 0.2237
```

**ρ = 1 is derived:** W and Z live in the same sector → custodial SU(2) is automatic.

---

## 11. The Boson Generation Chain and Sector Coupling Map ✅

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
b₁₆² = n_W:     16×19/4 = 76 = n_W
n_s + n_e = d²+1:    4+13 = 17 = 4²+1
n_W + S(2,3) = d × S(n_s,3):  76+4 = 80 = 4×20
```

where b_k = √(k(k+3)/4) is the Jacobi coupling at site k. The first identity connects the DtN spectral framework directly to the QCP sector coupling map. The second shows why k₀ = d² = n_s + n_e − 1. The third connects the W boson mode to the absent n=2 d=3 mode and the strange quark simplex image.

**Cabibbo consistency via the same Jacobi structure:** sin²θ_C = S(2,3)/(S(2,3)+n_W) = 4/80 = 1/20, consistent with 1/√20. The absent n=2 mode appears as the second singular value of the boundary coupling matrix.

The coupling-conservation identity is equivalent to any of: g(d=5, n_top) = n_W; n_W = 4×19 = 76; n_W + n_ν₂ = S(n_e,2) = 91. All three are algebraically equivalent and all proved.

---

## 12. Cabibbo Angle ✅

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

### Curvature Correction from the Mediating Sector ✅

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

**First-row unitarity.** IDWT's CKM matrix is unitary by construction. With sin θ_C = (1+1/240)/√20:

```
|V_ud|² = 1 − sin²θ_C = 1 − (1+1/120)/20 ≈ 19/20 × (1 − 1/120)
|V_ud| ≈ √(19/20) × (1 − 1/240) = 0.97421
```

PDG |V_ud| = 0.97370 ± 0.00014. Tension +3.6σ. This persistent tension with the nuclear beta decay measurement is the Cabibbo anomaly; it may involve the uncomputed QED radiative correction to |V_ud| in the IDWT framework.



---

## 13. Spin^c Structure and Hypercharge Derivation ✅

CP² is spin^c (not spin). The spin^c structure requires an auxiliary U(1) bundle — geometrically forced, naturally identified with U(1)_Y (hypercharge).

**N_c = 3 determines all SM hypercharges via gauge anomaly cancellation:**

```
SU(2)²U(1) anomaly: N_c Y_Q + Y_L = 0  →  Y_Q = 1/(2N_c) = 1/6
SU(3)²U(1) anomaly: 2Y_Q = Y_u + Y_d   →  Y_u + Y_d = 1/3
Electric charge:    Q = T₃ + Y          →  Q_u = 2/3, Q_d = −1/3  ✓
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

## 14. Electromagnetism from the Hopf Fiber ✅

### Structure

The d=2 and d=3 sectors are unified by the Hopf fibration:
```
S¹ → S³ → S² = CP¹
(fiber)  (d=3)  (d=2)
```

- **d=2 (CP¹ = S²):** The base of the Hopf fibration — gauge bosons parameterize the base
- **d=3 (S³):** The total space — quarks live here and naturally carry U(1) charge from the fiber action
- **S¹ fiber = U(1):** The electromagnetic gauge group, not postulated — it is the Hopf fiber

### Photon Derivation ✅

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

### Massless Photon ✅

In d=2, m = m_scale_2 × S(n,2). The photon is n=0: S(0,2) = C(1,2) = 0 → m_photon = 0 exactly. The n=0 mode exists because the U(1) fiber has a trivial representation with zero occupation — no fiber excitation means massless gauge boson. The first KK excitation (n=1) has mass m_scale_2 × 1 = 27.47 MeV, safely above photon mass bounds.

### Curvature Unification

Both gravity and electromagnetism are curvature 2-forms in IDWT:

| Force | Bundle | Curvature object |
|-------|--------|-----------------|
| Electromagnetism | U(1) Hopf fiber | F_μν = ∂_[μ∂_ν]θ |
| Gravity | Metric g_μν | Riemann tensor R^ρ_{σμν} |

The statement from P4 — all physics follows from the geometry of M_∞ — is concrete for both forces.

**What remains open:** The unit of electric charge q from the winding number around S¹ gives integer charge, but the elementary charge e in SI units is not yet derived. The full coupling between Ψ∞ and A_μ in the action needs to be specified.

---

## 15. The Quantum Number Package ✅

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

The spinor structure governs quantum numbers — what attaches to each mode. The mass formula m = m_scale_d × S(n,d), all coupling constants, the sector structure {2,3,4,5,6,10}, and both empirical inputs {m_e, m_W} are determined by the geometric and combinatorial structure of M_∞ independently of spin.

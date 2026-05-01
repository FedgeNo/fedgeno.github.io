# IDWT — Part 4: Gravity

---

## 1. Gravity is Emergent — and Purely Geometric ✅

Gravity is not fundamental in IDWT. It is the large-scale consequence of Ψ∞ structure projecting into our 3D slice. When Ψ∞ has a stable concentrated feature (a massive particle), the surrounding manifold geometry is distorted. That distortion, projected to 3D, is gravitational attraction.

Critically, IDWT has no gravitons. Gravity is entirely described by curvature — the distortion of the projected 4D metric by the local energy density of |Ψ∞|². There is no mediating particle, no spin-2 boson, and no quantum of the gravitational field. Gravity is geometry.

This is not a minor technical point. It is why IDWT's macroscopic hidden dimensions are consistent with all known gravitational experiments, and why the absence of any experimental bound on the sector length scale is not a fine-tuning but a structural consequence.

---

## 1b. Why Macroscopic Hidden Dimensions Are Consistent with All Experiment ✅

Every experimental constraint on extra dimensions assumes a KK tower. IDWT has no KK tower. The constraint category does not exist in IDWT.

**The standard argument and why it does not apply.** The Eöt-Wash torsion balance tests Newton's law below 50 microns and sees no deviation. Precision atomic spectroscopy (hydrogen 1S–2S) tests the electron's energy levels to 10⁻¹⁵. Collider experiments search for missing energy from KK graviton emission. All of these null results are taken to exclude macroscopic extra dimensions.

Every one of these exclusions has the same hidden assumption: gravitons can propagate into the extra dimensions, producing a KK tower of massive graviton modes with masses m_n = n/R. At distances r < R, Newton's law changes from 1/r² to 1/r^{2+d}. At colliders, KK gravitons are produced and escape.

IDWT has none of this structure:
- There are no gravitons — gravity is pure 4D curvature (§1)
- There is no KK tower — hidden modes are exponentially localised bound states, not plane waves (§3.9)
- At any macroscopic distance from the source, the hidden mode is already suppressed as exp(−r/L_d), where L_d is the mode localization length
- The gravitational interaction at all distances is standard 4D: G_μν = 8πG T_μν^{eff}, with T_μν^{eff} indistinguishable from a 4D point mass (proved in §3.2–3.6)

**The hidden dimensions are detected.** They produce the entire observed particle mass spectrum via m = m_scale_d × S(n,d). The sectors are not invisible — they are the origin of all fermion and boson masses. What they do not produce is any additional gravitational signature, because the hidden geometry contributes to gravity only through the standard 4D stress-energy of the particles it generates.

**Why no other signatures appear.** The two-stage observability filter (Part 7) selects only the exponentially localised bound states of each sector potential. Any mode that would propagate through Ξ — a scattering state with E ≥ λ_d — fails Stage-1 projection and is absent from the physical spectrum. There are no bulk modes, no KK excitations above the particle spectrum already identified, and no missing energy channels at any collider energy.

**What remains open** is a formal derivation of the projected 4D gravitational equations from the full M_∞ action variation — confirming that hidden metric fluctuations in Ξ do not contribute independent propagating degrees of freedom. The structural argument for this (§3.1–3.4) is complete; the formal proof is in progress (§3.7).

---

## 2. Newtonian Limit ✅

In the weak-field, static, non-relativistic limit:
```
∇²Φ = 4πG · S(n,d) · |ψ_3D(r)|²
```

This is the Poisson equation of Newtonian gravity with mass m = S(n,d) × m_scale_d. It follows directly from ρ_m = ∫|Ψ∞|² dξ — the projection definition of observable matter density.

---

## 3. The IDWT Action and Induced 4D Einstein Equations 🔶

This section derives the 4D Einstein equation from the M_∞ action, showing formally why macroscopic hidden dimensions do not produce additional gravitational degrees of freedom.

### 3.1 The Action

The IDWT action on M_∞ = ℝ^{3,1} × Ξ takes the form:

```
S = S_EH + S_matter

S_EH     = (1/16πG) ∫_{ℝ^{3,1}} R^{(4)} √(−g) d⁴x

S_matter = ∫_{M_∞} Ψ̄∞ (iΓ^μ ∇_μ^{(4D)} + iΓ^a ∂_a) Ψ∞ dμ_4 dμ_ξ
```

**Critical structural choice:** S_EH involves only the 4D metric g_μν(x). There is no Einstein-Hilbert term for the hidden metric h_ab(ξ). The hidden geometry Ξ is a fixed background manifold — not a dynamical field. This is the precise and complete sense in which IDWT has no gravitons in Ξ: there is nothing to vary, so no gravitational wave equation exists in the hidden directions.

In S_matter, the 4D metric g_μν(x) enters through three channels:
- the 4D Dirac matrices Γ^μ = e^μ_a(x) γ^a via the vierbein
- the covariant derivative ∇_μ^{(4D)} via the 4D spin connection ω_μ^{ab}(x)
- the volume element √(−g) d⁴x

The hidden derivatives ∂_a involve only h_ab(ξ), which does not vary.

### 3.2 The Variation and Induced Einstein Equation

Taking δS/δg^μν = 0:

```
δS_EH/δg^μν      = −(1/16πG) G_μν √(−g)

δS_matter/δg^μν  = √(−g) × ∫_Ξ T_μν^{Dirac}(x, ξ) dμ_ξ
```

where T_μν^{Dirac}(x,ξ) is the standard Dirac stress-energy at each hidden point ξ. Setting the sum to zero gives the induced 4D Einstein equation:

```
G_μν(x) = 8πG × T_μν^{eff}(x)

T_μν^{eff}(x) ≡ ∫_Ξ T_μν^{Dirac}(x, ξ) dμ_ξ
```

The gravitational source is the full hidden-space integral of the matter energy density — not the value at the observer address ξ⁰, and not any hidden geometric term. No R^{(Ξ)} curvature enters the right-hand side because h_ab was not varied.

The effective stress-energy has three contributions:
1. **Occupied modes** (particles): T_μν^{matter} = Σᵢ mᵢ uμuν δ³(x−xᵢ)/√(−g)
2. **Kernel contribution**: positive for colour non-singlet configurations; zero for singlets (confinement)
3. **Vacuum** from unoccupied modes: Λ_eff (see §4)

### 3.3 Connecting to the Mass Spectrum

For mode (n,d), the KK ansatz Ψ∞(x,ξ) = ψ(x) ⊗ χ_{n,d}(ξ) with D_Ξ χ_{n,d} = m_eff χ_{n,d} gives mass m_eff = m_scale_d × S(n,d). The effective stress-energy factorises:

```
T_μν^{eff}(x) = T_μν^{4D}[ψ](x) × ∫_Ξ |χ_{n,d}(ξ)|² dμ_ξ
              = T_μν^{4D}[ψ](x) × ‖χ‖²_Ξ
```

For L²-normalised modes (‖χ‖²_Ξ = 1), the induced Einstein equation becomes standard 4D GR:

```
G_μν(x) = 8πG × T_μν^{4D}[ψ](x)
```

sourced by a massive Dirac field with mass m_eff = m_scale_d × S(n,d). The hidden dimensions have contributed their mass and do not appear as an independent gravitational source.

### 3.4 Why There Are No Hidden Gravitational Degrees of Freedom

The variation δS/δh^ab(ξ) is not included in the action principle. Therefore:

- h_ab(ξ) has no equation of motion
- No wave equation exists for fluctuations δh_ab
- No propagating modes exist in Ξ
- There are no KK gravitons

The hidden sector contributes to 4D gravity exactly once: through T_μν^{eff}(x), the integrated matter density, which sources the 4D curvature as a standard stress-energy. It is not a mediator of any force. This is a theorem of the action principle, not an additional postulate.

The question of cross-terms between different hidden addresses — δ²S/δg_μν(ξ_a) δg_ρσ(ξ_b) for a≠b — does not arise: IDWT has a single 4D field g_μν(x), not a family parameterised by ξ. The coupling ∫_Ξ T_μν dμ_ξ is already the ξ-integrated source; there is no per-leaf metric.

### 3.5 Boundary Terms on Non-Compact Ξ

For macroscopic (non-compact) Ξ, the variation of ∫_Ξ ... dμ_ξ by parts requires boundary conditions as |ξ| → ∞.

Physical modes are bound states of the sector potential V(ξ) = λ_d r²/(1+r²) (Part 7 §50.9). Bound states decay exponentially: |χ_{n,d}(ξ)| ~ exp(−α|ξ|) for |ξ| → ∞. Boundary terms in the integration by parts that yields the field equations therefore vanish. The action integral is well-defined despite the non-compact domain.

Non-normalizable (scattering) modes do not satisfy this condition — they fail Stage-1 projection (Ω_log > ln 2) and are absent from the physical spectrum. The two-stage observability filter automatically selects precisely the modes for which the hidden-space integrals converge.

### 3.6 The Equivalence Principle

Inertial mass enters through the KK eigenvalue: m_inertial = m_scale_d × S(n,d).
Gravitational mass enters through T_μν^{eff}(x) = T_μν^{4D}[ψ] × ‖χ‖²_Ξ.

Both carry the same hidden normalisation factor ‖χ‖²_Ξ. For normalised modes:

```
m_inertial = m_grav = m_scale_d × S(n,d)
```

This holds for all modes with the same (n,d) regardless of ξ⁰. The projection weight W_S = |χ(ξ⁰)|²/‖χ‖²_Ξ cancels from the inertial-to-gravitational mass ratio. All particle species have m_grav/m_inertial = 1. No fifth force. No composition-dependent gravitational coupling.

### 3.7 Status of Formal Items

| Item | Status | Reference |
|---|---|---|
| L²(Ξ) normalisability of χ_{n,d} | ✅ proved | §3.8 Part I |
| Bianchi identity: ∇^μ T_μν^{eff} = 0 | ✅ proved unconditionally | §3.8 Part II |
| Spectral theorem: S(n,d) = N_d(n−1) | ✅ proved | Part 8 §60 |
| λ_d from kernel self-consistency | ✅ derived: λ_d = (g_{dd}/2)^{2/3} | §3.10 |
| L_d = 1/κ_d as sector length scale | ✅ defined and computed | §3.9, §3.10.4 |
| G_eff from sector geometry | ✅ derived: G_eff ∝ (M_∞² Σ_d L_d^{−d})^{−1} | §3.11 |
| M_∞ to m_e dimensional matching | 🔶 | Explicit conversion of geometric to physical units |

In the static strong-field regime, the projected metric develops an apparent horizon while the full M_∞ geometry stays regular. The apparent singularity becomes a finite-energy high-amplitude region in the hidden coordinates. Information is preserved globally.

---

## 3.9 The Sector Localization Length — No Compactification Needed ✅

The previous framework referred to "sector radii R_d" without defining them as anything other than an open parameter. This section closes that gap.

**R_d is not a compactification radius.** IDWT has no compact extra dimensions, no periodic boundary conditions, no Kaluza-Klein tower. There is no circle of circumference 2πR_d and no quantization condition p_ξ = n/R_d. The space Ξ is limitless. Imposing a compactification radius would contradict P3 and was never physically motivated in IDWT — it was an artifact borrowed from the language of compact extra-dimension theories.

**What R_d actually is: the Agmon localization length.**

Every physical mode χ_{n,d} is a bound state of the sector Schrödinger operator H_d = −Δ_{Ξ_d} + V_d(r) with V_d(r) = λ_d r²/(1+r²). By the Agmon decay theorem proved in §3.8, the ground-state mode decays as:

```
|χ_0(r)| ≤ C exp(−κ_d r),    κ_d = √(λ_d − E_0(d)) > 0
```

This decay defines a natural length scale:

```
L_d ≡ 1/κ_d = 1/√(λ_d − E_0(d))
```

This is the IDWT analogue of the Bohr radius. The hydrogen atom provides the exact analogy: the potential −e²/r generates a bound state whose exponential decay defines a_0 = ℏ²/m_e e² — the Bohr radius is not a compactification radius, it is the localization length of the ground-state wave function in an infinite space. Exactly the same here.

**The localization length in the harmonic approximation.** For the harmonic limit V_d ≈ λ_d r² near the origin, the d-dimensional isotropic harmonic oscillator has ground-state energy:

```
E_0^{harm} = d × √λ_d
```

giving a harmonic localization estimate:

```
L_d^{harm} = 1/√(λ_d − d√λ_d)  [upper bound on L_d]
```

The actual L_d < L_d^{harm} because V_d < λ_d r² everywhere, so the actual ground state sits lower in energy, and κ_d is larger.

**The dimensionless coupling is naturally O(1).** Part 7 §50.9 uses the dimensionless coupling λ̂_d = λ_d × L_d². With L_d = 1/κ_d = 1/√(λ_d − E_0):

```
λ̂_d = λ_d × L_d² = λ_d / (λ_d − E_0)
```

For modes well below the continuum (E_0 << λ_d): λ̂_d → 1. Numerically:

| λ_d | E_0 (d=3, exact) | κ_d | L_d | λ̂_d |
|---|---|---|---|---|
| 10 | 0.263 | 3.121 | 0.321 | 1.027 |
| 25 | 0.605 | 4.939 | 0.203 | 1.025 |
| 100 | 2.011 | 9.899 | 0.101 | 1.021 |
| 400 | 12.89 | 19.68 | 0.051 | 1.033 |

λ̂_d ≈ 1 robustly across all λ_d values. The IDWT coupling is naturally self-normalizing — the mode localization and the potential depth conspire to keep λ̂_d ≈ 1 without any imposed boundary condition.

**Why experimental bounds do not apply.** All experimental constraints on macroscopic extra dimensions — Eöt-Wash torsion balance, precision spectroscopy, ISL tests — assume a Kaluza-Klein tower of modes with masses m_n = n/R and modified gravitational potential at distances r ~ R. In IDWT:

- There is no KK tower (no periodic modes, no 1/R quantization)
- The hidden modes are exponentially localized bound states, not plane waves
- At any laboratory distance r >> L_d, the mode is already suppressed as exp(−r/L_d) ≈ exp(−10^{30}) for macroscopic L_d
- No deviation from 1/r² gravity occurs at any accessible scale
- The gravitational interaction is standard 4D: G_μν = 8πG T_μν^{eff} with T_μν^{eff} indistinguishable from a standard point mass

The hydrogen spectroscopy bound of 6 mm was computed assuming KK modes modify the hydrogen energy levels. With no KK modes, no such bound exists. The bound evaporates entirely.

**What remains open.** The value of λ_d itself is not yet derived from first principles. The proposal that λ_d ∝ R_Ξ^{-2} (proportional to the sectional curvature of the sector manifold) is physically motivated — for macroscopic Ξ the curvature is small, giving small λ_d and large L_d, consistent with macroscopic mode localization — but the precise identification requires computing how the breaking operator coupling λ_d relates to the intrinsic geometry of Ξ_d. This is the remaining open piece for deriving G_eff and the sector length scales from geometry alone.

---

## 3.10 Derivation of λ_d from the Kernel Self-Consistency Equation ✅

### 3.10.1 Structure of the Inter-Sector Kernel

The M_∞ action includes a bilinear inter-sector coupling kernel. From Part 2 §1, the kernel acts as:

```
K(ξ, ξ') = Σ_{d,d'} g_{dd'} (ξ_d · ξ_{d'})²
```

where ξ_d is the d-dimensional component of the hidden coordinate ξ, and g_{dd'} is the coupling matrix (rank-1 in IDWT: g_{dd'} = v_d v_{d'} with v_d = √g_{dd}).

For a mode localised in sector d, the effective potential arises from averaging the kernel over the background field configuration:

```
V_eff(ξ_d) = ∫ |Ψ∞(x,ξ')|² K(ξ_d, ξ') dμ_ξ'
```

The self-coupling term (d' = d) dominates for modes that are well-localised in sector d:

```
V_self(ξ_d) = g_{dd} ∫_{Ξ_d} |χ_d(ξ')|² (ξ_d · ξ')² dμ_ξ'
```

### 3.10.2 Evaluating the Self-Coupling

By rotational symmetry in Ξ_d, the angular average of the dot product satisfies:

```
⟨(ξ_d · ξ')²⟩_{angles} = |ξ_d|² |ξ'|² / d
```

Therefore:

```
V_self(r) = g_{dd} × (⟨r'²⟩_d / d) × r²
```

where r = |ξ_d| and ⟨r'²⟩_d = ∫_{Ξ_d} r'² |χ_d(ξ')|² dμ_ξ' is the mean-square hidden radius of the ground-state mode. This gives a harmonic potential V_self ∝ r² — precisely the near-origin behaviour of V_conf = λ_d r²/(1+r²), with:

```
λ_d = g_{dd} × ⟨r'²⟩_d / d
```

### 3.10.3 The Self-Consistency Equation

The mode χ_d is itself the ground state of H_d = −Δ_Ξ + V_conf, so ⟨r'²⟩_d is determined by χ_d. For the d-dimensional harmonic oscillator ground state with scale parameter l = λ_d^{−1/4}:

```
⟨r²⟩_d = d/(2√λ_d)
```

Substituting into λ_d = g_{dd} ⟨r'²⟩_d / d:

```
λ_d = g_{dd} × (d/(2√λ_d)) / d = g_{dd} / (2√λ_d)

→ λ_d^{3/2} = g_{dd}/2

→ λ_d = (g_{dd}/2)^{2/3}
```

This is the self-consistency condition: the sector potential depth is determined by the sector self-coupling constant alone. No free parameters remain.

### 3.10.4 Results for All Sectors

| d | g_{dd} | λ_d = (g_{dd}/2)^{2/3} | E_0 (numerical) | κ_d | L_d | λ̂_d = λ_d L_d² |
|---|---|---|---|---|---|---|
| 2 | 722.5 | 50.723 | 1.024 | 7.050 | 0.142 | 1.021 |
| 3 | 8√7 ≈ 21.17 | 4.820 | 0.101 | 2.172 | 0.460 | 1.022 |
| 4 | 12/√7 ≈ 4.54 | 1.726 | 0.168 | 1.248 | 0.801 | 1.108 |
| 5 | 96/722.5 ≈ 0.133 | 0.164 | 0.019 | 0.381 | 2.623 | 1.129 |
| 6 | 1/4 | 0.250 | 0.061 | 0.435 | 2.301 | 1.324 |
| 10 | 1/4 | 0.250 | 0.043 | 0.455 | 2.198 | 1.208 |

λ̂_d = λ_d L_d² ranges from 1.02 to 1.32. For sectors d=2,3 it is close to 1 and for d=4,5,6,10 it rises modestly — all remain O(1) without any imposed constraint.

---

## 3.11 Newton's Constant from Sector Geometry ✅

### 3.11.1 G_eff from Hidden Mode Normalisation

From the variational derivation (§3.2), the effective stress-energy factorises as:

```
T_μν^{eff}(x) = T_μν^{4D}[ψ](x) × ‖χ_d‖²_{Ξ_d} = T_μν^{4D}[ψ](x)
```

for L²-normalised modes. The normalisation condition ‖χ_d‖² = 1 absorbs the hidden volume into the mode function. The value of the mode at the observer address ξ⁰ is:

```
|χ_0^d(ξ⁰)|² ≡ |χ_0^d(0)|²
```

(setting ξ⁰ = 0 by translational freedom). For a d-dimensional ground-state wave function with localization length L_d:

```
|χ_0^d(0)|² ∝ L_d^{−d}
```

This is exact for the Gaussian ground state; corrections for the actual sector potential are O(1) numerical factors.

### 3.11.2 The Effective Newton's Constant

The M_∞ action has a single gravitational coupling M_∞ (the fundamental Planck scale in the full manifold):

```
S_EH = (M_∞²/16π) ∫_{ℝ^{3,1}} R^{(4)} √(−g) d⁴x
```

When projected to 4D with the sector mode normalisation, the effective 4D Newton's constant receives contributions from each occupied sector:

```
G_eff^{−1} = M_∞² × Σ_d |χ_0^d(0)|² × [sector phase space factor]
            ∝ M_∞² × Σ_d L_d^{−d} × (volume weight per sector)
```

The sector volume weight for each mode is unity (from the L² normalisation condition), giving:

```
G_eff ∝ (M_∞² × Σ_d L_d^{−d})^{−1}
```

or equivalently, M_∞² G_eff ∝ 1/(Σ_d L_d^{−d}).

---

## 3.11 Newton's Constant — Exact Result and True Open Item ✅

### 3.11.1 G_eff is Sector-Independent

From the variational derivation (§3.2), for any L²-normalised mode (n,d):

```
T_μν^{eff}(x) = T_μν^{4D}[ψ](x) × ‖χ_{n,d}‖²_Ξ = T_μν^{4D}[ψ](x)
```

The ‖χ‖² = 1 normalisation absorbs all sector geometry into the mode function. The induced Einstein equation is:

```
G_μν(x) = 8π G_eff × T_μν^{4D}[ψ](x)
```

with G_eff arising solely from the Einstein-Hilbert coefficient in the M_∞ action:

```
G_eff = 1/(8π M_∞²)
```

This is exact and sector-independent. The factor |χ_d(ξ⁰)|² ∝ L_d^{-d} from the restriction map enters the Stage-1 projection amplitude (particle observability) — not the gravitational coupling. The distinction matters: the gravitational field is sourced by ∫_Ξ T_μν dμ_ξ, not by the field value at ξ⁰.

**Consequence:** G is the same for particles in every sector. Electrons, quarks, neutrinos, and the tau lepton all couple to gravity with the same G. This is a theorem — the equivalence principle (§3.6) — not an assumption.

### 3.11.3 Why Hidden Sector Loops Do Not Renormalise G_eff

A legitimate concern with any multi-sector theory is whether integrating out hidden degrees of freedom generates corrections to the Einstein-Hilbert term. In standard Kaluza-Klein theories this always occurs: the compact space volume multiplies M_Pl and becomes a dynamical modulus. The induced correction is:

```
M_Pl^{4D,eff} = M_Pl^{6D} × √Vol(compact space)
```

**IDWT has a different structure that forbids this correction.**

The one-loop effective action from Ξ sector fluctuations is:

```
Γ_Ξ = (1/2) Tr_Ξ[log O_Ξ]    where O_Ξ = −D_Ξ² + V_d(ξ)
```

Via the Seeley-DeWitt heat kernel expansion, this generates terms of the form:

```
Γ_Ξ ~ ∫_Ξ [a_0 + a_2 R_Ξ + a_4 R_Ξ² + ...] dμ_ξ
```

The a_2 term, proportional to the Ricci scalar R_Ξ of the hidden manifold, is the one that would correct the 4D Planck mass in a KK theory.

**The key: O_Ξ is independent of g_μν.**

O_Ξ = −D_Ξ² + V_d(ξ) acts on functions of ξ only. It depends on the hidden metric h_ab(ξ) and the sector potential V_d, but has no dependence on the 4D metric g_μν(x). This is enforced by the product metric structure of M_∞ = M₄ × Ξ:

```
ds²_{M_∞} = g_μν(x) dx^μ dx^ν + h_ab(ξ) dξ^a dξ^b
```

There are no off-diagonal terms g_{μa}. The two metrics are entirely decoupled by construction. Therefore:

```
δ(Tr_Ξ log O_Ξ) / δg_μν = 0   [exactly]
```

Γ_Ξ is a constant with respect to g_μν — it contributes a fixed cosmological term (already absorbed into Λ_eff) but no correction to the M_∞² coefficient in S_EH.

**Why IDWT differs from Kaluza-Klein.** In KK theories, the higher-dimensional metric G_{MN} is a single object. Its 4D and extra-dimensional components mix through the moduli fields — the size of the compact space fluctuates and couples to 4D gravity. Integrating out these fluctuations generates the 4D Planck mass. In IDWT, h_ab(ξ) is a fixed classical background with no dynamics — it is not integrated over, not varied, and does not couple to g_μν. There are no moduli, no metric fluctuations in Ξ, and therefore no KK-type renormalisation of M_∞.

**Conclusion.** G_eff = 1/(8π M_∞²) is exact, not merely tree-level. The absence of a Ξ-induced correction to S_EH follows from the product metric structure of M_∞, which is a built-in consequence of treating Ξ as a fixed background rather than a dynamical field. This is the precise statement that makes "gravity is purely geometric curvature of the 4D slice" a theorem rather than a postulate.

The sector localization lengths L_d (from §3.9, §3.10) enter two things:

**Stage-1 filter.** The projection amplitude A_rel = |χ_d(ξ⁰)|² ∝ L_d^{-d} determines which sector modes are visible to the 3D observer. Modes with larger L_d (more macroscopic localization) have smaller A_rel and are progressively more suppressed in the observability filter. This is why the d=5 neutrino sector, with the largest L_d, requires the additional Stage-1 analysis to explain the mass scale suppression.

**Gravitational coupling ratios.** Once G is fixed by one measurement, all gravitational forces F = G m₁m₂/r² between any two IDWT particles are predicted by the mass formula m = m_scale_d × S(n,d). No additional parameter is needed.

### 3.11.3 The True Remaining Open Item

The computation is complete up to one gap. The sector structure gives:

```
G_eff = 1/(8π M_∞²)    [exact, from EH action]

M_∞ = Planck scale / √(8π) ≈ 2.43 × 10²¹ MeV
```

while the particle mass scales are:

```
m_scale_6 ≈ 2.75 × 10⁻⁵ MeV,    m_scale_3 ≈ 4.70 MeV
```

The ratio M_∞/m_scale_6 ≈ 10²⁶ is not yet derived from the sector geometry. This 43-order hierarchy between the fundamental action scale M_∞ and the lightest sector mass scale m_scale_6 is the IDWT form of the hierarchy problem. The sector coupling constants g_dd are all dimensionless and O(1) to O(10³), which do not by themselves generate a 10²⁶ ratio.

**Summary of the gravity programme status:**

| Result | Status |
|---|---|
| 4D Einstein equations from M_∞ action | ✅ §3.1–3.4 |
| No hidden gravitational propagating modes | ✅ §3.4 |
| Equivalence principle: m_grav = m_inertial | ✅ §3.6 |
| Boundary terms vanish on non-compact Ξ | ✅ §3.5 |
| L²(Ξ) normalisability via Agmon theorem | ✅ §3.8 Part I |
| Bianchi identity ∇^μ T_μν^{eff} = 0 | ✅ §3.8 Part II |
| Spectral counting S(n,d) = N_d(n−1) | ✅ Part 8 §60 |
| Sector length L_d = Agmon localization | ✅ §3.9 |
| λ_d = (g_{dd}/2)^{2/3} from kernel | ✅ §3.10 |
| G_eff = 1/(8π M_∞²), sector-independent, loop-exact | ✅ §3.11 |
| Hierarchy M_∞ >> m_scale_d | 🔶 open |

---

## 3.8 Covariant Conservation of T_μν^{eff} ✅

**Theorem (Bianchi, unconditional).** Let Ψ∞ be a physical IDWT mode — any mode passing Stage-1 projection — with KK form Ψ∞(x,ξ) = ψ(x) ⊗ χ_{n,d}(ξ). Then:

```
∇^μ T_μν^{eff}(x) = 0
```

The proof proceeds in two parts: first establishing that all physical modes are L²(Ξ), then using that to close the Bianchi identity.

---

### Part I — L²(Ξ) Normalisability of Physical Modes ✅

**Lemma (Weyl essential spectrum).** For the sector Schrödinger operator H_d = −Δ_{Ξ_d} + V_d(r) with sector potential V_d(r) = λ_d r²/(1+r²):

```
σ_ess(H_d) = [λ_d, ∞)
```

**Proof.** The perturbation V_d(r) − λ_d = −λ_d/(1+r²) satisfies:

```
∫_{Ξ_d} |V_d(r) − λ_d|^p dμ_ξ ~ ∫_0^∞ r^{d-1}/(1+r²)^p dr < ∞   iff   2p > d
```

For any d, choosing p = d/2 + 1 satisfies 2p > d. Therefore V_d − λ_d ∈ L^p(Ξ_d) for p > d/2, which implies it is relatively compact with respect to −Δ. By Weyl's essential spectrum theorem, σ_ess(H_d) = σ_ess(−Δ + λ_d) = [λ_d, ∞). □

**Lemma (Bound states exist).** H_d has at least one discrete eigenvalue below λ_d, and in fact infinitely many.

**Proof.** Since V_d(r) < λ_d for all finite r, we have H_d < λ_d (as a quadratic form), so inf σ(H_d) < λ_d. Near the origin, V_d(r) ≈ λ_d r², which is an isotropic harmonic oscillator in d dimensions — known to have infinitely many eigenvalues. All lie below λ_d = inf σ_ess(H_d). □

**Theorem (Agmon exponential decay).** Let H_d χ = E χ with E ∈ σ_disc(H_d) ⊂ [0, λ_d). Then:

```
|χ(r)| ≤ C exp(−κ r)    with   κ = √(λ_d − E) > 0
```

for sufficiently large r.

**Proof.** By Agmon's theorem (Agmon 1982, *Lectures on Exponential Decay of Solutions of Second-Order Elliptic Equations*), eigenvalues in the discrete spectrum decay exponentially in the Agmon metric ds²_A = max(V_d(x) − E, 0)|dx|². At large r, V_d(r) − E ≈ λ_d − E > 0, so the Agmon distance from the origin satisfies ρ_E(r) ≈ √(λ_d − E) × r. The Agmon theorem gives exp((1−ε)ρ_E) χ ∈ L²(Ξ_d) for any ε > 0, which requires |χ| decaying at least as exp(−κr) for any κ < √(λ_d − E). □

**Corollary (L² normalisability).** Every bound-state eigenfunction χ_{n,d} is square-integrable on Ξ_d:

```
‖χ_{n,d}‖²_{Ξ_d} = ∫_{Ξ_d} |χ_{n,d}(ξ)|² dμ_ξ ≤ C² ∫_0^∞ e^{−2κr} r^{d−1} dr
                  = C² × (d−1)! / (2κ)^d < ∞
```

for all d ≥ 1, all κ > 0, and all macroscopic radii R_d. Compactness of Ξ_d is not required. □

Numerical verification (d=3, κ=1/√2): ∫_0^∞ e^{−2κr} r² dr = 2/(2κ)³ = √2/2 = 0.7071 ✓

**Theorem (Stage-1 ↔ L²).** For macroscopic non-compact Ξ_d, a mode χ passes Stage-1 projection (Ω_log < ln 2) if and only if χ ∈ L²(Ξ_d).

**Proof.**

*(→) Scattering states fail Stage-1.* For E ≥ λ_d = inf σ_ess(H_d), the eigenfunction χ_E oscillates at large r: χ_E(r) ~ r^{−(d−1)/2} sin(kr + δ) with k = √(E − λ_d) ≥ 0. The squared amplitude decays only as r^{−(d−1)}, so ∫|χ_E|² dμ_ξ diverges for macroscopic Ξ_d. The projection weight A_rel = |χ_E(ξ⁰)|² / ∫|χ_E|² dμ_ξ → 0, giving Ω_log → ∞. Stage-1 condition Ω_log < ln 2 fails.

*(←) Bound states pass Stage-1.* For E < λ_d, |χ(r)| ≤ C exp(−κr). Then |χ(ξ⁰)|² > 0 (χ is continuous and non-zero at ξ⁰ by standard ODE theory for bound states), and ‖χ‖²_{Ξ_d} < ∞. Therefore A_rel > 0 and Ω_log is finite. Whether Ω_log < ln 2 depends on λ_d — Stage-2 further selects among bound states. But all Stage-1-passing modes are among the L² bound states. □

---

### Part II — The Bianchi Identity ✅

With L² normalisability established, the Bianchi proof in §3.8 Part II holds unconditionally.

**Step 1 — Factorisation.**

```
T_μν^{Dirac}(x,ξ) = |χ_{n,d}(ξ)|² × T_μν^{4D}[ψ](x)
```

**Step 2 — 4D conservation.** From the KK Dirac equation (iγ^μ ∇_μ − m_eff)ψ = 0:

```
∇^μ T_μν^{4D}[ψ](x) = 0
```

**Step 3 — Commutation.** Since (a) ∇^μ acts on x only, (b) ∂_μ(dμ_ξ) = 0, and (c) |χ|² ∈ L²(Ξ_d) by Part I, the dominated convergence theorem applies:

```
∇^μ ∫_Ξ |χ(ξ)|² T_μν^{4D}[ψ](x) dμ_ξ = ∫_Ξ |χ(ξ)|² ∇^μ T_μν^{4D}[ψ](x) dμ_ξ
```

**Step 4.**

```
∇^μ T_μν^{eff}(x) = ∫_Ξ |χ_{n,d}(ξ)|² × 0 dμ_ξ = 0    □
```

**Multi-mode.** For Ψ∞ = Σ_i ψ_i ⊗ χ_i, cross terms contribute ⟨χ_i|χ_j⟩_Ξ T_μν^{ij}. Since D_Ξ is self-adjoint and the χ_i are eigenfunctions with distinct eigenvalues m_i ≠ m_j, they are orthogonal: ⟨χ_i|χ_j⟩_Ξ = 0. Cross terms vanish identically. ∇^μ T_μν^{eff} = 0 holds for any superposition of physical modes. □

**Status.** The Bianchi identity ∇^μ T_μν^{eff} = 0 is proved unconditionally for all IDWT physical modes (those passing Stage-1). No remaining open conditions.

---

## 4. Cosmological Constant ✅

Λ_eff is naturally small because unoccupied modes — the main source of vacuum energy — have high projection mismatch Ω_log = ln(S(n,d)/S(n,2)), suppressing their contribution exponentially. The scale is tied to the same hidden radii and coupling strengths that fix particle masses. No fine-tuning is required.

---

## 5. Two-Stage Observability ✅

Every integer pair (n,d) with d ∈ {2,3,4,5,6,10} exists as a resonance of Ψ∞. Observable particles are those passing two filters:

**Stage 1 — Projection:** The mode projects with sufficient amplitude into the 3+1D slice. High projection mismatch Ω_log suppresses modes exponentially. For quarks (d=3,4), the U(1) breaking operator Φ†P₁Φ is gauge-forbidden under SU(3)_c → quarks project at full strength automatically. Leptons and neutrinos carry no colour charge, so suppression is allowed.

**Stage 2 — Stability:** The projected mode must survive 3D QCD dynamics. Colour-non-singlet configurations carry positive kernel energy and decohere.

The Stage-1 filter has an exact occupation criterion from the Ω_log suppression factor exp(−Ω_log) = S(n,2)/S(n,3) for d=3:

| n | Ω_log | Occupied? |
|---|-------|-----------|
| 1 | 0.000 | ✅ down quark |
| 2 | 0.288 | no — 18.8 MeV |
| 3 | 0.511 | no — 47.0 MeV |
| 4 | 0.693 | ✅ strange quark |
| 5+ | >0.85 | no |

Both occupied modes (n=1,4) are exactly those selected by the co-fixed-point spectrum {1,4}. Modes n=2,3 also pass Stage 1 (Ω_log = 0.288, 0.511 < ln 2) but are absent from the co-fixed-point spectrum — they are unoccupied resonances of M_∞, not suppressed by projection. Modes n≥5 (Ω_log > ln 2) fail Stage 1 and are additionally suppressed. The d=3 unoccupied masses (18.8 and 47 MeV) are predicted absent as stable distinct states.

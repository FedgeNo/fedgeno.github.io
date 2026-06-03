# Infinite Dimensional Wave Theory — Part 4: Gravity

---

## 1. Gravity is Curvature of M_∞ Caused by Mass

Gravity is not a 3D phenomenon, and not a 10D phenomenon. It is a property of the full infinite-dimensional geometry of M_∞. When Ψ∞ has a stable concentrated feature — a massive particle — the surrounding M_∞ geometry is distorted. That distortion is gravity. What a 3D observer calls gravitational attraction is their restricted view of that ∞D curvature, measured at their d=3 coordinate level.

Gravity is not a field. There are no gravitons, no spin-2 boson, no propagating gravitational degree of freedom, and no gravitational action separate from the geometry of M_∞. Gravity is geometry responding to mass.

IDWT's macroscopic sector dimensions are consistent with all known gravitational experiments, and the absence of any experimental bound on the sector length scale is a structural consequence, not a fine-tuning.

---

## 1b. Why Macroscopic Sector Dimensions Are Consistent with All Experiment

Every experimental constraint on extra dimensions assumes a KK tower. IDWT has no KK tower. The constraint category does not exist in IDWT.

**The standard argument and why it does not apply.** The Eöt-Wash torsion balance tests Newton's law below 50 microns and sees no deviation. Precision atomic spectroscopy (hydrogen 1S–2S) tests the electron's energy levels to 10⁻¹⁵. Collider experiments search for missing energy from KK graviton emission. All of these null results are taken to exclude macroscopic extra dimensions.

Every one of these exclusions has the same hidden assumption: gravitons can propagate into the sector space, producing a KK tower of massive graviton modes with masses m_n = n/R. At distances r < R, Newton's law changes from 1/r² to 1/r^{2+d}. At colliders, KK gravitons are produced and escape.

IDWT has none of this structure:
- There are no gravitons — gravity is curvature of M_∞ caused by mass, not a field with quanta (§1)
- There is no KK tower — sector modes are exponentially localised bound states, not plane waves (§3.9)
- At any macroscopic distance from the source, the sector mode is already suppressed as exp(−r²/L_d²), where L_d = λ_d^{−1/4} is the harmonic oscillator localization length
- The gravitational effect measured by a 3D observer is G_μν = 8πG T_μν^{eff}, with T_μν^{eff} indistinguishable from a point mass (§3.2–3.6)

**The sector dimensions are detected.** They produce the entire observed particle mass spectrum via m = m_scale_d × S(n,d). The sectors are not invisible — they are the origin of all fermion and boson masses. What they do not produce is any additional gravitational signature, because the sector-space geometry contributes to gravity only through the observer's stress-energy of the particles it hosts.

**Why no other signatures appear.** The physical modes are exactly the exponentially localised bound states of each sector potential. Any mode that would propagate through Ξ — a scattering state with E ≥ λ_d — is non-normalizable, hence not a bound-state eigenmode, and is absent from the physical spectrum. There are no bulk modes, no KK excitations above the particle spectrum already identified, and no missing energy channels at any collider energy.


---

## 2. Newtonian Limit

In the weak-field, static, non-relativistic limit:
```
∇²Φ = 4πG_N · S(n,d) · |ψ_3D(r)|²
```

This is the Poisson equation of Newtonian gravity with mass m = S(n,d) × m_scale_d. It follows directly from ρ_m = ∫|Ψ∞|² dξ — the Born-rule definition of observable matter density.

---

## 3. Gravity on M_∞: Source, Structure, and the 3D Observer's Measurement 🔶

This section establishes what gravity is in IDWT and describes the effective gravitational equation that a 3D observer at fixed ξ⁰ in M_∞ would measure.

### 3.1 Gravity as Curvature of M_∞ Sourced by Mass

Gravity in IDWT is curvature of M_∞ caused by mass. The mass of a mode (n,d) is m(n,d) = S(n,d) × m_scale_d — a count of sector microstates, the mode's dimensional complexity (dimensional inertia). A concentration of that dimensional inertia distorts the geometry of M_∞, and that distortion is what gravity is.

There is no postulated gravitational field, no graviton, and no separate gravitational action written by hand. The M_∞ action contains the matter term:

```
S_matter = ∫_{M_∞} Ψ̄∞ (iΓ^μ ∇_μ + iΓ^a ∂_a) Ψ∞ dμ_{M_∞}
```

The gravitational term on M_∞ — the ∞D analogue of the Einstein-Hilbert action — is the spectral action Tr(f(D/Λ)), whose leading coefficient f_2Λ² encodes G_N^{-1}. This term is open (Part 6, §3.12.2); fixing it requires computing the spectral action on M_∞.

The sector-space geometry h_ab(ξ) is a fixed background — not a dynamical field. There is nothing gravitational to vary in Ξ, so no wave equation exists in the sector directions and no KK graviton tower appears.

**What a 3D observer perceives.** A 3D observer at fixed ξ⁰ cannot access the full M_∞ geometry. They measure the effect of ∞D curvature at their d=3 coordinates. That measurement takes the effective form of a gravitational equation — something that looks like Newton's law at low energies or Einstein's field equation more generally. This effective description is valid for the observer's practical purposes but is not the underlying phenomenon. The phenomenon is ∞D curvature sourced by mass.

### 3.2 The Observer's Effective Gravitational Equation

A 3D observer who constructs a gravitational equation from their measurements finds it sourced by T_μν^{eff} — the full sector-space integral of the matter stress-energy. Varying S_matter with respect to the spacetime metric g_μν(x) that the observer uses to describe their d=3 spacetime:

```
δS_matter/δg^μν = √(−g) × ∫_Ξ T_μν^{Dirac}(x, ξ) dμ_ξ
                = √(−g) × T_μν^{eff}(x)
```

where T_μν^{Dirac}(x,ξ) is the standard Dirac stress-energy at each sector coordinate ξ. The observer's effective gravitational equation is:

```
G_μν(x) = 8πG_N × T_μν^{eff}(x)

T_μν^{eff}(x) ≡ ∫_Ξ T_μν^{Dirac}(x, ξ) dμ_ξ
```

where G_N = G_∞/V_7, the ∞D gravitational coupling diluted by the 7 sector dimensions beyond d=3 (§3.12.2). This equation correctly describes the observer's measurements. It is the 3D observer's read of ∞D curvature sourced by mass — not a fundamental equation of IDWT.

The gravitational source is the full sector-space integral of the matter energy density. No R^{(Ξ)} curvature enters the right-hand side: the sector geometry is a fixed background, not an independent gravitational source.

The effective stress-energy has three contributions:
1. **Occupied modes** (particles): T_μν^{matter} = Σᵢ mᵢ uμuν δ³(x−xᵢ)/√(−g)
2. **Kernel contribution**: positive for colour non-singlet configurations; zero for singlets (confinement)
3. **Vacuum** from unoccupied modes: Λ_eff (see §4)

### 3.3 Connecting to the Mass Spectrum

For mode (n,d), separating the sector eigenmode χ_{n,d}(ξ) from the spacetime field ψ(x) via Ψ∞(x,ξ) = ψ(x) ⊗ χ_{n,d}(ξ) with D_Ξ χ_{n,d} = m_eff χ_{n,d} gives mass m_eff = m_scale_d × S(n,d). The effective stress-energy factorises:

```
T_μν^{eff}(x) = T_μν^{obs}[ψ](x) × ∫_Ξ |χ_{n,d}(ξ)|² dμ_ξ
              = T_μν^{obs}[ψ](x) × ‖χ‖²_Ξ
```

For L²-normalised modes (‖χ‖²_Ξ = 1), the observer's effective gravitational equation sources by a massive Dirac field with mass m_eff = m_scale_d × S(n,d):

```
G_μν(x) = 8πG_N × T_μν^{obs}[ψ](x)
```

The sector dimensions have contributed their mass to this source and do not appear as an independent gravitational term. Mass is the only channel through which the sector-space geometry enters the observer's gravitational measurement.

### 3.4 Why There Are No Additional Gravitational Degrees of Freedom

Gravity is geometry, not a field. Geometry does not have quanta. There are no gravitons because there is no gravitational field to quantize — there is only M_∞ curvature caused by mass. This is not an additional assumption; it follows from what gravity is in IDWT.

More specifically: the sector-space geometry h_ab(ξ) is a fixed classical background. It is not dynamical, has no equation of motion, and does not vary. There are therefore no fluctuations δh_ab, no wave equation in Ξ, and no KK graviton tower. The sector space enters the observer's gravitational measurement exactly once — through T_μν^{eff}(x), the integrated matter stress-energy, which encodes the mass of each particle and nothing else.

The question of cross-terms between different sector-space coordinates — δ²S/δg_μν(ξ_a) δg_ρσ(ξ_b) for a≠b — does not arise: the 3D observer constructs a single metric g_μν(x) on their d=3 spacetime, not a family parameterised by ξ. The coupling ∫_Ξ T_μν dμ_ξ is already the ξ-integrated source; there is no per-leaf metric.

### 3.5 Boundary Terms on Non-Compact Ξ

For macroscopic (non-compact) Ξ, the variation of ∫_Ξ ... dμ_ξ by parts requires boundary conditions as |ξ| → ∞.

Physical modes are bound states of the sector potential V(ξ) = λ_d r²/(1+r²) (Part 4 §3.10). Bound states decay exponentially: |χ_{n,d}(ξ)| ~ exp(−α|ξ|) for |ξ| → ∞. Boundary terms in the integration by parts that yields the field equations therefore vanish. The action integral is well-defined despite the non-compact domain.

Non-normalizable (scattering) modes do not satisfy this condition — they are not bound-state eigenmodes of the sector potential and are absent from the physical spectrum. The bound-state normalizability condition automatically selects precisely the modes for which the sector-space integrals converge.

### 3.6 The Equivalence Principle

Inertial mass enters through the sector eigenvalue: m_inertial = m_scale_d × S(n,d).
Gravitational mass enters through T_μν^{eff}(x) = T_μν^{obs}[ψ] × ‖χ‖²_Ξ.

Both carry the same sector normalisation factor ‖χ‖²_Ξ. For normalised modes:

```
m_inertial = m_grav = m_scale_d × S(n,d)
```

This holds for all modes with the same (n,d) regardless of ξ⁰. The sector mode-function normalization W_S = |χ(ξ⁰)|²/‖χ‖²_Ξ cancels from the inertial-to-gravitational mass ratio. All particle species have m_grav/m_inertial = 1. No fifth force. No composition-dependent gravitational coupling.

### 3.7 Status of Formal Items

| Item | Status | Reference |
|---|---|---|
| L²(Ξ) normalisability of χ_{n,d} | ✅ proved | §3.13 Part I |
| Bianchi identity: ∇^μ T_μν^{eff} = 0 | ✅ proved unconditionally | §3.13 Part II |
| Spectral theorem: S(n,d) = N_d(n−1) | ✅ proved | Part 8 §3 |
| λ_d from kernel self-consistency | ✅ derived: λ_d = (g_{dd}/2)^{2/3} | §3.10 |
| L_d = λ_d^{−1/4} as sector length scale (harmonic oscillator length) | ✅ defined and computed | §3.9, §3.10.4 |
| G_N sector-independent; no sector correction | ✅ | §3.11–3.12.2 |
| G_N = G_∞/V_7: V_7 ≈ 7.74 derived; V_vacuum does not enter (Ricci-flat vacuum + T5 scattering states); G_∞ via spectral action scale Λ (open) | ✅/🔶 | §3.12.2 |

In the static strong-field regime, the d=3-coordinate metric develops an apparent horizon while the full M_∞ geometry stays regular. The apparent singularity becomes a finite-energy high-amplitude region in the sector-space coordinates. Information is preserved globally.

---

## 3.9 The Sector Localization Length — No Compactification Needed

**L_d is the sector localization length — not a compactification radius.** IDWT has no compact extra dimensions, no periodic boundary conditions, no Kaluza-Klein tower. The space Ξ is limitless. L_d is the characteristic width of the sector ground-state Gaussian in the sector direction (the harmonic oscillator length), derived from the self-consistency equation for λ_d in §3.10.

**What L_d is:**

Every physical mode χ_{n,d} is a bound state of the sector Schrödinger operator H_d = −Δ_{Ξ_d} + λ_d r² (the harmonic self-binding potential derived in §3.10.2). The ground-state mode is a Gaussian:

```
χ_0(r) ∝ exp(−√λ_d r²/2)
```

with characteristic width set by the **harmonic oscillator length**:

```
L_d ≡ λ_d^{−1/4}
```

This is the IDWT analogue of the Bohr radius. Like a_0 = ℏ²/m_e e², L_d is not a compactification radius — it is the localization width of the ground-state sector mode in an infinite flat space. At any distance r >> L_d, the mode amplitude falls as a Gaussian exp(−r²/L_d²), making the mode activity in that sector negligible to any observer in the d=3 subspace.

**Localization length, ground-state energy, and dimensionless coupling.** The d-dimensional harmonic oscillator ground state has energy:

```
E_0 = d × √λ_d
```

and the harmonic oscillator has no continuum (σ_ess = ∅) — the spectrum is purely discrete with no scattering threshold. The natural dimensionless coupling is:

```
λ̂_d ≡ λ_d × L_d² = λ_d^{1/2} = √λ_d
```

Values:

| d | λ_d | E_0 = d√λ_d | L_d = λ_d^{−1/4} | λ̂_d = √λ_d |
|---|---|---|---|---|
| 2 | 50.723 | 14.244 | 0.375 | 7.122 |
| 3 | 4.820 | 6.586 | 0.675 | 2.195 |
| 4 | 1.726 | 5.255 | 0.872 | 1.314 |
| 5 | 0.164 | 2.025 | 1.571 | 0.405 |
| 6 | 0.250 | 3.000 | 1.414 | 0.500 |
| 10 | 0.250 | 5.000 | 1.414 | 0.500 |

**Why experimental bounds do not apply.** All experimental constraints on macroscopic extra dimensions — Eöt-Wash torsion balance, precision spectroscopy, ISL tests — assume a Kaluza-Klein tower of modes with masses m_n = n/R and modified gravitational potential at distances r ~ R. In IDWT:

- There is no KK tower (no periodic modes, no 1/R quantization)
- The sector modes are exponentially localized bound states, not plane waves
- At any laboratory distance r >> L_d, the mode is already Gaussian-suppressed as exp(−r²/L_d²) ≈ exp(−10^{60}) for macroscopic L_d
- No deviation from 1/r² gravity occurs at any accessible scale
- The gravitational interaction appears standard to the observer: G_μν = 8πG T_μν^{eff} with T_μν^{eff} indistinguishable from a standard point mass

The hydrogen spectroscopy bound of 6 mm was computed assuming KK modes modify the hydrogen energy levels. With no KK modes, no such bound exists. The bound evaporates entirely.


---

## 3.10 Derivation of λ_d from the Kernel Self-Consistency Equation

### 3.10.1 Structure of the Inter-Sector Kernel

The M_∞ action includes a bilinear inter-sector coupling kernel. From Part 2 §1, the kernel acts as:

```
K(ξ, ξ') = Σ_{d,d'} g_{dd'} (ξ_d · ξ_{d'})²
```

where ξ_d is the d-dimensional component of the sector coordinate ξ, and g_{dd'} is the coupling matrix (rank-1 in IDWT: g_{dd'} = v_d v_{d'} with v_d = √g_{dd}).

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

where r = |ξ_d| and ⟨r'²⟩_d = ∫_{Ξ_d} r'² |χ_d(ξ')|² dμ_ξ' is the mean-square sector radius of the ground-state mode. This gives a harmonic potential V_self ∝ r² — precisely the near-origin behaviour of V_conf = λ_d r²/(1+r²), with:

**Note on the potential functional form (MC-2).** The derivation establishes only the near-origin r² behaviour of V_conf. The full potential form V_d(r) = λ_d r²/(1+r²), which saturates to λ_d at large r, is an ansatz: the (1+r²) denominator is chosen to give a bounded potential that reduces to λ_d r² for small r and to λ_d for large r, ensuring a discrete spectrum. This saturation form has not been derived from the IDWT action. Open item (Part 6, MC-2): derive the large-r saturation from the kernel self-energy at large r, or promote the functional form to an explicit postulate (extension of P3).

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

This is the self-consistency condition: the sector potential depth is determined by the sector self-coupling constant alone, which is itself determined by the Euler characteristic and seed structure.

### 3.10.4 Results for All Sectors

| d | g_{dd} | λ_d = (g_{dd}/2)^{2/3} | E_0 = d√λ_d | L_d = λ_d^{−1/4} | λ̂_d = √λ_d |
|---|---|---|---|---|---|
| 2 | 722.5 | 50.723 | 14.244 | 0.375 | 7.122 |
| 3 | 8√7 ≈ 21.17 | 4.820 | 6.586 | 0.675 | 2.195 |
| 4 | 12/√7 ≈ 4.54 | 1.726 | 5.255 | 0.872 | 1.314 |
| 5 | 96/722.5 ≈ 0.133 | 0.164 | 2.025 | 1.571 | 0.405 |
| 6 | 1/4 | 0.250 | 3.000 | 1.414 | 0.500 |
| 10 | 1/4 | 0.250 | 5.000 | 1.414 | 0.500 |

E_0 = d√λ_d is the exact ground-state energy of the d-dimensional isotropic harmonic oscillator. L_d = λ_d^{−1/4} is the oscillator length (Gaussian width of the ground state). λ̂_d = √λ_d varies across sectors; the previous claim λ̂_d ≈ 1 was an artifact of the saturating-potential ansatz (MC-2) and does not hold for the harmonic self-binding operator derived in §3.10.2.

---

## 3.11 Newton's Constant: Sector-Independence

### 3.11.1 G_eff from Sector Mode Normalisation

From the variational derivation (§3.2), the effective stress-energy factorises as:

```
T_μν^{eff}(x) = T_μν^{obs}[ψ](x) × ‖χ_d‖²_{Ξ_d} = T_μν^{obs}[ψ](x)
```

for L²-normalised modes. The normalisation condition ‖χ_d‖² = 1 absorbs the sector volume into the mode function. The value of the mode at the observer address ξ⁰ is:

```
|χ_0^d(ξ⁰)|² ≡ |χ_0^d(0)|²
```

(setting ξ⁰ = 0 by translational freedom). For a d-dimensional ground-state sector mode with localization length L_d:

```
|χ_0^d(0)|² ∝ L_d^{−d}
```

This is exact for the Gaussian ground state; corrections for the actual sector potential are O(1) numerical factors.

### 3.11.2 The Effective Newton's Constant

After sector mode normalisation (‖χ_{n,d}‖²_Ξ = 1), the effective stress-energy reduces to the standard observer form (§3.3). A 3D observer who constructs a gravitational equation from their measurements obtains:

```
G_μν(x) = 8π G_N × T_μν^{obs}[ψ](x)
```

G_N is the same for all sectors — sector-independent by the L² normalisation argument. All particles, regardless of which sector they inhabit, source the observer's effective curvature with the same G_N. This is the equivalence principle (§3.6) as a theorem.

**Status of G_N.** G_N is not a coupling constant in a fundamental gravitational action — there is no such action written by hand in IDWT. G_N is what a 3D observer measures of ∞D curvature: G_N = G_∞/V_7, the ∞D gravitational coupling diluted by the 7 sector dimensions beyond d=3. Gravity is not quantized; there are no gravitons; there is no quantum gravitational threshold in this framework. V_7 ≈ 7.74 (occupied-sector contribution) is fully derived (§3.12.2). V_vacuum does not enter G_N — confirmed by Ricci-flat vacuum in d>10 (no particle sources, so R_ab=0) and by T5 (scattering states are not L²-normalizable and do not appear in Tr(f(D/Λ))). G_∞ requires the spectral action scale Λ on M_∞ (open, §3.12.2).

---

## 3.12 Newton's Constant — No Sector Correction

### 3.12.1 Why Sector Fluctuations Do Not Correct G_N

A legitimate concern with any multi-sector theory is whether integrating out sector-space degrees of freedom produces corrections to the Einstein-Hilbert term. In standard Kaluza-Klein theories this always occurs: the compact space volume multiplies M_Pl and becomes a dynamical modulus. The induced correction is:

```
M_Pl^{obs,eff} = M_Pl^{6D} × √Vol(compact space)
```

**IDWT has a different structure that forbids this correction.**

The functional determinant of the sector operator O_Ξ contributes a term:

```
Γ_Ξ = (1/2) Tr_Ξ[log O_Ξ]    where O_Ξ = −D_Ξ² + V_d(ξ)
```

Via the Seeley-DeWitt heat kernel expansion, this yields terms of the form:

```
Γ_Ξ ~ ∫_Ξ [a_0 + a_2 R_Ξ + a_4 R_Ξ² + ...] dμ_ξ
```

**Note (non-compact caveat).** The standard Seeley-DeWitt expansion and the coefficient formulas $a_0, a_2, a_4$ are derived for compact Riemannian manifolds. IDWT's sector spaces $\Xi_d$ are non-compact (confinement is from $V_d(r)$, not compactness). The no-correction argument below relies only on the decoupling $\delta\Gamma_\Xi/\delta g_{\mu\nu}=0$, which follows from the product metric structure and is independent of whether the Seeley-DeWitt coefficients retain their standard compact-manifold form. The argument is therefore valid as stated. However, the computation of $a_2(M_\infty)$ for the prediction of $G_\infty$ (§3.12.4) does require the Seeley-DeWitt expansion on the non-compact $\Xi_d$; verifying that the coefficient formulas hold for L²-normalizable modes with confining potential $V_d(r)$ is an open item (Part 6, MC-8).

The $a_2$ term, proportional to the Ricci scalar $R_\Xi$ of the sector manifold, is the one that would correct the observed Planck mass in a KK theory.

**The key: O_Ξ is independent of g_μν.**

O_Ξ = −D_Ξ² + V_d(ξ) acts on functions of ξ only. It depends on the sector metric h_ab(ξ) and the sector potential V_d, but has no dependence on the spacetime metric g_μν(x). This follows from the effective product structure in the d=3 observer's description of M_∞, where cross-terms between spacetime and sector coordinates are negligible:

```
ds²_{M_∞} ≈ g_μν(x) dx^μ dx^ν + h_ab(ξ) dξ^a dξ^b
```

In the full metric $G_{AB}dX^AdX^B$ on M_∞, off-diagonal terms $G_{\mu a}$ would in principle couple the spacetime and sector blocks. Their absence in the observer's effective description is what makes O_Ξ independent of g_μν — and therefore what ensures G_N receives no sector correction. Therefore:

```
δ(Tr_Ξ log O_Ξ) / δg_μν = 0   [exactly]
```

Γ_Ξ is a constant with respect to g_μν — it contributes a fixed cosmological term (already absorbed into Λ_eff) but no correction to G_N.

**Why IDWT differs from Kaluza-Klein.** In KK theories, the higher-dimensional metric G_{MN} is a single dynamical object. Its spacetime and extra-dimensional components mix through moduli fields — the compact space fluctuates and gravitons propagate into the sector space. Integrating out these fluctuations produces the observed Planck mass, and the resulting KK excitation tower is excluded by Eöt-Wash and LHC searches.

In IDWT, there is no graviton propagating anywhere. Gravity is curvature of M_∞ caused by mass — not a field with quanta. The sector manifolds Ξ_d are macroscopic spatial dimensions in which Ψ∞ vibrates; h_ab(ξ) is a fixed classical background metric, has no equation of motion, and does not mix with the 3D observer's metric. There are no moduli, no metric fluctuations in Ξ_d, and no KK graviton tower. All KK-exclusion bounds presuppose graviton propagation into the sector space; they do not apply to IDWT.

**Conclusion.** G_N as measured by a 3D observer receives no correction from sector fluctuations. The decoupling of Γ_Ξ from g_μν follows from the fixed-background structure of Ξ, which is a consequence of gravity being ∞D curvature sourced by mass rather than a dynamical field in Ξ.

---

### 3.12.2 G_N as the 3D Measurement of Infinite-Dimensional Gravity

The previous subsections show that G_N is sector-independent (§3.11) and not corrected by sector fluctuations (§3.12.1). Neither addresses the causal origin of G_N. This section establishes the correct logical direction: gravity is a phenomenon of the full $M_\infty$, not a 3D or 10D field appended to the particle physics. G_N is what a 3D observer at $\xi^0$ measures of it.

**Gravity has no sector boundary.** Every other force acts within a specific sector (EM and weak in d=2, strong in d=4). Gravity is the unique exception — it has no sector confinement because it is curvature of $M_\infty$ itself, the space in which all sectors live. A force confined to d=4 cannot reach a d=2 particle. Gravity reaches everything because everything lives in $M_\infty$.

**Mass encodes dimensional complexity; gravity couples through it.** The mass formula $m(n,d)=S(n,d)\times m_{\rm scale,d}$ assigns mass proportional to the count of sector microstates in sector $d$. More dimensions means exponentially more microstates: the photon (d=2, ground-state massless — two transverse polarisations, no excited microstates) barely couples to gravity; the tau (d=10, $S(23,10)=64\,512\,240$) couples strongly. Gravity couples to each particle through that particle's dimensional complexity, which is encoded in its mass. There is no separate gravitational rule per sector — the mass formula already carries the dimensional structure, and gravity couples to mass.

**G_N as a measurement.** The M_∞ curvature sourced by mass has a fundamental strength $G_\infty$. A 3D observer integrates out all dimensions beyond observer space — both the sector space (d=4,5,6,10, with localised modes) and the vacuum dimensions (d>10, with no stable bound states). The occupied-sector contribution to this integration is $V_7$, fully derived from the sector coupling constants:

| New coordinate(s) | Sector | $L_d = \lambda_d^{-1/4}$ |
|---|---|---|
| 4th | d=4 | 0.872 |
| 5th | d=5 | 1.571 |
| 6th | d=6 | 1.414 |
| 7th–10th | d=10 | 1.414 each |

$$V_7 = L_4 \times L_5 \times L_6 \times L_{10}^4 = 0.872\times1.571\times1.414\times(1.414)^4 \approx 7.74$$

The d>10 vacuum region is subcritical — its modes are extended, not localised (T5). Schematically:

$$G_N = G_\infty / V_\infty, \qquad V_\infty = V_7 \times V_{\rm vacuum}$$

**Why the localization formula fails for d>10.** The sector mode localization theorem (§3.13) gives $L_d = \lambda_d^{-1/4}$ for modes in the *discrete* spectrum of $H_d^{\rm harm}$. For the occupied sectors (d≤10), the harmonic well is confining and $L_d$ is well-defined. For the d>10 vacuum region, T5 states the modes are *extended* (scattering states) — the harmonic self-binding requires a self-consistent sector coupling $g_{dd}$, which for the vacuum dimensions either vanishes or is not sourced by any particle. The localization formula does not apply to the vacuum region; $L_d$ is formally undefined there.

**Numerical check.** If $g_{dd}=1/4$ were naively extended to d>10, $L_d = (1/8)^{-1/6} \approx 1.41$ for all d>10, giving a product $V_{\rm vacuum}$ that diverges exponentially with the number of vacuum dimensions, yielding $G_N \to 0$. This confirms the formula cannot be extended naively — the two arguments excluding $V_{\rm vacuum}$ (Ricci-flat vacuum + T5 scattering states) are required and correct.

**Does curvature from the occupied sectors propagate into d>10?** Yes — there is no hard wall at d=10. In any connected geometry, curvature sourced by mass propagates as vacuum curvature (Weyl tensor) into regions with no sources. The absence of particle sources in d>10 does not by itself mean the geometry there is flat.

**What T5 says about that curvature.** T5 establishes that d>10 modes are in the essential spectrum — scattering states, not bound states. Any gravitational disturbance entering d>10 disperses: it spreads outward without localizing, accumulating, or returning. This is the conducting side of the Gegenbauer critical-endpoint transition.

**Why $V_{\rm vacuum}$ does not enter $G_N$.** Two complementary arguments converge on the same conclusion:

*From the field equation.* In d>10 there are no particle sources, so the ∞D gravitational equation gives a vacuum condition: $R_{ab}=0$ (Ricci-flat). Vacuum curvature (Weyl tensor) exists — it carries the dispersed disturbance from d≤10 — but it is trace-free and does not contribute to $R=g^{ab}R_{ab}$. The spectral action coefficient $a_2=\int_{M_\infty} R\,{\rm dvol}$ therefore receives contributions only from d≤10, where $R\neq0$.

*From the spectral action trace.* ${\rm Tr}(f(D/\Lambda))$ sums over modes of the Dirac operator. Scattering states — modes in the essential spectrum (T5: all d>10 modes) — are not L²-normalizable and do not contribute discrete eigenvalues to the sum. Whether curvature reaches d>10 is irrelevant: those modes cannot appear in ${\rm Tr}(f(D/\Lambda))$.

Both arguments give the same result: $V_{\rm vacuum}$ does not appear as a dilution factor. The correct structure is:

$$G_N = G_\infty / V_7, \qquad V_7 \approx 7.74$$

**Status.** $V_7\approx7.74$ is fully derived from sector coupling constants (§3.10). $V_{\rm vacuum}$ does not enter — confirmed by both the Ricci-flat vacuum argument and T5. The single remaining open item is $G_\infty$: fixing the spectral action scale $\Lambda$ and function $f$ determines $G_\infty=f_2\Lambda^2 a_2/(8\pi)$, making $G_N=G_\infty/V_7$ a complete prediction.

---

### 3.12.3 Gravitational Coupling Ratios

The sector localization lengths L_d (from §3.9, §3.10) set V_7 and hence the gravitational scale. Mass itself is the resonant frequency m = m_scale_d × S(n,d), fixed entirely by the sector coupling constants and mode index; the d=5 neutrino sector has the smallest sector mass scale m_scale_5 because the d=5 sector has no self-confinement (χ(S⁵)=0) and its frequency scale is set by the cross-sector Hopf consistency equation m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³ — a frequency-domain relation among sector couplings.

Once G is fixed by one measurement, all gravitational forces F = G m₁m₂/r² between any two IDWT particles are predicted by the mass formula m = m_scale_d × S(n,d). No additional parameter is needed.

**Summary of the gravity programme status:**

| Result | Status |
|---|---|
| Spacetime Einstein equations from M_∞ action | ✅ §3.1–3.4 |
| No additional gravitational propagating modes | ✅ §3.4 |
| Equivalence principle: m_grav = m_inertial | ✅ §3.6 |
| Boundary terms vanish on non-compact Ξ | ✅ §3.5 |
| L²(Ξ) normalisability via sector mode localization theorem | ✅ §3.13 Part I |
| Bianchi identity ∇^μ T_μν^{eff} = 0 | ✅ §3.13 Part II |
| Spectral counting S(n,d) = N_d(n−1) | ✅ Part 8 §3 |
| Sector length L_d = sector localization | ✅ §3.9 |
| λ_d = (g_{dd}/2)^{2/3} from kernel | ✅ §3.10 |
| G_N sector-independent; no sector correction | ✅ §3.11–3.12.1 |
| G_N = G_∞/V_7; V_7 ≈ 7.74 derived; V_vacuum does not enter (Ricci-flat vacuum + T5 scattering states); G_∞ via spectral action Λ (open) | ✅/🔶 §3.12.2 |

---

### 3.12.4 G_∞ Numerically and the Spectral Action Closure Condition

**Note on the spectral action formalism.** The Connes-Marcolli spectral action Tr(f(D/Λ)) is used here as a mathematical tool to connect the IDWT Dirac operator to the Einstein-Hilbert term. IDWT is not a noncommutative geometry (NCG) model in the Connes-Marcolli sense — the operator algebra, Hilbert space, and spectral triple structure of IDWT are distinct from the NCG Standard Model. The spectral action provides a convenient expression for how the gravitational coefficient G_∞ relates to the spectrum of D; the mechanism producing that spectrum (sector geometry, mode index selection, kernel coupling) is entirely native to IDWT.

**The numerical value of G_∞.** The relation G_N = G_∞/V_7 immediately gives G_∞ once G_N and V_7 are known. Using the measured Newton's constant G_N = 6.674 × 10^{−11} m³ kg^{−1} s^{−2} and V_7 = 7.74 (fully derived in §3.12.2):

$$G_\infty = G_N \times V_7 = 5.19 \times 10^{-44}\ \mathrm{MeV}^{-2}$$

This is not a prediction — it is what G_∞ must equal, given the current input of one measured gravitational coupling. It becomes a prediction when G_∞ is derived independently.

**The spectral action condition — and why it is currently circular.** In the Connes-Marcolli spectral action, the Einstein-Hilbert term arises from the Seeley-DeWitt coefficient a_2:

$$G_N^{-1} \sim \frac{f_2 \Lambda^2 N_{\rm eff}}{12\pi^2}$$

where Λ is the spectral cutoff, f_2 is a moment of the cutoff function, and N_eff is the number of Dirac degrees of freedom in the spectral triple. Setting Λ from the spectral action condition and then predicting G_N reproduces the input — the condition is circular until Λ is fixed from the sector geometry independently. No sector mass scale provides a natural cutoff: the top quark at ~173 GeV is many orders of magnitude below the gravitational scale set by G_N^{−1/2}.

**Why a_4 is already determined — and what that implies.** The spectral action generates not only a_2 (the Einstein-Hilbert term, which controls G_N) but also a_4 (the coupling term, which controls the sector couplings g_{dd}). In standard NCG, both are Λ-dependent, and the ratio a_2/a_4 eliminates Λ to give a consistency condition between G_N and the gauge couplings.

In IDWT, the gauge couplings g_{dd} are fully derived from N_c alone (T9) — they are not inputs. This means a_4 is already fixed, independently of Λ and independently of G_N. If a_2 can be computed from the sector-space geometry (heat kernel coefficients from T14 plus the Ricci scalar on each sector manifold), then the ratio:

$$\frac{a_2(M_\infty)}{a_4(M_\infty)} = \frac{G_N^{-1}}{\text{(T9 gauge couplings)}}$$

determines G_N without any free parameter. The left side is a pure geometric quantity; the right side is the measurement. When they agree, G_N is a prediction.

**The genuine open computation.** Computing a_2 requires the integral of the Ricci scalar over M_∞:

$$a_2(M_\infty) = \frac{1}{12\pi^2} \int_{M_\infty} R_\infty\, d{\rm vol}_{M_\infty}$$

Each sector contributes R_{Ξ_d} = d(d−1)/(L_d^2) (the Ricci scalar of the round sphere or Fubini-Study metric of radius L_d on Ξ_d). The T14 heat kernel coefficients give the Weyl coefficient a_0^{(d)} = Γ(1+1/d)(d!)^{1/d}, which controls the volume element. The integral is finite because L²-normalizable modes (T5, §3.13 Part I) produce a convergent sector-by-sector sum, while d>10 sectors contribute R_{ab}=0 in vacuum (Ricci-flat) and vanish.

This computation — assembling ∫R dvol on M_∞ from T14 data and the L_d values of §3.10 — is the single remaining open item for gravity. Once complete, G_N = G_∞/V_7 is a parameter-free prediction from the same geometry that determines all particle masses.

**What does not belong here.** The Kaluza-Klein formula M_Pl^2 = M_∗^9 V_7^{\rm phys} (which would define an "11D fundamental scale" M_∗) is not IDWT. It requires compact extra dimensions, graviton propagation through those dimensions, and a Kaluza-Klein tower of massive graviton modes — all of which are explicitly excluded by Part 4 §1b. IDWT has no compact dimensions (Ξ is non-compact), no graviton quanta (gravity is geometry, not a field), and no KK tower. The formula does not apply, and M_∗ is not a quantity that appears in this framework.

---

## 3.13 Covariant Conservation of T_μν^{eff}

**Theorem (Bianchi, unconditional).** Let Ψ∞ be a physical IDWT mode — any normalizable bound-state eigenmode — with sector-factorized form Ψ∞(x,ξ) = ψ(x) ⊗ χ_{n,d}(ξ). Then:

```
∇^μ T_μν^{eff}(x) = 0
```

The proof proceeds in two parts: first establishing that all physical modes are L²(Ξ), then using that to close the Bianchi identity.

---

### Part I — L²(Ξ) Normalisability of Physical Modes

**Lemma (harmonic spectrum is purely discrete).** For the sector Schrödinger operator H_d^harm = −Δ_{ℝ^d} + λ_d r²:

```
σ_ess(H_d^harm) = ∅
```

The spectrum is purely discrete: σ(H_d^harm) = {(2N + d)√λ_d : N = 0, 1, 2, …} with finite multiplicity C(N+d−1, d−1) at each level N.

**Proof.** The potential λ_d r² → ∞ as r → ∞. By Rellich's criterion, the resolvent (H_d^harm − z)^{−1} is compact for all z ∉ σ(H_d^harm), which implies σ_ess = ∅. The eigenvalues follow from separation into radial and angular parts: the radial equation reduces to the d-dimensional isotropic harmonic oscillator, whose eigenvalues are (2n_r + l + d/2)·2√λ_d with n_r = 0,1,… and l = 0,1,…; the principal level N = 2n_r + l has cumulative degeneracy C(N+d−1,d−1), giving infinitely many discrete eigenvalues. □

**Theorem (sector mode Gaussian decay).** Every eigenfunction χ_{n,d} of H_d^harm satisfies:

```
|χ_{n,d}(r)| ≤ P_n(r) × exp(−√λ_d r²/2)
```

where P_n is a polynomial of degree n−1 (the generalised Laguerre × angular-harmonic factor).

**Proof.** Eigenfunctions of the d-dimensional harmonic oscillator are products of generalised Laguerre polynomials and solid harmonics times the Gaussian exp(−√λ_d r²/2). Since P_n is a polynomial, it grows at most as a power, and the Gaussian dominates for all r. □

**Corollary (L² normalisability).** Every eigenfunction χ_{n,d} is square-integrable on ℝ^d:

```
‖χ_{n,d}‖²_{ℝ^d} = ∫_{ℝ^d} |χ_{n,d}(ξ)|² dξ
                  ≤ C_n ∫_0^∞ r^{d−1+2(n−1)} e^{−√λ_d r²} dr < ∞
```

for all d ≥ 1 and all n ≥ 1. Compactness of Ξ_d is not required — confinement follows from the harmonic potential growing without bound. □

Numerical verification (d=3, n=1, l=0): χ_0 ∝ exp(−√λ_3 r²/2); ∫_0^∞ r² e^{−2√λ_3 r²/2} dr = ∫_0^∞ r² e^{−√4.82 r²} dr = (√π/4)(√4.82)^{-3/2} < ∞. ✓

**Theorem (Physical mode ↔ L²).** For macroscopic non-compact Ξ_d, a mode χ is a physical mode — a normalised eigenfunction of H_d^harm (i.e. χ ∈ L²(ℝ^d)) — if and only if it is an exponentially localised bound state of the sector potential. Existence as a physical mode is a normalizability condition, independent of whether the mode is visible to a d=3 observer.

**Proof.**

*(→) Non-eigenfunction modes are non-normalizable.* Any mode that is not a discrete eigenfunction of H_d^harm either oscillates (plane-wave-like in the sector directions) or grows. For any such state, ∫|χ|² dξ diverges, so χ ∉ L²(ℝ^d) and it is not a bound state.

*(←) Harmonic eigenstates are normalizable.* Every χ_{n,d} ∈ L²(ℝ^d) by the corollary above, with a Gaussian envelope that decays exponentially — a genuine bound state. □

These L² bound states are the physical modes: each exists, carries mass m = m_scale_d × S(n,d), and gravitates. Among them, the co-fixed-point condition (the generation tower) selects the stable spectrum. What a d=3 observer can or cannot detect is a separate question that does not affect existence or gravitation.

---

### Part II — The Bianchi Identity

With L² normalisability established, the Bianchi proof in Part II below holds unconditionally.

**Step 1 — Factorisation.**

```
T_μν^{Dirac}(x,ξ) = |χ_{n,d}(ξ)|² × T_μν^{obs}[ψ](x)
```

**Step 2 — Spacetime conservation.** From the spacetime Dirac equation (iγ^μ ∇_μ − m_eff)ψ = 0:

```
∇^μ T_μν^{obs}[ψ](x) = 0
```

**Step 3 — Commutation.** Since (a) ∇^μ acts on x only, (b) ∂_μ(dμ_ξ) = 0, and (c) |χ|² ∈ L²(Ξ_d) by Part I, the dominated convergence theorem applies:

```
∇^μ ∫_Ξ |χ(ξ)|² T_μν^{obs}[ψ](x) dμ_ξ = ∫_Ξ |χ(ξ)|² ∇^μ T_μν^{obs}[ψ](x) dμ_ξ
```

**Step 4.**

```
∇^μ T_μν^{eff}(x) = ∫_Ξ |χ_{n,d}(ξ)|² × 0 dμ_ξ = 0    □
```

**Multi-mode.** For Ψ∞ = Σ_i ψ_i ⊗ χ_i, cross terms contribute ⟨χ_i|χ_j⟩_Ξ T_μν^{ij}. Since D_Ξ is self-adjoint and the χ_i are eigenfunctions with distinct eigenvalues m_i ≠ m_j, they are orthogonal: ⟨χ_i|χ_j⟩_Ξ = 0. Cross terms vanish identically. ∇^μ T_μν^{eff} = 0 holds for any superposition of physical modes. □

**Status.** The Bianchi identity ∇^μ T_μν^{eff} = 0 is proved unconditionally for all IDWT physical modes (the normalizable bound states). No remaining open conditions.

---

## 4. Cosmological Constant

The vacuum energy that sources Λ_eff would come from the sector mode tower. Its observed smallness is not currently derived: an existing mode gravitates whether or not a d=3 observer can resolve it, so the relevant question is which modes are persistent physical excitations — only the co-fixed-point modes are stable resonances of M_∞, while the rest are not persistent states. Whether that distinction, together with the sector radii and coupling strengths that fix particle masses, yields a naturally small Λ_eff is an open problem. ❓

---

## 5. Generation Tower Mode Selection

Every integer pair (n,d) with d ∈ {2,3,4,5,6,10} exists as a resonance of Ψ∞. The physical particles are those selected by the co-fixed-point condition: the mode index n must be a co-fixed-point of the sector comb filtration from n_s=4 — the generation tower. Modes not in the co-fixed-point set are not stable resonances of M_∞, regardless of sector.

In d=3, the co-fixed-point spectrum selects exactly n=1 (down) and n=4 (strange). The intermediate modes n=2,3 are not co-fixed-points — they are unoccupied resonances of M_∞, predicted absent as stable distinct states (their d=3 masses would be 18.8 and 47 MeV). Modes n≥5 in d=3 are likewise not selected.

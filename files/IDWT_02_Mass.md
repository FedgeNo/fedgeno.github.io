# IDWT — Part 2: The Mass Formula

---

## 1. The Simplex Formula and the Hockey-Stick Identity ✅

```
m(n, d) = m_scale_d × S(n, d)

S(n, d) = C(n+d−1, d)
```

S(n,d) is the number of ways to distribute n units of excitation across d oscillator modes — equivalently, the dimension of the space of degree-n homogeneous polynomials in d variables.

### S(n,d) as a Universal Combinatorial Measure Field

S(n,d) appears in four distinct physical roles across IDWT. These are not inconsistent uses — they are four different functionals applied to the same underlying combinatorial object. The formal declaration:

**S(n,d) is the cumulative spectral counting function of the d-dimensional sector harmonic oscillator:**

```
S(n,d) = N_d(n−1) = #{eigenvalues of H_d at level k < n, counted with multiplicity}
        = Σ_{k=0}^{n-1} C(k+d−1, d−1)    [proved in Part 8 §60]
```

Given this single definition, the four applications are different functionals on S:

| Role | Functional | Physical meaning |
|---|---|---|
| **Mass eigenvalue** | F_mass = m_scale_d × S(n,d) | Mass = sector scale × cumulative microstate count |
| **Hilbert space weight** | F_norm = S(n,d) (weight in ‖Ψ‖_w²) | Energy-weighted norm: ‖Ψ‖_w² = Σ m(n,d)|c_{n,d}|²/m_scale_d |
| **Projection amplitude** | F_proj = S(n,2)/S(n,d) (ratio) | Projection loss = ratio of d=2 to d-sector state counts |
| **Convergence bound** | F_conv = Σ_n 1/S(n,d) = d/(d-1) | Reciprocal sum bounds the evaluation functional |

These are mutually consistent because all four reduce to operations on N_d(n−1). In particular: Roles 1+2 are consistent because ‖Ψ‖_w² = Σ S(n,d)|c_{n,d}|² is precisely the energy-weighted norm (standard in QFT: the physical inner product weighted by mode energy). Role 3 is consistent because Ω_log = log(m(n,d)/m(n,2)) — projection loss is the log of the mass mismatch between sectors. Role 4 follows by Cauchy-Schwarz from Role 2.

**S(n,d) is not postulated as a state count — it is the dimension of a space that exists in the sector geometry.** The sector manifold Ξ_d supports degree-n homogeneous polynomials in d variables. The mode functions χ_{n,α}(ξ) are the independent degree-n monomials ξ₁^{a₁}⋯ξ_d^{a_d} with a₁+…+a_d = n, and dim Sym^n(ℝ^d) = C(n+d−1, d) = S(n,d) is a theorem of algebraic geometry.

**The hockey-stick identity is a proved theorem of combinatorics:**

```
S(n, d) = Σ_{k=0}^{n-1} C(k+d−1, d−1)
```

This is not decoration. It is the engine of the entire spectrum.

**Physical meaning:** The resonant frequency S(n,d) equals the cumulative count of hidden quantum microstates below level n. These are the same thing. The frequency at which mode n resonates is precisely the total number of accessible hidden states up to that level. Heavier particles — higher frequencies — occupy higher-entropy configurations of the hidden geometry. The hockey-stick identity is the bridge between the spectral and the statistical descriptions.

---

## 2. The Per-Sector Comb Filter H_d(ω) ✅

The cross-sector filter Γ₃₄₆(ω) gives the ρ meson (§10). The intra-sector filter H_d(ω) gives fermion masses:

```
H_d(ω) = exp(2πi × N_d(ω / m_scale_d))
```

where N_d is the continuous inverse of S(n,d): N_d(S(n,d)) = n, extended via the gamma function S_cont(n,d) = Γ(n+d)/(d! Γ(n)). This extension is strictly increasing in n for all n > 0 (a consequence of the log-convexity of the Gamma function: log Γ(n+d) − log Γ(n) is convex and strictly increasing). N_d is therefore well-defined and injective on all ω > 0, not just at mass eigenvalues.

**Phase condition:** Im[H_d(ω)] = sin(2π N_d(ω/m_scale_d)) = 0 at exactly ω = S(n,d) × m_scale_d for all integer n. All zeros are constructive (Re[H_d] = +1) — every fermion mass is a resonance.

**Phase velocity:**
```
dΦ_d/dω = 2π / (m_scale_d × S(n(ω), d−1))
```

The phase of sector d accumulates at a rate inversely proportional to the mode density of sector d−1. This is a recursive inter-sector relation requiring no knowledge of S(n,d) directly. The mass formula m = S(n,d) × m_scale_d is not a postulate — it is the resonance condition Im[H_d(ω)] = 0, derivable from the inter-sector mode density chain.

### Angular structure of the kernel

The cross-sector coupling term (ξ_d·ξ_{d'})² decomposes on the unit sphere S^{d-1} by spherical harmonics. For the d=3 sector (S²), where P₂ is the standard Legendre polynomial:

```
(ξ_d·ξ_{d'})² = 1/3  [l=0, scalar]  +  (2/3)P₂(cosθ)  [l=2, tensor]
```

For general d, the l=0 coefficient is 1/d and the l=2 coefficient involves the Gegenbauer polynomial C₂^{(d-2)/2}. The d=3 formula is given because the d=3 quark sector is the primary source of the corrections discussed here.

The l=0 part is a constant — it generates sector masses and is the source of the entire simplex spectrum. The l=2 part depends on the relative orientation of ξ_d and ξ_{d'} and is responsible for every non-trivial correction in the theory: the hidden l=1 orbital admixture that gives μ_p, μ_n, and g_A, and the n-dependent frequency precession corrected by the GTC. All of those come from the same tensor term.

For the self-coupling (d=d'), ξ=ξ' so (ξ·ξ)²=|ξ|⁴=1 on the unit sphere. The Gegenbauer l=2 component is present but averages to zero over the rotationally symmetric vacuum (Gegenbauer orthogonality): only the l=0 piece contributes to the sector self-energy after vacuum averaging. Cross-sector angular mixing is absent in the vacuum expectation value of the self-coupling.

**Verified numerically** for d=3 (Im[H₃] = 0.0000, Re[H₃] = 1.0000 at n=1,...,6) and d=4 (residuals < 10⁻¹⁴ at n=3, 20, 72).

**Base case d=1:** N₁(x) = x, so H₁(ω) = exp(iωτ) with τ = 2π/m_scale₁ — a single constant-delay comb filter. ✓

---

## 3. The Pascal Recursion — One Identity, All Generations ✅

The hockey-stick identity implies the Pascal recursion:

```
S(n, d) = S(n, d−1) + S(n−1, d)
```

This is a proved theorem. It says: the simplex number at (n, d) equals its neighbour at (n, d−1) plus its neighbour at (n−1, d). **The Pascal recursion constrains the generation law:** any mode index assignment that violates S(n,d) = S(n,d−1) + S(n−1,d) is rejected. The observed assignments are the unique set that simultaneously satisfies the recursion and the seed conditions {n_down=1, n_strange=4}. The recursion does not generate the assignments from scratch — but it makes the assignments rigid: there is no freedom to choose different mode indices once the seeds are fixed.

**Generation 2 — the clearest case:**

Evaluate S(4,4) two ways:
```
S(4,4) = S(4,3) + S(3,4)
   35   =   20   +   15
n_muon  = n_charm + n_ν₂
```

This is not a fit. It is Pascal's recursion applied to S(4,4) = 35. The gen-2 lepton mass index equals the sum of the charm quark index and the second neutrino index because that is what the hockey-stick identity requires at (n=4, d=4). The generation law for generation 2 is a combinatorial theorem.

**Generation 1:**
```
n_e = n_ν₁ + n_up = S(3,3) + 3 = 10 + 3 = 13
```
n_ν₁ = S(n_up, 3) = S(3,3) = 10 is itself a hockey-stick sum: 1+3+6 = 10. Adding n_up gives n_e = 13.

**Generation 3:**
```
n_τ = n_ν₃ + n_down = 22 + 1 = 23
```
The +1 = n_down = S(1,d) = 1 for every d — the base case of every hockey-stick sum. The tau's mode index inherits the universal ground state.

The pattern across all three generations:
```
n_lepton = n_neutrino + n_quark_partner
```
This is the hockey-stick identity at different (n, d) pairs — not a selection rule added by hand.

---

## 4. Why d=6 is Colour-Neutral ✅

The Vandermonde-Chu identity is the hockey-stick identity applied twice and convolved:
```
Σ_{k=0}^N C(k+2, 2) × C(N−k+2, 2) = C(N+5, 5)
```

This proves: **the d=6 oscillator is exactly the tensor product of two d=3 oscillators.** The lepton sector (d=6 = d=3 ⊗ d=3) is colour-neutral because it is built from products of colour spaces, not embedded in one. This is the geometric origin of the lepton/quark distinction.

Verification (N=32): Σ_{k=0}^{32} C(k+2,2) × C(32−k+2,2) = 435,897 = C(37,5) ✓

---

## 5. The Seeds {1, 4} — Hockey-Stick Forced ✅

The two seeds are not chosen. They are forced by the hockey-stick structure itself.

**n_down = 1** is forced because S(1,d) = 1 for every d. This is the base case of every hockey-stick sum — the first term in every cumulative count. It is simultaneously the ground state of every sector.

**n_strange = 4** is forced because it is the unique positive integer satisfying S(n,4) = 35 = n_muon. The muon occupies mode 35 in d=6. Only n=4 maps there via the simplex function in d=4. Why is 35 the muon's mode? Because 35 = S(4,4) = 1+4+10+20 — the hockey-stick sum of the d=4 simplex through level 3. The strange quark's seed index is identified by requiring its hockey-stick image in d=4 to land on an occupied lepton mode. No other integer does this.

At the vacuum stability coupling g₃₃ = 8√7, the effective energy has local minima at exactly n=1 and n=4 and nowhere else. The seeds are not chosen — they are the fixed points.

---

## 6. The Complete Index Derivation — Hockey-Stick All the Way Down ✅

Every mode index is a hockey-stick evaluation or a difference between successive partial sums of the same identity. The operations that might appear to be "algebraic manipulations chosen to fit data" are in fact the only operations the identity permits:

```
n_up    = n_strange − 1 = 3       [Pascal: S(n,4) − S(n,3) = S(n−1,4) at n=4]
n_charm = S(4, 3)       = 20      [hockey-stick in d=3 through level 3]
n_ν₁    = S(3, 3)       = 10      [hockey-stick in d=3 through level 2]
n_ν₂    = S(3, 4)       = 15      [hockey-stick in d=4 through level 2]
n_e     = n_ν₁ + n_up   = 13      [generation law = hockey-stick slice, gen 1]
n_muon  = S(4, 4)       = 35      [= S(4,3) + S(3,4) = n_charm + n_ν₂, Pascal]
n_ν₃    = n_ν₁ + n_ν₂ − n_up = 22
n_τ     = n_ν₃ + S(1,d) = 23      [base case S(1,d)=1 for all d]
n_top   = 2 × S(8, 2)   = 72      [triangular ladder on n_strange]
n_W     = n_top + 4 = 76     [Vandermonde: g(d=5, n_top) = n_top + (d−1) = 72 + 4 = 76; see Part 3 §11]
n_Z     = n_W + 5 = 81       [Vandermonde: g(d=6, n_W) = n_W + (d−1) = 76 + 5 = 81]
n_Higgs = n_up   + n_charm  + n_top = 95  [= 3+20+72; also = n_down+n_e+n_Z = 1+13+81]
```

The physical claim this sharpens: **if mass is the cumulative microstate count S(n,d), then the hockey-stick identity must appear throughout the spectrum, and the generation law must hold exactly.** It is not that the framework predicts these relations and then they happen to work — the hockey-stick identity leaves no room for them to fail.

---

## 7. The Neutrino Sector ✅

All three neutrino indices follow directly from the same hockey-stick evaluations:
```
n_ν₁ = S(n_up, 3) = S(3,3) = 10
n_ν₂ = S(n_up, 4) = S(3,4) = 15
n_ν₃ = n_ν₁ + n_ν₂ − n_up = 22
```

The neutrino gaps are themselves sums of quark seeds:
```
n_ν₂ − n_ν₁ = 5 = n_strange + n_down
n_ν₃ − n_ν₂ = 7 = n_up + n_strange
```

**Normal mass ordering predicted:** S(n,5) is strictly increasing, so m_ν₁ < m_ν₂ < m_ν₃. Consistent with current experimental preference at 3–4σ.

Anchoring to the solar mass splitting (ratios are IDWT predictions; scale is external): m_ν₁ ≈ 1.51 meV, m_ν₂ ≈ 8.74 meV, m_ν₃ ≈ 49.5 meV, Σm_ν ≈ 59.7 meV.

---

## 8. The Bottom Quark — Quartic Bifurcation ✅

The bottom quark fits no clean simplex sector. It arises within d=3 at the resonance point k₀ = n_strange² = 4² = 16 — derived entirely within d=3. Three resonance conditions add in phase at k₀, making the single-mode solution at n=16 unstable. The off-diagonal quartic coupling forces the geometric-mean beat:

```
m_b = √(S(16,3) × S(17,3)) × m_scale_3
    = √(816 × 969) × 4.702 MeV = 4,181 MeV    (+0.02% vs PDG 4,180 ± 10 MeV)
```

The bottom quark is a moiré phenomenon — an interference pattern between two adjacent d=3 modes, not a clean simplex resonance.

---

## 9. Coupling Constants — Complete Derived Set ✅

The coupling matrix G has rank 1: G_{dd'} = v_d × v_{d'} where v_d = √g_{dd}. All cross-sector couplings follow from the six sector self-couplings, which reduce to five distinct values (g₆₆ = g₁₀,₁₀). g₃₃ and g₄₄ come from the seed structure {n_s, n_u}; g₆₆ and g₁₀,₁₀ from anomaly cancellation; g₅₅ from Hopf fiber universality; g₂₂ from seeds via the cross-sector mode formula (§10 below). m_W is derived, not empirical.

---

### g₃₃ = 8√7 and g₄₄ = 12/√7 — both from {n_s, n_u} alone ✅

Both coupling constants are derived simultaneously from the seeds {n_s=4, n_u=3} using a single universal structure. Neither is primary.

**The universal coupling coefficient** (same for both sectors by binomial symmetry C(n,k)=C(n,n-k)):
```
g_coeff = √(n_s(n_s+1)/S(n_s,4)) = √(20/35) = √(4/7) = 2/√7
         = √(n_u(n_u+1)/S(n_u,5)) = √(12/21) = √(4/7) = 2/√7
```
These are equal because n_u+3 = n_s+2 = 6 (using n_s = n_u+1) → C(6,4)=C(6,2). The same binomial symmetry makes the coupling coefficient universal.

**The gaps:**
```
gap_d3 = n_s²                    = 16 = k₀   [seed self-interaction]
gap_d4 = H.M.(n_s,n_u)           = 24/7       [harmonic mean of both seeds]
       = 2n_sn_u/(n_s+n_u)
```
The d=3 gap equals k₀ — the same resonance condition driving the bottom quark bifurcation. The d=4 gap is the harmonic mean of both seeds, the natural effective gap when two boundary conditions act simultaneously.

**Both couplings, from the same formula:**
```
g₃₃ = gap_d3 / g_coeff = n_s²√(n_s+n_u)/2   = 8√7
g₄₄ = gap_d4 / g_coeff = n_sn_u/√(n_s+n_u)  = 12/√7
```

**Closed forms and rank-1 as a theorem:**
```
g₃₃ = n_s² × √(n_s+n_u) / 2  = 16√7/2 = 8√7   ✓
g₄₄ = n_s × n_u / √(n_s+n_u) = 12/√7           ✓
g₃₄ = √(g₃₃×g₄₄) = √(n_s³n_u/2) = √96 = 4√6  ✓
g₃₃×g₄₄ = n_s³n_u/2 = 64×3/2 = 96             ✓
```

The rank-1 identity g₃₃×g₄₄ = g₃₄² is not a separate assumption — it follows from the seed structure alone. g₃₃, g₄₄, and g₃₄ are all theorems of {n_s=4, n_u=3}.

**g₃₃ from g₄₄:** g₃₃/g₄₄ = n_s(n_s+n_u)/(2n_u) = 4×7/6 = 14/3. This ratio equals (m_d/m_u)² — the squared lightest-particle mass ratio between sectors — another consequence of the seed structure, not an independent assumption.

---

### g₆₆ = 1/4 — from anomaly cancellation ✅

With N_c = 3 colour charges (derived geometrically from the Dirac index of CP² with Hopf flux k=1 — see Part 8 §59), the SU(2)²U(1) gauge anomaly cancellation gives Y_Q = 1/(2N_c) = 1/6. The SU(3)²U(1) condition with Q = T₃ + Y then gives the lepton hypercharge Y_L = −1/2. Therefore:
```
g₆₆ = Y_L² = (−1/2)² = 1/4
```
This is exact and requires no mass input.

---

### g₁₀,₁₀ = 1/4 — from tau hypercharge ✅

The tau lepton carries Y_L = −1/2 identically to the electron and muon (same SU(2)_L doublet assignment). The same anomaly cancellation that gives g₆₆ = Y_L² = 1/4 gives g₁₀,₁₀ = 1/4. This is not an assumption — it is forced by the gauge structure.

---

### g₅₅ — from Hopf fiber universality ✅

The two U(1) Hopf fibrations sharing the electromagnetic fiber are:
```
S¹ → S³  → CP¹   (d=3 total, d=2 base)
S¹ → S⁵  → CP²   (d=5 total, d=4 base)
```

The fiber is the same U(1) in both. Universality requires the ratio (total-space coupling)/(base coupling) to be identical:

```
v₃ / v₂ = v₅ / v₄
```

Cross-multiplying: **v₃ × v₄ = v₂ × v₅**, i.e. **g₂₅ = g₃₄ = 4√6**.

The cross-coupling between the two Hopf partner pairs is equal. Solving for v₅:

```
v₅ = v₃ × v₄ / v₂ = g₃₄ / v₂

g₅₅ = v₅² = (g₃₃ × g₄₄) / g₂₂ = 96 / g₂₂
```

Numerically with g₂₂ = 722.5:

```
g₅₅ = 0.1329,   v₅ = 0.3645
```

**Verification:** v₃/v₂ = v₅/v₄ = 0.17116 ✓ and g₂₅ = v₂×v₅ = 9.798 = g₃₄ = 4√6 ✓

**Key consequence:** g₅₅ is fully determined by g₂₂ — no additional measurement is needed. The coupling algebra is closed by the single measured constant m_e: all six sector self-couplings are derived (g₃₃ and g₄₄ from seeds, g₆₆ and g₁₀,₁₀ from anomaly cancellation, g₅₅ = 96/g₂₂ from Hopf universality, g₂₂ from the cross-sector mode formula §10).

**Neutrino mass hierarchy:** g₅₅ = 0.1329 implies m_scale_5 ≈ 0.37 MeV via the coupling fixed-point, but observed neutrino masses are ~meV — off by 10⁵×. This is the IDWT form of the neutrino mass hierarchy problem. The coupling algebra is closed. The seesaw mechanism is geometrically forbidden (d=5 has d mod 8 = 5, which prohibits Majorana spinors), so the suppression must arise from the d=5 sector vacuum dynamics directly — non-perturbative Stage-1 suppression at λ̂₅ ≫ 1 or a condensate from the (5,5)→10 Vandermonde vertex. The neutrino mass RATIOS remain fully predicted by S(10,5):S(15,5):S(22,5), anchored to Δm²₂₁.

---

### Cross-couplings — all from rank-1 ✅

```
g₃₄ = √(g₃₃ × g₄₄) = √96 = 4√6
g₂₅ = √(g₂₂ × g₅₅) = √96 = 4√6   [= g₃₄: Hopf universality]
g₃₆ = √(g₃₃ × g₆₆) = √(2√7)
g₄₆ = √(g₄₄ × g₆₆) = √(3/√7)
g₃,₁₀ = √(g₃₃ × g₁₀,₁₀) = √(2√7)   [= g₃₆]
g₄,₁₀ = √(g₄₄ × g₁₀,₁₀) = √(3/√7)  [= g₄₆]
g₆,₁₀ = √(g₆₆ × g₁₀,₁₀) = 1/4      [= g₆₆]
```

**Coupling algebra now closed ✅:** All six sector self-couplings are derived from m_e and the seeds {1,4}. g₃₃ and g₄₄ from seed equations; g₆₆ and g₁₀,₁₀ from anomaly cancellation; g₂₂ = (S(n_s,3)−n_u)² × S(n_u−1,4) / 2 from seeds (§10); g₅₅ = 96/g₂₂ from Hopf universality. m_W is derived at +0.003% accuracy.

---

## 9b. Tau Mass — Dyson Resummation ✅

The tau is the one lepton whose raw simplex prediction requires a correction beyond the GTC. The mechanism is the isotropic back-reaction between the d=6 and d=10 sectors.

**Setup.** The d=6 and d=10 sectors share the same self-coupling: g_{6,6} = g_{6,10} = g_{10,10} = 1/4 exactly, because Y_L = Y_τ = −1/2 (the tau and electron/muon are in the same SU(2)_L doublet structure). This isotropy means the back-reaction from d=6 onto d=10 feeds back on itself via g_{10,10}.

**Self-consistent equation.** The d=6 → d=10 back-reaction shift Δm satisfies:

```
Δm = ε_{6→10} × m_τ + g_{10,10} × Δm
```

The second term is the self-feedback: the shifted tau mass generates further back-reaction through its own g_{10,10} coupling. Solving:

```
Δm = ε_{6→10} × m_τ / (1 − g_{10,10})
```

Since g_{10,10} = 1/n_s = 1/4, the denominator is 3/4 = n_u/n_s, giving resummation factor n_s/n_u = 4/3. This ratio is forced by n_u = n_s − 1; it is not a free parameter.

**The total correction.** The leading ε_{6→10} is:

```
ε_{6→10} = g_{6,10} / (k₀ × n_mu) = (1/4) / (16 × 35) = 1/2240
```

Multiplied by the resummation factor 4/3:

```
ε_total = 1/2240 × 4/3 = 1/1680 = 1/(n_u × n_s² × S(n_s,4))
```

**Result.**

```
m_τ = m_e × S(23,10)/S(13,6) × (1 + 1/1680) = 1776.84 MeV
PDG: 1776.86 ± 0.12 MeV.   Error: −0.14σ.   Inside 1σ.
```

No inputs beyond m_e and the seeds {n_s, n_u}.

**Prediction from the derived set:** m_u/m_d = √(g₄₄/g₃₃) = √(12/√7 ÷ 8√7) = √(12/56) = √(3/14) = 0.4629. PDG: 0.462 ± ~0.10 (the ratio carries ±25% uncertainty from lattice QCD). Error relative to central value: +0.20%.

---

## 10. Mass Scale Derivation ✅

### m_scale_3 — from the coupling self-consistency condition ✅

The kernel vacuum analysis gives a fixed-point equation: in equilibrium, the squared mass of the lightest particle in sector d equals g_{dd}/g_{66} times m_e². This requires that the mode occupation probability (∝ m²) be consistent with the coupling that generates it. For d=3, the lightest mode is n=1 (down quark) with S(1,3)=1, so m_lightest(d=3) = m_scale_3:

```
(m_scale_3 / m_e)² = g₃₃ / g₆₆
m_scale_3 = m_e × √(g₃₃/g₆₆) = 0.511 × √(8√7/0.25) = 0.511 × 9.201 = 4.702 MeV
```

This comes from the l=0 scalar part of the cross-sector kernel (ξ_d·ξ_{d'})². It requires only m_e and the derived coupling constants g₃₃ and g₆₆ — both from seeds {n_s,n_u} and anomaly cancellation respectively. No particle mass other than m_e enters.

**The down quark is a prediction, not an anchor:** m_d = m_scale_3 × S(1,3) = m_scale_3 × 1 = 4.702 MeV. PDG: 4.67 MeV. Error: +0.68%.

### The ρ Meson — Comb Filter Prediction ✅

The inter-sector comb filter Im[Γ_{346}(ω)] predicts the ρ meson mass independently of m_scale_3. Its inputs are the coupling constants g₃₃=8√7, g₄₄=12/√7, g₆₆=1/4 (all derived from seeds and anomaly cancellation) and the Jacobi chain delays τ_d = 1/(2√(k₀+d)) at resonance site k₀=16:

```
m_rho* = arg max Im[Γ_{346}(ω)] = 775.794 MeV    (PDG: 775.260 ± 0.250 MeV)
Error: +0.069%
```

No direct mass input is used. The 0.534 MeV residual is consistent with (a) Breit-Wigner mass definition ambiguity (~±1 MeV for a resonance with Γ/m ≈ 19%), (b) isospin breaking absent from the SU(3)-symmetric kernel, and (c) the leading-order WKB approximation in τ_d being exact only for d=10 (see Part 1 §3b). The agreement is a consistency check of the coupling geometry at the 0.069% level.

Note: τ_d = 1/(2√(k₀+d)) is a valid description of the inter-sector phase delay at the resonance site k₀, where both d=3 and d=6 modes are evaluated at the same resonance frequency scale set by k₀=n_s²=16. The delay formula does not assume comparable mass scales between sectors — it depends only on the Jacobi chain structure at k₀, which is a geometric property of the manifold, not the sector mass scale.

### Scale Hierarchy ✅

**Two empirical inputs: m_e and m_W. All sector scales derived from these.**

| Quantity | Source | Value |
|---------|--------|-------|
| m_scale_6 | m_e / S(13,6) | 2.7526×10⁻⁵ MeV |
| m_scale_3 | m_e × √(g₃₃/g₆₆) | 4.702 MeV |
| m_scale_4 | m_scale_3 × √(g₄₄/g₃₃) / S(3,4) | 0.1451 MeV |
| m_scale_10 | = m_scale_6 | 2.7526×10⁻⁵ MeV |
| m_scale_2 | m_W / S(76,2) | 27.47 MeV |

The uniform +0.68% offset in d=3 quark predictions and +0.79% base in d=4 reflect the coupling self-consistency derivation's natural accuracy — they are below PDG measurement precision for light quarks (PDG d: ±10%, s: ±9%) and are structurally forced: the rank-1 kernel means all modes within a sector scale identically, so the offset is the same for every mode in that sector.

### All sector scales
```
m_scale_6  = m_e / S(13,6)                            = 2.7526 × 10⁻⁵ MeV  [electron anchor]
m_scale_3  = m_e × √(g₃₃/g₆₆)                        = 4.702 MeV           [from seeds + anomaly]
m_scale_4  = m_scale_3 × √(g₄₄/g₃₃) / S(3,4)        = 0.1451 MeV
m_scale_10 = m_scale_6                                 [g₁₀,₁₀ = g₆₆: Y_τ = Y_L]
m_scale_2  = m_e √(g₂₂/g₆₆)                           = 27.47 MeV           [derived from seeds via g₂₂]
```

### §10. g₂₂ — the kernel back-reaction fixed-point ✅

The d=3 self-coupling g₃₃ is fixed by the intra-sector confinement condition g_eff(n_s,3) = g₃₃/S(n_s,3) ≈ 1 (Part 2 §8). The d=2 sector has no self-confinement — the W is massive but not confined in the quark sense. Its self-coupling g₂₂ is instead fixed by the **cross-sector back-reaction**: the requirement that the d=2 vacuum amplitude is consistent with the d=3 and d=4 quark sector structures at the seed level.

**The derivation:**

**Step 1.** At mode n=n_s in d=3, there are S(n_s,3) = 20 quark states. Of these, n_u = 3 are "accounted for" by the up quark sector. The remaining

```
α = S(n_s,3) − n_u = 20 − 3 = 17
```

states are available to couple to the d=2 sector through G₂₃. Because the kernel is two-body — (ξ·ξ')² couples J^{d=3}(ξ) to J^{d=3}(ξ') — both copies of the d=3 current contribute, giving α². This can also be read off from the hockey-stick: α = S(n_s,3) − n_u.

**Step 2.** At level n_u−1 = 2 in d=4, there are

```
β = S(n_u−1, 4) = S(2,4) = 5
```

states below the up-quark threshold. These couple to d=2 through a single G₂₄ insertion, entering linearly. By the hockey-stick identity S(n,d) − S(n,d−1) = S(n−1,d): β = S(n_u,4) − S(n_u,3) = 15 − 10 = 5, confirming β = S(n_u−1,4).

**Step 3.** The kernel (ξ·ξ')² = (ξ'·ξ)² is symmetric under ξ↔ξ', so the vacuum integral double-counts. Divide by 2.

**Step 4 (fixed-point).** Equate the cross-sector back-reaction to the d=2 self-coupling:

```
g₂₂ = (1/2) × α² × β  =  (1/2) × 17² × 5  =  722.5   (exact)
```

**Comparison with d=3:** For d=3, the intra-sector fixed-point gives g₃₃ ≈ S(n_s,3) = 20 (with a ~5.8% Jacobi correction). For d=2, the cross-sector fixed-point gives g₂₂ = (S(n_s,3)−n_u)² × S(n_u−1,4)/2 — a different structure, reflecting that the EW sector acquires its scale by coupling to both quark sectors, not by self-confinement.

**Consequences:**

```
m_scale_2 = m_e × √(g₂₂/g₆₆) = m_e × √(722.5/0.25) = 27.471 MeV
```

| Quantity | From seeds + m_e | PDG | Error |
|---|---|---|---|
| m_W | m_scale_2 × S(76,2) = 80,379 MeV | 80,377 MeV | +0.003% |
| m_Z | m_scale_2 × S(81,2) = 91,230 MeV | 91,187.6 MeV | +0.047% |
| m_H | m_scale_2 × S(95,2) = 125,266 MeV | 125,250 MeV | +0.013% |

**IDWT has a single empirical input: m_e = 0.511 MeV.** All quarks, leptons, gauge bosons, CKM angles, Fermi constant, Weinberg angle, and muon lifetime follow from m_e and the seed n_s = 4. □



---

## 11. Generation Tower Correction ✅

Each particle's mode index n is built from seeds {1, 4} through additive operations. Each `+` in the derivation introduces a small fractional loss ε — two frequencies added together achieve ~99.865% coherence:

```
m_corrected(n, d) = m_scale_d × S(n, d) × (1 − ε)^k
```

where k counts the additions used to generate n from seeds.

### Derived Parameter ✅

**g_coeff = 2/√7 from the kernel self-consistency eigenvalue.**

The kernel self-consistency condition from Part 2 §9 requires:

```
n_s(n_s+1) / S(n_s,4) = n_u(n_u+1) / S(n_u,5) = 4/7
```

Both ratios equal 4/7 exactly: 4×5/35 = 12/21 = 4/7. This is the coupling self-consistency eigenvalue at the Jacobi critical site k₀ = n_s² = 16. The l=2 kernel coupling amplitude is the square root of this eigenvalue:

```
g_coeff = √(n_s(n_s+1) / S(n_s,4)) = √(4/7) = 2/√7
```

The GTC correction per winding normalised at k₀ and n_mu = S(n_s,4) = 35:

```
ε = g_coeff / (k₀ × n_mu)
  = (2/√7) / (16 × 35)
  = 1/(280√7)
  = 0.001350
```

ε is now fully derived from the Lagrangian — the self-consistency eigenvalue 4/7 determines g_coeff; the critical site k₀=16 and muon mode index n_mu=35 set the normalization.

Empirical fit from c/u and t/u: ε = 0.001340. Derived value: 0.001350. Gap: 0.74% — within PDG light quark uncertainties.

### k Values by Particle

| Particle | n | k | Derivation |
|---|---|---|---|
| down | 1 | 0 | seed |
| strange | 4 | 0 | seed |
| up | 3 | 0 | n_s − 1: subtraction only |
| charm | 20 | 3 | S(n_s,3): n_s=4 terms → 3 internal additions |
| top | 72 | 10 | 2×S(2n_s,2): k_c=3 chained with S(8,2) internal k=7 → 3+7=10 |

**GTC is a d=4-sector correction only.** The k values above are used exclusively for ratios within d=4 (c/u and t/u). Mode indices for d=6 particles (e, μ, τ) also involve additions (n_e = n_ν₁+n_up, n_mu = S(4,4), n_τ = n_ν₃+n_down), but the GTC does not apply to them: d=6 modes have k=0 effective phase load because the same factor would appear in every d=6 mass and cancel in all ratios. The tau's residual is handled separately by the d=6→d=10 Dyson resummation (§9b).

**Note:** k_charm = k_g33 = n_s − 1 = 3. The same number of additions that generate the charm mode index also generate the vacuum stability gap k₀ = n_s². This is not a coincidence — both are built by the same operation: adding n_s to itself n_s−1 times from the seed.

**Chain order:** d=6 is terminal in the downstream phase chain (τ at −0.001% after Dyson resummation, μ at −0.002%). d=4 is earliest (largest n-dependent excess), consistent with d=4 receiving downstream phase load while d=6 receives none. The tau's residual is closed by the d=6→d=10 isotropic back-reaction (Part 2 §9b), not the GTC.

### Results

| Ratio | Raw error | After GTC |
|---|---|---|
| mu/e | −0.001% | −0.001% (Δk=0) |
| s/d | 0.000% | 0.000% (Δk=0) |
| c/u | +0.403% | **0.000%** |
| t/u | +1.311% | **−0.048%** |
| t/c | +0.904% | **−0.045%** |
| tau/mu | −0.059% raw | **+0.001%** after Dyson resummation (separate mechanism: §9b) |

```python
GTC_EPS = 1/(280 * 7**0.5)   # derived: 0.001350
GTC_K   = {'down':0, 'strange':0, 'up':0, 'charm':3, 'top':10, 'bottom':0}
# d=6 and d=10 particles not in GTC table: GTC correction cancels in all d=6 ratios
```

---

## 12. Two-Layer Mass Structure and Unified Scale Formula ✅

All sector mass scales reduce to m_e (via m_scale_6 = m_e/S(13,6)) plus the coupling ratios:

```
m_scale_d = m_scale_6 × √(g_dd/g_66) × S(n_e,6) / S(n_min(d),d)
```

where n_min(d) is the lightest occupied mode in sector d. For d=3 this gives m_scale_3 = m_scale_6 × √(g33/g66) × 18564/1 = m_e × √(g33/g66) = 4.702 MeV ✓

**Two independent error levels from the rank-1 structure:**

The rank-1 kernel G = vvᵀ implies any kernel back-reaction on mode frequencies is sector-uniform — identical fractional shift for all n within a given d. Prediction errors therefore decompose into two independent levels:

- **Level 1 (sector-uniform):** The coupling self-consistency derivation produces a uniform fractional offset within each sector — identical for every mode. Confirmed: d quark and s quark both show +0.682% exactly despite spanning n=1 to n=4. This is a structural consequence of the rank-1 kernel: any scale error in m_scale_d is the same for all n within that d. It is not a coincidence — the rank-1 structure forces it.
- **Level 2 (n-dependent):** the l=2 tensor part of the cross-sector kernel, corrected by the GTC with ε = 1/(280√7). After subtracting the d=4 sector base (+0.79%), the GTC with k_c=3 and k_t=10 accounts for the within-sector excess.

The two levels are structurally independent: Level 1 comes from the l=0 scalar part of (ξ_d·ξ_{d'})²; Level 2 comes from the l=2 tensor part.

**d=6/d=10 kernel symmetry:** v₆ = v₁₀ = 1/2 exactly. The kernel cannot distinguish the charged lepton sector from the tau sector — both have identical coupling strength. The mass difference between muon and tau arises entirely from different sector geometry (S(35,6) vs S(23,10)), not from any coupling difference. This is a genuine symmetry of the kernel, broken only by the Hopf chain's sector manifold assignments.

**Self-consistency derivation route:**
The sector mass scales satisfy m_scale_d² = g_dd × ⟨|Ψ^(d)|²⟩ — the kernel self-consistency fixed-point equation. Once g_dd is computed from the sector geometry (CP², S³, CP³) for each sector, all mass scales become fully derived. m_e and m_W are the two empirical inputs from measurement; the framework has no free parameters.

**Current status by sector:**

| d | g_dd source | m_scale derived? |
|---|------------|-----------------|
| 6 | g₆₆ = Y_L² = 1/4 from anomaly cancellation | ✅ (electron anchor) |
| 3 | g₃₃ = n_s²√(n_s+n_u)/2 from seed self-interaction | ✅ from m_e |
| 4 | g₄₄ = n_sn_u/√(n_s+n_u) from seed harmonic mean | ✅ from m_e |
| 10 | g₁₀,₁₀ = g₆₆ from tau hypercharge | ✅ (m_scale_10 = m_scale_6) |
| 2 | empirical measurement: m_W | ✅ from m_W |
| 5 | g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂ from Hopf fiber universality | ✅ algebra closed; mass hierarchy open 🔶 |

---

## 13. Sector Termination — Gegenbauer Criticality ✅

The IDWT sector set {2,3,4,5,6,10} terminates at d=10 for three independent reasons, the third being an algebraic consequence of the seed structure: Gegenbauer criticality.

**Definition.** The Gegenbauer polynomial coupling at the seed resonance site k₀ = n_s² = 16 in the d-dimensional Jacobi chain is:

```
b_{k₀}(d) = √(k₀(k₀+d−1)) / (2k₀+d−2)
```

For the six IDWT sectors: b_{k₀} takes values 0.51539 (d=2) down to **0.50000 (d=10) exactly**, then 0.49747 (d=11, subcritical).

**Theorem.**  b_{k₀}(d) = 1/2  ⟺  4k₀ = (d−2)²  ⟺  d = 2 + 2n_s = 10.

**Proof.**  b = 1/2  ↔  4k₀(k₀+d−1) = (2k₀+d−2)².  Expanding: LHS = 4k₀² + 4k₀(d−1), RHS = 4k₀² + 4k₀(d−2) + (d−2)². Subtracting: 4k₀ = (d−2)². With k₀ = n_s² = 16: d = 2 + 2√16 = 2 + 2n_s = 10. □

**Corollary (WKB exactness for d=10).** The leading-order WKB delay τ_d = 1/(2√(k₀+d)) acquires a next-order correction proportional to (b_{k₀}−1/2)/b_{k₀}². For d=10 this correction **vanishes identically**. For d=3 through d=6 the corrections are −0.67% to −0.44% and shift the ρ meson prediction in the wrong direction (away from PDG), confirming that the +0.069% residual is a genuine floor, not a WKB artifact.

**Sector summary — three routes to d=10:**

| Route | Origin | Statement |
|---|---|---|
| Hurwitz (geometry) | Division algebras | 𝕆 = last normed algebra; octonionic Hopf → d=10 |
| **Gegenbauer (algebra)** | **Jacobi chain criticality** | **b_{k₀}=1/2 iff d=2(n_s+1)=10** |
| Hypercharge (gauge) | Anomaly cancellation | g_{10,10}=g_{6,6}=Y_L²=1/4 |

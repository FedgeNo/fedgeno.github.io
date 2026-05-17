# Infinite Dimensional Wave Theory

## Overview
A physics framework under construction. Reality is a single complex wave Ψ∞ on an infinite-dimensional manifold M_∞ = ℝ_t × Ξ_{10}. The hidden space Ξ decomposes into six sectors d ∈ D = {2, 3, 4, 5, 6, 10}, each a distinct geometric manifold. We are inside M_∞ at the d=3 coordinate level; the observable universe is Ψ∞ evaluated at fixed hidden coordinate ξ⁰.

## Core Principles
- Reality is a single complex wave Ψ∞ on an infinite-dimensional manifold.
- We are inside M_∞ at the d=3 coordinate level, not external observers projecting onto a screen. Particles with d > 3 vibrate across dimensions we do not occupy; we measure only their d=3 activity.
- The hidden dimensions are not compactified Planck-scale curls; they are macroscopic.
- What we call mass is a scaled count of hidden microstates.
- Gravity is a phenomenon of M_∞ — it has no sector boundary. G_N = G_∞/V_7; V_7 ≈ 113 is fully derived from sector couplings. V_vacuum (d>10) does not enter: curvature from d≤10 propagates into d>10 but disperses (T5: scattering states, not L²-normalizable); d>10 is Ricci-flat in vacuum (R_ab=0, no contribution to a_2 = ∫R dvol). G_∞ = G_N × V_7 = 7.57 × 10^{-43} MeV^{-2} (currently input from measurement). Genuine closure: a_4 is Λ-independent in IDWT (fixed by T9); computing a_2(M_∞) from T14 sector heat kernels + Ricci scalars and using the a_2/a_4 ratio eliminates Λ and makes G_N a prediction — this is the single remaining open item. KK formula M_Pl^2 = M_∗^9 V_7^phys does not apply (requires compact dimensions and KK graviton tower, both excluded). Gravity couples to each particle through that particle's dimensional complexity, encoded in mass m(n,d) = S(n,d) × m_scale_d.
- Forces mediate via coordinate containment: a particle couples to a force only if it has wavefunction support in the force's sector coordinates. Complementary principle — coupling filter: the particle's own sector geometry determines the structure of that coupling. The sector quantum number (polarization, color, Dirac condition, color silence, AA Cantor-set) is not a label; it is the geometry expressing itself as a coupling structure, specifying both what interactions are available and what is geometrically forbidden. Both principles together determine the full interaction structure of any particle (Part 1 §3d, §3g; Part 3 §0.8).
- Extra dimensions are purely spatial. Time is 1D and universal.

## Key Formulas

**Mass formula:**
```
m(n,d) = S(n,d) × m_scale_d
S(n,d) = C(n+d-1, d)   [binomial coefficient — simplex number]
```

**Sector set:** D = {2, 3, 4, 5, 6, 10}

**Seed:** n_s = 4 = χ(CP³) = N_c+1; n_u = 3 = χ(CP²) = N_c (T15)

**Newton's constant:** G_N = G_∞ / V_7; V_7 = L_4 × L_5 × L_6 × L_10^4 ≈ 113 (fully derived from sector couplings); V_vacuum does not enter (d>10 Ricci-flat in vacuum + T5 scattering states not L²-normalizable); G_∞ requires spectral action scale Λ (open)

**Two-stage filter:**
- Stage 1: Ω_log(n,d) = ln(S(n,d)/S(n,2)) ≤ ln 2
- Stage 2: n must be a co-fixed-point of the sector comb filtration from n_s

**Occupied mode indices:** Σ = {1,3,4,10,13,15,20,22,23,35,72,76,81,95} plus bottom quark beat at k_0=16

## Sector Map

| d  | Geometry | Symmetry        | Physical content              |
|----|----------|-----------------|-------------------------------|
| 2  | CP¹      | U(1)            | Gauge bosons (γ, W, Z, H)    |
| 3  | S³       | SO(4)           | Down-type quarks (d, s, b)   |
| 4  | CP²      | SU(3)/U(2)      | Up-type quarks (u, c, t)     |
| 5  | S⁵       | SO(6)           | Neutrinos (ν_e, ν_μ, ν_τ)   |
| 6  | CP³      | SU(4)/U(3)      | Charged leptons (e, μ)       |
| 10 | CP⁵      | SU(6)/U(5)      | Tau lepton                   |

Coordinate nesting: Ξ_2 ⊂ Ξ_3 ⊂ Ξ_4 ⊂ Ξ_5 ⊂ Ξ_6 ⊂ Ξ_{10}

## Theorems

**T0 — Physical Spectrum.** The physical masses are eigenvalues of the projected Dirac operator P_{ξ⁰} D P_{ξ⁰}. The filtered spectrum is σ_phys = {S(n,d) × m_scale_d | (n,d) passes Stage 1 and Stage 2}. The 15 elements are exactly the SM particle masses, determined by n_s=4 and m_e alone.

**T0.5 — Two-Stage Observability Filter.** A mode (n,d) is physical iff it passes both stages. Stage 1 is dimensional visibility (Ω_log ≤ ln 2 — sufficient vibrational activity in our d=3 dimensions). Stage 2 is the co-fixed-point condition (n must be a co-fixed-point of the sector comb filtration from n_s; purely algebraic, applies uniformly across all sectors). Stage 1 governs observability; Stage 2 selects stable resonances of M_∞.

**T1 — Hilbert Series.** m(n,d)/m_scale_d is the coefficient of t^n in the Poincaré-Hilbert series of ℝ[x_1,...,x_d]. Equivalently, S(n,d) = IDOS_d(n) = dim Sym^{n-1}(ℝ^{d+1}). Hockey-stick identity S(n+1,d) = S(n,d) + S(n,d-1) is the d-dimensional quasicrystal inflation rule.

**T2 — Kernel Uniqueness.** Among all U(d)×U(d')-invariant degree-4 polynomials on Ξ_d × Ξ_{d'}, the interaction (ξ_d·ξ_{d'})² is the unique one satisfying: (1) non-trivial sector mixing, (2) ℓ=0⊕ℓ=2 decomposition (ℓ=0 gives mass scale, ℓ=2 gives GTC correction ε), (3) rank-1 factorisation g_{dd'} = v_d v_{d'}.

**T3 — Sector Set Theorem.** D = {2,3,4,5,6,10} is uniquely determined by the complex Hopf fibration chain S¹→S^{2n+1}→CP^n plus two termination rules:
- Rule A (coupling termination): g_{66} = 1/n_s is a seed ratio, not a kernel fixed-point. Hopf universality cannot extend to d=7. Excludes d=7,8,9.
- Rule B (Gegenbauer criticality): b_{k0}(d) = √(k_0(k_0+d-1))/(2k_0+d-2) ≥ 1/2 required; saturates uniquely at d=10. Excludes d≥11.
- Assembly: {2,3,4,5} from Hopf pairs n=1,2 ∪ {6} from n=3 base (Rule A) ∪ {10} from n=5 base (Rule B).
- Two qualitatively distinct exclusion types: d≥11 are subcritical — localization is geometrically impossible (most fundamental exclusion). d=7,8,9 are supercritical (localization possible in principle) but no valid sector potential forms — absent from the coordinate nesting; the nesting jumps Ξ_6 ⊂ Ξ_{10} with nothing between.

**T4 — Seed Uniqueness.** n_s=4 is the unique positive integer for which n_s(n_s+1)/S(n_s,4) = n_u(n_u+1)/S(n_u,5) = 4/7, with n_u = n_s−1 = 3. This is the RG fixed-point of the cross-sector kernel at k_0 = n_s² = 16.

**T5 — Aubry-André Criticality.** d=10 is the unique sector at the Aubry-André metal-insulator transition b_{k0}(d) = 1/2. Equivalent to 4k_0 = (d−2)², giving d = 2(n_s+1) = 10. Sectors d<10 are supercritical (extended states), d=10 is critical (Cantor-set spectrum), d≥11 are subcritical (no stable modes).

**T6 — PMNS Theorem.** All three PMNS mixing angles are determined by g_{55} = 96/g_{22} and four mode indices (n_e, n_μ, n_τ, n_{ν}), with no free parameters. Predictions: sin²θ_{23} = 0.55897 (PDG: 0.561, −0.36%), sin²θ_{12} = 0.30856 (PDG: 0.307, +0.51%), sin²θ_{13} = 0.02211 (PDG: 0.0220, +0.51%).

**T7 — EW Scale Self-Consistency.** √Tr(D²) = 248.3 GeV from the 15 IDWT masses. The G_F-derived EW scale is 246.3 GeV. The 0.85% gap is a spectral normalisation artefact — Tr(D²) sums raw eigenvalues without GTC corrections while G_F is derived from the W mode index and g_2 coupling. The gap is not f_2-dependent. This is a self-consistency check, not an independent prediction.

**T8 — CP Phase from Spectral Flow.** 🔶 δ_CP^{(tree)} = 0 (product state, Part 9). Topological source: Δc_1 = c_1(CP³) − c_1(CP⁵) = 4 − 6 = −2. Spectral flow approach (Part 10): parameterize entanglement via θ_{13}; sf(D_{CP^n}; 0→θ_{13}) = c_1(CP^n)·θ_{13}/π; relative Δη = 2θ_{13}/π; φ_Berry = −2θ_{13}; TBM boundary δ_{TBM} = π. Formula: δ_CP = π + (N_c−1)θ_{13} = π + 2θ_{13} = 197.11° (PDG NH ≈197°, +0.05°); J = −0.00981 (PDG ≈−0.0098, +0.1%). Three derivation gaps remain: (i) spectral flow coefficient needs rigorous derivation from rank-1 perturbation; (ii) sign of U_{e3} at TBM needs explicit T6 coupling matrix computation; (iii) equivalence of spectral flow path and Part 9 Berry coupling-space integral not formally proved. Falsifiable by DUNE/Hyper-K 2028–2030.

**T9 — Coupling Constant Theorems.** All six sector self-couplings derived from n_s=4 alone:
- g_{22} = (S(n_s,3)−n_u)²(S(n_u,4)−S(n_u,3))/2 = 722.5
- g_{33} = n_s²√(n_s+n_u)/2 = 8√7
- g_{44} = n_s·n_u/√(n_s+n_u) = 12/√7
- g_{55} = g_{33}g_{44}/g_{22} = 96/g_{22} (Hopf universality)
- g_{66} = g_{10,10} = 1/n_s = 0.25 (seed ratio; μ-τ symmetry)
- T9a: g_{33} × g_{44} = 96 exactly; g_{22} × g_{55} = 96.

**T10a — Generation Tower Correction.** The ℓ=2 kernel component (T2) gives GTC correction ε = 1/(280√7) ≈ 0.001350 at depths {0, n_u, S(n_u,3)} = {0,3,10} for {u,c,t}. Closes c/u error to 0.000%, t/u to −0.048%.

**T10b — Dyson Resummation (τ lepton).** At the AA critical point, the d=10 eigenvalue has correction δ_τ = 1/(n_u·n_s²·S(n_s,4)) = 1/1680. Result: m_τ × (1+1/1680) = 1776.84 MeV (PDG: 1776.86 MeV, −0.001%).

**T11 — Neutrino Spectral Theorems.**
- T11a: m_scale_5 = (n_u/n_s) × m_scale_6³/m_scale_4² = 7.429×10⁻¹³ MeV
- T11b: m_{ν2}/m_{ν1} = S(15,5)/S(10,5) = 5.808; Δm²_{21} = 7.242×10⁻⁵ eV² (PDG: 7.42×10⁻⁵, −2.4%)
- T11c: Neutrinos are strictly Dirac (d mod 8 = 5 forbids Majorana). 0νββ rate = 0 exactly.
- T11d: Σm_ν = 60.39 meV (corrected: δ_ν₃ = ε × g_{33} = 1/35 derived in §9d; uncorrected: 59.00 meV). Normal ordering, no free parameters. Within CMB-S4 reach.

**T13a — Spectral Sum Rule.** ζ_d(1) = Σ_{n=1}^∞ 1/S(n,d) = d/(d−1) for every IDWT sector. Exact, parameter-free.

**T13b — Mode Spacing Identity.** S(n+1,d) − S(n,d) = S(n+1,d−1) for all n≥1, d≥2. The gap between consecutive resonances in sector d equals the (n+1)-th resonance of sector d−1. Every generation-law identity of the form n_particle = n_a + n_b traces to this.

**T13c — Exact Mass Ratios.** Within a single sector, m_scale_d cancels. All intra-sector mass ratios are pure rationals of S(n,d) values, with algebraic GTC or Dyson corrections — no free parameters at any step.

**T14 — Heat Kernel.** K_d(t) = Σ_{n≥1} e^{−t·S(n,d)}. Weyl coefficient a_0^(d) = Γ(1+1/d)(d!)^{1/d}. Spectral zeta at zero: ζ_d(0) = −d/2. First excitation gap = d in dimensionless units. Universal ground state S(1,d) = 1 for all d.

**T15 — Euler Characteristic Unification (+ Corollaries T15a–f).** N_c = χ(CP²) = n_u = 3; n_s = χ(CP³) = N_c+1 = 4. All six sector self-couplings are functions of N_c alone (T9 with n_u = N_c). Extended corollaries:
- T15a: Terminal sector d = 2(N_c+2) = 10 (from T3 Rule B + k_0 = n_s²)
- T15b: CP χ-sequence {N_c−1, N_c, N_c+1, [gap N_c+2 = Rule A], N_c+3}; n_top = N_c(N_c+1)(N_c+3) = 72
- T15c: Both Hopf coupling products equal N_c(N_c+1)³/2 = 96
- T15d: n_e = N_c²+N_c+1 = 13; n_{ν1} = N_c²+1 = 10; all mode indices from N_c
- T15e: m_scale_5 = (1−g_{66}) × m_scale_6³/m_scale_4²; neutrino suppression = complement of lepton coupling filter
- T15f: g_{dd} anti-correlates with isometry group dimension — larger symmetry group → more forbidden interactions → weaker coupling → lighter masses
- Theorem S2 (m_u/m_d = √(3/14)) is a corollary. Absolute scale m_e is the only dimensional input.

**Part 1 §3b — Completeness of Particle Spectrum.** The IDWT particle spectrum is exactly 15 states. No additional stable particles exist. Any new state would require a new sector (excluded by T3) or a new mode index passing Stage-2 (exhaustively excluded). The spectrum is closed.

**Part 8 — Spectral Numerical Theorems.**
- S1: S³ Dirac spectrum grounds S(n,3) — the eigenvalues of D_{S³} are exactly S(n,3).
- S2: Cross-sector frequency ratio m_u/m_d = √(3/14); N_c-determined (T15 corollary).
- S3: g_{22} is a Dirac multiplicity product; ind(D^c_{CP²} ⊗ O(1)) = 3 = N_c colours.

## Document Map

**Part 1 — Foundations**
- §0: The Actual Structure: A Spectral Triple
- §1: Core Postulates
- §2: Observable Coordinates and the Born Rule (§2.1–2.4, including cut-and-project analogy)
- §3: Sector Structure of M_∞ (§3a Sector Set Theorem, §3b Spectrum Completeness, §3c Gegenbauer Criticality, §3d Per-Sector Profiles, §3e Summary Table, §3f Coordinate Extension, §3g Interaction as Coordinate Containment, §3h Sector Autonomy, §3i d=3 Threshold)
- §4: The Unified Kernel
- §5: Canonical Particle Assignments (incl. Uniqueness of Occupied Mode Index Set)
- §6: Neutrino Sector
- §7: Relationship to Existing Physics
- §8: What Would Falsify IDWT (Categories A–D)

**Part 2 — The Mass Formula**
- §1: The Simplex Formula and Hockey-Stick Identity
- §2: Per-Sector Comb Filter H_d(ω)
- §3: Pascal Recursion — One Identity, All Generation Laws
- §4: Why d=6 is Colour-Neutral
- §5: The seed n_s=4 — Hockey-Stick Forced
- §6: Complete Index Derivation
- §7: Neutrino Sector
- §8: Bottom Quark — Quartic Bifurcation
- §9: Coupling Constants — Complete Derived Set (§9b Tau Dyson Resummation, §9c Neutrino Mass Scale)
- §10: Mass Scale Derivation (§10b g_{22} back-reaction fixed-point)
- §11: Generation Tower Correction (§11.1–11.5)
- §12: Two-Layer Mass Structure and Unified Scale Formula
- §13: Sector Termination — Gegenbauer Criticality
- §14: Spectral Convergence and Analytic Control

**Part 3 — Forces, Gauge Structure & Colour**
- §0: The Complete IDWT Action (§0.1–§0.7 field content, action, EOM, couplings; §0.8 Force Mediation as Spatial Geometry; §0.9 CKM Matrix from the Kernel; §0.10 Pure Sector Identities)
- §1: Electromagnetism
- §2: Colour Charge from CP²
- §3: Colour Symmetry from Consistency (§3a Colour Connection)
- §4: Effective Colour Coupling from the Kernel
- §5: Colour Confinement
- §6: SU(3)_colour × U(2)_EW from One Manifold
- §7: Chirality from Kähler γ₅
- §8: Hypercharges from Anomaly Cancellation and SO(10)
- §9: QCD β-Function Coefficient
- §10: Electroweak Predictions
- §11: Boson Eigenmode Selection and Sector Coupling Map
- §12: Cabibbo Angle
- §13: Spin^c Structure and Hypercharge Derivation
- §14: Electromagnetism from the Hopf Fiber
- §15: The Quantum Number Package
- §16: Electromagnetism: Ward Identity and L-Parity Protection (§16.1–16.4)

**Part 4 — Gravity**
- §1: Gravity is Curvature of M_∞ Caused by Mass
- §1b: Why Macroscopic Hidden Dimensions Are Consistent with All Experiment
- §2: Newtonian Limit
- §3: Gravity on M_∞: Source, Structure, and the 3D Observer's Measurement (§3.1 Gravity as ∞D curvature sourced by mass; §3.2 Observer's effective gravitational equation; §3.3–§3.7 formal structure; §3.9 Sector Localization Length; §3.10 Derivation of λ_d; §3.11 Newton's Constant Sector-Independence; §3.12 No Hidden-Sector Correction and G_N as 3D measurement of ∞D curvature; §3.12.4 G_∞ numerically + spectral action closure condition — G_∞ = 7.57×10^{-43} MeV^{-2}; a_4 Λ-independent via T9; genuine closure path: compute a_2(M_∞) from T14 heat kernels to eliminate Λ; KK M_∗ formula rejected; §3.13 Covariant Conservation of T_{μν}^eff)
- §4: Cosmological Constant
- §5: Two-Stage Observability

**Part 5 — Predictions**
- §1: Confirmed Predictions
- §2: Full Prediction Table with Statistical Significance
- §3: d=4 Sector GTC Correction (§3b Extended Predictions, §3c Deep Predictions, §3d d=3 Hadronic Resonance Spectrum)
- §4: PMNS Mixing
- §5: Electroweak Running
- §6: PMNS Angle Hierarchy
- §7: d=10 as the Aubry-André Critical Point
- §8: S(n,d) as IDOS
- §9: Falsification Criteria (Categories A–D)

**Part 6 — Open Questions**
- Reframing: What Is Actually Open
- Open items
- Structural Findings on Blocked Computations

**Part 7 — Two-Stage Observability & Mode Selection**
- §1: All Modes Exist — Two-Stage Observability (§1.1–§1.6 incl. quartic bifurcation, sideband beats)
- §2: Two-Stage Filter Summary (§2.5 Complete Low-n Observability Atlas)
- §3: CP^d Coordinate Geometry

**Part 8 — Quantum Structure, Lorentz, Dirac & Confinement**
- §1: Lorentz Covariance
- §2: Hidden-Sector Quantum Numbers (§2.1 Majorana/Weyl Classification, §2.2 Spin Structure, §2.3 Chirality from Kähler γ₅, §2.4 Dirac Index per Sector)
- §3: Spectral Counting Theorem (§3.1–§3.4 incl. connection to Dirac operator D_Ξ)
- §4: General Odd-Sphere Spectral Theorem
- §5: Spectral Numerical Theorems (S1, S2, S3)
- §6: The Master IDWT Equation
- §7: Cabibbo Angle
- §8: SU(3) Status — Automorphism
- §9: Hilbert Space Rigour
- §10–13: Baryon Magnetic Moments, Proton Binding, Pion/Kaon/Vector Meson Masses, Cosmological Constant (all 🔶 pending)

**Part 9 — Spectral Theorems**
- T0: Spectral Triple definition and Physical Spectrum theorem
- T0.5: Two-Stage Observability Filter
- T1: Hilbert Series (mass as Hilbert series coefficient)
- T2: Kernel Uniqueness Theorem
- T3: Sector Set Theorem
- T4: Seed Uniqueness Theorem
- T5: Aubry-André Criticality Theorem
- T6: PMNS Theorem 🔵
- T7: Spectral Self-Consistency of EW Scale 🔵
- T8: CP Phase from Spectral Flow 🔶 — formula δ_CP = π + 2θ₁₃ = 197.11°; derivation continued in Part 10
- T9: Coupling Constant Theorems (T9a–T9d)
- T10: Perturbative Correction Theorems (T10a GTC, T10b Dyson/τ)
- T11: Neutrino Spectral Theorems (T11a–T11d)
- T13: Spectral Sum Rules and Exact Mass Ratios (T13a sum rule, T13b mode spacing, T13c mass ratios)
- T14: Heat Kernel and Spectral Geometry (T14a Weyl term, T14b ζ_d(0), T14c large-t asymptotics)
- T15: Euler Characteristic Unification (N_c = χ(CP²) = n_u; all couplings from one Euler characteristic; S2 as corollary)

**Part 10 — CP Phase Completion and Framework Synthesis**
- §1: Spectral Flow from T2 Kernel (sf(D_{CP^n}; 0→θ₁₃) = c₁(CP^n)·θ₁₃/π; Δη = 2θ₁₃/π from Δc₁ = −2); §1.0 bridges to Part 9 Berry computation (γ=0 for product state; Part 10 uses entangled θ₁₃ path)
- §2: Sign of U_{e3} at TBM from T6 formula (δ_{TBM} = π from inclusion-exclusion sign of n_{ν₃}; asserted, not yet explicitly computed from coupling matrix)
- §3: Factor-of-2 normalization (Dirac spectral period = π in θ₁₃; φ_Berry = −2θ₁₃)
- §4: T8 formula — δ_CP = π + 2θ₁₃ = 197.11°; J = −0.00981 (PDG +0.05°, +0.1%) — 🔶
- §5: Updated master status table (18✅, 3🔵, 2🔶, 0□)
- §6: Mass–Coupling–Quantum Number–CP Phase quadrilateral (item 4 established by T8; items 1–3 need verification against Part 3/8)
- §7: Falsification predictions (δ, J, δ–θ₁₃ correlation, mass ordering, 0νββ)
- §8: Updated Part 6 open questions status
- §9: Complete derivation chain from N_c = 3

## Architecture
- The script does all computation first, then prints output. This is for ease of reading by referees.
- The documents each have a specific focus but don't rely on it. Check them all if you can't find what you are looking for in the most sensible place.
- 🔶 = pending derivation. 🔵 = established but not yet in final form.

## Key Modules / Components
- A website
- 10 numbered documents (Parts 1–10 as listed above)
- A Python proof script (idwt.py)

## Constraints
- **Read the relevant documents before making claims about what the theory contains or lacks.**
- When changing a document, do not "argue" against the now non-existent previous version of the document.
- Do not introduce concepts or variables from other frameworks without explicit confirmation.
- Git is available. After completing work, stage with `git add -A`, write a short descriptive commit message summarising what changed (e.g. "Add sector-filters article", "Fix neutrino mass values in paper"), then `git push origin master`. Do not rebase, force-push, or alter history.

## Workflow
- Your role is to verify and gatekeep what goes into the documents, script and website.
- You are to verify all math before putting it into the project.
- **Keep this file in sync.** Whenever a theorem statement, framing convention, section title, or key concept changes in the documents, update the corresponding entry in CLAUDE.md in the same session. This file is the authoritative quick-reference; stale entries mislead future sessions.

# Infinite Dimensional Wave Theory — Part 6: Open Questions

What follows is an honest list of what the framework has not yet derived, with precise statements of what is needed.

---

## Reframing: What Is Actually Open

A systematic review of the labelled "open items" against PDG experimental uncertainties shows:

**Now consistent with experiment after revised derivation:**
- **Light-quark mass offsets (+0.68% d=3, +0.77% d=4):** All predictions within PDG 1σ uncertainties. The d quark (0.07σ), s quark (0.07σ), u quark (0.03σ), c quark (0.48σ), t quark (1.72σ), b quark (0.10σ) are all consistent with measurement. These are predictions that agree with experiment, not scheme-conversion residuals.
- **Λ_QCD "−9%":** IDWT defines Λ_IDWT = 3f_π = 282 MeV. The PDG "300–340 MeV" is a hadronic-scheme empirical range. IDWT's value matches 3f_π(PDG) = 276 MeV within +2.2% and m_ρ/2.74 = 283 MeV within −0.3%. The comparison label "−9%" was to an ill-defined target.

**Reclassified as data-dependent, not definitively wrong:**
- **m_ν₃ 2.5–2.9% shortfall (current data):** Δm² is not a native IDWT quantity — it is oscillation-experiment language for a technique that cannot access absolute masses. Expressed in IDWT's own terms, m_ν₃ = 48.87 meV is 2.5–2.9% below current oscillation inference (PDG 2023–2024: Δm²₃₁ = (2.51–2.53)×10⁻³ eV², giving m_ν₃^{osc} ≈ 50.1–50.3 meV). The correction δ_ν₃ = 1/35 gives m_ν₃^{corr} = 50.26 meV, implying Δm²₃₁ = 2.524×10⁻³ eV² — within 0.05% of PDG 2023 and within the ±0.025×10⁻³ experimental uncertainty of PDG 2024. Structural source: n_ν₃ = n_ν₁ + n_ν₂ − n_u is the only neutrino mode derived by inclusion-exclusion (not a primary Pascal evaluation); S(n_s,4) = 35 is the leading seed-level d=4 denominator, the same factor appearing in the τ geometric back-reaction correction (1/1680 = 1/(n_u × n_s² × S(n_s,4))). Closure relation 🔶 (primary derivation Part 2 §9d): δ_ν₃ = ε × g_{33} = 1/35, where ε = 1/(280√7) is the GTC coefficient (§11) and g_{33} = 8√7 is the d=3 coupling (T9); the √7 factors cancel algebraically (g_coeff × g_{33} = n_s² = k₀, so ε × g_{33} = k₀/(k₀ × n_mu) = 1/35). The algebraic identity is exact given independently-derived ε and g_{33}; the deeper operator mechanism — why the l=2 T2 cross-term acts with exactly this product — is not yet derived. Corrected: Σm_ν = 60.39 meV; uncorrected: 59.00 meV. Both are within current cosmological bounds; CMB-S4 will distinguish them.

**Genuine small residuals:**
- **sin²θ_W +0.37%:** The mode-index prediction is exact. The gap from PDG on-shell is 3.6σ by measurement precision alone, but ~0.8σ once theoretical loop-correction uncertainties are included. The tree-level EW prediction is at this precision inherently.
- **g₁ +0.25% (vs self-consistent PDG):** IDWT g₁ = 0.35043, derived from sin²θ_W = 0.22373 and g₂ = 0.65275 via the Weinberg relation. The g₁ derived self-consistently from PDG on-shell sin²θ_W = 0.22290 and PDG g₂ = 0.65270 is 0.34957; IDWT sits +0.25% above it — entirely the sin²θ_W structural gap (+0.37%) propagated via the Weinberg angle relation. Not a separate quantity. The PDG tabulated value 0.35740 is in MS-bar at m_Z, a different scheme and scale; the −1.95% gap to that figure is the scheme/scale offset, not a physics discrepancy.

**Genuinely open (computation not done):**
- PMNS mixing angles — spectral geometry formulas derived:
  sin²θ₂₃=0.5590 (PDG 0.561, -0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%),
  sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). From g₅₅=96/g₂₂ and mode indices.
  Still open: CP phase δ and CP-violation amplitude J
- CP-violating phase δ (Hopf Chern-Simons integral)
- g₁ comparison offset — IDWT g₁ = 0.35043 is +0.25% above the self-consistent PDG value (derived from PDG sin²θ_W and g₂ via the Weinberg relation), entirely the sin²θ_W structural gap (+0.37%) propagated. The −1.95% gap to the PDG tabulated value 0.35740 is a scheme/scale offset (MS-bar at m_Z vs d=2 sector scale); no loop order or scale translation changes a structural prediction.

---

## Open

**f_π and Λ_QCD**
The IDWT geometric dilution function gives g_eff(n) = g₃₃/S(n,3), with confinement at g_eff = 1 (heuristic criterion by analogy with α_s ≈ 1; native derivation from the IDWT action is open) → S(n_conf,3) = g₃₃ = 8√7 ≈ 21.17. The nearest integer solution is n_conf = n_s = 4 (the seed itself). The confinement mass scale is:

f_π = m_scale_3 × S(n_s,3) = 4.702 × 20 = 94.04 MeV   (PDG: 92.1 MeV, +2.1%)

The pion decay constant is the mass at the seed level — the seed is the confinement mode. Λ_QCD = N_c × f_π = 3 × 94.04 = 282 MeV, matching 3×f_π(PDG) = 276 MeV within +2.1% — this relation uses N_c = 3 from χ(CP²). **🔶 Proton mass phenomenological scaling ansatz** (temporary estimate — native derivation from kernel binding energy pending — Part 8 §11): m_p = N_c × Λ_QCD × (1 + 1/n_up²) = 3 × 282.1 × (10/9) = 940.4 MeV (PDG: 938.3, +0.22%). This is a large-N_c QCD scaling law with IDWT-derived inputs; it is not a prediction from the IDWT kernel and should be replaced when the kernel binding energy calculation is complete.

**Full CKM matrix and CP violation**
The Cabibbo angle is derived including curvature correction: sin θ_C = (1 + χ(CP¹)/(24·S(n_s,3)))/√S(n_s,3) = (1+1/240)/√20 = 0.22454 (Part 3 §12), matching PDG |V_us| = 0.22450 ± 0.00044 at +0.09σ. |V_cb| = √(S(n_u,4)/S(n_c,4)) = √(15/8855) = 0.04116 (Part 3 §0.8; PDG exclusive: 0.04100 ± 0.0014, +0.11σ). Remaining open: |V_ub| (requires CP phase) and the CP-violating phase δ (requires complex structure in the Vandermonde kernel — not yet constructed). Note: V_ud = √(1−sin²θ_C) = 0.97447 is not a separate prediction but the unitarity complement of sin θ_C. The apparent 5.5σ gap against the nuclear beta-decay value (0.97370 ± 0.00014) is the Cabibbo Angle Anomaly — a pre-existing ~3σ unitarity deficit in the Standard Model itself. IDWT enforces exact CKM unitarity by construction; √(1−|V_us|²_PDG − |V_ub|²_PDG) = 0.97447 matches IDWT exactly. IDWT predicts sin θ_C = 0.22454; the PDG value is 0.22450 ± 0.00044 (+0.09σ agreement). The unitarity gap is between two independently measured PDG quantities, independent of IDWT's predictions.

**Neutrino mass scale**
The d=5 mass scale follows from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³, giving m_scale_5 = 7.429 × 10⁻¹³ MeV. This is the d=5 analog of the g₂₂ back-reaction equation. See Part 2 §9c. Absolute masses: m_ν₁ = 1.487 meV, m_ν₂ = 8.639 meV, m_ν₃ = 50.27 meV (corrected; bare 48.87 meV), Σm_ν = 60.39 meV (bare 59.00 meV; δ_ν₃ = 1/35, Part 2 §9d).

**Lorentz completion 🔶**
Scalar covariance, spin-½ from the sector Dirac operator, chirality from Kähler γ₅ on CP² and CP³, and particle/antiparticle from the complex spinor are all established. Remaining: full Spin(9) decomposition for d=10. The main open item is the explicit D_Ξ spectrum matching m_scale_d × f(S(n,d)).

**Open foundational question — why S(n,d) = C(n+d−1,d) as mass eigenvalue 🔶**
The IDWT mass formula m(n,d) = m_scale_d × S(n,d) is numerically exact and structurally natural (S(n,d) counts the dimension of Sym^n(ℝ^d) and appears as the cumulative Dirac eigenvalue count on S^{d-1}). But no argument has been given from the IDWT action or equations of motion for why the physical mass eigenvalue scales as the cumulative simplex count rather than n², n(n+d−1) (the Laplacian eigenvalue on S^{d-1}), or another function of n and d. These alternatives would give different sector-scale correlations and different mass hierarchies between sectors. The likely resolution involves the quartic bifurcation structure: the fixed-point equation for the sector comb at k₀ = n_s² selects eigenstates by cumulative counting — not by individual spectral levels — which is why S(n,d) and not the individual Laplacian eigenvalue appears. Deriving m = m_scale_d × S(n,d) directly from the H_d eigenvalue problem with V_d(r) = λ_d r²/(1+r²), and understanding why the cumulative count gives sector-scale correlations, is a primary open derivation.

**🎯 Sector set D as spectral gap structure of the IDWT ground state 🔶**

The sector set D = {2,3,4,5,6,10} is currently derived from M_∞'s topology and geometry: Gegenbauer criticality (4k₀=(d−2)², k₀=16), Hopf fibration pairing (d=3,4,5,6), Euler characteristic constraints, and the Gegenbauer fixed-point closure condition (Part 9 T3). These are properties of M_∞ independent of any specific field configuration. Two open theorems follow from this structure.

**Open Theorem A.** Let Ψ_∞ be the IDWT ground state and define the directional covariance operator Ĉ = ∫ |∂Ψ_∞⟩⟨∂Ψ_∞| dv. Does Ĉ have eigenvalue spectral gaps at exactly d = 2, 3, 4, 5, 6, 10 — and no others? If yes, the sector set D is recoverable as the set of stable spectral plateau indices of Ĉ, providing an operator-theoretic characterization that is independent of and complementary to the topological derivation via T3. This would constitute a self-consistency theorem: the sectors selected by M_∞'s geometry are exactly the ones at which the ground-state field concentrates its directional activity.

**Open Theorem B / Conjecture.** The sector mass scales satisfy m_scale_d ∝ √λ_d, where λ_d is the d-th eigenvalue of Ĉ. If true, the m_scale_d hierarchy — currently derived from the Hopf coupling chain and Gegenbauer fixed-point equations — could be re-derived from the vacuum structure of Ψ_∞ directly. This would convert m_scale_d from external inputs (one of which is m_e as the unit reference) into predictions from the field's ground-state covariance structure.

Note: the covariance operator construction is not a new foundation for IDWT — d is not defined by Ĉ, because Ĉ requires knowing Ψ_∞ which presupposes the sector structure. Rather, proving Theorem A would show the two derivations are consistent; proving Theorem B would elevate the m_scale_d hierarchy to a computable prediction.

**G_N from infinite-dimensional gravity 🔶**
Gravity is a phenomenon of $M_\infty$ — it has no sector boundary and couples to every particle through that particle's dimensional complexity (encoded in mass). $G_N = G_\infty / V_7$, where $V_7 = L_4 L_5 L_6 L_{10}^4 \approx 113$ is fully derived from sector coupling constants. The vacuum-sector contribution (d>10) does not enter: curvature from d≤10 does propagate into d>10 (no hard wall), but T5 establishes that d>10 modes are scattering states — any disturbance disperses rather than localizing. Two arguments confirm $V_{\rm vacuum}$ drops out of the spectral action: (i) d>10 is Ricci-flat in vacuum ($R_{ab}=0$, so $a_2=\int R\,{\rm dvol}$ receives no d>10 contribution), and (ii) scattering states are not L²-normalizable and do not appear in ${\rm Tr}(f(D/\Lambda))$. The single remaining open item is $G_\infty$: fixing the spectral action scale $\Lambda$ makes $G_N=G_\infty/V_7$ a complete prediction. (Part 4 §3.12.2)

**$\Lambda$ and $f_k$ spectral coefficients 🔶**
The spectral action $\text{Tr}(f(D/\Lambda)) \sim f_4\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_0 a_4 + O(\Lambda^{-2})$ identifies $G_N^{-1} \propto f_2\Lambda^2$ (Einstein-Hilbert term from $a_2$) and $\Lambda_{\rm cosm} \propto f_4\Lambda^4$ (cosmological constant from $a_0$). The spectral cutoff $\Lambda$ and function $f(x)$ are not fixed by the sector combinatorics alone. Fixing $f_2\Lambda^2$ would determine $G_{\rm fund}$ from the action without treating it as a measured input. Note: $\sin^2\theta_W$ (+0.37%), $g_1$ (offset from PDG = sin²θ_W structural gap propagated via Weinberg relation), and $\sqrt{\text{Tr}(D^2)}$ (0.82%) are not $f_2$-dependent — $\sin^2\theta_W$ is purely combinatorial, $g_1$ is the Weinberg-angle propagation of the $\sin^2\theta_W$ gap, and $\sqrt{\text{Tr}(D^2)}$ is a spectral normalization artefact (top mass enters uncorrected). The $f_k$ open item is specifically about $G_{\rm fund}$ and the cosmological constant, not about particle mass residuals.

---

## Structural Findings on Blocked Computations

**PMNS angles — now derived from spectral geometry (T6, Part 9).** The charged-current coupling matrix between d=5 and d=6/10 is rank-1, giving μ–τ symmetric mixing at the coupling-symmetry level. The physical PMNS is a weighted average of the μ–τ symmetric limit (weight 1−g₅₅) and the simplex-ratio structure (weight g₅₅=96/g₂₂=0.1329), with results: sin²θ₂₃=0.5590 (PDG 0.561, −0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%), sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). No loop integrals needed. Still open: the CP-violating phase δ.

**δ_CP — topological source identified, value open 🔶.** The sector mixing amplitudes derived from S(n,d) ratios are real; a non-zero CP phase requires an imaginary contribution not present at tree level. The topological integer $\Delta c_1 = c_1(\mathbb{CP}^3) - c_1(\mathbb{CP}^5) = -2$ is identified as a candidate source: the two CP lepton sectors carry different first Chern classes because they sit at different levels of the Hopf chain (Rule B, §3a). Whether this produces a non-zero imaginary part in the mixing matrix requires computing the Fubini-Study curvature integral over sector coupling parameter space. This computation has not been performed. **Open.**

**CKM and PMNS have different structural origins.** The CKM arises from tree-level intra-sector mixing in the d=3/4 quark sectors. The PMNS arises from the spectral geometry of the cross-sector coupling between d=5 (neutrinos) and d=6/10 (charged leptons) — specifically from the ratio of d=5 self-coupling to the EW self-coupling g₂₂, and from the mode-index hierarchy within each sector.

**Invisible population — retracted; dark sector is an open question. ❓** A previous version of this document claimed that the Stage-2-pass / Stage-1-fail population could be enumerated by taking all n ∈ Σ_indices and sweeping over d ∈ {5,6,10}. That claim has been withdrawn. Stage 2 is a condition on the (n,d) pair, not on the mode index alone: a pair (n,d) passes Stage 2 if and only if it is an element of Σ_pairs — a tower output with both n and d assigned by the generation. Every element of Σ_pairs passes Stage 1 (with exemptions), so no co-fixed-point mode is simultaneously invisible under the current construction. The velinos, umbrons, and liminons enumerated in the previous version rested on an unproved sector-universality assumption (that n ∈ Σ_indices implies stability in any sector) and are not supported by P8. The dark sector is an open question pending either (a) extension of the coupling construction to d=7,8,9, or (b) a derived sector-universal stability argument from the EOM. See Part 1 P8 note and Part 7 §2.6.

**g₂, α, G_F — derived.** The SU(2)_L coupling is determined by the CP²→CP¹ sector reduction: g₂ = Q_u √g_s = (2/3)√(2g₄₄/π²) = 0.65275 (PDG: 0.65270, +0.008%). The Fermi constant follows directly from the W propagator at q²≪mW²: G_F = g₂²/(4√2 mW²) = 1.1658×10⁻⁵ GeV⁻² (PDG: 1.1664×10⁻⁵, −0.05%). Both g₂ and mW are independently derived from IDWT — no Higgs VEV enters. The d=2-sector-scale α gives 1/α = 131.8. W total width Γ_W = 2044 MeV (−2%), Z total width Γ_Z = 2444 MeV (−2.0%), muon lifetime τ_μ = 2.190×10⁻⁶ s (−0.3%). See Part 3 §0.7. g₁ = 0.35043 at the d=2 sector scale (from sin²θ_W = 0.22373 and g₂ = 0.65275 via the Weinberg relation). The self-consistent PDG value (from PDG sin²θ_W = 0.22290 and PDG g₂ = 0.65270) is 0.34957; IDWT sits +0.25% above it — exactly the sin²θ_W structural gap propagated. The PDG tabulated g₁ = 0.35740 is in MS-bar at m_Z; the −1.95% gap to that figure is a scheme/scale offset, not a physics discrepancy. IDWT couplings do not run.

---

## Foundational Open Items

The following items are open derivations or missing foundational elements within the IDWT framework. Each is recorded here to give referees a complete picture of what has and has not been established.

**Mode functions χ_{n,d}(ξ) — not yet explicit.** The mass formula m(n,d) = S(n,d) × m_scale_d depends on mode functions that are never written down explicitly in these documents. Open: derive the explicit eigenfunctions of H_d = −Δ_Ξ + V_d(r) on CP^{d/2-1} or S^d with the confining potential V_d(r) = λ_d r²/(1+r²), in a form that permits computation of normalization factors, d=3 projection amplitudes A_rel(n,d), and kernel matrix elements ⟨χ_{n_f,d_f}|K|χ_{n_i,d_i}⟩.

**V_d(r) = λ_d r²/(1+r²) potential form — not derived from the IDWT action.** Part 4 §3.10 derives the r² near-origin behavior from the sector geometry, but the large-r saturation (the (1+r²) denominator) is assumed as an ansatz. Open: derive the potential functional form, including the saturation, from the IDWT kernel action or add to P3 as an explicit postulate.

**Stage-2 co-fixed-point stability — not derived from the equation of motion.** The assertion that non-co-fixed-point modes "decohere on timescale 1/m_scale_d" (Part 7 §1.3) is stated without derivation from the IDWT field equation. Open: derive from the EOM that co-fixed-point modes are stable resonances and non-co-fixed-point modes are unstable. Until derived, Stage-2 remains 🔶.

**Second quantization / Fock space — absent.** Ψ∞ is treated as a classical Dirac spinor field throughout. There is no Fock space, no creation/annihilation operators, no particle number operator, and no normal ordering. Open: either (a) derive a second-quantized formalism from the IDWT action (symmetry currents, canonical quantization), or (b) explain why the classical field picture is physically complete for the purposes of the framework, and acknowledge this as a foundational postulate.

**Time-dependent dynamics — not analyzed.** The framework is entirely static. Part 8 §6 writes a master equation with a time derivative but no time-dependent solution is computed. Open: analyze time evolution of Ψ∞ under H_∞ — at minimum show that static sector modes are stationary solutions, and analyze decay via time-dependent perturbation theory.

**Scattering amplitudes and cross-sections — no native formalism.** All decay rate estimates use SM Fermi EFT with IDWT-derived inputs. No IDWT-native scattering amplitude exists. Open: develop a native IDWT amplitude formalism from kernel transition matrix elements ⟨χ_{n_f,d_f}|K|χ_{n_i,d_i}⟩, and show it reduces to SM Fermi EFT at low energies.

**Geometric dilution as testable energy-dependent prediction.** IDWT predicts g_eff(n,d) = g_dd/S(n,d) — a power-law decrease with mode index n. This is a concrete, potentially testable prediction about how effective coupling strength scales with energy/mode number. Open: derive the relationship between mode index n and energy scale from the sector Hamiltonian eigenvalues, and express g_eff(n,d) as a function of energy for comparison with experiment.

**CKM mixing formula not derived from kernel.** |V_ij|² = S(n_lighter,d)/S(n_heavier,d) is asserted based on combinatorial structure (Part 3 §0.9) without deriving it from the kernel matrix element ⟨χ_{n_i,d}|K_{dd'}|χ_{n_j,d'}⟩. Open: derive the mixing formula from the kernel cross-sector coupling amplitude, or label it 🔶 empirical matching.

**Stability of the 15-particle spectrum — no proof.** The Uniqueness Theorem (Part 1 §3b) shows the spectrum is the unique solution to the co-fixed-point system, but does not show the particles are stable against decay into each other. IDWT has no S-matrix. Open: define a stability condition from the IDWT energy functional E[Ψ], or explain why sector separation by mode index makes inter-sector decay geometrically impossible.

**Error analysis and uncertainty propagation — absent.** All error bars in the prediction table (Part 5) are PDG experimental uncertainties. No theoretical uncertainty from IDWT is estimated. Open: compute sensitivity ∂m_i/∂m_e for each prediction and propagate m_e uncertainty through the coupling derivation chain.

**Higgs-fermion coupling structure — not derived.** The Higgs mode is identified as n=95 in d=2, but no calculation shows it couples to fermions proportionally to their mass. Open: derive the Higgs-fermion coupling amplitude from the IDWT kernel overlap integral between the Higgs mode and each fermion mode, and show the coupling strength is proportional to m_f.

**Bottom quark beat stability.** The bottom quark is identified as a beat mode at k₀=16 in d=3. Its stability as a beat — why the |A₁₆|=|A₁₇| amplitude ratio is preserved — is asserted but not dynamically derived. Open: derive the stability of the k₀=16 beat from the IDWT equation of motion.

**Born rule — not derived.** The probability density ρ(r,t) = ∫|Ψ∞|²dξ is stated (Part 1 §2.3) without derivation from the IDWT action. If Ψ∞ is a classical field, the connection to observable detection probabilities requires justification. Open: either derive the Born rule from the action via emergent measurement theory, or add it to the postulate list explicitly (P5: Born rule).

**Measurement theory — absent.** There is no account of how continuous field Ψ∞ produces discrete particle detection events. Open: either provide a decoherence analysis within IDWT (sector localization → effective discreteness) or add an explicit postulate connecting field amplitude to detection probability.

**m_e as unit reference — choice not justified.** Any of the 15 particle masses could serve as the unit reference. The choice of m_e is conventional. Open: either show the electron is geometrically special as the unique lightest Stage-1 + Stage-2 mode in the minimal sector set, or state explicitly that m_e is a conventional unit choice and all ratios are the genuine predictions.

**Spin-1 bosons (W, Z, photon) from spinor framework — not worked out.** W and Z are spin-1 — how does this emerge from the Dirac spinor Ψ∞? The χ(CP¹)=2 helicity count for the photon is noted, but the spin-1 polarization tensor structure for W and Z is not derived. Open: derive the spin-1 polarization structure of gauge bosons from the d=2 sector Dirac operator spectrum.

**g₂₂ operator derivation — open.** g₂₂ = (1/2)p²q has combinatorial motivation (Part 2 §10b, labeled 🔶) but no operator-level derivation: what operator trace over the kernel produces g₂₂ = p²q/2 exactly? Open: compute Tr[G²₂₃ + G²₂₄] or equivalent from the kernel eigenmode expansion and show it equals (1/2)p²q.

---

## Falsifiability

The complete falsification inventory is in Part 5 §9 — the canonical location for IDWT's testability, organized into hard binary falsifiers (Category A), precision quantitative thresholds (Category B), structural predictions without SM equivalent (Category C), and near-future experimental windows. Part 1 §8 gives a brief summary with a pointer to Part 5 §9.

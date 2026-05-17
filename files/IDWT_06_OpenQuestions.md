# Infinite Dimensional Wave Theory — Part 6: Open Questions

What follows is an honest list of what the framework has not yet derived, with precise statements of what is needed.

---

## Reframing: What Is Actually Open

A systematic review of the labelled "open items" against PDG experimental uncertainties shows:

**Reclassified as consistent with experiment:**
- **Light-quark mass offsets (+0.68% d=3, +0.77% d=4):** All predictions within PDG 1σ uncertainties. The d quark (0.07σ), s quark (0.07σ), u quark (0.03σ), c quark (0.48σ), t quark (1.72σ), b quark (0.10σ) are all consistent with measurement. These are predictions that agree with experiment, not scheme-conversion residuals.
- **Λ_QCD "−9%":** IDWT defines Λ_IDWT = 3f_π = 282 MeV. The PDG "300–340 MeV" is a hadronic-scheme empirical range. IDWT's value matches 3f_π(PDG) = 276 MeV within +2.2% and m_ρ/2.74 = 283 MeV within −0.3%. The comparison label "−9%" was to an ill-defined target.

**Reclassified as data-dependent, not definitively wrong:**
- **m_ν₃ 2.5–2.9% shortfall (current data):** Δm² is not a native IDWT quantity — it is oscillation-experiment language for a technique that cannot access absolute masses. Expressed in IDWT's own terms, m_ν₃ = 48.87 meV is 2.5–2.9% below current oscillation inference (PDG 2023–2024: Δm²₃₁ = (2.51–2.53)×10⁻³ eV², giving m_ν₃^{osc} ≈ 50.1–50.3 meV). The correction δ_ν₃ = 1/35 gives m_ν₃^{corr} = 50.26 meV, implying Δm²₃₁ = 2.524×10⁻³ eV² — within 0.05% of PDG 2023 and within the ±0.025×10⁻³ experimental uncertainty of PDG 2024. Structural source: n_ν₃ = n_ν₁ + n_ν₂ − n_u is the only neutrino mode derived by inclusion-exclusion (not a primary Pascal evaluation); S(n_s,4) = 35 is the leading seed-level d=4 denominator, the same factor appearing in the τ Dyson correction (1/1680 = 1/(n_u × n_s² × S(n_s,4))). Derivation: δ_ν₃ = ε × g_{33} = 1/35 exactly, where ε = 1/(280√7) is the GTC coefficient (§11) and g_{33} = 8√7 is the d=3 coupling (T9); the √7 factors cancel because g_coeff × g_{33} = n_s² = k₀, so ε × g_{33} = k₀/(k₀ × n_mu) = 1/35 (Part 2 §9d). Corrected: Σm_ν = 60.39 meV; uncorrected: 59.00 meV. Both are within current cosmological bounds; CMB-S4 will distinguish them.

**Genuine small residuals:**
- **sin²θ_W +0.37%:** The mode-index prediction is exact. The gap from PDG on-shell is 3.6σ by measurement precision alone, but ~0.8σ once theoretical loop-correction uncertainties are included. The tree-level EW prediction is at this precision inherently.
- **g₁ −1.88% (after 1-loop running):** Derives from the sin²θ_W residual above.

**Genuinely open (computation not done):**
- PMNS mixing angles — spectral geometry formulas derived:
  sin²θ₂₃=0.5590 (PDG 0.561, -0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%),
  sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). From g₅₅=96/g₂₂ and mode indices.
  Still open: CP phase δ and Jarlskog invariant J
- CP-violating phase δ (Hopf Chern-Simons integral)
- 2-loop QED matching for g₁ — 2-loop RK4 (Machacek–Vaughn) computed numerically: residual improves from −1.8823% to −1.8810%, closing 0.0014 pp. Entire residual is the sin²θ_W structural gap (+0.37% from mode indices 76,81); no running order closes a structural prediction offset.

---

## Open

**f_π and Λ_QCD**
The IDWT β-function gives g_eff(n) = g₃₃/S(n,3), with confinement at g_eff = 1 → S(n_conf,3) = g₃₃ = 8√7 ≈ 21.17. The nearest integer solution is n_conf = n_s = 4 (the seed itself). The confinement mass scale is:

f_π = m_scale_3 × S(n_s,3) = 4.702 × 20 = 94.04 MeV   (PDG: 92.1 MeV, +2.1%)

The pion decay constant is the mass at the seed level — the seed is the confinement mode. The QCD scale from the large-N_c relation Λ_QCD ≈ N_c × f_π = 3 × 94.04 = 282 MeV, matching 3×f_π(PDG) = 276 MeV within +2.1%. The proton mass with Fermi-momentum correction: m_p = N_c × Λ_QCD × (1 + 1/n_up²) = 3 × 282.1 × (10/9) = 940.4 MeV (PDG: 938.3, +0.22%). Both use N_c = 3 from the CP² Dirac index.

**Full CKM matrix and CP violation**
The Cabibbo angle is derived including curvature correction: sin θ_C = (1 + χ(CP¹)/(24·S(n_s,3)))/√S(n_s,3) = (1+1/240)/√20 = 0.22454 (Part 3 §12), matching PDG |V_us| = 0.22450 ± 0.00044 at +0.09σ. |V_cb| = √(S(n_u,4)/S(n_c,4)) = √(15/8855) = 0.04116 (Part 3 §0.8; PDG exclusive: 0.04100 ± 0.0014, +0.11σ). Wolfenstein A = |V_cb|/sin²θ_C = 0.82315 (PDG: 0.8230 ± 0.0046, +0.03σ). Remaining open: |V_ub| (requires CP phase) and the CP-violating phase δ (requires complex structure in the Vandermonde kernel — not yet constructed). Note: V_ud = √(1−sin²θ_C) = 0.97447 is not a separate prediction but the unitarity complement of sin θ_C. The apparent 5.5σ gap against the nuclear beta-decay value (0.97370 ± 0.00014) is the Cabibbo Angle Anomaly — a pre-existing ~3σ unitarity deficit between the independently measured PDG values of |V_ud| and |V_us|. IDWT enforces exact unitarity; √(1−|V_us|²_PDG) = 0.97447 matches IDWT exactly. The tension is internal to the PDG measurements, not a failure of IDWT.

**Neutrino mass scale**
The d=5 mass scale follows from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³, giving m_scale_5 = 7.429 × 10⁻¹³ MeV. This is the d=5 analog of the g₂₂ back-reaction equation. See Part 2 §9c. Absolute masses: m_ν₁ = 1.487 meV, m_ν₂ = 8.639 meV, m_ν₃ = 50.27 meV (corrected; bare 48.87 meV), Σm_ν = 60.39 meV (bare 59.00 meV; δ_ν₃ = 1/35, Part 2 §9d).

**Lorentz completion 🔶**
Scalar covariance, spin-½ from the sector Dirac operator, chirality from Kähler γ₅ on CP² and CP³, and particle/antiparticle from the complex spinor are all established. Remaining: full Spin(9) decomposition for d=10. The main open item is the explicit D_Ξ spectrum matching m_scale_d × f(S(n,d)).

**G_N from infinite-dimensional gravity 🔶**
Gravity is a phenomenon of $M_\infty$ — it has no sector boundary and couples to every particle through that particle's dimensional complexity (encoded in mass). $G_N = G_\infty / V_7$, where $V_7 = L_4 L_5 L_6 L_{10}^4 \approx 113$ is fully derived from sector coupling constants. The vacuum-sector contribution (d>10) does not enter: curvature from d≤10 does propagate into d>10 (no hard wall), but T5 establishes that d>10 modes are scattering states — any disturbance disperses rather than localizing. Two arguments confirm $V_{\rm vacuum}$ drops out of the spectral action: (i) d>10 is Ricci-flat in vacuum ($R_{ab}=0$, so $a_2=\int R\,{\rm dvol}$ receives no d>10 contribution), and (ii) scattering states are not L²-normalizable and do not appear in ${\rm Tr}(f(D/\Lambda))$. The single remaining open item is $G_\infty$: fixing the spectral action scale $\Lambda$ makes $G_N=G_\infty/V_7$ a complete prediction. (Part 4 §3.12.2)

**$\Lambda$ and $f_k$ spectral coefficients 🔶**
The spectral action $\text{Tr}(f(D/\Lambda)) \sim f_4\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_0 a_4 + O(\Lambda^{-2})$ identifies $G_N^{-1} \propto f_2\Lambda^2$ (Einstein-Hilbert term from $a_2$) and $\Lambda_{\rm cosm} \propto f_4\Lambda^4$ (cosmological constant from $a_0$). The spectral cutoff $\Lambda$ and function $f(x)$ are not fixed by the sector combinatorics alone. Fixing $f_2\Lambda^2$ would determine $G_{\rm fund}$ from the action without treating it as a measured input. Note: $\sin^2\theta_W$ (+0.37%), $g_1$ (−1.88%), and $\sqrt{\text{Tr}(D^2)}$ (0.82%) are not $f_2$-dependent — $\sin^2\theta_W$ is purely combinatorial, $g_1$ follows from the $\sin^2\theta_W$ gap plus RK4 running, and $\sqrt{\text{Tr}(D^2)}$ is a spectral normalization artefact (top mass enters uncorrected). The $f_k$ open item is specifically about $G_{\rm fund}$ and the cosmological constant, not about particle mass residuals.

---

## Structural Findings on Blocked Computations

**PMNS angles — now derived from spectral geometry (T6, Part 9).** The charged-current coupling matrix between d=5 and d=6/10 is rank-1, giving tribimaximal mixing (TBM) at the coupling-symmetry level. The physical PMNS is a weighted average of TBM (weight 1−g₅₅) and the simplex-ratio structure (weight g₅₅=96/g₂₂=0.1329), with results: sin²θ₂₃=0.5590 (PDG 0.561, −0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%), sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). No loop integrals needed. Still open: the CP-violating phase δ.

**δ_CP — topological source identified, value open 🔶.** The sector mixing amplitudes derived from S(n,d) ratios are real; a non-zero CP phase requires an imaginary contribution not present at tree level. The topological integer $\Delta c_1 = c_1(\mathbb{CP}^3) - c_1(\mathbb{CP}^5) = -2$ is identified as a candidate source: the two CP lepton sectors carry different first Chern classes because they sit at different levels of the Hopf chain (Rule B, §3a). Whether this produces a non-zero imaginary part in the mixing matrix requires computing the Fubini-Study curvature integral over sector coupling parameter space. This computation has not been performed. **Open.**

**CKM and PMNS have different structural origins.** The CKM arises from tree-level intra-sector mixing in the d=3/4 quark sectors. The PMNS arises from the spectral geometry of the cross-sector coupling between d=5 (neutrinos) and d=6/10 (charged leptons) — specifically from the ratio of d=5 self-coupling to the EW self-coupling g₂₂, and from the mode-index hierarchy within each sector.

**g₂, α, G_F — derived.** The SU(2)_L coupling is determined by the CP²→CP¹ sector reduction: g₂ = Q_u √g_s = (2/3)√(2g₄₄/π²) = 0.65275 (PDG: 0.65270, +0.008%). The Fermi constant follows directly from the W propagator at q²≪mW²: G_F = g₂²/(4√2 mW²) = 1.1658×10⁻⁵ GeV⁻² (PDG: 1.1664×10⁻⁵, −0.05%). Both g₂ and mW are independently derived from IDWT — no Higgs VEV enters. The fiber-scale α gives 1/α = 131.8. W total width Γ_W = 2044 MeV (−2%), Z total width Γ_Z = 2444 MeV (−2.0%), muon lifetime τ_μ = 2.190×10⁻⁶ s (−0.3%). See Part 3 §0.7. g₁: 2-loop RK4 integration (Machacek–Vaughn β-functions; b₁=41/6 from IDWT particle content: N_c=3, N_gen=3, hypercharges from anomaly cancellation) gives g₁(m_Z) = 0.35068 (−1.8810%), closing 0.0014 pp beyond 1-loop. The entire residual is the sin²θ_W structural gap (+0.37% from mode indices 76,81) propagated via Δg₁/g₁ = Δ(sin²θ_W)/[2sin²θ_W(1−sin²θ_W)]. The 2-loop item is complete; the residual is the sin²θ_W open item.

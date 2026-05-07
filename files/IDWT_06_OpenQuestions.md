# IDWT — Part 6: Open Questions

What follows is an honest list of what the framework has not yet derived, with precise statements of what is needed.

---

## Closed

| What | How |
|---|---|
| Seeds {1,4} uniqueness | S(n,4)=35 has unique solution n=4; n=1 forced by S(1,d)=1 for all d |
| Eigenmode selection rule | n_lepton = n_neutrino + n_quark, all three generations exact |
| Tau mode index | n_τ = n_ν₃ + n_down = 23; the eigenmode selection rule applied at d=10 (CP⁵), cross-coupled to d=3 via the Vandermonde rule g(d=10, n_s=4) = 13 = n_e |
| Bottom quark mass | Quartic bifurcation at k₀ = n_strange² within d=3, +0.02% |
| Coupling constants from seeds | g₃₃ = n_s²√(n_s+n_u)/2, g₄₄ = n_sn_u/√(n_s+n_u), g₃₄ = √(n_s³n_u/2) — all from seed n_s; n_u = n_s−1 derived. Universal coupling coefficient 2/√(n_s+n_u) applies to both sectors by binomial symmetry C(n,k)=C(n,n-k). g₃₃ and g₄₄ are symmetric derivations; neither is primary. g₃₃×g₄₄ = n_s³n_u/2 = 96 is a theorem of the seed structure. |
| Sector scale hierarchy | m_scale_3 = m_e × √(g₃₃/g₆₆) = 4.702 MeV from the kernel vacuum fixed-point equation (l=0 scalar part of the cross-sector coupling). Requires only m_e and coupling constants derived from seeds and anomaly cancellation. All other sector scales follow from m_scale_3 or m_W. |
| ρ meson from comb filter | Im[Γ₃₄₆] maximum at 775.794 MeV (+0.069% vs PDG 775.260 MeV). Inputs: g₃₃=8√7, g₄₄=12/√7, g₆₆=1/4, τ_d=1/(2√(k₀+d)) at k₀=16. Consistency check — the same coupling constants that fix m_scale_3 also determine this peak, so agreement is a self-consistency verification. The +0.069% is a consistency-level residual: WKB correction to τ_d for d=3 goes in the wrong direction, and is zero for d=10 by the Gegenbauer criticality theorem. |
| Hilbert space rigour | Absolute convergence proved; operators self-adjoint |
| Spectral independence | Occupied set is sum-free with no S-value degeneracy. Proved computationally for all 91 pairs; d=3 internal case proved analytically via non-tetrahedral-number argument; tau dominance algebraic; sector scale gaps structural from {1,4} seeds |
| Spin-½ from KK Dirac | The 3+1D Dirac equation follows from the Kaluza-Klein Dirac operator on M_∞ = ℝ^{3,1} × Ξ_d. Spin-½ is derived from the spinor bundle of Ψ∞, not postulated per particle. |
| S(n,d) geometric grounding | S(n,d) = dim Sym^{n-1}(ℝ^{d+1}) = IDOS_d(n): the cumulative count of harmonic oscillator eigenstates at levels 0 through n−1 in d dimensions. Mass equals frequency equals microstate count. Mass = frequency = cumulative microstate count. All three are the same quantity. |
| Top quark and W boson derivation | n_ν₂ = S(n_u,4) = C(6,4) = 15 = C(6,2) = S(n_s+1,2) by binomial symmetry C(n,k)=C(n,n-k), where n_u+3 = n_s+2 = 6 follows from n_u = n_s−1. Therefore n_W = S(n_e,2) − n_ν₂ = 76, and g(d=5, n_top) = 76 forces n_top = 72 uniquely. |
| Three k₀ resonance conditions | k₀ = n_s² = n_e+n_u = S(n_s,3)−S(2,3) = 16. Three independent expressions equal k₀ simultaneously: (1) seed self-product, (2) cross-sector lepton+quark mode sum, (3) intra-d=3 gap identity from the g₃₃ derivation. All three add in phase at k₀, destabilising the single-mode solution and forcing the geometric-mean beat at m_b = √(S(16,3)×S(17,3)) × m_scale_3 = 4181 MeV (+0.02%). |
| Generation Tower Correction (GTC) | ε = g_coeff/(k₀ × n_mu) = (2/√7)/(16×35) = 1/(280√7) = 0.001350. Derived from: g_coeff = 2/√(n_s+n_u) (universal Jacobi coefficient), k₀ = n_s² (vacuum stability gap), n_mu = S(n_s,4) (fixed-point mode scale). Corrects c/u to 0.000% and t/u to −0.048%. Note k_charm = k_g33 = n_s−1 = 3: the same comb filtration stages that select the charm mode index also determine the coupling gap k₀. |
| d=5 coupling g₅₅ (algebraic structure) | Hopf fiber universality: both S¹→S³→CP¹ and S¹→S⁵→CP² share the electromagnetic U(1) fiber. Universality requires v₃/v₂ = v₅/v₄, giving g₂₅ = g₃₄ = 4√6 and g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂ = 0.1329. g₂₂ = (M₃^{S³}−n_u)²×β/2 = 722.5 is a Dirac multiplicity product (Theorem S3, Part 8 §60b). g₅₅ = 96/722.5 then follows with no new input. Complete coupling vector: {v₂=26.879, v₃=4.601, v₄=2.130, v₅=0.3645, v₆=v₁₀=0.500}. Neutrino mass scale derived (§9c). |
| Tau mass residual — Dyson resummation | The d=6 and d=10 sectors are isotropically coupled: g_{6,6} = g_{6,10} = g_{10,10} = 1/n_s = 1/4 exactly (all equal: d=6 and d=10 share the seed coupling). The d=6→d=10 back-reaction correction feeds back on itself via g_{10,10}, giving a self-consistent equation: Δm = ε_{6→10}×m_τ + g_{10,10}×Δm → Δm = ε_{6→10}×m_τ/(1−g_{10,10}). Since g_{10,10} = 1/n_s, the resummation factor is 1/(1−1/n_s) = n_s/(n_s−1) = n_s/n_u (forced by n_u = n_s−1). Result: ε_total = 1/(n_u × n_s² × S(n_s,4)) = 1/1680. Correction +m_τ/1680 = +1.057 MeV. **m_τ = 1776.84 MeV (−0.14σ from PDG = 1776.86 ± 0.12 MeV). Inside 1σ.** No new inputs: m_e only. |
| d=10 Gegenbauer uniqueness | The Gegenbauer coupling at the seed resonance site b_{k₀}(d) = √(k₀(k₀+d−1))/(2k₀+d−2) satisfies b_{k₀}=1/2 if and only if 4k₀=(d−2)², i.e. d=2+2√k₀=2(n_s+1)=10. This is a second independent algebraic derivation of d=10 (the first being Hurwitz; the third being hypercharge anomaly cancellation). d=10 is the last sector with b_{k₀}≥1/2; d>10 is evanescent. Proved: 4×16=64=(10−2)². As a WKB corollary: the next-order correction to τ_{d=10} vanishes identically (since it is proportional to b_{k₀}−1/2=0), making d=10 the only sector for which the leading-order WKB delay is exact. |
| **Sector set D forced by seed** | n_top = 72 = N_c × n_s × N_f where N_c=3 (spin^c index), n_s=4 (seed), N_f=6 (= n_top/(N_c n_s)); the three CP sectors d=4,6,10 follow as d=2(N_c-1), 2(n_s-1), 2(N_f-1); d=2 is the Hopf base; d=3,5 are Hopf total spaces with derivable couplings. g₆₆=1/n_s=1/4 is from the seed, not from external hypercharge. (Part 1 §3a) |
| **Particle spectrum complete** | Every potential new particle requires either a new sector (excluded by §3a) or a new mode index consistent with the eigenmode selection rule (excluded by §5c uniqueness). The only beat mode is at k₀=16 in d=3 — uniquely verified by exhaustive search. No additional stable states exist. (Part 1 §3b) |
| **CKM unitarity exact at tree level** | |Vud|²+|Vus|²+|Vub|² = 1 exactly at tree level (since Vud=√(1−Vus²), Vub=0). The literature +5.5σ tension is in the nuclear-QED-corrected extracted value, not in the bare IDWT coupling. The nuclear β-decay QED correction δ_R ≈ 0.024 is external to IDWT. IDWT satisfies exact CKM unitarity. |
| Dirac neutrino prediction | The Clifford algebra Cl(d) has Bott periodicity 8. For d=5, d mod 8 = 5, which is the unique residue class for which Majorana spinors do not exist. The d=5 hidden-space spinor cannot support a Majorana mass term — no seesaw mechanism is possible from the hidden-space geometry. IDWT therefore predicts: **neutrinos are Dirac fermions.** Falsifiable by neutrinoless double beta decay (0νββ); no signal is expected ever. |
| Spin(10) weight lattice cross-check for d=10 | The d=10 sector admits a Majorana-Weyl spinor (d mod 8 = 2). Its 16-component Weyl spinor is exactly the **16** of SO(10) ≅ Spin(10), which under the SM subgroup decomposes as Q_L + u_R^c + e_R^c + d_R^c + L_L + ν_R^c — one complete SM generation including right-handed neutrino. The tau, ν_τ, b, and t all live in the same SO(10) multiplet. Their hypercharges Y = {−1, 0, −1/3, +2/3} follow from the SO(10) algebra, not from separate SM assignments. |
| Chirality from Kähler γ₅ | The CP^m sectors (d=2m, so d=2,4,6) carry a Kähler form ω. The operator γ₅^Kähler = i^m (ω^m)_{a₁…a_{2m}} γ^{a₁}⋯γ^{a_{2m}} splits each sector spinor into LEFT (holomorphic) + RIGHT (anti-holomorphic). For d=4 (CP², m=2): 4-spinor = 2L + 2R → (u_L,d_L) + (u_R,d_R). For d=6 (CP³, m=3): 8-spinor = 4L + 4R → two lepton doublets + right-handed partners. The W boson couples only to the LEFT components. |

---

---

## Reframing: What Is Actually Open

A systematic review of the labelled "open items" against PDG experimental uncertainties shows:

**Reclassified as consistent with experiment:**
- **Light-quark mass offsets (+0.68% d=3, +0.77% d=4):** All predictions within PDG 1σ uncertainties. The d quark (0.07σ), s quark (0.07σ), u quark (0.03σ), c quark (0.48σ), t quark (1.72σ), b quark (0.10σ) are all consistent with measurement. These are predictions that agree with experiment, not scheme-conversion residuals.
- **Λ_QCD "−9%":** IDWT defines Λ_IDWT = 3f_π = 282 MeV. The PDG "300–340 MeV" is a hadronic-scheme empirical range. IDWT's value matches 3f_π(PDG) = 276 MeV within +2.2% and m_ρ/2.74 = 283 MeV within −0.3%. The comparison label "−9%" was to an ill-defined target.

**Reclassified as data-dependent, not definitively wrong:**
- **Δm²₃₁ "−7.7%":** Different oscillation analyses give: PDG 2022: −7.7%; NuFit 5.2: −5.5%; T2K+NOvA 2020: −2.7%. IDWT sits at the low end of the experimental range. The mode indices fix this prediction exactly (n_ν₃=22); whether it is inside or outside the experimental range depends on which analysis is used.

**Genuine small residuals:**
- **sin²θ_W +0.37%:** The mode-index prediction is exact. The gap from PDG on-shell is 3.6σ by measurement precision alone, but ~0.8σ once theoretical loop-correction uncertainties are included. The tree-level EW prediction is at this precision inherently.
- **g₁ −1.88% (after 1-loop running):** Derives from the sin²θ_W residual above.

**Genuinely open (computation not done):**
- ~~PMNS mixing angles~~ **CLOSED** — spectral geometry formulas derived:
  sin²θ₂₃=0.5590 (PDG 0.561, -0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%),
  sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). From g₅₅=96/g₂₂ and mode indices.
  Still open: CP phase δ and Jarlskog invariant J
- CP-violating phase δ (Hopf Chern-Simons integral)
- Gravity hierarchy M_∞/m_e ~ 4.8×10²¹
- 2-loop QED matching for g₁

---

## Open

**f_π and Λ_QCD ✅/🔶**
The IDWT β-function gives g_eff(n) = g₃₃/S(n,3), with confinement at g_eff = 1 → S(n_conf,3) = g₃₃ = 8√7 ≈ 21.17. The nearest integer solution is n_conf = n_s = 4 (the seed itself). The confinement mass scale is:

f_π = m_scale_3 × S(n_s,3) = 4.702 × 20 = 94.04 MeV   (PDG: 92.1 MeV, +2.1% ✅)

The pion decay constant is the mass at the seed level — the seed is the confinement mode. The QCD scale from the large-N_c relation Λ_QCD ≈ N_c × f_π = 3 × 94.04 = 282 MeV (PDG hadronic scheme: 300–340 MeV, −9% 🔶). The proton mass from the same relation m_p = N_c × Λ_QCD = 930.9 MeV (PDG: 938.3, −0.78% ✅). Both use N_c = 3 from the CP² Dirac index. The connection between N_tot = 66 (the 66-factor formula giving 310 MeV) and the β-function integral has not been derived.

**Full CKM matrix and CP violation**
The Cabibbo angle is derived including curvature correction: sin θ_C = (1 + χ(CP¹)/(24·S(n_s,3)))/√S(n_s,3) = (1+1/240)/√20 = 0.22454 (Part 3 §12), matching PDG |V_us| = 0.22450 ± 0.00044 at +0.09σ. |V_cb| = √(S(n_u,4)/S(n_c,4)) = √(15/8855) = 0.04116 (Part 3 §0.8; PDG exclusive: 0.04100 ± 0.0014, +0.11σ). Wolfenstein A = |V_cb|/sin²θ_C = 0.82315 (PDG: 0.8230 ± 0.0046, +0.03σ). Remaining open: |V_ub| (requires CP phase) and the CP-violating phase δ (requires complex structure in the Vandermonde kernel — not yet constructed). The |V_ud| tension is resolved: IDWT predicts the bare coupling |V_ud|_bare = √(1−sin²θ_C) = 0.97447, giving exact CKM unitarity. The nuclear β-decay extraction applies QED corrections δ_R ≈ 0.024 before reporting; that correction is external to IDWT, not a framework prediction. See Closed table.

**Neutrino mass scale (resolved ✅)**
The d=5 mass scale follows from the cross-sector fixed point m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³, giving m_scale_5 = 7.429 × 10⁻¹³ MeV. This is the d=5 analog of the g₂₂ back-reaction equation. See Part 2 §9c. Absolute masses: m_ν₁ = 1.487 meV, m_ν₂ = 8.639 meV, m_ν₃ = 48.87 meV, Σm_ν = 59.0 meV.

**Lorentz completion 🔶**
Scalar covariance, spin-½ from the KK Dirac operator, chirality from Kähler γ₅ on CP² and CP³, and particle/antiparticle from the complex spinor are all established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure. The main open item is the explicit D_Ξ spectrum matching m_scale_d × f(S(n,d)).

**4D gravity from M_∞ action ✅ (complete)**
The gravity programme is complete. Proved: 4D Einstein equations from the M_∞ action (§3.1–3.4), no hidden gravitational propagating modes (§3.4), equivalence principle m_grav = m_inertial (§3.6), L²(Ξ) normalisability (§3.8 Part I), Bianchi identity ∇^μ T_μν^{eff} = 0 (§3.8 Part II), spectral counting S(n,d) = N_d(n−1) (§60), sector localization lengths L_d from Agmon theory (§3.9), sector potential depth λ_d = (g_dd/2)^{2/3} from kernel self-consistency (§3.10), G_eff = 1/(8π M_∞²) sector-independent (§3.11.1), and G_eff is loop-exact — hidden sector loops cannot renormalise M_∞² because the Ξ operator O_Ξ is independent of g_μν by the product metric structure of M_∞ = M₄ × Ξ (§3.11.3). The hierarchy M_∞ >> m_e is the remaining open item in a different category — it is the IDWT form of the hierarchy problem, not a gap in the gravitational framework.


---

## Structural Findings on Blocked Computations

**PMNS angles — now derived from spectral geometry (T6, Part 9).** The charged-current coupling matrix between d=5 and d=6/10 is rank-1, giving tribimaximal mixing (TBM) at the coupling-symmetry level. The physical PMNS is a weighted average of TBM (weight 1−g₅₅) and the mode-amplitude structure (weight g₅₅=96/g₂₂=0.1329), with results: sin²θ₂₃=0.5590 (PDG 0.561, −0.36%), sin²θ₁₂=0.3086 (PDG 0.307, +0.51%), sin²θ₁₃=0.02211 (PDG 0.022, +0.51%). No loop integrals needed. Still open: the CP-violating phase δ, which requires the Berry phase curvature integral around the lepton sector loop d=5→6→10→5.

**CKM and PMNS have different structural origins.** The CKM arises from tree-level intra-sector mixing in the d=3/4 quark sectors. The PMNS arises from the spectral geometry of the cross-sector coupling between d=5 (neutrinos) and d=6/10 (charged leptons) — specifically from the ratio of d=5 self-coupling to the EW self-coupling g₂₂, and from the mode-index hierarchy within each sector.

**g₂, α, G_F — now derived ✅.** The SU(2)_L coupling is determined by the CP²→CP¹ sector reduction: g₂ = Q_u √g_s = (2/3)√(2g₄₄/π²) = 0.65275 (PDG: 0.65270, +0.008%). The Fermi constant follows directly from the W propagator at q²≪mW²: G_F = g₂²/(4√2 mW²) = 1.1658×10⁻⁵ GeV⁻² (PDG: 1.1664×10⁻⁵, −0.05%). Both g₂ and mW are independently derived from IDWT — no Higgs VEV enters. The fiber-scale α gives 1/α = 131.8; after hadronic vacuum polarisation (≈3.8 units) between m_W and m_Z, the running gives 1/α(m_Z) ≈ 127.9 (PDG: 127.9). W total width Γ_W = 2044 MeV (−2%), Z total width Γ_Z = 2444 MeV (−2.0%), muon lifetime τ_μ = 2.190×10⁻⁶ s (−0.3%). See Part 3 §0.7. Open: g₁ has −1.88% residual after 1-loop U(1)_Y running to m_Z. The remaining gap requires 2-loop QED matching between the IDWT fiber scheme and MS-bar.

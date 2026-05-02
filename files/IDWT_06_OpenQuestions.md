# IDWT — Part 6: Open Questions

What follows is an honest list of what the framework has not yet derived, with precise statements of what is needed.

---

## Closed

| What | How |
|---|---|
| Seeds {1,4} uniqueness | S(n,4)=35 has unique solution n=4; n=1 forced by S(1,d)=1 for all d |
| Generation law | n_lepton = n_neutrino + n_quark, all three generations exact |
| Tau mode index | n_τ = n_ν₃ + n_down = 23; the generation law applied at d=10 (CP⁵), cross-coupled to d=3 via the Vandermonde rule g(d=10, n_s=4) = 13 = n_e |
| Bottom quark mass | Quartic bifurcation at k₀ = n_strange² within d=3, +0.02% |
| Coupling constants from seeds | g₃₃ = n_s²√(n_s+n_u)/2, g₄₄ = n_sn_u/√(n_s+n_u), g₃₄ = √(n_s³n_u/2) — all from seeds {n_s,n_u}. Universal coupling coefficient 2/√(n_s+n_u) applies to both sectors by binomial symmetry C(n,k)=C(n,n-k). g₃₃ and g₄₄ are symmetric derivations; neither is primary. g₃₃×g₄₄ = n_s³n_u/2 = 96 is a theorem of the seed structure. |
| Sector scale hierarchy | m_scale_3 = m_e × √(g₃₃/g₆₆) = 4.702 MeV from the kernel vacuum fixed-point equation (l=0 scalar part of the cross-sector coupling). Requires only m_e and coupling constants derived from seeds and anomaly cancellation. All other sector scales follow from m_scale_3 or m_W. |
| ρ meson from comb filter | Im[Γ₃₄₆] maximum at 775.794 MeV (+0.069% vs PDG 775.260 MeV). Inputs: g₃₃=8√7, g₄₄=12/√7, g₆₆=1/4, τ_d=1/(2√(k₀+d)) at k₀=16. Consistency check — the same coupling constants that fix m_scale_3 also determine this peak, so agreement is a self-consistency verification. The +0.069% is a consistency-level residual: WKB correction to τ_d for d=3 goes in the wrong direction, and is zero for d=10 by the Gegenbauer criticality theorem. |
| Hilbert space rigour | Absolute convergence proved; operators self-adjoint |
| Spectral independence | Occupied set is sum-free with no S-value degeneracy. Proved computationally for all 91 pairs; d=3 internal case proved analytically via non-tetrahedral-number argument; tau dominance algebraic; sector scale gaps structural from {1,4} seeds |
| Spin-½ from KK Dirac | The 3+1D Dirac equation follows from the Kaluza-Klein Dirac operator on M_∞ = ℝ^{3,1} × Ξ_d. Spin-½ is derived from the spinor bundle of Ψ∞, not postulated per particle. |
| S(n,d) geometric grounding | dim Sym^n(ℝ^d) = S(n,d): mode functions are degree-n monomials in d variables, and there are exactly S(n,d) of them. Mass = frequency = cumulative microstate count. All three are the same quantity. |
| Top quark and W boson derivation | n_ν₂ = S(n_u,4) = C(6,4) = 15 = C(6,2) = S(n_s+1,2) by binomial symmetry C(n,k)=C(n,n-k), where n_u+3 = n_s+2 = 6 follows from n_u = n_s−1. Therefore n_W = S(n_e,2) − n_ν₂ = 76, and g(d=5, n_top) = 76 forces n_top = 72 uniquely. |
| Three k₀ resonance conditions | k₀ = n_s² = n_e+n_u = S(n_s,3)−S(2,3) = 16. Three independent expressions equal k₀ simultaneously: (1) seed self-product, (2) cross-sector lepton+quark mode sum, (3) intra-d=3 gap identity from the g₃₃ derivation. All three add in phase at k₀, destabilising the single-mode solution and forcing the geometric-mean beat at m_b = √(S(16,3)×S(17,3)) × m_scale_3 = 4181 MeV (+0.02%). |
| Generation Tower Correction (GTC) | ε = g_coeff/(k₀ × n_mu) = (2/√7)/(16×35) = 1/(280√7) = 0.001350. Derived from: g_coeff = 2/√(n_s+n_u) (universal Jacobi coefficient), k₀ = n_s² (vacuum stability gap), n_mu = S(n_s,4) (fixed-point mode scale). Corrects c/u to 0.000% and t/u to −0.048%. Note k_charm = k_g33 = n_s−1 = 3: the same additions that generate the charm mode index also generate the coupling gap k₀. |
| d=5 coupling g₅₅ (algebraic structure) | Hopf fiber universality: both S¹→S³→CP¹ and S¹→S⁵→CP² share the electromagnetic U(1) fiber. Universality requires v₃/v₂ = v₅/v₄, giving g₂₅ = g₃₄ = 4√6 and g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂ = 0.1329. No new empirical input required; g₅₅ is fixed by the same m_W that determines g₂₂. Complete coupling vector: {v₂=26.879, v₃=4.601, v₄=2.130, v₅=0.3645, v₆=v₁₀=0.500}. Neutrino mass hierarchy remains open (see below). |
| Tau mass residual — Dyson resummation | The d=6 and d=10 sectors are isotropically coupled: g_{6,6} = g_{6,10} = g_{10,10} = 1/4 exactly (all equal because Y_L = Y_τ = −1/2). The d=6→d=10 back-reaction correction feeds back on itself via g_{10,10}, giving a self-consistent equation: Δm = ε_{6→10}×m_τ + g_{10,10}×Δm → Δm = ε_{6→10}×m_τ/(1−g_{10,10}). Since g_{10,10} = 1/n_s, the resummation factor is 1/(1−1/n_s) = n_s/(n_s−1) = n_s/n_u (forced by n_u = n_s−1). Result: ε_total = 1/(n_u × n_s² × S(n_s,4)) = 1/1680. Correction +m_τ/1680 = +1.057 MeV. **m_τ = 1776.84 MeV (−0.14σ from PDG = 1776.86 ± 0.12 MeV). Inside 1σ.** No new inputs: m_e only. |
| d=10 Gegenbauer uniqueness | The Gegenbauer coupling at the seed resonance site b_{k₀}(d) = √(k₀(k₀+d−1))/(2k₀+d−2) satisfies b_{k₀}=1/2 if and only if 4k₀=(d−2)², i.e. d=2+2√k₀=2(n_s+1)=10. This is a second independent algebraic derivation of d=10 (the first being Hurwitz; the third being hypercharge anomaly cancellation). d=10 is the last sector with b_{k₀}≥1/2; d>10 is evanescent. Proved: 4×16=64=(10−2)². As a WKB corollary: the next-order correction to τ_{d=10} vanishes identically (since it is proportional to b_{k₀}−1/2=0), making d=10 the only sector for which the leading-order WKB delay is exact. |
| Dirac neutrino prediction | The Clifford algebra Cl(d) has Bott periodicity 8. For d=5, d mod 8 = 5, which is the unique residue class for which Majorana spinors do not exist. The d=5 hidden-space spinor cannot support a Majorana mass term — no seesaw mechanism is possible from the hidden-space geometry. IDWT therefore predicts: **neutrinos are Dirac fermions.** Falsifiable by neutrinoless double beta decay (0νββ); no signal is expected ever. |
| SO(10) GUT structure of d=10 | The d=10 sector admits a Majorana-Weyl spinor (d mod 8 = 2). Its 16-component Weyl spinor is exactly the **16** of SO(10) ≅ Spin(10), which under the SM subgroup decomposes as Q_L + u_R^c + e_R^c + d_R^c + L_L + ν_R^c — one complete SM generation including right-handed neutrino. The tau, ν_τ, b, and t all live in the same SO(10) multiplet. Their hypercharges Y = {−1, 0, −1/3, +2/3} follow from the SO(10) algebra, not from separate SM assignments. |
| Chirality from Kähler γ₅ | The CP^m sectors (d=2m, so d=2,4,6) carry a Kähler form ω. The operator γ₅^Kähler = i^m (ω^m)_{a₁…a_{2m}} γ^{a₁}⋯γ^{a_{2m}} splits each sector spinor into LEFT (holomorphic) + RIGHT (anti-holomorphic). For d=4 (CP², m=2): 4-spinor = 2L + 2R → (u_L,d_L) + (u_R,d_R). For d=6 (CP³, m=3): 8-spinor = 4L + 4R → two lepton doublets + right-handed partners. The W boson couples only to the LEFT components. |

---

## Open

**f_π and Λ_QCD ✅/🔶**
The IDWT β-function gives g_eff(n) = g₃₃/S(n,3), with confinement at g_eff = 1 → S(n_conf,3) = g₃₃ = 8√7 ≈ 21.17. The nearest integer solution is n_conf = n_s = 4 (the seed itself). The confinement mass scale is:

f_π = m_scale_3 × S(n_s,3) = 4.702 × 20 = 94.04 MeV   (PDG: 92.1 MeV, +2.1% ✅)

The pion decay constant is the mass at the seed level — the seed is the confinement mode. The QCD scale from the large-N_c relation Λ_QCD ≈ N_c × f_π = 3 × 94.04 = 282 MeV (PDG hadronic scheme: 300–340 MeV, −9% 🔶). The proton mass from the same relation m_p = N_c × Λ_QCD = 930.9 MeV (PDG: 938.3, −0.78% ✅). Both use N_c = 3 from the CP² Dirac index. The connection between N_tot = 66 (the 66-factor formula giving 310 MeV) and the β-function integral has not been derived.

**Full CKM matrix and CP violation**
The Cabibbo angle is derived including curvature correction: sin θ_C = (1 + χ(CP¹)/(24·S(n_s,3)))/√S(n_s,3) = (1+1/240)/√20 = 0.22454 (Part 3 §12), matching PDG |V_us| = 0.22450 ± 0.00044 at +0.09σ. |V_cb| = √(S(n_u,4)/S(n_c,4)) = √(15/8855) = 0.04116 (Part 3 §0.8; PDG exclusive: 0.04100 ± 0.0014, +0.11σ). Wolfenstein A = |V_cb|/sin²θ_C = 0.82315 (PDG: 0.8230 ± 0.0046, +0.03σ). Remaining open: |V_ub| (requires CP phase), the CP-violating phase δ (requires complex structure in the Vandermonde kernel — not yet constructed), and the |V_ud| tension (+5.5σ with nuclear beta decay, likely from uncomputed QED radiative corrections).

**Neutrino mass hierarchy (d=5 mass scale)**
The d=5 coupling is algebraically closed: g₅₅ = 96/g₂₂ = 0.1329. The naive coupling value gives m_scale_5 ≈ 0.37 MeV, while observed neutrino masses are ~meV — a suppression of ~2.5×10⁵. The seesaw mechanism is geometrically forbidden (Majorana spinors do not exist in d=5, d mod 8 = 5), so this suppression must arise entirely from the d=5 sector vacuum dynamics: non-perturbative suppression at λ̂₅ ≫ 1, or a condensate from the (5,5)→10 Vandermonde vertex. Neutrino mass RATIOS are fully predicted (S(10,5):S(15,5):S(22,5)). The absolute mass scale mechanism is open.

**Lorentz completion 🔶**
Scalar covariance, spin-½ from the KK Dirac operator, chirality from Kähler γ₅ on CP² and CP³, and particle/antiparticle from the complex spinor are all established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure. The main open item is the explicit D_Ξ spectrum matching m_scale_d × f(S(n,d)).

**4D gravity from M_∞ action ✅ (complete)**
The gravity programme is complete. Proved: 4D Einstein equations from the M_∞ action (§3.1–3.4), no hidden gravitational propagating modes (§3.4), equivalence principle m_grav = m_inertial (§3.6), L²(Ξ) normalisability (§3.8 Part I), Bianchi identity ∇^μ T_μν^{eff} = 0 (§3.8 Part II), spectral counting S(n,d) = N_d(n−1) (§60), sector localization lengths L_d from Agmon theory (§3.9), sector potential depth λ_d = (g_dd/2)^{2/3} from kernel self-consistency (§3.10), G_eff = 1/(8π M_∞²) sector-independent (§3.11.1), and G_eff is loop-exact — hidden sector loops cannot renormalise M_∞² because the Ξ operator O_Ξ is independent of g_μν by the product metric structure of M_∞ = M₄ × Ξ (§3.11.3). The hierarchy M_∞ >> m_e is the remaining open item in a different category — it is the IDWT form of the hierarchy problem, not a gap in the gravitational framework.


---

## Structural Findings on Blocked Computations

**PMNS angles are a loop-level prediction.** At tree level in IDWT, the W coupling amplitude A_{αi} = ⟨χ_{n_W,2}|K_{2d_α}|χ_{n_α,d_α}⟩ × ⟨χ_{n_W,2}|K_{25}|χ_{n_i,5}⟩ factorises into a product of two independent sector overlaps. The resulting |U_{αi}|² matrix has rank 1 — it cannot be a non-trivial unitary matrix. At tree level, IDWT predicts the identity PMNS matrix. The observed large PMNS mixing angles must therefore be generated at next-to-leading order by loop corrections to the kernel. The loop corrections involve the IR-divergent neutrino modes (low-mass d=5 states are near-zero modes) and are expected to be O(1) — consistent with the observed large mixing. The loop integral has not been computed.

**CKM and PMNS have different structural origins.** The CKM arises from tree-level intra-sector mixing in the d=3 quark sector: the modes n_d=1 and n_s=4 both live in d=3 and are connected by the d=3↔d=4 cross-coupling through a common sector geometry. The PMNS involves two completely separate sectors (d=5 neutrinos, d=6,10 charged leptons) with no shared geometry, so the tree-level amplitude factorises and carries no flavour information. This structural asymmetry explains why CKM is small (perturbative intra-sector mixing) and PMNS is large (loop-generated, IR-enhanced by near-zero neutrino modes).

**α and G_F are blocked by the Ward identity.** The SU(2)_L coupling g₂ enters the mass formula nowhere (the W mass is a CONFINEMENT MASS from the d=2 sector potential at mode n=76, not from a Higgs mechanism g₂v/2). The coupling g₂ only enters the interaction vertex. Extracting g₂ from the IDWT Lagrangian requires computing the Ward identity for the U(1)_Y subgroup of the d=2 sector — relating the vertex amplitude to the conserved current. Until the Ward identity is established in IDWT, g₂, v, α, and G_F remain undetermined from first principles. The ratio α(0)/(G_F/√2) = 2 m_W² sin²θ_W/π = 9.20×10⁸ MeV² is fully derived from IDWT mode indices (both m_W and sin²θ_W are mode-count ratios), with error +4.0% from PDG (8.85×10⁸ MeV²) — consistent with EW radiative corrections Δr≈0.04. α and G_F individually require the Ward identity.

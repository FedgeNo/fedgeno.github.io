# IDWT — Part 6: Open Questions

What follows is an honest list of what the framework has not yet derived, with precise statements of what is needed.

---

## Closed

| What | How |
|---|---|
| Seeds {1,4} uniqueness | S(n,4)=35 has unique solution n=4; n=1 forced by S(1,d)=1 for all d |
| Generation law | n_lepton = n_neutrino + n_quark, all three generations exact |
| Tau mode (OQ28) | n_τ = n_ν₃ + n_down = 23, octonionic Hopf coupling to d=3 |
| Bottom quark mass (OQ30a) | Quartic bifurcation at k₀ = n_strange² within d=3, +0.02% |
| Exact coupling constants (OQ30b) | g₃₃ = n_s²√(n_s+n_u)/2, g₄₄ = n_sn_u/√(n_s+n_u), g₃₄ = √(n_s³n_u/2) — all from seeds {n_s,n_u}. Universal coupling coefficient 2/√(n_s+n_u) applies to both sectors by OQ26 binomial symmetry. g₃₃ and g₄₄ are symmetric derivations; neither is primary. g₃₃×g₄₄ = n_s³n_u/2 = 96 is a theorem of the seed structure. |
| Scale hierarchy (OQ17) | m_scale_3 from comb filter beat = ρ meson mass |
| ρ meson from comb filter (OQ35) | Im[Γ₃₄₆] maximum at 775.8 MeV, no mass input |
| Hilbert space rigour (OQ25) | Absolute convergence proved; operators self-adjoint |
| Spectral independence (OQ32) | Occupied set is sum-free with no S-value degeneracy. Proved computationally for all 91 pairs; d=3 internal case proved analytically via non-tetrahedral-number argument; tau dominance algebraic; sector scale gaps structural from {1,4} seeds |
| Spin-½ from KK Dirac | The 3+1D Dirac equation follows from the Kaluza-Klein Dirac operator on M_∞ = ℝ^{3,1} × Ξ_d when Ψ∞ is a spinor field. Spin-½ is derived from the spinor bundle, not postulated per particle |
| S(n,d) geometric grounding | dim Sym^n(ℝ^d) = S(n,d): mode functions are degree-n monomials in d variables, and there are exactly S(n,d) of them. Mass = frequency = cumulative microstate count. All three are the same quantity. |
| Top quark derivation (OQ26) | n_ν₂ = S(n_u,4) = C(6,4) = 15 = C(6,2) = S(n_s+1,2) by binomial symmetry C(n,k)=C(n,n-k), where n_u+3 = n_s+2 = 6 follows from n_u = n_s−1. Therefore n_W = S(n_e,2) − n_ν₂ = 76, and g(d=5, n_top) = 76 forces n_top = 72 uniquely. |
| Three k₀ resonance conditions | k₀ = n_s² = n_e+n_u = S(n_s,3)−S(2,3) = 16. Three independent expressions equal k₀ simultaneously: (1) seed self-product, (2) cross-sector lepton+quark mode sum, (3) intra-d=3 gap identity from the g₃₃ derivation. All three add in phase at k₀, destabilising the single-mode solution and forcing the geometric-mean beat at m_b = √(S(16,3)×S(17,3)) × m_scale_3 = 4181 MeV (+0.02%). |
| Generation Tower Correction (GTC) | ε = g_coeff/(k₀ × n_mu) = (2/√7)/(16×35) = 1/(280√7) = 0.001350. Derived from: g_coeff = 2/√(n_s+n_u) (universal Jacobi coefficient), k₀ = n_s² (vacuum stability gap), n_mu = S(n_s,4) (fixed-point mode scale). Corrects c/u to 0.000% and t/u to −0.048%. Note k_charm = k_g33 = n_s−1 = 3: the same additions that generate the charm mode index also generate the coupling gap k₀. |
| d=5 coupling g₅₅ (algebraic structure) | Hopf fiber universality: both S¹→S³→CP¹ and S¹→S⁵→CP² share the electromagnetic U(1) fiber. Universality requires v₃/v₂ = v₅/v₄, giving g₂₅ = g₃₄ = 4√6 and g₅₅ = g₃₃×g₄₄/g₂₂ = 96/g₂₂ = 0.1329. No new empirical input required; g₅₅ is fixed by the same m_W that determines g₂₂. Complete coupling vector: {v₂=26.879, v₃=4.601, v₄=2.130, v₅=0.3645, v₆=v₁₀=0.500}. Neutrino mass hierarchy remains open (see below). |
| Tau mass residual — Dyson resummation | The d=6 and d=10 sectors are isotropically coupled: g_{6,6} = g_{6,10} = g_{10,10} = 1/4 exactly (all equal because Y_L = Y_τ = −1/2). The d=6→d=10 back-reaction correction feeds back on itself via g_{10,10}, giving a self-consistent equation: Δm = ε_{6→10}×m_τ + g_{10,10}×Δm → Δm = ε_{6→10}×m_τ/(1−g_{10,10}). Since g_{10,10} = 1/n_s, the resummation factor is 1/(1−1/n_s) = n_s/(n_s−1) = n_s/n_u (forced by n_u = n_s−1). Result: ε_total = 1/(n_u × n_s² × S(n_s,4)) = 1/1680. Correction +m_τ/1680 = +1.057 MeV. **m_τ = 1776.85 MeV (−0.11σ from PDG = 1776.86 ± 0.12 MeV). Inside 1σ.** No new inputs: m_e only. |
| d=10 Gegenbauer uniqueness | The Gegenbauer coupling at the seed resonance site b_{k₀}(d) = √(k₀(k₀+d−1))/(2k₀+d−2) satisfies b_{k₀}=1/2 if and only if 4k₀=(d−2)², i.e. d=2+2√k₀=2(n_s+1)=10. This is a second independent algebraic derivation of d=10 (the first being Hurwitz; the third being hypercharge anomaly cancellation). d=10 is the last sector with b_{k₀}≥1/2; d>10 is evanescent. Proved: 4×16=64=(10−2)². As a WKB corollary: the next-order correction to τ_{d=10} vanishes identically (since it is proportional to b_{k₀}−1/2=0), making d=10 the only sector for which the leading-order WKB delay is exact. |
| Ψ∞ spinor — Dirac neutrino prediction | The Clifford algebra Cl(d) has Bott periodicity 8. For d=5, d mod 8 = 5, which is the unique residue class for which Majorana spinors do not exist. Therefore the d=5 (neutrino) sector hidden-space spinor cannot support a Majorana mass term — no seesaw mechanism from the hidden-space geometry. IDWT with Ψ∞ a spinor predicts: **neutrinos are Dirac fermions.** Falsifiable by neutrinoless double beta decay (0νββ); no signal is expected ever. |
| Ψ∞ spinor — SO(10) GUT from d=10 | The d=10 sector admits a Majorana-Weyl spinor (d mod 8 = 2). Its 16-component Weyl spinor is exactly the **16** of SO(10) ≅ Spin(10), which under the SM subgroup decomposes as Q_L + u_R^c + e_R^c + d_R^c + L_L + ν_R^c — one complete SM generation including right-handed neutrino. The tau, ν_τ, b, and t all live in the same SO(10) multiplet. Their hypercharges Y = {−1, 0, −1/3, +2/3} follow from the SO(10) algebra, not from separate SM assignments. |
| Ψ∞ spinor — chirality from Kähler γ₅ | The CP^m sectors (d=2m, so d=2,4,6) carry a Kähler form ω. The operator γ₅^Kähler = i^m (ω^m)_{a₁…a_{2m}} γ^{a₁}⋯γ^{a_{2m}} splits each sector spinor into LEFT (holomorphic) + RIGHT (anti-holomorphic). For d=4 (CP², m=2): 4-spinor = 2L + 2R → (u_L,d_L) + (u_R,d_R). For d=6 (CP³, m=3): 8-spinor = 4L + 4R → two lepton doublets + right-handed partners. The W boson couples only to the LEFT components. |

---

## Open

**Λ_QCD — the mass gap**
IDWT derives the SU(3) gauge group, Yang-Mills action, UV coupling, and β-function coefficient. What it does not derive: why Λ_QCD ≈ 310 MeV >> m_scale_3 ≈ 4.7 MeV. The total ratio is ~66. Some of this is geometric (the k₀ = 16 resonance structure amplifies frequencies by O(10)), but the dominant non-perturbative mechanism that sets Λ_QCD is not yet derived. This is the IDWT form of the Yang-Mills mass-gap problem.

**Full CKM matrix and CP violation**
The Cabibbo angle is derived: sin θ_C = 1/√S(n_s,3) = 1/√20 = 0.22361 (Part 3 §12), matching PDG |V_us| = 0.22450 ± 0.00044 at −2.0σ. Full CKM mixing angles (|V_cb|, |V_ub|) and the CP-violating phase require a complex phase in the manifold structure — the mechanism is not yet identified.

**Neutrino mass hierarchy (d=5 mass scale)**
The d=5 coupling is algebraically closed: g₅₅ = 96/g₂₂ = 0.1329. Naive Route B gives m_scale_5 ≈ 0.37 MeV, while observed neutrino masses are ~meV — a suppression of ~5×10¹¹. With spinor Ψ∞, the seesaw mechanism is geometrically forbidden (Majorana condition impossible for d mod 8 = 5), so this suppression cannot be explained by seesaw. It must arise entirely from the d=5 sector vacuum dynamics: non-perturbative suppression at λ̂₅ ≫ 1, or a condensate from the (5,5)→10 Vandermonde vertex. Neutrino mass RATIOS are fully predicted (S(10,5):S(15,5):S(22,5)). The absolute mass scale mechanism is open.

**Lorentz completion 🔶**
Scalar covariance, spin-½ from the KK Dirac operator, chirality from Kähler γ₅ on CP² and CP³, and particle/antiparticle from the complex spinor are all established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure. The main open item is the explicit D_Ξ spectrum matching m_scale_d × f(S(n,d)).


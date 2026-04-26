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

---

## Open

**Tau mass residual**
m_tau = m_scale_6 × S(23,10) = 1775.79 MeV, −0.060% from PDG. The scale is closed (m_scale_10 = m_scale_6 from tau hypercharge). The residual is a d=6→d=10 back-reaction through g_{6,10}: d=6 acts as a source for d=10, giving a positive frequency correction vs. the negative correction in d=4. Mechanism identified; not yet derived from g_{6,10}.

**Λ_QCD — the mass gap**
IDWT derives the SU(3) gauge group, Yang-Mills action, UV coupling, and β-function coefficient. What it does not derive: why Λ_QCD ≈ 310 MeV >> m_scale_3 ≈ 4.7 MeV. The total ratio is ~66. Some of this is geometric (the k₀ = 16 resonance structure amplifies frequencies by O(10)), but the dominant non-perturbative mechanism that sets Λ_QCD is not yet derived. This is the IDWT form of the Yang-Mills mass-gap problem.

**Full CKM matrix and CP violation**
The Cabibbo angle follows from the seed ratio. Full CKM mixing angles and the CP-violating phase require a complex phase in the manifold structure — the mechanism is not yet identified.

**Complete the coupling vector v for d=5**
The coupling matrix G_{dd'} = v_d × v_{d'} is complete for d ∈ {2,3,4,6,10}. The d=2 coupling g₂₂ has been confirmed non-derivable from CP¹ geometry: all geometric approaches (Hopf size ratio, Chern number, Dirac index pattern, hypercharge, electromagnetic coupling) miss the correct m_scale_2 by factors of 3–54, and the ratio m_scale_2/m_scale_6 ≈ 10⁶ has no combinatorial form. m_W is therefore a genuine empirical input. One sector remains open: d=5 (neutrinos). g₅₅ is not yet constrained; the Vandermonde pair 2+3=5 links it to g₂₂ and g₃₃ but does not fix it independently.

**Lorentz completion (~90% closed)**
Scalar covariance, spin-½ from the KK Dirac operator, and chirality from spin^c on CP² are established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure.


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
| Exact coupling constants (OQ30b) | g₄₄=12/√7, g₃₄=4√6 from seeds {n_s,n_u} |
| Scale hierarchy (OQ17) | m_scale_3 from comb filter beat = ρ meson mass |
| ρ meson from comb filter (OQ35) | Im[Γ₃₄₆] maximum at 775.8 MeV, no mass input |
| Hilbert space rigour (OQ25) | Absolute convergence proved; operators self-adjoint |
| Spectral independence (OQ32) | Occupied set is sum-free with no S-value degeneracy. Proved computationally for all 91 pairs; d=3 internal case proved analytically via non-tetrahedral-number argument; tau dominance algebraic; sector scale gaps structural from {1,4} seeds |
| Spin-½ from KK Dirac | The 3+1D Dirac equation follows from the Kaluza-Klein Dirac operator on M_∞ = ℝ^{3,1} × Ξ_d when Ψ∞ is a spinor field. Spin-½ is derived from the spinor bundle, not postulated per particle |
| S(n,d) geometric grounding | dim Sym^n(ℝ^d) = S(n,d): mode functions are degree-n monomials in d variables, and there are exactly S(n,d) of them. Mass = frequency = cumulative microstate count. All three are the same quantity. |
| Top quark derivation (OQ26) | n_ν₂ = S(n_u,4) = C(6,4) = 15 = C(6,2) = S(n_s+1,2) by binomial symmetry C(n,k)=C(n,n-k), where n_u+3 = n_s+2 = 6 follows from n_u = n_s−1. Therefore n_W = S(n_e,2) − n_ν₂ = 76, and g(d=5, n_top) = 76 forces n_top = 72 uniquely. |
| Three k₀ resonance conditions | k₀ = n_s² = n_e+n_u = S(n_s,3)−S(2,3) = 16. Three independent expressions equal k₀ simultaneously: (1) seed self-product, (2) cross-sector lepton+quark mode sum, (3) intra-d=3 gap identity from the g₃₃ derivation. All three add in phase at k₀, destabilising the single-mode solution and forcing the geometric-mean beat at m_b = √(S(16,3)×S(17,3)) × m_scale_3 = 4181 MeV (+0.02%). |

---

## Open

**Generation Tower Correction (GTC) — sector function φ_d required**
The GTC (Part 2 §11) fits ε = 0.001340 from the d=4 within-sector curve and corrects c/u to 0.000% and t/u to −0.04%. Structural candidate: ε = 1/(g₃₃ × n_mu) = 1/(280√7) = 0.001350, matching to 0.74% (inside PDG light quark uncertainties).

The on-shell derivation was attempted. The IDWT mode equation is (∂² + M²)χ_{n,d} = g_{dd} K χ, giving a first-order energy shift δ(M²) = g²_{dd} |⟨χ_{n,d}|φ_d⟩|². The inter-shell coupling in the hockey-stick sum requires the matrix element:

  K_{k,k+1} = g²_{dd} × ⟨χ_k|φ_d⟩ × ⟨φ_d|χ_{k+1}⟩

where φ_d is the sector kernel function. If φ_d = χ_{n_s,d} (seed-degree section), orthogonality kills all inter-shell coupling except at k = n_s — wrong structure. If φ_d is a non-homogeneous coherent state on CP^{d-1}, the matrix elements are non-zero and in principle computable, but require explicit integration over the Fubini-Study measure.

The derivation is blocked at a definite integral:
  ε ~ g²₃₃ × ∫_{CP²} χ_k(ξ) φ₃(ξ) dμ_{FS}(ξ) × ∫_{CP²} φ₃(ξ') χ_{k+1}(ξ') dμ_{FS}(ξ')
evaluated at k = n_s−1 with the IDWT sector function φ₃ specified.

What remains: identify the explicit form of φ_d from the IDWT action (specifically, whether it is a coherent state on CP^{d-1} peaked at the seed configuration), then evaluate the Fubini-Study integral. The result must equal 1/(g²₃₃ × n_mu) to confirm the structural candidate.

**Tau mass residual**
m_scale_10 = m_scale_6 is derived from g₁₀,₁₀ = g₆₆ = 1/4. The tau prediction is therefore m_τ = m_scale_6 × S(23,10) = 1775.79 MeV, −0.060% from PDG. The scale is closed. Any correction would be internal to the d=10 sector — a modification to the n=23 mode frequency — not a scale problem.


**Λ_QCD — the mass gap**
IDWT derives the SU(3) gauge group, Yang-Mills action, UV coupling, and β-function coefficient. What it does not derive: why Λ_QCD ≈ 310 MeV >> m_scale_3 ≈ 4.7 MeV. Geometric amplification accounts for a factor of ~45; the remaining factor of ~230 requires non-perturbative dynamics. This is the IDWT form of the Yang-Mills mass-gap problem.

**Full CKM matrix and CP violation**
The Cabibbo angle follows from the seed ratio. Full CKM mixing angles and the CP-violating phase require a complex phase in the manifold structure — the mechanism is not yet identified.

**Complete the coupling vector v for d=2 and d=5**
The coupling matrix G_{dd'} = v_d × v_{d'} is now complete for d ∈ {3,4,6,10} — all self-couplings and cross-couplings among these four sectors are derived. Two sectors remain: d=2 (gauge bosons, Higgs mechanism) and d=5 (neutrinos). The Vandermonde pair 2+3=5 means g₅₅ requires g₂₂ first, and g₂₂ is not constrained by the hypercharge argument because bosons acquire mass via the Higgs mechanism rather than the fermion coupling structure. These two encode the electroweak and neutrino mass scales.

A numerical observation at current precision: m_u² ≈ m_d in MeV (4.67 ≈ 4.67, within PDG uncertainties). If structural, only one quark mass would be needed as anchor. Not yet proved.

**Lorentz completion (~90% closed)**
Scalar covariance, spin-½ from the KK Dirac operator, and chirality from spin^c on CP² are established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure.

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

---

## Open

**Top quark derivation (OQ26)**
n_top = 72 is uniquely selected by the Level-2 double-crossing condition g(n_charm, n_top) = S(n_e, 2) = 91. The proof reduces to a single identity: n_W = S(n_e,2) − n_ν₂ = 76, which follows if n_ν₂ = S(n_s+1, 2) is established from the d=5 Hopf structure rather than matched from oscillation data.

**Generation Tower Correction (GTC) — derive ε from the action**
The GTC (Part 2 §11) fits ε = 0.001340 from the d=4 within-sector curve and corrects c/u to 0.000% and t/u to −0.04%. The correction is per-particle, depends only on how many additions were used to generate the mode index n, and leaves mu/e, s/d, tau/mu untouched by construction. What remains: derive ε from the IDWT kernel coupling structure rather than fitting it; confirm the k_t = k_c + (2×n_s−1) = 10 chain rule from first principles.

**Tau mass residual**
m_scale_10 = m_scale_6 is derived from g₁₀,₁₀ = g₆₆ = 1/4. The tau prediction is therefore m_τ = m_scale_6 × S(23,10) = 1775.79 MeV, −0.060% from PDG. The scale is closed. Any correction would be internal to the d=10 sector — a modification to the n=23 mode frequency — not a scale problem.

**Three k₀ resonance conditions**
The bottom quark bifurcation at k₀=16 is driven by three independent resonance conditions adding in phase. The mechanism is identified; the three conditions are not yet individually enumerated.

**Λ_QCD — the mass gap**
IDWT derives the SU(3) gauge group, Yang-Mills action, UV coupling, and β-function coefficient. What it does not derive: why Λ_QCD ≈ 310 MeV >> m_scale_3 ≈ 4.7 MeV. Geometric amplification accounts for a factor of ~45; the remaining factor of ~230 requires non-perturbative dynamics. This is the IDWT form of the Yang-Mills mass-gap problem.

**Full CKM matrix and CP violation**
The Cabibbo angle follows from the seed ratio. Full CKM mixing angles and the CP-violating phase require a complex phase in the manifold structure — the mechanism is not yet identified.

**Complete the coupling vector v for d=2 and d=5**
The coupling matrix G_{dd'} = v_d × v_{d'} is now complete for d ∈ {3,4,6,10} — all self-couplings and cross-couplings among these four sectors are derived. Two sectors remain: d=2 (gauge bosons, Higgs mechanism) and d=5 (neutrinos). The Vandermonde pair 2+3=5 means g₅₅ requires g₂₂ first, and g₂₂ is not constrained by the hypercharge argument because bosons acquire mass via the Higgs mechanism rather than the fermion coupling structure. These two encode the electroweak and neutrino mass scales.

A numerical observation at current precision: m_u² ≈ m_d in MeV (4.67 ≈ 4.67, within PDG uncertainties). If structural, only one quark mass would be needed as anchor. Not yet proved.

**Lorentz completion (~90% closed)**
Scalar covariance, spin-½ from the KK Dirac operator, and chirality from spin^c on CP² are established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure.

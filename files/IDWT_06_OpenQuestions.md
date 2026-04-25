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
| Spectral independence | Occupied set is sum-free; proved computationally and structurally |

---

## Open

**Prove that Ψ∞ resonates at frequencies S(n,d) × m_scale_d, not at n × m_scale_d**

The combinatorics are clean: S(n,d) is the cumulative microstate count, and it is also the resonant frequency of mode n in sector d (in units of m_scale_d). Mass is frequency in natural units. The hockey-stick identity is a theorem. The generation law follows from the Pascal recursion. None of this is in question.

What is not yet proved is the dynamical step: that the IDWT coupling structure {g_dd, g_34, k₀=16} forces Ψ∞ to resonate at frequencies S(n,d) × m_scale_d rather than n × m_scale_d. S(n,d) grows as n^d; n grows linearly. The combinatorics select S(n,d); the dynamics must confirm it.

What is established toward this: the graded block structure follows from SU(d) symmetry via Schur's lemma — Schur gives a scalar eigenvalue λ_n on each block, but does not determine its value. The d-dimensional harmonic oscillator has S(n,d) as its cumulative state count (analytically exact). The operator class is identified. The remaining work is showing that the coupling structure forces λ_n = S(n,d) × m_scale_d.

**Top quark derivation (OQ26)**
n_top = 72 is uniquely selected by the Level-2 double-crossing condition g(n_charm, n_top) = S(n_e, 2) = 91. The proof reduces to a single identity: n_W = S(n_e,2) − n_ν₂ = 76, which follows if n_ν₂ = S(n_s+1, 2) is established from the d=5 Hopf structure rather than matched from oscillation data.

**Tau mass residual**
The leading-order prediction m_τ = m_e × S(23,10)/S(13,6) = 1775.79 MeV is −0.060% from PDG. The m_scale_10/m_scale_6 ratio is not yet derived geometrically.

**Three k₀ resonance conditions**
The bottom quark bifurcation at k₀=16 is driven by three independent resonance conditions adding in phase. The mechanism is identified; the three conditions are not yet individually enumerated.

**Λ_QCD — the mass gap**
IDWT derives the SU(3) gauge group, Yang-Mills action, UV coupling, and β-function coefficient. What it does not derive: why Λ_QCD ≈ 310 MeV >> m_scale_3 ≈ 4.7 MeV. Geometric amplification accounts for a factor of ~45; the remaining factor of ~230 requires non-perturbative dynamics. This is the IDWT form of the Yang-Mills mass-gap problem.

**Full CKM matrix and CP violation**
The Cabibbo angle follows from the seed ratio. Full CKM mixing angles and the CP-violating phase require a complex phase in the manifold structure — the mechanism is not yet identified.

**Lorentz completion (~90% closed)**
Scalar covariance, spin-½ from the KK Dirac operator, and chirality from spin^c on CP² are established. Remaining: full Spin(9) decomposition for d=10, and α_s running from the IDWT coupling structure.

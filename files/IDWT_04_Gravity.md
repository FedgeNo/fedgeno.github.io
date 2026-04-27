# IDWT — Part 4: Gravity

---

## 1. Gravity is Emergent ✅

Gravity is not fundamental in IDWT. It is the large-scale consequence of Ψ∞ structure projecting into our 3D slice. When Ψ∞ has a stable concentrated feature (a massive particle), the surrounding manifold geometry is distorted. That distortion, projected to 3D, is gravitational attraction.

---

## 2. Newtonian Limit ✅

In the weak-field, static, non-relativistic limit:
```
∇²Φ = 4πG · S(n,d) · |ψ_3D(r)|²
```

This is the Poisson equation of Newtonian gravity with mass m = S(n,d) × m_scale_d. It follows directly from ρ_m = ∫|Ψ∞|² dξ — the projection definition of observable matter density.

---

## 3. Einstein Field Equations 🔶

Varying the full action on M_∞ with respect to the visible metric, and projecting to the observable slice:
```
G_μν + Λ_eff g_μν = 8π G_eff T_μν^obs
```

The effective stress-energy has three contributions:
1. **Matter** from occupied resonances: T_μν = Σᵢ mᵢ uμuν δ³(x−xᵢ)/√(−g)
2. **Kernel contribution**: positive energy for colour non-singlet configurations; zero for singlets
3. **Vacuum** from unoccupied modes

G_eff emerges from the hidden volume and kernel normalization, numerically consistent with Newton's constant given m_scale_3 and R_CP³ ≈ 0.5 fm.

In the static strong-field regime, the projected metric develops an apparent horizon while the full M_∞ geometry stays regular. The "singularity" becomes a finite-energy high-amplitude region in the hidden coordinates. Information is preserved globally.

---

## 4. Cosmological Constant ✅

Λ_eff is naturally small because unoccupied modes — the main source of vacuum energy — have high projection mismatch Ω_log = ln(S(n,d)/S(n,2)), suppressing their contribution exponentially. The scale is tied to the same hidden radii and coupling strengths that fix particle masses. No fine-tuning is required.

---

## 5. Two-Stage Observability ✅

Every integer pair (n,d) with d ∈ {2,3,4,5,6,10} exists as a resonance of Ψ∞. Observable particles are those passing two filters:

**Stage 1 — Projection:** The mode projects with sufficient amplitude into the 3+1D slice. High projection mismatch Ω_log suppresses modes exponentially. For quarks (d=3,4), the U(1) breaking operator Φ†P₁Φ is gauge-forbidden under SU(3)_c → quarks project at full strength automatically. Leptons and neutrinos carry no colour charge, so suppression is allowed.

**Stage 2 — Stability:** The projected mode must survive 3D QCD dynamics. Colour-non-singlet configurations carry positive kernel energy and decohere.

The Stage-1 filter has an exact occupation criterion from the Ω_log suppression factor exp(−Ω_log) = S(n,2)/S(n,3) for d=3:

| n | Ω_log | Occupied? |
|---|-------|-----------|
| 1 | 0.000 | ✅ down quark |
| 2 | 0.288 | no — 18.8 MeV |
| 3 | 0.511 | no — 47.0 MeV |
| 4 | 0.693 | ✅ strange quark |
| 5+ | >0.85 | no |

Both occupied modes (n=1,4) are exactly those selected by the co-fixed-point spectrum {1,4}. Modes n=2,3 also pass Stage 1 (Ω_log = 0.288, 0.511 < ln 2) but are absent from the co-fixed-point spectrum — they are unoccupied resonances of M_∞, not suppressed by projection. Modes n≥5 (Ω_log > ln 2) fail Stage 1 and are additionally suppressed. The d=3 unoccupied masses (18.8 and 47 MeV) are predicted absent as stable distinct states.

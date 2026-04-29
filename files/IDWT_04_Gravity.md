# IDWT — Part 4: Gravity

---

## 1. Gravity is Emergent — and Purely Geometric ✅

Gravity is not fundamental in IDWT. It is the large-scale consequence of Ψ∞ structure projecting into our 3D slice. When Ψ∞ has a stable concentrated feature (a massive particle), the surrounding manifold geometry is distorted. That distortion, projected to 3D, is gravitational attraction.

Critically, IDWT has no gravitons. Gravity is entirely described by curvature — the distortion of the projected 4D metric by the local energy density of |Ψ∞|². There is no mediating particle, no spin-2 boson, and no quantum of the gravitational field. Gravity is geometry.

This is not a minor technical point. It is why IDWT's macroscopic hidden dimensions are consistent with all known gravitational experiments.

---

## 1b. Why Macroscopic Hidden Dimensions Do Not Violate Experiment ✅

The standard objection to macroscopic extra dimensions is that they strengthen gravity at short distances and produce detectable deviations from Newton's inverse-square law. This objection assumes that gravitons propagate into the extra dimensions. Once gravitons can travel off the 4D slice, they dilute the gravitational force, changing the 1/r² potential to 1/r^(2+n) at distances smaller than the extra dimension size. Experiments — most precisely the Eöt-Wash torsion balance, which tests gravity down to roughly 50 microns — see no such deviation and exclude macroscopic extra dimensions under that assumption.

IDWT is not under that assumption. There are no gravitons. A geometric theory of gravity has nothing to propagate into hidden dimensions, because gravity is not a particle — it is the curvature of the projected 4D slice caused by the distribution of |Ψ∞|². The entire framework of graviton propagation, KK graviton resonances, and modified Newton's law at short distances simply has no analogue in IDWT. The Eöt-Wash exclusions and all collider searches for KK graviton excitations are irrelevant to a graviton-free theory.

More precisely: in IDWT, the gravitational field is defined by varying the projected 4D action with respect to the visible metric g_μν. The hidden sector geometry Ξ enters only through its contribution to the effective stress-energy (via the mass spectrum and the vacuum energy of unoccupied modes). It does not contribute independent gravitational degrees of freedom that could propagate separately. The 4D curvature is sourced entirely by the projected matter distribution — everything in Ξ that affects gravity does so only by first becoming a particle mass or a vacuum contribution, and those are already counted in T_μν^obs.

**The hidden dimensions are detected.** They are what produces the mass spectrum. Every particle mass being m_scale_d × S(n,d) is a direct readout of the hidden sector geometry — the dimension d, the sector manifold curvature that sets m_scale_d, and the mode count S(n,d). The sectors are not invisible; they are the origin of all observed particle masses. What the hidden geometry does not produce is any *additional* gravitational signature beyond the normal 4D gravitational effect of those masses, because the geometrical structure of Ξ is already fully accounted for as matter.

**Why no other extra-dimensional signatures appear** is explained by the two-stage observability mechanism (§5 below and Part 7). Any mode that would correspond to a particle propagating through Ξ rather than sitting at a sector resonance fails Stage-1 projection — its amplitude at the slice ξ⁰ is exponentially suppressed. The only modes that reach 3D are the stable resonances of M_∞ that pass both filters. There are no bulk modes in IDWT, no tower of KK excitations accessible to experiment beyond those already identified as the SM particle spectrum.

**What remains open** is a formal derivation of the projected 4D gravitational equations directly from the full M_∞ action — showing explicitly that the hidden metric fluctuations in Ξ do not contribute independent gravitational propagating degrees of freedom. The qualitative argument is sound and rests on the absence of gravitons; the formal proof from the action is in Part 6 as an open item.

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

G_eff emerges from the hidden volume and kernel normalization, numerically consistent with Newton's constant given m_scale_3 and the macroscopic sector radii.

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

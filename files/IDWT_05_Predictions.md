# IDWT — Part 5: Predictions

---

## 1. Confirmed Predictions

The mass ratios below are not fitted. Within each sector, S(n,d)/S(m,d) is a ratio of binomial coefficients — fixed the moment the mode indices are assigned. The generation law identities (muon = charm + ν₂, etc.) are consequences of the Pascal recursion S(n,d) = S(n,d−1) + S(n−1,d), not separate postulates.

**Strange/down ratio = 20 exactly**
```
S(4,3) / S(1,3) = 20 / 1 = 20.000
```
Fixed by the formula before comparing to data. Zero-error prediction.

**Muon/electron ratio**
```
S(35,6) / S(13,6) = 3,838,380 / 18,564 = 206.7647   (PDG: 206.7683,  −0.002%)
```

**Tau/electron ratio**
```
S(23,10) / S(13,6) = 64,512,240 / 18,564 = 3,475.13   (PDG: 3,477.23, bare −0.060%; Dyson-resummed: −0.11σ inside 1σ)
```

**Up-type quark mass ratios — with Generation Tower Correction**

The raw simplex predictions for d=4 run systematically high (+0.40% to +1.31%). Applying the Generation Tower Correction (Part 2 §11) with ε = 1/(280√7) = 0.001350 (derived) and k values {u:0, c:3, t:10}:

```
c/u corrected: 590.333 × (1−ε)³  / 1 = 587.95   (PDG 587.96,  0.000%)
t/u corrected: 81,030  × (1−ε)¹⁰ / 1 = 79,943   (PDG 79,981, −0.048%)
t/c corrected: 137.261 × (1−ε)⁷      = 135.97   (PDG 136.03, −0.045%)
```

**Bottom quark**
```
√(S(16,3) × S(17,3)) × m_scale_3 = √(816 × 969) × 4.702 = 4,181 MeV   (PDG: 4,180 ± 10,  +0.02%)
```

**Photon mass = 0**
```
S(0, 2) = C(1, 2) = 0   →   m_photon = 0   (exact, derived)
```

**Electroweak sector (empirical input: m_W = 80,377 MeV)**
```
m_W:      80,377 MeV   (PDG: 80,377,   input)
m_Z:      91,228 MeV   (PDG: 91,188,   +0.044%)
m_Higgs: 125,263 MeV   (PDG: 125,250,  +0.010%)
sin²θ_W:      0.2237   (PDG on-shell: 0.22290,   +0.37%)
ρ parameter:       1   (exact, derived)
```

**ρ meson from the comb filter (no mass input)**
```
Im[Γ₃₄₆(ω)] peak = 775.8 MeV   (PDG: 775.3 MeV,  +0.07%)
```
All inputs — g₃₃=8√7, g₄₄=12/√7, g₆₆=1/4, delays from k₀=16 — come from seeds {1,4} and m_e alone.

**Cabibbo angle**
```
sin θ_C = 1/√20 = 0.2236   (PDG: 0.2245,  −0.40%)
```

**Up/down quark mass ratio**
```
m_u / m_d = √(3/14) = 0.463   (PDG: 0.462,  +0.08%)
```

**Neutrino mass ordering: normal hierarchy**
S(n,5) is monotonically increasing, n_ν₁ < n_ν₂ < n_ν₃ → m_ν₁ < m_ν₂ < m_ν₃. Consistent with current experimental preference at 3–4σ.

---

## 2. Full Prediction Table with Statistical Significance

Using m_e = 0.511 MeV and m_W = 80,377 MeV as the two empirical inputs (both from measurement, neither fitted):

| Particle | IDWT (MeV) | PDG (MeV) | Error | Note |
|----------|-----------|-----------|-------|------|
| e | 0.5110 | 0.5110 | 0.000% | anchor |
| μ | 105.657 | 105.658 | −0.001% | — |
| τ | 1776.85 | 1776.86 | −0.11σ† | — |
| d | 4.702 | 4.670 | +0.68% | OQ35 residual |
| s | 94.04 | 93.40 | +0.68% | OQ35 residual |
| u | 2.177 | 2.160 | +0.77% | OQ35 + d=4 |
| c | 1284.9 | 1270.0 | +1.17% | OQ35 + d=4 |
| t (raw) | 176,365 | 172,760 | +2.09% | OQ35 + d=4 |
| t (GTC, k=10) | 173,999 | 172,760 | +0.72% | ε = 1/(280√7) |
| b | 4,181 | 4,180 | +0.02% | — |
| W | 80,377 | 80,377 | 0.000% | empirical measurement |
| Z | 91,228 | 91,188 | +0.044% | OQ35 bounded |
| H | 125,263 | 125,250 | +0.010% | OQ35 bounded |

† **m_τ = m_e × S(23,10)/S(13,6) × (1 + 1/1680) = 1776.85 MeV (−0.11σ, inside 1σ).** The correction 1/1680 = 1/(n_u × n_s² × S(n_s,4)) is the Dyson resummation of the d=6→d=10 back-reaction. Physical mechanism: (1) g_{6,10}/(k₀×n_mu) = 1/2240 is the leading back-reaction from the isotropic coupling g_{6,6}=g_{6,10}=g_{10,10}=1/4; (2) the correction feeds back via the d=10 self-coupling g_{10,10}=1/n_s, giving resummation factor n_s/(n_s−1) = n_s/n_u (forced by n_u=n_s−1). Combined: 1/2240 × 4/3 = 1/1680. No inputs beyond m_e and seeds {n_s,n_u}.

**Boson precision note:** m_W is the empirical measurement used to set the d=2 sector scale; W sits at 0.000% by definition. The Z and H predictions follow from the same m_scale_2 and their simplex mode indices. Their residuals (+0.044% and +0.010%) are consistent with the OQ35 precision budget.

---

## 3. d=4 Sector: GTC Correction

The d=4 excess above the OQ35 baseline grows with mode index, corrected by the GTC with ε = 1/(280√7) and k values {u:0, c:3, t:10}. The GTC corrects within-d=4 RATIOS; the OQ35 scale offset (+0.77%) remains in all absolute masses:

| Particle | Absolute raw | Absolute after GTC | Ratio (vs u) raw | Ratio after GTC |
|---|---|---|---|---|
| u | +0.77% | +0.77% (k=0) | — | — |
| c | +1.17% | **+0.76%** | +0.403% | **0.000%** |
| t | +2.09% | **+0.72%** | +1.311% | **−0.048%** |

The GTC closes the within-sector ratio errors. It does not remove the OQ35 scale error, which persists uniformly across all d=4 absolute masses at ~+0.77%.

The l=2 tensor part of the kernel (explained by Wigner-Eckart) gives the √C₂(n) functional form of the within-sector correction — confirming that the GTC's growing correction with k is geometrically natural. The coefficient is derived (ε = 1/(280√7)), not fitted.

**Nucleon static properties** (from hidden l=1 admixture, Part 8 §66)
```
μ_p = 2.793 μ_N    (PDG: 2.7928,  match to 0.01%)
μ_n = −1.913 μ_N   (PDG: −1.9130, match to 0.02%)
g_A = 1.272         (PDG: 1.2723,  match to 0.02%)
```
All from the same kernel that produces confinement and meson masses.

**Two unobserved d=3 states**
```
n=2: 18.8 MeV   (= m_scale_3 × S(2,3))
n=3: 47.0 MeV   (= m_scale_3 × S(3,3))
```
Real resonances of M_∞ that fail Stage-1 projection. No stable hadron-like states should exist in the 15–50 MeV window unexplained by pion relatives or nuclear states.

**Neutrino absolute masses** (anchored to solar mass splitting Δm²₂₁ = 7.53×10⁻⁵ eV²)
```
m_ν₁ = 1.517 meV,   m_ν₂ = 8.809 meV,   m_ν₃ = 49.833 meV,   Σm_ν = 60.16 meV
Δm²₃₁ predicted = 2.481×10⁻³ eV²   (observed: 2.453×10⁻³ eV²,  +1.14%)
```

**Absent high-energy states** — observation of either falsifies the framework:
```
S(35,10) × m_scale_10 ≈ 68.3 GeV    [below Z mass; excluded at LEP]
S(72,10) × m_scale_10 ≈ 51.7 TeV    [beyond LHC reach; no fourth generation]
```

**Fine-structure observation**
```
S(72,4) / S(20,4) = 137.261 ≈ 1/α   (0.17% from CODATA)
```
Both mode indices are independently derived. The matching is observed, not derived.

---

## 4. What Would Falsify IDWT

1. m_strange / m_down measured significantly different from 20
2. μ/e ratio outside 206.7647 ± 0.005
3. Observation of a stable particle consistent with S(35,10) ≈ 68.3 GeV (IDWT predicts its absence; non-observation at LEP is consistent with this)
4. A fourth SM quark generation
5. Tau lepton requiring n ≠ 23 or d ≠ 10 in any consistent assignment
6. Normal neutrino mass ordering falsified by experiment

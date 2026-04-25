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
S(23,10) / S(13,6) = 64,512,240 / 18,564 = 3,475.13   (PDG: 3,477.23,  −0.060%)
```

**Up-type quark mass ratios — with Generation Tower Correction**

The raw simplex predictions for d=4 run systematically high (+0.40% to +1.31%). Applying the Generation Tower Correction (Part 2 §11) with ε = 0.001340 and k values {u:0, c:3, t:10}:

```
c/u corrected: 590.333 × (1−ε)³  / 1 = 587.96   (PDG 587.96,  0.000%)
t/u corrected: 81,030  × (1−ε)¹⁰ / 1 = 79,998   (PDG 79,981, +0.021%)
t/c corrected: 137.261 × (1−ε)⁷      = 136.03   (PDG 136.03,  0.000%)
```

**Bottom quark**
```
√(S(16,3) × S(17,3)) × m_scale_3 = √(816 × 969) × 4.702 = 4,181 MeV   (PDG: 4,180 ± 10,  +0.02%)
```

**Photon mass = 0**
```
S(0, 2) = C(1, 2) = 0   →   m_photon = 0   (exact, derived)
```

**Electroweak sector (one input: m_W)**
```
m_Z:      91,228 MeV   (PDG: 91,188,   +0.044%)
m_Higgs: 125,263 MeV   (PDG: 125,250,  +0.010%)
sin²θ_W:      0.2237   (PDG: 0.2231,   +0.31%)
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

## 2. Novel Predictions (Not Yet Tested)

**Two unobserved d=3 states**
```
n=2: 18.7 MeV
n=3: 46.7 MeV
```
Real resonances of M_∞ that fail Stage-1 projection. Exist between the down and strange quarks.

**Neutrino absolute masses** (anchored to solar mass splitting)
```
m_ν₁ ≈ 1.52 meV,   m_ν₂ ≈ 8.81 meV,   m_ν₃ ≈ 49.8 meV
Sum ≈ 60 meV
```

**Absent high-energy states** (three-generation closure)
```
S(72,10) × m_scale_10 ≈ 45.1 TeV   [predicted absent — no fourth generation]
S(35,10) × m_scale_10 ≈ 231 GeV    [predicted absent — in current LHC range]
```
Observation of either immediately falsifies the framework.

**Fine-structure observation**
```
S(72,4) / S(20,4) = 137.261 ≈ 1/α   (0.17% from CODATA)
```
Both mode indices are derived independently. The matching is observed, not derived.

---

## 3. What Would Falsify IDWT

1. m_strange / m_down measured significantly different from 20
2. μ/e ratio outside 206.7647 ± 0.005
3. Detection of the S(35,10) ≈ 231 GeV state at LHC
4. A fourth SM quark generation
5. Tau lepton requiring n ≠ 23 or d ≠ 10 in any consistent assignment
6. Down-quark sector spectral exponent converging to a value significantly different from T(3) = 6

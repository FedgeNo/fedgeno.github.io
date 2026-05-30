# Infinite Dimensional Wave Theory — Part 7: Two-Stage Observability & Mode Selection

*Sections 49–51: Dimensional Visibility, Stage-1/Stage-2 Mechanism, Beat Tower, CP^d Heat Kernel*

---

**Where we are.** We are inside M_∞ at the d=3 coordinate level — not external observers viewing a projection from a separate space. Every mode of Ψ_∞ is a feature of the same manifold we occupy. What this document calls "observability" is therefore not the question of how an outside observer projects modes onto our space, but the question of which resonances of M_∞ have enough of their vibrational activity in the d=3 coordinates that constitute our space for us to resolve them, and which are stable resonances at all. Both are intrinsic properties of the modes and of M_∞, not properties of an observer.

---

## 1. Candidate Resonances — Two-Stage Observability

The framework treats every integer pair (n,d) with d ∈ {2,3,4,5,6,10} as a candidate resonance of Ψ∞ on M_∞. Observable particles are those passing **two successive filters**:

- **Stage 1 (Dimensional Visibility):** Enough of the mode's vibrational activity must be in our d=3 dimensions. Modes with high dimensional depth Ω_log(n,d) = ln(S(n,d)/S(n,2)) have most of their activity in the d>3 sector coordinates and are observationally obscured by exp(−Ω_log).
- **Stage 2 (Co-fixed-point):** The mode-sector pair (n,d) must be an element of Σ_pairs — the unique finite closed set produced by the generation tower from seeds (1,3) and (4,3). The generation tower assigns both the mode index and the sector; stability is a property of the pair, not of the mode index alone. A mode index n appearing in a sector not assigned by the tower does not pass Stage 2.

This reframes mode selection from a dynamical problem to a geometric filtering problem on M_∞ itself: which (n,d) pairs are stable resonances, and which of those have enough d=3-coordinate activity to be resolved by an observer at our coordinate level.

---

### 1.1 Dimensional Visibility (Stage 1)

The d=3 visible fraction for sector d relative to the quark sector (d=3) scales roughly as:
```
A_rel(d) ~ (m_scale_d / m_scale_3)^{1/3}
```
This is a heuristic estimate. The rigorous derivation from the sector heat kernel is in §2.9, which gives A_rel = exp(−c_d λ̂_d) with c_d = d/(d+1)² and λ̂_d ≈ 1.

The dimensional depth for mode (n,d):
```
Ω_log(n,d) = ln(S(n,d) / S(n,2))
```

Ω_log measures how much of the mode's activity is distributed across the d>3 sector coordinates relative to the d=2 gauge sector baseline. Modes with high Ω_log have most of their vibration in the d>3 sector coordinates; their d=3 visible fraction is exp(−Ω_log) = S(n,2)/S(n,d). Scattering states (non-normalizable modes, Part 4 §3.13) have Ω_log → ∞ — their activity is spread across the full infinite-dimensional space and they have negligible presence in our d=3 dimensions. Bound states have finite Ω_log; the co-fixed-point structure of the eigenmode selection rule selects the specific (n,d) pairs that appear in the observed spectrum regardless of their individual Ω_log values.

**Partition function interpretation:** The dimensional visibility weight exp(−Ω_log) = S(n,2)/S(n,d) is a Boltzmann weight. The visibility-weighted mode sum Z = Σ S(n,d)·exp(−Ω_log) = Σ S(n,2) — the result is independent of d. Every mode (n,d) contributes exactly S(n,2) to the d=3-visible count regardless of sector. The apparent mass hierarchy between sectors is a property of the resonance selection mechanism (co-fixed-point), not of dimensional structure itself.

### 1.2 Dimensional Visibility Table

| Sector | Geometry | Physical role | Dimensional visibility |
|--------|----------|---------------|------------------------|
| d=2 | CP¹ | Gauge bosons | fully visible (all activity in d≤3) |
| d=3 | S³ | Down-type quarks | fully visible (colour-protected) |
| d=4 | CP² | Up-type quarks | fully visible (colour-protected) |
| d=5 | S⁵ | Neutrinos | partially obscured in d>3 sector coordinates |
| d=6 | CP³ | Charged leptons | partially obscured in d>3 sector coordinates |
| d=10 | CP⁵ | Tau | most activity in d>3 sector coordinates |

Quarks (d=3,4) are fully visible because the U(1)-breaking operator Φ†P₁Φ is gauge-forbidden under SU(3)_c, forcing all their activity into d≤3. The visibility hierarchy for leptons/neutrinos follows from the heat-kernel derivation (§2.9).

### 1.3 Stage-2 Co-fixed-point Condition

A mode-sector pair (n,d) passes Stage 2 if and only if it is an element of Σ_pairs — the unique finite closed set of 15 pairs produced by the generation tower (Part 1 §5, Part 2 §2–4). The tower is seeded by (n_down=1, d=3) and (n_s=4, d=3); it applies hockey-stick evaluations and additive operations that generate both the mode index and the sector assignment for every stable pair. The full list of Σ_pairs and the derivation chain are in Appendix A §1 and §5.

**Two independent derivation chains.** Stage 2 membership in Σ_pairs requires both the correct mode index n and the correct sector d. These come from separate sources: (i) the generation tower derives n via hockey-stick, additive, and g-rule operations; (ii) the sector structure of Part 1 §3 assigns each particle family to its sector — quarks to d=3,4 via χ(CP²)=N_c; neutrinos to d=5 via the Hopf fibration S¹→S⁵→CP²; charged leptons to d=6 via d=3⊗d=3 colour neutrality; tau to d=10 via Gegenbauer criticality; gauge bosons to d=2 via the g-rule. Neither chain derives the other: d cannot be recovered from n alone, and the same HS operation applied to different seeds yields particles in different sectors. Concretely: n=10 is stable only as (10,5)=ν₁, because the sector structure assigns the neutrino family to d=5 and the generation tower produces n=10 within that family. The pair (10,6) fails Stage 2 not because of the tower but because no sector-structure rule places the n=10 particle in d=6.

**What Stage 2 excludes.** A mode index n ∈ Σ_indices appearing in a sector not assigned by the tower fails Stage 2: the pair (n,d) is not in Σ_pairs. Σ_pairs is the complete co-fixed-point set; verified exhaustively up to n ≤ 1000, no pair outside Σ_pairs is generated by the tower operations (Appendix A §15). The sectors d=7,8,9 appear in the coordinate hierarchy of M_∞ but the current coupling construction does not establish active eigenmode geometry there (Rule A, §3a); they have no co-fixed-point tower and therefore no stable modes under the present framework.

---

### 1.4 Quartic Bifurcation — The Bottom Quark

The bottom quark survives as a geometric-mean beat between two virtual d=3 modes rather than as a single simplex mode. The bifurcation point:

```
k₀ = n_strange² = 4² = 16
```

Three independent resonance conditions add in phase at k₀ (see Part 2 §8 and the three k₀ conditions):

1. k₀ = n_s² = 16 (seed self-product)
2. k₀ = n_e + n_u = 13 + 3 = 16 (cross-sector lepton + quark sum)
3. k₀ = S(n_s,3) − S(2,3) = 20 − 4 = 16 (intra-d=3 gap identity)

These raise the drive D_{16} by a factor of three, making the single-mode solution at n=16 unstable. The off-diagonal quartic coupling K_{16,17} then forces the symmetric fixed point |A₁₆| = |A₁₇|, yielding the geometric-mean beat:

```
m_b = √(S(16,3) × S(17,3)) × m_scale_3
    = √(816 × 969) × 4.702 ≈ 4,181 MeV
```
PDG: 4,180 ± 10 MeV. Error: +0.02%.

The beat partner n=17 = k₀+1 = n_c−n_u = 20−3.

### 1.4c g_{3,4} Effective Coupling at the Bifurcation 🔶

The exact cross-coupling g_{3,4} = 4√6 is fully derived from seed structure (Part 2 §9). At the bifurcation site k₀=16, the effective coupling involves kernel overlap integrals at n=16,17 in d=3. The bottom quark prediction (+0.02%) is consistent with g_{3,4} = 4√6; the detailed prefactor for the quartic amplitude is not yet derived from first principles.

---

### 1.5 Cross-Sector Two-Delay Beats

The (d,d') sector pairs give additional predicted resonances:

| Pair | Beat (MeV) | Nearest state | Mass error |
|------|-----------|----------------|-------|
| (3,6) | 775.0 | mass consistent with ρ(770) = 775.26 MeV; quantum numbers and decay channels not yet verified | −0.04% (simple beat; Im[Γ₃₄₆] gives 775.8 MeV, +0.07% consistency check) |
| (4,6) | 1207.6 | mass consistent with a₁(1260) = 1230 MeV; quantum numbers and decay channels not yet verified | −1.82% |

The (3,4) beat at 2163 MeV and the (6,10) beat at 736 MeV do not have clean hadronic mass matches. **Caveat on all beat identifications:** hadronic spectra are dense and overlapping; a mass match alone is insufficient for identification. Spin/parity quantum numbers, decay widths, and selection rules have not been verified from IDWT for any of the beat-tower states.

### 1.6 Complete d=3 Sideband Beat Tower

The formula beat(n,n+1) = √(S(n,3) × S(n+1,3)) × m_scale_3 produces a full tower:

| n, n+1 | Beat (MeV) | Nearest state | Mass error |
|--------|------------|---------------|-------|
| 4, 5 | 124.4 | (no identification — pion is a collective excitation, absent from sector spectrum; §3d Part 5) | — |
| 11, 12 | 1517.1 | mass consistent with f₂(1525); quantum numbers and decay channels not yet verified | −0.5% |
| **16, 17** | **4181** | **b quark (4180)** | **+0.02%** |

---

## 2. Two-Stage Filter — Summary

The two-stage paradigm unifies all mode-selection results. Every (n,d) exists as a resonance. Observable particles satisfy both filters. The co-fixed-point uniqueness (Part 1 §5), spectral independence, and sideband mechanism (§1.4 above) are all consequences.

The n=2,3 modes in d=3 are absent from the co-fixed-point spectrum — they pass Stage 1 (Ω_log = 0.288, 0.511, both below ln 2) but are not selected by the hockey-stick fixed-point structure. Their suppression is combinatorial, not geometric.

The two filters are independent conditions in principle. Under the current construction, all 15 elements of Σ_pairs pass Stage 1 (with colour and lepton exemptions where applicable), so the Stage-2-pass / Stage-1-fail cell is empty — there is no dark sector within the present framework. Whether a dark sector exists depends on whether stable modes beyond Σ_pairs can be identified, which requires either an extension of the coupling construction (to reach d=7,8,9) or a sector-universal stability argument (not currently derived). This is an open question; see §2.6.

**Stage-1's role for the observed spectrum.** None of the 15 observed particles is selected or excluded by Stage-1 alone:
- **Quarks (d=3,4)**: Stage-1 is bypassed entirely — colour protection (SU(3)_c gauge invariance) forces Ω_log = 0, so A_rel = 1 unconditionally regardless of mode index.
- **Gauge bosons (d=2)**: Stage-1 is vacuous — d=2 is the reference sector by definition, so Ω_log = ln(S(n,2)/S(n,2)) = 0.
- **Leptons and neutrinos (d=5,6,10)**: Stage-1 yields Ω_log > ln 2 for the heavy states (muon, tau), so these would fail Stage-1 taken alone; they appear in the observed spectrum because Stage-2 selects them independently. Stage-1 does not override Stage-2.

The d=2 reference in Ω_log = ln(S(n,d)/S(n,2)) is irreplaceable: d=2 carries the U(1)_EM coupling (the photon is the d=2 n=0 mode), and any dimensional visibility measure must be referenced against the observable electromagnetic sector to have physical meaning.

---

## 2.5 Complete Low-n Observability Atlas

Full enumeration of all low-n modes, with Ω_log = ln(S(n,d)/S(n,2)) quantifying the Stage-1 dimensional depth. Modes with Ω_log ≲ ln 2 ≈ 0.693 pass Stage 1; co-fixed-point membership (Stage 2) determines final occupancy.

**d=2 (Gauge bosons)** — all have Ω_log = 0 by convention (d=2 is the reference sector):

| n | S(n,2) | Mass | Status |
|---|--------|------|--------|
| 0 | 0 | 0 | photon (massless, exact) |
| 76 | 2926 | 80.379 GeV | **W** |
| 81 | 3321 | 91.230 GeV | **Z** |
| 95 | 4560 | 125.266 GeV | **H** |

**d=3 (Down-type quarks)** — m_scale_3 = 4.702 MeV:

| n | S(n,3) | Mass (MeV) | Ω_log | Stage 1 | Stage 2 | Final status |
|---|--------|------------|-------|---------|---------|--------------|
| 1 | 1 | 4.702 | 0.000 | ✅ pass | ✅ co-fp | **Occupied (down)** |
| 2 | 4 | 18.807 | 0.288 | ✅ pass | ❌ absent | Short-lived resonance only |
| 3 | 10 | 47.019 | 0.511 | ✅ pass | ❌ absent | Short-lived resonance only |
| 4 | 20 | 94.037 | 0.693 | ✅ marginal | ✅ co-fp | **Occupied (strange / confinement)** |
| 5 | 35 | 164.565 | 0.847 | ❌ suppressed | — | Absent |
| 6 | 56 | 263.304 | 0.981 | ❌ suppressed | — | Absent |

The n=2 and n=3 d=3 modes pass Stage 1 but fail Stage 2. They are not stable hadrons; they may appear as very short-lived colour-triplet resonances. No stable particles are predicted in the 15–50 MeV window beyond known pion sector states. The n=5 mode is the first to fail Stage 1 outright (Ω_log > ln 2).

**d=4 (Up-type quarks)** — m_scale_4 = 0.14510 MeV:

| n | S(n,4) | Mass (MeV) | Ω_log | Status |
|---|--------|------------|-------|--------|
| 3 | 15 | 2.177 | 0.916 | **Occupied (up)** |
| 20 | 8,855 | 1,279.7 | 3.742 | **Occupied (charm)** |
| 72 | 1,215,450 | 174,000 | 6.137 | **Occupied (top)** |

**d=5 (Neutrinos)** — m_scale_5 = 7.429 × 10⁻¹³ MeV:

| n | S(n,5) | Mass (meV) | Ω_log | Status |
|---|--------|------------|-------|--------|
| 10 | 2,002 | 1.487 | 3.595 | **Occupied (ν₁)** |
| 15 | 11,628 | 8.639 | 4.574 | **Occupied (ν₂)** |
| 22 | 65,780 | 50.27 (bare: 48.871) | 5.561 | **Occupied (ν₃)** |

**d=6 (Charged leptons)** — m_scale_6 = 2.753 × 10⁻⁵ MeV:

| n | S(n,6) | Mass (MeV) | Ω_log | Status |
|---|--------|------------|-------|--------|
| 13 | 18,564 | 0.511 | 5.318 | **Occupied (e)** |
| 35 | 3,838,380 | 105.657 | 8.715 | **Occupied (μ)** |

**d=10 (Tau sector)** — m_scale_10 = m_scale_6:

| n | S(n,10) | Mass (MeV) | Ω_log | Status |
|---|---------|------------|-------|--------|
| 23 | 64,512,240 | 1776.84 | 12.362 | **Occupied (τ)** |

**Falsifiable predictions from this atlas:**

1. Two light colour-triplet d=3 resonances at **18.807 MeV** (n=2) and **47.019 MeV** (n=3) should exist as short-lived states but are absent as stable particles (pass Stage 1, fail Stage 2). No stable hadrons or narrow resonances are predicted in the 15–50 MeV window beyond the known pion sector.
2. The next d=3 mode above strange (n=5, 164.565 MeV) is suppressed at Stage 1 (Ω_log = 0.847 > ln 2 = 0.693) and absent entirely.
3. The Ω_log threshold ln 2 ≈ 0.693 is not adjusted to fit these predictions; it is the majority-support localization criterion: the condition that at least half of mode (n,d)'s spectral support lies in the observable d=2 reference subspace (§2.9.1).

**Ω_log values for heavy particles:** The top quark (Ω_log = 6.137), muon (8.715), and tau (12.362) all exceed ln 2 = 0.693. For the top (d=4 quark), this is irrelevant: colour protection sets λ_d = 0, so A_rel = 1 and Stage-1 passes unconditionally regardless of Ω_log. For the muon (d=6) and tau (d=10), these large Ω_log values confirm that most of their vibrational activity is in extra dimensions — they survive as observable particles because they satisfy Stage-2 co-fixed-point selection, which operates independently of Stage-1. The ln 2 threshold governs dimensional visibility; it does not override the co-fixed-point occupancy condition.

---

## 2.6 Dark Matter — Open Question ❓

Under the corrected Stage-2 definition (§1.3 above), the Stage-2-pass / Stage-1-fail cell of the two-filter table is empty. Stage 2 selects the pair (n,d), not the mode index n alone. Every element of Σ_pairs passes Stage 1 (with colour and lepton exemptions), so no co-fixed-point mode is simultaneously invisible. The present construction produces no dark sector.

The previous version of this section enumerated 36 candidate invisible modes (11 velinos in d=5, 12 umbrons in d=6, 13 liminons in d=10) by taking all n ∈ Σ_indices and sweeping over sectors outside their tower-assigned homes. That construction assumed co-fixed-point stability is sector-universal — that n=10, stable as ν₁ in d=5, is also stable in d=6 and d=10. This assumption has not been derived from IDWT's dynamics (P8 is still a postulate) and is not supported by the generation tower: adding any non-Σ_pairs pair to the closed set breaks closure immediately (Appendix A §15). The velino/umbron/liminon enumeration is retracted as a derivation; it was a conjecture presented as a result.

**The logical structure of the four cells:**

| Stage 1 | Stage 2 | Population under current construction |
|---------|---------|---------------------------------------|
| ✅ pass | ✅ pass | Observable particles (15-state spectrum) |
| ✅ pass | ❌ fail | Short-lived resonances (d=3 n=2,3 modes) |
| ❌ fail | ✅ pass | **Empty** — no Σ_pairs member fails Stage 1 |
| ❌ fail | ❌ fail | Absent entirely |

**What could produce a dark sector.** Two genuine avenues remain open:

1. *Extension to d=7,8,9.* These sectors are geometrically permissible (supercritical Gegenbauer b_{k₀} > 1/2 means localisation is not excluded) but the coupling construction does not reach them (Rule A, Part 1 §3a). If the coupling were extended to d=7,8,9, each new active sector would have its own generation tower and its own Σ_pairs; modes in those sectors would not be reached by the d=2–10 tower's Stage-1 visibility filter, and could plausibly have negligible d=3 amplitude. This is a genuine extension, not a reuse of existing indices.

2. *Sector-universal stability from EOM analysis.* If the EOM analysis (open item MC-4, Part 6) shows that the decoherence mechanism underlying P8 depends only on n and is independent of d — e.g., because the rank-1 coupling (P6) makes the stability eigenvalue sector-agnostic — then n ∈ Σ_indices could be stable in any active sector. This would recover something like the original velino/umbron/liminon picture, but derived rather than assumed. This derivation has not been attempted.

Until one of these is carried through, IDWT makes no dark matter prediction.

---


## 2.9 CP^d Heat Kernel and Dimensional Visibility

The sector dimensional visibility is given by the first-principles heat-kernel derivation below: A_rel = exp(−c_d λ̂_d) with c_d = d/(d+1)².

**Setup.** Sector d corresponds to CP^d with Fubini-Study metric. The Laplacian eigenvalues on CP^d are E_n = n(n+d)/L_d² where L_d = λ_d^{−1/4} is the sector localization length (harmonic oscillator length of the ground-state mode; Part 4 §3.9). The gap to the first excited multiplet: E₁ = (d+1)/L_d² = (d+1)√λ_d.

**Breaking operator.** The lowest-degree spurion breaking SU(d+1) → SU(d)×U(1):
```
V_kernel(z) = λ_d (1 − |⟨e₁|z⟩|² / ⟨z|z⟩) = λ_d r²/(1+r²)
```
Gauge-invariant, unique lowest-rank perturbation coupling only n=0 and n=1 sectors. Note: this spurion is a perturbation on the CP^d Fubini-Study geometry used in the heat-kernel derivation; it is distinct from the sector confinement potential (§3.10.2), which is the harmonic well λ_d r².

**Dimensional visibility:**
```
A_rel = exp(−c_d λ̂_d),    c_d = d/(d+1)²,    λ̂_d ≡ λ_d L_d² = √λ_d

where L_d = λ_d^{−1/4} is the sector localization length. Numerically λ̂_d = √λ_d
varies across sectors (7.12, 2.20, 1.31, 0.40, 0.50, 0.50 for d=2,3,4,5,6,10).
```

| Sector | d | c_d = d/(d+1)² |
|--------|---|----------------|
| Gauge boson | 2 | 0.222 |
| Down quarks | 3 | 0.188 |
| Up quarks | 4 | 0.160 |
| Neutrinos | 5 | 0.139 |
| Leptons | 6 | 0.122 |
| Tau | 10 | 0.083 |

**Colour protection.** For sectors d=3,4 (quarks), Φ†P₁Φ is not an SU(3)_c singlet and is gauge-forbidden. Therefore λ_d = 0 for quarks automatically — all their activity is in our d=3 dimensions. For d=2,5,6,10 (gauge bosons, neutrinos, leptons, tau), Φ is a colour singlet and λ_d > 0 is allowed. This is why quarks are fully visible while leptons and neutrinos have activity in d>3 sector coordinates.

**KK excitation energies.** First excited modes on CP^d have energy ΔE ≈ (d+1)/L_d². For macroscopic L_d (the mode is spread over macroscopic scales), ΔE is negligibly small and completely unobservable. There is no KK tower — excited modes above the ground state fail Stage-1 for the same reason scattering states do: their activity is spread too far into extra dimensions to be detectable at d=3.

**Caveats:**
1. **Symbol disambiguation:** In the heat-kernel derivation below, the Laplacian eigenvalue at level n in sector d is n(n+d−1) — a different quantity from the IDWT simplex count S(n,d) = C(n+d−1,d). To prevent confusion, the heat-kernel eigenvalue is written as E_n = n(n+d−1) throughout §2.9; S(n,d) always denotes the IDWT simplex count.
2. A_rel controls **observability** — what fraction of a mode's vibrational activity is in our d=3 dimensions. It does not affect the mode frequency itself. The d=5 sector mass scale m_scale_5 is suppressed because χ(S⁵)=0 forces its frequency scale to be determined by the cross-sector Hopf equation m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³, not by dimensional visibility. Mass is a frequency. Stage-1 does not set frequencies.
3. λ̂_d = √λ_d values are fully determined by the sector coupling constants via λ_d = (g_dd/2)^{2/3}. The heat-kernel formula A_rel = exp(−c_d √λ_d) gives a correctly-ordered visibility gradient: d=2 largest (√50.7≈7.1), falling to d=5,6,10 smallest (√0.16–0.25≈0.4–0.5). The operative primary visibility measure is |χ_0(0)|² ∝ λ_d^{d/4} (Part 4 §3.11), which gives the same ordering and is exact for the Gaussian ground state.

### 2.9.1 Stage-1 Projection Theorem ⭐

The ln 2 threshold in the Stage-1 condition Ω_log ≤ ln 2 is not fitted or hand-placed. It follows from a purely combinatorial majority-support criterion on the state space of each mode.

**Setup.** Associate mode (n,d) with the polynomial space V = Sym^{≤n-1}(ℝ^d) of total degree ≤ n-1 in d variables. The IDWT mass eigenvalue m(n,d) = m_scale_d × S(n,d) is proportional to dim(V) = S(n,d) = C(n+d-1, d). Equivalently, S(n,d) = dim Sym^{n-1}(ℝ^{d+1}), the degree-(n-1) symmetric tensor space on ℝ^{d+1}; this is the homogeneous form of the same identity. The observable reference subspace is W = Sym^{≤n-1}(ℝ^2) ⊂ V, the polynomials depending only on 2 of the d coordinates. It satisfies dim(W) = S(n,2) = C(n+1, 2) = n(n+1)/2.

In the Sym^{n-1}(ℝ^{d+1}) framing, the projection ratio S(n,2)/S(n,d) = dim Sym^{n-1}(ℝ^3) / dim Sym^{n-1}(ℝ^{d+1}) is the fraction of degree-(n-1) symmetric tensor degrees of freedom on ℝ^{d+1} that survive projection into the 3-dimensional observable subspace. Stage-1 is therefore a representation-compression ratio: how much of the mode's tensor support fits within observable geometry.

**Theorem (Stage-1 Projection Identity) ⭐.**
Let Π_obs: Sym^{≤n-1}(ℝ^d) → Sym^{≤n-1}(ℝ^2) be the orthogonal projection onto the observable subspace. Then:

```
dim(range Π_obs) / dim(V) = S(n,2) / S(n,d) = exp(−Ω_log(n,d))
```

*Proof.* S(n,d) = C(n+d-1, d) is the dimension of Sym^{≤n-1}(ℝ^d) by polynomial counting; S(n,2) = C(n+1,2) is the d=2 special case; W ⊂ V is an exact subspace embedding. The equality S(n,2)/S(n,d) = exp(−Ω_log) follows directly from the definition Ω_log = ln(S(n,d)/S(n,2)). □

The sector potential V_d(r) = λ_d r²/(1+r²) is fully isotropic in Ξ_d, so the ground-state occupancy is uniform over the S(n,d)-dimensional eigenspace. By the standard Hilbert subspace projection formula, the expected observable fraction for a uniformly distributed state vector equals dim(W)/dim(V) = S(n,2)/S(n,d) exactly.

**Operator form.** Let Π_obs: H_∞ → H_2 be the orthogonal projector onto the d=2 observable sector. The observable component of mode (n,d) is Ψ_obs^{(n,d)} = Π_obs Ψ_{n,d}, with observability weight:

```
O[Ψ_{n,d}] = ||Π_obs Ψ_{n,d}||² / ||Ψ_{n,d}||² = S(n,2)/S(n,d) = exp(−Ω_log)
```

Stage-1 is the condition O ≥ 1/2. The projector Π_obs is not defined via a spectral decomposition of Ψ_∞ — it is defined by the geometric embedding Ξ_2 ⊂ Ξ_d, which is a property of M_∞'s coordinate structure independent of any field configuration (P1 dependency structure, Part 1 §1).

**Corollary (ln 2 from majority support) ⭐.**
The condition that at least half the spectral support of mode (n,d) lies in the observable d=2 reference subspace is:

```
S(n,2) / S(n,d) ≥ 1/2  ⟺  Ω_log ≤ ln 2
```

The ln 2 threshold is the majority-support localization criterion. It involves no free parameters and is not adjusted to fit the observed spectrum.

**Ontological note.** Stage-1 does not delete modes. Every (n,d) mode exists as a candidate resonance of M_∞ regardless of Ω_log. Stage-1 quantifies what fraction of a mode's spectral support is resolvable in the d=2 observable subspace. Modes with Ω_log > ln 2 have less than half their spectral activity in the observable subspace — they are not absent, they are geometrically buried. The Stage-2-pass / Stage-1-fail population (§2.6) is exactly this: modes whose state-space projection onto the d=2 reference is minority-weight but whose co-fixed-point index makes them stable resonances.

**Structural observation — n_s from the Stage-1 boundary (⭐ algebraic identity).** The ratio S(n,d)/S(n,d+1) = (d+1)/(n+d) is an exact algebraic identity (Appendix A §18). Setting it to 1/2 gives n = d+2 universally — the Stage-1 boundary is always two above the sector dimension. At d=2 specifically: S(n,2)/S(n,3) = 3/(n+2), which equals 1/2 at n=4. Therefore:

```
n_s = 4 = the unique n at which S(n,2)/S(n,3) = 1/2
         = d=2 case of the universal Stage-1 boundary formula n = d+2
```

The seed value $n_s = 4$ is the Stage-1 boundary mode of the d=3 sector: the last mode satisfying the majority-support condition when viewed from d=2. This provides an alternative derivation of $n_s=4$ purely from the visibility structure, complementing the topological derivation via $\chi(\mathbb{CP}^3) = 4$ (Part 1 §3). The two routes agree — a structural self-consistency check. (Quarks bypass Stage-1 via colour protection regardless of $n$, so this does not mean quark modes with $n > 4$ are unphysical; it means the seed sits at the visibility threshold.)

**Large-n asymptotics. ⭐** Using S(n,d) ~ n^d/d! for large n:

```
S(n,2)/S(n,d) ~ (d!/2) n^{2-d}

Ω_log(n,d) ~ (d-2) ln n + ln(2/d!)
```

The participation ratio S(n,2)/S(n,d) decays as n^{2-d}: algebraically for d=3 (~1/n), and as fast as n^{-8} for d=10. The entropy depth Ω_log grows as (d-2) ln n — linear in spectral codimension (d-2) and logarithmic in mode index. No mechanism or tuning produces this: dimensional structure alone drives the delocalization of high-index modes from the observable subspace.

---

## 3. CP^d Coordinate Geometry 🔶

**What is established:**
- Exponential hierarchy A_rel = exp(−c_d λ̂_d) with geometrically fixed c_d = d/(d+1)²
- Colour protection: quarks get λ_d = 0 automatically (gauge argument)
- Sector excitation gap: ΔE ≈ (d+1)/L_d² where L_d is the sector localization length (Part 4 §3.9) — negligibly small for macroscopic L_d, so no KK-tower states are accessible

**What remains open:**
- Deriving λ_d from sector geometry (the identification λ_d ∝ curvature of Ξ_d requires computing how the breaking operator coupling relates to the intrinsic geometry; L_d = λ_d^{−1/4} and G_eff then follow)
- Deriving the 3D gauge group from U(d) subgroups

**Explicitly NOT an open item:** The neutrino sector mass scale is not a Stage-1 problem. The mass scale m_scale_5 ≪ m_scale_3 is a frequency-domain result — the Hopf consistency equation sets the sector scale. A_rel affects only how much of a neutrino mode's vibrational activity is in the d=3 coordinates an observer at our coordinate level can resolve; it plays no role in determining the mode's frequency.

| IDWT result | Heat-kernel interpretation |
|-------------|---------------------------|
| m_scale_d hierarchy | Set by vacuum stability fixed-point and cross-sector Hopf coupling equations — a **frequency-domain** property. A_rel controls observability only (how much of a mode's vibrational activity is in our d=3 dimensions), not the mode frequency. The d=5 neutrino mass scale is suppressed because its sector has no self-confinement (χ(S⁵)=0), fixed by m_scale_5 × m_scale_4² = (n_u/n_s) × m_scale_6³. Stage-1 plays no role in setting mass. |
| Quarks fully visible | Colour protection forces λ_d = 0 for triplets |
| Stage-1 heuristic A_rel | Replaced by exp(−c_d λ̂_d) with geometrically fixed c_d |
| Vacuum stability fixes g₃₃ | Analogous: vacuum stability should fix λ̂_d |

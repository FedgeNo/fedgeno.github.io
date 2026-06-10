# Infinite Dimensional Wave Theory — Part 11: Chemistry

**Status key:** ⭐ Identity · ✅ Structural consequence · 🔵 Numerically verified · 🔶 Motivated / open · ❓ Conjecture

---

## Overview

Part 11 develops chemistry from the d=6 orbit structure established in Part 8. The boundary between the two documents is fixed as follows: the single-electron machinery — the hydrogen Hamiltonian and its exact potential separability (Part 8 §14.2, Lemma 1), the orbit state classification Sym^L(ℂ⁴) under SU(4) ⊃ SU(3) ⊃ SO(3) with its observable and CP³-hidden states (Part 8 §14.3), the selection rules (Lemma 2), and the Bohr spectrum — lives in Part 8 and is used here by reference. Part 11 begins where more than one electron, or more than one nucleus, enters.

Three established results are inherited throughout:

- The electron is the (n=13, d=6) mode of Ψ∞, executing a 6D orbit on the CP³ sector; the s, p, d, f orbital shapes are the d=3 projections of its orbit angular-momentum eigenstates (Part 1 §3d; Part 8 §14.3).
- A d=3 observer sees an exact 1/R Coulomb potential from any sector d ≥ 3 (Part 3 §0.8a, Coulomb projection theorem); the atomic force law carries no correction from the hidden CP³ coordinates.
- Pauli exclusion is a structural consequence of the fermionic anticommutation of Ψ∞ (Part 1 §7; Part 8 §14.4): co-present electron resonances are distinct modes.

Part 8 also establishes the multi-electron and molecular setting this Part works in: the two-electron Hamiltonian with the repulsion term as the same Coulomb vertex (Part 8 §16.1), exchange antisymmetry from the spinor anticommutation (§16.2), the Aufbau filling structure (§16.4), and the two-center bond mechanism with Born–Oppenheimer decoupling (§17). What Part 8 leaves open — quantitative bond parameters, bond angles (§17.6), correlation energies — is the business of this Part. Every result here is stated with its premises explicit, and each status label applies to the result *given those premises*; §4 derives the premises of §1 from the Part 8 structure to the extent currently possible.

---

## §1. Hybridisation Angles from Orbit-State Orthogonality

### 1.1 Setting and premises

Hybridisation in IDWT is a basis choice, not a mixing process: the SU(4) isometry of CP³ rotates exactly between the d=3 projections of the electron's orbit angular-momentum eigenstates, and the electron settles into the angular-momentum configuration of its 6D orbit that fits its bonding environment (Part 1 §3d). The states available to a bonding electron at a single center, at lowest angular momentum, are the L=0 and L=1 observable orbit states of Part 8 §14.3:

```
V = span{ |s⟩, |p_x⟩, |p_y⟩, |p_z⟩ }     (four orbit states)
```

Every state in V is a full 6D orbit state of the d=6 electron — the labels s, p refer to its observable harmonics, not to a 3D object. The L=1 level also contains one CP³-hidden state (the z₄ direction, Part 8 §14.3); it is excluded from V not by neglect but by Lemma 2: the nuclear potential that shapes the bonding environment is a d=3 structure, and no d=3 operator connects the hidden state to the observable ones, so it takes no part in selecting bond directions.

A hybrid orbit state along the unit direction **n**_i ∈ ℝ³ is

```
|h_i⟩ = a_i |s⟩ + b_i ( n_i · |p⟩ ),     a_i² + b_i² = 1,
```

where a_i² is the s-share of the state. The premises:

- **P1 (orbit states). ✅ in the degenerate-shell idealization (§4.2).** Each σ-bonding electron at the center occupies a hybrid orbit state |h_i⟩ ∈ V whose direction **n**_i is the internuclear axis of its bond. The state space V is established (Part 8 §14.3); the directed zonal form is derived in §4.2 from the axial symmetry of the companion nucleus's potential, exactly in the degenerate-shell idealization, with the s–p splitting of multi-electron centers as the stated refinement.
- **P2 (orthogonality). ✅ (§4.1).** The n co-present bonding resonances at the center are distinct modes of Ψ∞ and their orbit states are mutually orthogonal. This is derived in §4.1 from exchange antisymmetry (Part 8 §16.2): the n-electron state depends only on the occupied subspace, so the directed states may always be taken orthonormal.
- **P3 (equivalence). ✅ given identical ligands (§4.3).** The n bonds are equivalent: the n hybrid states are related by a symmetry of the center and have equal s-share. Derived in §4.3 for n identical ligands whose arrangement symmetry acts transitively on the bond axes.

### 1.2 The angle identity

⭐ **Theorem (hybridisation angles).** Let |h_1⟩, …, |h_n⟩ (2 ≤ n ≤ 4) be orthonormal states of the form above whose span contains |s⟩, with equal s-shares. Then

```
n_i · n_j = −1/(n−1)     for all i ≠ j.
```

*Proof.* Since the |h_i⟩ are an orthonormal basis of a subspace containing |s⟩, completeness gives Σ_i |⟨s|h_i⟩|² = Σ_i a_i² = 1; equivalence gives a_i² = 1/n for each i. Orthogonality of a pair then reads

```
⟨h_i|h_j⟩ = 1/n + (1 − 1/n)( n_i · n_j ) = 0   ⟹   n_i · n_j = −1/(n−1).  ∎
```

The identity is pure linear algebra — it holds for any states of this form, with or without the IDWT postulates. The bond angles follow:

| Configuration | n | cos θ | Angle |
|---|---|---|---|
| sp | 2 | −1 | 180° |
| sp² | 3 | −1/2 | 120° |
| sp³ | 4 | −1/3 | 109.471° |

The sp³ entry is the tetrahedral angle arccos(−1/3) = 109.47° of Part 1 §3d, obtained here from the orbit state space with no input beyond P1–P3.

⭐ **Capacity remark.** V holds four mutually orthogonal states in all, so a center bonding through L ≤ 1 orbit states supports at most four σ bonds. Larger coordination requires L=2 orbit states (the d-shell), which enlarges the available state set; the six-coordinate case is worked out in §1.6.

### 1.3 Numerical verification

🔵 `files/idwt.py` STEP 42 constructs the hybrid states explicitly for n = 2, 3, 4 (collinear, trigonal planar, tetrahedral direction sets), confirms orthonormality to machine precision, and reproduces 180°, 120°, 109.471°.

### 1.4 Non-equivalent hybrids: water 🔶

Dropping P3 while keeping P1–P2: oxygen in H₂O carries four hybrid orbit states — two bond states (each reaching an H nucleus) and two lone-pair states. Parameterise the s-share asymmetry as a_bond² = 1/4 − δ, a_lone² = 1/4 + δ (the completeness sum Σ a_i² = 1 is preserved). Orthogonality of the two bond states gives

```
cos θ_HOH = −(1/4 − δ) / (3/4 + δ).
```

The measured H–O–H angle of 104.5° corresponds to δ = 0.050, i.e. lone-pair states with five percentage points more s-share than bond states; the same δ puts the lone-pair axes at 115.4°. The value of δ is fitted to the measured angle, not predicted; deriving δ from the oxygen nuclear charge and bonding environment is an open calculation. *Cross-framework comparison:* in quantum-chemistry language this s-share asymmetry is Bent's rule; here it is a statement about the s-content of orbit states, and the comparison is not a derivation.

Ammonia fits the same one-parameter family: nitrogen carries three bond states with s-share 1/4 − δ and one lone-pair state with s-share 1/4 + 3δ (the factor 3 preserves the completeness sum Σ a_i² = 1). Bond-state orthogonality gives the same relation cos θ_HNH = −(1/4 − δ)/(3/4 + δ); the measured H–N–H angle of 107.8° corresponds to δ = 0.016. The fitted values order by lone-pair count — δ(CH₄) = 0 < δ(NH₃) = 0.016 < δ(H₂O) = 0.050 — which is the qualitative content of the family: each value is fitted, the monotone trend is the observation. 🔶 (`files/idwt.py` STEP 43.)

### 1.5 What is open

- The selection mechanism: §4.2 derives the directed zonal form of the bonding states at leading multipole order in the degenerate-shell idealization; the remaining energetics (the promotion-energy crossover and the symmetric ligand arrangement) are listed in §4.5.
- The quantitative two-center orbit: the bond mechanism is established (Part 8 §17), but the bond parameters (D_e, R_eq) and the full 6D character of the two-center orbit are open (Part 8 §17.6).
- δ for non-equivalent centers (§1.4) from first principles.

### 1.6 The general zonal identity and six-coordinate centers

The theorem of §1.2 extends to higher angular momentum. Call a hybrid orbit state *zonal* if it is built from the axially symmetric degree-L components about its own bond axis — true of the σ-bonding hybrids considered here, whose observable harmonics are symmetric about the internuclear axis.

- **P1′ (zonal form). 🔶** Each σ-bonding hybrid at the center is zonal about its bond axis, with angular-momentum shares c_L² (Σ_L c_L² = 1, c_0² the s-share).

⭐ **Overlap identity.** For two zonal hybrids along **n**_i and **n**_j, the spherical-harmonic addition theorem gives

```
⟨h_i|h_j⟩ = Σ_L c_L² P_L( n_i · n_j ),
```

with P_L the Legendre polynomials. §1.2 is the L ≤ 1 case, where the identity reads 1/n + (1 − 1/n)x = 0.

⭐ **Six equivalent bonds (sp³d²).** Six equivalent zonal hybrids through L ≤ 2 span the nine observable states of L ≤ 2 only partially: the six hybrids exhaust |s⟩, the three |p⟩ states, and two zonal d states, so completeness forces the shares c_0² = 1/6, c_1² = 1/2, c_2² = 1/3 (sum = 1). Orthogonality of any pair then reads

```
1/6 + x/2 + (1/3) P₂(x) = 0   ⟺   3x² + 3x = 0   ⟺   x ∈ {0, −1}.
```

Every pair of bond directions is forced to be perpendicular or antipodal, and six unit directions with pairwise cosines in {0, −1} are three orthogonal axes: the octahedron. The 90° geometry of six-coordinate centers (e.g. SF₆) follows from the shares and orthogonality alone, with no angle put in by hand.

⭐ **Equiangular cap.** n directions in the three observable coordinates with equal pairwise cosine c have Gram matrix (1−c)I + cJ, with eigenvalues 1−c (multiplicity n−1) and 1+(n−1)c; realizability requires rank ≤ 3, forcing c = −1/(n−1) and n ≤ 4. At most four equivalent equiangular σ directions exist. A five-coordinate center therefore cannot carry five equivalent bonds of the §1.2 form — consistent with the axial/equatorial inequivalence observed at five-coordinate centers (PF₅), though the trigonal-bipyramidal geometry itself is not derived here. 🔶

🔵 Numerical verification: `files/idwt.py` STEP 43 (explicit octahedral Gram matrix orthonormal to machine precision; orthogonality roots; equiangular Gram rank).

---

## §2. Program

The directions this Part is intended to develop, all currently open:

- **Helium and multi-electron atoms. 🔶** Electron–electron repulsion is the U(1) self-coupling of Ψ∞ on the shared d=2 coordinates of two d=6 resonances (Part 8 §14.4). A first variational bound on the helium ground state is in §3. Electron correlation involves the full 6D structure: two electrons in the same CP³ sector correlate through the sector coordinates as well as the d=3 projection, and the product-form deficit of §3 measures what that correlation must supply.
- **Shell filling and the Madelung order. 🔶** The 2(2L+1) shell counts are established (Part 8 §14.3); the energy ordering of shells in multi-electron atoms (why 4s fills before 3d) requires the screened effective potential and is an open calculation.
- **Crystal field structure. 🔶** The branching of the observable d-shell states under a ligand point group reproduces the standard decomposition (e.g. e_g ⊕ t_2g under O_h); splitting magnitudes require 6D energy integrals, not representation theory alone. The IDWT-specific content is the CP³-hidden states (four in the d-shell) and their strict inaccessibility (Part 8 §14.3, Lemma 2).
- **Dispersion forces. ❓** A candidate reformulation of London dispersion as overlap of the two atoms' d=6 mode structures on their shared d=2 coordinates, with polarisability as the susceptibility of the 6D orbit to deformation along the d=2 directions.

---

## §3. Helium: a First Variational Bound 🔶

### 3.1 The Hamiltonian

The d=3 marginal Hamiltonian for two electrons at a Z=2 nucleus is established in Part 8 §16.1:

```
H = Σ_{i=1,2} [ −∇_i²/(2m_e) − Zα/r_i ] + α/r₁₂.
```

The single-electron part is exact (Part 8 §14.2, Lemma 1); the repulsion term is the same Coulomb vertex — the U(1) self-coupling of Ψ∞ on the d=2 coordinates the two d=6 resonances share — with no new coupling introduced (Part 8 §16.1). What remains open is the two-electron problem in the full 6D coordinates: how the two resonances correlate through the CP³ sector directions, beyond what the d=3 marginal resolves.

### 3.2 The bound

With a product trial state of screened scale η (each electron in a hydrogenic ground state of charge η), the energy functional is E(η) = [η² − 2Zη + (5/8)η] α²m_e; the stationary point is η = Z − 5/16 = 27/16 and

```
E_He = −η² α²m_e = −2.84766 hartree     (hartree ≡ α²m_e).
```

The screening value 5/16 is the output of the repulsion integral, not an empirical input. The measured value (the sum of the two ionisation energies) is −2.90339 hartree; the bound lies 1.9% above it, as a variational bound must. This sharpens the first-order perturbative estimate of Part 8 §16.3 (−2.75 hartree, 5.3% above) using the same Hamiltonian. 🔵 (`files/idwt.py` STEP 44.)

The comparison is made in hartree units, where α and m_e cancel: the IDWT-derived α(0) carries a known −2.87% residual traced to the sin²θ_W structural gap (Part 3 §0.7), which would dominate an absolute-eV comparison, while the dimensionless −η² is the content specific to this section.

### 3.3 What the deficit is

The trial state is an uncorrelated product in the d=3 marginal. The 1.9% deficit is the energy the two-electron correlation must supply. Under the established potentials this correlation is fixed by the d=3 marginal problem — the repulsion α/r₁₂ is supported on the observable coordinates, so the marginal exactness theorem (§6.1) applies and the exact answer is the standard correlated one. The open 6D question is therefore not whether correlation differs under the established potentials (it cannot), but whether the cross-sector kernel contact terms leave any residue at chemical scales (§6.1 scope condition). No claim is made here beyond the bound.

---

## §4. Deriving the Premises of §1

The angle theorem of §1.2 rests on premises P1–P3. This section derives them from the Part 8 structure, in decreasing order of completeness. (`files/idwt.py` STEP 45 verifies the computational content.)

### 4.1 Orthogonality is a property of fermionic occupancy ✅

The n bonding electrons at a center form an antisymmetric n-electron state — exchange antisymmetry is established from the spinor anticommutation of Ψ∞ (Part 8 §16.2). An antisymmetrised product of single-particle states |h_1⟩, …, |h_n⟩ has a basis-change property: replacing the |h_i⟩ by any other basis of the same span multiplies the state by the determinant of the basis change — a scalar. The physical n-electron state therefore depends only on the occupied *subspace* of V, not on which basis describes it. Any set of directed states spanning that subspace may be taken orthonormal without changing the physical state.

P2 is thus not an assumption about dynamics; it is a statement of which descriptions are physically equivalent. The content of the angle theorem shifts accordingly: orthogonality is free, and the physics lies in P1 (the subspace admits a basis of bond-directed zonal states) and P3 (with equal s-shares). ✅

### 4.2 The directed zonal form from axial symmetry ✅ (degenerate-shell idealization)

Consider one bond: the electron at center A, with a companion nucleus B at distance R along the unit direction **n**. The potential of B is a d=3 structure (Part 1 §3i) and enters the electron's d=3 marginal exactly as the Part 8 Hamiltonian does — the Lemma 1 separation applies per electron, so the analysis lives in the established d=3 effective problem.

The potential of B is axially symmetric about **n**. Decompose the degenerate L ≤ 1 shell by angular momentum about the **n** axis: |s⟩ and |p_n⟩ carry m = 0; the two transverse p states carry m = ±1 and vanish on the axis. The leading multipole of B's potential across the shell is the dipole term, and its matrix elements respect the axial symmetry: it couples |s⟩ ↔ |p_n⟩ and nothing else. On the hydrogenic n_H = 2 shell the only non-zero element is ⟨2s|z|2p₀⟩ = −3a₀ (radial quadrature, STEP 45); the perturbation eigenstates are (|s⟩ ± |p_n⟩)/√2 with the bound combination directed toward B, while the m = ±1 states are unshifted at this order.

The bound state of the block is therefore a zonal hybrid directed along the internuclear axis — the form P1 assumes. Within the degenerate-shell idealization this is derived, not chosen. ✅ The stated refinement: in a multi-electron center the s and p levels of the same shell are split by inner-electron screening, so the mixing at finite bonding strength is partial rather than maximal; the bonding regime is the one in which the off-diagonal coupling dominates that splitting. Quantifying the crossover (the promotion-energy threshold of bond formation) is an open calculation. 🔶

### 4.3 Equal shares from ligand symmetry ✅ (given identical ligands)

Let the n ligands be identical nuclei whose arrangement is invariant under a symmetry group G acting transitively on the bond axes, and let the occupied bonding subspace be G-invariant (the non-degenerate ground configuration). Then G permutes the bond-directed hybrid states of §4.2 among themselves while fixing |s⟩ (the L = 0 state is isotropic), so all n s-shares are equal. ⭐ as linear algebra; the physical input is that n identical ligands bind in a symmetric arrangement, which is the energetics statement that remains open (§4.5).

### 4.4 The completeness loop ⭐

The §1.2 proof needs Σ_i a_i² = 1 — the occupied bonding subspace must contain |s⟩ entirely. This closes by counting. The perturbations of §4.2 couple |s⟩ only to p components along the bond directions. If the n bond directions span a (n−1)-dimensional subspace of the three observable directions, the n bonding states lie in span{|s⟩, p along that span} — n states in a space of n states — so the bonding subspace *is* that span, and it contains |s⟩. Completeness applies, the shares are 1/n, and the angle theorem delivers cos θ = −1/(n−1).

The loop then closes on itself: the derived angles realize exactly the direction-span assumed. n = 2 gives 180° — collinear, a 1-dimensional direction span; n = 3 gives 120° — coplanar, 2-dimensional; n = 4 gives 109.47° — fully 3-dimensional. Each case is self-consistent, and the impossible cases exclude themselves: three collinear bonds would require three orthonormal states in a span of two states. A center whose bond directions span fewer dimensions than n−1 cannot bind n equivalent ligands through L ≤ 1 states at all.

Centers with lone pairs sit outside the loop deliberately: there the full four-state space is occupied (bonds plus lone pairs), completeness holds over all four states, and the share asymmetry δ of §1.4 — not yet derived — sets the geometry.

### 4.5 What remains open after §4

- The energetics: that n identical ligands adopt the symmetric arrangement (the input of §4.3), and the nuclear positions themselves, follow from minimising the total energy over the Born–Oppenheimer surface (Part 8 §17). Not yet computed for any polyatomic case.
- The promotion-energy crossover of §4.2 (degenerate-shell idealization vs the real s–p splitting of carbon, nitrogen, oxygen).
- The lone-pair share asymmetry δ (§1.4).
- The full 6D character of the two-center orbit (Part 8 §17.6).

---

## §5. Aromatic Ring Current: Closed-Shell Scaling 🔶

Part 8 §17a establishes the benzene π system as one 6D orbit coupling to all six centers, with the 4n+2 closed-shell rule as a structural consequence, and names the ring current as its direct experimental signature. This section adds the leading quantitative scaling, in the rigid-ring model.

⭐ **Within the model.** The angular modes of the ring orbit on a ring of radius R, threaded by applied flux φ, have energies ε_m = (m − φ/φ₀)² E_R with E_R = ℏ²/(2m_e R²); the level current is I_m = −∂ε_m/∂φ, linear in (m − φ/φ₀). For a closed shell — m = −n … n, doubly occupied — the m-linear parts cancel in the sum and the field-induced parts add over all 2(2n+1) electrons:

```
I_induced ∝ 2(2n+1) = N_π,
```

the π-electron count, independent of R (the flux φ = BπR² cancels the R² in E_R). The top filled level is m_max = n = (N_π − 2)/4. The induced dipole field opposes the applied field inside the loop and reinforces it in the outer plane: inner protons shielded, outer protons deshielded — the observed annulene pattern ([18]annulene: outer 9.28 ppm, inner −2.99 ppm). A half-filled top level (4n electron systems) breaks the cancellation and reverses the response, the antiaromatic paramagnetic current. (`files/idwt.py` STEP 46.)

🔶 **Status.** The scaling I ∝ N_π and the sign geometry are exact within the rigid-ring model; the model itself is the approximation. Real annulenes relax geometrically with size, and the proton shifts depend on position relative to the loop, so the testable consequence — inner-proton shielding of large annulenes growing stepwise with N_π — requires the geometric refinement before it is a sharp number. Open.

---

## §6. Marginal Exactness: What 6D Chemistry Is

### 6.1 The theorem ✅

✅ **Theorem (marginal exactness of chemistry).** Let a system of bound electrons be governed by potentials that separate per Part 8 Lemma 1 — nuclear Coulomb terms supported on the observable coordinates **r**, sector confinement supported on the CP³ coordinates ξ — and let O be any observable supported on the observable coordinates. This covers every chemical probe: energies, geometries, spectra, electric and magnetic response, including the electron–photon vertex (Part 8 §15), since the d=2 coupling acts on shared observable coordinates. Then for product eigenstates ψ ⊗ χ,

```
⟨ψ ⊗ χ_a | O | ψ′ ⊗ χ_b⟩ = ⟨ψ|O|ψ′⟩ δ_ab,
```

so every expectation value and transition amplitude is fixed by the d=3 marginal dynamics alone; the sector factor drops out, and CP³-hidden components contribute nothing (Lemma 2). Since the d=3 marginal Hamiltonian is the standard molecular Hamiltonian with IDWT-derived inputs (Part 8 §14.2, §16.1, §17.1), IDWT reproduces standard molecular structure and response theory for every chemistry observable measured by a d=3 apparatus — vibrational and isotopic effects included, since nuclear motion is likewise a d=3 structure. (`files/idwt.py` STEP 47.)

This is the chemistry-wide form of the Coulomb projection consistency of Part 3 §0.8a: the framework does not disturb tested chemistry. A corollary cuts in the other direction: no chirality, spectroscopy, or kinetics experiment performed with 3D apparatus can deviate from the standard-theory result within the established structure. Proposals of such deviations are not open items — they are excluded.

🔶 **Scope condition.** The theorem covers the established potentials. Whether the cross-sector kernel contact terms contribute any residue at chemical energy scales is the one stated caveat. §6.3 bounds it.

### 6.2 What 6D chemistry consists of

Given §6.1, the content of 6D chemistry is three things, none of which is a deviating lab number:

- **Foundation.** What standard chemistry postulates, IDWT derives: Pauli exclusion from spinor anticommutation (Part 8 §16.2); the 2L+1 degeneracies, shell counts, and selection rules from the SU(4) ⊃ SU(3) ⊃ SO(3) chain and ξ-orthogonality (Part 8 §14.3); the bond mechanism (Part 8 §17); the bond angles from orbit-state orthogonality with the premises derived (§1, §4); the Hückel rule and ring-current scaling (Part 8 §17a, §5). The observed numbers are unchanged; their status changes from axiom to theorem of the sector geometry.
- **Ontology and falsifier.** The CP³-hidden orbit states exist at every shell L ≥ 1 and are strictly inaccessible to 3D apparatus at any order (Part 8 §14.3, Lemma 2). Standard QM has no counterpart states. Any measured coupling to one falsifies the d=6 sector identification — a standing, permanent discriminator.
- **Frontier.** The one place a quantitative residue could appear is the cross-sector kernel contact contribution at chemical scales (§6.1 scope condition); §6.3 bounds it at the 10⁻¹⁰ level — nil for all chemistry. Independent of observables, the orbit trajectory geometry in the CP³ coordinates (Part 8 §14.4) remains the structural frontier. 6D chemistry is the foundation and the ontology.

### 6.3 The kernel residue bound 🔶

The scope condition of §6.1 closes in two steps.

✅ **Cancellation lemma.** Any kernel component supported on the sector factor alone shifts every atomic and molecular state by the same amount: by Lemma 1, all chemistry states of an electron share one sector eigenstate, so the component's expectation is state-independent and cancels in every measurable difference — spectra, bond energies, barriers are all energy differences. Only kernel components with observable-coordinate support can leave a residue.

🔶 **Bound on the remainder.** The kernel is a contact structure (the colour coupling is its clearest case, Part 3 §0.6), with observable-coordinate range set by the sector length scale: L_6 = 1.414 fm (Part 1 §3e). A contact term of range L and depth V₀ shifts an s-state by ΔE ≈ V₀ |ψ(0)|² (4π/3)L³ with |ψ(0)|² = 1/(πa₀³), and shifts non-s states only at higher order in L/a₀ (their orbit-state density vanishes at contact). The depth premise: the kernel's entire l=0 output in the d=6 sector is the sector eigenvalue m_e, so a residual contact piece is bounded by the scale it generates, V₀ ≤ m_e — a deliberately generous bound. Then

```
ΔE / (α²m_e) ≤ (4/3)(L_6/a₀)³ × m_e/(α²m_e) = 4.8 × 10⁻¹⁰.
```

The kernel residue on any chemistry observable is at most a few parts in 10¹⁰ — the same order as the proton-finite-size correction already catalogued in Part 8 §14.4, three orders below Lamb-scale effects, and far below any chemical measurement. (`files/idwt.py` STEP 48.)

**Consequence.** With the cancellation lemma exact and the remainder bounded at 10⁻¹⁰, the §6.1 caveat closes: within the established framework, 6D chemistry has no measurable quantitative residue. Its content is the foundation and the ontology of §6.2. The premise that carries the 🔶 is the depth bound V₀ ≤ m_e; deriving the actual contact amplitude from the kernel normalization would convert the bound into a value, and is the remaining refinement.

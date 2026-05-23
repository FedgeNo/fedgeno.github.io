# Atomic Orbital Structure as CP³ Projection in IDWT

**Author:** Fedge No  
**Reference:** *Infinite Dimensional Wave Theory* (2026), [doi:10.5281/zenodo.19767493](https://doi.org/10.5281/zenodo.19767493)

---

## Abstract

In Infinite Dimensional Wave Theory, the charged lepton sector has dimension $d=6$ with local geometry $\mathrm{CP}^3$ and isometry group $\mathrm{SU}(4)$. The angular momentum eigenstates of the electron in the hydrogen atom are representations of $\mathrm{SU}(4)$, not of the observable $\mathrm{SO}(3)$ alone. Projection to the observable 3D slice via the subgroup chain $\mathrm{SU}(4) \supset \mathrm{SU}(3) \supset \mathrm{SO}(3)$ recovers the standard atomic orbital families with exact degeneracies $2L+1$ for shells $s, p, d, f$. The degree-$L$ holomorphic representation $\mathrm{Sym}^L(\mathbb{C}^4)$ of $\mathrm{SU}(4)$ has dimension $\binom{L+3}{3} = S(L+1,3)$ and contributes exactly $2L+1$ observable states after projection. The remaining $\binom{L+3}{3}-(2L+1)$ states split into two distinct classes: $L(L+1)(L+2)/6$ states carrying angular momentum in the hidden $\Xi_6$ fibre direction (spectroscopically dark by $\xi$-orthogonality, Lemma 2), and $L(L-1)/2$ non-harmonic degree-$L$ polynomials in $(z_1,z_2,z_3)$ (non-harmonic remnants of lower orbital shells, not new states). The exact separability of the hydrogen potential on $M_\infty = \mathbf{R}^3 \times \Xi_6$ — enforced by the $d=2$ electromagnetic coupling and the colour silence of $d=6$ — implies that the effective 3D Hamiltonian is exactly $H_{3\mathrm{D}} + m_e$, recovering the standard Bohr spectrum without correction. Every standard spectroscopic result — orbital degeneracy, Bohr levels, all EM multipole selection rules, Zeeman splitting, Stark mixing, Dirac fine structure, and hyperfine spectrum — follows from two lemmas about the CP³ sector geometry. The hidden-sector orbital states are not merely unobserved; $\xi$-orthogonality makes them structurally inaccessible to every 3D operator at every order.

---

## 1. Setup

### 1.1 The Electron as a d=6 Eigenmode

In IDWT (Part 1 §3g), the electron is the mode $(n=13,\, d=6)$: the 13th eigenmode of the sector-6 Dirac-Harmonic operator on $\mathrm{CP}^3$, with mass $m_e = m_{\mathrm{scale},6} \times S(13,6)$. The $d=6$ sector has six real sector dimensions. Per postulate P3, these are not compactified extra dimensions — they are full-size Riemannian spaces supporting exponentially localised bound states via the Agmon decay theorem. The label $\mathrm{CP}^3$ describes the local symmetry near the potential minimum $V_6(|\xi|) = \lambda_6 |\xi|^2/(1+|\xi|^2)$, not a global compactification.

### 1.2 The Hydrogen Atom on $M_\infty$

The hydrogen atom is the bound system of an electron ($d=6$) and a proton (quarks in $d=3$, $d=4$) interacting via the Coulomb potential. The electromagnetic interaction is mediated by the $d=2$ gauge sector (photon), which couples only to the 3D projected charge density:

$$\rho_{3\mathrm{D}}(\mathbf{r}) = \int |\Psi_e(\mathbf{r},\xi,t)|^2\, d^6\xi.$$

The Coulomb force acting on the electron's centre of mass is therefore purely in the three observable directions $(x,y,z)$. The electron's full wavefunction on $M_\infty = \mathbf{R}^{3,1} \times \Xi_6$ factors as:

$$\Psi_e(\mathbf{r},\xi,t) = \psi(\mathbf{r},t)\times\chi_{13}(\xi),$$

where $\chi_{13}(\xi)$ is the internal sector mode function (the exponentially localised bound state in $\Xi_6$ that makes the electron an electron) and $\psi(\mathbf{r},t)$ is the centre-of-mass wavefunction in 3D. The angular momentum quantum number $L$ labels the angular excitation of the electron's sector mode in $\mathrm{CP}^3 \subset \mathbb{C}^4$. Different orbital families ($s, p, d, f$) are different angular eigenstates of the same $n=13$ sector mode, all degenerate in sector energy since $H_6$ depends only on the radial excitation. The factorisation $\Psi_e = \psi \times \chi_{13}$ is not an approximation — it is exact, forced by the separability of the potential (Lemma 1 below).

---

## 2. The Projection Theorem

### 2.1 The Subgroup Chain

The three sectors relevant to atomic structure sit in a natural group-theoretic hierarchy:

| Sector | Geometry | Group |
|--------|----------|-------|
| $d=6$ | $\mathrm{CP}^3$ | $\mathrm{SU}(4)$ |
| $d=4$ | $\mathrm{CP}^2$ | $\mathrm{SU}(3)$ |
| Observable | $\mathbf{R}^3$ | $\mathrm{SO}(3)$ |

The relevant subgroup chain is:

$$\mathrm{SU}(4) \supset \mathrm{SU}(3) \supset \mathrm{SO}(3).$$

$\mathrm{SU}(3)$ is the isometry group of the $d=4$ quark sector ($\mathrm{CP}^2$, Part 3 §2), embedded in $\mathrm{SU}(4)$ via the coordinate nesting $\Xi_4 \subset \Xi_6$ (Part 1 §3a): the inclusion $\mathrm{CP}^2 \hookrightarrow \mathrm{CP}^3$ places $\mathrm{SU}(3)$ as the stabiliser subgroup of $\mathrm{SU}(4)$ fixing the $z_4=0$ hyperplane. Under the triplet embedding $\mathrm{SO}(3) \subset \mathrm{SU}(3)$, the fundamental $\mathbf{3}$ of $\mathrm{SU}(3)$ maps to the spin-1 representation of $\mathrm{SO}(3)$.

### 2.2 The Holomorphic Orbital Representations

At angular momentum $L$, the orbital states of the electron in the CP³ sector are classified by the holomorphic symmetric tensor representations of $\mathrm{SU}(4)$:

$$\mathrm{Sym}^L(\mathbb{C}^4), \qquad \dim = \binom{L+3}{3}.$$

These are the degree-$L$ homogeneous polynomial functions on $\mathbb{C}^4$ restricted to $\mathrm{CP}^3$.

| $L$ | Representation | Dimension $\binom{L+3}{3}$ | Orbital family |
|-----|---------------|---------------------------|----------------|
| 0 | $\mathbf{1}$ (trivial) | 1 | $s$ |
| 1 | $\mathbf{4}$ (fundamental) | 4 | $p$ |
| 2 | $\mathbf{10}$ (sym 2-tensor) | 10 | $d$ |
| 3 | $\mathbf{20}$ (sym 3-tensor) | 20 | $f$ |

### 2.3 Decomposition Under $\mathrm{SU}(4) \supset \mathrm{SU}(3) \times \mathrm{U}(1)$

The fundamental $\mathbf{4}$ of $\mathrm{SU}(4)$ decomposes under $\mathrm{SU}(3) \times \mathrm{U}(1)$ as $\mathbf{4} \to \mathbf{3} + \mathbf{1}$, where $\mathbf{3}$ is the fundamental of $\mathrm{SU}(3)$ and $\mathbf{1}$ is the $\mathrm{U}(1)$ singlet (the hidden fibre direction $z_4$). The symmetric tensor powers decompose as:

| $\mathrm{Sym}^L(\mathbf{4})$ | Under $\mathrm{SU}(3)$ |
|---|---|
| $\mathbf{1}$ | $\mathbf{1}$ |
| $\mathbf{4}$ | $\mathbf{3} + \mathbf{1}$ |
| $\mathbf{10}$ | $\mathbf{6} + \mathbf{3} + \mathbf{1}$ |
| $\mathbf{20}$ | $\mathbf{10} + \mathbf{6} + \mathbf{3} + \mathbf{1}$ |

where $\mathbf{6} = \mathrm{Sym}^2(\mathbf{3})$, $\mathbf{10} = \mathrm{Sym}^3(\mathbf{3})$ of $\mathrm{SU}(3)$.

### 2.4 Decomposition Under $\mathrm{SU}(3) \supset \mathrm{SO}(3)$

Under the triplet embedding $\mathrm{SO}(3) \subset \mathrm{SU}(3)$, with $\mathbf{3} \to$ spin-1:

| $\mathrm{SU}(3)$ rep | $\mathrm{SO}(3)$ decomposition |
|---|---|
| $\mathbf{1}$ | $j=0$ |
| $\mathbf{3}$ | $j=1$ |
| $\mathbf{6} = \mathrm{Sym}^2(\mathbf{3})$ | $j=2 \oplus j=0$ |
| $\mathbf{10} = \mathrm{Sym}^3(\mathbf{3})$ | $j=3 \oplus j=1$ |

### 2.5 The Projection

Projection to the observable 3D slice selects states with zero amplitude in the hidden-sector directions — precisely the highest-spin $\mathrm{SO}(3)$ irrep in each block. These are the harmonic (traceless) degree-$L$ polynomials in $(z_1,z_2,z_3)$, the standard spherical harmonics $Y_L^m$.

| $L$ | Total | Observable | IDWT-hidden | Lower-$j$ 3D |
|-----|-------|-----------|-------------|--------------|
| 0 | 1 | 1 ($j=0$: constant) | 0 | 0 |
| 1 | 4 | 3 ($j=1$: $z_1,z_2,z_3$) | 1 ($z_4$) | 0 |
| 2 | 10 | 5 ($j=2$: traceless) | 4 ($z_iz_4,z_4^2$) | 1 ($z_1^2+z_2^2+z_3^2$) |
| 3 | 20 | 7 ($j=3$: harmonic) | 10 (all $z_4$-dependent) | 3 ($r^2 z_i$) |

### 2.6 The Orbital Counting Theorem

⭐ **Theorem (pure representation theory).** At orbital angular momentum $L$, projection of $\mathrm{Sym}^L(\mathbb{C}^4)$ to the observable $\mathrm{SO}(3)$ selects exactly $2L+1$ states — the harmonic (traceless) polynomials of degree $L$ in $(z_1,z_2,z_3)$, which form the unique spin-$L$ irrep of $\mathrm{SO}(3)$. The remaining $\binom{L+3}{3}-(2L+1)$ states fall into exactly two classes:

**(i) IDWT-hidden:** $\displaystyle\frac{L(L+1)(L+2)}{6} = \binom{L+3}{3} - \binom{L+2}{2}$ states carrying at least one factor of $z_4$. These have angular momentum support in the hidden $\Xi_6$ direction and are spectroscopically dark by $\xi$-orthogonality (Lemma 2).

**(ii) Lower-$j$ 3D:** $\displaystyle\frac{L(L-1)}{2} = \binom{L+2}{2} - (2L+1)$ states that are non-harmonic degree-$L$ polynomials in $(z_1,z_2,z_3)$ only — no $z_4$ dependence. These are standard lower-angular-momentum configurations ($j < L$) already counted in orbital shells $L' < L$. They are not new or hidden states; they fail the harmonic condition, not the observability condition.

*Proof sketch.* The $z_4$-dependent states are $\mathrm{Sym}^L(\mathbb{C}^4) \setminus \mathrm{Sym}^L(\mathbb{C}^3)$, of dimension $\binom{L+3}{3}-\binom{L+2}{2} = L(L+1)(L+2)/6$. Within $\mathrm{Sym}^L(\mathbb{C}^3)$, the harmonic (traceless) degree-$L$ polynomials span the $j=L$ irrep of dimension $2L+1$; the remaining $\binom{L+2}{2}-(2L+1) = L(L-1)/2$ states are the non-harmonic content, decomposing under $\mathrm{SO}(3)$ into $j = L-2, L-4, \ldots$ The uniqueness of the $j=L$ irrep at each level follows because each $\mathrm{SU}(3)$ block contributes at most one $j=L$ state, and the full $\mathrm{SU}(4)$ decomposition contains exactly one such block. $\square$

**Corollary ⭐.** The IDWT-hidden count $L(L+1)(L+2)/6$ grows as $L^3/6$; the lower-$j$ 3D count $L(L-1)/2$ grows as $L^2/2$. For large $L$, hidden states dominate: hidden/total $\to L/(L+3) \to 1$ as $L \to \infty$.

---

## 3. A Structural Identity

### 3.1 Orbital Shell Counts are d=3 Simplex Numbers ⭐

The total number of orbital states at angular momentum level $L$ is $\dim(\mathrm{Sym}^L(\mathbb{C}^4)) = \binom{L+3}{3}$. This is algebraically identical to the IDWT simplex number $S(L+1,3)$:

$$\dim\bigl(\mathrm{Sym}^L(\mathbb{C}^4)\bigr) = \binom{L+3}{3} = S(L+1,3).$$

This is a pure combinatorial identity — $\binom{L+3}{3} = \binom{(L+1)+2}{3} = S(L+1,3)$ holds for all $L \geq 0$.

| $L$ | Shell | Total | Observable | IDWT-hidden | Lower-$j$ 3D | $S(L+1,3)$ |
|-----|-------|-------|-----------|-------------|--------------|-----------|
| 0 | $s$ | 1 | 1 | 0 | 0 | $S(1,3)=1$ |
| 1 | $p$ | 4 | 3 | 1 | 0 | $S(2,3)=4$ |
| 2 | $d$ | 10 | 5 | 4 | 1 | $S(3,3)=10$ |
| 3 | $f$ | 20 | 7 | 10 | 3 | $S(4,3)=20$ |

The total microstate count of orbital shell $L$ in the $d=6$ lepton sector equals the IDWT spectral weight of mode $n=L+1$ in the $d=3$ hadronic sector. The orbital shell structure of atomic physics and the hadronic mass spectrum of IDWT are governed by the same combinatorial sequence.

---

## 4. Explicit Bases

### 4.1 L = 1 ($p$ shell)

$\mathrm{Sym}^1(\mathbb{C}^4)$ has basis $\{z_1, z_2, z_3, z_4\}$.

**Observable p-orbitals (3):** $\{z_1, z_2, z_3\} \to (p_x, p_y, p_z)$. These are the standard $Y_1^m$ spherical harmonics.

**IDWT-hidden (1):** $\{z_4\}$ — the single fibre coordinate. Its inner product with any monomial in $(z_1,z_2,z_3)$ under the $\mathrm{SU}(4)$-invariant measure is zero. Hence $\langle z_4 | O | z_i \rangle = 0$ for every 3D operator $O$ and $i \in \{1,2,3\}$.

### 4.2 L = 2 ($d$ shell)

$\mathrm{Sym}^2(\mathbb{C}^4)$ has 10 basis monomials.

**Observable d-orbitals (5):** The traceless degree-2 polynomials in $(z_1,z_2,z_3)$ — the standard $Y_2^m$.

**IDWT-hidden (4):** $\{z_1z_4,\, z_2z_4,\, z_3z_4\}$ (forming $j=1$) and $\{z_4^2\}$ ($j=0$). All carry $z_4$-dependence and are zero-amplitude at every 3D operator vertex by Lemma 2.

**Lower-$j$ 3D (1):** $\{z_1^2+z_2^2+z_3^2\}$ — the SO(3) trace, $j=0$, no $z_4$-dependence. This is not IDWT-hidden: a 3D apparatus couples to it normally. It does not introduce a new observable — it is a higher-degree copy of the $j=0$ representation already appearing at $L=0$.

### 4.3 L = 3 ($f$ shell)

$\mathrm{Sym}^3(\mathbb{C}^4)$ has 20 basis monomials.

**Observable f-orbitals (7):** The harmonic degree-3 polynomials in $(z_1,z_2,z_3)$ — the standard $Y_3^m$, $m=-3,\ldots,+3$.

**IDWT-hidden (10):** All monomials containing at least one $z_4$ factor, in three sub-families by $z_4$ multiplicity:

- (i) $\{z_iz_jz_4 : i,j \in \{1,2,3\}\}$ — six states: the five traceless combinations ($j=2$) and the trace $z_4(z_1^2+z_2^2+z_3^2)$ ($j=0$);
- (ii) $\{z_1z_4^2,\, z_2z_4^2,\, z_3z_4^2\}$ — three states, $j=1$;
- (iii) $\{z_4^3\}$ — one state, $j=0$.

Total: $5+1+3+1 = 10$. All are zero-amplitude at every 3D operator vertex by Lemma 2.

**Lower-$j$ 3D (3):** $\{(z_1^2+z_2^2+z_3^2)z_1,\; (z_1^2+z_2^2+z_3^2)z_2,\; (z_1^2+z_2^2+z_3^2)z_3\}$ — degree-3 polynomials in $(z_1,z_2,z_3)$ only, $j=1$. Not IDWT-hidden; already counted in the $L=1$ $p$-shell.

---

## 5. Derivations

### Lemma 1 — Exact Potential Separability ✅

**Statement.** The total interaction potential on $M_\infty = \mathbf{R}^3 \times \Xi_6$ for the hydrogen system is:

$$V(\mathbf{r}, \xi) = V_\mathrm{Coulomb}(|\mathbf{r}|) + V_6(|\xi|)$$

an exact sum with no $\mathbf{r}$-$\xi$ cross terms.

**Proof.**

*$V_\mathrm{Coulomb}$ has no $\xi$-dependence.* The electromagnetic interaction is mediated by the $d=2$ photon sector. The photon's coupling to the electron is through the EM current integrated over the observable 3D slice: $J^\mu(\mathbf{r}) = e\rho_{3\mathrm{D}}(\mathbf{r})$ where $\rho_{3\mathrm{D}}(\mathbf{r}) = \int|\Psi_e(\mathbf{r},\xi)|^2\, d^6\xi$. The resulting Coulomb term $-e^2/|\mathbf{r}|$ depends only on the 3D separation. No $\xi$-dependent term enters because the $d=2$ photon sector has support only in the 3D observable directions.

*The proton creates no $\xi$-dependent potential for the electron.* The proton's quark modes ($d=3$, $d=4$) share the directions $\Xi_4 \subset \Xi_6$ with the electron. A $\xi$-dependent coupling between them would require the strong force to reach the electron across those shared directions. The $d=6$ sector has $\mathrm{SU}(4)$ geometry of $\mathrm{CP}^3$, which gives complete colour silence: $\chi(\mathrm{CP}^3) = 4 \neq 3$, so colour contributions cancel in the $\mathrm{SU}(4)$ representation and all colour-charged coupling matrix elements are geometrically zero (Part 1 §3g). The proton's quark-sector modes create no $\xi$-dependent potential for the electron.

*$V_6$ has no $\mathbf{r}$-dependence.* The sector confining potential $V_6(|\xi|) = \lambda_6|\xi|^2/(1+|\xi|^2)$ depends only on $|\xi|$ by the $\mathrm{CP}^3$ isometry. $\square$

**Consequence.** The Schrödinger equation on $M_\infty$ is exactly separable. Setting $\Psi(\mathbf{r},\xi) = \psi(\mathbf{r})\chi(\xi)$:

$$\left[-\frac{\hbar^2}{2m_e}\nabla^2_r + V_\mathrm{Coulomb}(|\mathbf{r}|)\right]\psi = E_r\,\psi, \qquad \left[-\frac{\hbar^2}{2m_e}\nabla^2_\xi + V_6(|\xi|)\right]\chi = E_\xi\,\chi.$$

The electron occupies sector mode $n=13$, so $\chi = \chi_{13}$ and $E_\xi = m_e$. The factorisation is exact.

### 5.1 Effective Hamiltonian ✅

$$H_\mathrm{eff} = -\frac{\hbar^2}{2m_e}\nabla^2_r - \frac{e^2}{|\mathbf{r}|} + m_e.$$

This is the standard 3D hydrogen Hamiltonian plus the electron rest mass. The derivation uses only: (i) the $d=2$ EM coupling structure; (ii) the colour silence of the $d=6$ sector; (iii) the $\mathrm{CP}^3$ isometry of the sector potential.

### 5.2 Energy Levels ✅

From §5.1, the hydrogen energy eigenvalues are:

$$E_{n_H} = m_e - \frac{m_e\,\alpha^2}{2n_H^2},$$

where $n_H = 1, 2, 3, \ldots$ is the hydrogenic principal quantum number (distinct from the IDWT mode index $n=13$). Full $L$-degeneracy holds for $L = 0, 1, \ldots, n_H - 1$. The Coulomb potential has no $\xi$-dependence by Lemma 1, so no correction to the 3D Hamiltonian appears.

### Lemma 2 — $\xi$-Orthogonality ✅

**Statement.** Let $O(\mathbf{r}, \nabla_r)$ be any operator that depends only on 3D position and momentum (no $\xi$-dependence). Let $|\mathrm{obs}\rangle$ be any observable orbital state whose angular part is a polynomial in $(z_1,z_2,z_3)$ only. Let $|\mathrm{hid}\rangle$ have nontrivial $z_4$-dependence. Then $\langle\mathrm{hid}|O|\mathrm{obs}\rangle = 0$.

**Proof.** Write $\Psi_\mathrm{hid}(\mathbf{r},\xi) = R(|\mathbf{r}|)\, P_\mathrm{hid}(\hat{r},\hat{\xi})\, f_{13}(|\xi|)$ where $P_\mathrm{hid}$ has nontrivial $\hat{\xi}$-dependence, and $\Psi_\mathrm{obs}(\mathbf{r},\xi) = R'(|\mathbf{r}|)\, Y_L^m(\hat{r})\, f_{13}(|\xi|)$. Since $O$ acts on $\mathbf{r}$ only:

$$\langle\Psi_\mathrm{hid}|O|\Psi_\mathrm{obs}\rangle = \underbrace{\int |f_{13}(|\xi|)|^2\, d|\xi|}_{\text{radial }\xi} \times \underbrace{\int P_\mathrm{hid}^*(\hat{r},\hat{\xi})\, d\Omega_\xi}_{=\;0} \times \int R^* O R'\, Y_L^m\, d^3r.$$

The middle factor vanishes: $P_\mathrm{hid}$ has nontrivial $\hat{\xi}$-dependence, and integration of any non-constant angular function over the full $\xi$-sphere is zero by spherical harmonic orthogonality. The matrix element is zero regardless of $O$. $\square$

### 5.3 Consequences of Lemma 2

Every standard physical interaction that describes atomic structure is a 3D operator. Lemma 2 therefore gives the following results, each with the same proof skeleton:

**Spectroscopic darkness — all multipoles ✅.** The EM current $J^\mu(\mathbf{r})$ has no $\xi$-dependence. Hidden states are zero-amplitude at every EM vertex — electric dipole E1, electric quadrupole E2, magnetic dipole M1, and all higher multipoles $\mathrm{E}k$, $\mathrm{M}k$. No radiative transition of any multipole order can connect a hidden state to an observable one. The selection rules are structural, not perturbative.

**Zeeman splitting — exactly $2L+1$ levels ✅.** The Zeeman perturbation $H_B = -(e/2m_e)\mathbf{B}\cdot\mathbf{L}_{3\mathrm{D}}$ is a 3D operator (the external field $\mathbf{B}$ lives in $\mathbf{R}^3$ and has zero $\Xi_6$ component). Lemma 2 kills all mixing with hidden states. The $m_L = -L,\ldots,+L$ substates of each shell split into exactly $2L+1$ Zeeman levels.

**Stark selection rules ✅.** The Stark operator $H_\mathrm{Stark} = e|\mathbf{E}|z_3$ depends only on the 3D coordinate $z_3$. Lemma 2 eliminates all mixing between hidden and observable states. The 2s–2p matrix element $\langle 2s|z_3|2p_z\rangle$ is the standard hydrogen value with no $\xi$-correction (the $\chi_{13}$ normalisation gives 1). The selection rules $\Delta L = \pm 1$, $\Delta m_L = 0$ follow from $\mathrm{SO}(3)$ Clebsch-Gordan on the $2L+1$ projected states.

**Dirac fine structure — unmodified ✅.** The spin-orbit coupling $H_\mathrm{SO} = (1/2m_e^2c^2)(1/r^3)\mathbf{L}\cdot\mathbf{S}$ and the Darwin term $(1/2m_e^2c^2)\nabla^2 V$ are 3D operators. Lemma 2 gives zero admixture of hidden states. The standard Dirac fine-structure corrections are exact consequences of the 3D Hamiltonian and are unmodified by the sector geometry.

**Hyperfine spectrum — unmodified ✅.** The hyperfine interaction terms $\mathbf{I}\cdot\mathbf{L}$, $\mathbf{I}\cdot\mathbf{S}$, and $\delta^3(\mathbf{r})\mathbf{I}\cdot\mathbf{S}$ are all 3D operators. Lemma 2 gives zero hyperfine admixture from hidden states. The hyperfine spectrum is exactly the standard result.

**Permanent undetectability ✅.** Every physical measurement apparatus operating in $\mathbf{R}^3$ implements a 3D operator. Lemma 2 therefore applies universally: hidden-sector orbital states are structurally inaccessible to every experiment confined to the observable three dimensions — not merely undetected but impossible to couple to at any order and by any mechanism.

---

## 6. Scope and Falsifiability

**What this paper establishes:**

| Result | Status | Mechanism |
|--------|--------|-----------|
| Orbital degeneracy $2L+1$ | ⭐ | Harmonic component of $\mathrm{Sym}^L(\mathbb{C}^4)$ |
| $H_\mathrm{eff} = H_{3\mathrm{D}} + m_e$ (exact) | ✅ | Lemma 1: $d=2$ coupling + colour silence |
| Bohr spectrum $E_{n_H} = m_e - m_e\alpha^2/2n_H^2$ | ✅ | §5.1 |
| All EM multipole selection rules | ✅ | Lemma 2 applied to $J^\mu A_\mu$ multipole expansion |
| Zeeman splitting: exactly $2L+1$ levels | ✅ | Lemma 2 applied to $\mathbf{B}\cdot\mathbf{L}_{3\mathrm{D}}$ |
| Stark selection rules $\Delta L=\pm 1$ | ✅ | Lemma 2 applied to $e\mathbf{r}\cdot\mathbf{E}$ |
| Dirac fine structure (unmodified) | ✅ | Lemma 2 applied to $H_\mathrm{SO}$ and Darwin term |
| Hyperfine spectrum (unmodified) | ✅ | Lemma 2 applied to $\mathbf{I}\cdot\mathbf{L}$, $\mathbf{I}\cdot\mathbf{S}$ |
| Hidden states permanently undetectable | ✅ | Lemma 2 applies to all 3D operators at all orders |
| Orbital count = hadronic simplex number | ⭐ | $S(L+1,3) = \binom{L+3}{3}$, pure algebra |

**What this paper does not yet establish:**

- *Orbital hybridisation (sp, sp², sp³).* These involve superpositions of projected $L=1$ and $L=2$ states. They likely follow from the same $\xi$-orthogonality structure under molecular Hamiltonian perturbations, but have not been derived explicitly here.
- *Relativistic corrections at full Dirac level.* The present treatment is non-relativistic. Lemma 2 confirms that the standard non-relativistic Hamiltonian is exact for the 3D sector; the relativistic extension requires the full Dirac structure of $H_6$.
- *Lamb shift.* This is a QED vacuum polarisation effect; its treatment in IDWT requires the kernel loop sum formalism (Part 8 §6), which is not yet complete.

**Falsification conditions.** Any spectroscopic measurement that finds:

- More than $2L+1$ levels in the Zeeman pattern for any shell $L$,
- Any EM transition (at any multipole order) that violates $\Delta L = \pm 1$ or $\Delta m_L = 0, \pm 1$,
- Any anomalous energy shift in the Bohr spectrum attributable to hidden-sector coupling,
- Any deviation from the standard Dirac fine-structure or hyperfine splitting that cannot be attributed to known QED effects,

would falsify the $\mathrm{CP}^3$ identification of the $d=6$ electron sector in IDWT.

---

## 7. Summary

The atomic orbital families $s, p, d, f$ are projections of the $\mathrm{CP}^3$ sector geometry of IDWT to the observable 3D slice. The orbital degeneracy count $2L+1$ at angular momentum $L$ is a theorem of the representation theory of $\mathrm{SU}(4)$ under the chain $\mathrm{SU}(4) \supset \mathrm{SU}(3) \supset \mathrm{SO}(3)$, with the $\mathrm{SU}(3)$ link provided by the $d=4$ quark sector colour group embedded within the $d=6$ lepton sector isometry. At each shell $L$, $\mathrm{Sym}^L(\mathbb{C}^4)$ contains three classes: the $2L+1$ observable states (harmonic polynomials in $(z_1,z_2,z_3)$), $L(L+1)(L+2)/6$ IDWT-hidden states involving the $z_4$ fibre direction, and $L(L-1)/2$ non-harmonic 3D polynomials of lower angular momentum already counted in lower shells. The IDWT-hidden states — and only those — are spectroscopically invisible via $\xi$-orthogonality (Lemma 2), which applies to every 3D operator at every order: EM transitions of all multipoles, Zeeman and Stark couplings, spin-orbit and Darwin fine-structure terms, and hyperfine nuclear couplings. The effective hydrogen Hamiltonian on the 3D slice is exactly $H_{3\mathrm{D}} + m_e$ — the Bohr spectrum follows without correction — because the electromagnetic potential separates exactly on $M_\infty = \mathbf{R}^3 \times \Xi_6$, enforced by the $d=2$ sector coupling and the colour silence of $\mathrm{CP}^3$ (Lemma 1). The total dimension of orbital shell $L$ equals the $d=3$ sector simplex number $S(L+1,3)$, an algebraic identity connecting atomic orbital structure to the IDWT hadronic mass spectrum. Chemistry is a shadow of the $d=6$ sector geometry.

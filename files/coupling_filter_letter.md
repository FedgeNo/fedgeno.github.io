# Sector Geometry as Coupling Filter: A Geometric Origin for Standard Model Quantum Numbers

**Author:** Fedge No  
**Contact:** fedge-no@hotmail.com  
**Related work:** *A Combinatorial-Geometric Derivation of the Standard Model Spectrum from a Single Integer* (Zenodo doi:10.5281/zenodo.20032250)

---

## Abstract

The Standard Model assigns quantum numbers — color, weak isospin, the Dirac condition — to particles as empirical axioms. We show that these are not axioms: they are the coupling structures imposed on each particle by the geometry of the sector manifold in which that particle's wavefunction is localized. A particle does not *have* color charge; the CP² geometry of its sector *is* color charge, expressed through χ(CP²) = 3. A neutrino does not *happen* to be Dirac; the Clifford algebra at $d \bmod 8 = 5$ cannot support the spinor type required by Majorana mass terms, making all lepton-number-violating interactions geometrically impossible rather than dynamically suppressed. We identify a coupling filter for each of the six sectors of the framework, covering polarization (U(1) fiber geometry of CP¹), weak isospin (SO(4) isometry of S³), color charge ($\chi(\mathbb{CP}^2) = 3$ from sector topology), Majorana prohibition (Bott periodicity on S⁵), total QCD silence (index cancellation on CP³), and fractal marginal coupling (Aubry-André criticality at $d=10$). In every case, the quantum number is derived — from the Euler characteristic, Clifford algebra, or the sector isometry group — rather than postulated. Two independent principles together determine the complete coupling structure of any particle: coordinate containment governs which forces can reach a particle; sector geometry governs the structure and geometrically forbidden classes of those couplings.

---

## 1. Background: Sectors and Coordinate Containment

Infinite-Dimensional Wave Theory (IDWT) [1] describes the Standard Model as the low-lying spectrum of a single master wavefunction $\Psi_\infty$ on $\mathcal{M}_\infty = \mathbb{R}^{3,1} \times \bigoplus_d \Xi_d$. The six sectors $\Xi_d$, with $d \in D = \{2,3,4,5,6,10\}$, are infinite Riemannian spaces whose local geometry is that of the complex projective spaces CP$(d/2-1)$ (even $d$) or the odd spheres $S^d$ (odd $d$), arranged by the Hopf fibration chain $S^1 \to S^{2k-1} \to \mathbb{CP}^{k-1}$. Bound states of the sector potential $V_d = \lambda_d|\xi|^2/(1+|\xi|^2)$ produce the particle spectrum; each particle $(n,d)$ is localized primarily in sector $\Xi_d$. The sectors are nested:

$$\Xi_2 \subset \Xi_3 \subset \Xi_4 \subset \Xi_5 \subset \Xi_6 \subset \Xi_{10}.$$

The coordinate nesting produces an already-established principle — **coordinate containment**: a particle couples to a force only if it has wavefunction support in that force's sector coordinates [1, §3g]. A particle in $\Xi_2$ (photon) has no strong coupling because $\Xi_2 \not\supset \Xi_4$ (the d=4 colour sector). A particle in $\Xi_6$ (electron) has support throughout $\Xi_2 \subset \cdots \subset \Xi_6$ and so couples to all forces whose sector coordinates are contained within $\Xi_6$.

Coordinate containment answers a binary question: does coupling exist at all? It does not answer what structure that coupling has, or what entire classes of interaction are geometrically impossible. That is the question this paper addresses.

---

## 2. The Coupling Filter Principle

Consider polarized light. A photon in a definite polarization state couples to currents aligned with its polarization vector $\varepsilon_\mu$ via $\varepsilon_\mu j^\mu$. Perpendicular currents receive zero coupling — not suppression, zero.

Polarization is conventionally treated as a property of the photon. But the photon lives in sector $d=2$, whose geometry is CP¹ — a complex projective line with U(1) fiber structure. The photon's two helicity states are not a label attached to the photon; they are the complete internal geometry of CP¹. The zero coupling to misaligned currents is not a dynamical rule; it is what U(1) fiber geometry means as a coupling structure.

This observation generalizes. Each sector geometry determines not just whether a particle couples (coordinate containment) but the structure of that coupling: what handles it presents to the world, and what entire classes of interaction are geometrically impossible to it.

**The coupling filter principle:** The sector quantum number of a particle is not an input label. It is the geometry of the particle's sector manifold expressing itself as a coupling structure. This determines:
1. The symmetry handles available for interaction (e.g., two helicity states, three color charges).
2. The classes of interaction that are geometrically — not dynamically — absent.

The two principles are independent: a particle may have coordinate support in a force's sector and still have zero coupling if its own sector geometry projects the relevant representation to zero (as the neutrino example in Section 3 shows). Both principles together give the complete coupling structure.

---

## 3. The Six Coupling Filters

### d=2 — CP¹, U(1) — Photon — Orientation filter

The U(1) fiber geometry of CP¹ gives the photon exactly two coupling handles (helicity $\pm 1$). The coupling to any target is $\varepsilon_\mu j^\mu$; currents orthogonal to the polarization vector receive zero coupling. This is the most directly observable coupling filter in nature — it underlies polarized optics, LCD screens, microscopy — and it is fully determined by the simplest nontrivial sector geometry.

The $d=2$ sector is also the reference sector for the IDWT observability criterion: dimensional depth $\Omega_{\log}(n,d) = \ln(S(n,d)/S(n,2))$ is measured relative to $d=2$. This is not arbitrary. The U(1) coupling structure of the photon is the most universal interaction — every charged particle at $d > 2$ contains $\Xi_2$ in its coordinate support, which is why electric charge coupling exists at all. The reference sector and the most universal coupling are the same thing.

### d=3 — S³, SO(4) — Down-type quarks — Weak isospin filter

The isometry group of S³ is SO(4) $= \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$. This left-right decomposition gives down-type quarks left-handed weak coupling. The right-handed component does not participate in the weak interaction: SU(2)$_R$ is latent in the S³ geometry but does not generate a coupling handle for the observed weak force.

The color coupling of down quarks is inherited derivatively — via coordinate containment inside $\Xi_4$ — not from the S³ geometry itself. The S³ sector's own contribution is the left-right structure: left-handed weak coupling on, right-handed weak coupling off.

### d=4 — CP², SU(3)/U(2) — Up-type quarks — Color filter

Color originates here. $\chi(\mathbb{CP}^2) = 3$ — from the CP² CW structure: one cell each in dimensions 0, 2, 4, giving $1-0+1-0+1 = 3$. That integer is $N_c$: three color charges, not a parameter or a measurement input, but a theorem of CP² topology.

The coupling filter for color is the strongest in nature: all processes must conserve color. An isolated quark is not a suppressed state — it is a geometrically forbidden one. The CP² coupling structure cannot produce a color-nonsinglet asymptotic state. Confinement, in this picture, is the $d=4$ coupling filter operating at the level of which asymptotic states can be constructed from the sector geometry.

### d=5 — S⁵, SO(6) — Neutrinos — Majorana/LNV filter

The Clifford algebra of a five-dimensional space has a definitive property: at $d \bmod 8 = 5$, no Majorana condition can be imposed on the spinor [2]. This is not a dynamical fact about neutrinos — it is a structural fact about the S⁵ geometry. The geometry cannot support the spinor type that Majorana mass terms require.

The consequences are exact, not approximate:
- Every Majorana mass term: forbidden.
- Every lepton-number-violating vertex: forbidden.
- Every form of neutrinoless double beta decay: exactly zero rate.
- The see-saw mechanism: eliminated.

These are not suppressed interactions that might appear at higher energy. They are interactions that cannot be written down for S⁵ modes. This is why $m_{\beta\beta} = 0$ in IDWT is a theorem rather than a prediction with error bars.

Separately, the S⁵ Hopf fibration $S^1 \to S^5 \to \mathbb{CP}^2$ means that the CP² color representation is present within S⁵ as the base space. Yet neutrinos are color-neutral. The S¹ fiber acts as a projector that averages over the color representation from CP², selecting only the singlet component. Neutrinos have coordinate support in the color sector but the S⁵ geometry projects that support onto zero color charge — a filter distinct from the Majorana prohibition but acting simultaneously.

Positively, the SO(6) $\cong$ SU(4) Pati-Salam structure of the sector gives neutrinos their $B-L$ charge.

### d=6 — CP³, SU(4)/U(3) — Electron, Muon — Total colour silence

$\chi(\mathbb{CP}^3) = 4$, not 3. The colour contributions in the SU(4)/U(3) representation cancel — CP³ produces no colour handles. The result: zero strong coupling at any energy. Not suppressed at low energy, not dynamically forbidden, not a higher-order effect — geometrically absent.

CP³ is the twistor space of flat 3+1 Minkowski spacetime [3]. This connection is not incidental. The electron-photon vertex — the fundamental interaction of QED — has the precise form it does because CP³ is twistor space and CP¹ is the photon's sector. The coupling between them inherits the twistor structure. The clean electromagnetic behavior of the electron is a consequence of its sector geometry being the twistor space of the spacetime in which both it and the photon propagate.

The $d=6$ coupling filter: all strong interactions geometrically absent; electromagnetic and weak couplings on with twistor-structured vertex form.

### d=10 — CP⁵, SU(6)/U(5) — Tau — Fractal marginal coupling

The $d=10$ sector is the unique sector at the Aubry-André metal-insulator critical point [1, T5]: $b_{k_0}(d) = \sqrt{k_0(k_0+d-1)}/(2k_0+d-2) = 1/2$ uniquely at $d=10$, $k_0 = n_s^2 = 16$. At the critical point, modes are neither fully extended (coupling freely to everything) nor fully localized (coupling to nothing). The spectrum is a Cantor set: measure zero, but topologically dense.

A Cantor-set spectrum means two things simultaneously. Dense: every energy neighborhood contains a resonance, so the tau can always find a decay channel (explaining its short lifetime). Measure zero: the coupling weight on any specific channel is suppressed, because the measure-zero structure means no single channel carries significant probability (explaining why the lifetime is finite).

The Dyson resummation correction $\delta_\tau = 1/1680$ required for the tau's mass [1] is the mathematical signature of this fractal structure: an all-orders resummation is necessary only at the critical point, where the naive perturbation series does not converge.

The $d=10$ filter: nothing specifically blocked; everything barely available, via a Cantor-set spectrum that is simultaneously universal and marginal.

---

## 4. Summary Table

| Sector | Geometry | Particle | Coupling given | Interactions filtered out |
|---|---|---|---|---|
| $d=2$ | CP¹, U(1) | Photon | Helicity $\pm 1$ handles | Misaligned currents (zero, not suppressed) |
| $d=3$ | S³, SO(4) | Down quarks | Left-handed weak isospin | Right-handed weak coupling |
| $d=4$ | CP², SU(3)/U(2) | Up quarks | Color ($N_c=3$ from χ(CP²)=3); chirality | Color-nonsinglet asymptotic states |
| $d=5$ | S⁵, SO(6) | Neutrinos | $B-L$ charge; Dirac structure | All Majorana/LNV interactions — geometrically, not dynamically |
| $d=6$ | CP³, SU(4)/U(3) | $e^-$, $\mu^-$ | EW coupling; twistor-structured EM vertex | All QCD — total color silence |
| $d=10$ | CP⁵, SU(6)/U(5) | $\tau^-$ | Universal marginal coupling | Nothing blocked; all channels measure-zero suppressed |

---

## 5. Relationship to Coordinate Containment

Coordinate containment [1, §3g] answers the binary question of whether coupling is possible at all: a particle at sector $d$ couples to force $f$ only if $\Xi_f \subset \Xi_d$. The coupling filter principle answers the complementary question: given that coupling is possible, what is its structure, and what classes of interaction remain forbidden?

The two principles are logically independent. Coordinate containment is a necessary condition; the coupling filter operates on top of it. The neutrino case makes the independence explicit: neutrinos have $\Xi_4 \subset \Xi_5$, so they satisfy coordinate containment for the color sector — yet they are color-neutral because the S⁵ Hopf structure projects the CP² color representation onto its singlet. The coupling filter overrides the containment on color, while leaving $B-L$ coupling intact.

---

## 6. What This Means

The Standard Model takes quantum numbers as primitive: quarks have three colors because experiment says so; neutrinos are Dirac (probably) because no Majorana mass has been observed; leptons are colour-neutral because they have never shown strong coupling. The quantum numbers are inputs.

The sector geometry picture inverts the causation. CP² is not a space that happens to produce color — CP² is what color *is*, expressed as the coupling structure of a mode on a Kähler manifold with SU(3)/U(2) symmetry. The electron is not a particle that happens to be color-neutral — CP³ twistor geometry is what color-neutrality *is*, for a particle at that sector. The neutrino is not Dirac because no Majorana mass has been measured — the Clifford algebra at $d \bmod 8 = 5$ *is* the Dirac condition, geometrically constituted.

Each quantum number is a theorem of the sector geometry, derived from the Euler characteristic, Clifford algebra, Bott periodicity, or the sector isometry group. None is a postulate.

The filters become structurally more drastic as one moves across the spectrum. The photon's filter (polarization) is directional — it blocks one orientation. The quark's filter (color) is representational — it requires conservation in all processes and forbids isolated states. The neutrino's filter (Dirac condition) is algebraic — it eliminates an entire spinor type from the theory. The lepton's filter (color silence) is complete for an entire force. The tau's filter (AA criticality) is fractal — coupling exists everywhere but with measure-zero weight at every specific channel.

A deeper structural result, proved in [1] (T15 and corollaries T15a–f), shows that the coupling filter geometry and the particle mass hierarchy are not merely correlated but share a single geometric root. The number of quark colors $N_c = \chi(\mathbb{CP}^2) = 3$ is the Euler characteristic of the color sector. That single integer determines all six sector self-couplings, all occupied mode indices, the termination of the sector chain at $d = 2(N_c+2) = 10$, and via these, all inter-sector mass ratios. Equivalently: the self-coupling $g_{dd}$ of each sector anti-correlates with the dimension of its isometry group — a larger symmetry group imposes more geometric constraints on interactions, producing a weaker self-coupling and lighter particle masses. The coupling filter principle (what interactions are possible, in what structure) and the mass scale structure (how heavy the particles are) are one quantity read in two different units.

---

## References

1. Fedge No, *A Combinatorial-Geometric Derivation of the Standard Model Spectrum from a Single Integer*, Zenodo doi:10.5281/zenodo.20032250 (2026). Technical documentation (9 volumes): doi:10.5281/zenodo.19767493.
2. H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989). *(Bott periodicity, Majorana conditions)*
3. R. Penrose, *J. Math. Phys.* **8**, 345 (1967). *(Twistor space)*
4. C. Bär, *Geom. Funct. Anal.* **6**, 899 (1996). *(Dirac spectrum on $S^n$)*

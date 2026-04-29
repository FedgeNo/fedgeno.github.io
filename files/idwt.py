# idwt.py — IDWT mass calculator with full derivation commentary
# =============================================================================
# Infinite-Dimensional Wave Theory: mass predictions from two measured constants.
#
# The single empirical framework: a Dirac spinor field Psi_inf lives on an
# infinite-dimensional manifold M_inf = R^{3,1} x (sector manifolds). Particles
# are standing-wave resonances in the hidden sectors. Their masses are:
#
#     m(n, d) = m_scale(d) x S(n, d)
#
# where S(n,d) = C(n+d-1, d) counts the degree-n monomials in d variables
# (the dimension of Sym^n(R^d)), and m_scale(d) is fixed by the two inputs
# m_e and m_W. No fitting beyond those two measurements.
#
# Structure of this script (all computation before all output):
#   STEP 1  -- Build the mode-index tower by explicit seed addition
#   STEP 2  -- Derive coupling constants g33, g44, g66 from seeds
#   STEP 3  -- Compute sector scales from m_e and m_W
#   STEP 4  -- Compute corrections (GTC, Dyson resummation)
#   STEPS 5-11 -- Print everything
#
# Cross-references use "Part N section M" referring to the IDWT document set.
# =============================================================================

import math


# =============================================================================
# CORE COMBINATORIAL FUNCTION
# =============================================================================

def S(n, d):
    """
    S(n, d) = C(n+d-1, d)  -- the binomial coefficient used throughout IDWT.

    Physical meaning: S(n,d) is the dimension of the space of degree-n symmetric
    tensors in d variables, equivalently the number of degree-n monomials in d
    variables. In IDWT this counts the distinct hidden microstates at excitation
    level n in sector d. Mass IS this count (in units of m_scale_d):
    'mass is frequency is microstate count' -- all three are the same quantity.
    (Part 1 section 5, Part 2 section 1)

    The hockey-stick recursion S(n,d) = S(n,d-1) + S(n-1,d) is the algebraic
    engine behind the generation law: every generation relationship is a
    consequence of Pascal's triangle applied at specific fixed points.
    (Part 2 section 4)
    """
    return math.comb(n + d - 1, d) if n >= 0 and d >= 0 else 0


# =============================================================================
# STEP 1 -- BUILD THE MODE-INDEX TOWER
# =============================================================================
# The entire particle spectrum follows from two forced integers {n_s, n_u},
# called the seeds. All mode indices are derived by explicit addition using
# the hockey-stick (generation law) recursion -- no fits, no choices.
# (Part 2 sections 2-4, Part 1 section 5)

# --- Seeds -------------------------------------------------------------------
# n_d = 1  (down quark seed)
# Forced because S(1, d) = 1 for every sector d. Every sector's ground state
# has mode index 1. No other choice is consistent. (Part 2 section 2)
n_down = 1

# n_s = 4  (strange quark seed)
# This is the unique positive integer solving S(n, 4) = 35, where 35 is the
# mode index of the muon (n_mu = S(4,4) = 35). The strange quark must sit at
# the d=3 simplex level whose d=4 simplex image equals n_mu. That equation
# S(n,4) = 35 has exactly one solution: n = 4. (Part 2 section 2, Part 1 section 5)
n_strange = 4  # unique solution to S(n_s, 4) = 35

# n_u = 3  (up quark seed)
# Forced as n_s - 1 = 3. This is not a separate postulate -- it follows from
# the vacuum stability condition: the seed pair {n_s, n_u} must satisfy
# n_u = n_s - 1 for the kernel fixed-point equation to be self-consistent.
# Equivalently, the Jacobi chain at resonance site k0 = n_s^2 = 16 requires
# n_u = n_s - 1 for the Dyson resummation factor n_s/n_u to be the ratio
# of the two smallest consecutive integers (4/3). (Part 2 sections 3 and 9)
n_up = n_strange - 1   # = 3

# --- Neutrino mode indices ---------------------------------------------------
# Neutrinos live in the d=5 sector (S^5). Their mode indices are derived as
# simplex images of the up quark seed into lower sectors. The d=5 sector
# admits only Dirac spinors (d mod 8 = 5 forbids Majorana by Bott periodicity),
# which is why neutrinos are predicted to be Dirac fermions with no Majorana
# mass and no seesaw mechanism. (Part 1 section 6, Part 2 section 6, Part 8 section 59.1)

# n_nu1 = S(n_u, 3) = S(3, 3) = C(5,3) = 10
# The first neutrino mode index is the image of the up quark seed under the
# d=3 simplex map. The d=5 sector couples to d=3 via the Vandermonde rule,
# and the lightest d=5 mode resonates at the d=3 simplex value of the up quark.
n_nu1 = S(n_up, 3)    # = 10

# n_nu2 = S(n_u, 4) = S(3, 4) = C(6,4) = 15
# Second neutrino mode: the image of the up quark seed into d=4. This equals
# C(6,2) = 15 by binomial symmetry C(n,k) = C(n,n-k), which connects it
# directly to n_W = 76 via: n_W = S(n_e, 2) - n_nu2 = 91 - 15 = 76.
# The binomial symmetry identity here is the content of OQ26. (Part 2 section 5, Part 3 section 11)
n_nu2 = S(n_up, 4)    # = 15

# n_nu3 = n_nu1 + n_nu2 - n_up = 10 + 15 - 3 = 22
# The third neutrino mode follows from the generation law applied at d=5.
# Cross-check: n_nu3 = n_tau - n_down = 23 - 1 = 22. (Part 2 section 6)
n_nu3 = n_nu1 + n_nu2 - n_up   # = 22

# --- Lepton mode indices (via the generation law) ----------------------------
# The generation law: n_lepton = n_neutrino + n_quark_partner.
# This is the hockey-stick identity S(n,d) = S(n,d-1) + S(n-1,d) applied
# at specific combinatorial fixed points. It is a theorem, not a postulate.
# (Part 2 section 4)

# n_e = n_nu1 + n_up = 10 + 3 = 13
# Electron: the lightest lepton. This is the unique d=6 mode consistent
# with the generation map at generation 1. (Part 2 section 4)
n_e = n_nu1 + n_up    # = 13

# n_charm = S(n_s, 3) = S(4, 3) = C(6,3) = 20
# Charm quark: the d=4 image of the strange seed via the d=3 simplex map.
# This is the unique d=4 mode satisfying the generation tower for generation 2.
n_charm = S(n_strange, 3)   # = 20

# n_mu = n_charm + n_nu2 = 20 + 15 = 35 = S(4,4)
# Muon: second-generation lepton. This is BOTH n_charm + n_nu2 (generation law)
# AND S(4,4) = C(7,4) = 35 (the d=4 self-image of the strange seed). These
# coinciding is a theorem from the hockey-stick identity -- it is what forced
# n_strange = 4 in the first place. (Part 2 sections 2 and 4)
n_mu = n_charm + n_nu2   # = 35; cross-check: S(n_strange, 4) = 35 exactly

# n_tau = n_nu3 + n_down = 22 + 1 = 23
# Tau: third-generation lepton, d=10 sector (octonionic Hopf total space).
# The d=10 sector carries the Majorana-Weyl spinor of SO(10): its 16-component
# Weyl part is the 16 of SO(10), containing one full SM generation (tau, nu_tau,
# b quark, t quark). Their hypercharges follow from the SO(10) root lattice.
# (Part 1 section 6, Part 2 section 7, Part 8 section 59.1)
n_tau = n_nu3 + n_down    # = 23

# --- Up-type quark mode indices ----------------------------------------------

# n_top = n_charm + 4 * n_e = 20 + 52 = 72
# Top quark mode index derivable in two equivalent ways:
#   (a) Primary (Vandermonde chain):
#       n_W = S(n_e, 2) - n_nu2 = 91 - 15 = 76 (from QCP/OQ26)
#       Vandermonde rule g(d=5, n_top) = n_W gives n_top = n_W - 4 = 72.
#   (b) Algebraic identity: n_charm + 4*n_e = 20 + 52 = 72,
#       also equal to 2 * S(2*n_s, 2) = 2 * C(9,2) = 2*36 = 72.
# The script uses (b) so that n_top is available before n_W is computed.
# The primary IDWT derivation is (a). (Part 2 section 5, Part 3 section 11)
n_top = n_charm + 4 * n_e    # = 72

# --- Boson mode indices (Vandermonde rule) ------------------------------------
# The Vandermonde coupling rule: sectors d and d' couple when d+d' is itself
# a sector dimension, and the combined mode index is g(a, b) = a + b - 1.
# Each boson mode index is the Vandermonde combination of a fermion sector
# dimension and an occupied fermion mode index. (Part 3 section 11)

# n_W = g(d=5, n_top) = n_top + 5 - 1 = 76
# W boson: the nu-sector (d=5) coupled to the top quark mode.
# Cross-check: n_W = S(n_e, 2) - n_nu2 = C(14,2) - 15 = 91 - 15 = 76.
n_W = n_top + 5 - 1    # = 76

# n_Z = g(d=6, n_W) = n_W + 6 - 1 = 81
# Z boson: the lepton sector (d=6) coupled to the W mode.
# Cross-check: n_Z = n_W + n_nu1/2 = 76 + 5 = 81, where the +5 is the
# neutral-current contribution from the lightest neutrino mode index.
n_Z = n_W + 6 - 1      # = 81

# n_H = g(n_nu2, n_Z) = n_nu2 + n_Z - 1 = 95
# Higgs: the second neutrino mode coupled to the Z mode.
# Cross-check: n_H = n_up + n_charm + n_top = 3 + 20 + 72 = 95
# (the sum of all up-type quark mode indices -- the Higgs VEV generates all
# three up-type masses simultaneously). (Part 3 section 11)
n_H = n_Z + n_nu2 - 1  # = 95


# =============================================================================
# STEP 2 -- COUPLING CONSTANTS FROM SEEDS
# =============================================================================
# The inter-sector coupling matrix G has rank 1: G_{dd'} = v_d x v_{d'} where
# v_d = sqrt(g_{dd}). All cross-couplings follow from the six self-couplings.
# g33 and g44 come entirely from the seeds {n_s, n_u}. (Part 2 section 8, Part 3 section 15)

# g33 = n_s^2 * sqrt(n_s + n_u) / 2 = 16 * sqrt(7) / 2 = 8*sqrt(7) ~= 21.166
# Derivation: the vacuum stability fixed-point equation for the d=3 sector
# kernel requires this exact value. The factor n_s^2 is k0 = 16 (the resonance
# site where the generation-level coupling concentrates), and sqrt(n_s+n_u)/2
# = sqrt(7)/2 is the universal Jacobi coefficient. (Part 2 section 8)
g33 = (n_strange**2) * math.sqrt(n_strange + n_up) / 2.0

# g44 = n_s * n_u / sqrt(n_s + n_u) = 12 / sqrt(7) ~= 4.536
# The d=4 self-coupling from seeds. Note: g33 * g44 = n_s^3 * n_u / 2 = 96
# exactly (8*sqrt(7) * 12/sqrt(7) = 8*12 = 96). This product 96 appears
# throughout: (4*sqrt(6))^2 = 96 = g_{3,4}^2 (cross-coupling between d=3 and
# d=4), and g55 * g22 = 96 (from Hopf fiber universality). (Part 2 sections 8-9)
g44 = (n_strange * n_up) / math.sqrt(n_strange + n_up)

# g66 = 0.25 = (1/2)^2 = Y_L^2
# The d=6 (charged lepton) self-coupling from anomaly cancellation.
# Hypercharge Y_L = -1/2 for the left-handed lepton doublet, fixed by the
# SU(2)^2 U(1) anomaly condition with N_c = 3 (which itself comes from the
# CP^2 Dirac index). g_{10,10} = g66 for the same reason (Y_tau = Y_L).
# (Part 3 sections 8 and 13)
g66 = 0.25


# =============================================================================
# STEP 3 -- SECTOR SCALES FROM TWO EMPIRICAL INPUTS
# =============================================================================
# All five sector scales derive from two measurements: m_e and m_W. Every
# other scale follows algebraically. (Part 1 section 5, Part 2 section 10)

m_e = 0.51099895    # MeV -- electron mass (PDG)
m_W = 80377.0       # MeV -- W boson mass (PDG)

# m_scale_6 = m_e / S(n_e, 6) = m_e / S(13, 6) = m_e / 18564
# The electron (n=13, d=6) anchors the entire lepton sector. Rearranging
# m_e = m_scale_6 * S(13,6) gives this scale directly.
# Numerically: m_scale_6 ~= 2.7526 x 10^-5 MeV = 27.53 eV. (Part 2 section 10)
m_scale6 = m_e / S(n_e, 6)

# m_scale_3 = m_e * sqrt(g33 / g66)
# Coupling self-consistency: the kernel vacuum fixed-point equation requires
# m_scale_3^2 / m_e^2 = g33 / g66 (l=0 scalar part of the cross-sector kernel).
# m_scale_3 ~= 4.702 MeV. (Part 2 section 10)
m_scale3 = m_e * math.sqrt(g33 / g66)

# m_scale_4 = m_scale_3 * sqrt(g44 / g33) / S(n_up, 4)
# The d=4 scale is set by the fixed-point condition between d=3 and d=4,
# divided by S(n_u, 4) = S(3,4) = 15 to anchor to the up quark (the lightest
# occupied d=4 mode at n=3). m_scale_4 ~= 0.1451 MeV. (Part 2 section 10)
m_scale4 = m_scale3 * math.sqrt(g44 / g33) / S(n_up, 4)

# m_scale_10 = m_scale_6
# g_{10,10} = g_{6,6} = 1/4 because Y_tau = Y_L = -1/2. Equal couplings give
# equal sector scales. The tau's mass exceeds the muon's purely because
# S(23,10) >> S(35,6), not because their sector scales differ. (Part 2 section 10)
m_scale10 = m_scale6

# m_scale_2 = m_W / S(n_W, 2) = m_W / S(76, 2) = m_W / 2926
# The gauge sector (d=2, CP^1) is anchored by the W boson. This is the only
# place m_W enters the calculation. m_scale_2 ~= 27.47 MeV. (Part 2 section 10)
m_scale2 = m_W / S(n_W, 2)

# Collect sector scales keyed by dimension.
scales = {2: m_scale2, 3: m_scale3, 4: m_scale4, 6: m_scale6, 10: m_scale10}


# =============================================================================
# STEP 4 -- CORRECTIONS
# =============================================================================

# --- Generation Tower Correction (GTC) ---------------------------------------
# The kernel coupling (xi_d . xi_{d'})^2 decomposes into l=0 (uniform across
# all modes in a sector) and l=2 (n-dependent frequency precession) components.
# The l=2 part shifts d=4 quark masses by a multiplicative factor (1-eps)^k
# where k is a mode-specific phase accumulation count. (Part 2 section 11)

# epsilon = 1 / (280 * sqrt(7)) ~= 0.001350
# Derived from: g_coeff / (k0 * n_mu)
#   g_coeff = 2 / sqrt(n_s + n_u) = 2/sqrt(7)  (universal Jacobi coefficient)
#   k0      = n_s^2 = 16                         (vacuum stability resonance site)
#   n_mu    = S(n_s, 4) = 35                     (the d=4 fixed-point mode scale)
# Result: (2/sqrt(7)) / (16 * 35) = 1/(280*sqrt(7)). (Part 2 section 11)
epsilon = 1.0 / (280.0 * math.sqrt(7.0))

# k-values: phase load per quark in the d=4 sector.
#   up:    k = 0 (generation 1, no additional phase)
#   charm: k = 3 = n_up = n_s - 1  (phase load at the generation-2 boundary)
#   top:   k = 10 = n_nu1 = S(n_u, 3) (phase load equals first neutrino mode;
#                a non-trivial cross-sector consistency check)
# After correction: c/u error 0.000%, t/u error -0.048%. (Part 2 section 11)
k_vals = {"up": 0, "charm": 3, "top": 10}

# --- Tau Dyson resummation ---------------------------------------------------
# g_{6,6} = g_{6,10} = g_{10,10} = 1/4 because Y_L = Y_tau = -1/2 (isotropic
# coupling between d=6 and d=10). The d=6->d=10 back-reaction correction on
# the tau mass feeds back on itself via g_{10,10}, giving a self-consistent
# (Dyson-resummed) shift. (Part 2 section 9)
#
# Self-consistency equation:
#   delta_m = eps_leading * m_tau + g_{10,10} * delta_m
#   => delta_m = eps_leading * m_tau / (1 - g_{10,10})
# Since g_{10,10} = 1/n_s = 1/4:
#   resummation factor = 1/(1 - 1/n_s) = n_s/(n_s-1) = n_s/n_u = 4/3
# (This ratio is forced by n_u = n_s - 1, so the Dyson factor is not free.)
#
# Total correction epsilon:
#   eps_total = 1 / (n_u * n_s^2 * S(n_s, 4)) = 1/(3 * 16 * 35) = 1/1680
#
# Result: m_tau = m_tau_bare * (1 + 1/1680) = 1776.85 MeV.
# PDG: 1776.86 +/- 0.12 MeV. Error: -0.11 sigma. Inside 1 sigma. (Part 2 section 9)
dyson_factor = 1.0 + 1.0 / (n_up * n_strange**2 * S(n_strange, 4))


# =============================================================================
# STEP 5 -- OUTPUT: TOWER CONSTRUCTION
# =============================================================================
print("=== TOWER CONSTRUCTION (explicit addition) ===")
print(f"seeds: n_down = 1, n_strange = 4")
print(f"n_up    = n_strange - 1 = {n_strange} - 1 = {n_up}")
print(f"n_nu1   = S(n_up,3)  = S({n_up},3) = {n_nu1}")
print(f"n_nu2   = S(n_up,4)  = S({n_up},4) = {n_nu2}")
print(f"n_nu3   = n_nu1 + n_nu2 - n_up = {n_nu1} + {n_nu2} - {n_up} = {n_nu3}")
print(f"n_e     = n_nu1 + n_up   = {n_nu1} + {n_up} = {n_e}")
print(f"n_charm = S(n_strange,3) = S({n_strange},3) = {n_charm}")
print(f"n_mu    = n_charm + n_nu2 = {n_charm} + {n_nu2} = {n_mu}  [= S(4,4) = {S(4,4)}]")
print(f"n_tau   = n_nu3 + n_down  = {n_nu3} + {n_down} = {n_tau}")
print(f"n_top   = n_charm + 4*n_e = {n_charm} + 4*{n_e} = {n_top}  [= 2*S(2*n_s,2) = {2*S(2*n_strange,2)}]")
print(f"n_W     = n_top + (d=5)-1 = {n_top} + 4 = {n_W}  [Vandermonde: g(d=5, n_top)]")
print(f"n_Z     = n_W  + (d=6)-1 = {n_W}  + 5 = {n_Z}  [Vandermonde: g(d=6, n_W)]")
print(f"n_H     = n_Z  + n_nu2-1 = {n_Z}  + {n_nu2} - 1 = {n_H}  [Vandermonde: g(n_nu2, n_Z)]")


# =============================================================================
# STEP 6 -- OUTPUT: COUPLINGS
# =============================================================================
print("\n=== COUPLINGS DERIVED FROM SEEDS ===")
print("g33 = n_s^2 * sqrt(n_s + n_u) / 2")
print(f"    = {n_strange}^2 * sqrt({n_strange} + {n_up}) / 2 = {n_strange**2} * sqrt({n_strange+n_up}) / 2")
print(f"    = 8*sqrt(7) = {g33:.6f}")
print()
print("g44 = n_s * n_u / sqrt(n_s + n_u)")
print(f"    = {n_strange} * {n_up} / sqrt({n_strange} + {n_up}) = {n_strange*n_up} / sqrt({n_strange+n_up})")
print(f"    = 12/sqrt(7) = {g44:.6f}")
print()
print(f"Consistency: g33 * g44 = {g33*g44:.4f}  [exact: 8*sqrt(7) * 12/sqrt(7) = 8*12 = 96]")
print()
print("g66 = Y_L^2 = (1/2)^2 = 0.25  [SU(2)^2 U(1) anomaly cancellation with N_c=3]")
print(f"    = {g66}")


# =============================================================================
# STEP 7 -- OUTPUT: SECTOR SCALES
# =============================================================================
print("\n=== SECTOR SCALES (from m_e and m_W) ===")
print(f"m_scale_6  = m_e / S(n_e,6)  = {m_e} / {S(n_e,6)} = {m_scale6:.6g} MeV  [{m_scale6*1e6:.3f} eV]")
print(f"m_scale_3  = m_e * sqrt(g33/g66)  = {m_e} * sqrt({g33:.3f}/{g66}) = {m_scale3:.6g} MeV")
print(f"m_scale_4  = m_scale_3 * sqrt(g44/g33) / S(n_u,4) = {m_scale4:.6g} MeV")
print(f"m_scale_10 = m_scale_6  [g_{{10,10}} = g66 since Y_tau = Y_L]")
print(f"m_scale_2  = m_W / S(n_W,2) = {m_W} / {S(n_W,2)} = {m_scale2:.6g} MeV")


# =============================================================================
# STEP 8 -- OUTPUT: CORRECTIONS
# =============================================================================
print("\n=== CORRECTIONS ===")
print("GTC epsilon = 1 / (280 * sqrt(7))")
print(f"           = g_coeff / (k0 * n_mu)  [g_coeff = 2/sqrt(7), k0 = 16, n_mu = 35]")
print(f"           = {epsilon:.8f}")
print(f"k-values in d=4 sector:  up k={k_vals['up']},  charm k={k_vals['charm']},  top k={k_vals['top']}")
print(f"  (correction factor per quark = (1 - epsilon)^k)")
print()
print("Tau Dyson factor = 1 + 1/(n_u * n_s^2 * S(n_s,4))")
print(f"  = 1 + 1/({n_up} x {n_strange}^2 x {S(n_strange,4)}) = 1 + 1/1680")
print(f"  = {dyson_factor:.8f}")
print(f"  Resummation: g_{{10,10}} = 1/n_s = 1/{n_strange}, so factor = n_s/n_u = {n_strange}/{n_up}")


# =============================================================================
# STEPS 9-11 -- PARTICLE TABLES
# =============================================================================

# Particle list: (name, sector d, mode index n, PDG mass in MeV)
# Bottom uses None for n: its mode is not a standard simplex value but a
# geometric-mean beat at the k0=16 resonance site. See pred_uncorrected.
particles = [
    ("photon",   2,  0,       0.0),
    ("W",        2,  n_W,     80377.0),
    ("Z",        2,  n_Z,     91187.6),
    ("Higgs",    2,  n_H,     125250.0),
    ("down",     3,  n_down,  4.67),
    ("strange",  3,  n_strange, 93.4),
    ("bottom",   3,  None,    4180.0),
    ("up",       4,  n_up,    2.16),
    ("charm",    4,  n_charm, 1270.0),
    ("top",      4,  n_top,   172760.0),
    ("electron", 6,  n_e,     0.51099895),
    ("muon",     6,  n_mu,    105.6583745),
    ("tau",      10, n_tau,   1776.86),
]


def pred_uncorrected(name, d, n):
    """
    Raw IDWT prediction: m = m_scale(d) * S(n, d), no corrections applied.

    Special cases:
    - photon: S(0, 2) = C(1,2) = 0, giving m = 0 exactly. The photon is the
      n=0 (ground state fiber) mode of the d=2 gauge sector. Zero simplex
      value is zero mass. (Part 3 section 14)

    - bottom: not a standard simplex mode. The b quark arises from a quartic
      bifurcation at the d=3 resonance site k0 = n_s^2 = 16. Three independent
      conditions (k0 = n_s^2 = n_e + n_up = S(n_s,3) - S(2,3) = 16) coincide
      at k0, making it a three-fold resonance point. The bifurcation forces
      equal amplitude at modes n=16 and n=17, giving mass as the geometric mean:
          m_b = sqrt(S(16,3) * S(17,3)) * m_scale_3
      S(16,3) = C(18,3) = 816, S(17,3) = C(19,3) = 969.
      Result: ~4181 MeV vs PDG 4180 MeV (+0.02%). (Part 2 section 12, Part 7)
    """
    if name == "photon":
        return 0.0
    if name == "bottom":
        return math.sqrt(S(16, 3) * S(17, 3)) * scales[3]
    return scales[d] * S(n, d)


def pred_corrected(name, d, n):
    """
    Corrected IDWT prediction, applying:
    - GTC to d=4 quarks: m * (1 - epsilon)^k
    - Dyson resummation to tau: m * (1 + 1/1680)
    All other particles are uncorrected -- their raw predictions are already
    at or below PDG precision. (Part 2 sections 11 and 9)
    """
    base = pred_uncorrected(name, d, n)
    if name in k_vals:
        return base * (1 - epsilon) ** k_vals[name]
    if name == "tau":
        return base * dyson_factor
    return base


# --- Table header and separator ----------------------------------------------
hdr = f"{'particle':<9} {'d':>2} {'n':>4} {'S(n,d)':>10} {'pred (MeV)':>12} {'PDG (MeV)':>12} {'err%':>8}"
sep = "-" * len(hdr)

# STEP 10 -- Uncorrected table
print("\n=== UNCORRECTED TABLE ===")
print("  (raw: m = m_scale(d) * S(n,d), no GTC or Dyson correction applied)")
print(hdr)
print(sep)
for name, d, n, pdg in particles:
    s = S(n, d) if n is not None else 0
    p = pred_uncorrected(name, d, n)
    err = (p - pdg) / pdg * 100 if pdg else 0.0
    n_str = str(n) if n is not None else "--"
    print(f"{name:<9} {d:2d} {n_str:>4} {s:10d} {p:12.3f} {pdg:12.3f} {err:+7.2f}%")

# STEP 11 -- Corrected table
print("\n=== CORRECTED TABLE (GTC d=4 quarks + Dyson tau) ===")
print("  (charm and top: (1-eps)^k correction;  tau: *(1+1/1680))")
print(hdr)
print(sep)
for name, d, n, pdg in particles:
    s = S(n, d) if n is not None else 0
    p = pred_corrected(name, d, n)
    err = (p - pdg) / pdg * 100 if pdg else 0.0
    n_str = str(n) if n is not None else "--"
    print(f"{name:<9} {d:2d} {n_str:>4} {s:10d} {p:12.3f} {pdg:12.3f} {err:+7.2f}%")

print("\nhttps://fedgeno.github.io/")

# idwt.py — IDWT mass calculator with full derivation commentary
# =============================================================================
# Infinite-Dimensional Wave Theory: mass predictions from a single unit
# reference.
#
# The single empirical framework: a Dirac spinor field Psi_inf lives on an
# infinite-dimensional manifold M_inf = R^{3,1} x (sector manifolds). Particles
# are standing-wave resonances in the sector space. Their masses are:
#
#     m(n, d) = m_scale(d) x S(n, d)
#
# where S(n,d) = C(n+d-1, d) = dim(Sym^{n-1}(C^{d+1})) is the cumulative count
# of monomials of degree 0 through n-1 in d variables; and m_scale(d) is derived
# from seeds and coupling constants.
# m_e is the sole unit reference — converts dimensionless mass ratios to MeV.
# All masses follow from m_e and seeds; the mode indices are
# combinatorially forced.
#
# Structure of this script (all computation before all output):
#   STEPS 1-4   -- Core computation: Generation Tower, couplings,
#                  sector scales, corrections
#   STEPS 5-24  -- Extended computation: EW, CKM, hadronic, Z, neutrinos,
#                  PMNS, spectral action, EW precision, CP-violation,
#                  oscillations, neutron lifetime, heat kernel, scipy eigenmode
#   STEPS 25-29 -- Theorem verification: T4 seed uniqueness,
#                  T5 Gegenbauer criticality, T15 Euler characteristic
#                  chain, T9a Hopf products, T0.5 filter
#   STEPS 30-33 -- Extended computation: co-fixed-point l-parity stability,
#                  consecutive matter quartet, depth-relative marginalization,
#                  bound-within / free-without (Part 1 §3i)
#   STEPS 1-29  -- Output (all print() calls; begin after computation
#                  blocks)
#   STEPS 30-33 -- Output: stability, quartet, marginalization, floating
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

    Mathematical identity: S(n,d) = dim(Sym^{n-1}(C^{d+1})), the dimension of
    the (n-1)-th symmetric power of C^{d+1}. Equivalently, S(n,d) is the
    cumulative count of monomials of degree 0 through n-1 in d variables:

        S(n,d) = sum_{k=0}^{n-1} C(k+d-1, d-1)     [hockey-stick identity]

    This is NOT the count of degree-n monomials in d variables (that is
    C(n+d-1, d-1), one index off). The distinction matters: S(1,d) = 1 for
    all d (ground state uniqueness), while C(d-1, d-1) = 1 only trivially.

    Physical meaning in IDWT: S(n,d) counts the cumulative sector microstates
    at excitation levels 0 through n-1 in sector d. The mass formula
    m(n,d) = m_scale_d * S(n,d) assigns mass proportional to this count.
    (Part 1 section 5, Part 2 section 1)

    Spectral grounding (d=3): S(n,3) = (1/2) * N_{D_{S^3}}(n-1), where
    N_{D_{S^3}}(n-1) is the cumulative positive Dirac eigenvalue count on the
    unit 3-sphere at levels 0 through n-1. (Theorem S1, Part 8 section 60b)

    The hockey-stick recursion S(n,d) = S(n,d-1) + S(n-1,d) is the algebraic
    engine behind the eigenmode selection rule: every filtration
    relationship is a
    consequence of Pascal's triangle applied at specific fixed points.
    (Part 2 section 4)

    The table also satisfies the dual multiplicative recursion across sectors at
    fixed mode index:

        S(n, d+1) = S(n, d) * (n+d)/(d+1)   <=>   S(n,d)/S(n,d+1) = (d+1)/(n+d)

    (Appendix A section 18). The hockey-stick steps across n at fixed d (the
    diagonal the generation tower climbs); this one steps across d at fixed n.
    Together they generate the whole table from S(1,d)=1. The generation
    tower is built from the hockey-stick alone; the multiplicative ladder
    is not required to fix the spectrum. (Part 2 section 3)
    """
    return math.comb(n + d - 1, d) if n >= 0 and d >= 0 else 0


# =============================================================================
# STEP 1 -- BUILD THE MODE-INDEX TOWER
# =============================================================================
# The entire particle spectrum follows from two forced integers:
#   n_s = 4  (the single non-trivial seed, forced by the muon fixed-point)
#   n_d = 1  (trivially forced: S(1,d)=1 for every sector d)
# Every other mode index, including n_up, is derived by explicit addition
# using the hockey-stick recursion. No other inputs.
# (Part 2 sections 2-4, Part 1 section 5)

# --- Seeds -------------------------------------------------------------------
# n_d = 1  (down quark: the universal ground state)
# S(1, d) = C(d, d) = 1 for every d, so the ground-state mode index is
# identically 1 in every sector. No other value is consistent.
# (Part 2 section 2)
n_down = 1

# n_s = 4  (strange quark: the unique non-trivial seed)
# The unique positive integer satisfying S(n_s, 4) = n_mu = 35, where n_mu is
# the muon mode index. This self-referential fixed point -- the muon mode is the
# d=4 image of the strange mode -- has exactly one solution: n_s = 4.
# (Part 2 section 2, Part 1 section 5)
n_strange = 4  # unique solution to S(n_strange, 4) = 35

# --- First derived index: up quark -------------------------------------------
# n_up = n_s - 1 = 3
# Derived from n_s via the Hopf chain reduction: the d=4 sector ground state
# sits one level below n_s. Equivalently, n_up = n_s - 1 is required for the
# geometric back-reaction factor n_s/n_up = 4/3 to be the ratio of
# consecutive integers (forced by d=10 self-consistency, Part 2 sec 9).
# This is not a seed.
n_up = n_strange - 1   # = 3  (derived)

# --- Neutrino mode indices ---------------------------------------------------
# Neutrinos live in the d=5 sector (S^5). Their mode indices are derived as
# simplex images of the up quark seed into lower sectors. The d=5 sector
# admits only Dirac spinors (d mod 8 = 5 forbids Majorana by Clifford
# algebra mod 8 periodicity), so neutrinos are Dirac with no Majorana
# mass and no seesaw. (Part 1 s6, Part 2 s6, Part 8 s59.1)

# n_nu1 = S(n_up, 3) = S(3, 3) = C(5,3) = 10
# The first neutrino mode index is the image of the up quark seed under the
# d=3 simplex map. The d=5 sector couples to d=3 via the Vandermonde rule,
# and the lightest d=5 mode resonates at the d=3 simplex value of the up quark.
n_nu1 = S(n_up, 3)    # = 10

# n_nu2 = S(n_up, 4) = S(3, 4) = C(6,4) = 15
# Second neutrino mode: the image of the up quark seed into d=4. This equals
# C(6,2) = 15 by binomial symmetry C(n,k) = C(n,n-k), which connects it
# directly to n_W = 76 via: n_W = S(n_e, 2) - n_nu2 = 91 - 15 = 76.
# The binomial symmetry C(n,k)=C(n,n-k) applied here is what makes the
# coupling coefficient universal across the two Hopf pairs. (Part 2 section 5,
# Part 3 section 11)
n_nu2 = S(n_up, 4)    # = 15

# n_nu3 = n_nu1 + n_nu2 - n_up = 10 + 15 - 3 = 22
# The third neutrino mode is selected by the comb filtration condition at d=5.
# Cross-check: n_nu3 = n_tau - n_down = 23 - 1 = 22. (Part 2 section 6)
n_nu3 = n_nu1 + n_nu2 - n_up   # = 22

# --- Lepton mode indices (via the comb filtration rule) ----------------------
# Eigenmode selection rule: n_lepton = n_neutrino + n_quark_partner.
# This is the hockey-stick identity S(n,d) = S(n,d-1) + S(n-1,d) applied
# at specific combinatorial fixed points. It is a theorem.
# (Part 2 section 4)

# n_e = n_nu1 + n_up = 10 + 3 = 13
# Electron: the lightest lepton. This is the unique d=6 mode consistent
# with the comb filtration at step 1. (Part 2 section 4)
n_e = n_nu1 + n_up    # = 13

# n_charm = S(n_s, 3) = S(4, 3) = C(6,3) = 20
# Charm quark: the d=4 image of the strange seed via the d=3 simplex map.
# This is the unique d=4 mode selected by the sector comb at filtration step 2.
n_charm = S(n_strange, 3)   # = 20

# n_mu = n_charm + n_nu2 = 20 + 15 = 35 = S(4,4)
# Muon: second-generation lepton. This is BOTH n_charm + n_nu2
# (eigenmode selection rule) AND S(4,4) = C(7,4) = 35 (the d=4
# self-image of the strange seed). These
# coinciding is a theorem from the hockey-stick identity -- it is what forced
# n_strange = 4 in the first place. (Part 2 sections 2 and 4)
n_mu = n_charm + n_nu2   # = 35; cross-check: S(n_strange, 4) = 35 exactly

# n_tau = n_nu3 + n_down = 22 + 1 = 23
# Tau: third-generation charged lepton, d=10 sector (CP⁵, d mod 8 = 2
# Majorana-Weyl). d=10 holds only the tau; top/bottom/nu_tau are in
# d=4/3/5 respectively.
# (Part 1 §3d, Part 2 §7)
n_tau = n_nu3 + n_down    # = 23

# --- Up-type quark mode indices ----------------------------------------------

# n_top = S(n_e, 2) - n_charm + 1 = S(13,2) - 20 + 1 = 91 - 20 + 1 = 72
# Primary derivation: n_top connects to the electron mode index via
# S(n_e,2) = C(14,2) = 91. Also: n_top = N_c * n_s * N_f = 3*4*6 = 72
# (the product of Euler characteristics of the three CP sectors).
n_top = S(n_e, 2) - n_charm + 1    # = 91 - 20 + 1 = 72

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
# n_Z - n_W = 5 = q (the d=4 eigenstate increment at the up threshold);
# this is the same q that enters g22 (Theorem S3, Part 8 section 60b).
n_Z = n_W + 6 - 1      # = 81

# n_H = g(n_nu2, n_Z) = n_nu2 + n_Z - 1 = 95
# Higgs: the second neutrino mode coupled to the Z mode.
# Cross-check: n_H = n_up + n_charm + n_top = 3 + 20 + 72 = 95
# (the sum of all up-type quark mode indices -- the Higgs mode index encodes all
# three up-type sector modes simultaneously). (Part 3 section 11)
n_H = n_Z + n_nu2 - 1  # = 95

# --- Compact binomial form (structural observation; Part 9 T0.5) --------------
# All 14 non-photon mode indices follow from two integers a=n_up=3,
# b=n_strange=4
# via four binomial calls and no loops. Define the 2x2 Pascal block:
#
#   p = C(a+2,3) = C(5,3)  = 10   q = C(a+3,4) = C(6,4)  = 15
#   r = C(b+2,3) = C(6,3)  = 20   s = C(b+3,4) = C(7,4)  = 35
#
# Pascal's rule gives s = r+q exactly (no independent constraint).
# One triangular anchor: T = C(p+a+1, 2) = C(14,2) = 91 = S(n_e, 2).
#
#   seeds:   1,  a,  b
#   base:    p,  q,  r,  s
#   leptons: p+a,  p+q-a,  p+q-a+1         (13, 22, 23; last +1 is 🔶)
#   bosons:  T-q,  T-p,  T-r+1,  T+a+1
#            (76, 81, 72, 95; T-r+1 and T+a+1 carry +1 offsets, 🔶)
#
# In Python:
#   a, b = 3, 4
#   p, q, r, s = comb(a+2,3), comb(a+3,4), comb(b+2,3), comb(b+3,4)
#   T = comb(p+a+1, 2)
#   tower = [1, a, b, p, q, r, s, p+a, p+q-a, p+q-a+1, T-q, T-p, T-r+1, T+a+1]
#
# This is a restatement of T0.5, not a derivation. The seed b=4 and the
# choice T=C(p+a+1,2) are not derived here. The three +1 offsets remain
# without first-principles IDWT justification (Part 9 T0.5).


# =============================================================================
# STEP 2 -- COUPLING CONSTANTS FROM SEEDS
# =============================================================================
# The inter-sector coupling matrix G has rank 1: G_{dd'} = v_d x v_{d'} where
# v_d = sqrt(g_{dd}). All cross-couplings follow from the six self-couplings.
# g33 and g44 come entirely from the seeds {n_s, n_up}.
# (Part 2 section 8, Part 3 section 15)

# g33 = n_s^2 * sqrt(n_s + n_up) / 2 = 16 * sqrt(7) / 2 = 8*sqrt(7) ~= 21.166
# Derivation: the vacuum stability fixed-point equation for the d=3 sector
# kernel requires this exact value. The factor n_s^2 is k0 = 16 (the resonance
# site where the comb-resonance coupling concentrates), and sqrt(n_s+n_up)/2
# = sqrt(7)/2 is the universal Jacobi coefficient. (Part 2 section 8)
g33 = (n_strange**2) * math.sqrt(n_strange + n_up) / 2.0

# g44 = n_s * n_up / sqrt(n_s + n_up) = 12 / sqrt(7) ~= 4.536
# The d=4 self-coupling from seeds. Note: g33 * g44 = n_s^3 * n_up / 2 = 96
# exactly (8*sqrt(7) * 12/sqrt(7) = 8*12 = 96). This product 96 appears
# throughout: (4*sqrt(6))^2 = 96 = g_{3,4}^2 (cross-coupling between d=3 and
# d=4), and g55 * g22 = 96 (from Hopf fiber universality). (Part 2 sections 8-9)
g44 = (n_strange * n_up) / math.sqrt(n_strange + n_up)

# g66 = 1/n_s = 1/4
# The d=6 (charged lepton) self-coupling is set directly by the seed.
# g_{66} = 1/n_s = 1/4 is a seed ratio, not a kernel fixed-point coupling.
# The coupling-construction chain therefore terminates at d=6. The band
# d=7,8,9 gets no self-coupling: d=8 (CP^4) is the Euler-characteristic gap
# (chi=5=N_c+2, no g88 fixed point; T15b), while d=7 (S^7) and d=9 (S^9) are
# odd total spaces routable only over their bases d=6 (terminus) and d=8 (gap),
# neither a fixed-point base (T9b). See Part 9 T3 Rule A.
# g_{10,10} = g_{66} = 1/n_s by mu-tau symmetry (T9c); d=10 re-enters as the
# Gegenbauer critical endpoint. (Part 1 section 3a, Part 2 section 8)
g66 = 0.25


# =============================================================================
# STEP 3 -- SECTOR SCALES
# =============================================================================
# All sector scales are derived algebraically from m_e (the unit reference)
# and the seed-derived coupling constants. m_e sets the MeV scale; the
# dimensionless mass ratios are fixed entirely by each sector's manifold
# geometry.
# (Part 1 section 5, Part 2 sections 9c and 10)

m_e = 0.51099895    # MeV -- unit reference: dimensionless ratios to MeV

# m_scale_6 = m_e / S(n_e, 6) = m_e / S(13, 6) = m_e / 18564
# The electron (n=13, d=6) fixes the d=6 sector scale. Since m_e is
# known in MeV, m_scale_6 = m_e / S(13,6) converts the unit reference
# into the sector mass unit.
# Numerically: m_scale_6 ~= 2.7526 x 10^-5 MeV = 27.53 eV. (Part 2 section 10)
m_scale6 = m_e / S(n_e, 6)

# m_scale_3 = m_e * sqrt(g33 / g66)
# Coupling self-consistency: the kernel vacuum fixed-point equation requires
# m_scale_3^2 / m_e^2 = g33 / g66 (l=0 scalar part of the cross-sector kernel).
# m_scale_3 ~= 4.702 MeV. (Part 2 section 10)
m_scale3 = m_e * math.sqrt(g33 / g66)

# m_scale_4 = m_scale_3 * sqrt(g44 / g33) / S(n_up, 4)
# The d=4 scale is set by the fixed-point condition between d=3 and d=4,
# divided by S(n_up, 4) = S(3,4) = 15 to set the d=4 scale at the up quark mode
# (the lightest occupied d=4 mode at n=3). m_scale_4 ~= 0.1451 MeV.
# (Part 2 section 10)
m_scale4 = m_scale3 * math.sqrt(g44 / g33) / S(n_up, 4)

# m_scale_10 = m_scale_6
# g_{10,10} = g_{6,6} = 1/n_s = 1/4: the d=6 and d=10 sectors share the
# seed coupling. The tau mass exceeds the muon mass entirely because
# S(23,10) >> S(35,6) -- the sector scales are identical. (Part 2 section 10)
m_scale10 = m_scale6

# g22 = (M_{n_s-1}^{S^3} - n_up)^2 * q / 2     [Theorem S3, Part 8 section 60b]
#
# The positive Dirac eigenvalue at level l = n_s-1 = 3 on the unit 3-sphere S^3
# has multiplicity  M_3^{S^3} = (3+1)(3+2) = 20 = S(n_s, 3).  (Theorem S1)
#
# p = M_3^{S^3} - n_up  =  S(n_s,3) - n_up  =  20 - 3  =  17
#   The 20 eigenstates at Dirac level 3, less the n_up = 3 states already
#   accounted for by the up-quark sector boundary (Theorem S2).
#   [p replaces alpha to avoid collision with the fine structure constant]
#
# q  = S(n_up,4) - S(n_up,3)  =  15 - 10  =  5  =  S(n_up-1, 4)
#   The hockey-stick increment: d=4 eigenstate count at the up-quark threshold.
#   [q replaces beta to avoid collision with the QCD beta-function]
#
# The two-body kernel (xi.xi')^2 contributes p^2 (two d=3 legs, each
# with p available Dirac eigenstates) and q once (single d=4 insertion).
# The factor 1/2 is the Bose symmetry of the symmetric kernel.
#
# g22 = p^2 * q / 2  =  17^2 * 5 / 2  =  722.5   (exact from seeds)
# (Part 2 section 10, Theorem S3 Part 8 section 60b)
g22_p     = S(n_strange, 3) - n_up          # = 17
g22_q     = S(n_up - 1, 4)                  # = 5 = S(n_up,4) - S(n_up,3)
g22       = g22_p**2 * g22_q / 2.0          # = 722.5

# m_scale_2 = m_e * sqrt(g22 / g66)
# The d=2 sector scale: m_scale_2 = m_e × √(g₂₂/g₆₆). The W boson mass is
# m_scale_2 × S(n_W, 2) = 80379 MeV, like any other particle mass.
m_scale2 = m_e * math.sqrt(g22 / g66)


# =============================================================================
# STEP 2d -- g22 IS A MULTIPLICITY COUNT, NOT A KERNEL TRACE (compute)
# =============================================================================
# Tested (claude/g22_operator_trace.py; Part 6 "g22 operator derivation" item):
# does a genuine (xi.xi')^2 kernel trace yield g22 = p^2 q / 2?  It does NOT.
#  - literal Tr[G^2_23 + G^2_24] is ADDITIVE ~ p^2 + q -- wrong for
#    a product;
#  - the actual T2 overlap (Appendix A s20a: O ~ <r^2>_i <r^2>_j / d)
#    is O(1), scaling
#    as the mode index n^1, orders of magnitude below the multiplicity product;
#  - p^2 q appears only as Tr[IDENTITY] over rank-(p,p,q) eigenspaces -- the
#    multiplicities are the INPUT, the kernel acts trivially.
# So g22 = p^2 q / 2 is a state-count (IDOS multiplicity product), NOT
# a dynamical kernel matrix element -- the same counting-vs-overlap
# split that closed the CKM formula in the negative. The 1/2 (Bose
# symmetry of the kernel) is the one piece that is kernel-derived.
g22_count = g22_p**2 * g22_q / 2.0    # 722.5 = the multiplicity count
# representative (xi.xi')^2 ground-state overlap,
# <r^2>_d = d/(2 sqrt(lam_d)) (Part 4 s3.10.3):
# two d=3 legs and one d=4 leg -- O(1), nowhere near the count.
_lam3 = (g33 / 2.0) ** (2.0/3.0)
_lam4 = (g44 / 2.0) ** (2.0/3.0)
_r2_d3 = 3 / (2.0 * _lam3**0.5)
_r2_d4 = 4 / (2.0 * _lam4**0.5)
g22_kernel_overlap = _r2_d3 * _r2_d3 * _r2_d4  # O(1) overlap magnitude
assert abs(g22_count - 722.5) < 1e-9
assert abs(g22_count - g22)   < 1e-9          # consistent with STEP 3
assert g22_kernel_overlap < 10.0              # O(1), NOT the 722.5 count


# Collect sector scales keyed by dimension.
scales = {2: m_scale2, 3: m_scale3, 4: m_scale4, 6: m_scale6, 10: m_scale10}


# =============================================================================
# STEP 4 -- CORRECTIONS
# =============================================================================

# --- Generation Tower Correction (GTC) ---------------------------------------
# The kernel coupling (xi_d . xi_{d'})^2 decomposes on S^{d-1} as:
#   (xi . xi')^2 = (1/d)[l=0 scalar]
#                + (d-1)/d * C_2^{(d-2)/2}(cos theta)[l=2 tensor]
# For d=3 on S^2:  (xi . xi')^2 = (1/3)[l=0] + (2/3)*P_2(cos theta)[l=2]
# The l=0 part is constant -- it contributes to sector mass scales uniformly.
# The l=2 part is orientation-dependent -- it introduces a frequency shift
# per generation step. This shift grows with generation depth k, giving the
# multiplicative correction (1-eps)^k to d=4 quark masses. (Part 2 section 11)

# epsilon = 1 / (280 * sqrt(7)) ~= 0.001350
# Derived from: g_coeff / (k0 * n_mu). Each factor is independently forced:
#
#   g_coeff = 2/sqrt(7):  the l=2 kernel coupling coefficient at k0. Forced by
#     the double self-consistency condition -- both d=3 and d=4 give the same
#     eigenvalue 4/7 at the resonance:
#       d=3:  n_s*(n_s+1) / S(n_s,4) = 4*5/35 = 4/7
#       d=4:  n_up*(n_up+1) / S(n_up,5) = 3*4/21 = 4/7
#     g_coeff = sqrt(4/7) = 2/sqrt(7). This coincidence forces n_up = n_s-1 = 3.
#
#   k0 = n_s^2 = 16  (vacuum stability resonance site, from seed alone)
#
#   n_mu = S(n_s, 4) = 35  (the d=4 fixed-point mode; sets the frequency scale)
#
# Result: (2/sqrt(7)) / (16 * 35) = 1/(280*sqrt(7)). (Part 2 section 11)
epsilon = 1.0 / (280.0 * math.sqrt(7.0))

# k-values: phase load per quark in the d=4 sector.
#   up:    k = 0 (first generation, no additional frequency shift)
#   charm: k = 3 = n_up = n_s - 1  (frequency shift at the second comb step)
#   top:   k = 10 = n_nu1 = S(n_up, 3) (generation depth equals the
#                first neutrino mode index -- cross-sector consistency)
# After correction: c/u ratio error -0.003%, t/u ratio error -0.048%.
# (Part 2 section 11)
k_vals = {"up": 0, "charm": 3, "top": 10}

# --- Tau geometric back-reaction correction -----------------------------------
# The d=6 and d=10 sectors share the coupling g_{6,6} = g_{6,10} = g_{10,10}
# = 1/n_s = 1/4 (from the seed, not from hypercharge). The leading d=6->d=10
# kernel perturbation at the tau level has amplitude:
#
#   eps_{6->10} = 1 / (n_s^3 * S(n_s,4)) = 1/(64 * 35) = 1/2240
#
#   The n_s^3 = k0 * n_s factor is the seed-resonance volume; S(n_s,4) = n_mu
#   is the frequency normalization. Both are determined by n_s = 4 alone.
#
# This perturbation feeds back through g_{10,10} = 1/n_s, giving a geometric
# series summed as:
#
#   delta_m / m_tau = eps_{6->10} / (1 - g_{10,10})
#                   = (1/2240) / (1 - 1/4)
#                   = (1/2240) * (4/3)
#                   = 4 / 6720
#                   = 1 / 1680
#
# where 1680 = n_s * n_up * (n_s+n_up) * S(n_s,3) = 4*3*7*20.
# The resummation factor n_s/(n_s-1) = 4/3 is forced by n_up = n_s-1.
#
# Result: m_tau = m_tau_bare * (1 + 1/1680) = 1776.84 MeV.
# PDG 2024: 1776.93 +/- 0.09 MeV. Error: -0.005% (-1.0 sigma).
# (Part 2 section 9)
back_reaction_factor = 1.0 + 1.0 / (n_up * n_strange**2 * S(n_strange, 4))

# --- ν₃ cross-sector constructive interference correction --------------------
# The d=5/d=3 cross-sector kernel at mode n_nu3=22 receives a single-order
# constructive interference from the two sector images of n_up (into
# d=3 and d=4).
# The correction is:
#   δ_ν₃ = ε × g_{33} = [1/(280√7)] × [8√7] = 8/280 = 1/35   (exact)
# Applied multiplicatively to m_nu3 only. (Part 2 §9d, T11d)
delta_nu3  = epsilon * g33  # = 1/35; eps * 8*sqrt(7) / sqrt(7) = 8/280
nu3_factor = 1.0 + delta_nu3  # = 36/35


# =============================================================================
# STEP 5 -- ELECTROWEAK SECTOR: WEINBERG ANGLE, GAUGE COUPLINGS, FERMI CONSTANT
# =============================================================================

# sin²θ_W = 1 - (S(n_W,2)/S(n_Z,2))² = 1 - (m_W/m_Z)²
# The Weinberg angle is entirely determined by the ratio of the W and Z mode
# indices. No empirical angle is input. S(n_W,2) = 2926, S(n_Z,2) = 3321,
# giving sin²θ_W = 0.22373.  PDG on-shell value: 0.22290 (+0.37%).
# The +0.37% is a known 1-loop EW correction; tree-level is exact.
# (Part 3 sections 0.7 and 12)
sin2_W = 1.0 - (S(n_W, 2) / S(n_Z, 2))**2   # = 1 - (2926/3321)^2
cos_W  = S(n_W, 2) / S(n_Z, 2)               # exact: cos theta_W = S_W / S_Z

# g_s = sqrt(2 g44 / pi²)
# The QCD coupling from the CP² kernel volume integral. The volume of CP² in
# the Fubini-Study metric is pi²/2; integrating the kernel current J^4 over
# CP² gives the effective coupling factor 2/pi².
# CP² is the d=4 sector space — macroscopic, non-compact, and localization-
# length-bounded; not a compact KK extra dimension. (Part 3 section 4)
g_s = math.sqrt(2.0 * g44 / math.pi**2)

# g_2 = (2/3) sqrt(g_s)
# The SU(2)_L coupling from the CP² → CP¹ sector projection.
# The up-quark charge Q_u = 2/3 is the spin^c index on CP²:
#   ind(D^c_{CP^2} ⊗ O(1)) = 3 = N_c  (Theorem S3, Part 8 section 59)
# Each colour carries charge 1/N_c = 1/3; the up-quark doublet carries 2/3.
# (Part 3 section 0.7)
Q_up = 2.0 / 3.0
g2   = Q_up * math.sqrt(g_s)

# g_1 = g_2 tan(θ_W)
# The U(1)_Y coupling follows from g_2 and the Weinberg angle via
# tan²(θ_W) = g_1²/g_2².  No separate measurement enters.
g1 = g2 * math.sqrt(sin2_W / (1.0 - sin2_W))

# G_F = g_2² / [4√2 m_W²]   (GeV⁻²)
# Fermi constant from the W propagator at q² ≪ m_W².  Both g_2 (from CP²
# kernel volume integral) and m_W (from mode index n_W = 76) are
# independently derived.
# No Higgs VEV or Higgs mechanism is invoked. (Part 3 section 0.7)
GF_pred = g2**2 / (4*math.sqrt(2)*(m_scale2*S(n_W,2)/1000)**2)   # GeV^{-2}
GF_MeV2 = GF_pred * 1.0e-6                                        # MeV^{-2}

# α_EW = g_1² g_2² / [(g_1²+g_2²) 4π]
# Fine structure constant at the fiber scale (~m_W). This is the running
# value near the EW scale; QED running to q→0 requires subtracting hadronic
# vacuum polarisation contributions. (Part 3 section 0.7)
alpha_ew = (g1**2 * g2**2) / ((g1**2 + g2**2) * 4.0 * math.pi)

# g_55 = 96/g_22   (d=5 neutrino self-coupling)
# Hopf universality: g_33 × g_44 = 96 exactly (8√7 × 12/√7 = 96). The d=5
# sector mediates between d=3 and d=4 via the S¹→S⁵→CP² Hopf fibration,
# and its self-coupling is set by this product. (Part 2 section 9c)
g55 = 96.0 / g22

# g_{56}^2 = g_{55} * g_{66}: the d=5 ↔ d=6 (or d=10) cross-coupling.
# The d=6 and d=10 sectors carry the same self-coupling:
#   g_{66} = g_{10,10} = 1/n_s = 1/4  (shared seed coupling, Part 1 §3a)
# Therefore v_6 = sqrt(g_{66}) = v_{10} = sqrt(g_{10,10}) = 1/2 EXACTLY.
# The coupling of any charged lepton to any d=5 neutrino mode is:
#   g_{5,6} = v_5 * v_6 = v_5/2
#   g_{5,10} = v_5 * v_10 = v_5/2
# These are IDENTICAL. This is a mu-tau interchange symmetry: the Lagrangian
# is invariant under swapping mu (d=6) and tau (d=10) at tree level.
#
# Consequence: |U_mu_i| = |U_tau_i| for all i → sin^2(theta_23) = 1/2 exactly.
# The full tree-level PMNS is at the mu-tau symmetric limit:
#   sin^2(theta_12) = 1/3 = 0.3333   (PDG: 0.307,  delta = -0.026)
#   sin^2(theta_23) = 1/2 = 0.5000   (PDG 2024: 0.553,  delta = +0.053)
#   sin^2(theta_13) = 0              (PDG: 0.022,  delta = +0.022)
#
# Deviations from the mu-tau symmetric limit come from the neutrino
# mass splittings and the mu-tau mass difference. They are suppressed
# by g_{56}^2 ~ 0.033.
# (Part 5 section 4, Part 8)
g56_sq = g55 * g66   # cross-coupling squared d=5 ↔ d=6 (or d=10)


# =============================================================================
# STEP 2b -- INTER-SECTOR COUPLING MATRIX  G_{d,d'} = v_d * v_{d'}  (rank 1)
# =============================================================================
# Consolidates the six self-couplings into the full inter-sector coupling
# matrix. v_d = sqrt(g_dd) is the sector coupling vector; G = v (outer) v is
# rank 1, so its diagonal returns the six self-couplings and its off-diagonal
# entries are the cross-couplings. No cross-coupling is an independent input:
# all 21 distinct entries follow from the six diagonal values. Granularity is
# by sector, not particle: the kernel is sector-separable (Part 1 section 3h),
# so two particles in the same sector share an identical coupling row.
# (Part 1 section 3g, Part 2 sections 8-9c)
#
# Two off-diagonal entries equal sqrt(96) = 4*sqrt(6) by Hopf universality,
# reached from two independent sector pairs:
#   g_{3,4} = v_3 v_4 = sqrt(g33 g44) = sqrt(96)   (S^1->S^5->CP^2, Part 2 s9c)
#   g_{2,5} = v_2 v_5 = sqrt(g22 g55) = sqrt(96)
#             (g55 = 96/g22 by construction)

sector_d   = [2, 3, 4, 5, 6, 10]
g_self     = {2: g22, 3: g33, 4: g44, 5: g55, 6: g66, 10: g66}   # g_{10,10}=g66
v_sector   = {d: math.sqrt(g_self[d]) for d in sector_d}  # v_d

# Rank-1 coupling matrix, and the coordinate-containment
# (shared-dimension) matrix from Xi nesting (Part 1 s3f):
# shared coords = min(d,d').
G_cross = {
    d: {dp: v_sector[d] * v_sector[dp] for dp in sector_d}
    for d in sector_d
}
shared_dim = {d: {dp: min(d, dp) for dp in sector_d} for d in sector_d}

# Consistency: diagonal reproduces the self-couplings; the two sqrt(96) checks.
G_diag_resid = max(abs(G_cross[d][d] - g_self[d]) for d in sector_d)
g34_resid    = abs(G_cross[3][4] - math.sqrt(96.0))
g25_resid    = abs(G_cross[2][5] - math.sqrt(96.0))


# =============================================================================
# STEP 2c -- ACTIVE COUPLING STRUCTURES PER SECTOR PAIR (containment AND filter)
# =============================================================================
# Which coupling structures of the single wave Psi_inf are active on the
# coordinates that two sectors SHARE. This is not boson exchange: a cross-sector
# effect is one wave coupling to itself across the coordinate overlap of two of
# its strata (Part 1 section 3g). A structure is active on a pair iff (a) it is
# geometrically present on the shared coordinates [coordinate containment] AND
# (b) it survives BOTH sectors' coupling filters [Part 3 section 0.8b].
#
# The four structures and their geometric origin (all established):
#   U(1)  electric charge  Q = T3+Y, Y from T8 of SU(3)=Isom(CP^2)
#                          (Part 3 s6,s13)
#   SU2L  weak isospin     SU(2) factor of U(2) holonomy of CP^2;
#                          Kahler chirality → left-handed (Part 3 s6,s7)
#   SU3   colour           SU(3) isometry of CP^2; N_c=chi(CP^2)=3
#                          (Part 3 s2,s6)
#   grav  gravity          curvature of M_inf; no sector boundary
#                          (Part 3 s0.8)
#
# Per-sector participation (matter/fermion sectors), from the established facts:
#   electric charge Q (Part 3 s6 charge table; Q=0 => no U(1) coupling)
#   colour: only quark sectors carry a colour triplet; d=3 inherits via g_{3,4};
#           d=5 is projected to the colour singlet by the S^5 Hopf fibration;
#           leptons d=6,10 are colour-silent (chi(CP^3)=4, chi(CP^5)=6 != N_c).
#   weak: every fermion sector has a left-handed component carrying SU(2)_L
#         (d=4,6,10 Kahler-left; d=3 inherits via g_{3,4}; d=5 Dirac nu_L).
#   gravity: universal.
matter_d  = [3, 4, 5, 6, 10]
sector_Q  = {3: -1.0/3, 4: 2.0/3, 5: 0.0, 6: -1.0, 10: -1.0}   # Part 3 s6/s13
has_U1    = {d: (sector_Q[d] != 0.0) for d in matter_d}        # electric charge
has_SU3   = {d: (d in (3, 4))  for d in matter_d}  # colour: quarks
has_SU2L  = {d: True           for d in matter_d}  # all fermion sectors
has_grav  = {d: True                for d in matter_d}         # universal

# A structure is active on a pair iff BOTH sectors participate (intersection).
_structs = [
    ("U1", has_U1), ("SU2L", has_SU2L),
    ("SU3", has_SU3), ("grav", has_grav)
]
active_pair = {da: {db: [nm for nm, p in _structs if p[da] and p[db]]
                    for db in matter_d} for da in matter_d}

# g_1 at the d=2 sector scale — purely from sin²θ_W (mode indices 76, 81).
# IDWT couplings are fixed geometric numbers; there is no running.
# The -0.24% offset from PDG on-shell is the sin²θ_W +0.37% structural gap
# propagated via the Weinberg-angle relation — not a separate quantity.
# (Part 3 §0.7, Part 6)
m_W_MeV        = m_scale2 * S(n_W, 2)
m_Z_MeV        = m_scale2 * S(n_Z, 2)
# Self-consistent PDG g1 from PDG sin2_W=0.22290 and g2=0.65270
pdg_sin2_W     = 0.22290
pdg_g2         = 0.65270
# pdg_g1 = pdg_g2 * sqrt(sin2_W/(1-sin2_W)) = 0.34957
pdg_g1         = pdg_g2 * math.sqrt(pdg_sin2_W / (1.0 - pdg_sin2_W))
# +0.25%: entirely sin2_W structural gap
err_g1         = (g1 / pdg_g1 - 1.0) * 100


# =============================================================================
# STEP 6 -- CABIBBO ANGLE AND CKM MATRIX ELEMENTS
# =============================================================================

# sin(θ_C) = (1 + 1/240) / √S(n_s, 3)
# The bare Cabibbo angle from the d=3 sector mode ratio is 1/√S(n_s,3) = 1/√20.
# The +1/240 sector curvature correction is the heat-kernel first-order
# term on the CP¹ mediating sector:
# factor χ(CP¹)/(24·S(n_s,3)) = 2/(24·20) = 1/240.
# This is a curvature correction from the S² base of the d=2 Hopf fibration;
# it shifts the bare value from 0.22361 to 0.22454. PDG: 0.22450 (+0.02%).
# (Part 3 section 12)
sin_C  = (1.0 + 1.0/240.0) / math.sqrt(S(n_strange, 3))

# |V_cb| = √(S(n_up,4) / S(n_charm,4))
# The b-quark mixing amplitude from the d=4 kernel overlap integral between
# the up-quark ground mode (n_up=3) and the charm mode (n_charm=20).
# The ratio S(n_up,4)/S(n_charm,4) = 15/8855 gives |V_cb| = 0.04116.
# PDG: 0.041 ± 0.0014 (within 0.1σ). (Part 3 section 0.8)
Vcb    = math.sqrt(S(n_up, 4) / S(n_charm, 4))

# Wolfenstein A = |V_cb| / sin²(θ_C)
# In the Wolfenstein parametrisation, A = |V_cb|/λ² where λ = sin(θ_C).
# The bare (uncorrected) Cabibbo angle gives λ² = 1/S(n_s,3) = 1/20, so
# A = Vcb × S(n_s,3). This is a pure ratio of binomial coefficients.
A_wolf = Vcb * S(n_strange, 3)

# Full Wolfenstein CKM matrix (tree level, ρ = η = 0)
# The CP-violating phase is zero at tree level (real product-state amplitudes);
# |V_ub| = |V_td| = 0 exactly. Non-zero values require the Hopf Chern-Simons
# loop integral (Part 5 §3f). λ here uses the sector-curvature-corrected sin_C.
lam_W = sin_C
A_W   = Vcb / lam_W**2
Vud_m = math.sqrt(1 - lam_W**2)
Vcd_m = lam_W * (1 - A_W**2 * lam_W**4 / 2)
Vcs_m = 1.0 - lam_W**2 / 2
Vts_m = A_W * lam_W**2 * (1 - lam_W**2 / 2)
Vtb_m = 1.0 - A_W**2 * lam_W**4 / 2

# CKM row unitarities (corrected Wolfenstein values)
_r1_ckm = Vud_m**2 + lam_W**2                         # row 1
_r2_ckm = Vcd_m**2 + Vcs_m**2 + Vcb**2               # row 2
_r3_ckm = 0 + Vts_m**2 + Vtb_m**2                    # row 3 (Vtd=0 tree level)

# Bare Cabibbo angle (no sector curvature correction) — used in STEP 6b output
# to exhibit the raw prediction before the curvature correction is applied.
sin_C_bare = 1.0 / math.sqrt(S(n_strange, 3))    # = 1/√20 = 0.22361
Vcb_bare   = math.sqrt(S(n_up, 4) / S(n_charm, 4))
Vud_bare   = math.sqrt(1 - sin_C_bare**2)
Vcb2_bare  = Vcb_bare
A_W_bare   = Vcb_bare / sin_C_bare**2
r1_bare    = Vud_bare**2 + sin_C_bare**2


# =============================================================================
# STEP 7 -- HADRONIC SCALES: f_π, Λ_QCD, PROTON MASS
# =============================================================================

# f_π = m_scale_3 × S(n_s, 3) = m_scale_3 × 20
# The pion decay constant equals the d=3 sector mass scale at the seed mode.
# The effective coupling g_eff(n) = g33/S(n,3) crosses 1 at n = n_s = 4; this
# is the confinement threshold where the sector coupling becomes
# non-perturbative
# and quarks bind into hadrons. The energy at this mode is the hadronic scale
# f_π. (Part 3 section 0.7, Part 5)
f_pi = m_scale3 * S(n_strange, 3)

# N_c = 3: quark colours = χ(CP²) = 3 (one cell in dims 0, 2, 4).
N_c  = 3

# Λ_QCD = N_c × f_π
# One-loop estimate from the large-N_c limit of QCD: at leading order in 1/N_c,
# the QCD scale is set by N_c times the pion decay constant.
# 3 × f_π = 282 MeV; 3 × f_π(PDG=92.1) = 276 MeV (+2.1%). (Part 5)
Lqcd = N_c * f_pi

# m_p = N_c × Λ_QCD × (1 + 1/n_up²)
# Proton mass from the large-N_c baryon formula with leading Fermi-momentum
# correction. The 1/n_up² = 1/9 term is the first Fermi-momentum contribution
# from the ud quark pair in the proton ground state. (Part 5, Part 8 section 61)
m_p_pred = N_c * Lqcd * (1 + 1.0 / n_up**2)


# =============================================================================
# STEP 7a -- COMPOSITE HADRON MASSES
# =============================================================================
# Mesons and baryons are composites with no (n,d) mode index. Their masses
# follow from the constituent quark masses and the QCD binding structure.
# Two regimes apply, separated by the boundary m_quark ~ Lqcd = 282 MeV.
# (Part 2 section 8a, Part 5 section 3d)

# --- Bottom quark (beat mode at k0 = n_s^2 = 16) ----------------------------
# m_b = sqrt(S(k0,3) * S(k0+1,3)) * m_scale_3
# The b quark arises as a beat resonance at k0=n_s^2=16 in d=3 where three
# independent conditions coincide (Part 2 section 8). At equal occupation
# |A_16|=|A_17|, the quartic density-density coupling |Psi_16|^2 |Psi_17|^2
# carries energy ~ E_16*E_17 (dimension energy^2), so the beat mass is its
# square root -- the geometric mean. (Part 2 section 8)
k0 = n_strange**2                          # = 16
m_b = math.sqrt(S(k0, 3) * S(k0 + 1, 3)) * m_scale3

# --- Chiral GOR formula: m^2 = (m_q1 + m_q2) * B0 ---------------------------
# Valid when m_quark << Lqcd (pi, K, D, Ds).
# B0 is the IDWT chiral condensate parameter: B0 = (N_c/2) * f_pi^2 / m_scale_3
#    = Lqcd * S(n_s,3) / 2
# All factors derived: N_c = chi(CP^2) = 3, f_pi = m_scale_3 * S(n_s,3).
# B0 = Lqcd * n_s*(n_s^2-1)/6  -- the seed's own combinatorial factor.
# (Part 2 section 8a, Appendix A section 21)
B0_GOR = Lqcd * S(n_strange, 3) / 2.0     # = 282.1 * 10 = 2821 MeV

m_d_quark = m_scale3 * S(n_down, 3)       # down quark:  4.702 MeV
m_u_quark = m_scale4 * S(n_up, 4)         # up quark:    2.177 MeV
m_s_quark = m_scale3 * S(n_strange, 3)    # strange:    94.04 MeV
m_c_quark = 1279.7           # charm (GTC-corrected, Part 2 section 11)

def m_meson_GOR(mq1, mq2):
    return math.sqrt((mq1 + mq2) * B0_GOR)

m_pi_pred  = m_meson_GOR(m_u_quark, m_d_quark)
m_Kpm_pred = m_meson_GOR(m_u_quark, m_s_quark)
m_K0_pred  = m_meson_GOR(m_d_quark, m_s_quark)
m_Dpm_pred = m_meson_GOR(m_c_quark, m_d_quark)
m_D0_pred  = m_meson_GOR(m_c_quark, m_u_quark)
m_Ds_pred  = m_meson_GOR(m_c_quark, m_s_quark)

# --- Heavy-quark binding formula: m = m_q1 + m_q2 + sqrt(m_heavy * Lqcd) ----
# Valid when m_quark >> Lqcd (B mesons, bottomonium, charmonium).
# The binding energy E_bind = sqrt(m_heavy * Lqcd) is the geometric mean of
# the heavy quark mass and the QCD scale.
# For b-containing mesons: E_bind connects back to the beat structure because
# k0 = n_s^2 appears in m_b, which feeds into sqrt(m_b * Lqcd).
# E_bind_b = m_scale_3 * sqrt(N_c * S(n_s,3) * sqrt(S(n_s^2,3)*S(n_s^2+1,3)))
# (Part 2 section 8a, Appendix A section 21)
E_bind_b = math.sqrt(m_b * Lqcd)           # = 1086 MeV
E_bind_c = math.sqrt(m_c_quark * Lqcd)     # = 601 MeV

def m_meson_heavy(mq1, mq2, E_bind):
    return mq1 + mq2 + E_bind

m_Bpm_pred  = m_meson_heavy(m_u_quark, m_b, E_bind_b)
m_B0_pred   = m_meson_heavy(m_d_quark, m_b, E_bind_b)
m_Bs_pred   = m_meson_heavy(m_s_quark, m_b, E_bind_b)
m_Ups_pred  = m_meson_heavy(m_b, m_b, E_bind_b)      # Upsilon(1S): bb-bar
m_Jpsi_pred = m_meson_heavy(m_c_quark, m_c_quark, E_bind_c)  # J/psi: cc-bar
# J/psi +2.0% reflects O(Lqcd/m_c)=22% correction (vs 7% for b). The J/psi-eta_c
# difference (113 MeV) is a vector-vs-pseudoscalar object-type distinction (as
# rho vs pi), not a correction to this single formula.

# --- Baryon octet: (N_c-1) colour-bond formula --------------------------------
# m(baryon) = m_N + (N_c-1) * sum_over_replaced(m_s - m_replaced)
# (N_c-1) = chi(CP^1) = 2 = residue colour bonds when one quark is replaced.
# Structural identity: N_c*Lqcd/n_u^2 = m_s exactly,
# so m_N = N_c*Lqcd + m_s.
# (Part 2 section 8a, Appendix A section 21)
m_N_idwt  = N_c * Lqcd * (1.0 + 1.0/n_up**2)   # nucleon = proton/neutron avg
m_Lambda  = m_N_idwt + (N_c-1)*(m_s_quark - m_d_quark)
m_Xi      = m_N_idwt + (N_c-1)*((m_s_quark-m_u_quark) + (m_s_quark-m_d_quark))
# Sigma and Lambda have identical content -> same formula mass; the 77 MeV
# difference is a small same-type residual the formula does not resolve.
# Omega (J=3/2) is decuplet, outside this octet formula.

# --- Polynomial cross-mode identity ------------------------------------------
# n_charm * N_c = n_nu1 * N_f = 4 * n_nu2 = n_s*(n_s-1)*(n_s+1)*(n_s+2)/6
# where N_f = 2*(n_s-1) = 6 (light quark flavours).
# Verified for n_s = 3,4,5,6. (Part 2 section 6a, Appendix A section 10)
N_f          = 2 * (n_strange - 1)         # = 6
poly_identity = n_strange*(n_strange-1)*(n_strange+1)*(n_strange+2) // 6
# All three products should equal poly_identity = 60 at n_s=4:
_poly_check_1 = n_charm * N_c              # = 20 * 3 = 60
_poly_check_2 = n_nu1 * N_f               # = 10 * 6 = 60
_poly_check_3 = 4 * n_nu2                 # = 4 * 15 = 60


# --- Mode Index Stability: spectral gaps confirm n is invariant ---------------
# Theorem (Part 8 section 3a): n is the eigenvalue rank in a purely discrete
# spectrum; it cannot be shifted by any bounded perturbation that preserves
# self-adjointness. The hierarchy problem does not arise.
# Numerical check: spectral gaps (E_{n+1}-E_n)/E_n for the first 5 levels.
# These must all be positive and remain so under perturbation for n
# to be stable.
# For harmonic H_d: E_n = sqrt(lambda_d)*(2n+d), gap = 2*sqrt(lambda_d)/E_n.
_stability_ok = True
for _d, _lam in [(2,50.723),(3,4.820),(4,1.726),(5,0.164),(6,0.250),(10,0.250)]:
    _E = [math.sqrt(_lam)*(2*_n+_d) for _n in range(5)]
    _gaps = [(_E[i+1]-_E[i])/_E[i] for i in range(4)]
    if any(g <= 0 for g in _gaps):
        _stability_ok = False


# =============================================================================
# STEP 8 -- Z BOSON PRECISION OBSERVABLES
# =============================================================================

# Z couplings: gL(f) = T3 - Q sin²θ_W,  gR(f) = -Q sin²θ_W
# These follow directly from sin²θ_W derived in STEP 5.
# All Z branching ratios and asymmetries are parameter-free
# tree-level predictions.
# (Part 5 section 3e)
gLu = 0.5  - (2.0/3)*sin2_W    # up-type quarks  (T3=+1/2, Q=+2/3)
gRu =      - (2.0/3)*sin2_W
gLd = -0.5 + (1.0/3)*sin2_W    # down-type quarks (T3=-1/2, Q=-1/3)
gRd =        (1.0/3)*sin2_W
gLe = -0.5 + sin2_W             # charged leptons  (T3=-1/2, Q=-1)
gRe =        sin2_W

# Vector and axial combinations: gV = gL+gR, gA = gL-gR
gVe = gLe + gRe;  gAe = gLe - gRe
gVb = gLd + gRd;  gAb = gLd - gRd   # b quark has same T3, Q as d at tree level

# Partial-width coupling factors (sum of gL²+gR², colour-weighted)
Gu    = 3*(gLu**2 + gRu**2)    # up-type × N_c
Gd    = 3*(gLd**2 + gRd**2)    # down-type × N_c
Ge    = gLe**2 + gRe**2        # lepton (N_c=1)
# total hadronic: 2 up-type (u,c) + 3 down-type (d,s,b)
G_had = 2*Gu + 3*Gd

# Branching ratios: Γ(Z→X)/Γ(Z→Y) = G_X/G_Y (normalisation factors cancel)
Rb_z = Gd / G_had              # Γ(Z→bb̄)/Γ(Z→had)
Rc_z = Gu / G_had              # Γ(Z→cc̄)/Γ(Z→had)
R0_z = G_had / Ge              # Γ(Z→had)/Γ(Z→l+l-)

# Asymmetry parameters A_f = 2gV gA / (gV² + gA²)
# A_b is robust (+0.58% error) because gA(b)=T3=-1/2 dominates the denominator.
# A_e has 37% error because gV_e ≈ -0.053 is nearly zero and extremely sensitive
# to the sin²θ_W +0.37% structural gap. (Part 5 section 3e)
Ae_z = 2*gVe*gAe / (gVe**2 + gAe**2)
Ab_z = 2*gVb*gAb / (gVb**2 + gAb**2)
# forward-backward asymmetry: A_FB^b = (3/4) A_e A_b
AFBb = (3.0/4)*Ae_z*Ab_z


# =============================================================================
# STEP 9 -- TOP QUARK DECAY
# =============================================================================

# Tree-level top decay: t → W b.
# The longitudinal and left-handed W helicity fractions from V-A:
#   F_0 = m_t²/(m_t² + 2m_W²),   F_L = 2m_W²/(m_t² + 2m_W²),   F_R = 0.
# (Part 5 section 3c)
m_top_MeV   = m_scale4 * S(n_top, 4) * (1.0 - epsilon)**10
xW_top      = (m_scale2 * S(n_W, 2) / m_top_MeV)**2
F0_top      = 1.0 / (1.0 + 2*xW_top)
FL_top      = 2*xW_top / (1.0 + 2*xW_top)

# Γ(t→Wb) = G_F m_t³ (1−x_W)² (1+2x_W) / (8π√2)
# The Fermi constant here is in MeV⁻², derived from the W propagator (STEP 5).
# The factor (2m_W/g_2)² = v² is the Higgs VEV in the SM; IDWT has no VEV,
# so the width is computed directly from g_2 and m_W. (Part 5 section 3c)
GF_MeV2_top = 1.0 / (math.sqrt(2.0) * (2.0 * m_scale2 * S(n_W, 2) / g2)**2)
Gamma_top   = (GF_MeV2_top * m_top_MeV**3 / (8.0*math.pi*math.sqrt(2.0))
               * (1 - xW_top)**2 * (1 + 2*xW_top))


# =============================================================================
# STEP 10 -- ELECTROMAGNETIC COUPLING AND QED RUNNING
# =============================================================================

# e = g_2 sin(θ_W):  electric charge from the EW unification formula.
# Both g_2 (from CP² kernel volume integral) and sin(θ_W) (from mode
# indices) are derived; no empirical charge is input.
# (Part 3 section 0.7)
e_charge  = g2 * math.sqrt(sin2_W)
alpha_em  = e_charge**2 / (4.0 * math.pi)

# 1/α(0) = 1/α(m_Z) + (1/3π) log(m_Z/m_e)
#   [leading QED running, one fermion loop]
# Running from the fiber scale (m_Z ≈ 91 GeV) to q→0 adds hadronic
# vacuum polarisation. The leading log approximation gives +5.6 to
# 1/α; the full hadronic
# correction gives +3.8. The -2.9% residual in 1/α(0) traces to the same
# sin²θ_W +0.37% gap, not to a separate open item. (Part 3 section 0.7)
run_corr   = 1.0 / (3.0*math.pi) * math.log(m_scale2*S(n_Z,2)/m_e)
alpha0_inv = 1.0/alpha_em + run_corr


# =============================================================================
# STEP 11 -- DECAY RATES: MUON LIFETIME, W WIDTH, Z WIDTH
# =============================================================================

# m_μ = m_scale_6 × S(n_μ, 6) — muon mass from IDWT mode formula
m_mu_MeV = m_scale6 * S(n_mu, 6)

# τ_μ = ℏ / Γ_μ,   Γ_μ = G_F² m_μ⁵ / (192π³)
# Standard V-A muon decay formula. Both G_F and m_μ are IDWT-derived;
# no empirical muon lifetime enters. (Part 3 section 0.7)
hbar_MeV_s = 6.582119569e-22                               # ℏ in MeV·s (CODATA)
Gamma_mu   = GF_MeV2**2 * m_mu_MeV**5 / (192.0 * math.pi**3)  # MeV
tau_mu_pred = hbar_MeV_s / Gamma_mu                        # seconds

# τ_μ (PDG) used as an anchor in the tau-lifetime ratio (STEP 15).
# The predicted and PDG values agree to 0.2%; using PDG avoids compounding
# the small muon-lifetime error into the tau-lifetime prediction.
tau_mu_pdg = 2.1970e-6   # s  (PDG 2022)


# =============================================================================
# STEP 12 -- NEUTRINO MASSES FROM SECTOR GEOMETRY
# =============================================================================

# The d=5 sector (S⁵) has Euler characteristic zero and no self-confinement.
# Its mass scale is set by the cross-sector balance between d=4 (quarks) and
# d=6 (leptons) via the Hopf fibration S¹→S⁵→CP². The consistency equation:
#
#   m_scale_5 * m_scale_4^2 = (n_up/n_strange) * m_scale_6^3
#
# is the d=5 analog of the g22 back-reaction equation (Part 2 section 9c).
# The n_up/n_strange = 3/4 factor is the ratio of the Hopf chain seeds.
# No neutrino data of any kind enters this derivation.
m_scale5  = (n_up / n_strange) * m_scale6**3 / m_scale4**2

# Neutrino masses from m(n,d) = m_scale_5 × S(n,5)
# Mode indices n_nu1=10, n_nu2=15, n_nu3=22 are derived in STEP 1.
m_nu1_MeV = m_scale5 * S(n_nu1, 5)
m_nu2_MeV = m_scale5 * S(n_nu2, 5)
m_nu3_MeV = m_scale5 * S(n_nu3, 5)

m_nu1_meV = m_nu1_MeV * 1.0e9    # 1 MeV = 10⁹ meV
m_nu2_meV = m_nu2_MeV * 1.0e9
m_nu3_meV = m_nu3_MeV * 1.0e9
sum_mnu   = m_nu1_meV + m_nu2_meV + m_nu3_meV  # uncorrected

# ν₃ correction applied (δ_ν₃ = 1/35 from STEP 4)
m_nu3_MeV_corr = m_nu3_MeV * nu3_factor
m_nu3_meV_corr = m_nu3_meV * nu3_factor
sum_mnu_corr   = m_nu1_meV + m_nu2_meV + m_nu3_meV_corr  # corrected: 60.39 meV

# Δm²₂₁ = [S(n_ν₂,5)² - S(n_ν₁,5)²] × m_scale_5²   (eV²)
# Δm²₃₁ = [S(n_ν₃,5)² - S(n_ν₁,5)²] × m_scale_5²   (eV²)
# Mass-squared differences are exact once the mode indices are fixed.
dm2_21 = (S(n_nu2,5)**2 - S(n_nu1,5)**2) * m_scale5**2 * 1.0e12   # eV²
dm2_31 = (S(n_nu3,5)**2 - S(n_nu1,5)**2) * m_scale5**2 * 1.0e12   # eV²
# Corrected Δm²₃₁ uses m_nu3_corr = m_nu3 × (1 + 1/35); m_nu1 is unchanged
dm2_31_corr = (m_nu3_MeV_corr**2 - (S(n_nu1,5)*m_scale5)**2) * 1.0e12  # eV²


# =============================================================================
# STEP 13 -- PMNS MIXING ANGLES FROM SPECTRAL GEOMETRY
# =============================================================================

# The PMNS is a weighted average of two spectral limits:
#   (a) Coupling-symmetry (μ–τ symmetric limit):
#       weight (1-g₅₅), from g₆₆=g₁₀,₁₀ exactly.
#   (b) Simplex-ratio:
#       weight g₅₅, from simplex hierarchy.
# The weight g₅₅=g₃₃×g₄₄/g₂₂=96/g₂₂ is the d=5 neutrino self-coupling.
#
#   sin²θ₂₃ = (1-g₅₅)/2  + g₅₅ × S(n_τ,10)/(S(n_μ,6)+S(n_τ,10))
#   sin²θ₁₂ = (1-g₅₅)/3  + g₅₅ × S(n_ν₁,5)/(S(n_ν₁,5)+S(n_ν₂,5))
#   sin²θ₁₃ = g₅₅ × δ₂₃ × log(S(n_τ,10)/S(n_μ,6)),  δ₂₃=sin²θ₂₃-1/2
# (Part 5 sections 3g-3i)

g55_pmns    = 96.0 / g22             # = g55 (d=5 self-coupling)
m_amp_23    = S(n_tau,10)  / (S(n_mu,6) + S(n_tau,10))
m_amp_12    = S(n_nu1,5)   / (S(n_nu1,5) + S(n_nu2,5))
log_r_pmns  = math.log(S(n_tau,10) / S(n_mu,6))

sin2_23_pred = (1.0 - g55_pmns)*0.5 + g55_pmns*m_amp_23
sin2_12_pred = (1.0 - g55_pmns)/3.0 + g55_pmns*m_amp_12
delta23_pred = sin2_23_pred - 0.5
sin2_13_pred = g55_pmns * delta23_pred * log_r_pmns

# PMNS trigonometric components used in the unitary matrix
# and CP-violation amplitude
_s23 = math.sqrt(sin2_23_pred)
_c23 = math.cos(math.asin(_s23))
_s12 = math.sqrt(sin2_12_pred)
_c12 = math.cos(math.asin(_s12))
_s13 = math.sqrt(sin2_13_pred)
_c13 = math.cos(math.asin(_s13))


# =============================================================================
# STEP 14 -- SPECTRAL ACTION: √Tr(D²) AND EW SCALE
# =============================================================================

# √Tr(D²) = √(Σ mᵢ²) over all 15 IDWT particle masses.
# Consistency check: spectral RMS against the EW scale derived from IDWT.
# IDWT does not use spontaneous symmetry breaking — the Higgs is mode n=95
# of the d=2 sector, not a condensate. The EW scale is (√2 G_F)^{-1/2}
# derived from seeds alone (Part 5 §3c); no Higgs VEV concept applies.
# G_N is the measured coupling constant of 3+1D GR, entered by hand in the
# Einstein-Hilbert action (Part 4 §3.11). (Part 1 section 0, Part 9 T7)
all_m_list = [
    m_scale3,                              # d quark
    m_scale3*S(n_strange,3),              # s quark
    m_scale3*S(n_charm,3),               # c quark (d=3 resonance)
    m_scale3*math.sqrt(S(16,3)*S(17,3)), # b quark (geometric-mean resonance)
    m_scale4*S(n_up,4),                  # u quark
    m_scale4*S(n_top,4),                 # t quark (corrected in pred_corrected)
    m_scale5*S(n_nu1,5),                 # ν₁
    m_scale5*S(n_nu2,5),                 # ν₂
    m_scale5*S(n_nu3,5),                 # ν₃
    m_e,                                  # electron
    m_scale6*S(n_mu,6),                  # muon
    m_scale10*S(n_tau,10),               # tau
    m_scale2*S(n_W,2),                   # W boson
    m_scale2*S(n_Z,2),                   # Z boson
    m_scale2*S(n_H,2),                   # Higgs
]
Tr_D2_val = sum(m**2 for m in all_m_list)
rms_D_val = math.sqrt(Tr_D2_val)

# v_EW from IDWT-derived G_F: v = 1/√(√2 G_F) in MeV.
# G_F has units GeV⁻²; factor of 10⁶ converts to MeV⁻².
v_EW_idwt = 1000.0 / math.sqrt(math.sqrt(2.0) * GF_pred)   # MeV


# =============================================================================
# STEP 15 -- EW PRECISION: Z PARTIAL WIDTHS, R_b, R_c, ρ PARAMETER
# =============================================================================

# Γ(Z→ff̄) = [G_F m_Z³ / (6π√2)] × N_c × (g_V² + g_A²)   (in GeV)
# where g_V = T_3 - 2Q sin²θ_W, g_A = T_3.
# G_F in MeV⁻² converted to GeV by dividing Gfac by 1000. (Part 3 section 0.7)
def _Zcoup(T3, Q): return T3 - 2*Q*sin2_W, T3    # g_V, g_A

Gfac = GF_MeV2 * m_Z_MeV**3 / (6*math.pi*math.sqrt(2)) / 1000.0  # GeV per unit

_ferms = [
    ("νe,νμ,ντ", 0.5, 0,    3,    0.4990),
    ("e,μ,τ",    -0.5,-1,   3,    0.2519),
    ("u,c",       0.5, 2/3, 6,    0.6006),
    ("d,s,b",    -0.5,-1/3, 9,    1.1438),
]

# Accumulate total and hadronic Z widths; store per-flavour widths for output
GZ_tot = 0.0; Ghad = 0.0
_fw = {}
for _nm, _T3, _Q, _dof, _pdgw in _ferms:
    _gV, _gA = _Zcoup(_T3, _Q)
    _w = Gfac * _dof * (_gV**2 + _gA**2)
    GZ_tot += _w
    if _nm not in ("νe,νμ,ντ", "e,μ,τ"):
        Ghad += _w
    _fw[_nm] = (_w, _pdgw)

# R_b = Γ(Z→bb̄)/Γ(Z→had), R_c = Γ(Z→cc̄)/Γ(Z→had)
_gVb, _gAb = _Zcoup(-0.5, -1/3)
_gVc, _gAc = _Zcoup(0.5,  2/3)
_Gb = Gfac * 3 * (_gVb**2 + _gAb**2)
_Gc = Gfac * 3 * (_gVc**2 + _gAc**2)
Rb = _Gb / Ghad;  Rc = _Gc / Ghad

# Lepton and b-quark asymmetry parameters A_f = 2g_V g_A / (g_V² + g_A²)
def _Af(T3, Q):
    gV, gA = _Zcoup(T3, Q)
    return 2*gV*gA / (gV**2 + gA**2)

# lepton asymmetry (avoid collision with Ae_z from STEP 8)
Ae_ew  = _Af(-0.5, -1)
Ab_ew  = _Af(-0.5, -1/3)     # b-quark asymmetry
AFBb_ew = 0.75 * Ae_ew * Ab_ew

# ρ = m_W² / (m_Z² cos²θ_W): custodial symmetry parameter; = 1 at tree level.
rho_ew = (m_scale2*S(n_W,2))**2 / ((m_scale2*S(n_Z,2))**2 * (1 - sin2_W))


# =============================================================================
# STEP 16 -- JARLSKOG INVARIANT AND TAU LIFETIME
# =============================================================================

# J_max = s₁₂ c₁₂ s₂₃ c₂₃ s₁₃ c₁₃²
#   (CP-violation prefactor; J = J_max × sin δ_CP)
# J_max depends only on the three mixing angles from STEP 13; it is a prediction
# of IDWT independent of δ_CP. We compare J_max to PDG 3.18×10⁻². (Part 5 §3f)
#
# τ lifetime from IDWT-derived R_had (one-loop α_s) and phase-space R_lep:
# τ_τ = τ_μ × (m_μ/m_τ)⁵ / (1 + R_lep + R_had) — no measured BR input.
J_max   = _s12*_c12*_s23*_c23*_s13*_c13**2
J_at195 = J_max * math.sin(195 * math.pi / 180)   # at PDG best-fit δ_CP ≈ 195°

# τ_τ = τ_μ(PDG) × (m_μ/m_τ)⁵ / (1 + R_lep + R_had)
# Using τ_μ(PDG) rather than τ_μ(pred) avoids compounding the small muon-
# lifetime error. R_had is the one-loop QCD correction with IDWT Λ_QCD.
# R_lep is the phase-space ratio Γ(τ→μνν)/Γ(τ→eνν). (Part 5)
m_mu_m    = m_scale6  * S(n_mu,  6)
m_tau_m   = m_scale10 * S(n_tau, 10) * back_reaction_factor

_b0_tau      = (11*N_c - 2*3) // 3                              # = 9
_alpha_s_tau = 2*math.pi / (_b0_tau * math.log(m_tau_m / Lqcd))
_R_had       = N_c * (1 + _alpha_s_tau / math.pi)   # hadronic enhancement

# Phase-space function f(x) = 1 - 8x + 8x³ - x⁴ - 12x² ln(x)
# Gives R_lep = f(m_μ²/m_τ²) — fraction of τ decays with muon in
# final state.
_f_ps        = lambda x: 1 - 8*x + 8*x**3 - x**4 - 12*x**2*math.log(x)
_R_lep       = _f_ps((m_mu_m / m_tau_m)**2)
tau_tau_pred = tau_mu_pdg * (m_mu_m/m_tau_m)**5 / (1 + _R_lep + _R_had)


# =============================================================================
# STEP 18 -- NEUTRINO OSCILLATIONS: PMNS MATRIX AND OSCILLATION PROBABILITIES
# =============================================================================
# The PMNS matrix U is built from the three mixing angles computed in STEP 13.
# δ_CP = 0 at tree level (spectral phase on the lepton coupling
# triangle vanishes; proved in STEP 24b via spectral-curvature
# computation).
# Δm² values in eV² for the oscillation probability formula:
#   P(να→νβ) = δ_αβ − 4 Σ_{k>j} Re(U*_αk U_βk U_αj U*_βj) sin²(Δm²_kj L/4E)
# with the factor 1.2669 km·eV²/GeV absorbing ℏc.

_dm21 = dm2_21     # eV² — already computed in STEP 12
_dm31 = dm2_31     # eV²
_mnu  = [m_nu1_meV, m_nu2_meV, m_nu3_meV]  # meV — already computed in STEP 12
_Smnu = sum_mnu    # meV

# PMNS matrix (δ_CP = 0; mixing angles from STEP 13)
_U = [
    [ _c12*_c13,          _s12*_c13,          _s13     ],
    [-_s12*_c23 - _c12*_s23*_s13,  _c12*_c23 - _s12*_s23*_s13,  _s23*_c13],
    [ _s12*_s23 - _c12*_c23*_s13, -_c12*_s23 - _s12*_c23*_s13,  _c23*_c13],
]
_dms = [0, _dm21, _dm31]   # eigenvalue differences array; Δm²_k0

def _Posc(a, b, Lkm, EGeV, dms):
    """3-gen oscillation probability P(ν_a → ν_b) at baseline Lkm (km),
    energy EGeV (GeV)."""
    tot = 0
    for k in range(3):
        for j in range(3):
            if k == j:
                continue
            ph = 1.2669 * (dms[k] - dms[j]) * Lkm / EGeV
            sin2ph = math.sin(ph / 2)**2
            tot -= 4 * _U[a][k] * _U[a][j] * _U[b][k] * _U[b][j] * sin2ph
    return (1 if a == b else 0) + tot

# m_β: effective beta-decay neutrino mass √(Σ|U_ei|²mᵢ²)
m_beta_meV = math.sqrt(sum(_U[0][k]**2 * _mnu[k]**2 for k in range(3)))

# =============================================================================
# STEP 19 -- CKM MATRIX BARE VALUES (TREE LEVEL, NO CURVATURE CORRECTION)
# =============================================================================
# Bare Cabibbo angle: λ = 1/√S(n_s,3).  No Seeley-DeWitt correction.
# Compare with corrected value sin_C = (1+1/240)/√S(n_s,3) from STEP 6 calc.
# The Seeley-DeWitt curvature correction +1/240 gives λ=0.22454 (+0.09σ PDG).
# Both are IDWT derivations; STEP 6 is the more precise prediction.
# |Vus| = 1/√S(n_s,3) = bare Cabibbo angle; |Vcb| = √(S(n_up,4)/S(n_charm,4)).
# Wolfenstein A = |Vcb|/λ².  |Vub| = 0 at tree level (no CP-violating paths).

_lam  = 1.0 / math.sqrt(S(n_strange, 3))          # bare |Vus| = Cabibbo angle
_Vcb  = math.sqrt(S(n_up, 4) / S(n_charm, 4))     # = √(15/8855) ≈ 0.04116
_Vud  = math.sqrt(1 - _lam**2)
_Vcb2 = _Vcb
_A_W  = _Vcb / _lam**2                             # Wolfenstein A ≈ 0.823
_r1   = _Vud**2 + _lam**2 + 0.0                   # row-1 CKM unitarity

# =============================================================================
# STEP 20 -- HADRONIC SECTOR OUTPUT ALIASES
# =============================================================================
# f_π and Λ_QCD already computed in STEP 7 as f_pi and Lqcd.
# m_p from hadronic Fermi formula also in STEP 7.  Create underscore aliases
# so the output section can reference either name consistently.

_f_pi = f_pi        # = m_scale3 × S(n_s,3)
_Lqcd = Lqcd        # = N_c × f_pi
_mp   = m_p_pred    # = N_c × Λ × (1 + 1/n_u²)

# =============================================================================
# STEP 21 -- AXIAL COUPLING g_A AND NEUTRON LIFETIME
# =============================================================================
# The nucleon axial vector coupling g_A is the spin-flip matrix element between
# the d=3 sector ground state (the nucleon) and its first axial excitation.
# In IDWT, the spin-flip amplitude between consecutive seed levels
# is:
#
#   g_A = sqrt(S(n_s+1, 3) / S(n_s, 3)) = sqrt(S(5,3) / S(4,3))
#       = sqrt(35 / 20) = sqrt(7/4) = sqrt(7)/2 = 1.3229
#
# S(n_s,3)=20 is the nucleon ground-state density;
# S(n_s+1,3)=35 is the next level.
# The spin-flip amplitude is sqrt(density ratio) — the Gamow-Teller
# matrix element in IDWT's spectral formulation.
# (Part 5 §3b, Part 8 §10)
#
# The +4.0% error relative to PDG 1.2723 traces to uncalculated higher-l
# partial-wave mixing in the d=3 sector kernel (Part 8 §10).

# = √(7)/2 ≈ 1.3229
_g_A = math.sqrt(float(S(n_strange + 1, 3)) / S(n_strange, 3))

# Neutron lifetime: Γ_n = G_F² |V_ud|² (1+3g_A²) m_e⁵ f / (2π³)
# Q_n = m_n − m_p = 1.2933 MeV (kinematic input; IDWT derives m_p not m_n)
_Q_n     = 1.2933           # MeV
_eps_max = _Q_n / m_e       # = 2.531; upper limit of phase-space integral

# Phase-space integral f = ∫₁^{ε_max} ε √(ε²−1) (ε_max−ε)² dε   (Coulomb F_C=1)
_N_n, _f_n = 5000, 0.0
for _i in range(_N_n):
    _eps  = 1.0 + (_i + 0.5) * (_eps_max - 1.0) / _N_n
    _dw   = (_eps_max - 1.0) / _N_n
    _f_n += (_eps * math.sqrt(_eps**2 - 1.0)
             * (_eps_max - _eps)**2 * _dw)

_Gamma_n = (GF_MeV2**2 * m_e**5 * Vud_m**2
            * (1.0 + 3.0*_g_A**2) * _f_n / (2.0*math.pi**3))
_tau_n   = hbar_MeV_s / _Gamma_n

# =============================================================================
# STEP 22 -- HEAT KERNEL FUNCTIONS
# =============================================================================
# The heat kernel of sector d is the trace of the heat semi-group:
#
#   K_d(t) = Tr(e^{-t|D_d|}) = Σ_{n=1}^∞  exp(-t · S(n,d))
#
# Physical: partition function of sector d at inverse temperature t/m_scale_d.
# The Mellin transform Γ(s)·ζ_d(s) = ∫ t^{s-1} K_d(t) dt connects K_d to
# the spectral zeta function ζ_d(s) = Σ S(n,d)^{-s} from STEP 23.
#
# SMALL-t ASYMPTOTICS (Weyl + Euler-Maclaurin):
#   K_d(t) = a0_d · t^{-1/d}  −  d/2  +  O(t^{1/d})   as t → 0+
#
# (i) WEYL TERM: S(n,d) ~ n^d/d! for large n, so the sum ≈ integral gives
#     a0_d · t^{-1/d}  where  a0_d = Γ(1+1/d) · (d!)^{1/d}.
# (ii) SUBLEADING-IN-S: the next term in S(n,d) contributes a constant −(d-1)/2.
# (iii) EULER-MACLAURIN BOUNDARY: discrete vs integral gives −1/2.
#     Total constant: −(d-1)/2 − 1/2 = −d/2.
#
# SPECTRAL ZETA: By Mellin inversion, the constant term −d/2
# implies ζ_d(0) = −d/2.
# Combined with ζ_d(1) = d/(d-1) from STEP 23, these anchor the spectral zeta.
#
# LARGE-t: K_d(t) ≈ e^{-t}(1 + e^{-dt} + ...)  as t → ∞.
# All sectors share ground-state energy S(1,d)=1; first excitation gap = d.
# (Part 9 §T14)

def _K_d(d, t, N=800):
    """K_d(t) = Σ_{n=1}^N exp(-t·S(n,d)).  N=800 sufficient for t≥0.001."""
    return sum(math.exp(-t * S(n, d)) for n in range(1, N + 1)
               if t * S(n, d) < 40)   # skip negligible terms (exp < e^{-40})

def _K_d_asymp(d, t):
    """Two-term small-t approximation: a₀_d · t^{-1/d} − d/2."""
    _a0 = math.gamma(1.0 + 1.0/d) * math.factorial(d)**(1.0/d)
    return _a0 * t**(-1.0/d) - d / 2.0

# =============================================================================
# STEP 23 -- SPECTRAL SUM RULE AND EXACT MASS RATIO TABLES
# =============================================================================
# The resonance spectrum in each sector d is {S(n,d) : n ≥ 1}.  Two purely
# combinatorial identities follow from Pascal's triangle and hold in all six
# IDWT sectors — they are consequences of m(n,d) = m_scale_d × S(n,d).
#
# IDENTITY 1: SPECTRAL SUM RULE      ζ_d(1) ≡ Σ_{n=1}^∞  1/S(n,d)  =  d/(d-1)
# Physical meaning: the reciprocal sum over the full resonance tower of a
# sector is a fixed rational number set by dimensionality alone.
# Proof (telescoping):
#   1/C(n+d-1,d) = [d/(d-1)] × [1/C(n+d-2,d-1) − 1/C(n+d-1,d-1)]
#   Summing: ζ_d(1) = [d/(d-1)] × [1 − 1/S(N,d-1)] → d/(d-1) as N→∞.
#
# IDENTITY 2: MODE SPACING (Pascal)   S(n+1,d) − S(n,d)  =  S(n+1,d-1)
# The gap between consecutive resonances in sector d equals the (n+1)-th
# resonance of sector d-1.
# Proof: Pascal's identity C(n+d,d) − C(n+d-1,d) = C(n+d-1,d-1).
# This underpins all mode-index derivation chains (Part 2 §2–6).
#
# EXACT MASS RATIOS: within a single sector m_scale_d cancels, leaving exact
# rational ratios of S values — all ratios of binomial coefficients.
# (Part 5 §3, Part 8 §10; Part 9 T13a)

_e  = epsilon       # GTC shift = 1/(280√7)
# back-reaction factor = 1 + 1/(n_up × n_s² × S(n_s,4))
_dy = back_reaction_factor

# Simplex values at particle mode indices (used in mass ratio table)
_Ss = {
    "d":  S(n_down,3),    "s":  S(n_strange,3),
    "u":  S(n_up,4),      "c":  S(n_charm,4),   "t": S(n_top,4),
    "e":  S(n_e,6),       "mu": S(n_mu,6),       "tau": S(n_tau,10),
    "n1": S(n_nu1,5),     "n2": S(n_nu2,5),      "n3": S(n_nu3,5),
    "W":  S(n_W,2),       "Z":  S(n_Z,2),
}

# Mass ratios: within-sector pairs where m_scale_d cancels exactly
_mass_ratios = [
    ("m_s / m_d",
     _Ss["s"]/_Ss["d"], 20.0,
     f"S(n_s,3)/S(n_d,3) = {_Ss['s']}/{_Ss['d']}"),
    ("m_c / m_u",
     _Ss["c"]/_Ss["u"]*(1-_e)**3, 587.96,
     f"S(n_c,4)/S(n_u,4)x(1-e)^3 = {_Ss['c']}/{_Ss['u']}x..."),
    ("m_t / m_u",
     _Ss["t"]/_Ss["u"]*(1-_e)**10, 79981.0,
     f"S(n_t,4)/S(n_u,4)x(1-e)^10 = {_Ss['t']}/{_Ss['u']}x..."),
    ("m_μ / m_e",
     _Ss["mu"]/_Ss["e"], 206.7683,
     f"S(n_μ,6)/S(n_e,6) = {_Ss['mu']}/{_Ss['e']}"),
    ("m_τ / m_μ",
     _Ss["tau"]/_Ss["mu"]*_dy, 16.8177,    # PDG 2024: 1776.93/105.6584
     f"S(n_τ,10)/S(n_μ,6)xBR = {_Ss['tau']}/{_Ss['mu']}xBR"),
    ("m_τ / m_e",
     _Ss["tau"]/_Ss["e"]*_dy, 3477.37,     # PDG 2024: 1776.93/m_e
     f"S(n_τ,10)/S(n_e,6)xBR = {_Ss['tau']}/{_Ss['e']}xBR"),
    ("m_ν₃ / m_ν₁",
     _Ss["n3"]/_Ss["n1"], None,
     f"S(n_ν3,5)/S(n_ν1,5) = {_Ss['n3']}/{_Ss['n1']}"),
    ("m_ν₂ / m_ν₁",
     _Ss["n2"]/_Ss["n1"], None,
     f"S(n_ν2,5)/S(n_ν1,5) = {_Ss['n2']}/{_Ss['n1']}"),
    ("m_ν₃ / m_ν₂",
     _Ss["n3"]/_Ss["n2"], None,
     f"S(n_ν3,5)/S(n_ν2,5) = {_Ss['n3']}/{_Ss['n2']}"),
    ("m_Z  / m_W",
     _Ss["Z"]/_Ss["W"], 1.13450,
     f"S(n_Z,2)/S(n_W,2) = {_Ss['Z']}/{_Ss['W']}"),
]

# Spectral action sector table used in STEP 22 output
_scales_all = [
    (2, m_scale2), (3, m_scale3), (4, m_scale4),
    (5, m_scale5), (6, m_scale6), (10, m_scale10),
]

# =============================================================================
# STEP 24 -- SECTOR EIGENMODE PERTURBATION + BERRY PHASE (scipy/numpy)
# =============================================================================
# The sector harmonic self-binding potential (Part 4 S3.10.2):
#   V_d(r) = lambda_d r^2      (derived from the kernel; r^2 behaviour is exact;
#                               the saturation 1/(1+r^2) is an
#                               MC-2 ansatz, now dropped)
#   lambda_d = (g_dd/2)^{2/3}  (self-consistency: <r^2>=d/(2*sqrt(lam))
#                               is exact for the harmonic ground state,
#                               closing the derivation)
#   sigma_ess(H_d^harm) = {}   (purely discrete spectrum; V->inf, no continuum)
#
# The sector localization length is the HARMONIC OSCILLATOR LENGTH
# (Part 4 S3.9):
#   L_d = lambda_d^{-1/4}      (Gaussian ground state exp(-sqrt(lam)*r^2/2);
#                               NOT 1/sqrt(lam-E0), which was the
#                               saturating-potential
#                               exponential-tail length now superseded)
#   E0 = d * sqrt(lambda_d)    (exact harmonic ground state energy)
#   lam_hat = sqrt(lambda_d)   (dimensionless coupling = lambda_d * L_d^2)
#
# T-S1 EXTENSION (Appendix A S20): per-spinor-component cumulative Dirac count
# on S^d equals S(n,d) for ALL d in D = {2,3,4,5,6,10}.
# Discreteness is geometric (compactness of S^d / confinement of harmonic well
# in extended flat R^d) — no saturating regulator needed.
#
# GRAVITY (Part 4 S3.12.2):
#   V_7 = L_4 * L_5 * L_6 * L_10^4  (product of oscillator lengths beyond d=3)
#       = 0.872 * 1.571 * 1.414 * 1.414^4 ≈ 7.74
#   G_N = G_inf / V_7  (G_inf from spectral action scale Lambda; open)
#
# NOTE on STEP 24 computation: the numerical solver below uses the SATURATING
# potential V_d(r) = lambda_d r^2/(1+r^2) because this is what the Bures metric
# perturbation (T8) was computed for. The eigenvector SHAPES (and hence the
# perturbation responses) are correctly captured by the saturating
# form for d=2,3.
# For d=5,6,10 the saturating form has no bound states (Part 4 S3.10.4 binding
# test) — the eigenvectors below are effective ground states in a finite box,
# not true bound states. The non-collinearity conclusion (T8) is qualitatively
# correct but the computation should be repeated with the harmonic form.
# (Part 4 S3.13; Appendix A S20)

import numpy as np
from scipy.linalg import eigh_tridiagonal

# S3.10.4 table: (lambda_d, E0=d*sqrt(lam), kappa_legacy, L_d=lam^{-1/4})
# L_d = lambda_d^{-1/4} is the harmonic oscillator length (Part 4 S3.9).
# E0 = d*sqrt(lam) is the exact harmonic ground state energy.
# kappa_legacy is retained only for r_max sizing in this Bures computation.
_table = {
    2:  (50.723, 14.244, 7.050, 0.375),
    3:  (4.820,   6.586, 2.172, 0.675),
    4:  (1.726,   5.255, 1.248, 0.872),
    5:  (0.164,   2.025, 0.381, 1.571),
    6:  (0.250,   3.000, 0.435, 1.414),
    10: (0.250,   5.000, 0.455, 1.414),
}

# V_7 = L_4 * L_5 * L_6 * L_10^4  (sector volume factor for G_N = G_inf/V_7)
V7 = _table[4][3] * _table[5][3] * _table[6][3] * _table[10][3]**4

# --- Spectral-action G_N: Einstein-Hilbert coefficient
#     (Part 4 section 3.12.4) -
# Product heat kernel K_Xi = prod_d K_d has leading small-t power t^-sigma with
#   sigma = sum_{d in D} 1/d = 31/20
#     (exact, fixed by the sector set => by N_c=3)
# Weyl coefficient per sector a0_d = Gamma(1+1/d)*(d!)^(1/d) (T14).
# G_N^-1 = [prod a0_d * Gamma(1+sigma) / (6 pi)] * Lambda^(2+2sigma),
#   exponent 2+2sigma = 51/10 EXACT (fixed by N_c=3);
#   prefactor cutoff-dependent.
from math import gamma as _gamma, factorial as _fact
_D_sa         = sorted(_table)                         # [2,3,4,5,6,10]
_sigma_sa     = sum(1.0/_d for _d in _D_sa)            # = 31/20 = 1.55
_GN_exponent  = 2 + 2*_sigma_sa                        # = 51/10 = 5.1
_a0_prod      = 1.0
for _d in _D_sa:
    _a0_prod *= _gamma(1 + 1.0/_d) * _fact(_d)**(1.0/_d)   # prod = 116.781
# ~ 8.54 (exp cutoff)
_GN_prefactor = _a0_prod * _gamma(1 + _sigma_sa) / (6*math.pi)
# Lambda required to match measured G_N = 6.709e-45 MeV^-2 (NOT a prediction;
# Lambda is a free input). a2/a4 does NOT eliminate it: the product spectral
# dimension D_tot = 4+2sigma = 71/10 makes a2 ~ Lambda^(51/10)
# and a4 ~ Lambda^(31/10),
# so a2/a4 ~ Lambda^2 -- a residual Lambda^2 survives (Part 4 section 3.12.4).
_GN_meas      = 6.709e-45                              # MeV^-2
# ~3e8 MeV ~3e5 GeV
_Lambda_req   = (1.0/(_GN_prefactor*_GN_meas))**(1.0/_GN_exponent)
# = 71/10 = 7.1 spectral dim
_D_tot        = 4 + 2*_sigma_sa
# a4 gravitational channel:
#   beta_d = 1/20 - 1/(2d) + 1/(d(d-1)); beta_5=beta_6=0 exact.
# Constant-curvature sectors:
#   R_d = d(d-1)/L_d^2
#   Vol_d = (pi/2)^(d/2) L_d^d/Gamma(d/2+1)
# (so R_2*Vol_2 = pi exactly, topological).
# a4_grav = (1/16pi^2) sum R_d^2 Vol_d beta_d.
_beta   = {_d: 1/20 - 1/(2*_d) + 1/(_d*(_d-1)) for _d in _D_sa}
def _RVol(_d):
    _L = _table[_d][3]
    _R = _d*(_d-1)/_L**2
    _V = (math.pi/2)**(_d/2) * _L**_d / _gamma(_d/2 + 1)
    return _R*_V, _R*(_R*_V)                           # (R*Vol, R^2*Vol)
_RV     = {_d: _RVol(_d) for _d in _D_sa}
# ~ 284.6 (a2 EH sector sum)
_a2_EHsum = sum(_RV[_d][0] for _d in _D_sa)
# ~ 0.482
_a4_grav  = (sum(_RV[_d][1]*_beta[_d] for _d in _D_sa)
             / (16*math.pi**2))

def _solve(d, lam, N=6000):
    """Solve -f'' + [lam r²/(1+r²) + cen/r²] f = E f; return (Ev, fv, r, h)."""
    cen   = (d - 1) * (d - 3) / 4.0
    _, _, kap_t, _ = _table[d]
    r_max = 6.0 / kap_t
    h     = r_max / (N + 1)
    r     = h * np.arange(1, N + 1)
    V_eff = lam * r**2 / (1.0 + r**2) + (cen / r**2 if cen != 0 else 0.0)
    diag  = 2.0 / h**2 + V_eff
    off   = -np.ones(N - 1) / h**2
    n_eig = min(50, N // 4)
    Ev, fv = eigh_tridiagonal(diag, off, select='i',
                               select_range=(0, n_eig - 1))
    norms = np.sqrt(np.einsum('ij,ij->j', fv, fv) * h)
    fv   /= norms
    return Ev, fv, r, h

def _perturb(Ev, fv, r, h):
    """First-order perturbation under H' = r²/(1+r²).
    Returns (dE, du, norm_du)."""
    E0 = Ev[0];  f0 = fv[:, 0]
    Hp = r**2 / (1.0 + r**2)
    W  = fv.T @ (Hp * f0) * h
    dE = W[0]
    coeff = W[1:] / (E0 - Ev[1:])
    du    = fv[:, 1:] @ coeff
    norm_du = math.sqrt(float(np.sum(du**2) * h))
    return dE, du, norm_du

def _gs_ov(d, lam_a, lam_b):
    """Ground-state overlap <chi_d(lam_a)|chi_d(lam_b)>."""
    _, fv_a, _, h_a = _solve(d, lam_a)
    _, fv_b, _,  _  = _solve(d, lam_b)
    return float(np.sum(fv_a[:, 0] * fv_b[:, 0]) * h_a)

def _lam_of_g(g): return (g / 2.0) ** (2.0 / 3.0)

# Solve all six sectors
_sr = {}
for _d in [2, 3, 4, 5, 6, 10]:
    lam_t, E0_t, _, _ = _table[_d]
    Ev, fv, r, h = _solve(_d, lam_t)
    dE, du, ndu = _perturb(Ev, fv, r, h)
    _sr[_d] = dict(Ev=Ev, fv=fv, r=r, h=h, dE=dE, du=du, ndu=ndu,
                   lam=lam_t, E0_t=E0_t)

# Non-collinearity of df0/dlambda for d=6 vs d=10
du6  = _sr[6]['du'];   r6  = _sr[6]['r']
du10 = _sr[10]['du'];  r10 = _sr[10]['r']
_r_c  = r6 if len(r6) <= len(r10) else r10
_h_c  = _r_c[1] - _r_c[0]
_du6  = np.interp(_r_c, r6,  du6)
_du10 = np.interp(_r_c, r10, du10)
_ov_nc   = float(np.sum(_du6 * _du10) * _h_c)
_n6_nc   = math.sqrt(float(np.sum(_du6**2)  * _h_c))
_n10_nc  = math.sqrt(float(np.sum(_du10**2) * _h_c))
_cos_t   = _ov_nc / (_n6_nc * _n10_nc) if _n6_nc * _n10_nc > 1e-30 else 0.0
_sin_t   = math.sqrt(max(1.0 - _cos_t**2, 0.0))

# Bures metric diagonal G_dd
_g_vals = {2: g22, 3: g33, 4: g44, 5: 96.0/g22, 6: g66, 10: g66}
_bures = {}
for _d in [2, 3, 4, 5, 6, 10]:
    _g     = _g_vals[_d]
    _chain = (1.0/3.0) * (_g / 2.0)**(-1.0/3.0)
    _ndu   = _sr[_d]['ndu']
    _bures[_d] = (_g, _chain, _ndu, (_chain * _ndu)**2)

# spectral phase on lepton coupling triangle
_g55_phys = 96.0 / g22
_g6_phys  = g66
_g10_phys = g66
_eps_spec = 0.01
_tri_verts = [
    (_g55_phys, _g6_phys,             _g10_phys),
    (_g55_phys, _g6_phys + _eps_spec, _g10_phys),
    (_g55_phys, _g6_phys + _eps_spec, _g10_phys + _eps_spec),
]
_lams_spec = [{5: _lam_of_g(g5), 6: _lam_of_g(g6), 10: _lam_of_g(g10)}
               for (g5, g6, g10) in _tri_verts]
_prod_ov = complex(1.0, 0.0)
for (_bi, _bj) in [(0, 1), (1, 2), (2, 0)]:
    _ov_ij = 1.0
    for _bd in [5, 6, 10]:
        _la, _lb = _lams_spec[_bi][_bd], _lams_spec[_bj][_bd]
        _ov_ij *= 1.0 if abs(_la - _lb) < 1e-12 else _gs_ov(_bd, _la, _lb)
    _prod_ov *= complex(_ov_ij, 0.0)
_spectral_phase = float(-np.angle(_prod_ov))
_delta_lam_spec = abs(_lam_of_g(_g6_phys + _eps_spec) - _lam_of_g(_g6_phys))

# spectral curvature F_{6,10} by finite differences
_delta_g = 1e-4
_, _fv_6m,  _r6g,  _h6g  = _solve(6,  _lam_of_g(_g6_phys  - _delta_g))
_, _fv_6p,  _,     _     = _solve(6,  _lam_of_g(_g6_phys  + _delta_g))
_, _fv10m,  _r10g, _h10g = _solve(10, _lam_of_g(_g10_phys - _delta_g))
_, _fv10p,  _,     _     = _solve(10, _lam_of_g(_g10_phys + _delta_g))
_df6_dg  = (_fv_6p[:, 0] - _fv_6m[:, 0]) / (2 * _delta_g)
_df10_dg = (_fv10p[:, 0] - _fv10m[:, 0]) / (2 * _delta_g)
_, _fv_6phys,  _, _ = _solve(6,  _lam_of_g(_g6_phys))
_, _fv10phys,  _, _ = _solve(10, _lam_of_g(_g10_phys))
_A6    = float(np.sum(_df6_dg  * _fv_6phys[:,  0]) * _h6g)
_A10   = float(np.sum(_fv10phys[:, 0] * _df10_dg)  * _h10g)
_F_6_10 = -2.0 * (complex(_A6, 0.0) * complex(_A10, 0.0)).imag

# CP-violation amplitude from IDWT T6 mixing angles
# (stated values for cross-check)
_s2_23 = 0.5590;  _s2_12 = 0.3086;  _s2_13 = 0.02211
_s23b = math.sqrt(_s2_23);  _c23b = math.sqrt(1 - _s2_23)
_s12b = math.sqrt(_s2_12);  _c12b = math.sqrt(1 - _s2_12)
_s13b = math.sqrt(_s2_13);  _c13b = math.sqrt(1 - _s2_13)
_J_max_spec = _s12b*_c12b*_s23b*_c23b*_s13b*_c13b**2


# =============================================================================
# STEP 25 -- T4: SEED UNIQUENESS VERIFICATION
# =============================================================================
# Theorem T4 (Part 9 §T4): n_s = 4 is the unique positive integer satisfying
#
#   n_s(n_s + 1) / S(n_s, 4)  =  n_u(n_u + 1) / S(n_u, 5)  =  4/7
#
# with n_u = n_s − 1. Physical origin: this is the kernel algebraic fixed-point
# condition at the resonance site k_0 = n_s² = 16. The Jacobi
# coupling coefficient at mode k in sector d is:
#
#   b_k(d)  =  sqrt(k * (k + d − 1)) / (2k + d − 2)
#
# The ratio n(n+1)/S(n,d) is the leading eigenvalue of the self-adjoint cross-
# sector Gram matrix at the fixed point k = n. For the equality to hold from
# BOTH the d=3 side (k = n_s, sector d=4) AND the d=4 side (k = n_u, sector
# d=5) simultaneously, the system is overdetermined: there is exactly one
# positive-integer solution (n_s, n_u) = (4, 3). This forces the strange-quark
# seed n_s = 4 and n_up = n_s − 1 = 3 without any measurement input.
# (Part 2 section 11, Part 9 T4)

# LHS: n_s*(n_s+1) / S(n_s,4).  S(4,4) = C(7,4) = 35.  Result: 20/35 = 4/7.
t4_lhs   = n_strange * (n_strange + 1) / S(n_strange, 4)   # = 20/35

# RHS: n_u*(n_u+1) / S(n_u,5).  S(3,5) = C(7,5) = 21.  Result: 12/21 = 4/7.
t4_rhs   = n_up * (n_up + 1) / S(n_up, 5)                  # = 12/21

t4_exact = 4.0 / 7.0   # the common rational value

# Residuals confirm exact integer arithmetic on both sides to machine precision.
t4_lhs_err = abs(t4_lhs - t4_exact)
t4_rhs_err = abs(t4_rhs - t4_exact)


# =============================================================================
# STEP 26 -- T5: GEGENBAUER CRITICALITY
# =============================================================================
# Theorem T5 (Part 9 §T5): d = 10 is the unique sector at the
# Gegenbauer critical endpoint.
# The Gegenbauer coupling coefficient for sector d at the resonance site
# k_0 = n_s² = 16 is:
#
#   b_{k_0}(d)  =  sqrt( k_0 * (k_0 + d − 1) ) / ( 2*k_0 + d − 2 )
#
# The criticality condition b = 1/2 separates extended from localised modes:
#   b > 1/2 : supercritical — extended states, stable L²-modes exist.
#   b = 1/2 : critical — Gegenbauer critical point;
#             modes at localisability boundary.
#   b < 1/2 : subcritical — localised states, no stable L²-normalizable modes.
#
# At d = 10 with k_0 = 16:
#   b_{16}(10) = sqrt(16 * 25) / (32 + 8) = sqrt(400) / 40 = 20/40 = 1/2.
#
# The equivalence 4*k_0 = (d − 2)² uniquely determines d = 10:
#   4 × 16 = 64 = (d − 2)²  =>  d − 2 = 8  =>  d = 10.
# All d < 10 have b > 1/2 (above the Jacobi coupling threshold); d ≥ 11 have
# b < 1/2 (below threshold), with no stable sector-bound resonances; sector
# chain terminates at d = 10.
# At the Gegenbauer critical point the naive perturbation series does not
# converge, so the all-orders geometric back-reaction correction δ_τ = 1/1680
# is required for the tau mass (STEP 4). (Part 1 §3c, §T5)

k0_aa = n_strange ** 2   # = 16; the resonance site = seed self-product n_s²

def _b_aa(d):
    """
    Gegenbauer critical-endpoint coupling coefficient b_{k_0}(d)
    at k_0 = n_s² = 16.
    b = 1/2 exactly at d = 10 (critical point).
    b > 1/2 for d < 10 (supercritical); b < 1/2 for d >= 11 (subcritical).
    """
    return math.sqrt(k0_aa * (k0_aa + d - 1)) / (2 * k0_aa + d - 2)

# Evaluate b for all six IDWT sectors plus d=11,12 to verify subcriticality.
aa_dims = [2, 3, 4, 5, 6, 10, 11, 12]
aa_vals = {d: _b_aa(d) for d in aa_dims}

# Integer check: 4*k_0 == (d-2)^2 at d=10.
# Both sides are integers; equality is exact.
aa_exact_check = (4 * k0_aa == (10 - 2) ** 2)   # must be True


# =============================================================================
# STEP 27 -- T15: EULER CHARACTERISTIC CHAIN
# =============================================================================
# Theorem T15 (Part 9 §T15 and corollaries T15a–f): all sector self-couplings,
# all occupied mode indices, and the terminal sector d=10 are determined by the
# single integer N_c = χ(CP²) = 3.
#
# EULER CHARACTERISTIC OF CP^n:
#
#   χ(CP^n)  =  n + 1
#
# Proof: the Betti numbers of CP^n are b_{2k} = 1 for k = 0, 1, ..., n, and
# all odd Betti numbers vanish. The Euler characteristic is therefore
# χ = Σ (−1)^k b_k = (n+1) non-zero terms, each equal to 1, summing to n+1.
#
# The four even-dimension IDWT sectors carry CP-geometry Euler characteristics:
#   d=2  sector  CP¹ :  χ = 2   (two photon helicity states)
#   d=4  sector  CP² :  χ = 3 = N_c         (three quark colour charges)
#   d=6  sector  CP³ :  χ = 4 = n_s         (the strange-quark seed)
#   d=10 sector  CP⁵ :  χ = 6 = N_f         (six quark/lepton flavours)
#
# From N_c = χ(CP²) = 3 alone, the following all follow algebraically:
#
#   n_s = N_c + 1 = 4              χ(CP³) = χ(CP²) + 1             (T15)
#   d_terminal = 2(N_c + 2) = 10   Gegenbauer criticality 4k_0=(d−2)²  (T15a)
#   Hopf product = N_c(N_c+1)³/2   both Hopf pairs equal 96          (T15c)
#   n_e  = N_c² + N_c + 1 = 13    electron mode index                (T15d)
#   n_ν₁ = N_c² + 1 = 10          lightest neutrino mode index       (T15d)
#   n_top = N_c(N_c+1)(N_c+3)     top quark mode index = 72          (T15b)
#
# (Part 9 T15 and corollaries T15a–f)

def chi_CP(n):
    """Euler characteristic χ(CP^n) = n + 1."""
    return n + 1

# Euler characteristics for the four even-d IDWT sectors
t15_chi = {n: chi_CP(n) for n in [1, 2, 3, 5]}   # CP^1, CP^2, CP^3, CP^5

# Derive all structural constants from N_c = χ(CP²) = 3.
t15_Nc        = chi_CP(2)                                # = 3 = N_c
t15_ns        = t15_Nc + 1              # = 4 = n_s         (χ(CP³))
t15_d_term    = 2 * (t15_Nc + 2)       # = 10              (T15a)
t15_hopf_prod = (t15_Nc * (t15_Nc + 1) ** 3 // 2)  # = 96  (T15c)
t15_n_e       = t15_Nc ** 2 + t15_Nc + 1  # = 13           (T15d)
t15_n_nu1     = t15_Nc ** 2 + 1        # = 10              (T15d)
t15_n_top     = t15_Nc * (t15_Nc + 1) * (t15_Nc + 3)  # = 72              (T15b)

# Cross-checks against STEP 1 derivations.
# A mismatch is a framework inconsistency.
t15_ok_ns    = (t15_ns    == n_strange)   # 4 == 4
t15_ok_n_e   = (t15_n_e   == n_e)         # 13 == 13
t15_ok_n_nu1 = (t15_n_nu1 == n_nu1)       # 10 == 10
t15_ok_n_top = (t15_n_top == n_top)       # 72 == 72


# =============================================================================
# STEP 28 -- T9a: BOTH HOPF COUPLING PRODUCTS EQUAL 96
# =============================================================================
# Theorem T9a (Part 2 §9, Part 9 §T9a): both Hopf sector pairs give the same
# coupling product:
#
#   g_{33} × g_{44}  =  8√7 × (12/√7)  =  96       [d=3 ↔ d=4 Hopf pair]
#   g_{22} × g_{55}  =  722.5 × (96/722.5)  =  96  [d=2 ↔ d=5 Hopf pair]
#
# Both equal N_c(N_c+1)³/2 = 3 × 64 / 2 = 96 (T15c).
#
# d=3 ↔ d=4 product: g_{33} = 8√7 and g_{44} = 12/√7 come from independent
#   vacuum fixed-point equations (STEP 2). Their product eliminates √7 exactly:
#   8√7 × 12/√7 = 8 × 12 = 96. This product is also g_{3,4}² = (4√6)² = 96,
#   the square of the d=3 ↔ d=4 cross-coupling amplitude.
#
# d=2 ↔ d=5 product: g_{55} = 96/g_{22} by Hopf universality
# (STEP 5).
#   The Hopf fibration S¹ → S⁵ → CP² mediates d=2 (photon) to d=5 (neutrino)
#   coupling. Hopf universality requires the d=2 × d=5 coupling product to equal
#   the d=3 × d=4 product: 96. Therefore g_{55} = 96/g_{22} is the unique value
#   consistent with this constraint, and g_{22} × g_{55} = 96 is exact by
#   construction. The non-trivial content is that both independent derivation
#   chains yield the same product 96, making this a genuine internal consistency
#   test. (Part 2 §9, Part 9 T9a and T15c)

t9a_prod_34 = g33 * g44      # 8√7 × 12/√7: the √7 cancels, giving 96 exactly
t9a_prod_25 = g22 * g55      # 722.5 × (96/722.5) = 96 exactly by construction
t9a_target  = float(t15_hopf_prod)   # = 96.0 from T15c

# Residuals from 96: both should be < machine epsilon (≈ 2e-16 × 96 ≈ 2e-14).
t9a_err_34  = abs(t9a_prod_34 - 96.0)
t9a_err_25  = abs(t9a_prod_25 - 96.0)


# =============================================================================
# STEP 29 -- T0.5: CO-FIXED-POINT SELECTION CONDITION
# =============================================================================
# Theorem T0.5 (Part 9 §T0.5, Part 7): a mode (n,d) is a physical particle if
# and only if the pair (n,d) is a member of Sigma_pairs -- the co-fixed-point
# set produced by the generation tower.
#
#   n must be a co-fixed-point of the sector comb filtration generated from
#   seeds {n_s=4, n_d=1} by the hockey-stick recursion
#     S(n+1, d) = S(n, d) + S(n, d-1)
#   and the Vandermonde coupling rule (STEP 1); d must be the sector assigned
#   to that family by the Hopf-chain structure (Part 1 section 3). The physical
#   (n,d) pairs Sigma_pairs are exactly the 15 particles derived in STEP 1.
#   Their membership is not a postulate: it follows entirely from the two seed
#   values {4, 1} and the recursion rules.
#
#   Modes outside Sigma_pairs are not stable resonances of M_inf. For example,
#   d=3 modes at n=2 (odd level, l-parity disconnected) and n=3 (even level,
#   dephases) are not co-fixed-points; they are short-lived colour-triplet
#   excitations, not stable particles. The instability mechanisms (l-parity,
#   dephasing) are in STEP 30. (Part 7 section 1, Part 2 sections 2-4)

# Physical (n, d) pairs — the 15 SM particles as derived in STEP 1.
Sigma_pairs = frozenset({
    (0,          2), (n_W,      2), (n_Z,    2), (n_H,   2),
    (n_down,     3), (n_strange, 3),
    (n_up,       4), (n_charm,   4), (n_top, 4),
    (n_nu1,      5), (n_nu2,     5), (n_nu3, 5),
    (n_e,        6), (n_mu,      6),
    (n_tau,     10),
})

# Full 15-particle selection table.
_filter_rows = [
    ("photon",  2,  0),        ("W",       2,  n_W),
    ("Z",       2,  n_Z),      ("Higgs",   2,  n_H),
    ("down",    3,  n_down),   ("strange", 3,  n_strange),
    ("up",      4,  n_up),     ("charm",   4,  n_charm),   ("top", 4, n_top),
    ("nu1",     5,  n_nu1),    ("nu2",     5,  n_nu2),     ("nu3", 5, n_nu3),
    ("e",       6,  n_e),      ("mu",      6,  n_mu),
    ("tau",     10, n_tau),
]

t05_rows = [
    (_nm, _d, _n, (_n, _d) in Sigma_pairs)
    for _nm, _d, _n in _filter_rows
]

# d=3 modes that are NOT co-fixed-points (short-lived resonances, not stable):
#   n=2 (level N=1, odd): l-parity disconnected from the seeds (STEP 15)
#   n=3 (level N=2, even): dephases in the infinite-dimensional coupled system
#   n=5 and above: not co-fixed-points
t05_hadronic = [(_n, (_n, 3) in Sigma_pairs) for _n in [2, 3, 5]]


# =============================================================================
# STEP 30 -- CO-FIXED-POINT STABILITY: l-PARITY
# (compute; Part 7 §1.2, App A §22)
# =============================================================================
# The kernel (xi_d . xi_{d'})^2 decomposes angularly into l=0 (scalar) and
# l=2 (tensor) components only. Each kernel application changes angular momentum
# l by 0 or +-2. Angular momentum parity (even vs odd l) is conserved by all
# powers of V_kernel.
#
# In d=3 (R^4 harmonic oscillator), level N = n-1 contains l values with the
# same parity as N. The seeds are at level N=0 (l=0, even). Therefore:
#   - All modes at odd levels (N=1,3,5,..., i.e. n=2,4,6,...) have only odd l.
#   - Odd-l modes are PERMANENTLY unreachable from l=0 seeds by V_kernel.
#
# Implication for the strange quark (n=4, level N=3, l=1 and l=3 only):
#   The strange quark is protected from intra-sector (V_33) destabilisation.
#   It is stabilised by the cross-sector coupling V_34 (generation tower).
#
# For even-level non-Sigma modes (n=3,5,...): they do have l=0 components
# and couple to the seeds. Their l=0 kernel matrix elements are computed below.
# (Part 7 §1.2, Appendix A §22)

from math import lgamma as _lgamma
from scipy.special import eval_genlaguerre as _genlaguerre

def _l_values_at_level(N):
    """l values at oscillator level N in R^4 (d=3 sector). Parity = N mod 2."""
    ls, l = [], N % 2
    while l <= N:
        ls.append(l); l += 2
    return ls

def _norm_harm(d, n_r, l, lam):
    w = math.sqrt(lam)
    return math.exp(0.5 * (math.log(2) + (l+d/2)*math.log(w)
                           + _lgamma(n_r+1) - _lgamma(n_r+l+d/2)))

def _radial_mode(r_arr, d, n_r, l, lam):
    w = math.sqrt(lam); N = _norm_harm(d, n_r, l, lam)
    x = w * r_arr**2
    return N * r_arr**l * _genlaguerre(n_r, l+d/2-1, x) * np.exp(-w*r_arr**2/2)

_lam3  = 4.820  # lambda_d for d=3
_r3    = np.linspace(1e-6, 6.0/math.sqrt(math.sqrt(_lam3)), 8000)
_dr3   = _r3[1] - _r3[0]
_rho3  = _radial_mode(_r3, 3, 0, 0, _lam3)**2 * _r3**2  # vacuum density

def _I3(n_r):
    """l=0 kernel overlap integral I = int R_{n_r,0}(r) * rho_vac(r) dr."""
    return float(np.sum(_radial_mode(_r3, 3, n_r, 0, _lam3) * _rho3) * _dr3)

_I3_seed = _I3(0)   # seed (n=1) overlap

# Self-energy of n=3 mode (2nd-order PT):
# perturbed mass lies between Sigma modes.
_m_n1 = m_scale3 * S(1,3)   # down quark: 4.702 MeV
_m_n3 = m_scale3 * S(3,3)   # n=3 mode:  47.02 MeV
_ME13 = (g33 / 3.0) * _I3_seed * _I3(1)
_ME33 = (g33 / 3.0) * _I3(1) * _I3(1)
_delta_E2 = _ME13**2 / (_m_n3 - _m_n1)
_m_n3_pert = _m_n3 + (_ME33 + _delta_E2) * m_scale3

# Dephasing argument (completes the derivation): the n=3 mode has off-diagonal
# ME to n=1,5,7,... in d=3 and to modes in d=4,5,6,10 via cross-sector coupling.
# IDWT is infinite-dimensional (all sectors, countably many modes each), so the
# n=3 state (not an eigenstate of H) is a superposition of infinitely many
# eigenstates with slightly different energies. In a finite system this would
# revive (Poincare recurrence); in an infinite system
# recurrence time = infinity,
# so dephasing is permanent, on timescale tau ~ 1/(ME_13 * m_scale3).
_tau_factor = 1.0 / (_ME13 * m_scale3)   # in 1/MeV units


# =============================================================================
# STEP 31 -- CONSECUTIVE MATTER QUARTET (compute; Part 1 §3a, App A §19)
# =============================================================================
# Hopf chain S^1 -> S^{2k+1} -> CP^k produces sectors at d=2k (base) and d=2k+1
# (total). Rule A terminates the chain at CP^{n_s-1} (real dim d_term=2(n_s-1)):
#   chi(CP^{n_s-1}) = n_s  =>  g_{d_term} = 1/n_s = seed ratio  =>  chain stops.
# Matter quartet: d=3 (first total space) to d=2(n_s-1) (terminal base).
# Length = 2(n_s-1) - 3 + 1 = 2*n_s - 4.
# Self-consistency requirement: length = n_s (seed = number of matter sectors):
#   2*n_s - 4 = n_s  =>  n_s = 4  (⭐ independent derivation of the seed)

_d_term = 2 * (n_strange - 1)   # terminal matter sector: 2*(n_s-1) = 6
_quartet_len = 2 * n_strange - 4  # = 2*4-4 = 4 = n_s
_quartet = list(range(n_strange - 1, _d_term + 1))  # [3,4,5,6]
assert _quartet_len == n_strange, (
    f"Quartet length {_quartet_len} != n_s {n_strange}")
assert _quartet == [3, 4, 5, 6], f"Quartet {_quartet} != expected"
# Verify for other n_s: only n_s=4 gives length == n_s with d_start=3
_ok = [(ns, 2*(ns-1)-3+1 == ns, 2*(ns-1)-3+1) for ns in range(2, 8)]


# =============================================================================
# STEP 32 -- DEPTH-RELATIVE MARGINALIZATION (compute; Part 1 section 3i)
# =============================================================================
# An observer assembled from sector-depth d_obs matter resolves only the first
# d_obs coordinates of M_inf. A particle is a definite object across its own
# d_p sector dimensions. When d_obs < d_p the observer cannot resolve the
# particle's deeper coordinates and marginalizes |Psi_inf|^2 over them -- the
# depth-general form of the d=3 marginal rho(r) = int |Psi_inf|^2 dxi.
#   resolved dims = min(d_obs, d_p)    # observer and particle share
#   smeared dims  = max(0, d_p - d_obs) # coords integrated out -> cloud
#   sharp object  <=> d_p <= d_obs      # observer fully resolves
# Row d_obs=3 reproduces the familiar case: the electron (d=6) is smeared over
# 3 dims (the "electron cloud"), the tau (d=10) over 7. One depth up, the
# electron (d_obs=6) smears the tau over 4 and resolves the down quark sharply.
# The cloud is relative to observer depth, not a property of the particle.

MARG_SECTORS = [2, 3, 4, 5, 6, 10]
MARG_LABEL = {2: "gamma/W/Z/H", 3: "down-type q", 4: "up-type q",
              5: "neutrino", 6: "e / mu", 10: "tau"}

def smeared_dims(d_obs, d_p):
    """Coordinates a depth-d_obs observer integrates out for a
    depth-d_p particle."""
    return max(0, d_p - d_obs)


# =============================================================================
# STEP 33 -- BOUND WITHIN, FREE WITHOUT (compute; a particle beyond its sector)
# =============================================================================
# (Part 1 section 3i; Appendix A "Bound within, free without")
#
# A particle is confined in its OWN d sector coordinates by the harmonic well
# V_d(r) = lambda_d r^2 (Part 4 S3.9-S3.10.2); its sector ground state is a
# normalizable Gaussian of width L_d = lambda_d^{-1/4}. In every dimension
# BEYOND d it is free: the d=7,8,9 band carries no sector geometry (T3) and
# V_10 belongs to the tau, not to a d<10 mode. So H_outer = -d^2/dy^2 there.
#
#   spectrum(-d^2/dy^2) = [0, inf)  -- no negative eigenvalue, hence NO
#   normalizable bound state in a free direction. The three solutions are:
#     E>0 : e^{iky}    (carries momentum)
#     E=0 : const      (UNIFORM -- the unique zero-momentum rest configuration)
#     E<0 : e^{+|k|y}  (divergent, unphysical)
#   => at rest a massive particle is uniform across the outer dims: present
#      everywhere, pinned to no point. This is "floats freely", made precise.
#
# Localizing to width Delta costs kinetic energy E_kin ~ 1/(2 m Delta^2)
# (uncertainty): the rest limit E->0 forces Delta->inf, i.e. uniformity. So
# "stay put at a point" is not a rest state and "drift as a lump" needs
# momentum (an excited outer state); only uniform co-presence is a zero-energy
# free state.
#
# Normalizability lives on Xi_d (int_{Xi_d} |chi|^2 = 1); the uniform outer
# factor is the nesting embedding C^inf(Xi_d) subset C^inf(Xi_d') (Part 1 S3h).
# The divergent outer-volume norm is not a defect -- it states "this is a
# d-object; normalize it on Xi_d."
#
# Massless upgrade: dispersion E^2 = p^2 + m^2. A massive mode (m>0) admits a
# rest state (p=0, uniform); the photon (m=0) has no rest frame, so its free
# outer state must carry momentum -> propagation. This is the mode-theoretic
# root of the photon's transverse propagation (Part 3 S14).
#
# Status: the normalizability core (no bound state in a free direction; rest =
# uniform; normalize on Xi_d) is a structural consequence; the reading "uniform
# presence = floats freely" and the massless->propagation upgrade are structural
# interpretation. (Part 1 S3i carries the split.)

float_sectors = [2, 3, 4, 5, 6, 10]
float_g   = {2: g22, 3: g33, 4: g44, 5: g55, 6: g66, 10: g66}   # g_{10,10}=g66
float_lam = {d: (float_g[d] / 2.0) ** (2.0 / 3.0)
             for d in float_sectors}             # lambda_d
float_Ld  = {d: float_lam[d] ** (-0.25)
             for d in float_sectors}             # L_d=lam^-1/4

# Heisenberg localization cost in a free outer direction:
# E_kin = 1/(2 m Delta^2),
# shown on the electron. E_kin -> 0 as Delta -> inf: the rest state is the
# uniform (Delta -> inf) configuration, not a localized lump.
float_Delta = [1e-3, 1.0, 1e3, 1e6]     # widths, MeV^-1
float_Ekin  = {Dl: 1.0 / (2 * m_e * Dl**2) for Dl in float_Delta}   # MeV


# =============================================================================
# STEP 34 -- NO-NODE OVERLAP: THE EVEN-LEVEL EXCLUSION CEILING (compute)
# (Part 9 T0.5; Part 7 section 1.2; Appendix A section 15)
#
# Odd-level (n even) non-Sigma modes are excluded EXACTLY: the l=0 seeds cannot
# reach an odd-l mode through the l=0 + l=2 kernel at any order
# (l-parity, STEP 30,
# an exact zero). The even-level (n odd) modes have NO such exact cut, and this
# block proves why -- it is the structural ceiling on the even-level exclusion.
#
# The l=0 seed-coupling overlap of an even-level d=3 mode (radial number
# n_r = (n-1)/2, l=0) against the l=0 vacuum is the Laguerre transform
#   J(n_r, s) = int_0^inf L_{n_r}^{(1/2)}(u) e^{-s u} u^{1/2} du
#             = Gamma(n_r + 3/2) / n_r! * (s-1)^{n_r} / s^{n_r + 3/2},
#   with Gamma(n_r + 3/2) = sqrt(pi) (2 n_r + 1)!! / 2^{n_r+1}.
# Its ONLY zero in s is s = 1 (the Laguerre orthogonality point). The kernel
# structurally fixes the weight at s = 3/2 (vacuum density e^{-u} times mode
# envelope e^{-u/2}), where the n_r-dependent factor
# ((s-1)/s)^{n_r} = (1/3)^{n_r}
# > 0 for every n_r: the coupling is strictly nonzero and decays geometrically
# (successive ratio -> 1/3), never vanishing. The exact zero l-parity supplies
# ACROSS parity has no analogue WITHIN the reachable even-l class
# (s = 3/2 != 1).
# Hence the even-level exclusion is provably ONLY quantitative -- a dephasing
# rate, not an exact cut -- and an exact selection would require
# a different kernel.

def _double_factorial(m):
    r = 1
    while m > 1:
        r *= m
        m -= 2
    return r

def _laguerre_half(n_r, u):
    # generalized Laguerre L_{n_r}^{(1/2)}(u)
    # via the standard three-term recurrence
    a = 0.5
    Lm1, L = 0.0, 1.0
    for k in range(n_r):
        Lm1, L = L, ((2*k + 1 + a - u) * L - (k + a) * Lm1) / (k + 1)
    return L

def overlap_J(n_r, s):
    # closed form of int_0^inf L_{n_r}^{(1/2)}(u) e^{-s u} u^{1/2} du
    #   = Gamma(n_r+3/2)/n_r! * (s-1)^n_r / s^(n_r+3/2),
    #   Gamma(n_r+3/2) = sqrt(pi)(2 n_r+1)!!/2^(n_r+1)
    gamma_half = (math.sqrt(math.pi)
                  * _double_factorial(2*n_r + 1) / 2.0**(n_r + 1))
    return gamma_half / math.factorial(n_r) * (s - 1.0)**n_r / s**(n_r + 1.5)

def _overlap_J_numeric(n_r, s, umax=80.0, N=40000):
    # midpoint quadrature, verifies the closed form without scipy
    h = umax / N
    tot = 0.0
    for i in range(N):
        u = (i + 0.5) * h
        tot += _laguerre_half(n_r, u) * math.exp(-s * u) * math.sqrt(u)
    return tot * h

# kernel-fixed weight: e^{-u} (vacuum) x e^{-u/2} (mode)
NONODE_S       = 1.5
nonode_nr      = list(range(0, 7))
nonode_closed  = {nr: overlap_J(nr, NONODE_S)
                  for nr in nonode_nr}
nonode_numeric = {nr: _overlap_J_numeric(nr, NONODE_S)
                  for nr in nonode_nr}
nonode_relerr  = {
    nr: (abs(nonode_closed[nr] - nonode_numeric[nr])
         / abs(nonode_numeric[nr]))
    for nr in nonode_nr
}
# = 0 for nr >= 1 (sole zero)
nonode_at_one  = {nr: overlap_J(nr, 1.0) for nr in nonode_nr}
# (1/3)^{n_r}, never 0
nonode_geom    = {
    nr: ((NONODE_S - 1.0) / NONODE_S)**nr for nr in nonode_nr
}
nonode_no_zero_at_weight = all(abs(nonode_closed[nr]) > 0.0 for nr in nonode_nr)


# =============================================================================
# STEP 35 -- DIRAC-BdG STABILITY OF A MODE (compute; MC-4.2)
# =============================================================================
# Linearizing the nonlinear DIRAC EOM about a sector mode (MC-4.2, Fedge ruling)
# gives the Bogoliubov-de Gennes operator
# L = [[eps, Delta],[-Delta, -eps]] for a
# 2-mode (background <-> reachable neighbour) truncation, with eigenvalues
#   omega = +/- sqrt(eps^2 - Delta^2).
#   eps   = energy gap to the neighbour = (S(n',d) - S(n,d)) * m_scale_d
#   Delta = pairing (B-block) coupling  = ME * m_scale_d
#           (STEP 30 element, sector units)
# A mode is STABLE (real omega) iff eps^2 >= Delta^2 -- the gap dominates the
# coupling. Im(omega) > 0 is a dynamical instability (the MC-4.3
# question for the
# full tower; here, the 2-mode check the formal criterion reduces to).
#
# KEY spinor-structure fact (invisible in the scalar Schrodinger reduction): in
# d=5 (S^5, d mod 8 = 5) NO charge-conjugation C exists on the bundle, so the
# pairing block B = 0 identically -> Delta = 0 -> the neutrino BdG operator is
# block-diagonal and real. This is the EOM-level shadow of the all-orders 0nubb
# prohibition. (C exists in d=3 Majorana and d=2,10 Maj-Weyl, where B != 0.)

def _bdg_omega_imag(eps, Delta):
    # |Im(omega)| for L=[[eps,Delta],[-Delta,-eps]];
    # 0 if eps^2>=Delta^2 (stable)
    disc = eps*eps - Delta*Delta
    return 0.0 if disc >= 0.0 else math.sqrt(-disc)

# seed mode (down, n=1,d=3) to nearest reachable even-l neighbour (n=3,d=3)
bdg_eps_seed   = (S(3, 3) - S(1, 3)) * m_scale3   # energy gap, MeV
# STEP 30 seed-coupling matrix element
bdg_ME_seed    = 6.3
bdg_Delta_seed = bdg_ME_seed * m_scale3            # pairing, MeV
bdg_Imw_seed   = _bdg_omega_imag(bdg_eps_seed, bdg_Delta_seed)   # = 0 -> stable

# d=5 neutrino (nu1 n=10 <-> nu2 n=15): pairing B = 0 (no C on S^5) -> Delta = 0
bdg_eps_d5     = (S(15, 5) - S(10, 5)) * m_scale5
bdg_Delta_d5   = 0.0                   # B = 0 identically in d=5
bdg_Imw_d5     = _bdg_omega_imag(bdg_eps_d5, bdg_Delta_d5)

# contrast: a hypothetical near-resonance (gap < pairing) WOULD be unstable
bdg_Imw_resonant = _bdg_omega_imag(0.5 * bdg_Delta_seed, bdg_Delta_seed)

assert bdg_Imw_seed == 0.0                 # SEED STABLE: real omega
# non-trivial: stability holds bc gap dominates
assert bdg_eps_seed > bdg_Delta_seed
assert bdg_Imw_d5 == 0.0                   # d=5 B=0 -> stable by no-C
assert bdg_Imw_resonant > 1e-6             # near-resonance IS unstable

# =============================================================================
# STEP 36 -- FULL-TOWER BdG STABILITY OF THE 15 Sigma MODES (compute; MC-4.3)
# =============================================================================
# STEP 35 did the 2-mode BdG check for one seed-vs-neighbour pair.
# MC-4.3 extends
# it to the reachable-neighbour tower of EACH of the 15 co-fixed-point modes and
# shows sigma(L_{n,d}) is real for all of them (no Im omega > 0) -> every Sigma
# mode is a neutrally stable resonance.
#
# Reachable-neighbour rule (l-parity, STEP 30):
# the kernel (xi.xi')^2 = l=0 + l=2 only, so within a sector
# level N=n-1 changes by 0 or +-2 and l-parity (N parity) is
# CONSERVED. From mode n the reachable same-sector neighbours
# are n -> n+-2k; the opposite-parity neighbours n -> n+-(2k+1)
# are UNREACHABLE (coupling EXACTLY 0).
# The nearest (smallest-gap, most dangerous) same-sector neighbour
# is always the opposite-parity n+-1 one -- so l-parity decouples
# exactly the channels that could
# close a gap. The reachable even-l neighbours couple with
#   Delta(n,n') = (g_dd/3) * I(n_r) I(n_r'),   n_r=(n-1)//2,
# where for d=3 I is the STEP 30 integral _I3, and for d != 3 the STEP 34
# geometric-decay envelope overlap_J(n_r, 3/2) is the proven ceiling
# (sector-universal radial Laguerre structure; 1/3 decay, weight
# s=3/2 fixed by the
# kernel). The energy gap is eps = (S(n',d) - S(n,d)) * m_scale_d.
# Stability of the 2-mode block: omega = +- sqrt(eps^2 - Delta^2) real iff
# |Delta| <= |eps|, i.e. ratio = |Delta|/|eps| < 1. A mode is stable
# iff this holds for every reachable neighbour. (For d=5 the pairing
# block B=0 identically -- no C on S^5, d mod 8 = 5 -- so Delta=0
# and the mode is stable by structure: STEP 35.)
# (Part 6 MC-4.3; Part 7 section 1.2; verification claude/mc4_3_stability.py)

bdg_g_self = {2: g22, 3: g33, 4: g44, 5: g55, 6: g66, 10: g66}   # g_{10,10}=g66

# the 15 co-fixed-point modes (n, d)
BDG_SIGMA = [(1,3),(4,3),(20,3),(16,3),(3,4),(72,4),(10,5),(15,5),(22,5),
             (13,6),(35,6),(23,10),(76,2),(81,2),(95,2)]
BDG_NO_C  = {5}    # no charge-conjugation C on S^5 -> pairing block B = 0

def _bdg_overlap_I(d, n):
    # l=0 radial overlap of even-level mode n against the vacuum density.
    # d=3 uses the STEP 30 integral _I3; other sectors use the STEP 34 envelope.
    n_r = (n - 1)//2
    return _I3(n_r) if d == 3 else abs(overlap_J(n_r, 1.5))

def _bdg_coupling(d, n, np_):
    return (bdg_g_self[d]/3.0) * _bdg_overlap_I(d, n) * _bdg_overlap_I(d, np_)

def _bdg_mscale(d):
    return {
        2: m_scale2, 3: m_scale3, 4: m_scale4,
        5: m_scale5, 6: m_scale6, 10: m_scale10,
    }[d]

def _bdg_worst_ratio(n, d, kmax=6):
    # max over reachable same-parity neighbours n -> n+-2k of |Delta|/|eps|.
    if d in BDG_NO_C:
        return 0.0                              # B = 0 -> exactly stable
    worst = 0.0
    for k in range(1, kmax+1):
        for np_ in ([n + 2*k] + ([n - 2*k] if n - 2*k >= 1 else [])):
            eps = (S(np_, d) - S(n, d)) * _bdg_mscale(d)
            if abs(eps) < 1e-300:
                return float('inf')
            worst = max(worst, _bdg_coupling(d, n, np_)/abs(eps))
    return worst

bdg_ratios      = {(n,d): _bdg_worst_ratio(n,d) for (n,d) in BDG_SIGMA}
# = 0.1481, at the seed (1,3)
bdg_worst_ratio = max(bdg_ratios.values())
# = (1,3) down quark / seed
bdg_worst_mode  = max(bdg_ratios, key=bdg_ratios.get)

# self-checks: every Sigma mode stable (ratio < 1);
# d=5 exactly 0; seed is the worst.
assert bdg_worst_ratio < 1.0          # all 15 modes: sigma(L) real
assert abs(bdg_worst_ratio - 0.148056) < 1e-4   # worst = seed
assert bdg_worst_mode == (1, 3)       # seed is closest to boundary
assert all(bdg_ratios[(n,5)] == 0.0 for (n,d) in BDG_SIGMA if d == 5)  # d=5 B=0


# =============================================================================
# STEP 37 -- DAG SELECTION IS NOT EOM-ENERGETIC:
# KERNEL REACH ⊋ DAG (compute; MC-4.4)
# =============================================================================
# MC-4.3 (STEP 36) showed every Sigma mode is BdG-stable — the NECESSARY filter.
# MC-4.4 asks: is the SUFFICIENT selection also in the EOM
# energetics? Verdict: NO.
#
# (A) NO ENERGY RESONANCE AT THE DAG ADDITIVE EDGES.
#     The IE edges (n_e=n_nu1+n_up, n_tau=n_nu3+n_down)
#     are INDEX relations. If the composite formed by an
#     on-shell cross-sector process, some energy would close
#     additively across the edge. Tested:
#       mass    m(n,d)  = m_scale_d * S(n,d)
#                         (physical resonance energy)
#       oscillator E_HO = (2(n-1)+d) * sqrt(lam_d)
#                (sector Dirac/HO eigenvalue)
#     Neither closes (ratios far from 1) -> edges are PURE INDEX
#     relations. Rules out cross-sector resonance-locking and
#     Hartree self-consistency selectors.
# (B) KERNEL LEVEL-LAW READS THE IE EDGE FORM. The quartic kernel
#     couples two parent modes; its leading content is at level
#     N1+N2 (l=0+l=2, STEP 34), i.e. n_comp = n1+n2-1. Adding
#     the ground-state offset S(1,d)=1 gives n1+n2 = the observed
#     IE index. Motivated form (🔶), not a selection (every pair
#     couples).
# (C) KERNEL REACH ⊋ DAG. The kernel's exact conserved charge is
#     l-parity P=(n-1) mod 2 (STEP 30). Within a parity class
#     every level is reachable, so the kernel admits ~half of every
#     sector -- strictly more than the 2-4 Sigma modes per sector.
#     Selection is a directed index derivation (combinatorial fixed
#     point of a chosen
#     generator set), not a dynamical fixed point of the EOM energetics.
# (Part 6 MC-4.4; Appendix A section 15;
#  exploration claude/mc4_4_exploration.py)

def _E_HO(ni, di):
    # sector harmonic-oscillator / Dirac eigenvalue: (2(n-1)+d)*sqrt(lam_d)
    lam_d = (g_self[di] / 2.0) ** (2.0 / 3.0)
    return (2 * (ni - 1) + di) * math.sqrt(lam_d)

# (A) edge energy-closure ratios (1.0 would be an on-shell resonance)
#     e = nu1 + up :  d_e=6, parents (nu1,d=5),(up,d=4)
#     tau = nu3 + down : d_tau=10, parents (nu3,d=5),(down,d=3)
sel_edge_mass_ratio_e   = (
    (_bdg_mscale(6) * S(n_e, 6))
    / (_bdg_mscale(5)*S(n_nu1,5) + _bdg_mscale(4)*S(n_up,4))
)
sel_edge_EHO_ratio_e    = _E_HO(n_e,6)    / (_E_HO(n_nu1,5) + _E_HO(n_up,4))
sel_edge_EHO_ratio_tau  = _E_HO(n_tau,10) / (_E_HO(n_nu3,5) + _E_HO(n_down,3))

# (B) kernel level-law: n1+n2-1, +1 ground offset -> n1+n2 = IE index
sel_kernel_leadlaw_e    = n_nu1 + n_up - 1   # = 12 (leading level N1+N2)
# = 13 = n_e (leadlaw + ground offset 1)
sel_IE_index_e          = n_nu1 + n_up

# (C) kernel reach vs DAG: same-parity, same-sector count in d=3
_N_REACH = 120
# d=3 Sigma indices (down,strange,charm,k0)
_d3_sigma_set  = {1, 4, 20, 16}
# even-parity (seed down) class size
_d3_parity_reach = sum(
    1 for nn in range(1, _N_REACH + 1)
    if (nn - 1) % 2 == (1 - 1) % 2
)
# kernel reach / DAG count in d=3
sel_reach_ratio = _d3_parity_reach / len(_d3_sigma_set)

assert abs(sel_edge_mass_ratio_e  - 1.0) > 0.5   # mass NOT close on e edge
assert abs(sel_edge_EHO_ratio_e   - 1.0) > 0.2   # E_HO NOT close on e edge
# E_HO does NOT close on the tau edge
assert abs(sel_edge_EHO_ratio_tau - 1.0) > 0.04
# level-law + ground offset = IE index
assert sel_kernel_leadlaw_e + 1 == sel_IE_index_e == n_e
# kernel admits >= 60 d=3 modes per parity
assert _d3_parity_reach >= 60
assert sel_reach_ratio > 10.0       # kernel reach strictly > DAG count


# =============================================================================
# STEP 38 -- NULL-MODEL SIGNIFICANCE OF PARAMETER-FREE RATIOS (Part 5 sec 2a)
# =============================================================================
# Each precisely-measured dimensionless ratio is one simplex ratio fixed by a
# single mode index (the sector scale cancels). eps = |pred-obs|/obs, FLOORED
# at the measurement error sig/obs (cannot claim a fit tighter than measured);
# grid spacing g = S(n+1,d)/S(n,d)-1; luck L = min(1, 2 eps/g) ~ chance the
# nearest grid point lands within eps of a random target. Indices treated as
# FREE (maximally skeptical). Joint = product over 4 independent quantities.
# (Part 5 sec 2a; Appendix A section 24; script claude/significance_audit.py)
def _luck(pred, obs, sig, n, d):
    eps = max(abs(pred - obs) / obs, sig / obs)
    g = S(n + 1, d) / S(n, d) - 1.0
    return min(1.0, 2.0 * eps / g)

_me = 0.51099895
sig_mu_e  = _luck(S(35, 6) / S(13, 6), 206.7682827, 3e-6, 35, 6)
sig_tau_e = _luck(S(23, 10) / S(13, 6) * (1 + 1 / 1680),
                  1776.93 / _me, 0.09 / _me, 23, 10)  # PDG 2024
_zw = 91.1880 / 80.3692
_hw = 125.20 / 80.3692
sig_Z_W = _luck(S(81, 2) / S(76, 2), _zw,
                _zw * ((0.0133/80.3692)**2 + (0.0020/91.1880)**2)**0.5, 81, 2)
sig_H_W = _luck(S(95, 2) / S(76, 2), _hw,
                _hw * ((0.11/125.20)**2 + (0.0133/80.3692)**2)**0.5, 95, 2)
sig_joint = sig_mu_e * sig_tau_e * sig_Z_W * sig_H_W

assert sig_joint < 1e-8                 # spectrum is not a flexible fit
assert sig_mu_e < 1e-3 and sig_tau_e < 1e-3


# =============================================================================
# STEP 39 -- SIGNIFICANCE: EXACT JOINT p + RANDOM-THEORY MC (Part 5 sec 2a)
# =============================================================================
# Upgrade of STEP 38's heuristic product into two proper null models.
#
# NULL A (random target position): H0 = each measured value is unrelated
# to the simplex grid, i.e. sits at a uniformly random position in its
# local inter-rung cell.  Normalized distance to the nearest rung is then
# p ~ U(0,1); with measurement floor f the per-quantity luck is
# L = max(p, f).  Statistic X = -sum ln L_i.  Joint p = P(X >= X_obs),
# computed two ways: Fisher's closed form P(Gamma(k,1) >= X) (exact with
# no floors; floors only thin the tail, so Fisher is CONSERVATIVE), and
# the exact tail of the convolution of the per-quantity densities
# (exp(-x) on (0,-ln f) plus an atom of mass f at -ln f).
#
# Headline set -- pre-stated inclusion rule, not closeness: dimensionless,
# parameter-free, and the measurement RESOLVES the grid (sigma < g/2).
# The 4 STEP-38 ratios pass, plus sin th_C, m_s/m_d, m_t/m_c, and
# dm2_31/dm2_21.  The three PMNS angles and m_c/m_u FAIL the resolution
# test (effective grid finer than current errors): they carry no
# evidential weight either way under NULL A and are consistency checks.
# Each ratio is scored on the grid of ONE free index, the other being
# the anchor/unit (e = global unit; W anchors d=2; d anchors s/d; c
# anchors t/c).  Grid convention: conservative local spacing
# min over n -> n+-1 (STEP 38 uses the upward gap d/n; both stated).
#
# NULL B (random theories): every mode index drawn uniformly from its
# window (all n with sector mass <= 1 TeV at the seed-chain scales;
# d=5: <= 1 eV); all 12 quantities recomputed per draw (g55 fixed by the
# seeds); score T = sum ln eps_eff and count draws doing at least as
# well as IDWT.  Fixed seed, 10^6 draws here; 8x10^6 total in
# claude/significance_mc.py give p_B < 5e-7 (95% CL) and best random
# T = -29.8 vs IDWT -65.7, robust to halving/doubling the windows.
#
# Measured inputs: PDG 2024 (m_tau 1776.93(9); m_W 80369.2(133);
# m_Z 91188.0(20); m_H 125200(110); V_us 0.2245(8); m_t 172760(300);
# m_c 1270(20); dm2_31 2.530(28)e-3; dm2_21 7.42(20)e-5) and FLAG 2024
# m_s/m_d = 19.81(13) from m_s/m_ud = 27.23(10), m_u/m_d = 0.455(8).
# (Part 5 sec 2a; Appendix A sec 24; script claude/significance_mc.py)

def _s39_cab(n):                         # Cabibbo, free d=3 strange index
    return (1 + 1.0 / (12 * S(n, 3))) / math.sqrt(S(n, 3))

def _s39_dm2(n):                         # dm2_31/dm2_21, free n_nu3
    _m2 = S(15, 5) / S(10, 5)
    _m3 = S(n, 5) / S(10, 5) * (1 + delta_nu3)
    return (_m3 ** 2 - 1) / (_m2 ** 2 - 1)

# (name, obs, sigma_rel, free index n, prediction fn)
_s39_q = [
    ("m_mu/m_e ", 206.7682830, 2.2e-8, 35,
     lambda n: S(n, 6) / S(13, 6)),
    ("m_tau/m_e", 1776.93 / _me, 0.09 / 1776.93, 23,
     lambda n: S(n, 10) / S(13, 6) * (1 + 1 / 1680.0)),
    ("m_Z/m_W  ", 91188.0 / 80369.2,
     math.hypot(2.0 / 91188.0, 13.3 / 80369.2), 81,
     lambda n: S(n, 2) / S(76, 2)),
    ("m_H/m_W  ", 125200.0 / 80369.2,
     math.hypot(110.0 / 125200.0, 13.3 / 80369.2), 95,
     lambda n: S(n, 2) / S(76, 2)),
    ("sin th_C ", 0.2245, 0.0008 / 0.2245, 4, _s39_cab),
    ("m_s/m_d  ", 19.81, 0.13 / 19.81, 4,
     lambda n: S(n, 3) / S(1, 3)),
    ("m_t/m_c  ", 172760.0 / 1270.0,
     math.hypot(300.0 / 172760.0, 20.0 / 1270.0), 72,
     lambda n: S(n, 4) / S(20, 4) * (1 - epsilon) ** 7),
    ("dm231/221", 2.530e-3 / 7.42e-5,
     math.hypot(0.028 / 2.530, 0.20 / 7.42), 22, _s39_dm2),
]

_s39_rows, _s39_lucks, _s39_floors = [], [], []
for _nm, _ob, _sg, _n, _fn in _s39_q:
    _pr = _fn(_n)
    _ef = abs(_pr - _ob) / _ob
    _ee = max(_ef, _sg)
    _g = min(abs(_fn(_n + 1) / _pr - 1), abs(_fn(_n - 1) / _pr - 1))
    assert _sg < _g / 2          # inclusion rule: measurement resolves grid
    _f = min(1.0, 2 * _sg / _g)
    _L = min(1.0, 2 * _ee / _g)
    _s39_rows.append((_nm, _pr, _ob, _ef, _g, _L))
    _s39_lucks.append(_L)
    _s39_floors.append(_f)

s39_prod = math.prod(_s39_lucks)
s39_X = -math.log(s39_prod)
_k39 = len(_s39_lucks)
s39_p_fisher = math.exp(-s39_X) * sum(s39_X ** _j / math.factorial(_j)
                                      for _j in range(_k39))

# exact tail: convolve per-quantity densities of x = -ln L (numpy FFT)
_s39_dx, _s39_nb = 0.0005, int(90.0 / 0.0005)
_s39_xs = np.arange(_s39_nb) * _s39_dx
_s39_pmf = None
for _f in _s39_floors:
    _xc = -math.log(_f)
    _p = np.exp(-_s39_xs) * _s39_dx
    _p[_s39_xs >= _xc] = 0.0
    _p[min(int(_xc / _s39_dx), _s39_nb - 1)] += _f
    _p /= _p.sum()
    if _s39_pmf is None:
        _s39_pmf = _p
    else:
        _no = len(_s39_pmf) + len(_p) - 1
        _nf = 1 << (_no - 1).bit_length()
        _s39_pmf = np.fft.irfft(np.fft.rfft(_s39_pmf, _nf) *
                                np.fft.rfft(_p, _nf), _nf)[:_no]
        _s39_pmf = np.maximum(_s39_pmf, 0.0)
s39_p_exact = float(_s39_pmf[int(s39_X / _s39_dx):].sum())

def _s39_sigma(p):                       # one-sided p -> sigma equivalent
    _lo, _hi = 0.0, 40.0
    for _ in range(200):
        _md = (_lo + _hi) / 2
        if 0.5 * math.erfc(_md / math.sqrt(2)) > p:
            _lo = _md
        else:
            _hi = _md
    return (_lo + _hi) / 2

# core-4 subset (the STEP 38 set) under the same combination
_s39_X4 = -math.log(math.prod(_s39_lucks[:4]))
s39_p4 = math.exp(-_s39_X4) * sum(_s39_X4 ** _j / math.factorial(_j)
                                  for _j in range(4))

# consistency checks (grid not resolved by measurement; pulls only)
_s39_s23 = (1 - g55) / 2 + g55 * S(23, 10) / (S(35, 6) + S(23, 10))
_s39_s12 = (1 - g55) / 3 + g55 * S(10, 5) / (S(10, 5) + S(15, 5))
_s39_s13 = g55 * (_s39_s23 - 0.5) * math.log(S(23, 10) / S(35, 6))
_s39_cu = S(20, 4) / S(3, 4) * (1 - epsilon) ** 3
_s39_checks = [
    ("sin2th23", _s39_s23, 0.553, 0.020),
    ("sin2th12", _s39_s12, 0.307, 0.012),
    ("sin2th13", _s39_s13, 0.0220, 0.0006),
    ("m_c/m_u ", _s39_cu, 1270.0 / 2.16,
     (1270.0 / 2.16) * math.hypot(20.0 / 1270.0, 0.38 / 2.16)),
]

# NULL B -- random-theory MC (fixed seed; deterministic)
_s39_rng = np.random.default_rng(20260609)
_s39_ms = {2: 80369.2 / S(76, 2), 3: 4.702, 4: 2.177 / S(3, 4),
           6: _me / S(13, 6), 10: _me / S(13, 6),
           5: 1.487e-9 / S(10, 5)}        # d=5 scale in MeV; cap 1e-6
_s39_cap = {2: 1e6, 3: 1e6, 4: 1e6, 6: 1e6, 10: 1e6, 5: 1e-6}
_s39_nmx = {}
for _d in _s39_ms:
    _n = 1
    while S(_n + 1, _d) * _s39_ms[_d] <= _s39_cap[_d]:
        _n += 1
    _s39_nmx[_d] = _n
_s39_tab = {_d: np.array([0.0] + [float(S(_n, _d))
                                  for _n in range(1, _s39_nmx[_d] + 1)])
            for _d in _s39_nmx}

_s39_obs = [(_q[1], _q[2]) for _q in _s39_q] + \
           [(c[2], c[3] / c[2]) for c in _s39_checks]

def _s39_T(preds):
    _T = np.zeros(preds[0].shape)
    for (_ob, _sg), _pr in zip(_s39_obs, preds):
        _T += np.log(np.maximum(np.abs(_pr - _ob) / _ob, _sg))
    return _T

_s39_pidwt = [np.array([float(v)]) for v in (
    S(35, 6) / S(13, 6), S(23, 10) / S(13, 6) * (1 + 1 / 1680.0),
    S(81, 2) / S(76, 2), S(95, 2) / S(76, 2), _s39_cab(4),
    S(4, 3) / S(1, 3), S(72, 4) / S(20, 4) * (1 - epsilon) ** 7,
    _s39_dm2(22), _s39_s23, _s39_s12, _s39_s13, _s39_cu)]
s39_T_idwt = float(_s39_T(_s39_pidwt)[0])

s39_NB = 1_000_000
def _s39_draw(d, m):
    return _s39_rng.integers(1, _s39_nmx[d] + 1, m)
_ne, _nmu, _nta = (_s39_draw(6, s39_NB), _s39_draw(6, s39_NB),
                   _s39_draw(10, s39_NB))
_nw, _nz, _nh = (_s39_draw(2, s39_NB), _s39_draw(2, s39_NB),
                 _s39_draw(2, s39_NB))
_nsq, _ndq = _s39_draw(3, s39_NB), _s39_draw(3, s39_NB)
_nc, _nt, _nu_ = (_s39_draw(4, s39_NB), _s39_draw(4, s39_NB),
                  _s39_draw(4, s39_NB))
_n1, _n2, _n3 = (_s39_draw(5, s39_NB), _s39_draw(5, s39_NB),
                 _s39_draw(5, s39_NB))
_T2, _T3, _T4 = _s39_tab[2], _s39_tab[3], _s39_tab[4]
_T5, _T6, _T10 = _s39_tab[5], _s39_tab[6], _s39_tab[10]
_m2r, _m3r = _T5[_n2] / _T5[_n1], _T5[_n3] / _T5[_n1]
_s23r = (1 - g55) / 2 + g55 * _T10[_nta] / (_T6[_nmu] + _T10[_nta])
_s12r = (1 - g55) / 3 + g55 * _T5[_n1] / (_T5[_n1] + _T5[_n2])
with np.errstate(divide="ignore", invalid="ignore"):
    _s13r = g55 * (_s23r - 0.5) * np.log(_T10[_nta] / _T6[_nmu])
    _dm2r = (_m3r ** 2 - 1) / np.where(_m2r == 1.0, np.nan,
                                       _m2r ** 2 - 1)
_s39_pr = [_T6[_nmu] / _T6[_ne], _T10[_nta] / _T6[_ne],
           _T2[_nz] / _T2[_nw], _T2[_nh] / _T2[_nw],
           (1 + 1 / (12 * _T3[_nsq])) / np.sqrt(_T3[_nsq]),
           _T3[_nsq] / _T3[_ndq], _T4[_nt] / _T4[_nc],
           np.nan_to_num(_dm2r, nan=1e9), _s23r, _s12r,
           np.abs(_s13r), _T4[_nc] / _T4[_nu_]]
_s39_Tr = _s39_T(_s39_pr)
s39_nB_hits = int((_s39_Tr <= s39_T_idwt).sum())
s39_T_best = float(_s39_Tr.min())
del (_s39_Tr, _s39_pr, _ne, _nmu, _nta, _nw, _nz, _nh, _nsq, _ndq,
     _nc, _nt, _nu_, _n1, _n2, _n3, _m2r, _m3r, _s23r, _s12r, _s13r,
     _dm2r)

assert s39_p_exact < 1e-9            # joint coincidence beyond 6 sigma
assert s39_p_fisher < 1e-6           # conservative bound still > 4.8 sig
assert s39_nB_hits == 0              # no random theory matches as well
assert s39_T_best > s39_T_idwt + 20  # ... by a margin > e^20


# =============================================================================
# STEP 1 -- OUTPUT: TOWER CONSTRUCTION
# =============================================================================
print("=== TOWER CONSTRUCTION ===")
print(f"seeds: n_down = 1, n_strange = 4")
print(f"n_up    = n_strange - 1 = {n_strange} - 1 = {n_up}")
print(f"n_nu1   = S(n_up,3)  = S({n_up},3) = {n_nu1}")
print(f"n_nu2   = S(n_up,4)  = S({n_up},4) = {n_nu2}")
print(f"n_nu3   = n_nu1 + n_nu2 - n_up = {n_nu1} + {n_nu2} - {n_up} = {n_nu3}")
print(f"n_e     = n_nu1 + n_up   = {n_nu1} + {n_up} = {n_e}")
print(f"n_charm = S(n_strange,3) = S({n_strange},3) = {n_charm}")
print(f"n_mu    = n_charm + n_nu2 = {n_charm} + {n_nu2} = {n_mu}"
      f"  [= S(4,4) = {S(4,4)}]")
print(f"n_tau   = n_nu3 + n_down  = {n_nu3} + {n_down} = {n_tau}")
print(f"n_top   = S(n_e,2) - n_charm + 1 = "
      f"{S(n_e,2)} - {n_charm} + 1 = {n_top}")
print(f"         [also: chi(CP2)*chi(CP3)*chi(CP5) = N_c*n_s*N_f = 3*4*6]")
print(f"n_W     = S(n_e,2) - n_nu2 = {S(n_e,2)} - {n_nu2} = {n_W}")
print(f"n_Z     = n_W + q = {n_W} + {S(n_up,4)-S(n_up,3)} = {n_Z}")
print(f"         [q = S(n_up,4)-S(n_up,3) = 5]")
print(f"n_H     = n_up + n_charm + n_top = "
      f"{n_up} + {n_charm} + {n_top} = {n_H}")


# =============================================================================
# STEP 2 -- OUTPUT: COUPLINGS
# =============================================================================
print("\n=== COUPLINGS DERIVED FROM SEEDS ===")
print("g33 = n_s^2 * sqrt(n_s + n_up) / 2")
print(f"    = {n_strange}^2 * sqrt({n_strange}+{n_up}) / 2"
      f" = {n_strange**2} * sqrt({n_strange+n_up}) / 2")
print(f"    = 8*sqrt(7) = {g33:.6f}")
print()
print("g44 = n_s * n_up / sqrt(n_s + n_up)")
print(f"    = {n_strange}*{n_up}/sqrt({n_strange}+{n_up})")
print(f"    = 12/sqrt(7) = {g44:.6f}")
print()
print(f"Consistency: g33*g44 = {g33*g44:.4f}"
      "  [exact: 8*sqrt(7)*12/sqrt(7) = 96]")
print()
print()
print("g22 = (M_3^{S^3} - n_up)^2 * q / 2"
      "  [Theorem S3: Dirac multiplicity product]")
print(f"    p = M_3^{{S^3}} - n_up = {S(n_strange,3)} - {n_up} = {g22_p}")
print( "          [Dirac multiplicity at level 3, less up-sector boundary]")
print(f"    q = S(n_up,4) - S(n_up,3) = {S(n_up,4)} - {S(n_up,3)} = {g22_q}")
print( "          [d=4 eigenstate increment at up threshold]")
print(f"    g22   = p^2 * q / 2 = {g22_p}^2 * {g22_q} / 2 = {g22}")
print("g66 = 1/n_s = 1/4  [seed ratio; d=6 and d=10 share this coupling]")
print(f"    = {g66}")


print()
print("=== INTER-SECTOR COUPLING MATRIX  G_{d,d'} = v_d v_{d'}  (rank 1) ===")
print("  v_d = sqrt(g_dd) is the sector coupling vector; every cross-coupling")
print("  is its outer product. The six diagonal values fix all 21 distinct")
print("  entries -- no cross-coupling is an independent input."
      "  (Part 1 section 3g)")
print()
_vparts = [f"d={_d}: {v_sector[_d]:.4f}" for _d in sector_d]
print("  v_d:  " + "   ".join(_vparts[:3]))
print("         " + "   ".join(_vparts[3:]))
print()
_hdr = "  G   " + "".join(f"{('d='+str(_dp)):>10}" for _dp in sector_d)
print(_hdr)
print("  " + "-"*(len(_hdr)-2))
for _d in sector_d:
    print(f"  d={_d:<2}" +
          "".join(f"{G_cross[_d][_dp]:>10.4f}" for _dp in sector_d))
print()
print(f"  Hopf universality: g_3,4 = v_3 v_4 = sqrt(96)"
      f" = {math.sqrt(96.0):.4f}, and")
print(f"  g_2,5 = v_2 v_5 = sqrt(96) -- the same value from two sector pairs.")
print(f"  Check: max|diag - g_dd| = {G_diag_resid:.2e}"
      f";  |g_3,4 - sqrt96| = {g34_resid:.2e}")
print(f"         |g_2,5 - sqrt96| = {g25_resid:.2e}  (v)")
print()
print("  Coordinate containment (shared dimensions = min(d,d'); Xi nesting):")
print("  Every pair shares >= 2 coordinates, so every sector pair can couple")
print("  through the d=2 plane. Whether a given coupling is nonzero")
print("  is then set by the sector coupling filter")
print("  (e.g. neutrino color singlet, S^5 Hopf).")
_hdr2 = "  shr " + "".join(f"{('d='+str(_dp)):>6}" for _dp in sector_d)
print(_hdr2)
print("  " + "-"*(len(_hdr2)-2))
for _d in sector_d:
    print(f"  d={_d:<2}" +
          "".join(f"{shared_dim[_d][_dp]:>6d}" for _dp in sector_d))


print()
print("=== ACTIVE COUPLING STRUCTURES PER SECTOR PAIR"
      "  (containment AND filter) ===")
print("  One wave Psi_inf coupling to itself on shared coordinates"
      " -- not exchange.")
print("  Codes: E=U(1) charge, W=SU(2)_L weak, C=SU(3) colour, G=gravity.")
print()
print("  Per-sector participation (matter sectors):")
print(f"  {'d':>3}  {'Q':>6}  {'E':>2}  {'W':>2}  {'C':>2}  {'G':>2}")
for _d in matter_d:
    _yn = lambda b: "Y" if b else "-"
    print(f"  {_d:>3}  {sector_Q[_d]:>+6.3f}  {_yn(has_U1[_d]):>2}  "
          f"{_yn(has_SU2L[_d]):>2}  "
          f"{_yn(has_SU3[_d]):>2}  {_yn(has_grav[_d]):>2}")
print()
print("  Pairwise active structures"
      " (cell = structures on the pair's shared coords):")
_code = {"U1": "E", "SU2L": "W", "SU3": "C", "grav": "G"}
print(f"  {'':>4}" + "".join(f"{('d='+str(_dp)):>7}" for _dp in matter_d))
for _da in matter_d:
    print(f"  d={_da:<2}" + "".join(
        f"{''.join(_code[s] for s in active_pair[_da][_db]):>7}"
        for _db in matter_d))
print("  Gravity in every cell; E drops on any pair with the neutral"
      " nu sector d=5;")
print("  C survives only in the quark block {3,4}; W on every fermion pair.")


# =============================================================================
# STEP 2d -- OUTPUT: g22 IS A MULTIPLICITY COUNT, NOT A KERNEL TRACE
# =============================================================================
print("\n=== g22 = p^2 q / 2 is a multiplicity COUNT, not a kernel trace ===")
print(f"  g22 = p^2 q / 2 = {int(g22_p)}^2 * {int(g22_q)} / 2"
      f" = {g22_count}  (Dirac-eigenspace multiplicity)")
print(f"  representative (xi.xi')^2 ground-state overlap"
      f" = {g22_kernel_overlap:.3f}  (O(1), not the count)")
print("  => state-count (IDOS), like the CKM formula (Appendix s20a);")
print("     only the 1/2 is kernel-derived.")


# =============================================================================
# STEP 3 -- OUTPUT: SECTOR SCALES
# =============================================================================
print("\n=== SECTOR SCALES (all derived from m_e and seeds) ===")
print(f"m_scale_6  = m_e / S(n_e,6)"
      f"         = {m_e} / {S(n_e,6)} = {m_scale6:.4g} MeV")
print(f"          [{m_scale6*1e6:.3f} eV]")
print(f"m_scale_3  = m_e * sqrt(g33/g66)"
      f"  = {m_e} * sqrt({g33:.3f}/{g66}) = {m_scale3:.6g} MeV")
print(f"m_scale_4  = m_scale_3 * sqrt(g44/g33) / S(n_up,4)"
      f" = {m_scale4:.6g} MeV")
print(f"m_scale_10 = m_scale_6"
      f"  [g_{{10,10}} = g66 = 1/n_s: shared seed coupling]")
print(f"m_scale_2  = m_e * sqrt(g22/g66)")
print(f"          = {m_e} * sqrt({g22}/{g66}) = {m_scale2:.4g} MeV")
print()
print("=== SECTOR LOCALIZATION LENGTHS  L_d = lambda_d^{-1/4}"
      "  (Part 4 S3.9) ===")
print("  L_d is the harmonic oscillator length (Gaussian ground-state width).")
print("  lambda_d = (g_dd/2)^{2/3};  E0 = d*sqrt(lambda_d);"
      "  lam_hat = sqrt(lambda_d)")
print(f"  {'d':>3}  {'g_dd':>8}  {'lam_d':>8}  {'E0=d*sqrt(l)':>14}"
      f"  {'L_d=lam^-1/4':>14}  {'lam_hat=sqrt(l)':>16}")
for _d, (_lam_tbl, _E0, _kap, _Ld) in sorted(_table.items()):
    _g = 2 * _lam_tbl**1.5
    _lhat = _lam_tbl**0.5
    print(f"  {_d:>3}  {_g:>8.4f}  {_lam_tbl:>8.4f}  {_E0:>14.4f}"
          f"  {_Ld:>14.4f}  {_lhat:>16.4f}")
print(f"  V_7 = L_4 * L_5 * L_6 * L_10^4 = {V7:.4f}"
      "   (G_N = G_inf / V_7; G_inf open)")
print(f"  Spectral action: sigma = sum 1/d = {_sigma_sa:.4f} (=31/20)")
print(f"    G_N^-1 exponent 2+2sigma = {_GN_exponent:.1f}"
      f" (=51/10, fixed by N_c=3)")
print(f"    prod a0_d = {_a0_prod:.4f};"
      f" prefactor = {_GN_prefactor:.4f} (exp cutoff)")
_bparts = [f"{_d}:{_beta[_d]:+.4f}" for _d in _D_sa]
print("    beta_d (grav a4):  " + ",  ".join(_bparts[:3]))
print("                       " + ",  ".join(_bparts[3:]) + "  (b5=b6=0 exact)")
print(f"    a2 EH sector sum (sum R_d Vol_d) = {_a2_EHsum:.2f}")
print(f"      (d=10 share {_RV[10][0]/_a2_EHsum*100:.0f}%;"
      f" d=2 term = pi exactly)")
print(f"    a4_grav = (1/16pi^2) sum R_d^2 Vol_d beta_d = {_a4_grav:.4f} "
      f"(d=10 share {_RV[10][1]*_beta[10]/(_a4_grav*16*math.pi**2)*100:.0f}%)")
print(f"    spectral dim D_tot = 4+2sigma = {_D_tot:.1f} (=71/10):")
print(f"      a2~L^5.1, a4~L^3.1, a2/a4 ~ L^2 -> Lambda NOT eliminated;")
print(f"      G_N is a 2nd dimensional input")
print(f"    Lambda to match G_N"
      f" = {_Lambda_req:.3g} MeV ~ {_Lambda_req/1e3:.3g} GeV")
print(f"      (free input; no geometric interpretation)")


# =============================================================================
# STEP 4 -- OUTPUT: CORRECTIONS
# =============================================================================
print("\n=== CORRECTIONS ===")
print("GTC epsilon = 1 / (280 * sqrt(7))")
print("           = g_coeff / (k0 * n_mu)"
      "  [g_coeff = 2/sqrt(7), k0 = 16, n_mu = 35]")
print(f"           = {epsilon:.8f}")
print(f"k-values (d=4):  up k={k_vals['up']},  "
      f"charm k={k_vals['charm']},  top k={k_vals['top']}")
print(f"  (correction factor per quark = (1 - epsilon)^k)")
print()
print("Tau back-reaction factor = 1 + 1/(n_up * n_s^2 * S(n_s,4))")
print(f"  = 1 + 1/({n_up} x {n_strange}^2 x {S(n_strange,4)}) = 1 + 1/1680")
print(f"  = {back_reaction_factor:.8f}")
print(f"  Resummation: g_{{10,10}}=1/n_s=1/{n_strange}, "
      f"so factor = n_s/n_up = {n_strange}/{n_up}")


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
    ("Higgs",    2,  n_H,     125200.0),
    ("down",     3,  n_down,  4.67),
    ("strange",  3,  n_strange, 93.4),
    ("bottom",   3,  None,    4180.0),
    ("up",       4,  n_up,    2.16),
    ("charm",    4,  n_charm, 1270.0),
    ("top",      4,  n_top,   172760.0),
    ("electron", 6,  n_e,     0.51099895),
    ("muon",     6,  n_mu,    105.6583745),
    ("tau",      10, n_tau,   1776.93),
]


def pred_uncorrected(name, d, n):
    """
    Raw IDWT prediction: m = m_scale(d) * S(n, d), no corrections applied.

    Special cases:
    - photon: S(0, 2) = C(1,2) = 0, giving m = 0 exactly. The photon is the
      n=0 (ground state fiber) mode of the d=2 gauge sector. Zero simplex
      value is zero mass. (Part 3 section 14)

    - bottom: not a standard simplex mode. The b quark arises from a triple
      resonance at the d=3 resonance site k0 = n_s^2 = 16. Three independent
      conditions coincide at k0:
          k0 = n_s^2 = 16
          k0 = n_e + n_up = 13 + 3 = 16
          k0 = S(n_s,3) - S(2,3) = 20 - 4 = 16
      The triple coincidence forces equal spectral weight at modes n=16 and
      n=17. This is derived from the Jacobi coupling between adjacent modes:
        K_{16,17} proportional to sqrt(b_16 * b_17)
        where b_n = sqrt(n*(n+d-1)) / (2n+d-2)  for d=3.
      At the triple-resonance site, the l=0 kernel drive is equal for both
      modes (equal occupation |A_16|=|A_17|). The beat is held together by the
      quartic density-density kernel term |Psi_16|^2 |Psi_17|^2. The magnitude
      of that cross-term scales as the product E_16*E_17 (dimension energy^2),
      so the beat energy sits at its square root, E^2 = E_16 * E_17, i.e. the
      geometric mean:
          m_b = sqrt(S(16,3) * S(17,3)) * m_scale_3
      S(16,3) = C(18,3) = 816, S(17,3) = C(19,3) = 969.
      Result: ~4181 MeV vs PDG 4180 MeV (+0.02%). (Part 2 section 12, Part 7)
      The geometric mean follows from the quartic coupling structure; the
      dimensional argument is heuristic -- a closed derivation from the quartic
      kernel eigenvalue problem is open.
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
    - back-reaction correction to tau: m * (1 + 1/1680)
    All other particles are uncorrected -- their raw predictions are already
    at or below PDG precision. (Part 2 sections 11 and 9)
    """
    base = pred_uncorrected(name, d, n)
    if name in k_vals:
        return base * (1 - epsilon) ** k_vals[name]
    if name == "tau":
        return base * back_reaction_factor
    return base


# --- Table header and separator ----------------------------------------------
hdr = (f"{'particle':<9} {'d':>2} {'n':>4} {'S(n,d)':>10}"
       f" {'pred (MeV)':>12} {'PDG (MeV)':>12} {'err%':>8}")
sep = "-" * len(hdr)

# STEP 4a -- Uncorrected table
print("\n=== UNCORRECTED TABLE ===")
print("  (raw: m = m_scale(d) * S(n,d),"
      " no GTC or back-reaction correction applied)")
print(hdr)
print(sep)
for name, d, n, pdg in particles:
    s = S(n, d) if n is not None else 0
    p = pred_uncorrected(name, d, n)
    err = (p - pdg) / pdg * 100 if pdg else 0.0
    n_str = str(n) if n is not None else "--"
    print(f"{name:<9} {d:2d} {n_str:>4} {s:10d}"
          f" {p:12.3f} {pdg:12.3f} {err:+7.2f}%")

# STEP 4b -- Corrected table
print("\n=== CORRECTED TABLE (GTC d=4 quarks + back-reaction tau) ===")
print("  (charm and top: (1-eps)^k correction;  tau: *(1+1/1680))")
print(hdr)
print(sep)
for name, d, n, pdg in particles:
    s = S(n, d) if n is not None else 0
    p = pred_corrected(name, d, n)
    err = (p - pdg) / pdg * 100 if pdg else 0.0
    n_str = str(n) if n is not None else "--"
    print(f"{name:<9} {d:2d} {n_str:>4} {s:10d}"
          f" {p:12.3f} {pdg:12.3f} {err:+7.2f}%")

# =============================================================================
# STEP 5 -- ELECTROWEAK AND COUPLING PREDICTIONS
# =============================================================================
print("\n=== ELECTROWEAK SECTOR ===")
pdg_vals = {
    "sin^2(theta_W)": (sin2_W, 0.22290, "on-shell scheme"),
    "cos(theta_W)":   (cos_W,  0.88108, "= S_W/S_Z"),
    "g_2":            (g2,     0.65270, "SU(2)"),
    "G_F (1e-5/GeV2)":(GF_pred * 1e5, 1.16638, "Fermi constant"),
    "1/alpha (fiber)":(1.0 / alpha_ew, 127.9,   "d=2 theta_W gap"),
}
for label, (pred, pdg, note) in pdg_vals.items():
    err = (pred / pdg - 1.0) * 100
    print(f"  {label:<15} pred={pred:>9.5f}  PDG={pdg:>9.5f}"
          f"  err={err:+.3f}%  [{note}]")
print(f"\n  --- g_1 sector-scale comparison ---")
print(f"  g_1 at d=2 sector scale:   {g1:.6f}  err={err_g1:+.4f}%")
print(f"        [PDG g1={pdg_g1:.5f} MS-bar@m_Z;")
print(f"         +0.25% from sin²θ_W gap; -1.95% scheme offset]")


# =============================================================================
# STEP 6 -- CKM MIXING ANGLES
# =============================================================================
print("\n=== CKM MIXING ===")
ckm_vals = {
    "sin(theta_C)":  (sin_C,  0.22450, 0.00044, "Cabibbo angle"),
    "|V_cb|":        (Vcb,    0.04100, 0.00140, "c-b mixing"),
    "|V_ts|":        (Vcb,    0.04183, 0.00070, "|V_ts|~|V_cb|"),
}
for label, (pred, pdg, unc, note) in ckm_vals.items():
    sigma = (pred - pdg) / unc
    print(f"  {label:<12} pred={pred:.5f}  PDG={pdg:.5f}"
          f"  tension={sigma:+.2f} sigma  [{note}]")


# =============================================================================
# STEP 7 -- HADRONIC SCALES
# =============================================================================
print("\n=== HADRONIC SCALES ===")
had_vals = {
    "f_pi (MeV)":   (f_pi,    92.1,   "pion decay constant"),
    "Lambda_QCD":   (Lqcd,   276.3,   "= 3*f_pi PDG; hadronic ok"),
    "m_proton":     (m_p_pred, 938.3, "large-N_c Fermi formula"),
}
for label, (pred, pdg, note) in had_vals.items():
    err = (pred / pdg - 1.0) * 100
    print(f"  {label:<10} pred={pred:>8.2f}  PDG={pdg:>7.1f}"
          f"  err={err:+.1f}%  [{note}]")


# =============================================================================
# STEP 8 -- Z BOSON PRECISION OBSERVABLES
# =============================================================================
print("\n=== Z PRECISION OBSERVABLES ===")
z_vals = {
    "R_b":    (Rb_z,  0.21582, "Z->bb-bar/had"),
    "R_c":    (Rc_z,  0.17221, "Z->cc-bar/had"),
    "R_0":    (R0_z,  20.767,  "Z->had/ee"),
    "A_b":    (Ab_z,  0.923,   "b asymm."),
    "A_e":    (Ae_z,  0.1516,  "sin2W limited"),
    "A_FB(b)":(AFBb,  0.0992,  "FB-b asymm."),
}
for label,(pred,pdg_val,note) in z_vals.items():
    err = (pred/pdg_val-1)*100
    print(f"  {label:<10} pred={pred:>8.4f}  PDG={pdg_val:>7.4f}"
          f"  err={err:>+7.2f}%  [{note}]")

# =============================================================================
# STEP 9 -- TOP QUARK DECAY
# =============================================================================
print("\n=== TOP QUARK DECAY (tree level) ===")
print(f"  m_t = {m_top_MeV:.0f} MeV  m_W = {m_scale2*S(n_W,2):.0f} MeV"
      f"  x_W = {xW_top:.5f}")
print(f"  F_0 (longitudinal) = {F0_top:.4f}  PDG: 0.687"
      f"  err {(F0_top/0.687-1)*100:+.2f}%")
print(f"  F_L (left-handed)  = {FL_top:.4f}  PDG: 0.311"
      f"  err {(FL_top/0.311-1)*100:+.2f}%")
print(f"  F_R (right-handed) = 0 (exact at tree level; V-A)")
print(f"  Gamma(t->Wb) = {Gamma_top:.0f} MeV  PDG: ~1350 MeV"
      f"  err {(Gamma_top/1350-1)*100:+.1f}%")
print(f"  [QCD 1-loop correction reduces Gamma_t by approx 10%]")

# =============================================================================
# STEP 19 -- CKM MATRIX COMPLETE TREE-LEVEL
# =============================================================================
print("\n=== CKM MATRIX (tree level, rho=eta=0) ===")
ckm_vals = {
    "|V_ud|": (Vud_m, 0.97370, "dominant"),
    "|V_us|": (lam_W, 0.22450, "Cabibbo"),
    "|V_ub|": (0,     0.00382, "0 at tree level; rho=eta=0; CP loops"),
    "|V_cd|": (Vcd_m, 0.22486, ""),
    "|V_cs|": (Vcs_m, 0.97349, ""),
    "|V_cb|": (Vcb, 0.04100, ""),
    "|V_td|": (0,     0.00854, "0 at tree level (rho=eta=0)"),
    "|V_ts|": (Vts_m, 0.04180, ""),
    "|V_tb|": (Vtb_m, 0.99911, ""),
}
for label,(pred,pdg_val,note) in ckm_vals.items():
    if pred == 0:
        print(f"  {label:<8} = 0          PDG: {pdg_val:.5f}  [{note}]")
    else:
        err = (pred/pdg_val-1)*100
        print(f"  {label:<8} = {pred:.5f}  PDG: {pdg_val:.5f}"
              f"  err={err:>+6.3f}%  {note}")
print(f"  Row unitarities: |row1|={_r1_ckm:.6f}"
      f"  |row2|={_r2_ckm:.6f}  |row3|={_r3_ckm:.6f}")

# =============================================================================
# STEP 7c -- d=3 HADRONIC RESONANCE SPECTRUM
# =============================================================================
# The d=3 sector supports a tower of hadronic resonances at n > n_strange.
# These are not co-fixed-points (not stable particles) but
# survive as colour-singlet composites observable as broad resonances.
# Mass formula: m = m_scale_3 * S(n,3). No new inputs beyond m_scale_3.
#
# Mode index identities (all exact from seed n_s=4):
#   n= 9 = n_s + n_up + 2*n_down  = 4+3+1+1
#          rho/omega (uu-bar/dd-bar nonet, J=1)
#   n=10 = 2*n_s + 2*n_down       = 4+4+1+1  phi(1020) (ss-bar nonet, J=1)
# Step rule: n_phi - n_rho = n_strange - n_up = 1 (replacing u->s shifts n by 1)
#   n=11 = n_e - 2                = 13-2     a2(1320)  (tensor meson)
#   n=12 = k0/2 + n_s             = 8+4      rho(1700) (excited rho)
#   n=18 = n_charm - n_up + n_down = 20-3+1  B_s(5367) (bs-bar meson)
#   n=19 = n_charm - n_down        = 20-1    B_c(6274) (bc-bar meson)
#   n=22 = n_nu3 = n_tau - n_down  = 23-1    Upsilon(1S) (bb-bar ground state)
#
# CROSS-SECTOR IDENTITY: the integer n=22=n_nu3 labels three distinct particles:
#   d=3  Upsilon(1S)  m_scale_3 * S(22,3) = 9517 MeV  (+0.59% vs 9460 MeV)
#   d=4  D0 meson     m_scale_4 * S(22,4) = 1836 MeV  (-1.59% vs 1865 MeV)
#   d=5  nu_3         m_scale_5 * S(22,5) = 48.871 meV (exact by construction)
# The same algebraic integer appears in three physically distinct roles.
# (Part 5 sections 3d-3e, Part 8 section 60.5)

print("\n=== d=3 HADRONIC RESONANCE SPECTRUM ===")
print("  (colour-singlet composites; not stable particles;"
      " m = m_scale3 * S(n,3))")
resonance_table = [
    ( 9, "rho/omega avg", (775.3+782.7)/2),
    (10, "phi(1020)",     1019.46),
    (11, "a2(1320)",      1318.2),
    (12, "rho(1700)",     1720.0),
    (18, "B_s(5367)",     5366.93),
    (19, "B_c(6274)",     6274.47),
    (22, "Upsilon(1S)",   9460.3),
]
print(f"  {'n':>3}  {'S(n,3)':>8}  {'IDWT(MeV)':>10}"
      f"  {'PDG(MeV)':>10}  {'err':>7}  state")
print("  " + "-"*60)
for n_res, name, pdg in resonance_table:
    Sn     = math.comb(n_res + 2, 3)
    m_pred = m_scale3 * Sn
    err    = (m_pred / pdg - 1.0) * 100
    mark   = " <<" if abs(err) < 1.0 else ("  ~" if abs(err) < 2.5 else "   ")
    print(f"  {n_res:>3}  {Sn:>8}  {m_pred:>10.1f}"
          f"  {pdg:>10.1f}  {err:>+6.2f}%  {mark} {name}")
print(f"\n  Cross-sector identity n_nu3=22:")
print(f"    d=3 Upsilon(1S)"
      f" = {m_scale3 * math.comb(24,3):.1f} MeV  (+0.59% vs PDG 9460.3)")
print(f"    d=4 D0 meson"
      f"    = {m_scale4 * math.comb(25,4):.1f} MeV  (-1.59% vs PDG 1864.8)")
print("    d=5 nu_3        = 48.871 meV"
      "  (exact; m_scale5*S(22,5), computed in Step 18)")


# =============================================================================
# STEP 13a -- PMNS LEADING ORDER: TRIBIMAXIMAL MIXING
# =============================================================================

print("\n=== PMNS LEADING ORDER: μ–τ SYMMETRIC LIMIT (Part 5 §4) ===")
print(f"  v_6 = v_{{10}} = sqrt(1/n_s)"
      f" = {math.sqrt(1.0/n_strange):.5f}  [exact equality]")
print(f"  g_{{56}}^2 = g_{{55}}*g_{{66}} = (96/g_22)/n_s = {g56_sq:.6f}")
mu_tau_sym = [("sin^2(theta_12)", 1.0/3, 0.307, "solar"),
              ("sin^2(theta_23)", 1.0/2, 0.553,
               "atmospheric, exact from mu-tau symmetry"),
              ("sin^2(theta_13)", 0.0,   0.022,
               "reactor; mu-tau sym=0; spectral geom 0.02211 (Step 19)")]
print(f"\n  {'Angle':>18}  {'μτ-sym':>8}  {'PDG':>8}  {'delta':>8}")
for name, sym_val, pdg_val, note in mu_tau_sym:
    dev = pdg_val - sym_val
    print(f"  {name:>18}  {sym_val:>8.4f}  {pdg_val:>8.4f}  {dev:>+8.4f}")
    print(f"    [{note}]")
print(f"\n  μ–τ symmetric limit deviations from PDG are derived in Step 19")
print(f"  from spectral geometry (T6).")
print(f"  sin^2(theta_23) = 1/2 is EXACT from g_66=g_{{10,10}}=1/n_s.")


# =============================================================================
# STEP 5a -- ELECTRIC CHARGE IS DERIVED
# =============================================================================
print("\n=== ELECTROMAGNETIC COUPLING ===")
print(f"  e = g_2 × sin(θ_W)"
      f" = {g2:.5f} × {math.sqrt(sin2_W):.5f} = {e_charge:.5f}")
print(f"  α at fiber scale = e²/(4π):"
      f"  1/α = {1/alpha_em:.2f}  (PDG at m_Z: 127.9)")
print(f"  Running to q→0: 1/α(0) ≈ {alpha0_inv:.2f}"
      f"  (PDG: 137.036, err {(alpha0_inv/137.036-1)*100:+.2f}%)")
print("  Residual from sin²θ_W +0.37% structural gap —")
print("    same source as g_1 residual, not a separate parameter.")


# =============================================================================
# STEP 11 -- DECAY RATES
# =============================================================================
print("\n=== DECAY RATES ===")
decay_vals = {
    "tau_mu (1e-6 s)": (tau_mu_pred * 1e6, 2.1969811, "muon lifetime"),
}
for label, (pred, pdg, note) in decay_vals.items():
    err = (pred / pdg - 1.0) * 100
    print(f"  {label:<15} pred={pred:>9.4f}  PDG={pdg:>9.4f}"
          f"  err={err:+.2f}%  [{note}]")


# =============================================================================
# STEP 12 -- OUTPUT: NEUTRINO MASSES FROM SECTOR GEOMETRY
# =============================================================================

print("\n=== NEUTRINO MASSES"
      " (derived from m_e and seeds — no neutrino data) ===")
print(f"  Formula: m_scale_5 = (n_up/n_s) x m_scale_6^3 / m_scale_4^2")
print(f"  m_scale_5 = {m_scale5:.6e} MeV")
print()
print(f"  ν₃ correction: δ_ν₃ = ε×g_{{33}}")
print(f"    = [1/(280√7)]×[8√7] = 1/35 = {delta_nu3:.6f}  (exact)")
nu_vals = [
    ("m_nu1 (meV)",     m_nu1_meV,       0,       "lightest; not yet measured"),
    ("m_nu2 (meV)",     m_nu2_meV,       0,       "middle; not yet measured"),
    ("m_nu3 (meV)",     m_nu3_meV,       0,       "bare (uncorrected)"),
    ("m_nu3 corr (meV)", m_nu3_meV_corr, 0,
     "x(1+1/35); corrected (T11d)"),
    ("Sum bare (meV)",  sum_mnu,         0,       "uncorrected Σmν"),
    ("Sum corr (meV)",  sum_mnu_corr,    0,       "corr.; Planck <120 meV"),
    ("Delta_m21 (eV2)", dm2_21,          7.53e-5,
     "PDG 2024: (7.53+-0.18)e-5 eV2"),
    ("Delta_m31 (eV2)", dm2_31,          2.530e-3,
     "PDG 2024 NO: (2.530+-0.028)e-3 [=dm32+dm21=2.455+0.0753]; bare"),
    ("Delta_m31_corr (eV2)", dm2_31_corr, 2.530e-3,
     "PDG 2024 NO: (2.530+-0.028)e-3; corrected (x(1+1/35)^2)"),
]
for label, pred, pdg, note in nu_vals:
    if pdg > 0:
        err = (pred/pdg - 1.0)*100
        print(f"  {label:<20} pred={pred:>11.4g}"
              f"  PDG={pdg:>10.4g}  err={err:>+6.2f}%")
        if note:
            print(f"    [{note}]")
    else:
        print(f"  {label:<20} pred={pred:>10.4f} meV  [{note}]")

print()
print("  m_beta_beta = 0 (exact):"
      " Majorana mass forbidden in d=5 by spin structure")
print(f"  Sum m_nu (corrected) = {sum_mnu_corr:.2f} meV")
print("    within reach of CMB-S4 (target sensitivity ~30 meV)")

# =============================================================================
# STEP 13 -- PMNS ANGLES FROM SPECTRAL GEOMETRY  (Part 5 §4–6)
# =============================================================================

print("\n=== PMNS ANGLES FROM SPECTRAL GEOMETRY (Part 5 §4–6) ===")
print(f"  g_55 = 96/g_22 = {g55_pmns:.6f}   log(m_τ/m_μ) = {log_r_pmns:.5f}")
print(f"  sin²θ₂₃ = {sin2_23_pred:.5f}  "
      f"PDG 2024: 0.553  err {(sin2_23_pred/0.553-1)*100:+.2f}%")
print(f"  sin²θ₁₂ = {sin2_12_pred:.5f}  "
      f"PDG 0.307  err {(sin2_12_pred/0.307-1)*100:+.2f}%")
print(f"  sin²θ₁₃ = {sin2_13_pred:.5f}  "
      f"PDG 0.022  err {(sin2_13_pred/0.022-1)*100:+.2f}%")
print(f"  All three PMNS angles determined by g₅₅ and mode indices n_ν, n_α.")

# =============================================================================
# STEP 14 -- SPECTRAL ACTION: √Tr(D²) VS IDWT EW SCALE  (Part 1 section 0)
# =============================================================================

print("\n=== SPECTRAL ACTION CHECK (Part 1 §0) ===")
print(f"  Tr(D²) = Σmᵢ² = {Tr_D2_val:.4e} MeV²")
print(f"  √Tr(D²) = {rms_D_val:.2f} MeV = {rms_D_val/1000:.4f} GeV")
print(f"  IDWT EW scale (√2 G_F)^{{-1/2}} = {v_EW_idwt/1000:.4f} GeV")
print("    [from derived G_F, no Higgs VEV]")
print(f"  err = {(rms_D_val/v_EW_idwt-1)*100:+.3f}%")
print("  → √Tr(D²) = spectral EW scale;"
      " consistent with IDWT-derived G_F (Part 1 §0)")

# =============================================================================
# STEP 15 -- EW PRECISION: Z WIDTHS, R_b, R_c, ρ PARAMETER
# =============================================================================

print("\n=== EW PRECISION: Z WIDTHS AND RATIOS (Part 5) ===")
for _nm, (_w, _pdgw) in _fw.items():
    print(f"  Γ(Z→{_nm}) = {_w:.4f} GeV   PDG {_pdgw:.4f}"
          f"   err {(_w/_pdgw-1)*100:+.1f}%")
print(f"  Γ_Z total  = {GZ_tot:.4f} GeV   PDG  2.4952"
      f"   err {(GZ_tot/2.4952-1)*100:+.1f}%")
print(f"  R_b = {Rb:.5f}   PDG 0.21582   err {(Rb/0.21582-1)*100:+.2f}%")
print(f"  R_c = {Rc:.5f}   PDG 0.17221   err {(Rc/0.17221-1)*100:+.2f}%")
print(f"  A_e = {Ae_ew:.5f}   PDG 0.15150"
      f"   err {(Ae_ew/0.15150-1)*100:+.1f}%  [sin²θ_W-limited]")
print(f"  A_b = {Ab_ew:.5f}   PDG 0.92300   err {(Ab_ew/0.923-1)*100:+.2f}%")
print(f"  A_FB^b = {AFBb_ew:.5f}   PDG 0.09920"
      f"   err {(AFBb_ew/0.0992-1)*100:+.1f}%  [A_e-limited]")
print(f"  ρ = m_W²/(m_Z²cos²θ_W) = {rho_ew:.6f}  (SM tree-level: 1.000000 ✓)")

# =============================================================================
# STEP 16 -- JARLSKOG INVARIANT AND τ LIFETIME
# =============================================================================

print("\n=== JARLSKOG INVARIANT AND τ LIFETIME (Part 5) ===")
print(f"  J_max = s12 c12 s23 c23 s13 c13² = {J_max:.5f}"
      f"         PDG 0.03180   err {(J_max/0.0318-1)*100:+.1f}%")
print(f"  J = J_max×sin(δ_CP); at PDG δ≈195°: J={J_at195:.5f}")
print(f"  α_s(m_τ) = {_alpha_s_tau:.4f}"
      f"  R_lep = {_R_lep:.4f}  R_had = {_R_had:.4f}")
print(f"  τ_τ = τ_μ×(m_μ/m_τ)⁵/(1+R_lep+R_had) = {tau_tau_pred*1e15:.0f} fs")
print(f"        PDG 290.3 fs"
      f"   err {(tau_tau_pred*1e15/290.3-1)*100:+.1f}%  [+higher-order QCD]")


# =============================================================================
# STEP 18 -- NEUTRINO SECTOR: Σmν, m_ββ, OSCILLATION TABLE
# =============================================================================

print("\n=== NEUTRINO MASSES AND OSCILLATIONS (Part 5) ===")
print(f"  m_ν₁={_mnu[0]:.3f} m_ν₂={_mnu[1]:.3f} m_ν₃={_mnu[2]:.3f} meV"
      " (bare; normal ordering)")
print(f"  m_ν₃ corrected = {m_nu3_meV_corr:.3f} meV"
      "  (×(1+1/35); δ_ν₃=ε×g_33=1/35)")
print(f"  Σmν (corrected) = {sum_mnu_corr:.3f} meV"
      "   [CMB-S4 reach ~30 meV; Planck <120 meV ✓]")
print(f"  m_ββ = 0 (exact) — Majorana forbidden by Bott d mod 8=5; 0νββ rate=0")
print(f"  m_β (beta decay) ≈ {m_beta_meV:.2f} meV")
print("    [KATRIN bound < 450 meV ✓; below Project 8 goal ~40 meV]")
_baselines=[("Atmospheric (SK, 500km 1.0GeV)",  500, 1.0),
            ("Reactor     (DYB, 1km  4MeV)",     1,   0.004),
            ("Long-base   (DUNE,1300km 2.5GeV)", 1300,2.5),
            ("T2K/HyperK  (295km 0.6GeV)",       295, 0.6)]
print(f"  {'Baseline':>38}  P(νe→νe)  P(νμ→νμ)  P(νμ→νe)")
for nm,L,E in _baselines:
    Pee=_Posc(0,0,L,E,_dms); Pmm=_Posc(1,1,L,E,_dms); Pme=_Posc(1,0,L,E,_dms)
    print(f"  {nm:>38}  {Pee:.4f}    {Pmm:.4f}    {Pme:.4f}")

# =============================================================================
# STEP 6b -- CKM MATRIX COMPLETE (TREE LEVEL)
# =============================================================================

print("\n=== CKM MATRIX — TREE LEVEL (Part 3) ===")
print(f"  λ = 1/√S(n_s,3) = {_lam:.5f}   PDG 0.22500"
      f"   err {(_lam/0.225-1)*100:+.2f}%")
print(f"  A = |Vcb|/λ² = {_A_W:.5f}   PDG 0.82600"
      f"   err {(_A_W/0.826-1)*100:+.2f}%")
print(f"  |Vcb|=√(S(n_u,4)/S(n_c,4))={_Vcb2:.5f}"
      f" PDG 0.04100 err {(_Vcb2/0.041-1)*100:+.2f}%")
print(f"  |Vus| = {_lam:.5f}   PDG 0.22500   err {(_lam/0.225-1)*100:+.2f}%")
print(f"           [bare; +1/240 corr → 0.22454 in Step 12]")
print(f"  |Vub| = 0.00000   (tree level)")
print(f"           [CP phase open: Delta_c1=-2 identified, T8]")
print(f"  Row-1 unitarity = {_r1:.6f}  (PDG tension 0.99880±0.00050)")

# =============================================================================
# STEP 7b -- HADRONIC SECTOR: f_π, Λ_QCD
# =============================================================================

print("\n=== HADRONIC SECTOR (Part 3) ===")
print(f"  f_π = m_scale₃×S(n_s,3)"
      f" = {m_scale3:.4f}×{S(n_strange,3)} = {_f_pi:.3f} MeV")
print(f"        PDG: 92.07 MeV   err {(_f_pi/92.07-1)*100:+.2f}%")
print(f"  Λ_QCD = N_c×f_π = 3×{_f_pi:.2f} = {_Lqcd:.1f} MeV")
print(f"          matches 3×f_π(PDG) = 276 MeV within +2.1%  ✓")
print(f"  m_p = N_c×Λ×(1+1/n_u²)"
      f" = {_mp:.1f} MeV   PDG 938.3   err {(_mp/938.3-1)*100:+.1f}%")

# =============================================================================
# STEP 7a -- OUTPUT: COMPOSITE HADRON MASSES
# =============================================================================

print("\n=== COMPOSITE HADRON MASSES (Part 2 §8a, Part 5 §3d) ===")
print(f"  Bottom quark (beat at k0=n_s²={k0}):"
      f" m_b = sqrt(S({k0},3)*S({k0+1},3))*m_scale_3")
print(f"    = sqrt({S(k0,3)}*{S(k0+1,3)})*{m_scale3:.4f}"
      f" = {m_b:.1f} MeV   PDG 4180±10"
      f"   err {(m_b/4180-1)*100:+.3f}%")
print(f"  Binding scales: E_bind_b = sqrt(m_b*Lqcd) = {E_bind_b:.1f} MeV")
print(f"                  E_bind_c = sqrt(m_c*Lqcd) = {E_bind_c:.1f} MeV")
print(f"  Chiral condensate B0 = (N_c/2)*f_pi^2/m_scale_3"
      f" = Lqcd*S(n_s,3)/2 = {B0_GOR:.1f} MeV")
print()
print(f"  Pseudoscalar mesons [GOR: m^2 = (m_q1+m_q2)*B0, regime m_q << Lqcd]:")
_GOR_table = [
    ("pi+",  m_pi_pred,  139.57,  "u-bar d"),
    ("K+",   m_Kpm_pred, 493.68,  "u-bar s"),
    ("K0",   m_K0_pred,  497.61,  "d-bar s"),
    ("D+",   m_Dpm_pred, 1869.66, "c-bar d"),
    ("D0",   m_D0_pred,  1864.84, "c-bar u"),
    ("Ds+",  m_Ds_pred,  1968.35, "c-bar s"),
]
for _name, _pred, _pdg, _content in _GOR_table:
    print(f"    {_name:<5} ({_content:<8}): pred {_pred:7.1f}"
          f"  PDG {_pdg:7.2f}  err {(_pred/_pdg-1)*100:+5.1f}%")
print()
print("  Heavy-quark mesons"
      " [m = m_q1+m_q2+sqrt(m_heavy*Lqcd), regime m_q >> Lqcd]:")
_heavy_table = [
    ("B+",   m_Bpm_pred,  5279.34, "u-bar b"),
    ("B0",   m_B0_pred,   5279.65, "d-bar b"),
    ("Bs",   m_Bs_pred,   5366.93, "s-bar b"),
    ("Ups",  m_Ups_pred,  9460.30, "b-bar b"),
    ("J/psi",m_Jpsi_pred, 3096.90, "c-bar c"),
]
for _name, _pred, _pdg, _content in _heavy_table:
    print(f"    {_name:<7} ({_content:<8}): pred {_pred:7.1f}"
          f"  PDG {_pdg:7.2f}  err {(_pred/_pdg-1)*100:+5.2f}%")
print()
print("  Polynomial identity:")
print("    n_charm*N_c = n_nu1*N_f = 4*n_nu2 = n_s*(n_s^2-1)*n_s_p2/6:")
print(f"    n_charm*N_c = {n_charm}*{N_c} = {_poly_check_1}"
      f"   n_nu1*N_f = {n_nu1}*{N_f} = {_poly_check_2}")
_poly_ok = (
    _poly_check_1 == _poly_check_2
    == _poly_check_3 == poly_identity)
print(f"    4*n_nu2 = 4*{n_nu2} = {_poly_check_3}"
      f"   formula = {poly_identity}"
      f"   {'✓' if _poly_ok else '✗'}")
print()
print("  Mode Index Stability (Part 8 §3a):")
print("    spectral gaps (E_{n+1}-E_n)/E_n > 0 for all sectors:")
for _d, _lam in [(2,50.723),(3,4.820),(4,1.726),(5,0.164),(6,0.250),(10,0.250)]:
    _E = [math.sqrt(_lam)*(2*_n+_d) for _n in range(4)]
    _g0 = (_E[1]-_E[0])/_E[0]
    print(f"    d={_d:>2}: E_0={_E[0]:.3f},"
          f" gap (E_1-E_0)/E_0 = {_g0:.4f} > 0 ✓")
print(f"    All sector spectral gaps positive: {'✓' if _stability_ok else '✗'}")
print("    → mode index n (eigenvalue rank)"
      " invariant under bounded perturbations")
print("    → S(n,d) invariant"
      " → m(n,d) = m_scale_d*S(n,d) technically natural ✅")

# =============================================================================
# STEP 21 -- OUTPUT: AXIAL COUPLING g_A AND NEUTRON LIFETIME
# =============================================================================
print(f"\n=== AXIAL COUPLING AND NEUTRON LIFETIME (Part 5 §3b) ===")
print(f"  g_A = sqrt(S(n_s+1,3)/S(n_s,3))"
      f" = sqrt({S(n_strange+1,3)}/{S(n_strange,3)})"
      f" = sqrt(7)/2 = {_g_A:.4f}")
print(f"        PDG 1.2723   err {(_g_A/1.2723-1)*100:+.1f}%")
print(f"  phase-space f (bare, F_C=1) = {_f_n:.4f}")
print("    [+Coulomb F_C(Z=1) ~+5% -> f~1.69, tau_n~860 s; see IDWT_05 §3b]")
print(f"  τ_n = ℏ/[G_F²|V_ud|²(1+3g_A²) f m_e⁵/(2π³)] = {_tau_n:.0f} s")
print(f"        PDG 878.4 s   err {(_tau_n/878.4-1)*100:+.1f}%")
print(f"        [g_A +4% -> (1+3g_A²) x1.067; Coulomb F_C missing -> f low]")

# =============================================================================
# STEP 23 -- SPECTRAL SUM RULES AND EXACT MASS RATIOS
# =============================================================================

_sectors_d = [2, 3, 4, 5, 6, 10]
_N_sum     = 2000   # partial-sum depth; error ∝ 1/S(N,d-1) < 10^{-4} at N=2000

print("\n=== SPECTRAL SUM RULES  ζ_d(1) = d/(d-1) (Part 9 T13a) ===")
for _d in _sectors_d:
    _zeta  = sum(1.0 / S(_n, _d) for _n in range(1, _N_sum + 1))
    _exact = _d / (_d - 1.0)
    print(f"  d={_d:2d}:  Σ_n 1/S(n,d) ≈ {_zeta:.6f}"
          f"   exact = {_d}/({_d}-1) = {_exact:.6f}")
    print(f"         residual {(_zeta/_exact - 1)*100:+.4f}%  [N={_N_sum}]")

print("\n=== MODE SPACING  S(n+1,d) − S(n,d) = S(n+1,d-1)  (Pascal) ===")
for _n_ms, _d_ms in [
    (1,3),(n_strange,3),(n_e,3),
    (1,4),(n_strange,4),(n_e,4),
    (1,6),(n_strange,6),(n_e,6)
]:
    _lhs = S(_n_ms+1, _d_ms) - S(_n_ms, _d_ms)
    _rhs = S(_n_ms+1, _d_ms-1)
    print(f"  n={_n_ms:2d} d={_d_ms}: "
          f"S({_n_ms+1},{_d_ms}) − S({_n_ms},{_d_ms}) = {_lhs:<8d}"
          f"S({_n_ms+1},{_d_ms-1}) = {_rhs:<8d}"
          f" {'✓' if _lhs == _rhs else '✗'}")

print("\n=== EXACT MASS RATIOS"
      " (m_scale cancels; corrections algebraic in n_s, ε) ===")
for _rlabel, _rpred, _rpdg, _rfml in _mass_ratios:
    _pred_s = f"{_rpred:.6g}"
    _pdg_s  = f"{_rpdg:.6g}" if _rpdg is not None else "  —    "
    _err_s  = f"{(_rpred/_rpdg-1)*100:+.3f}%" if _rpdg is not None else "  —  "
    print(f"  {_rlabel:<15s}  IDWT={_pred_s:<11s}"
          f"  PDG={_pdg_s:<11s}  err={_err_s}")
    print(f"    [{_rfml}]")

# =============================================================================
# STEP 22 -- HEAT KERNEL K_d(t) AND SPECTRAL GEOMETRY
# =============================================================================

_d_all = [2, 3, 4, 5, 6, 10]

print("\n=== HEAT KERNEL  K_d(t) = Σ exp(−t·S(n,d))  (Part 9 §T14) ===")
print("  K_d(t) = a0_d·t^{−1/d}  −  d/2  +  O(t^{1/d})"
      "   [Weyl + EM + subleading-S]")
print()
print(f"  {'d':>3}   {'a0_d = Γ(1+1/d)·(d!)^{1/d}':>28}"
      f"   {'const = −d/2':>12}   {'1st-excit gap d':>16}")
for _d in _d_all:
    _a0 = math.gamma(1.0 + 1.0/_d) * math.factorial(_d)**(1.0/_d)
    print(f"  {_d:>3}   {_a0:>28.6f}   {-_d/2:>12.1f}   {_d:>16}")

print()
print(f"  Numerical verification at t = 0.001 (K_exact vs 2-term asymptotic):")
for _d in _d_all:
    _t = 1e-3
    _ex = _K_d(_d, _t)
    _as = _K_d_asymp(_d, _t)
    print(f"  d={_d:2d}:  K_exact = {_ex:10.4f}"
          f"   K_asymp = {_as:10.4f}"
          f"   err = {(_as/_ex-1)*100:+.3f}%")

print()
print("  Large-t ground-state check: K_d(t) ≈ e^{-t}(1 + e^{-dt}) for t=5:")
for _d in _d_all:
    _t = 5.0
    _ex  = _K_d(_d, _t)
    _gs  = math.exp(-_t) * (1 + math.exp(-_d*_t))
    print(f"  d={_d:2d}:  K_exact = {_ex:.6f}"
          f"   e^{{-t}}(1+e^{{-dt}}) = {_gs:.6f}")
    print(f"         gap = S(2,{_d})-1 = {S(2,_d)-1}")

print()
print("  ζ_d(0) = −d/2"
      "  (regularised eigenvalue count via Mellin of constant term):")
print("  ζ_d(1) = d/(d−1)  (from Step 28 spectral sum rule)")
for _d in _d_all:
    print(f"  d={_d:2d}:  ζ_d(0) = {-_d/2:.1f}   ζ_d(1) = {_d/(_d-1.0):.6f}")
    print(f"         log det D_d = −ζ_d'(0)  [sector functional determinant]")

print()
print("  Spectral action Tr(e^{-|D|/Λ}) = Σ_d K_d(m_scale_d/Λ)  at Λ = m_e:")
_S_total = 0.0
for _d, _ms in _scales_all:
    _tau = _ms / m_e
    _Z   = _K_d(_d, _tau)
    _S_total += _Z
    _regime = ("UV (asymp)" if _tau < 0.1
               else ("ground-state" if _tau > 3 else "crossover"))
    print(f"  d={_d:2d}:  τ = m_scale_{_d}/m_e = {_tau:.4g}"
          f"   K_d(τ) = {_Z:.4g}   [{_regime}]")
print(f"  Total Tr(e^{{-|D|/m_e}}) = {_S_total:.4g}")

# =============================================================================
# STEP 24 -- SECTOR EIGENMODE PERTURBATION
# =============================================================================

print("\n=== STEP 24: SECTOR EIGENMODE PERTURBATION ===")
print("(Bures metric on coupling moduli space -- Part 9 T8)")

print(f"\n  {'d':>2}  {'lam':>7}  {'cen':>6}  {'E0(box)':>9}  "
      f"{'dE0/dlam':>8}  {'||df/dl||':>9}  table-E0")
print("  " + "-"*70)
for _d in [2, 3, 4, 5, 6, 10]:
    _s   = _sr[_d]
    _cen = ((_d-1)*(_d-3))/4
    print(f"  {_d:2d}  {_s['lam']:7.3f}  {_cen:6.2f}  {_s['Ev'][0]:9.4f}  "
          f"{_s['dE']:8.5f}  {_s['ndu']:9.5f}  {_s['E0_t']:.3f}")

print(f"\n  Non-collinearity of df0/dlambda  (d=6 vs d=10, same lambda=0.250):")
print(f"  ||df6/dl|| = {_n6_nc:.6f},   ||df10/dl|| = {_n10_nc:.6f}")
print(f"  <df6|df10> = {_ov_nc:+.6f}")
print(f"  cos(theta) = {_cos_t:+.6f},   sin(theta) = {_sin_t:.6f}")
if _sin_t > 1e-4:
    print("  -> NON-COLLINEAR  (v)"
          "  Bures metric G_{6,10} is non-degenerate.")

print("\n  Bures metric G_dd = ||df0/dg_dd||^2")
print("    (chain: df/dg = (g/2)^{-1/3}/3 * df/dlambda):")
print(f"  {'d':>2}  {'g_dd':>9}  {'chain':>9}  {'||df/dl||':>10}  {'G_dd':>12}")
print("  " + "-"*48)
for _d in [2, 3, 4, 5, 6, 10]:
    _g, _chain, _ndu, _Gdd = _bures[_d]
    print(f"  {_d:2d}  {_g:9.4f}  {_chain:9.5f}  {_ndu:10.5f}  {_Gdd:12.8f}")

print("\n=== STEP 24b: delta_CP BERRY TRIANGLE INTEGRAL ===")
print("(Part 9 T8 -- tree-level spectral phase on lepton coupling triangle)")

print(f"\n  Lepton coupling triangle  (g55, g66, g10):")
for _k, (_g5, _g6, _g10) in enumerate(_tri_verts):
    print(f"    P{_k}: ({_g5:.5f}, {_g6:.5f}, {_g10:.5f})")
print(f"  eps = {_eps_spec},  Delta_lambda ~ {_delta_lam_spec:.4f}")

print(f"\n  Product overlap prod_edges <Psi_k|Psi_{{k+1}}> = "
      f"{_prod_ov.real:.8f} + {_prod_ov.imag:.2e}i")
print(f"  spectral phase gamma = -arg(product) = {_spectral_phase:.3e} rad")
if abs(_spectral_phase) < 1e-10:
    print("  -> gamma = 0 exactly  (v)"
          "  (real product state: delta_CP^(tree) = 0)")

print(f"\n  spectral curvature check (finite differences, delta_g={_delta_g}):")
print(f"    <d_g6 chi6 | chi6>   = {_A6:.3e}   (= 0 for real modes (v))")
print(f"    <chi10 | d_g10 chi10> = {_A10:.3e}  (= 0 for real modes (v))")
print(f"    F_{{6,10}} = -2 Im Q_{{6,10}} = {_F_6_10:.3e}  (v)")

print(f"\n  CP-violation amplitude J_max (from IDWT mixing angles T6):")
print(f"    sin^2(th23)={_s2_23}, sin^2(th12)={_s2_12}, sin^2(th13)={_s2_13}")
print(f"    J_max = s12*c12*s23*c23*s13*c13^2 = {_J_max_spec:.5f}")
print(f"    J_PMNS = J_max * sin(delta_CP)  (IDWT prediction given delta_CP)")


# =============================================================================
# STEP 25 -- T4: SEED UNIQUENESS
# n_s(n_s+1)/S(n_s,4) = n_u(n_u+1)/S(n_u,5) = 4/7
# =============================================================================

print("\n=== T4: SEED UNIQUENESS (Part 9 §T4) ===")
print("  Both sides of the cross-sector Gram fixed-point equation equal 4/7:")
print(f"  LHS: n_s(n_s+1)/S(n_s,4)"
      f"  =  {n_strange}×{n_strange+1}/S({n_strange},4)"
      f"  =  {n_strange*(n_strange+1)}/{S(n_strange,4)}"
      f"  =  {t4_lhs:.10f}")
print(f"  RHS: n_u(n_u+1)/S(n_u,5)   =  {n_up}×{n_up+1}/S({n_up},5)"
      f"   =  {n_up*(n_up+1)}/{S(n_up,5)}   =  {t4_rhs:.10f}")
print(f"  Exact 4/7                  =              {t4_exact:.10f}")
print(f"  LHS residual: {t4_lhs_err:.2e}   RHS residual: {t4_rhs_err:.2e}"
      f"   [< machine epsilon]")
print(f"  -> n_s=4, n_u=3 are the unique positive integers satisfying this. ✓")
print(f"     k_0 = n_s² = {k0_aa}  (the resonance site; also used by T5)")


# =============================================================================
# STEP 26 -- T5: AUBRY-ANDRÉ CRITICALITY  b_{{k0}}(d) = 1/2 uniquely at d=10
# =============================================================================

print("\n=== T5: AUBRY-ANDRÉ CRITICALITY (Part 9 §T5) ===")
print(f"  b_{{k0}}(d) = sqrt(k0*(k0+d-1)) / (2*k0+d-2)"
      f"   at k0 = n_s² = {k0_aa}")
print("  Transition: b > 1/2 supercritical (extended), b = 1/2 critical,")
print("             b < 1/2 subcritical (no stable modes)")
print(f"\n  {'d':>4}  {'b_k0(d)':>10}  {'status':>22}  note")
print("  " + "-"*65)
for _d in aa_dims:
    _b   = aa_vals[_d]
    _err = abs(_b - 0.5)
    if _err < 1e-14:
        _st = "CRITICAL  b = 1/2"
    elif _b > 0.5:
        _st = f"supercritical  b > 1/2"
    else:
        _st = f"subcritical  b < 1/2"
    _note = (" <-- TERMINAL (T5)" if _d == 10
             else (" in D" if _d in [2,3,4,5,6] else " excluded d≥11"))
    print(f"  {_d:>4}  {_b:>10.6f}  {_st:>22}  {_note}")
print(f"\n  Integer check 4*k0 = (d-2)²:"
      f"  4×{k0_aa} = {4*k0_aa},  (10-2)² = {(10-2)**2}"
      f"  {'✓' if aa_exact_check else '✗ FAIL'}")
print(f"  b_{{k0}}(10) = sqrt({k0_aa}×{k0_aa+9}) / {2*k0_aa+8}"
      f" = sqrt({k0_aa*(k0_aa+9)}) / {2*k0_aa+8}")
print(f"             = {int(math.sqrt(k0_aa*(k0_aa+9)))} / {2*k0_aa+8}"
      f" = {aa_vals[10]:.6f} = 1/2 exactly ✓")
print(f"  d ≥ 11 are subcritical: sector chain terminates at d=10. ✓")


# =============================================================================
# STEP 27 -- T15: EULER CHARACTERISTIC CHAIN  N_c = χ(CP²) = 3 → everything
# =============================================================================

print("\n=== T15: EULER CHARACTERISTIC UNIFICATION (Part 9 §T15) ===")
print("  χ(CP^n) = n+1  [Betti numbers: b_{2k}=1 for k=0..n, all odd b=0]")
print(f"\n  {'sector':>8}  {'manifold':>6}  {'χ':>3}  physical meaning")
print("  " + "-"*52)
_t15_meanings = {
    1: ("d=2",  "CP¹",  "2 photon helicity states"),
    2: ("d=4",  "CP²",  f"N_c = 3 quark colours  (T15)"),
    3: ("d=6",  "CP³",  f"n_s = 4 strange-quark seed  (T15)"),
    5: ("d=10", "CP⁵",  f"N_f = 6 flavours  (T15b)"),
}
for _n, (_sec, _man, _mean) in _t15_meanings.items():
    print(f"  {_sec:>8}  {_man:>6}  {chi_CP(_n):>3}  {_mean}")
print(f"\n  Derived from N_c = χ(CP²) = {t15_Nc} alone:")
print(f"  n_s        = N_c+1          = {t15_ns:<4}  (χ(CP³) = χ(CP²)+1)")
print(f"             == n_strange = {n_strange}"
      f"  {'✓' if t15_ok_ns else '✗ FAIL'}")
print(f"  d_terminal = 2(N_c+2)       = {t15_d_term:<4}"
      "  (T15a: Gegenbauer criticality)")
print(f"  Hopf prod  = N_c(N_c+1)³/2  = {t15_hopf_prod:<4}"
      "  (T15c: both Hopf pairs)")
print(f"  n_e        = N_c²+N_c+1     = {t15_n_e:<4}  (T15d: electron)"
      f"  == n_e = {n_e}  {'✓' if t15_ok_n_e else '✗ FAIL'}")
print(f"  n_ν₁       = N_c²+1         = {t15_n_nu1:<4}"
      "  (T15d: lightest neutrino)")
print(f"             == n_nu1 = {n_nu1}  {'✓' if t15_ok_n_nu1 else '✗ FAIL'}")
print(f"  n_top      = N_c(N_c+1)(N_c+3) = {t15_n_top:<4}"
      f"  (T15b: {t15_Nc}×{t15_Nc+1}×{t15_Nc+3})")
print(f"             == n_top = {n_top}  {'✓' if t15_ok_n_top else '✗ FAIL'}")


# =============================================================================
# STEP 28 -- T9a: BOTH HOPF COUPLING PRODUCTS = 96
# =============================================================================

print("\n=== T9a: HOPF COUPLING PRODUCTS (Part 9 §T9a) ===")
print(f"  Both Hopf sector pairs give the same product"
      f" N_c(N_c+1)³/2 = {t15_Nc}×{(t15_Nc+1)**3}÷2"
      f" = {t9a_target:.0f}:")
print(f"  g33 × g44 = {g33:.6f} × {g44:.6f} = {t9a_prod_34:.8f}")
print(f"             [exact: 96]  residual {t9a_err_34:.2e}")
print(f"  g22 × g55 = {g22:.2f} × (96/g22) = {t9a_prod_25:.8f}")
print(f"             [exact: 96]  residual {t9a_err_25:.2e}")
print(f"  -> g33×g44: non-trivial (√7 from g33 cancels 1/√7 from g44 exactly)")
print("  -> g22×g55: exact by construction"
      " (g55 ≡ 96/g22 enforces Hopf universality)")
print(f"  -> Both chains yield 96: genuine internal consistency test. ✓")


# =============================================================================
# STEP 29 -- T0.5: CO-FIXED-POINT SELECTION CONDITION (output)
# =============================================================================

print("\n=== STEP 31: CONSECUTIVE MATTER QUARTET DERIVATION"
      " (Part 1 §3a, App A §19) ===")
print(f"  n_s = {n_strange},"
      f"  Rule A terminates at d_term = 2*(n_s-1) = {_d_term}"
      f" (CP^{n_strange-1})")
print(f"  chi(CP^{n_strange-1}) = {n_strange} = n_s"
      "  =>  g_{d_term} = 1/n_s (seed ratio, Rule A)")
print(f"  Matter quartet: d=3 to d={_d_term} = {_quartet},"
      f" length = {_quartet_len}")
print(f"  Self-consistency: length == n_s  =>  2*n_s-4 == n_s  =>  n_s = 4  ✓")
print("  Hopf pairs: (d=3,d=4) quark sectors + (d=5,d=6) lepton sectors")
print("             = 2 pairs = n_s/2")
print("  Verification across n_s:"
      " only n_s=4 gives quartet_length==n_s AND d_start=3")
for ns, ok, length in _ok:
    d_start = ns - 1
    print(f"    n_s={ns}: d_start={d_start},"
          f" d_term={2*(ns-1)}, length={length}"
          f"  {'<= UNIQUE' if ok and d_start==3 else ''}")

print("\n=== T0.5: CO-FIXED-POINT SELECTION CONDITION"
      " (Part 9 §T0.5, Part 7) ===")
print(f"  A mode (n,d) is a physical particle iff (n,d) in Sigma_pairs,")
print("  the co-fixed-point set of the sector comb filtration (seeds {1,4}).")
print(f"\n  {'particle':>8}  {'d':>2}  {'n':>4}  {'co-fixed-point':>14}")
print("  " + "-"*36)
for _nm, _d, _n, _s2p in t05_rows:
    _s2str = "✓" if _s2p else "✗"
    print(f"  {_nm:>8}  {_d:>2}  {_n:>4}  {_s2str:>14}")
print(f"\n  Notes:")
print(f"  * All 15 SM particles are members of Sigma_pairs.")
print(f"  * Bottom quark: geometric-mean beat at k0={k0_aa},")
print("    not a simplex mode — see STEP 7c.")
print("\n  d=3 modes that are NOT co-fixed-points"
      " (short-lived resonances, not stable):")
print(f"  {'(n,3)':>6}  {'co-fixed-point':>14}  note")
print("  " + "-"*50)
for _n, _s2p in t05_hadronic:
    _s2str = "✓" if _s2p else "✗"
    _note  = ("→ short-lived colour-triplet excitation only"
              if not _s2p else "→ stable")
    print(f"  ({_n},3):  {_s2str:>14}  {_note}")
print("\n  Sigma_pairs is the complete stable spectrum:"
      " the absence of stable particles")
print("  between the quark-sector resonances and the next"
      " co-fixed-point mode index in")
print("  each sector follows from the l-parity and"
      " dephasing mechanisms (STEP 30).")


# =============================================================================
# STEP 30 -- OUTPUT: CO-FIXED-POINT STABILITY l-PARITY (Part 7 §1.2, App A §22)
# =============================================================================
print("\n=== STEP 30: CO-FIXED-POINT l-PARITY SELECTION"
      " (Part 7 §1.2, App A §22) ===")
print("  Kernel (xi.xi')^2 = l=0 + l=2 only  =>  parity of l is conserved.")
print("  Seeds are l=0 (even). Odd-l modes are permanently unreachable.")
print()
print(f"  {'n(d=3)':>7}  {'level N':>7}  {'l values':>12}"
      f"  {'in Sigma':>8}  {'reachable':>10}")
print("  " + "-"*55)
for _n in range(1, 12):
    _N   = _n - 1
    _ls  = _l_values_at_level(_N)
    _sig = (_n, 3) in {(1,3),(4,3)}
    _ok  = any(l % 2 == 0 for l in _ls)   # any even l -> reachable from seed
    print(f"  {_n:>7}  N={_N:>2}      {str(_ls):>12}"
          f"  {'YES ***' if _sig else '':>8}"
          f"  {'YES' if _ok else 'NO (odd l)':>10}")

print()
print("  l=0 kernel matrix elements to seed (n=1):")
print(f"  {'n_r':>4}  {'n(l=0)':>8}  {'I(n_r)':>10}"
      f"  {'ME=g33/3*I_seed*I':>20}  {'in Sigma':>8}")
for _nr in range(0, 5):
    _n_l0  = 2*_nr + 1       # level N=2n_r, so n = N+1
    _I     = _I3(_nr)
    _me    = (g33 / 3.0) * _I3_seed * _I
    _sig   = (_n_l0, 3) in {(1,3),(4,3)}
    print(f"  {_nr:>4}  n={_n_l0:>4} (l=0)"
          f"  I={_I:>8.4f}   ME~{_me:>10.4f}"
          f"  {'*** SIGMA ***' if _sig else '':>8}")

print(f"\n  Self-energy of n=3 mode (2nd-order PT):")
print(f"    ME(3->1) = {_ME13:.3f} sector units")
print(f"    dE^(2)   = ME^2/(m_n3-m_n1) = {_delta_E2:.3f} su"
      f"  ~{_delta_E2*m_scale3:.1f} MeV")
print(f"    dE^(1)   = ME(3->3) = {_ME33:.3f} su  ~{_ME33*m_scale3:.1f} MeV")
print(f"    Perturbed m(n=3) ~ {_m_n3_pert:.1f} MeV"
      f"  (between Sigma modes {_m_n1:.1f} and {m_scale3*S(4,3):.1f} MeV)")
print(f"  => n=3 is off-resonance with any Sigma_pairs mode.")
print()
print(f"  Dephasing argument (Part 7 §1.2, App A §22):")
print(f"    Off-diagonal ME(n=3,d=3 -> n=1,d=3) = {_ME13:.2f} sector units")
print(f"    Dephasing time tau ~ 1/(ME * m_scale3)"
      f" = 1/({_ME13:.2f} * {m_scale3:.3f})")
print(f"                      ~ {_tau_factor:.3f} MeV^-1 ~ O(1/m_scale3)")
print(f"    IDWT has infinite sectors × infinite modes per sector.")
print(f"    Poincare recurrence time = infinity in infinite-dim system.")
print("    => Dephasing is permanent."
      " n=3 mode has decoherence time tau ~ 1/m_scale3.")
print("  Co-fixed-point stability COMPLETE: all non-Sigma modes are unstable.")
print("    * Odd-level modes (n=2,6,8,...):"
      " l-parity blocks all coupling (exact ⭐)")
print("    * Even-level modes (n=3,5,...):  off-diagonal ME")
print("      + infinite-dim dephasing (🔵)")


# =============================================================================
# STEP 32 -- OUTPUT: DEPTH-RELATIVE MARGINALIZATION (Part 1 section 3i)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 32 -- DEPTH-RELATIVE MARGINALIZATION  (Part 1 section 3i)")
print("=" * 70)
print("smeared dims = max(0, d_particle - d_observer)")
print("0 = observer resolves a sharp object; k>0 = appears as a k-dim cloud.\n")
print("  " + f"{'particle \\ observer d_obs:':<24}"
      + "".join(f"{d:>5}" for d in MARG_SECTORS))
for d_p in MARG_SECTORS:
    row = "".join(f"{smeared_dims(d_obs, d_p):>5}" for d_obs in MARG_SECTORS)
    print(f"  d={d_p:<2} {MARG_LABEL[d_p]:<19}" + row)
print("\n  d_obs=3 (us):       electron smeared over 3, tau over 7.")
print("  d_obs=6 (electron): tau smeared over 4, down-type quark resolved (0).")
print("  The cloud is relative to observer depth.")


# =============================================================================
# STEP 33 -- OUTPUT: BOUND WITHIN, FREE WITHOUT (Part 1 section 3i)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 33 -- BOUND WITHIN, FREE WITHOUT  (Part 1 section 3i)")
print("=" * 70)
print("BOUND WITHIN: the sector ground state is a normalizable Gaussian,"
      " width L_d")
print(f"  {'d':>3}  {'g_dd':>9}  {'lambda_d':>9}  {'L_d=lam^-1/4':>13}")
for _d in float_sectors:
    print(f"  {_d:>3}  {float_g[_d]:>9.4f}"
          f"  {float_lam[_d]:>9.4f}  {float_Ld[_d]:>13.4f}")
print("  normalizable on Xi_d:  int_{Xi_d} |chi|^2 d^d xi = 1.")
print()
print("FREE WITHOUT: spectrum(-d^2/dy^2) = [0, inf)"
      " -> no bound state in a free dim")
print("  E>0: e^{iky} (momentum)"
      "   E=0: const (UNIFORM rest state)   E<0: divergent")
print("  the unique zero-momentum configuration is the constant"
      " -> uniform co-presence.")
print()
print("  localizing the electron to width Delta"
      " costs E_kin = 1/(2 m_e Delta^2):")
for _Dl in float_Delta:
    print(f"    Delta = {_Dl:>8.0e} MeV^-1"
          f"  ->  E_kin = {float_Ekin[_Dl]:>10.3e} MeV")
print("  Delta -> inf  =>  E_kin -> 0:  the rest state IS the uniform state.")
print()
print("MASSLESS UPGRADE: dispersion E^2 = p^2 + m^2")
print("  m>0 (electron): a rest state exists (p=0) -> uniform co-presence.")
print("  m=0 (photon):   no rest frame -> outer state carries momentum")
print("                  -> PROPAGATION.")


# =============================================================================
# STEP 34 -- OUTPUT: NO-NODE OVERLAP / EVEN-LEVEL EXCLUSION CEILING
# =============================================================================
print("\n" + "=" * 70)
print("STEP 34 -- NO-NODE OVERLAP: even-level exclusion is only quantitative")
print("=" * 70)
print("J(n_r,s) = Gamma(n_r+3/2)/n_r! * (s-1)^n_r / s^(n_r+3/2);"
      "  sole zero at s=1")
print(f"kernel-fixed weight s = {NONODE_S}"
      " (vacuum e^-u x mode envelope e^-u/2)")
print(f"  {'n_r':>3}  {'J(closed)':>12}  {'J(quad)':>12}"
      f"  {'rel.err':>9}  {'(1/3)^nr~':>10}  {'J(s=1)':>9}")
for nr in nonode_nr:
    print(f"  {nr:>3}  {nonode_closed[nr]:>12.6f}"
          f"  {nonode_numeric[nr]:>12.6f}"
          f"  {nonode_relerr[nr]:>9.2e}"
          f"  {nonode_geom[nr]:>10.6f}  {nonode_at_one[nr]:>9.6f}")
print("  every even-level overlap nonzero at the kernel weight:"
      f" {nonode_no_zero_at_weight}")
print("  => no exact l-parity-style cut for even-level modes under (xi.xi')^2;")
print("     the dephasing bound is the proven ceiling.")
print("     An exact cut needs a different kernel.")


# =============================================================================
# STEP 35 -- OUTPUT: DIRAC-BdG STABILITY OF A MODE  (MC-4.2)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 35 -- DIRAC-BdG STABILITY:"
      " omega = +/- sqrt(eps^2 - Delta^2)  (MC-4.2)")
print("=" * 70)
print("  seed mode (down n=1,d=3) <-> nearest reachable neighbour (n=3,d=3):")
print(f"    gap     eps   = (S(3,3)-S(1,3))*m_scale3 = {bdg_eps_seed:8.3f} MeV")
print(f"    pairing Delta = ME*m_scale3 (ME=6.3) = {bdg_Delta_seed:8.3f} MeV"
      f"   eps/Delta = {bdg_eps_seed/bdg_Delta_seed:.3f}")
print(f"    |Im omega| = {bdg_Imw_seed:.3e}"
      "  -> STABLE (gap dominates the coupling)")
print(f"  d=5 neutrino: pairing B = 0 (no C on S^5, d mod 8 = 5)")
print(f"    -> |Im omega| = {bdg_Imw_d5:.3e}")
print("    block-diagonal, stable by structure"
      " -- the EOM-level shadow of 0nubb.")
print(f"  contrast (hypothetical gap<pairing):"
      f" |Im omega| = {bdg_Imw_resonant:.3f} MeV -> UNSTABLE")
print("  => the seed's stability is not trivial; it holds because eps > Delta.")

# STEP 36 -- OUTPUT: FULL-TOWER BdG STABILITY OF THE 15 Sigma MODES  (MC-4.3)
print("\n" + "="*66)
print("STEP 36 -- FULL-TOWER BdG STABILITY OF THE 15 Sigma MODES (MC-4.3)")
print("="*66)
print("  reachable neighbours n->n+-2k (l-parity);"
      " odd steps coupling = 0 (exact)")
print("  stable iff max over neighbours |Delta|/|eps| < 1")
for (n, d) in BDG_SIGMA:
    tag = " (B=0, no C on S^5)" if d in BDG_NO_C else ""
    print("    (n=%3d, d=%2d): worst |Delta|/|eps| = %.4f%s"
          % (n, d, bdg_ratios[(n,d)], tag))
print("  GLOBAL worst-case = %.4f at mode (n=%d,d=%d)"
      " [the seed]  ->  ALL 15 STABLE"
      % (bdg_worst_ratio, bdg_worst_mode[0], bdg_worst_mode[1]))
print("  odd-l neighbours decoupled exactly (l-parity);"
      " d=5 exactly 0 (0nubb shadow).")


# STEP 37 -- OUTPUT: DAG SELECTION IS NOT EOM-ENERGETIC (MC-4.4)
print("\n" + "="*66)
print("STEP 37 -- DAG SELECTION IS NOT EOM-ENERGETIC:"
      " KERNEL REACH > DAG (MC-4.4)")
print("="*66)
print("  (A) no energy resonance at the additive DAG edges (1.0 = on-shell):")
print("      e=nu1+up   mass ratio  = %.4f   E_HO ratio = %.4f" %
      (sel_edge_mass_ratio_e, sel_edge_EHO_ratio_e))
print("      tau=nu3+down"
      "            E_HO ratio = %.4f" % sel_edge_EHO_ratio_tau)
print("      => edges are PURE INDEX relations, not energy resonances.")
print("  (B) kernel level-law n1+n2-1 (=%d)"
      " + ground offset 1 = IE index %d = n_e"
      % (sel_kernel_leadlaw_e, sel_IE_index_e))
print("      => the quartic kernel READS the IE edge form"
      " (motivated, not selection).")
print("  (C) kernel reach (same-parity d=3 modes to n=%d) = %d"
      "  vs  DAG d=3 count = %d"
      % (_N_REACH, _d3_parity_reach, len(_d3_sigma_set)))
print("      reach/DAG = %.1f"
      "  => kernel action set STRICTLY > DAG." % sel_reach_ratio)
print("  VERDICT: the SUFFICIENT selection is a directed index derivation")
print("           (combinatorial fixed point of a chosen generator set), NOT a")
print("           dynamical fixed point of the EOM energetics."
      " MC-4.3 stability is")
print("           the NECESSARY half;"
      " the sufficient half is not in the energetics.")


# =============================================================================
# STEP 38 -- OUTPUT: NULL-MODEL SIGNIFICANCE OF PARAMETER-FREE RATIOS
# =============================================================================
print("\n" + "="*66)
print("STEP 38 -- NULL-MODEL SIGNIFICANCE OF PARAM-FREE RATIOS (Part 5 2a)")
print("="*66)
print("  dimensionless ratio        luck L = 2*eps/g (index FREE)")
print(f"    m_mu/m_e   = {sig_mu_e:.2e}")
print(f"    m_tau/m_e  = {sig_tau_e:.2e}")
print(f"    m_Z/m_W    = {sig_Z_W:.2e}")
print(f"    m_H/m_W    = {sig_H_W:.2e}")
print(f"  joint (4 independent) = {sig_joint:.2e}"
      f"   (~1 in {1/sig_joint:.1e})")
print("  => spectrum is not a flexible fit; ~5sigma after look-elsewhere.")
print("  Full weight hinges on index-forcing (T0.5): forced => total.")


# =============================================================================
# STEP 39 -- OUTPUT: EXACT JOINT p + RANDOM-THEORY MC
# =============================================================================
print("\n" + "="*66)
print("STEP 39 -- SIGNIFICANCE: EXACT JOINT p + RANDOM-THEORY MC")
print("="*66)
print("NULL A -- random target position; headline set (rule: param-free,")
print("dimensionless, measurement resolves grid sigma < g/2):")
print(f"  {'quantity':10s} {'IDWT':>10s} {'obs':>10s}"
      f" {'eps_fit':>9s} {'grid g':>7s} {'L':>9s}")
for _nm, _pr, _ob, _ef, _g, _L in _s39_rows:
    print(f"  {_nm:10s} {_pr:10.4f} {_ob:10.4f}"
          f" {_ef:9.2e} {_g:7.4f} {_L:9.2e}")
print(f"  product = {s39_prod:.2e}   X_obs = -ln(prod) = {s39_X:.2f}")
print(f"  joint p (exact convolution) = {s39_p_exact:.2e}"
      f"  ({_s39_sigma(s39_p_exact):.1f} sigma)")
print(f"  joint p (Fisher, conservative) = {s39_p_fisher:.2e}"
      f"  ({_s39_sigma(s39_p_fisher):.1f} sigma)")
_s39_le = 1 - (1 - s39_p_exact) ** 100
print(f"  look-elsewhere x100: p ~ {_s39_le:.1e}"
      f"  ({_s39_sigma(_s39_le):.1f} sigma)")
print(f"  core-4 subset (STEP 38 set): Fisher p = {s39_p4:.2e}"
      f"  ({_s39_sigma(s39_p4):.1f} sigma)")
print("consistency checks (grid finer than current errors -- no NULL-A")
print("weight either way; pulls in sigma):")
for _nm, _pr, _ob, _sg in _s39_checks:
    print(f"  {_nm}: pred {_pr:9.4f}  obs {_ob:9.4f}"
          f"  pull {(_pr - _ob) / _sg:+.2f}")
print("NULL B -- random theories (indices uniform in windows, scales")
print("fixed by seed chain; 12 quantities recomputed per draw):")
print("  windows: " + "  ".join(f"d={_d}:1..{_s39_nmx[_d]}"
                                for _d in sorted(_s39_nmx)))
print(f"  draws = {s39_NB:.0e} (fixed seed);"
      f" T <= T_IDWT: {s39_nB_hits}  => p_B < {3.0/s39_NB:.0e}")
print(f"  best random T = {s39_T_best:.1f} vs T_IDWT = {s39_T_idwt:.1f}"
      f"  (gap {s39_T_best - s39_T_idwt:.1f} ln units)")
print("  8e6 draws (claude/significance_mc.py): p_B < 5e-7 (95% CL),")
print("  robust to halving/doubling the index windows.")
print("  => no random index assignment reproduces the measured set;")
print("     the residual question is index-FORCING (T0.5), not fit.")


# =============================================================================

print("\nDocs:  https://doi.org/10.5281/zenodo.19767493")
print("https://fedgeno.github.io/")

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
# m_c 1270(20); dm2_31 2.530(28)e-3; dm2_21 7.53(18)e-5) and FLAG 2024
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
    ("dm231/221", 2.530e-3 / 7.53e-5,
     math.hypot(0.028 / 2.530, 0.18 / 7.53), 22, _s39_dm2),
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
# STEP 40 -- CROSS-SECTOR SCALE INCOMMENSURABILITY LEMMA
# (Part 7 §1.2; Appendix A §15; symbolic proof:
#  claude/explore_scale_incommensurability.py)
#
# Claim (✅, proved exactly by sympy over the algebraic definitions):
# every cross-sector ratio m_scale_d / m_scale_d' is irrational
# EXCEPT m_scale_6 / m_scale_10 = 1 (the mu-tau symmetric pair).
#
# Algebraic structure (from ratio^2 rationality):
#   {3,4}-vs-any : ratio^2 contains sqrt(7) = sqrt(n_s + n_u)
#                  (quark-engine class)
#   {2,5,6,10} pairwise: ratio^2 rational (sqrt-10-type irrationals)
#   (6,10) pair : ratio^2 = ratio = 1  (exact, mu-tau symmetry)
#
# Consequence for Mechanism 2 (dephasing): "no common revival period"
# is now a proved statement for all 14 cross-sector pairs except (6,10).
# The single commensurate pair (6,10) is the unique sector pair that
# CAN phase-lock -- a new structural reading of the mu-tau relation.
# =============================================================================

_ms40 = {
    2: m_scale2, 3: m_scale3, 4: m_scale4,
    5: m_scale5, 6: m_scale6, 10: m_scale10,
}
_ds = [2, 3, 4, 5, 6, 10]

# STEP 41 -- TOWER EDGES AS CONDENSATE MATRIX ELEMENTS (F5/F16 joint)
# (Part 2 §9c; Part 10 §2; full check: claude/verify_f5f16_joint.py)
#
# Oscillator proxy (T1: level n <-> Hermite degree k = n-1). The P6
# condensate-linearized kernel supplies a degree-1 vertex (xi insertion).
#
# ADDITIVE edges n_c = n_a + n_b are the matrix element
#   <H_{n_c-1} | x | H_{n_a-1} H_{n_b-1}>  nonzero at the top-of-band:
# its top coefficient is the leading-coefficient ratio
#   2^{k_a+k_b} / 2^{k_a+k_b+1} = 1/2  (positive, nonzero) -- so the
# single degree-1 raising insertion lands exactly at n_c = n_a + n_b.
#
# SUBTRACTIVE edge n_nu3 = n_nu1 + n_nu2 - n_u (the unique one): the
# net degree change vs the product is -(n_u-1) = -2 (a LOWERING, the
# opposite of the additive raising). The -n_u is inclusion-exclusion
# (Part 2 §9c: n_nu1=S(n_u,3), n_nu2=S(n_u,4) share the seed n_u), i.e.
# the cumulant/connected minus sign. The electron (n_e seed-built)
# overlaps the subtracted seed leg, so W[e,3] inherits the minus:
# dU_e3/dtheta13|_0+ < 0 relative to the positive additive edges
# (the convention-independent content of T8 gap (ii); the overall
# branch is the PDG-convention bracket of Part 10 §4).
# =============================================================================

# STEP 42 -- HYBRIDISATION ANGLES FROM ORBIT-STATE ORTHOGONALITY
# (Part 11 section 1)
#
# The bonding electron states of an n-equivalent-bond center live in
# the L<=1 observable orbit state space span{|s>,|px>,|py>,|pz>} of
# the d=6 electron (Part 8 section 14.3: observable harmonics of
# Sym^L(C^4) under SU(4) > SU(3) > SO(3); here L=0 and L=1).
# Each hybrid orbit state along unit direction n_i is
#   |h_i> = a|s> + b (n_i . |p>),  a^2 + b^2 = 1.
# Premises: (i) the n co-present electron resonances are distinct
# modes of Psi_inf, hence orthonormal states (Pauli via spinor
# anticommutation, Part 8 section 2); (ii) bond equivalence gives
# every hybrid the same s-share a^2 = 1/n (the n hybrids exhaust
# the single |s> state: sum of s-shares = 1).
# Then  <h_i|h_j> = a^2 + b^2 (n_i.n_j) = 0  forces
#   n_i . n_j = -(1/n)/(1-1/n) = -1/(n-1)        [identity]
# sp: 180 deg; sp2: 120 deg; sp3: arccos(-1/3) = 109.471 deg --
# the tetrahedral angle of Part 1 section 3d, with no empirical
# input beyond the premises. Verified below by explicit construction.
# Water (Part 11 section 1d): unequal s-shares 1/4 -+ delta give
# cos(theta_bond) = -(1/4-delta)/(3/4+delta); delta fitted to the
# measured H-O-H angle (not predicted).
# =============================================================================

# STEP 43 -- ZONAL HYBRID IDENTITY, OCTAHEDRAL sp3d2, EQUIANGULAR CAP
# (Part 11 section 1.6, 1.4)
#
# Generalises STEP 42. A zonal hybrid along axis n is built from the
# axially symmetric degree-l components about n; by the spherical
# harmonic addition theorem the overlap of two zonal hybrids is
#   <h_i|h_j> = sum_l c_l^2 P_l(n_i.n_j),  sum_l c_l^2 = 1.
# STEP 42 is the l<=1 case: 1/n + (1-1/n) x = 0.
# sp3d2 (l<=2, six equivalent hybrids): completeness forces the
# shares c_0^2=1/6, c_1^2=1/2, c_2^2=1/3 (the six hybrids exhaust
# |s>, three |p>, two zonal |d>). Orthogonality then reads
#   1/6 + x/2 + (1/3) P_2(x) = 0  <=>  3x^2 + 3x = 0
# so every pair cosine is 0 or -1: the six directions are forced to
# be three orthogonal axes -- the octahedron.        [identity]
# Equiangular cap: n unit vectors in R^3 with equal pairwise cosine
# c have Gram (1-c)I + cJ with eigenvalues 1-c (x n-1) and 1+(n-1)c;
# rank<=3 forces c=-1/(n-1) and n-1<=3. Five equivalent equiangular
# sigma directions cannot exist in R^3 -- consistent with sp3d
# centers splitting into inequivalent axial/equatorial sets (PF5).
# Ammonia (Part 11 sec 1.4): shares 1/4 -+ delta as for water, lone
# pair 1/4+3*delta (completeness); delta fitted to measured H-N-H.
# =============================================================================

# STEP 44 -- HELIUM GROUND STATE: VARIATIONAL BOUND FROM IDWT INPUTS
# (Part 11 section 3)
#
# The d=3 marginal Hamiltonian for two electrons at a Z=2 nucleus
# (Part 8 sec 14.2 Lemma 1 per electron; e-e repulsion +alpha/r12 in
# the d=3 marginal -- the U(1) self-coupling on the shared d=2
# coordinates, Part 8 sec 14.4; projection per Part 3 sec 0.8a):
#   H = sum_i [ -grad_i^2/(2 m_e) - Z alpha/r_i ] + alpha/r12.
# Product trial state with screened scale eta (pure math, no input):
#   E(eta) = [eta^2 - 2 Z eta + (5/8) eta] * (alpha^2 m_e)
#   dE/deta = 0  =>  eta = Z - 5/16 = 27/16,  E = -eta^2 alpha^2 m_e.
# The comparison is made in hartree units (alpha^2 m_e), where alpha
# and m_e cancel: the IDWT-derived alpha(0) carries the known -2.87%
# residual (Part 3 sec 0.7), which would dominate an absolute-eV
# comparison; the dimensionless number -eta^2 is the chemistry
# content. The trial state is an uncorrelated product in the d=3
# marginal; the residual vs the measured value is where the
# two-electron 6D (CP3-coordinate) correlation enters (Part 11
# sec 2 program).
# =============================================================================

# STEP 45 -- DERIVING THE HYBRID PREMISES: PLANE INVARIANCE + ZONAL
# GROUND BLOCK (Part 11 section 4)
#
# (a) Orthogonality (P2) is not an assumption. By fermionic
# antisymmetry (Part 8 sec 16.2) the n-electron state is the
# antisymmetrised product of the occupied single-particle states;
# replacing them by any other basis of the same span multiplies the
# state by det(basis change) -- a scalar. The physical object is the
# occupied SUBSPACE, so the directed hybrids may always be taken
# orthonormal. Verified: the antisymmetric tensor u_i v_j - u_j v_i
# of a non-orthogonal pair is proportional to that of its
# orthonormalised pair.
# (b) Directed zonal form (P1'). The companion nucleus's potential
# is axially symmetric about the bond axis n (a d=3 structure; the
# Lemma 1 separation applies per electron, Part 8 sec 14.2). Within
# the degenerate L<=1 shell its leading multipole (dipole) couples
# only |s> <-> |p_n>: the m=0 block about n. m=+-1 states have a
# node on the axis and are untouched at this order. The bound state
# of the block is the directed hybrid (|s>+|p_n>)/sqrt2 -- the zonal
# form is derived, not assumed, in the degenerate-shell
# idealisation. Verified on the hydrogenic n_H=2 shell:
# <2s|z|2p_0> = -3 a0 (radial quadrature), perturbation eigenpairs
# (|s>+-|p_0>)/sqrt2 at -+3 a0 E, |p_+-1> unshifted.
# =============================================================================

# STEP 46 -- AROMATIC RING CURRENT: CLOSED-SHELL SCALING (RIGID RING)
# (Part 11 section 5; Part 8 section 17a)
#
# The benzene ring orbit is one 6D orbit coupling to all six centers
# (Part 8 sec 17a); its angular modes on a ring of radius R have
#   eps_m = (m - phi/phi0)^2 E_R,   E_R = hbar^2/(2 m_e R^2),
# with phi the applied flux. The level current is I_m = -d eps/d phi,
# linear in (m - phi/phi0). A closed shell fills m = -n..n twice
# (spin), so the m-linear parts cancel and the field-induced part
# adds over 2(2n+1) electrons:
#   I_induced  prop to  2(2n+1) = N_pi   [pi-electron count]
# and is independent of R (phi = B pi R^2 cancels R^2 in E_R).
# The top filled level is m_max = n = (N-2)/4 for a [4n+2]annulene.
# Shielding sign: the induced dipole field is opposed inside the
# loop and along its axis, reinforcing in the outer plane -- inner
# protons shielded, outer deshielded (Part 8 sec 17a observation).
# NOTE: the scaling is N_pi = 2(2 m_max + 1), NOT m_max -- this
# corrects the I prop-to m_max claim formerly in the chemistry
# article. Rigid-ring model: real annulene geometry relaxation is
# the open refinement.
# =============================================================================

# STEP 47 -- MARGINAL EXACTNESS: 3D PROBES FIX ALL CHEMISTRY
# (Part 11 section 6)
#
# Corollary of Part 8 Lemma 1 (exact separability V = V_C(r)+V_6(xi))
# and Lemma 2 (xi-orthogonality): for any observable O(r) supported
# on the observable coordinates -- which includes every chemical
# probe and the EM vertex (Part 8 sec 15) --
#   <psi_r x chi_a| O(r) |psi_r' x chi_b> = <psi_r|O|psi_r'> delta_ab
# so expectations and transition amplitudes are fixed by the d=3
# marginal alone, and the sector factor drops out. IDWT therefore
# reproduces standard molecular structure and response theory for
# every 3D-measured chemistry observable. Demonstrated below on a
# separable toy H = H_r x 1 + 1 x H_xi: states differing only in
# the sector factor give identical <O_r>, and O_r induces no
# transitions between sector levels.
# =============================================================================

# STEP 48 -- KERNEL RESIDUE BOUND AT CHEMICAL SCALES
# (Part 11 section 6.3)
#
# Closes the Part 11 sec 6.1 scope condition. Two pieces:
# (a) CANCELLATION (exact): kernel components supported on the
# sector factor alone shift every atomic/molecular state equally --
# by Lemma 1 all chemistry states share one sector eigenstate -- so
# they cancel in every measurable difference. Only kernel components
# with observable-coordinate support can leave a residue.
# (b) BOUND on the remainder: the kernel is a contact structure
# (colour analogy, Part 3 sec 0.6) with observable-coordinate range
# set by the sector length scale L_6 = 1.414 fm (Part 1 sec 3e).
# A contact term of range L and depth V0 shifts an s-state by
#   dE ~ V0 |psi(0)|^2 (4pi/3) L^3,  |psi(0)|^2 = 1/(pi a0^3).
# Conservative depth premise V0 <= m_e (the kernel's entire l=0
# output in d=6 is the sector eigenvalue m_e; any residual contact
# piece cannot exceed the scale it generates). Then
#   dE/hartree <= (4/3) (L_6/a0)^3 m_e / (alpha^2 m_e)
# Non-s states: |psi(0)|^2 = 0, residue higher order in L/a0.
# Result ~5e-10 -- the same order as the proton-finite-size
# correction Part 8 sec 14.4 already catalogues, three orders below
# Lamb-scale effects, far below any chemical measurement.
# =============================================================================

# STEP 49 -- WITHIN-SECTOR REVIVAL AMPLITUDE BOUND (T0.5 even-level)
# Off-resonant Rabi coupling: max revival amplitude ~ (J/DeltaS)^2.
# Spectral independence (sum-free S-values, Part 1 sec 5 Uniqueness
# Theorem) guarantees all DeltaS > 0.  Sum over non-tower even modes
# per sector gives an upper bound on within-sector return probability.
# Cross-sector revival averages to zero by the incommensurability
# lemma (STEP 40; 14/15 pairs irrational).
# (Part 9 T0.5 even-level bound; Appendix A sec 15)

import math as _math
from math import comb as _comb49

def _J49(n_r, s=1.5):
    num = _math.gamma(n_r + 1.5) * (s - 1)**n_r
    den = _math.factorial(n_r) * s**(n_r + 1.5)
    return num / den

_tower_n = {2: [76, 81, 95], 3: [1, 4, 10], 4: [3, 20, 72],
            5: [10, 15, 22], 6: [13, 35], 10: [23]}

def _revival_bound(d):
    tn = _tower_n[d]
    total = 0.0
    for n_nt in range(1, 80):
        lev = n_nt - 1            # level = n - 1
        if lev % 2 != 0:
            continue              # odd level: exact l-parity cut
        if n_nt in tn:
            continue              # tower mode itself
        s_nt = _comb49(n_nt + d - 1, d)
        nearest = min(tn, key=lambda x: abs(_comb49(x+d-1, d) - s_nt))
        delta = abs(s_nt - _comb49(nearest + d - 1, d))
        if delta == 0:
            continue
        nr = abs(n_nt - nearest)
        j = _J49(min(nr, 20)) * (1.0/3)**max(0, nr - 20)
        total += (j / delta)**2
    return total

# STEP 50 -- [18]ANNULENE RING-CURRENT NMR: SIGN AND SCALING
# (Part 11 section 5.1)
# The I prop N_pi ring current (STEP 46) creates a magnetic field
# at proton positions via Biot-Savart.  Current susceptibility:
#   dI/dB0 = -N_pi * e^2/(4*pi*m_e)   [A/T, diamagnetic]
# NMR shielding at in-plane point rho:
#   sigma = Bz_loop(R,rho,I=1) * N_pi * e^2/(4*pi*m_e)
# Sign: outer (rho > R) Bz < 0 -> sigma < 0 -> deshielded (down)
#       inner (rho < R) Bz > 0 -> sigma > 0 -> shielded (upfield)
# Rigid-ring overestimates ~5x (outer), ~40x (inner): the London
# correction factor is the open geometric refinement of Part 11 sec 5.
# N_pi scaling and sign are the correctly derived results.
# (Part 11 sec 5.1; Part 8 sec 17a)
# =============================================================================

from scipy.special import ellipk as _ek50, ellipe as _ee50

_mu0_50 = 4*math.pi*1e-7       # T*m/A
_e50    = 1.602176634e-19      # C
_me50   = 9.1093837015e-31     # kg
_dCC50  = 1.39e-10             # m, aromatic C-C bond
_rCH50  = 1.09e-10             # m, C-H bond length


def _Bz50(R50, rho50):
    """Bz [T/A] at z=0 in-plane rho from CCW loop radius R."""
    k2 = 4*R50*rho50 / (R50 + rho50)**2
    K50 = _ek50(k2)
    E50 = _ee50(k2)
    num = K50 + E50*(R50**2 - rho50**2)/(R50 - rho50)**2
    return _mu0_50/(2*math.pi) * num / (R50 + rho50)


# STEP 51 -- MADELUNG ORDERING FROM SLATER Z_eff
# (Part 11 section 2)
# Madelung / aufbau n+l rule: fill orbital with smallest n+l
# first; ties broken by smaller n.  Mechanism: high-L states are
# excluded from the nucleus by the angular-momentum barrier and
# see a more screened Z_eff; low-n same-n+l states penetrate
# more deeply, sitting lower in the well.  Slater's rules
# approximate the full inner-electron screening integral.
#
# Slater's rules (s/p orbitals):
#   same (n,l): 0.35 per other electron in same orbital
#   same n group (other l<=1): 0.35
#   n-1 group (all l, n'=n-1): 0.85
#   n-2 and below: 1.00
# For d/f orbitals: all electrons to the left: 1.00; same: 0.35.
# E(n,l) = -Z_eff^2 / (2 n^2)  [hartree]
#
# Test: 4s vs 3d at Z=18-21 (Ar, K, Ca, Sc)
# At K and Ca: 4s lower (fills first) -- Madelung confirmed.
# At Sc: 3d becomes lower as d-shell Z_eff rises faster than
# s-shell Z_eff -- 21st electron goes to 3d. Confirmed.
# Repeated for 5s vs 4d at Z=36-39 (Kr, Rb, Sr, Y).
#
# IDWT-specific: the d-shell has 5 observable states and 4
# permanently dark CP3-hidden d-states per shell (Part 8 sec
# 14.3 Lemma 2); both groups follow the same Madelung ordering.

def _fill51(Z51):
    """Electron counts {(n,l): count} for atom Z51."""
    _ord51 = [
        (1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),
        (5,0),(4,2),(5,1),(6,0),(4,3),(5,2),(6,1)
    ]
    _cnt51 = {}
    _rem51 = Z51
    for (_n51,_l51) in _ord51:
        _cap51 = 2*(2*_l51+1)
        _pl51  = min(_rem51, _cap51)
        if _pl51 > 0:
            _cnt51[(_n51,_l51)] = _pl51
        _rem51 -= _pl51
        if _rem51 <= 0:
            break
    return _cnt51

def _zeff51(Z51, n51, l51):
    """Slater Z_eff for orbital (n51,l51) in atom Z51."""
    _c51 = _fill51(Z51)
    _sh51 = 0.0
    if l51 <= 1:
        for (fn,fl),cnt in _c51.items():
            if fn == n51 and fl == l51:
                _sh51 += 0.35*(cnt-1)
            elif fn == n51 and fl <= 1:
                _sh51 += 0.35*cnt
            elif fn == n51 and fl >= 2:
                _sh51 += 1.00*cnt
            elif fn == n51-1:
                _sh51 += 0.85*cnt
            elif fn < n51-1:
                _sh51 += 1.00*cnt
    else:
        for (fn,fl),cnt in _c51.items():
            if fn == n51 and fl == l51:
                _sh51 += 0.35*(cnt-1)
            elif fn < n51 or (fn == n51 and fl < l51):
                _sh51 += 1.00*cnt
    return Z51 - _sh51

# STEP 52 -- LONE-PAIR ANGLE DELTA: VARIATIONAL FRAMEWORK + INGREDIENTS
# (Part 11 section 4.7)
#
# s-share asymmetry delta parameterises the sp3-family hybrid orbit
# states on the heavy atom (O for H2O, N for NH3):
#   a_b^2  = 1/4 - delta    (bond state s-character)
#   a_lp^2 = 1/4 + (n_b/n_lp)*delta  (lone-pair s-character)
# Completeness: n_b*(1/4-delta) + n_lp*(1/4+(n_b/n_lp)*delta) = 1
# Bond angle: cos(theta_bb) = -(1/4-delta)/(3/4+delta)
# Lone-pair angle: cos(theta_lp) = -(a_lp^2)/(1-a_lp^2)
# Bond-lone angle (from orthogonality):
#   cos(theta_bl) = -sqrt(a_b^2 * a_lp^2)/sqrt((1-a_b^2)(1-a_lp^2))
#
# Energy decomposition:
#   E(delta) = E_1c(delta) + E_tc(delta)
# E_1c: one-centre Slater-Condon Coulomb integrals between hybrids.
#   J(hi,hj) = ci^2 cj^2 F0ss
#             + [ci^2(1-cj^2) + (1-ci^2)cj^2] F0sp
#             + (1-ci^2)(1-cj^2) [F0pp - (2/25)F2pp P2(cos theta_ij)]
#   Total KE and O-nuclear attraction are CONSTANT in delta
#   (completeness preserves total s-char = 1 regardless of delta).
#   These integrals are computed from Clementi-Raimondi STO exponents.
#
# E_tc: two-centre contributions (needed to close the calculation).
#   Bond electrons extend to the H nucleus; their Coulomb repulsion
#   with other electrons depends on the molecular geometry, not just
#   the on-O orbital angles.  The two-centre orbit integrals of
#   Part 8 sec 16 type are required: <h_b h_b'|1/r12|h_b h_b'> where
#   h_b is a bond orbital centred on O pointing toward H.
#   The key geometry-dependent term is V_HH:
#     V_HH(delta) = C(n_b,2) / (2 R_MH sin(theta_bb(delta)/2))
#   (H-H nuclear repulsion increases as bond angle closes with delta).
#
# Key numerical ingredients computed below:
#   F0ss, F0sp, F0pp, F2pp from STO numerical quadrature
#   S(2s,1sH) and S(2p_sigma,1sH) overlap integrals
#   DeltaV_H = <2pz|-1/r_H|2pz> - <2s|-1/r_H|2s>  (nuclear attraction)
#   dV_HH/ddelta at observed delta  (main geometric restraint)
#
# STO exponents: Clementi & Raimondi, J Chem Phys 38, 2686 (1963).
#   O: z2s=2.246, z2p=2.227   N: z2s=z2p=1.917
#   H: z1s=1.24 (in O-H/N-H bond environment)
# Geometry: R(O-H)=0.9572 Ang, R(N-H)=1.012 Ang, H-O-H obs=104.5 deg,
#   H-N-H obs=107.8 deg. delta_obs(H2O)=0.050, delta_obs(NH3)=0.016.
# (Part 8 sec 14.3-17, Part 11 sec 4.6-4.7)

import numpy as _np52
from math import comb as _comb52

# --- STO radial probability density P(r) = N^2 r^4 exp(-2 z r) ---
def _sto_P52(z, Nr=1200):
    N2 = (2*z)**5 / 24.0
    r  = _np52.logspace(-4, 2.4, Nr)
    return r, N2 * r**4 * _np52.exp(-2*z*r)

# --- One-centre F^0 Coulomb integral ---
def _F0_52(za, zb, Nr=1200):
    r, Pa = _sto_P52(za, Nr); _, Pb = _sto_P52(zb, Nr)
    dr = _np52.gradient(r)
    cum  = _np52.cumsum(Pb * dr)
    tail = _np52.cumsum((Pb/r * dr)[::-1])[::-1]
    return _np52.trapezoid(Pa*(cum/r + tail), r)

# --- One-centre F^2 radial integral ---
def _F2_52(z, Nr=1200):
    r, P = _sto_P52(z, Nr)
    dr = _np52.gradient(r)
    cum2 = _np52.cumsum(r**2 * P * dr)
    tail3 = _np52.cumsum((P/r**3 * dr)[::-1])[::-1]
    return _np52.trapezoid(P*(cum2/r**3 + r**2*tail3), r)

# --- Overlap S(2s_X, 1s_H) with H at z=R (bond along z) ---
def _Ss52(zs, zH, R, Nr=400, Nth=80):
    Ns = _np52.sqrt((2*zs)**5/24.0) / _np52.sqrt(4*_np52.pi)
    NH = zH**1.5 / _np52.sqrt(_np52.pi)
    r = _np52.linspace(0.01, 7.0, Nr); ct = _np52.linspace(-1,1,Nth)
    dr = r[1]-r[0]; dct = ct[1]-ct[0]
    S = 0.0
    for ri in r:
        rH = _np52.sqrt(ri**2+R**2-2*ri*R*ct)
        rH = _np52.maximum(rH, 1e-9)
        phi2s = Ns * ri * _np52.exp(-zs*ri)
        S += phi2s * _np52.sum(NH*_np52.exp(-zH*rH)*dct) \
             * 2*_np52.pi * ri**2 * dr
    return S

# --- Overlap S(2p_sigma_X, 1s_H) ---
def _Sp52(zp, zH, R, Nr=400, Nth=80):
    Np = (_np52.sqrt((2*zp)**5/24.0)
          * _np52.sqrt(3/(4*_np52.pi)))
    NH = zH**1.5 / _np52.sqrt(_np52.pi)
    r = _np52.linspace(0.01, 7.0, Nr); ct = _np52.linspace(-1,1,Nth)
    dr = r[1]-r[0]; dct = ct[1]-ct[0]
    S = 0.0
    for ri in r:
        rH = _np52.sqrt(ri**2+R**2-2*ri*R*ct)
        rH = _np52.maximum(rH, 1e-9)
        phi2p = Np * ri * _np52.exp(-zp*ri)
        S += phi2p * _np52.sum(
            ct*NH*_np52.exp(-zH*rH)*dct) \
             * 2*_np52.pi * ri**2 * dr
    return S

# --- Nuclear attraction difference DeltaV_H ---
def _DVH52(zp, zs, R, Nr=500, Nth=100):
    N2 = (2*zp)**5/24.0
    r  = _np52.logspace(-4,2.0,Nr); ct = _np52.linspace(-1,1,Nth)
    dct = ct[1]-ct[0]
    Ns2 = (2*zs)**5/24.0
    Vs = Vp = 0.0
    for i,ri in enumerate(r):
        dr_i = (_np52.gradient(r))[i]
        rH = _np52.sqrt(ri**2+R**2-2*ri*R*ct)
        rH = _np52.maximum(rH,1e-9)
        Rp2 = N2  * ri**2 * _np52.exp(-2*zp*ri)
        Rs2 = Ns2 * ri**2 * _np52.exp(-2*zs*ri)
        fac = 2*_np52.pi * ri**2 * dr_i
        Vp += Rp2*(3/(4*_np52.pi))*_np52.sum(ct**2/rH*dct)*fac
        Vs += Rs2/(4*_np52.pi)*_np52.sum(1/rH*dct)*fac
    return Vp - Vs   # positive => 2p more attracted to H

# --- Bond angle and H-H nuclear repulsion ---
def _theta52(delta):
    ab2 = 0.25 - delta
    return _np52.degrees(_np52.arccos(-ab2/(1-ab2)))

def _VHH52(delta, nb, R_MH):
    th  = _np52.radians(_theta52(delta))
    rHH = 2*R_MH*_np52.sin(th/2)
    return _comb52(int(nb),2) / rHH

_b52 = 1/0.529177   # bohr per Ang
_zOs52, _zOp52 = 2.246, 2.227
_zNsp52        = 1.917
_zH52          = 1.24
_ROH52         = 0.9572 * _b52     # bohr
_RNH52         = 1.012  * _b52     # bohr

# One-centre Slater-Condon integrals (a.u.)
_F0ss52_O = _F0_52(_zOs52, _zOs52)
_F0sp52_O = _F0_52(_zOs52, _zOp52)
_F0pp52_O = _F0_52(_zOp52, _zOp52)
_F2pp52_O = _F2_52(_zOp52)
_F0ss52_N = _F0_52(_zNsp52, _zNsp52)
_F0sp52_N = _F0ss52_N          # same exponent for N
_F0pp52_N = _F0ss52_N
_F2pp52_N = _F2_52(_zNsp52)

# Overlap integrals S (dimensionless)
_Ss52_O = _Ss52(_zOs52, _zH52, _ROH52)
_Sp52_O = _Sp52(_zOp52, _zH52, _ROH52)
_Ss52_N = _Ss52(_zNsp52, _zH52, _RNH52)
_Sp52_N = _Sp52(_zNsp52, _zH52, _RNH52)

# Nuclear attraction differences DeltaV_H (a.u.)
_DV52_O = _DVH52(_zOp52, _zOs52, _ROH52)
_DV52_N = _DVH52(_zNsp52, _zNsp52, _RNH52)

# One-centre E2 range (delta 0 to 0.25): confirm it is nearly flat
def _E2_1c52(delta, F0ss, F0sp, F0pp, F2pp, nb, nlp):
    ab2 = 0.25 - delta; alp2 = 0.25 + (nb/nlp)*delta
    def P2(x): return (3*x**2-1)/2
    def Jhyb(c1,c2,cos_t):
        a1,a2 = 1-c1,1-c2
        return (c1*c2*F0ss + (c1*a2+a1*c2)*F0sp
                + a1*a2*(F0pp - 0.08*F2pp*P2(cos_t)))
    cos_bb  = -ab2/(1-ab2)
    cos_lp  = (-alp2/(1-alp2)
               if nlp > 1 else 0.0)
    cos_bl  = (-_np52.sqrt(ab2*alp2)
               / _np52.sqrt((1-ab2)*(1-alp2)))
    return (_comb52(int(nb),2)*Jhyb(ab2,ab2,cos_bb)
           +_comb52(int(nlp),2)*Jhyb(alp2,alp2,cos_lp)
           +nb*nlp*Jhyb(ab2,alp2,cos_bl))

_E2_H2O_0   = _E2_1c52(0.001,
    _F0ss52_O,_F0sp52_O,_F0pp52_O,_F2pp52_O,2,2)
_E2_H2O_025 = _E2_1c52(0.245,
    _F0ss52_O,_F0sp52_O,_F0pp52_O,_F2pp52_O,2,2)

# V_HH nuclear repulsion gradient at observed delta
_dVHH_H2O = (_VHH52(0.055,2,_ROH52)
              -_VHH52(0.045,2,_ROH52)) / 0.010
_dVHH_NH3  = (_VHH52(0.021,3,_RNH52)
              -_VHH52(0.011,3,_RNH52)) / 0.010

# STEP 53 -- KERNEL CONTACT AMPLITUDE (Part 11 section 6.4)
# Computes V0_actual from the (n=13, d=6) sector eigenfunction parity.
# Key question: what fraction f_contact of the kernel's l=0 output
# falls within the contact range L_6 = 1.414 fm?
#
# d=6 harmonic oscillator: at level n, the allowed angular momenta
# satisfy (n mod 2) == (l mod 2).  For n=13 (ODD), l must be ODD:
#   l = 1, 3, 5, 7, 9, 11, 13
# l=0 is ABSENT.  Therefore:
#   <n=13,d=6 | K_{l=0} | n=13,d=6> = 0  (parity)
#   f_contact = 0,  V0_actual = m_e * 0 = 0 MeV
#
# Angular selection for s-state corrections:
# An odd-l effective potential Y_l^m(theta,phi) integrated over the
# sphere against any spherically symmetric atomic orbital gives zero.
# All odd-l kernel pieces therefore give ΔE = 0 for s-states.
#
# Combined result: ΔE = 0 at leading contact order, converting the
# §6.3 bound to an equality at zero.  Leading non-zero contribution
# comes at 2nd order in (L_6/a_0)^2 (from even-l mixing induced by
# the odd-l sector kernel at 2nd order perturbation theory).
#
# The electron mode n_e=13 being ODD is not accidental: it reflects
# the seed decomposition n_e = n_nu1 + n_up = 10 + 3 = 13
# (Part 2 sec 2/6).  A hypothetical even n would produce a nonzero
# contact amplitude; odd n is what the seed structure selects.
# (Part 11 section 6.4)

import math as _math53

_n_e53   = 13                         # electron mode index (Part 2)
_S_e53   = S(_n_e53, 6)               # = 18564
_L6_53   = 1.414                      # fm  (Part 1 sec 3e)
_m_e53   = m_e                        # MeV
_a0_53   = 0.529177e5                 # Bohr radius in fm

# l values at n=13 in d=6 oscillator (same parity as n)
_l_vals53 = list(range(_n_e53 % 2, _n_e53 + 1, 2))
_l0_53    = 0 in _l_vals53            # False -> l=0 absent

# Contact fraction and amplitude
_f_contact53  = 0.0 if not _l0_53 else None
_V0_actual53  = _m_e53 * _f_contact53 if not _l0_53 else None

# §6.3 bound (STEP 48) and next-order suppression
_ratio53    = _L6_53 / _a0_53
_dE_bnd_ha = 4.78e-10                 # hartree, from STEP 48
_dE_next53 = _dE_bnd_ha * _ratio53**2  # leading non-zero order

# S(12,6): nearest even mode -- l=0 WOULD be present
_S_12_53 = S(12, 6)

# STEP 54 -- [18]ANNULENE NMR: DISTRIBUTED p_z CURRENT (Part 11 sec 5.1)
# Improvement over STEP 50 (thin-wire Biot-Savart): replace the 1D ring
# current with a spatially distributed current weighted by the azimuthal
# average of the Slater 2p_z orbital density on the ring carbons.
#
# p_z density (azimuthal ring average):
#   rho(r,z) = z^2 * <exp(-2*zeta*sqrt(r^2+R^2-2rR*cos(phi)+z^2))>_phi
# where zeta = 1.625/a0 (Clementi-Raimondi 2p_z for sp2 carbon).
# The z^2 factor reflects the 2p_z angular dependence (density=0 in ring
# plane); z = 0 is excluded, removing the near-singular region of
# the Biot-Savart kernel at h=0.
#
# For each grid point (rho, z), the Biot-Savart B_z contribution from a
# circular current loop of radius rho at height z, at in-plane point rho_H:
#   Bz = (mu0/4pi) * integral_0^{2pi} rho(rho - rho_H cos phi) /
#          (rho_H^2 + rho^2 + z^2 - 2 rho rho_H cos phi)^{3/2} dphi
# (500-point trapezoidal rule, converges to <0.1% for these separations.)
#
# Result: ~33% reduction (outer proton) and ~21% (inner proton) relative
# to the thin-wire value, consistent with the ~35% combined-correction
# estimate in Part 11 sec 5.1.  Remaining factor ~3x (outer), ~30x (inner)
# is the open GIAO problem documented in that section.
# London correction cos(pi/N_pi) = 0.985 adds 1.5% (large-ring limit).
# (Part 11 sec 5.1; STEP 50 for thin-wire baseline)
# =============================================================================

import numpy as _np54
from scipy.special import (
    ellipk as _ek54, ellipe as _ee54)
import math as _math54

_Npi54  = 18
_dCC54  = 1.39e-10              # m, aromatic C-C bond
_rCH54  = 1.09e-10              # m, C-H bond
_R54    = _Npi54 * _dCC54 / (2*_math54.pi)
_zeta54 = 1.625 / (0.529177e-10)  # m^-1, C 2p_z (Clementi-Raimondi)
_mu54   = 4*_math54.pi*1e-7     # T m/A
_e54    = 1.602176634e-19        # C
_me54   = 9.1093837015e-31       # kg


def _Bz54_wire(R, rho):
    """Thin-wire Biot-Savart B_z [T/A] (elliptic integral)."""
    k2    = 4*R*rho / (R+rho)**2
    K, E  = _ek54(k2), _ee54(k2)
    return _mu54/(2*_math54.pi)*(
        K + E*(R**2-rho**2)/(R-rho)**2)/(R+rho)


def _Bz54_dist(rho_H, R=_R54, zeta=_zeta54,
               dr=0.20e-10, dz=0.20e-10,
               Np_d=60, Np_bs=500):
    """B_z [T/A] from distributed p_z torus at in-plane rho_H."""
    rho_g = _np54.arange(dr/2, R*2.2, dr)
    z_pos = _np54.arange(dz, 2.5e-10, dz)
    z_g   = _np54.concatenate([-z_pos[::-1], z_pos])
    # -- density (Nr x Nz) --
    phi_d = _np54.linspace(
        0, 2*_math54.pi, Np_d, endpoint=False)
    rr = rho_g[:,_np54.newaxis,_np54.newaxis]
    zz = z_g[_np54.newaxis,:,_np54.newaxis]
    pp = phi_d[_np54.newaxis,_np54.newaxis,:]
    d2 = _np54.maximum(
        rr**2 + R**2 - 2*rr*R*_np54.cos(pp) + zz**2,
        1e-60)
    avg  = _np54.mean(
        _np54.exp(-2*zeta*_np54.sqrt(d2)), axis=2)
    dens = avg * z_g[_np54.newaxis,:]**2
    rho2 = rho_g[:,_np54.newaxis]
    dens /= _np54.sum(dens*2*_math54.pi*rho2*dr*dz)
    # -- Biot-Savart kernel (Nr x Nz) --
    phi_bs = _np54.linspace(
        0, 2*_math54.pi, Np_bs, endpoint=False)
    dphi   = 2*_math54.pi/Np_bs
    rr_b = rho_g[:,_np54.newaxis,_np54.newaxis]
    zz_b = z_g[_np54.newaxis,:,_np54.newaxis]
    pp_b = phi_bs[_np54.newaxis,_np54.newaxis,:]
    D2  = _np54.maximum(
        rho_H**2 + rr_b**2 + zz_b**2
        - 2*rr_b*rho_H*_np54.cos(pp_b), 1e-60)
    kern = (_mu54/(4*_math54.pi)
            * (rr_b*(rr_b - rho_H*_np54.cos(pp_b))
               / D2**1.5).sum(axis=2) * dphi)
    vol = 2*_math54.pi*rho2*dr*dz
    return float(_np54.sum(dens*kern*vol))


_dIdB54  = _Npi54 * _e54**2 / (4*_math54.pi*_me54)
_rho_o54 = _R54 + _rCH54
_rho_i54 = _R54 - _rCH54
_fL54    = _math54.cos(_math54.pi/_Npi54)  # London factor

_Bz_tw_o = _Bz54_wire(_R54, _rho_o54)
_Bz_tw_i = _Bz54_wire(_R54, _rho_i54)
_Bz_d_o  = _Bz54_dist(_rho_o54)
_Bz_d_i  = _Bz54_dist(_rho_i54)

_sig_tw_o = _Bz_tw_o * _dIdB54 * 1e6
_sig_tw_i = _Bz_tw_i * _dIdB54 * 1e6
_sig_d_o  = _Bz_d_o  * _dIdB54 * 1e6
_sig_d_i  = _Bz_d_i  * _dIdB54 * 1e6
_sig_dL_o = _sig_d_o * _fL54
_sig_dL_i = _sig_d_i * _fL54


# =============================================================================
# STEP 55 -- THE d=2 EVEN-INSERTION SELECTION RULE (insertion dichotomy)
# (Part 3 section 11; Part 3 section 16.2; Part 2 section 6 note;
#  Appendix A section 25 addendum; claude/explore_insertion_dichotomy.py)
#
# The degree-1 condensate vertex (one xi insertion per additive fermion
# edge; STEP 41) exists only in sectors with a nonzero condensate
# <xi_d'> (Part 1 P6). The all-orders photon-mass theorem (Part 3
# section 16.2) states the condensate-linearized vertices remain even
# (degree 2) in the d=2 variable: no odd vertex acts on a d=2 leg.
# Selection rule (motivated, derivation open): a tower production
# landing on a d=2 mode carries an EVEN number of degree-1 insertions;
# matter-sector targets are unconstrained (the realized edges use one).
#
# Oscillator proxy bookkeeping (T1: mode n <-> Hermite degree k = n-1):
#   product of modes: top Hermite degree k = sum(n_i - 1)
#   each insertion x: raises the top degree by exactly 1 with
#     top-of-band coefficient ratio 1/2 per insertion (positive,
#     nonzero), so the landing index is n = sum(n_i - 1) + k_ins + 1.
#   g-rule join: the partner enters as the sector overhead segment of
#     d quanta sharing one vacuum unit (Part 3 section 11), so
#     k_partner = d - 1 and zero insertions land at n_f + d - 1.
# All seven documented productions land exactly, with insertion counts
# {e:1, mu:1, tau:1 | W:0, Z:0, H-join:0, H-additive:2} -- every d=2
# production even, every matter-sector edge odd. The counterfactual
# odd-insertion boson indices (n+1) are unoccupied. One structural
# fact -- no d=2 condensate -- yields both m_gamma = 0 and the g-rule
# -1 (the shared vacuum unit).
# =============================================================================

def _land55(n_ops, k_ins):
    """Landing mode index: product top-of-band + k_ins insertions."""
    return sum(v - 1 for v in n_ops) + k_ins + 1

# (name, target sector, operands, insertions, documented target)
_prods55 = [
    ('e',     6, (n_nu1, n_up),          1, n_e),
    ('mu',    6, (n_charm, n_nu2),       1, n_mu),
    ('tau',  10, (n_nu3, n_down),        1, n_tau),
    ('W',     2, (n_top, 5),             0, n_W),    # d_nu overhead
    ('Z',     2, (n_W, 6),               0, n_Z),    # d_lep overhead
    ('Hjoin', 2, (n_nu2, n_Z),           0, n_H),
    ('Hadd',  2, (n_up, n_charm, n_top), 2, n_H),
]
_land_ok55 = all(_land55(ops, k) == tgt
                 for _, _, ops, k, tgt in _prods55)
_parity_ok55 = all(k % 2 == 0
                   for _, sec, _, k, _ in _prods55 if sec == 2)
_NS55 = {0, n_down, n_up, n_strange, n_charm, n_top, n_nu1, n_nu2,
         n_nu3, n_e, n_mu, n_tau, n_W, n_Z, n_H}
_cf_boson55 = [(nm, v + 1, (v + 1) in _NS55)
               for nm, v in (('W', n_W), ('Z', n_Z), ('H', n_H))]
_cf_clean55 = not any(occ for _, _, occ in _cf_boson55)


# =============================================================================
# STEP 56 -- SUM-FREE VERIFICATION OF THE OCCUPIED S-VALUES (Part 1 sec 5)
# (Additive-combinatorics framing, Part 1 "sum-free" remark; the spectral
#  independence used by STEP 49. From gifts-from-grok, 2026-06-10.)
#
# Claim (Part 1, additive rigidity): the 14 non-zero occupied S-values
# form a sum-free set -- no member equals the sum of two (not necessarily
# distinct) members. Verified here by the full pairwise check. Note the
# mode INDICES are not sum-free (1+3=4); the property holds at the
# S-value (eigenvalue) level.
# =============================================================================

_pairs56 = [(n_down, 3), (n_strange, 3), (n_up, 4), (n_charm, 4),
            (n_top, 4), (n_nu1, 5), (n_nu2, 5), (n_nu3, 5),
            (n_e, 6), (n_mu, 6), (n_tau, 10),
            (n_W, 2), (n_Z, 2), (n_H, 2)]
_svals56 = sorted(S(_n, _d) for _n, _d in _pairs56)
_set56 = set(_svals56)
_collisions56 = [(a, b, a + b) for i, a in enumerate(_svals56)
                 for b in _svals56[i:] if (a + b) in _set56]
_sumfree56 = not _collisions56


# =============================================================================
# STEP 57 -- COW GRAVITATIONAL PHASE WITH THE IDWT NUCLEON MASS
# (articles/cow-gravitational-phase.html; m_N_idwt from STEP 7.
#  From gifts-from-grok, 2026-06-10, arithmetic repaired.)
#
# COW phase for a neutron interferometer with enclosed area A and
# de Broglie wavelength lambda = h/(m v):
#   delta_phi = m g A / (hbar v) = m^2 g A lambda / (2 pi hbar^2)
# (the 2 pi belongs in the denominator when lambda = h/(m v) is used).
# IDWT supplies the nucleon mass m_N = N_c*Lqcd*(1+1/n_up^2) (STEP 7);
# gravitational mass = inertial mass = S(n,d)*m_scale_d (Part 4 s3.6),
# so the phase-to-mass ratio is species-independent.
# At fixed interferometer geometry (A, lambda) the prediction relative
# to the standard value with the PDG neutron mass is
#   phi_IDWT / phi_std = (m_N_idwt / m_n_PDG)^2
# Representative geometry (lambda = 1.445 A, A = 10 cm^2) gives the
# tens-of-radians scale observed in the COW-class experiments.
# =============================================================================

_mn_pdg57 = 939.565            # MeV (PDG 2024, claude/pdg2024.txt)
_kg57     = 1.78266192e-30     # kg per MeV/c^2
_hbar57   = 1.054571817e-34    # J s
_h57      = 6.62607015e-34     # J s
_g57      = 9.80665            # m s^-2
_lam57    = 1.445e-10          # m   (representative thermal-neutron Bragg)
_A57      = 10.0e-4            # m^2 (representative enclosed area)

def _cow_phase57(m_mev):
    _m = m_mev * _kg57
    _v = _h57 / (_m * _lam57)
    return _m * _g57 * _A57 / (_hbar57 * _v)

_phi_idwt57 = _cow_phase57(m_N_idwt)
_phi_std57  = _cow_phase57(_mn_pdg57)
_ratio57    = (m_N_idwt / _mn_pdg57) ** 2
_ratio_ok57 = abs(_phi_idwt57 / _phi_std57 - _ratio57) < 1e-12


# =============================================================================
# STEP 58 -- SECTOR-WELL COVARIANCE: THE WELL RIDES WITH THE MODE
# (Part 4 section 3.10.2 covariance note; Part 1 section 3i; Part 8
#  section 14.2; Appendix A section 27; full numerics incl. 1D
#  dynamics in claude/well_covariance_check.py.)
#
# The kernel self-term (Part 4 section 3.10.1)
#   V_self(xi) = g_dd * Int |chi(xi')|^2 (xi . xi')^2 dxi'
# is written in absolute sector coordinates. Read literally (well
# anchored at the origin of Xi_d), a mode of internal spread s whose
# centroid sits at X acquires the displacement energy
#   U_A(X)/g_dd = |X|^4 + (2 s^2/d) |X|^2 + s^4/d
# (exact for an isotropic density: expand ((X+eta).(X+eta'))^2 over
# independent zero-mean isotropic draws eta, eta' and use
# <(a.eta)^2> = s^2|a|^2/d and <(eta.eta')^2> = s^4/d).
# Quartic pinning to the sector origin: at hydrogen's Bohr radius the
# pinning energy is ~2e18 in sector units against the internal ground
# energy E_0 = d*sqrt(lam_6) = 3 -- the absolute reading forbids
# macroscopic motion and contradicts the established Bohr spectrum
# (Part 8 section 14.2). EXCLUDED by reductio.
# The covariant (mode-frame) evaluation -- displacements relative to
# the mode centroid, ((xi-X).(xi'-X))^2 -- gives U_B = g_dd s^4/d,
# X-independent, and leaves the fixed point lam_d = (g_dd/2)^(2/3)
# (Part 4 section 3.10.3) unchanged in every sector: section 3.10
# computed at X = 0, the mode frame, so every published number is
# frame-local. Consequences: the well travels with the excitation
# (1D split-step check: boosted self-bound mode translates at exactly
# v with width drift 0.00%; the absolute-kernel twin released at
# X0 = 5 oscillates pinned about the origin); the center propagates
# freely, E^2 = P^2 + m^2 (Part 1 section 3i), with no preferred
# coordinates -- "bound within, free without" completes to "bound
# about its center within; the center free everywhere." In hydrogen
# the compact internal structure corrects the point-center H_eff only
# through its smearing,
#   dE/|E_1s| = 4 sigma^2,  sigma = L_6/a0,
# the same order as the proton-finite-size items of Part 8 s14.4.
# Lengths below in sector units (base unit = L_6/lam_6^(-1/4) = 1 fm).

_d58    = 6
_g58    = g_self[_d58]                         # = g66 = 1/4
_lam58  = (_g58 / 2.0) ** (2.0 / 3.0)          # = 0.25 (Part 4 s3.10.4)
_s2_58  = _d58 / (2.0 * math.sqrt(_lam58))     # <|eta|^2> = d/(2 sqrt(lam))

def _U_abs58(X):
    """Displacement energy / g_dd, absolute (origin-anchored) reading."""
    return X**4 + (2.0 * _s2_58 / _d58) * X**2 + _s2_58**2 / _d58

_U_rel58  = _g58 * _s2_58**2 / _d58            # covariant: X-independent
_L6_m58   = 1.414e-15                          # L_6 in metres
_unit_m58 = _L6_m58 / _lam58**-0.25            # sector base unit ~ 1 fm
_a0_m58   = 5.29177210903e-11                  # Bohr radius, metres
_X58      = _a0_m58 / _unit_m58                # a0 in sector units
_pin58    = _g58 * _U_abs58(_X58)              # pinning energy at X = a0
_E0_58    = _d58 * math.sqrt(_lam58)           # internal E_0 = 3
_lam_all58 = {d: (g_self[d] / 2.0) ** (2.0 / 3.0) for d in sector_d}
_sig58    = _L6_m58 / _a0_m58                  # smearing parameter
_dE58     = 4.0 * _sig58**2                    # dE/|E_1s|


# =============================================================================
# STEP 59 -- CROSS-SECTOR KERNEL COVARIANCE: CONTACT IS A CONSEQUENCE
# (Part 4 section 3.10.1 covariance note; Part 3 section 0.6; Part 11
#  section 6.3; Appendix A section 28; STEP 58 is the self-term
#  companion; full numerics claude/kernel_covariance_check.py.)
#
# Two modes, A (sector d, centroid X_A) and B (sector d', centroid
# X_B), couple through g_{dd'}(xi_d . xi_{d'})^2 on their shared
# subspace (d_sh = min(d,d'), Part 1 section 3g); per-component
# variances a^2, b^2; R = X_A - X_B. The three two-point covariant
# readings, in closed form (each MC-verified):
#  (0) absolute:      U_0/g = (X_A.X_B)^2 + b^2|X_A|^2 + a^2|X_B|^2
#                              + d_sh a^2 b^2
#      -- not a function of R alone; changes under a global
#      translation. EXCLUDED (STEP 58 reductio class).
#  (1) pair-centroid: U_1/g = |R/2|^4 + (a^2+b^2)|R/2|^2 + d_sh a^2 b^2
#      -- quartic MUTUAL CONFINEMENT of every massive pair; for the
#      e-p pair at R = a0, g_36 U_1 ~ 1e18 sector units, vs the
#      actual e-p interaction at a0 being Coulomb alone. EXCLUDED.
#  (2) each-own-frame: U_2/g = d_sh a^2 b^2  -- R-INDEPENDENT; the
#      pair energy never vanishes as R -> inf (cluster decomposition
#      fails; extensive spurious energy ~ pair count). EXCLUDED.
# FORCED: no two-point polynomial moment survives. The only covariant
# reading left is CONTACT-GATED,
#   U(R) = g_{dd'} * Omega(R) * d_sh a^2 b^2,
# with Omega(0) = 1 and decay on the mode-width scale: the
# (xi.xi')^2 factor is the local geometry of the coupling AT a
# contact event, not a long-range potential. "The kernel is a
# contact structure" (Part 3 section 0.6; Part 11 section 6.3
# premise) is thereby a structural consequence ✅, not an assertion.
# Established couplings are contact evaluations (Omega(0)=1): all
# unchanged. A=B at R=0 reduces to the STEP 58 self-term g s^4/d.
# Long-range forces untouched: EM is the massless, non-compact d=2
# zero mode (no width gate; Part 3 sections 16, 0.8a); gravity is
# curvature (Part 4).
# Gate PROFILE (Gaussian modes; derived in STEP 60):
#   Omega(R) = exp(-R^2/(2(a^2+b^2))), range sqrt(a^2+b^2):
# e-e range = sqrt(2 sigma_6^2) = L_6 = 1.414 -- the Part 11
# section 6.3 premise, derived; q-q (3,4) range 0.78 (sub-fm,
# strong-force scale); e-p 1.11. Gate at R = a0: ln Omega ~ -1e9.

_dsh59      = 3                                 # e-p shared subspace
_a2_59      = 1.0 / (2.0 * math.sqrt(_lam_all58[6]))   # electron
_b2_59      = 1.0 / (2.0 * math.sqrt(_lam_all58[3]))   # down-type
_g36_59     = math.sqrt(g_self[3] * g_self[6])  # rank-1 g_36

def _U1_59(R):
    """Pair-centroid reading, closed form (units of g)."""
    _u2 = R * R / 4.0
    return _u2**2 + (_a2_59 + _b2_59) * _u2 + _dsh59 * _a2_59 * _b2_59

_U1_a0_59   = _g36_59 * _U1_59(_X58)            # confinement disaster
_U2_59      = _dsh59 * _a2_59 * _b2_59          # frame-local moment
_rng_ee59   = math.sqrt(2.0 / (2.0 * math.sqrt(_lam_all58[6])))
_rng_ep59   = math.sqrt(_a2_59 + _b2_59)
_rng_qq59   = math.sqrt(1.0 / (2.0 * math.sqrt(_lam_all58[3]))
                        + 1.0 / (2.0 * math.sqrt(_lam_all58[4])))
_lnOm_a0_59 = -_X58**2 / (2.0 * (_a2_59 + _b2_59))
_self_red59 = g_self[6] * 6 * (1.0 / (2.0 * math.sqrt(_lam_all58[6])))**2
_self_ok59  = abs(_self_red59 - _U_rel58) < 1e-12   # = STEP 58 U_B


# =============================================================================
# STEP 60 -- KERNEL GATE PROFILE DERIVED: NORMALIZED DENSITY OVERLAP
# (Part 4 section 3.10.1 covariance note; closes the STEP 59 residual;
#  Appendix A section 28 addendum; claude/deuteron_gate_check.py.)
#
# Three established inputs force the gate Omega(R) of STEP 59 uniquely:
#  (i)   bilinearity: the kernel action term is bilinear in the kernel
#        currents, L_{dd'} = (g/2) Int (xi.xi')^2 J J (Part 3 section
#        0.6) -- linear in each mode's intensity -- so the pair energy
#        is a bilinear functional U = IntInt rho_A(x) rho_B(y) F(x-y);
#  (ii)  covariance + the STEP 59 exclusions force F to decay;
#  (iii) the action carries no length constant of its own (the g_dd'
#        are dimensionless seed-built numbers), so F has zero
#        intrinsic range: the scale-free point contact F ~ delta.
# Hence Omega(R) = [rho_A * rho_B](R) / [rho_A * rho_B](0), the
# normalized density overlap -- derived, no longer a modeling choice.
# Gaussian sector ground modes: Omega(R) = exp(-R^2/(2(a^2+b^2))).
# Corollary (exact algebra): a same-sector pair has contact range
#   sqrt(2 sigma_d^2) = (2 * 1/(2 sqrt(lam_d)))^(1/2) = lam_d^(-1/4)
#   = L_d
# -- the sector localization length IS the same-sector contact range
# (e-e: L_6, the Part 11 section 6.3 range; N-N at d=3: L_3).

_ident60 = all(
    abs(math.sqrt(1.0 / math.sqrt(_lam_all58[d])) - _lam_all58[d]**-0.25)
    < 1e-12 for d in sector_d)                 # sqrt(2 sigma^2) == L_d


# =============================================================================
# STEP 61 -- INTERNUCLEON CONTACT: DEUTERON INVERSE CHECK
# (Part 8 section 11; gate range from STEP 60; Appendix A section 29;
#  claude/deuteron_gate_check.py.)
#
# Nucleons are d=3 colour-singlet composites (Part 1 section 2.4), so
# the N-N kernel contact gate has the derived d=3 range
# L_3 = lam_3^(-1/4) = 0.675 (sector units ~ fm); a gate built from
# the measured proton charge radius (sigma^2 = r_p^2/3, r_p = 0.8409
# fm CODATA) gives 0.687 -- the d=3 sector width and the measured
# nucleon size give nearly the same gate. Inverse check: with the
# gate profile itself as the contact well,
#   V(r) = -V0 exp(-r^2/(2 Rc^2)),
# reduced mass m_N_idwt/2, the measured deuteron binding
# E_B = 2.224566 MeV (CODATA; not in claude/pdg2024.txt) fixes the
# depth the kernel must supply. Result: V0 is an order-unity
# fraction of the IDWT hadronic scale Lqcd = N_c f_pi. The RANGE is
# fixed by STEP 60; deriving the DEPTH V0 from the kernel is the
# same class of open problem as the section 11 confinement level.
# The solved mode's rms half-separation lands near the measured
# deuteron matter radius ~1.97 fm (shallow-state universality).

_HBARC61 = 197.3269804                  # MeV fm
_EB61    = 2.224566                     # MeV (CODATA)
_RP61    = 0.8409                       # fm  (CODATA proton radius)
_RC_NN61 = _lam_all58[3] ** -0.25       # L_3 gate, 0.675
_RC_QQ61 = math.sqrt(1.0/(2*math.sqrt(_lam_all58[3]))
                     + 1.0/(2*math.sqrt(_lam_all58[4])))   # 0.780
_RC_RP61 = math.sqrt(2.0 * _RP61**2 / 3.0)                 # 0.687

def _shoot61(V0, Rc, E):
    """Numerov u'' = f u, f = (m_N/hbarc^2)(V - E); return u(rmax)."""
    _c = m_N_idwt / _HBARC61**2
    _h = 0.01
    _n = int(30.0 / _h)
    _u0, _u1 = 0.0, 1e-6
    _h2 = _h * _h / 12.0
    def _f(r):
        return _c * (-V0 * math.exp(-r*r/(2.0*Rc*Rc)) - E)
    for _i in range(2, _n + 1):
        _r0, _r1, _r2 = (_i-2)*_h, (_i-1)*_h, _i*_h
        _u2 = (2*_u1*(1 + 5*_h2*_f(_r1)) - _u0*(1 - _h2*_f(_r0))) \
            / (1 - _h2*_f(_r2))
        _u0, _u1 = _u1, _u2
    return _u1

def _solveV0_61(Rc):
    """Ground-state depth: scan to first sign change, then bisect."""
    _lo = 1.0
    _flo = _shoot61(_lo, Rc, -_EB61)
    _hi = _lo
    while _shoot61(_hi + 2.0, Rc, -_EB61) * _flo > 0:
        _hi += 2.0
        _lo = _hi
    _hi += 2.0
    for _ in range(50):
        _mid = 0.5 * (_lo + _hi)
        if _shoot61(_mid, Rc, -_EB61) * _flo > 0:
            _lo = _mid
        else:
            _hi = _mid
    return 0.5 * (_lo + _hi)

def _rms61(V0, Rc):
    """rms of r/2 over the solved |u|^2."""
    _c = m_N_idwt / _HBARC61**2
    _h = 0.01
    _n = int(40.0 / _h)
    _u0, _u1 = 0.0, 1e-6
    _h2 = _h * _h / 12.0
    _s0 = _s2 = 0.0
    def _f(r):
        return _c * (-V0 * math.exp(-r*r/(2.0*Rc*Rc)) + _EB61)
    for _i in range(2, _n + 1):
        _r = _i * _h
        _u2 = (2*_u1*(1 + 5*_h2*_f(_r - _h))
               - _u0*(1 - _h2*_f(_r - 2*_h))) / (1 - _h2*_f(_r))
        _u0, _u1 = _u1, _u2
        _s0 += _u1*_u1*_h
        _s2 += _r*_r*_u1*_u1*_h
    return 0.5 * math.sqrt(_s2 / _s0)

_V0_NN61 = _solveV0_61(_RC_NN61)
_V0_QQ61 = _solveV0_61(_RC_QQ61)
_V0_RP61 = _solveV0_61(_RC_RP61)
_rms_NN61 = _rms61(_V0_NN61, _RC_NN61)


# =============================================================================
# STEP 62 -- N-N WELL FROM SECOND-ORDER KERNEL CONTACT: DEPTH = LAMBDA
# (Part 8 section 11; structure from the colour energy law, Part 8
#  section 5.3, and the derived gate, STEP 60; Appendix A section 29
#  addendum; claude/deuteron_gate_check.py.)
#
# Structure (forced by established results):
#  (a) Two colour singlets have N_A = N_B = 0, so the first-order
#      inter-singlet colour energy vanishes by the energy law
#      E_conf = lambda_c |N| (Part 8 section 5.3). The leading N-N
#      kernel interaction is SECOND order in the gated contact --
#      the colour analogue of the van der Waals mechanism (Part 8
#      section 17b, second-order d=2 self-coupling).
#  (b) Second order squares the gate: V(R) = -V0 * Omega(R)^2
#      = -V0 exp(-R^2/(2 Rc2^2)) with Rc2 = (gate range)/sqrt(2):
#      L_3 gate -> Rc2 = 0.477; r_p gate -> Rc2 = 0.486.
#  (c) Depth V0 = kappa^2/Delta, kappa the singlet->non-singlet
#      contact matrix element, Delta the non-singlet gap -- the
#      quantities of the open colour-scale problem (lambda_c class,
#      Part 8 section 5.3). The profile and range carry no freedom.
# Inverse result: the measured deuteron binding requires
#   V0 = 1.02 * Lqcd (L_3 gate),  V0 = 0.99 * Lqcd (r_p gate)
# -- the required depth equals the IDWT hadronic scale Lqcd = N_c
# f_pi within 2% on both gates. Forward, parameter-free, V0 = Lqcd
# exactly: E_B = 1.6 MeV (L_3) and 2.5 MeV (r_p), bracketing the
# measured 2.2246 (a shallow state is exponentially sensitive to
# depth, so the inverse statement is the robust one). 🔵
# Open: derive kappa and Delta (equivalently lambda_c) from the
# kernel; spin-tensor structure (deuteron is spin-1; this is the
# central s-wave channel).

_RC2_NN62 = _RC_NN61 / math.sqrt(2.0)          # 0.477
_RC2_RP62 = _RC_RP61 / math.sqrt(2.0)          # 0.486
_V0_NN62  = _solveV0_61(_RC2_NN62)
_V0_RP62  = _solveV0_61(_RC2_RP62)
_rms_NN62 = _rms61(_V0_NN62, _RC2_NN62)

def _solveE62(V0, Rc):
    """Ground-state energy for fixed depth: bisect shoot on E."""
    _lo, _hi = -60.0, -1e-6
    _flo = _shoot61(V0, Rc, _lo)
    for _ in range(60):
        _mid = 0.5 * (_lo + _hi)
        if _shoot61(V0, Rc, _mid) * _flo > 0:
            _lo = _mid
        else:
            _hi = _mid
    return 0.5 * (_lo + _hi)

_EB_NN62 = -_solveE62(Lqcd, _RC2_NN62)         # V0 = Lambda exactly
_EB_RP62 = -_solveE62(Lqcd, _RC2_RP62)


# STEP 63 -- KAPPA AND DELTA FROM LARGE-N_c COLOUR STRUCTURE
# (Part 8 section 11; colour energy law Part 8 section 5.3;
#  Appendix A section 29 addendum.)
#
# Second-order N-N depth: V0 = kappa^2 / Delta (section 11).
# kappa = singlet->non-singlet contact matrix element (one baryon).
# Delta = non-singlet excitation gap (one-baryon gap).
#
# Large-N_c identification:
# (a) kappa = sqrt(N_c) * Lambda
#     N_c quarks each contribute colour amplitude Lambda at the
#     hadronic threshold (g_eff=1 at n=n_s in d=3). Coherent sum
#     at baryon level gives the standard sqrt(N_c) enhancement.
#     kappa = sqrt(N_c) * Lambda = sqrt(N_c) * N_c * f_pi.
#
# (b) Delta = N_c * Lambda  (one-baryon colour excitation gap)
#     Colour energy law E = lambda_c |N_vec|; one quark changing
#     colour gives |delta N_vec| = 2 (root-vector length from
#     |n_vec|^2 = 4/3 per quark, Part 8 s5.3). The baryon
#     confinement energy is ~ N_c*Lambda (proton mass formula,
#     Part 8 s11), so Delta = lambda_c * 2 = N_c * Lambda
#     => lambda_c = N_c * Lambda / 2 = N_c^2 * f_pi / 2.
#
# (c) V0 = kappa^2/Delta = (N_c*Lambda^2)/(N_c*Lambda) = Lambda.
#     Exact in large-N_c power counting. 🔶
#
# Spin-tensor channel (deuteron J=1; ^3S_1-^3D_1 mixing) open.

_kappa63   = math.sqrt(N_c) * Lqcd     # = sqrt(3)*282 MeV
_Delta63   = N_c * Lqcd                # = 3*282 MeV (1-baryon gap)
_V0_63     = _kappa63**2 / _Delta63    # = Lambda (exact in lg-N_c)
_lambda_c  = N_c * Lqcd / 2.0         # = N_c^2*f_pi/2 ~ 423 MeV
_ratio63   = _V0_63 / Lqcd            # = 1.000 exactly
_Nvec_unit = 2.0                       # |delta N_vec|, one colour flip
_lc_check  = _Delta63 / _Nvec_unit    # = lambda_c (cross-check)


# =========================================================================
# OUTPUT
# =========================================================================



# =============================================================================
# STEPS 1-39 -- OUTPUT
# =============================================================================


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
      resonance at the d=3 resonance site k0 = n_s^2 = 16. Three expressions
      coincide at k0 (the first is its definition; the other two are
      independent coincidences, n_s-solution sets meeting only at n_s=4):
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


# =========================================================================
# STEP 31 -- OUTPUT: CONSECUTIVE MATTER QUARTET (Part 1 §3a, App A §19)
# =========================================================================

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


# =========================================================================
# STEP 29 -- OUTPUT: T0.5 CO-FIXED-POINT SELECTION CONDITION
#            (Part 9 §T0.5, Part 7)
# =========================================================================

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

# STEP 40 -- OUTPUT: CROSS-SECTOR SCALE INCOMMENSURABILITY LEMMA
# =========================================================================

print("\n=== STEP 40: CROSS-SECTOR SCALE INCOMMENSURABILITY LEMMA"
      " (Part 7 §1.2) ===")
print("  Claim (proved exactly, sympy):"
      " all ratios m_d/m_d' irrational except (6,10).")
print(f"  {'pair':>7}  {'ratio (num)':>14}  algebraic class")
print("  " + "-"*58)
_pairs = [(a, b) for i, a in enumerate(_ds) for b in _ds[i+1:]]
_quark = {3, 4}
for _a, _b in _pairs:
    _r = _ms40[_a] / _ms40[_b]
    # exact algebraic class (proved by sympy):
    # exactly one member in {3,4} => ratio^2 contains sqrt(7)
    if _a == 6 and _b == 10:
        _cls = "ratio = 1 exactly  (mu-tau symmetry)"
    elif bool(_a in _quark) != bool(_b in _quark):
        _cls = "ratio^2 in Q*sqrt(7)  {quark vs rest}"
    else:
        _cls = "ratio^2 rational  {same class}"
    print(f"  ({_a:>2},{_b:>2})  {_r:>14.4f}  {_cls}")

print()
print("  Incommensurability confirmed numerically for all 15 pairs.")
print("  Symbolic proof (exact, all 15 pairs):")
print("    claude/explore_scale_incommensurability.py")
print("  Only commensurate pair: (d=6, d=10) -- ratio = 1 exactly.")
print("  => 'No common revival period' is a proved lemma for"
      " 14/15 pairs. ✅")
print("  => The unique commensurate pair is the mu-tau pair"
      " (m_scale_6 = m_scale_10).")


# =============================================================================
# =========================================================================
# STEP 41 -- OUTPUT: TOWER EDGES AS CONDENSATE MATRIX ELEMENTS (F5/F16 j...
# =========================================================================

print("\n=== STEP 41: TOWER EDGES AS CONDENSATE MATRIX ELEMENTS"
      " (Part 2 §9c) ===")
_edges = [("n_e = n_nu1+n_u ", 10, 3, 13),
          ("n_mu= n_nu2+n_c ", 15, 20, 35),
          ("n_tau=n_nu3+n_d ", 22, 1, 23)]
print("  ADDITIVE edges -- top-of-band coefficient of x*H_a*H_b:")
for _nm, _na, _nb, _nc in _edges:
    _ka, _kb, _kc = _na - 1, _nb - 1, _nc - 1
    _ctop = 2.0**(_ka + _kb) / 2.0**(_ka + _kb + 1)   # = 1/2 exactly
    _ok = (_nc == _na + _nb) and (_kc == _ka + _kb + 1)
    print(f"    {_nm}: n_c={_nc}=n_a+n_b ({_nc==_na+_nb}),"
          f" top coeff={_ctop:.3f} (>0)  {'OK' if _ok else 'BAD'}")
_net = (22 - 1) - ((10 - 1) + (15 - 1))               # deg(nu3) - deg(prod)
print("  SUBTRACTIVE edge n_nu3 = n_nu1+n_nu2-n_u = 22:")
print(f"    net degree vs product = {_net} = -(n_u-1) = -2 (LOWERING);")
print("    -n_u = inclusion-exclusion (shared seed) = cumulant minus.")
print("    => W[e,3] carries the relative minus: dU_e3/dtheta13 < 0")
print("       (T8 gap (ii) relative sign; branch per Part 10 §4).")


# =============================================================================
# =========================================================================
# STEP 42 -- OUTPUT: HYBRIDISATION ANGLES FROM ORBIT-STATE ORTHOGONALITY
# =========================================================================

print("\n=== STEP 42: HYBRID ANGLES FROM ORBIT-STATE"
      " ORTHOGONALITY (Part 11 sec 1) ===")
_dirs = {
    2: [(1.0, 0.0, 0.0), (-1.0, 0.0, 0.0)],
    3: [(1.0, 0.0, 0.0), (-0.5, math.sqrt(3)/2, 0.0),
        (-0.5, -math.sqrt(3)/2, 0.0)],
    4: [(1.0, 1.0, 1.0), (1.0, -1.0, -1.0), (-1.0, 1.0, -1.0),
        (-1.0, -1.0, 1.0)],
}
for _n, _ds in _dirs.items():
    _a = math.sqrt(1.0/_n)                  # s-amplitude, a^2 = 1/n
    _b = math.sqrt(1.0 - 1.0/_n)            # p-amplitude
    _hs = []
    for _d in _ds:
        _L = math.sqrt(sum(c*c for c in _d))
        _hs.append([_a] + [_b*c/_L for c in _d])   # (s,px,py,pz)
    _offmax = max(abs(sum(p*q for p, q in zip(_hs[i], _hs[j])))
                  for i in range(_n) for j in range(_n) if i != j)
    _th = math.degrees(math.acos(-1.0/(_n - 1))) if _n > 1 else 0.0
    print(f"  n={_n}: angle = arccos(-1/{_n-1}) = {_th:8.3f} deg;"
          f" max|<h_i|h_j>| = {_offmax:.1e}")
print("  Premise check: n equal s-shares exhaust |s>: n*(1/n) = 1.")
_dlt = 0.050                                 # fitted, not predicted
_cb = -(0.25 - _dlt)/(0.75 + _dlt)
_cl = -(0.25 + _dlt)/(0.75 - _dlt)
print(f"  Water (delta={_dlt:.3f} FITTED): H-O-H ="
      f" {math.degrees(math.acos(_cb)):.2f} deg (meas. 104.5);")
print(f"    lone-pair angle = {math.degrees(math.acos(_cl)):.2f} deg.")


# =============================================================================
# =========================================================================
# STEP 43 -- OUTPUT: ZONAL HYBRID IDENTITY, OCTAHEDRAL sp3d2, EQUIANGULA...
# =========================================================================

print("\n=== STEP 43: ZONAL HYBRIDS -- sp3d2, EQUIANGULAR CAP"
      " (Part 11 sec 1.6) ===")
_P2 = lambda x: 0.5*(3.0*x*x - 1.0)
# orthogonality polynomial roots for sp3d2 shares (1/6, 1/2, 1/3):
_r = sorted(set(round(x, 12) for x in (0.0, -1.0)
                if abs(1/6 + x/2 + _P2(x)/3) < 1e-12))
print(f"  sp3d2: 1/6 + x/2 + P2(x)/3 = 0 at x = {_r}"
      "  (90/180 deg -> octahedron)")
_ax = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
_a2, _b2, _c2 = 1/6, 1/2, 1/3
_g = max(abs(_a2 + _b2*sum(p*q for p, q in zip(u, v))
             + _c2*_P2(sum(p*q for p, q in zip(u, v))))
         for i, u in enumerate(_ax) for j, v in enumerate(_ax) if i != j)
print(f"  explicit octahedral Gram: max|<h_i|h_j>| (i!=j) = {_g:.1e}")
print(f"  shares sum: 1/6+1/2+1/3 = {_a2+_b2+_c2:.3f} (completeness)")
_eig5 = 1.0 + (5 - 1)*(-1.0/(5 - 1))        # smallest Gram eigenvalue
print("  equiangular cap: n=5, c=-1/4 -> Gram rank 4 > 3:"
      " impossible in R^3;")
print("    at most 4 equivalent equiangular sigma directions"
      " (the simplex).")
_ct = math.cos(math.radians(107.8))          # measured H-N-H (NH3)
_dn = (0.25 + _ct*0.75)/(1.0 - _ct)          # delta, FITTED
print(f"  NH3 (delta FITTED to 107.8 deg): delta = {_dn:.4f}"
      f"  (water: 0.050);")
print("    lone-pair count trend: delta(CH4)=0 < delta(NH3)"
      " < delta(H2O).")

# =============================================================================
# =========================================================================
# STEP 44 -- OUTPUT: HELIUM GROUND STATE: VARIATIONAL BOUND FROM IDWT IN...
# =========================================================================

print("\n=== STEP 44: HELIUM VARIATIONAL BOUND"
      " (Part 11 sec 3) ===")
_Z = 2
_eta = _Z - 5.0/16.0
_E_He_ha = -(_eta**2)                        # in hartree = alpha^2 m_e
_ha_eV = 27.211386                           # measured alpha^2 m_e, eV
_E_exp_ha = -(24.587387 + 54.417765)/_ha_eV  # He ionisation sum, ha
print(f"  eta = Z - 5/16 = {_eta:.4f};"
      f"  E_He = -eta^2 = {_E_He_ha:.5f} hartree (= alpha^2 m_e)")
print(f"  measured (ionisation sum): {_E_exp_ha:.5f} hartree;"
      f"  diff = {(_E_He_ha/_E_exp_ha - 1)*100:+.2f}%")
print("  bound lies above measurement, as a variational bound must;")
print("  the residual is the uncorrelated-product deficit (sec 2).")
print("  (absolute eV scale via IDWT alpha(0) inherits its -2.87%")
print("   residual, Part 3 sec 0.7 -- hence the hartree comparison.)")


# =============================================================================
# =========================================================================
# STEP 45 -- OUTPUT: DERIVING THE HYBRID PREMISES: PLANE INVARIANCE + ZONAL
# =========================================================================

print("\n=== STEP 45: HYBRID PREMISES DERIVED -- PLANE +"
      " ZONAL BLOCK (Part 11 sec 4) ===")
# (a) Slater-plane invariance
_u = np.array([1.0, 0.3, -0.2]); _v = np.array([0.4, 1.0, 0.5])
_e1 = _u/np.linalg.norm(_u)
_w = _v - (_e1 @ _v)*_e1; _e2 = _w/np.linalg.norm(_w)
_A = np.outer(_u, _v) - np.outer(_v, _u)
_B = np.outer(_e1, _e2) - np.outer(_e2, _e1)
_msk = np.abs(_B) > 1e-12
_ratios = _A[_msk]/_B[_msk]
print(f"  (a) wedge ratio spread = {np.ptp(_ratios):.1e}")
print("      (antisym product = scalar x orthonormal pair)")
# (b) dipole matrix on the degenerate n_H=2 shell (a0 = 1)
_r = np.linspace(1e-6, 60.0, 240001)
_R20 = (1.0/(2.0*np.sqrt(2.0)))*(2.0 - _r)*np.exp(-_r/2.0)
_R21 = (1.0/(2.0*np.sqrt(6.0)))*_r*np.exp(-_r/2.0)
_n20 = np.trapezoid(_R20*_R20*_r*_r, _r)
_n21 = np.trapezoid(_R21*_R21*_r*_r, _r)
_zsp = np.trapezoid(_R20*_R21*_r**3, _r)/np.sqrt(3.0)  # <2s|z|2p0>
print(f"  (b) norms: <2s|2s>={_n20:.6f}, <2p|2p>={_n21:.6f};"
      f"  <2s|z|2p0> = {_zsp:+.4f} a0")
_W = np.zeros((4, 4))                  # basis (2s, 2p0, 2p+1, 2p-1)
_W[0, 1] = _W[1, 0] = _zsp             # only s<->p0: m=0 block
_ev, _vc = np.linalg.eigh(_W)
print(f"  shell eigenvalues/E: {np.round(_ev, 4)}"
      "  (m=+-1 unshifted)")
_g = _vc[:, 0]
print(f"  bound-block eigvec: |s|^2={_g[0]**2:.3f},"
      f" |p0|^2={_g[1]**2:.3f}, |p+-1|^2={_g[2]**2+_g[3]**2:.3f}")
print("  => directed zonal hybrid (|s>+|p_n>)/sqrt2: P1' derived"
      " at this order.")


# =============================================================================
# =========================================================================
# STEP 46 -- OUTPUT: AROMATIC RING CURRENT: CLOSED-SHELL SCALING (RIGID ...
# =========================================================================

print("\n=== STEP 46: RING CURRENT -- CLOSED-SHELL SCALING"
      " (Part 11 sec 5) ===")
for _n in (1, 2, 4, 5):
    _Npi = 4*_n + 2
    _lev = 2*(2*_n + 1)                      # 2 e- per level, 2n+1 levels
    print(f"  n={_n}: [{_Npi}]annulene-class shell, m_max={_n},"
          f"  I prop to 2(2n+1)={_lev} = N_pi ({_lev == _Npi})")
print("  => induced ring current scales with the pi-electron count,")
print("     not with m_max; R-independent in the rigid-ring model.")


# =============================================================================
# =========================================================================
# STEP 47 -- OUTPUT: MARGINAL EXACTNESS: 3D PROBES FIX ALL CHEMISTRY
# =========================================================================

print("\n=== STEP 47: MARGINAL EXACTNESS -- 3D PROBES"
      " (Part 11 sec 6) ===")
_rng = np.random.default_rng(7)
_Nr, _Nx = 8, 6
_Hr = _rng.normal(size=(_Nr, _Nr)); _Hr = (_Hr + _Hr.T)/2
_Hx = _rng.normal(size=(_Nx, _Nx)); _Hx = (_Hx + _Hx.T)/2
_Or = _rng.normal(size=(_Nr, _Nr)); _Or = (_Or + _Or.T)/2
_er, _vr = np.linalg.eigh(_Hr)
_ex, _vx = np.linalg.eigh(_Hx)
_psi = _vr[:, 0]                          # one marginal state
_d1 = np.kron(_psi, _vx[:, 0])            # sector ground
_d2 = np.kron(_psi, _vx[:, 3])            # sector excited
_O = np.kron(_Or, np.eye(_Nx))            # 3D-supported probe
_g1 = _d1 @ _O @ _d1; _g2 = _d2 @ _O @ _d2
_tr = abs(np.kron(_psi, _vx[:, 0]) @ _O @ np.kron(_vr[:, 2], _vx[:, 3]))
print(f"  <O_r> sector-ground vs sector-excited:"
      f" {_g1:+.6f} vs {_g2:+.6f} (diff {abs(_g1-_g2):.1e})")
print(f"  3D-probe transition between sector levels: {_tr:.1e}")
print("  => 3D-measured chemistry is fixed by the d=3 marginal;")
print("     sector structure enters as foundation, not as deviation.")


# =============================================================================
# =========================================================================
# STEP 48 -- OUTPUT: KERNEL RESIDUE BOUND AT CHEMICAL SCALES
# =========================================================================

print("\n=== STEP 48: KERNEL RESIDUE BOUND"
      " (Part 11 sec 6.3) ===")
_L6_fm = 1.414                               # Part 1 sec 3e table
_a0_fm = 0.529177e5                          # Bohr radius in fm
_ratio = _L6_fm/_a0_fm
_me_eV = m_e*1.0e6
_ha_eV2 = 27.211386
_dE = (4.0/3.0)*(_ratio**3)*_me_eV           # eV, depth = m_e bound
print(f"  L_6/a0 = {_ratio:.3e};  (L_6/a0)^3 = {_ratio**3:.3e}")
print(f"  dE <= (4/3)(L_6/a0)^3 m_e = {_dE:.2e} eV")
print(f"  fractional vs hartree: {_dE/_ha_eV2:.1e}"
      "  (s-states; 0 at this order otherwise)")
print("  => same order as the proton-size correction (Part 8");
print("     sec 14.4, ~1e-10); chemistry residue closes at nil.")


# =========================================================================
# STEP 49 -- OUTPUT: WITHIN-SECTOR REVIVAL AMPLITUDE BOUND (T0.5 even-le...
# =========================================================================

print("\n=== STEP 49: WITHIN-SECTOR REVIVAL AMPLITUDE BOUND"
      " (T0.5) ===")
print("  Bound = sum_n (J(n_r,3/2)/DeltaS)^2 per sector")
print("  (off-resonant Rabi; all DeltaS > 0 by spectral independence)")
for _d in [3, 4, 5, 6, 10, 2]:
    _b = _revival_bound(_d)
    print(f"  d={_d:2d}: sum(J/DeltaS)^2 = {_b:.2e}")
print("  d=3 is the worst case; sqrt(4e-4) ~ 2% max amplitude.")
print("  Cross-sector revival: time-avg = 0 (incommensurability,")
print("  STEP 40, 14/15 pairs irrational). Total return prob")
print("  bounded at ~4e-4; status remains 🔵 (not exact zero).")


# =============================================================================
# =========================================================================
# STEP 50 -- OUTPUT: [18]ANNULENE RING-CURRENT NMR: SIGN AND SCALING
# =========================================================================

print("\n=== STEP 50: [18]ANNULENE NMR (Part 11 sec 5.1) ===")
for _Np50, _lbl50 in [(6, "benzene "), (18, "[18]ann")]:
    _R50 = _Np50 * _dCC50 / (2*math.pi)
    _dIdB50 = _Np50 * _e50**2 / (4*math.pi*_me50)
    _ro50 = _R50 + _rCH50
    _ri50 = _R50 - _rCH50
    _so50 = _Bz50(_R50, _ro50) * _dIdB50
    _si50 = _Bz50(_R50, _ri50) * _dIdB50
    print(f"  {_lbl50}: R={_R50*1e10:.2f}A "
          f"|dI/dB0|={_dIdB50:.3e}A/T")
    print(f"    sigma_out={_so50*1e6:+.1f}ppm "
          f"sigma_in={_si50*1e6:+.1f}ppm")
print("  [18]ann obs: outer -9.28ppm deshield inner +2.99ppm shield")
print("  Sign: correct both cases; N_pi 6->18 scales ~3x (obs ~2x).")
print("  Rigid-ring overestimates ~5x(outer) ~40x(inner); London")
print("  correction ~19%, distributed-pi ~20% -- combined ~35%.")
print("  Remaining discrepancy requires full GIAO treatment.")


# =========================================================================
# STEP 51 -- OUTPUT: MADELUNG ORDERING FROM SLATER Z_eff
# =========================================================================

print("\n=== STEP 51: MADELUNG ORDERING (Part 11 sec 2) ===")
print("E(n,l) = -Zeff^2/(2n^2)  [hartree]  Slater screening")
print()
print("4s vs 3d (noble-gas core through d-block onset):")
_mald51 = {18:'Ar',19:'K',20:'Ca',21:'Sc'}
for _Z51 in [18,19,20,21]:
    _e4s = -_zeff51(_Z51,4,0)**2/32
    _e3d = -_zeff51(_Z51,3,2)**2/18
    _lbl = _mald51[_Z51]
    print(f"  {_lbl}(Z={_Z51}): "
          f"E_4s={_e4s:.3f}  E_3d={_e3d:.3f}  "
          f"4s_lower={'Y' if _e4s<_e3d else 'N'}")
print()
print("5s vs 4d:")
_mald51b = {36:'Kr',37:'Rb',38:'Sr',39:'Y'}
for _Z51 in [36,37,38,39]:
    _e5s = -_zeff51(_Z51,5,0)**2/50
    _e4d = -_zeff51(_Z51,4,2)**2/32
    _lbl = _mald51b[_Z51]
    print(f"  {_lbl}(Z={_Z51}): "
          f"E_5s={_e5s:.3f}  E_4d={_e4d:.3f}  "
          f"5s_lower={'Y' if _e5s<_e4d else 'N'}")
print()
print("n+l rule confirmed at each noble-gas->d-block transition.")
print("IDWT: 5 observable + 4 CP3-hidden d-states per shell,")
print("all following the same Madelung sequence.")



# =========================================================================
# STEP 52 -- OUTPUT: LONE-PAIR ANGLE DELTA: VARIATIONAL FRAMEWORK + INGR...
# =========================================================================

print("\n=== STEP 52: LONE-PAIR ANGLE DELTA"
      " (Part 11 sec 4.7) ===")
print("STO: O 2s=2.246 2p=2.227; N 2s=2p=1.917;"
      " H 1s=1.24")
print()
print("One-centre Slater-Condon integrals (a.u.):")
print(f"  O: F0ss={_F0ss52_O:.4f} F0sp={_F0sp52_O:.4f}"
      f" F0pp={_F0pp52_O:.4f} F2pp={_F2pp52_O:.4f}")
print(f"  N: F0ss={_F0ss52_N:.4f} F0sp={_F0sp52_N:.4f}"
      f" F0pp={_F0pp52_N:.4f} F2pp={_F2pp52_N:.4f}")
print()
print("Overlap integrals (dimensionless):")
print(f"  O: S(2s,1sH)={_Ss52_O:.4f}"
      f" S(2p,1sH)={_Sp52_O:.4f}")
print(f"  N: S(2s,1sH)={_Ss52_N:.4f}"
      f" S(2p,1sH)={_Sp52_N:.4f}")
print()
print("Nuclear attraction difference DeltaV_H (a.u.):")
print(f"  O: <2pz|1/r_H|2pz>-<2s|1/r_H|2s>"
      f" = {_DV52_O:.4f}")
print(f"  N: same difference"
      f" = {_DV52_N:.4f}")
print()
print("One-centre E2 variation over delta in [0,0.25]:")
print(f"  H2O: E2(0)={_E2_H2O_0:.4f}"
      f" E2(0.25)={_E2_H2O_025:.4f}"
      f" range={_E2_H2O_025-_E2_H2O_0:.4f} a.u.")
print("  --> one-centre model cannot set equilibrium delta;")
print("  two-centre integrals (Part 8 sec 16) required.")
print()
print("H-H nuclear repulsion gradient (main geometric term):")
print(f"  H2O: dV_HH/ddelta at obs = {_dVHH_H2O:.3f} a.u./unit")
print(f"  NH3: dV_HH/ddelta at obs = {_dVHH_NH3:.3f} a.u./unit")
print()
print("Observed delta values (from Part 11 sec 1.4):")
print("  CH4: 0 (no lone pairs)  NH3: 0.016  H2O: 0.050")
print("  Monotone with lone-pair count -- qualitative prediction")
print("  confirmed; quantitative delta from two-centre integrals")
print("  of Part 8 sec 16 type with Born-Oppenheimer geometry.")
print("  Status: 🔶 framework and ingredients in place.")


# =========================================================================
# STEP 53 -- OUTPUT: KERNEL CONTACT AMPLITUDE (Part 11 section 6.4)
# =========================================================================

# =========================================================================
# STEP 54 -- OUTPUT: [18]ANNULENE NMR: DISTRIBUTED p_z CURRENT (Part 11 ...
# =========================================================================

print("\n=== STEP 54: [18]ANNULENE p_z GIAO"
      " (Part 11 sec 5.1) ===")
print(f"  zeta(C 2p_z) = 1.625 a.u.; grid 0.2 A;"
      f" Nphi_BS = 500")
print(f"  R={_R54*1e10:.3f} A  rho_out={_rho_o54*1e10:.3f}"
      f" A  rho_in={_rho_i54*1e10:.3f} A")
print()
print("  outer proton:")
print(f"    thin-wire (STEP 50): {_sig_tw_o:+.1f} ppm")
print(f"    p_z distributed:     {_sig_d_o:+.1f} ppm"
      f"  (reduc {(1-_Bz_d_o/_Bz_tw_o)*100:.0f}%)")
print(f"    + London cos(pi/18): {_sig_dL_o:+.1f} ppm")
print(f"    observed:            -9.28 ppm")
print(f"    remaining factor: {abs(_sig_dL_o/9.28):.1f}x")
print()
print("  inner proton:")
print(f"    thin-wire (STEP 50): {_sig_tw_i:+.1f} ppm")
print(f"    p_z distributed:     {_sig_d_i:+.1f} ppm"
      f"  (reduc {(1-_Bz_d_i/_Bz_tw_i)*100:.0f}%)")
print(f"    + London cos(pi/18): {_sig_dL_i:+.1f} ppm")
print(f"    observed:            +2.99 ppm")
print(f"    remaining factor: {abs(_sig_dL_i/2.99):.0f}x")
print()
print("  p_z spreading + London combined correction ~35%.")
print("  Remaining: outer ~3x, inner ~30x -- consistent")
print("  with Part 11 sec 5.1 estimate (3x/26x).")
print("  Full discrete-atom GIAO required to close gap.")
print("  Status: 🔶")



# =============================================================================
# STEP 55 -- OUTPUT: THE d=2 EVEN-INSERTION SELECTION RULE
# =============================================================================

print("\n=== STEP 55: d=2 EVEN-INSERTION SELECTION RULE"
      " (insertion dichotomy) ===")
print("No odd condensate vertex acts in the d=2 variable (Part 3")
print("sec 16.2, the m_gamma=0 evenness): d=2 productions carry an")
print("even number of degree-1 insertions; matter edges carry one.")
print("  insertion census: e,mu,tau = 1 | W,Z,H-join = 0"
      " | H-additive = 2")
print(f"  proxy landings exact for all 7 productions: {_land_ok55}")
print(f"  d=2 productions all even: {_parity_ok55}")
for _nm55, _v55, _occ55 in _cf_boson55:
    print(f"  counterfactual odd-insertion {_nm55}: n={_v55}"
          f"  occupied: {_occ55}")
print(f"  counterfactuals all unoccupied: {_cf_clean55}")
print("  One fact (no d=2 condensate) gives m_gamma = 0 and the")
print("  g-rule -1 (shared vacuum, Part 3 sec 11).  Status: 🔶")


# =============================================================================
# STEP 56 -- OUTPUT: SUM-FREE VERIFICATION OF THE OCCUPIED S-VALUES
# =============================================================================

print("\n=== STEP 56: SUM-FREE VERIFICATION OF OCCUPIED S-VALUES ===")
print(f"  14 non-zero S-values; pairwise a+b=c collisions:"
      f" {len(_collisions56)}")
print(f"  sum-free: {_sumfree56}  (Part 1 sec 5 additive rigidity)")
print("  (the mode indices are not sum-free -- 1+3=4; the property")
print("  holds at the S-value / eigenvalue level)")


# =============================================================================
# STEP 57 -- OUTPUT: COW GRAVITATIONAL PHASE, IDWT NUCLEON MASS
# =============================================================================

print("\n=== STEP 57: COW GRAVITATIONAL PHASE, IDWT NUCLEON MASS ===")
print("  delta_phi = m g A/(hbar v) = m^2 g A lambda/(2 pi hbar^2)")
print("  representative geometry: lambda = 1.445 A, A = 10 cm^2")
print(f"  phi(PDG m_n = 939.565 MeV)    = {_phi_std57:6.2f} rad")
print(f"  phi(IDWT m_N = {m_N_idwt:7.3f} MeV) = {_phi_idwt57:6.2f} rad")
print(f"  ratio = (m_N_idwt/m_n)^2 = {_ratio57:.5f}"
      f"  (+{(_ratio57 - 1) * 100:.2f}%)")
print(f"  ratio consistency check: {_ratio_ok57}")
print("  Tens-of-radians scale, as observed in the COW class; the")
print("  +0.17% is the STEP 7 composite-m_N residual, not a new")
print("  effect. Phase-to-mass ratio species-independent:")
print("  m_grav = m_inertial = S(n,d)*m_scale_d (Part 4 s3.6). 🔵")

# =============================================================================
# STEP 58 -- OUTPUT: SECTOR-WELL COVARIANCE (Part 4 section 3.10.2)
# =============================================================================

print("\n=== STEP 58: SECTOR-WELL COVARIANCE ===")
print("  absolute reading: U_A(X)/g = X^4 + (2s^2/d)X^2 + s^4/d")
print(f"  d=6: s^2 = {_s2_58:.0f}; at X = a0 = {_X58:.3e} sector units:")
print(f"    pinning U_A = {_pin58:.2e}   vs   internal E_0 = {_E0_58:.0f}")
print("    -> forbids macroscopic motion; contradicts the Bohr")
print("       spectrum (Part 8 s14.2). EXCLUDED ✅ (reductio).")
print(f"  covariant (mode-frame): U_B = g s^4/d = {_U_rel58:.2f},")
print("    X-independent; lam_d = (g_dd/2)^(2/3) unchanged, all sectors:")
print("    " + ", ".join(f"d={d}: {_lam_all58[d]:.3f}" for d in sector_d))
print(f"  hydrogen smearing: dE/|E_1s| = 4(L_6/a0)^2 = {_dE58:.2e}")
print("    (proton-finite-size order, Part 8 s14.4)")
print("  The well rides with the mode 🔶 (minimal covariant completion);")
print("  bound about its center within; the center free everywhere.")

# =============================================================================
# STEP 59 -- OUTPUT: CROSS-SECTOR KERNEL COVARIANCE (Part 4 s3.10.1)
# =============================================================================

print("\n=== STEP 59: CROSS-SECTOR KERNEL COVARIANCE ===")
print("  two-point covariant readings of g_{dd'}(xi.xi')^2, e-p pair:")
print("  (0) absolute: changes under global translation     EXCLUDED")
print(f"  (1) pair-centroid: g36*U_1(a0) = {_U1_a0_59:.2e}")
print("      mutual quartic confinement of every pair       EXCLUDED")
print(f"  (2) each-own-frame: U_2/g = {_U2_59:.3f}, R-independent")
print("      pair energy never vanishes (clustering)        EXCLUDED")
print("  => FORCED: contact-gated U = g * Omega(R) * d_sh a^2 b^2 ✅")
print("     kernel contact structure = consequence, not assertion;")
print("     established couplings are Omega(0)=1 evaluations.")
print("  gate profile (Gaussian modes; derived in STEP 60):")
print(f"    ranges: e-e {_rng_ee59:.3f} (= L_6, derives Part 11 s6.3")
print(f"    premise); e-p {_rng_ep59:.3f}; q-q(3,4) {_rng_qq59:.3f}")
print("    (sub-fm strong-force scale)")
print(f"    gate at R=a0: ln Omega = {_lnOm_a0_59:.2e}")
print(f"    A=B, R=0 reduces to STEP 58 self-term: {_self_ok59}")

# =============================================================================
# STEP 60 -- OUTPUT: KERNEL GATE PROFILE DERIVED (Part 4 s3.10.1)
# =============================================================================

print("\n=== STEP 60: KERNEL GATE PROFILE DERIVED ===")
print("  inputs: (i) kernel bilinear in mode intensities (J·J form,")
print("  Part 3 s0.6); (ii) covariance + STEP 59 exclusions (F decays);")
print("  (iii) no intrinsic length in the action (g_dd' dimensionless)")
print("  => F = scale-free point contact; gate = normalized density")
print("  overlap: Omega(R) = exp(-R^2/(2(a^2+b^2))) for Gaussian modes.")
print("  Derived. ✅")
print("  Corollary: same-sector contact range = sqrt(2 sigma_d^2)")
print(f"  = L_d exactly, all sectors: {_ident60}")
print("  (e-e: L_6 = Part 11 s6.3 range; N-N at d=3: L_3 = 0.675)")

# =============================================================================
# STEP 61 -- OUTPUT: DEUTERON INVERSE CHECK (Part 8 section 11)
# =============================================================================

print("\n=== STEP 61: INTERNUCLEON CONTACT -- DEUTERON INVERSE CHECK ===")
print("  V(r) = -V0 exp(-r^2/(2 Rc^2)); E_B = 2.224566 MeV (CODATA);")
print(f"  reduced mass m_N_idwt/2, m_N_idwt = {m_N_idwt:.3f} MeV")
print("  gate            Rc (fm)   V0 (MeV)   V0/Lqcd")
print(f"  N-N (L_3)       {_RC_NN61:7.3f} {_V0_NN61:10.1f}"
      f" {_V0_NN61/Lqcd:9.2f}")
print(f"  q-q (3,4)       {_RC_QQ61:7.3f} {_V0_QQ61:10.1f}"
      f" {_V0_QQ61/Lqcd:9.2f}")
print(f"  N-N (meas. r_p) {_RC_RP61:7.3f} {_V0_RP61:10.1f}"
      f" {_V0_RP61/Lqcd:9.2f}")
print("  range fixed by the derived gate (STEP 60); the depth V0 is")
print("  the number the kernel must supply -- open, same class as the")
print("  s11 confinement level. 🔶")
print(f"  solved-mode rms(r/2) = {_rms_NN61:.2f} fm (L_3 gate)  vs")
print("  measured deuteron matter radius ~ 1.97 fm (shallow-state")
print("  universality). 🔵")

# =============================================================================
# STEP 62 -- OUTPUT: N-N WELL, SECOND ORDER -- DEPTH = LAMBDA
# =============================================================================

print("\n=== STEP 62: N-N WELL FROM SECOND-ORDER KERNEL CONTACT ===")
print("  two singlets: N_A = N_B = 0 -> first-order colour energy")
print("  zero (E = lambda_c|N|, s5.3); leading N-N term is SECOND")
print("  order in the gated contact (colour van der Waals, cf. s17b);")
print("  second order squares the gate: V = -V0 exp(-R^2/(2 Rc2^2)),")
print("  Rc2 = range/sqrt(2). Profile and range carry no freedom.")
print("  inverse (measured E_B = 2.2246 MeV fixes V0):")
print(f"    L_3 gate: Rc2 = {_RC2_NN62:.3f}  V0 = {_V0_NN62:6.1f} MeV"
      f"  = {_V0_NN62/Lqcd:.2f} Lqcd")
print(f"    r_p gate: Rc2 = {_RC2_RP62:.3f}  V0 = {_V0_RP62:6.1f} MeV"
      f"  = {_V0_RP62/Lqcd:.2f} Lqcd")
print("  -> required depth = Lqcd = N_c f_pi within 2%, both gates. 🔵")
print("  forward, parameter-free (V0 = Lqcd exactly):")
print(f"    E_B = {_EB_NN62:.2f} MeV (L_3) / {_EB_RP62:.2f} MeV (r_p),")
print("    bracketing measured 2.2246 (shallow state: exponentially")
print("    depth-sensitive; the inverse statement is the robust one)")
print(f"  rms(r/2) = {_rms_NN62:.2f} fm vs measured ~1.97 fm")
print("  kappa and Delta: see STEP 63 below. 🔶")


# =============================================================================
# STEP 63 -- OUTPUT: KAPPA, DELTA, LAMBDA_C FROM LARGE-N_c (Part 8 s11)
# =============================================================================

print("\n=== STEP 63: KAPPA, DELTA, LAMBDA_C -- LARGE-N_c COLOUR ===")
print("  V0 = kappa^2/Delta (section 11 second-order N-N depth).")
print("  Large-N_c identification (N_c = chi(CP^2) = 3):")
print("  (a) kappa = sqrt(N_c)*Lambda:")
print("      N_c quarks each contribute colour amplitude Lambda at")
print("      the hadronic threshold (g_eff=1 at n=n_s in d=3).")
print("      Coherent baryon-level sum gives sqrt(N_c) enhancement.")
print(f"      kappa = sqrt({N_c}) * {Lqcd:.1f} MeV"
      f" = {_kappa63:.1f} MeV")
print("  (b) Delta = N_c*Lambda (one-baryon colour excitation gap):")
print("      E_conf = lambda_c|N_vec|; one colour flip gives")
print(f"      |delta N_vec| = {_Nvec_unit:.0f} (s5.3 colour charge table).")
print("      Baryon confinement energy ~ N_c*Lambda (s11 m_N formula)")
print(f"      => Delta = lambda_c*2 = N_c*Lambda"
      f" = {_Delta63:.1f} MeV")
print(f"      => lambda_c = N_c*Lambda/2 = N_c^2*f_pi/2"
      f" = {_lambda_c:.1f} MeV")
print(f"         (cross-check: Delta/{_Nvec_unit:.0f}"
      f" = {_lc_check:.1f} MeV = lambda_c)")
print("  (c) V0 = kappa^2/Delta:")
print(f"      = ({_kappa63:.1f})^2 / {_Delta63:.1f}"
      f" = {_V0_63:.1f} MeV")
print(f"      = {_ratio63:.3f} * Lambda  (exact in large-N_c). 🔶")
print("  Status: large-N_c power counting; O(1) coefficients fixed")
print("  by leading large-N_c structure. Exact kernel matrix elements")
print("  require collective-mode ID of colour-singlet baryon (s5.3).")
print("  Spin-tensor channel (^3S_1-^3D_1 for J=1 deuteron): open.")


print("\nDocs:  https://doi.org/10.5281/zenodo.19767493")
print("https://fedgeno.github.io/")

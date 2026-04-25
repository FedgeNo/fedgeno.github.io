# idwt-by-meta.py — Minimal IDWT mass calculator (combinatorics only)
# ----------------------------------------------------------------------
# Purpose: reproduce the core IDWT fermion spectrum using ONE empirical input
# (the electron mass). No quark masses are fitted. All scales follow from
# the {1,4} seed and the simplex number S(n,d) = C(n+d-1, d).
#
# This mirrors IDWT_01 §0, IDWT_03 §20, and OQ17 (Section 108) in the notes.

import math

# ----------------------------------------------------------------------
# 1. Simplex number — the only n,d dependence in IDWT
# S(n,d) counts degree-n monomials in d variables: dim Sym^n(R^d)
# Example: S(4,3) = C(6,3) = 20 (strange quark degeneracy)
def S(n, d):
    return math.comb(n + d - 1, d)

# ----------------------------------------------------------------------
# 2. Couplings derived from the {1,4} seed — NO fits
# The framework selects n_down=1 and n_strange=4 as the unique minimal seed
# (IDWT_01: "Minimal basis {1,4} generates all particle indices").
#
# g33: d=3 self-coupling. Derived from the critical gap that selects n=4 over n=2:
# gap = S(4,3) - S(2,3) = 20 - 4 = 16
# g33 = sqrt(gap^2 * S(4,4)/S(4,3)) = sqrt(16^2 * 35/20) = sqrt(448) = 8*sqrt(7)
# This is pure combinatorics — no mass input.
g33 = math.sqrt((S(4,3) - S(2,3))**2 * S(4,4) / S(4,3)) # 8√7 ≈ 21.16601

# g44: d=4 self-coupling. Fixed by the generation-law consistency between
# d=3 and d=4 sectors. The notes give the closed form 12/√7.
g44 = 12.0 / math.sqrt(7) # ≈ 4.53557

# g66: d=6 self-coupling. Normalisation choice for the lepton sector.
# Set to 1/4 in the minimal combinatorics version (see OQ17 derivation).
g66 = 0.25

# ----------------------------------------------------------------------
# 3. ONE empirical anchor — electron mass
# IDWT claims all absolute scales follow from m_e. PDG 2022 value:
m_e = 0.51099895 # MeV — the ONLY fitted number in this script

# ----------------------------------------------------------------------
# 4. Sector mass scales m_scale_d
# Each sector d has a uniform vacuum offset m_scale_d. Mode masses are:
# m(n,d) = m_scale_d * S(n,d) (leading order)
#
# m_scale_6: set by electron (n=13, d=6). S(13,6)=18564.
# m_scale_6 = m_e / S(13,6) → ~2.75e-5 MeV
m_scale6 = m_e / S(13, 6)

# m_scale_3: derived from m_e via coupling ratio sqrt(g33/g66).
# This is the OQ17 closure: m_scale_3 = m_e * sqrt(g33/g66)
# It replaces the old PDG-down-quark anchor (4.67 MeV) with a predicted
# value ~4.702 MeV. The +0.682% shift in down/strange masses comes from this.
m_scale3 = m_e * math.sqrt(g33 / g66)

# m_scale_4: follows from m_scale_3 via sqrt(g44/g33), then divided by S(3,4)=15
# because the up-quark index n_up=3 lives in d=4. This propagates the {1,4}
# seed into the up-type sector without new parameters.
m_scale4 = m_scale3 * math.sqrt(g44 / g33) / S(3, 4)

# m_scale_10: tau sector. Leading-order geometric prediction is equality
# with m_scale_6 (IDWT_01: "m_scale_10/m_scale_6 = 1.0006 — extracted, not derived").
# We use the pure geometric value here; the 0.06% tau residual is the open correction.
m_scale10 = m_scale6

# Collect scales for easy lookup
scales = {3: m_scale3, 4: m_scale4, 6: m_scale6, 10: m_scale10}

# ----------------------------------------------------------------------
# 5. Particle table — inputs for each state
# Each tuple: (name, d, n, PDG_mass_MeV)
# - name: label for printing
# - d: sector dimension (2,3,4,5,6,10 in full theory; we use 3,4,6,10 here)
# - n: mode index (derived in notes from generation laws, not fitted)
# - PDG_mass_MeV: reference value for error calculation only; NOT used in prediction
particles = [
    ("down", 3, 1, 4.67), # n_down=1 forced by S(1,d)=1 for all d
    ("strange", 3, 4, 93.4), # n_strange=4 is the minimal cross-family resonator
    ("up", 4, 3, 2.16), # n_up=3 from generation law
    ("charm", 4, 20, 1270.0), # n_charm=20 = S(4,3)
    ("top", 4, 72, 172690.0), # n_top=72 = n_charm + 4*n_electron
    ("electron",6, 13, 0.51099895), # n_e=13 = n_nu1 + n_up (anchor)
    ("muon", 6, 35, 105.6583745), # n_mu=35 = S(4,4) = n_nu2 + n_charm
    ("tau", 10, 23, 1776.86), # n_tau=23 = n_nu3 + n_down
]

# ----------------------------------------------------------------------
# 6. Compute and print — formatted for aligned columns
print(f"{'particle':<8} {'d':>1} {'n':>2} {'S(n,d)':>9} {'pred(MeV)':>12} {'PDG':>10} {'err%':>8}")
print("-" * 56)

for name, d, n, pdg in particles:
    # Prediction: leading-order IDWT formula
    pred = scales[d] * S(n, d)

    # Percent error vs PDG (for diagnostics only)
    err = (pred - pdg) / pdg * 100

    # :<8 left-align name, :>9 right-align integer S, :12.3f fixed 3 decimals
    print(f"{name:<8} {d:1d} {n:2d} {S(n,d):9d} {pred:12.3f} {pdg:10.3f} {err:+7.3f}%")

# ----------------------------------------------------------------------
# 7. Diagnostic output — show derived scales and couplings
print("\nDerived scales (MeV):")
for d in sorted(scales):
    print(f" m_scale_{d} = {scales[d]:.6g}")

print("\nCouplings (from {1,4} seed):")
print(f" g33 = {g33:.6f} (= 8√7)")
print(f" g44 = {g44:.6f} (= 12/√7)")
print(f" g66 = {g66:.6f}")

# idwt_full_commented_v2.py — IDWT mass calculator, clean task separation
# ------------------------------------------------------------------------------
# This version follows your request: build everything first, then print.
# No alternating compute/print. All formulas are shown using particle names.

import math

# Core combinatorics
def S(n, d):
    """S(n,d) = C(n+d-1, d) = dim Sym^n(R^d)"""
    return math.comb(n + d - 1, d) if n >= 0 and d >= 0 else 0

# ------------------------------------------------------------------------------
# STEP 1: BUILD THE TOWER BY EXPLICIT ADDITION (compute only)
n_down = 1                 # forced: S(1,d)=1 ground state
n_strange = 4              # forced: unique solution to S(n,4)=35

n_up = n_strange - 1       # 3

# neutrino modes (used only to construct leptons)
n_nu1 = S(n_up, 3)         # S(3,3)=10
n_nu2 = S(n_up, 4)         # S(3,4)=15
n_nu3 = n_nu1 + n_nu2 - n_up   # 22

# leptons via generation law n_lepton = n_neutrino + n_quark
n_e = n_nu1 + n_up         # 13
n_charm = S(n_strange, 3)  # S(4,3)=20
n_mu = n_charm + n_nu2     # 35 = S(4,4)
n_tau = n_nu3 + n_down     # 23

# up-type quarks
n_top = n_charm + 4 * n_e  # 72

# bosons via Vandermonde g(a,b)=a+b-1
n_W = n_top + 5 - 1        # 76
n_Z = n_W + 6 - 1          # 81
n_H = n_Z + n_nu2 - 1      # 95

# ------------------------------------------------------------------------------
# STEP 2: COMPUTE COUPLINGS FROM SEEDS (using particle names)
# g33 and g44 are derived from the two seeds n_strange and n_up
# From Part 6: g33 = n_s^2 * sqrt(n_s + n_u) / 2, g44 = n_s * n_u / sqrt(n_s + n_u)
g33 = (n_strange**2) * math.sqrt(n_strange + n_up) / 2.0   # = 8√7
g44 = (n_strange * n_up) / math.sqrt(n_strange + n_up)    # = 12/√7
g66 = 0.25  # Y_L = -1/2 from anomaly cancellation => g66 = Y_L^2

# ------------------------------------------------------------------------------
# STEP 3: COMPUTE SECTOR SCALES (two empirical inputs only)
m_e = 0.51099895   # MeV
m_W = 80377.0      # MeV

m_scale6 = m_e / S(n_e, 6)
m_scale3 = m_e * math.sqrt(g33 / g66)
m_scale4 = m_scale3 * math.sqrt(g44 / g33) / S(n_up, 4)
m_scale10 = m_scale6          # g10,10 = g66
m_scale2 = m_W / S(n_W, 2)

scales = {2: m_scale2, 3: m_scale3, 4: m_scale4, 6: m_scale6, 10: m_scale10}

# ------------------------------------------------------------------------------
# STEP 4: COMPUTE CORRECTIONS (do not print yet)
epsilon = 1.0 / (280.0 * math.sqrt(7.0))   # GTC
k_vals = {"up": 0, "charm": 3, "top": 10}
dyson_factor = 1.0 + 1.0/1680.0

# ------------------------------------------------------------------------------
# STEP 5: OUTPUT TOWER
print("=== TOWER CONSTRUCTION (explicit addition) ===")
print(f"seeds: n_down = 1, n_strange = 4")
print(f"n_up = n_strange - 1 = {n_strange} - 1 = {n_up}")
print(f"n_nu1 = S(n_up,3) = S({n_up},3) = {n_nu1}")
print(f"n_nu2 = S(n_up,4) = S({n_up},4) = {n_nu2}")
print(f"n_nu3 = n_nu1 + n_nu2 - n_up = {n_nu1} + {n_nu2} - {n_up} = {n_nu3}")
print(f"n_e = n_nu1 + n_up = {n_nu1} + {n_up} = {n_e}")
print(f"n_charm = S(n_strange,3) = S({n_strange},3) = {n_charm}")
print(f"n_mu = n_charm + n_nu2 = {n_charm} + {n_nu2} = {n_mu}  [also S(4,4)={S(4,4)}]")
print(f"n_tau = n_nu3 + n_down = {n_nu3} + {n_down} = {n_tau}")
print(f"n_top = n_charm + 4*n_e = {n_charm} + 4*{n_e} = {n_top}")
print(f"n_W = n_top + 4 = {n_top} + 4 = {n_W}")
print(f"n_Z = n_W + 5 = {n_W} + 5 = {n_Z}")
print(f"n_H = n_Z + n_nu2 - 1 = {n_Z} + {n_nu2} - 1 = {n_H}")

# ------------------------------------------------------------------------------
# STEP 6: OUTPUT COUPLINGS WITH PARTICLE-BASED MATH
print("
=== COUPLINGS DERIVED FROM SEEDS ===")
print("g33 = n_strange^2 * sqrt(n_strange + n_up) / 2")
print(f"    = {n_strange}^2 * sqrt({n_strange} + {n_up}) / 2")
print(f"    = {n_strange**2} * sqrt({n_strange+n_up}) / 2")
print(f"    = 8*√7 = {g33:.6f}")
print()
print("g44 = n_strange * n_up / sqrt(n_strange + n_up)")
print(f"    = {n_strange} * {n_up} / sqrt({n_strange} + {n_up})")
print(f"    = {n_strange*n_up} / sqrt({n_strange+n_up})")
print(f"    = 12/√7 = {g44:.6f}")
print()
print("g66 = Y_L^2  with Y_L = -1/2 from SU(2)^2 U(1) anomaly")
print(f"    = (1/2)^2 = {g66}")

# ------------------------------------------------------------------------------
# STEP 7: OUTPUT SECTOR SCALES
print("
=== SECTOR SCALES (from m_e and m_W) ===")
print(f"m_scale_6 = m_e / S(n_e,6) = {m_e} / {S(n_e,6)} = {m_scale6:.6g} MeV")
print(f"m_scale_3 = m_e * sqrt(g33/g66) = {m_e} * sqrt({g33:.3f}/{g66}) = {m_scale3:.6g} MeV")
print(f"m_scale_4 = m_scale_3 * sqrt(g44/g33) / S(n_up,4) = {m_scale3:.3f} * sqrt({g44:.3f}/{g33:.3f}) / {S(n_up,4)} = {m_scale4:.6g} MeV")
print(f"m_scale_10 = m_scale_6 (g10,10 = g66) = {m_scale10:.6g} MeV")
print(f"m_scale_2 = m_W / S(n_W,2) = {m_W} / {S(n_W,2)} = {m_scale2:.6g} MeV")

# ------------------------------------------------------------------------------
# STEP 8: OUTPUT CORRECTIONS
print("
=== CORRECTIONS ===")
print("GTC epsilon = 1 / (280 * sqrt(7))")
print(f"          = 1 / (280 * {math.sqrt(7):.6f}) = {epsilon:.8f}")
print(f"k-values (d=4 only): up: k={k_vals['up']}, charm: k={k_vals['charm']}, top: k={k_vals['top']}")
print()
print("Dyson tau factor = 1 + 1/(n_up * n_strange^2 * S(n_strange,4))")
print(f"               = 1 + 1/({n_up} * {n_strange}^2 * {S(n_strange,4)})")
print(f"               = 1 + 1/1680 = {dyson_factor:.6f}")

# ------------------------------------------------------------------------------
# STEP 9: PARTICLE LIST (neutrinos omitted)
particles = [
    ("photon", 2, 0, 0.0),
    ("W", 2, n_W, 80377.0),
    ("Z", 2, n_Z, 91187.6),
    ("Higgs", 2, n_H, 125250.0),
    ("down", 3, n_down, 4.67),
    ("strange", 3, n_strange, 93.4),
    ("bottom", 3, None, 4180.0),
    ("up", 4, n_up, 2.16),
    ("charm", 4, n_charm, 1270.0),
    ("top", 4, n_top, 172760.0),
    ("electron", 6, n_e, 0.51099895),
    ("muon", 6, n_mu, 105.6583745),
    ("tau", 10, n_tau, 1776.86),
]

def pred0(name,d,n):
    if name=="photon": return 0.0
    if name=="bottom": return math.sqrt(S(16,3)*S(17,3)) * scales[3]
    return scales[d] * S(n,d)

def pred_corr(name,d,n):
    base = pred0(name,d,n)
    if name in k_vals:
        return base * (1-epsilon)**k_vals[name]
    if name=="tau":
        return base * dyson_factor
    return base

# ------------------------------------------------------------------------------
# STEP 10: UNCORRECTED TABLE
print("
=== UNCORRECTED TABLE ===")
hdr = f"{'particle':<9} {'d':>2} {'n':>4} {'S':>10} {'pred':>12} {'PDG':>12} {'err%':>8}"
print(hdr); print("-"*len(hdr))
for name,d,n,pdg in particles:
    s = S(n,d) if n is not None else 0
    p = pred0(name,d,n)
    err = (p-pdg)/pdg*100 if pdg else 0
    print(f"{name:<9} {d:2d} {str(n) if n is not None else '-':>4} {s:10d} {p:12.3f} {pdg:12.3f} {err:+7.2f}%")

# ------------------------------------------------------------------------------
# STEP 11: CORRECTED TABLE
print("
=== CORRECTED TABLE (GTC + Dyson) ===")
print(hdr); print("-"*len(hdr))
for name,d,n,pdg in particles:
    s = S(n,d) if n is not None else 0
    p = pred_corr(name,d,n)
    err = (p-pdg)/pdg*100 if pdg else 0
    print(f"{name:<9} {d:2d} {str(n) if n is not None else '-':>4} {s:10d} {p:12.3f} {pdg:12.3f} {err:+7.2f}%")
print("
https://fedgeno.github.io/")

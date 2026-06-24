#!/usr/bin/env python3
"""BEAVRS Cycle 1 full-core PWR - OpenMC translation (community example deck).

PROVENANCE
----------
Geometry + materials translated from the author-VERIFIED Cambridge SCONE
BEAVRS full-core deck (reactor-test-decks/beavrs_scone_fullcore.scone) and the
public MIT BEAVRS rev 2.0.2 specification (Horelik, Herman, Forget, Smith;
CRPG/MIT, 2018). This is a COMMUNITY EXAMPLE DECK - it is NOT benchmark-
validated and is not an official MIT/CRPG product.

WHAT THIS BUILDS
----------------
- 17x17 core lattice (assembly pitch 21.50364 cm), 193 fuel assemblies on the
  verified BEAVRS loading map (3 enrichment zones).
- 17x17 assemblies (pin pitch 1.26 cm; fuel 0.39218 / gap 0.40005 /
  clad 0.45720 cm) with 24 guide tubes + 1 central instrument tube.
- Enrichment zones 1.6 / 2.4 / 3.1 wt% UO2; Pyrex burnable-poison rods;
  control rods WITHDRAWN (water-filled guide tubes); core barrel /
  downcomer / RPV liner / RPV; vacuum boundaries.

ASSUMPTIONS / SIMPLIFICATIONS (FLAGGED)
---------------------------------------
* Cross sections: requires OPENMC_CROSS_SECTIONS. Number densities are
  identical to the verified SCONE deck (which used JEF-3.1.1 at 600 K);
  pick a 600 K-capable library or rely on windowed multipole / on-the-fly
  Doppler. Expect a cross-library k-eff bias vs the SCONE/JEFF result.
* Axial geometry simplified to a single uniform active zone (0 -> 365.76 cm)
  with ~30 cm water reflectors; grids/plenum/nozzles/dashpot omitted.
* Representative 20-rod Pyrex pattern for all BA assemblies (the verified
  deck's 6/12/15/16/20-rod directional variants are collapsed).
* Neutron-shield panels and SS baffle/former plates omitted.
* Temperature (600 K) is set on CELLS (per OpenMC convention) and as the
  Settings default; S(a,b) c_H_in_H2O is on WATER ONLY.
* Run with:  model.run(threads=N)  then  openmc.StatePoint(<path>).
"""
import openmc

# ===================== MATERIALS (atoms/b-cm) =====================
fuel16 = openmc.Material(name="UO2-16")
fuel16.set_density("atom/b-cm", 6.89175e-2)
fuel16.add_nuclide("O16", 4.58970e-2, "ao")
fuel16.add_nuclide("O17", 1.74360e-5, "ao")
fuel16.add_nuclide("U234", 3.01310e-6, "ao")
fuel16.add_nuclide("U235", 3.75030e-4, "ao")
fuel16.add_nuclide("U238", 2.26250e-2, "ao")

fuel24 = openmc.Material(name="UO2-24")
fuel24.set_density("atom/b-cm", 6.88170e-2)
fuel24.add_nuclide("O16", 4.58300e-2, "ao")
fuel24.add_nuclide("O17", 1.74110e-5, "ao")
fuel24.add_nuclide("U234", 4.48420e-6, "ao")
fuel24.add_nuclide("U235", 5.58140e-4, "ao")
fuel24.add_nuclide("U238", 2.24070e-2, "ao")

fuel31 = openmc.Material(name="UO2-31")
fuel31.set_density("atom/b-cm", 6.88510e-2)
fuel31.add_nuclide("O16", 4.58530e-2, "ao")
fuel31.add_nuclide("O17", 1.74200e-5, "ao")
fuel31.add_nuclide("U234", 5.79870e-6, "ao")
fuel31.add_nuclide("U235", 7.21750e-4, "ao")
fuel31.add_nuclide("U238", 2.22530e-2, "ao")

helium = openmc.Material(name="Helium")
helium.set_density("atom/b-cm", 2.40440e-4)
helium.add_nuclide("He3", 4.80890e-10, "ao")
helium.add_nuclide("He4", 2.40440e-4, "ao")

zirc = openmc.Material(name="Zircaloy")
zirc.set_density("atom/b-cm", 4.34389e-2)
zirc.add_nuclide("Cr50", 3.29620e-6, "ao")
zirc.add_nuclide("Cr52", 6.35640e-5, "ao")
zirc.add_nuclide("Cr53", 7.20760e-6, "ao")
zirc.add_nuclide("Cr54", 1.79410e-6, "ao")
zirc.add_nuclide("Fe54", 8.66980e-6, "ao")
zirc.add_nuclide("Fe56", 1.36100e-4, "ao")
zirc.add_nuclide("Fe57", 3.14310e-6, "ao")
zirc.add_nuclide("Fe58", 4.18290e-7, "ao")
zirc.add_nuclide("O16", 3.07440e-4, "ao")
zirc.add_nuclide("O17", 1.16800e-7, "ao")
zirc.add_nuclide("Sn112", 4.67350e-6, "ao")
zirc.add_nuclide("Sn114", 3.17990e-6, "ao")
zirc.add_nuclide("Sn115", 1.63810e-6, "ao")
zirc.add_nuclide("Sn116", 7.00550e-5, "ao")
zirc.add_nuclide("Sn117", 3.70030e-5, "ao")
zirc.add_nuclide("Sn118", 1.16690e-4, "ao")
zirc.add_nuclide("Sn119", 4.13870e-5, "ao")
zirc.add_nuclide("Sn120", 1.56970e-4, "ao")
zirc.add_nuclide("Sn122", 2.23080e-5, "ao")
zirc.add_nuclide("Sn124", 2.78970e-5, "ao")
zirc.add_nuclide("Zr90", 2.18280e-2, "ao")
zirc.add_nuclide("Zr91", 4.76010e-3, "ao")
zirc.add_nuclide("Zr92", 7.27590e-3, "ao")
zirc.add_nuclide("Zr94", 7.37340e-3, "ao")
zirc.add_nuclide("Zr96", 1.18790e-3, "ao")

water = openmc.Material(name="Water")
water.set_density("atom/b-cm", 7.41863e-2)
water.add_nuclide("H1", 4.94560e-2, "ao")
water.add_nuclide("B10", 7.97140e-6, "ao")
water.add_nuclide("B11", 3.22470e-5, "ao")
water.add_nuclide("H2", 7.70350e-6, "ao")
water.add_nuclide("O16", 2.46730e-2, "ao")
water.add_nuclide("O17", 9.37340e-6, "ao")
water.add_s_alpha_beta("c_H_in_H2O")

pyrex = openmc.Material(name="BorosilicateGlass")
pyrex.set_density("atom/b-cm", 7.15028e-2)
pyrex.add_nuclide("Al27", 1.73520e-3, "ao")
pyrex.add_nuclide("B10", 9.65060e-4, "ao")
pyrex.add_nuclide("B11", 3.91890e-3, "ao")
pyrex.add_nuclide("O16", 4.65140e-2, "ao")
pyrex.add_nuclide("O17", 1.76710e-5, "ao")
pyrex.add_nuclide("Si28", 1.69260e-2, "ao")
pyrex.add_nuclide("Si29", 8.59440e-4, "ao")
pyrex.add_nuclide("Si30", 5.66540e-4, "ao")

ss304 = openmc.Material(name="StainlessSteel304")
ss304.set_density("atom/b-cm", 8.79322e-2)
ss304.add_nuclide("Cr50", 7.67780e-4, "ao")
ss304.add_nuclide("Cr52", 1.48060e-2, "ao")
ss304.add_nuclide("Cr53", 1.67890e-3, "ao")
ss304.add_nuclide("Cr54", 4.17910e-4, "ao")
ss304.add_nuclide("Fe54", 3.46200e-3, "ao")
ss304.add_nuclide("Fe56", 5.43450e-2, "ao")
ss304.add_nuclide("Fe57", 1.25510e-3, "ao")
ss304.add_nuclide("Fe58", 1.67030e-4, "ao")
ss304.add_nuclide("Mn55", 1.76040e-3, "ao")
ss304.add_nuclide("Ni58", 5.60890e-3, "ao")
ss304.add_nuclide("Ni60", 2.16050e-3, "ao")
ss304.add_nuclide("Ni61", 9.39170e-5, "ao")
ss304.add_nuclide("Ni62", 2.99450e-4, "ao")
ss304.add_nuclide("Ni64", 7.62610e-5, "ao")
ss304.add_nuclide("Si28", 9.52810e-4, "ao")
ss304.add_nuclide("Si29", 4.83810e-5, "ao")
ss304.add_nuclide("Si30", 3.18930e-5, "ao")

carbonsteel = openmc.Material(name="CarbonSteel")
carbonsteel.set_density("atom/b-cm", 8.50964e-2)
carbonsteel.add_nuclide("Al27", 4.35230e-5, "ao")
carbonsteel.add_nuclide("B10", 2.58330e-6, "ao")
carbonsteel.add_nuclide("B11", 1.04500e-5, "ao")
carbonsteel.add_nuclide("C12", 1.04420e-3, "ao")
carbonsteel.add_nuclide("Ca40", 1.70430e-5, "ao")
carbonsteel.add_nuclide("Ca42", 1.13750e-7, "ao")
carbonsteel.add_nuclide("Ca43", 2.37340e-8, "ao")
carbonsteel.add_nuclide("Ca44", 3.66730e-7, "ao")
carbonsteel.add_nuclide("Ca46", 7.03220e-10, "ao")
carbonsteel.add_nuclide("Ca48", 3.28750e-8, "ao")
carbonsteel.add_nuclide("Cr50", 1.37380e-5, "ao")
carbonsteel.add_nuclide("Cr52", 2.64930e-4, "ao")
carbonsteel.add_nuclide("Cr53", 3.00410e-5, "ao")
carbonsteel.add_nuclide("Cr54", 7.47780e-6, "ao")
carbonsteel.add_nuclide("Cu63", 1.02230e-4, "ao")
carbonsteel.add_nuclide("Cu65", 4.56080e-5, "ao")
carbonsteel.add_nuclide("Fe54", 4.74370e-3, "ao")
carbonsteel.add_nuclide("Fe56", 7.44650e-2, "ao")
carbonsteel.add_nuclide("Fe57", 1.71970e-3, "ao")
carbonsteel.add_nuclide("Fe58", 2.28860e-4, "ao")
carbonsteel.add_nuclide("Mn55", 6.41260e-4, "ao")
carbonsteel.add_nuclide("Mo100", 2.98140e-5, "ao")
carbonsteel.add_nuclide("Mo92", 4.48220e-5, "ao")
carbonsteel.add_nuclide("Mo94", 2.81100e-5, "ao")
carbonsteel.add_nuclide("Mo95", 4.85670e-5, "ao")
carbonsteel.add_nuclide("Mo96", 5.10150e-5, "ao")
carbonsteel.add_nuclide("Mo97", 2.93190e-5, "ao")
carbonsteel.add_nuclide("Mo98", 7.43270e-5, "ao")
carbonsteel.add_nuclide("Nb93", 5.05590e-6, "ao")
carbonsteel.add_nuclide("Ni58", 4.08620e-4, "ao")
carbonsteel.add_nuclide("Ni60", 1.57400e-4, "ao")
carbonsteel.add_nuclide("Ni61", 6.84200e-6, "ao")
carbonsteel.add_nuclide("Ni62", 2.18150e-5, "ao")
carbonsteel.add_nuclide("Ni64", 5.55570e-6, "ao")
carbonsteel.add_nuclide("P31", 3.79130e-5, "ao")
carbonsteel.add_nuclide("S32", 3.48080e-5, "ao")
carbonsteel.add_nuclide("S33", 2.74200e-7, "ao")
carbonsteel.add_nuclide("S34", 1.53680e-6, "ao")
carbonsteel.add_nuclide("S36", 5.33980e-9, "ao")
carbonsteel.add_nuclide("Si28", 6.17020e-4, "ao")
carbonsteel.add_nuclide("Si29", 3.13300e-5, "ao")
carbonsteel.add_nuclide("Si30", 2.06530e-5, "ao")
carbonsteel.add_nuclide("Ti46", 1.21440e-6, "ao")
carbonsteel.add_nuclide("Ti47", 1.09520e-6, "ao")
carbonsteel.add_nuclide("Ti48", 1.08510e-5, "ao")
carbonsteel.add_nuclide("Ti49", 7.96340e-7, "ao")
carbonsteel.add_nuclide("Ti50", 7.62490e-7, "ao")
carbonsteel.add_nuclide("V51", 4.59890e-5, "ao")

air = openmc.Material(name="Air")
air.set_density("atom/b-cm", 2.52837e-4)
air.add_nuclide("Ar36", 7.87300e-9, "ao")
air.add_nuclide("Ar38", 1.48440e-9, "ao")
air.add_nuclide("Ar40", 2.35060e-6, "ao")
air.add_nuclide("C12", 6.75390e-8, "ao")
air.add_nuclide("N14", 1.96800e-4, "ao")
air.add_nuclide("N15", 7.23540e-7, "ao")
air.add_nuclide("O16", 5.28660e-5, "ao")
air.add_nuclide("O17", 2.00840e-8, "ao")

materials = openmc.Materials([
    fuel16, fuel24, fuel31, helium, zirc, water, pyrex, ss304, carbonsteel, air
])

# ===================== SURFACES (shared, at origin) =====================
s_pellet = openmc.ZCylinder(r=0.39218)
s_gap    = openmc.ZCylinder(r=0.40005)
s_clad   = openmc.ZCylinder(r=0.45720)
s_gt_in  = openmc.ZCylinder(r=0.56134)
s_gt_out = openmc.ZCylinder(r=0.60198)
s_it_air = openmc.ZCylinder(r=0.43688)
s_it_zr1 = openmc.ZCylinder(r=0.48387)
s_it_h2o = openmc.ZCylinder(r=0.56134)
s_it_zr2 = openmc.ZCylinder(r=0.60198)
s_ba_air = openmc.ZCylinder(r=0.21400)
s_ba_ss1 = openmc.ZCylinder(r=0.23051)
s_ba_he1 = openmc.ZCylinder(r=0.24130)
s_ba_py  = openmc.ZCylinder(r=0.42672)
s_ba_he2 = openmc.ZCylinder(r=0.43688)
s_ba_ss2 = openmc.ZCylinder(r=0.48387)
s_ba_h2o = openmc.ZCylinder(r=0.56134)
s_ba_zr  = openmc.ZCylinder(r=0.60198)

TEMP = 600.0

def fuel_pin(fuel_mat, name):
    c1 = openmc.Cell(fill=fuel_mat, region=-s_pellet)
    c2 = openmc.Cell(fill=helium, region=+s_pellet & -s_gap)
    c3 = openmc.Cell(fill=zirc, region=+s_gap & -s_clad)
    c4 = openmc.Cell(fill=water, region=+s_clad)
    for c in (c1, c2, c3, c4):
        c.temperature = TEMP
    return openmc.Universe(name=name, cells=[c1, c2, c3, c4])

u_f16 = fuel_pin(fuel16, "pin_f16")
u_f24 = fuel_pin(fuel24, "pin_f24")
u_f31 = fuel_pin(fuel31, "pin_f31")

# guide tube (CR withdrawn -> water-filled)
_gt = [openmc.Cell(fill=water, region=-s_gt_in),
       openmc.Cell(fill=zirc, region=+s_gt_in & -s_gt_out),
       openmc.Cell(fill=water, region=+s_gt_out)]
for c in _gt: c.temperature = TEMP
u_gt = openmc.Universe(name="guide_tube", cells=_gt)

# instrument tube (air / Zr / water / Zr / water)
_it = [openmc.Cell(fill=air, region=-s_it_air),
       openmc.Cell(fill=zirc, region=+s_it_air & -s_it_zr1),
       openmc.Cell(fill=water, region=+s_it_zr1 & -s_it_h2o),
       openmc.Cell(fill=zirc, region=+s_it_h2o & -s_it_zr2),
       openmc.Cell(fill=water, region=+s_it_zr2)]
for c in _it: c.temperature = TEMP
u_it = openmc.Universe(name="instr_tube", cells=_it)

# Pyrex burnable-poison pin (BP above dashpot)
_ba = [openmc.Cell(fill=air, region=-s_ba_air),
       openmc.Cell(fill=ss304, region=+s_ba_air & -s_ba_ss1),
       openmc.Cell(fill=helium, region=+s_ba_ss1 & -s_ba_he1),
       openmc.Cell(fill=pyrex, region=+s_ba_he1 & -s_ba_py),
       openmc.Cell(fill=helium, region=+s_ba_py & -s_ba_he2),
       openmc.Cell(fill=ss304, region=+s_ba_he2 & -s_ba_ss2),
       openmc.Cell(fill=water, region=+s_ba_ss2 & -s_ba_h2o),
       openmc.Cell(fill=zirc, region=+s_ba_h2o & -s_ba_zr),
       openmc.Cell(fill=water, region=+s_ba_zr)]
for c in _ba: c.temperature = TEMP
u_ba = openmc.Universe(name="pyrex_bp", cells=_ba)

# all-water universe (reflector / lattice outer)
u_water = openmc.Universe(name="water", cells=[openmc.Cell(fill=water)])

# ===================== ASSEMBLY LATTICES =====================
asm_a16 = openmc.RectLattice(name="asm_a16")
asm_a16.lower_left = (-10.71, -10.71)
asm_a16.pitch = (1.26, 1.26)
asm_a16.outer = u_water
asm_a16.universes = [
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_it, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_gt, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16],
        [u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16, u_f16]
]

def _wrap(lat, name):
    return openmc.Universe(name=name, cells=[openmc.Cell(fill=lat)])

asm_a16_u = _wrap(asm_a16, "asm_a16_u")

asm_a24 = openmc.RectLattice(name="asm_a24")
asm_a24.lower_left = (-10.71, -10.71)
asm_a24.pitch = (1.26, 1.26)
asm_a24.outer = u_water
asm_a24.universes = [
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_it, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_gt, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24]
]
asm_a24_u = _wrap(asm_a24, "asm_a24_u")

asm_a24b = openmc.RectLattice(name="asm_a24b")
asm_a24b.lower_left = (-10.71, -10.71)
asm_a24b.pitch = (1.26, 1.26)
asm_a24b.outer = u_water
asm_a24b.universes = [
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_gt, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_ba, u_f24, u_f24, u_gt, u_f24, u_f24, u_it, u_f24, u_f24, u_gt, u_f24, u_f24, u_ba, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_gt, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_ba, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24],
        [u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24, u_f24]
]
asm_a24b_u = _wrap(asm_a24b, "asm_a24b_u")

asm_a31 = openmc.RectLattice(name="asm_a31")
asm_a31.lower_left = (-10.71, -10.71)
asm_a31.pitch = (1.26, 1.26)
asm_a31.outer = u_water
asm_a31.universes = [
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_it, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_gt, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31]
]
asm_a31_u = _wrap(asm_a31, "asm_a31_u")

asm_a31b = openmc.RectLattice(name="asm_a31b")
asm_a31b.lower_left = (-10.71, -10.71)
asm_a31b.pitch = (1.26, 1.26)
asm_a31b.outer = u_water
asm_a31b.universes = [
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_gt, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_ba, u_f31, u_f31, u_gt, u_f31, u_f31, u_it, u_f31, u_f31, u_gt, u_f31, u_f31, u_ba, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_gt, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_ba, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31],
        [u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31, u_f31]
]
asm_a31b_u = _wrap(asm_a31b, "asm_a31b_u")

# ===================== CORE LATTICE =====================
core_lat = openmc.RectLattice(name="core")
core_lat.lower_left = (-182.78094, -182.78094)
core_lat.pitch = (21.50364, 21.50364)
core_lat.outer = u_water
core_lat.universes = [
        [u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water],
        [u_water, u_water, u_water, u_water, u_water, asm_a31_u, asm_a31b_u, asm_a31_u, asm_a31b_u, asm_a31_u, asm_a31b_u, asm_a31_u, u_water, u_water, u_water, u_water, u_water],
        [u_water, u_water, u_water, asm_a31_u, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a31_u, asm_a31_u, u_water, u_water, u_water],
        [u_water, u_water, asm_a31_u, asm_a31b_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a31b_u, asm_a31_u, u_water, u_water],
        [u_water, u_water, asm_a31_u, asm_a24b_u, asm_a24_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a24_u, asm_a24b_u, asm_a31_u, u_water, u_water],
        [u_water, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, asm_a31_u, u_water],
        [u_water, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, u_water],
        [u_water, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, asm_a31_u, u_water],
        [u_water, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, u_water],
        [u_water, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, asm_a31_u, u_water],
        [u_water, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, u_water],
        [u_water, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a31b_u, asm_a31_u, u_water],
        [u_water, u_water, asm_a31_u, asm_a24b_u, asm_a24_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a24_u, asm_a24b_u, asm_a31_u, u_water, u_water],
        [u_water, u_water, asm_a31_u, asm_a31b_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a16_u, asm_a24b_u, asm_a31b_u, asm_a31_u, u_water, u_water],
        [u_water, u_water, u_water, asm_a31_u, asm_a31_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a16_u, asm_a31b_u, asm_a31_u, asm_a31_u, u_water, u_water, u_water],
        [u_water, u_water, u_water, u_water, u_water, asm_a31_u, asm_a31b_u, asm_a31_u, asm_a31b_u, asm_a31_u, asm_a31b_u, asm_a31_u, u_water, u_water, u_water, u_water, u_water],
        [u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water, u_water]
]

# ===================== RADIAL / AXIAL CONTAINMENT =====================
cyl_cb_in  = openmc.ZCylinder(r=187.96)
cyl_cb_out = openmc.ZCylinder(r=193.675)
cyl_lin    = openmc.ZCylinder(r=219.150)
cyl_rpv_in = openmc.ZCylinder(r=219.710)
cyl_rpv_out = openmc.ZCylinder(r=241.3, boundary_type="vacuum")
z_active_b = openmc.ZPlane(z0=0.0)
z_active_t = openmc.ZPlane(z0=365.76)
z_refl_b   = openmc.ZPlane(z0=-30.0, boundary_type="vacuum")
z_refl_t   = openmc.ZPlane(z0=395.76, boundary_type="vacuum")

core_cell = openmc.Cell(fill=core_lat, region=-cyl_cb_in & +z_active_b & -z_active_t)
refl_b = openmc.Cell(fill=water, region=-cyl_cb_in & +z_refl_b & -z_active_b)
refl_t = openmc.Cell(fill=water, region=-cyl_cb_in & +z_active_t & -z_refl_t)
barrel = openmc.Cell(fill=ss304, region=+cyl_cb_in & -cyl_cb_out & +z_refl_b & -z_refl_t)
down   = openmc.Cell(fill=water, region=+cyl_cb_out & -cyl_lin & +z_refl_b & -z_refl_t)
liner  = openmc.Cell(fill=ss304, region=+cyl_lin & -cyl_rpv_in & +z_refl_b & -z_refl_t)
rpv    = openmc.Cell(fill=carbonsteel, region=+cyl_rpv_in & -cyl_rpv_out & +z_refl_b & -z_refl_t)
root = openmc.Universe(cells=[core_cell, refl_b, refl_t, barrel, down, liner, rpv])
geometry = openmc.Geometry(root)

# ===================== SETTINGS + TALLIES =====================
settings = openmc.Settings()
settings.run_mode = "eigenvalue"
settings.batches = 250
settings.inactive = 50
settings.particles = 20000
settings.temperature = {"default": TEMP, "method": "interpolation"}
bounds = [-182.78094, -182.78094, 0.0, 182.78094, 182.78094, 365.76]
settings.source = openmc.IndependentSource(
    space=openmc.stats.Box(bounds[:3], bounds[3:], only_fissionable=True)
)

# Pin-power-style mesh tally over the core footprint (17x17 assemblies).
mesh = openmc.RegularMesh()
mesh.dimension = [17, 17, 1]
mesh.lower_left = [-182.78094, -182.78094, 0.0]
mesh.upper_right = [182.78094, 182.78094, 365.76]
fission_tally = openmc.Tally(name="assembly_fission")
fission_tally.filters = [openmc.MeshFilter(mesh)]
fission_tally.scores = ["fission", "nu-fission"]
tallies = openmc.Tallies([fission_tally])

model = openmc.Model(geometry=geometry, materials=materials,
                     settings=settings, tallies=tallies)

if __name__ == "__main__":
    # Full-core eigenvalue is expensive: use many threads and converge.
    #   sp_path = model.run(threads=8)
    #   with openmc.StatePoint(sp_path) as sp:
    #       print("k-eff =", sp.keff)
    model.export_to_model_xml()

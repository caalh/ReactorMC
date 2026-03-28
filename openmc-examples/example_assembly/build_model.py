#!/usr/bin/env python3
"""17×17 PWR assembly — matches ReactorMC /openmc/example-assembly/.

Requires: OpenMC 0.15.x, OPENMC_CROSS_SECTIONS pointing at cross_sections.xml.
"""
from __future__ import annotations

import os
import sys

import numpy as np
import openmc


def _require_xs() -> None:
    if not os.environ.get("OPENMC_CROSS_SECTIONS"):
        print(
            "ERROR: Set OPENMC_CROSS_SECTIONS to your cross_sections.xml "
            "(see openmc-examples/README.md).",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    _require_xs()

    # —— MATERIALS ——
    fuel = openmc.Material(name="UO2 Fuel")
    fuel.set_density("g/cm3", 10.4)
    fuel.add_nuclide("U235", 0.045)
    fuel.add_nuclide("U238", 0.955)
    fuel.add_element("O", 2.0)

    clad = openmc.Material(name="Zircaloy-4")
    clad.set_density("g/cm3", 6.55)
    clad.add_element("Zr", 0.982)
    clad.add_element("Sn", 0.015)
    clad.add_element("Fe", 0.002)
    clad.add_element("Cr", 0.001)

    water = openmc.Material(name="Light Water")
    water.set_density("g/cm3", 1.0)
    water.add_nuclide("H1", 2.0)
    water.add_element("O", 1.0)
    water.add_s_alpha_beta("c_H_in_H2O")

    steel = openmc.Material(name="Stainless Steel")
    steel.set_density("g/cm3", 8.0)
    steel.add_element("Fe", 0.68)
    steel.add_element("Cr", 0.20)
    steel.add_element("Ni", 0.12)

    materials = openmc.Materials([fuel, clad, water, steel])

    # —— PIN UNIVERSES ——
    def create_fuel_pin():
        fuel_radius = 0.4096
        clad_inner = 0.4178
        clad_outer = 0.4750

        fuel_surf = openmc.ZCylinder(r=fuel_radius)
        clad_inner_surf = openmc.ZCylinder(r=clad_inner)
        clad_outer_surf = openmc.ZCylinder(r=clad_outer)

        fuel_region = -fuel_surf
        gap_region = +fuel_surf & -clad_inner_surf
        clad_region = +clad_inner_surf & -clad_outer_surf
        water_region = +clad_outer_surf

        fuel_cell = openmc.Cell(fill=fuel, region=fuel_region)
        gap_cell = openmc.Cell(fill=None, region=gap_region)
        clad_cell = openmc.Cell(fill=clad, region=clad_region)
        water_cell = openmc.Cell(fill=water, region=water_region)

        return openmc.Universe(cells=[fuel_cell, gap_cell, clad_cell, water_cell])

    def create_guide_tube():
        guide_inner = 0.5610
        guide_outer = 0.6020

        guide_inner_surf = openmc.ZCylinder(r=guide_inner)
        guide_outer_surf = openmc.ZCylinder(r=guide_outer)

        water_inner = -guide_inner_surf
        tube_region = +guide_inner_surf & -guide_outer_surf
        water_outer = +guide_outer_surf

        water_inner_cell = openmc.Cell(fill=water, region=water_inner)
        tube_cell = openmc.Cell(fill=steel, region=tube_region)
        water_outer_cell = openmc.Cell(fill=water, region=water_outer)

        return openmc.Universe(cells=[water_inner_cell, tube_cell, water_outer_cell])

    def create_instrumentation_tube():
        tube_inner = 0.5590
        tube_outer = 0.6050

        tube_inner_surf = openmc.ZCylinder(r=tube_inner)
        tube_outer_surf = openmc.ZCylinder(r=tube_outer)

        water_inner = -tube_inner_surf
        tube_region = +tube_inner_surf & -tube_outer_surf
        water_outer = +tube_outer_surf

        water_inner_cell = openmc.Cell(fill=water, region=water_inner)
        tube_cell = openmc.Cell(fill=steel, region=tube_region)
        water_outer_cell = openmc.Cell(fill=water, region=water_outer)

        return openmc.Universe(cells=[water_inner_cell, tube_cell, water_outer_cell])

    fuel_pin = create_fuel_pin()
    guide_tube = create_guide_tube()
    instr_tube = create_instrumentation_tube()

    # —— LATTICE ——
    lattice = openmc.RectLattice(name="Assembly Lattice")
    lattice.lower_left = [-10.71, -10.71]
    lattice.pitch = [1.26, 1.26]

    # Same 17×17 map as src/pages/openmc/ExampleAssembly.tsx
    assembly_pattern = [
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "G", "F", "F", "F", "F", "F", "F", "F", "F", "F", "G", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "G", "F", "F", "G", "F", "F", "I", "F", "F", "G", "F", "F", "G", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "G", "F", "F", "F", "F", "F", "F", "F", "F", "F", "G", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "G", "F", "F", "G", "F", "F", "G", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
    ]

    universe_map = {"F": fuel_pin, "G": guide_tube, "I": instr_tube}
    lattice_universes = [
        [universe_map[s] for s in row] for row in assembly_pattern
    ]
    lattice.universes = lattice_universes

    # —— ASSEMBLY GEOMETRY ——
    pitch = 1.26
    assembly_size = 17 * pitch

    assembly_left = openmc.XPlane(-assembly_size / 2, boundary_type="reflective")
    assembly_right = openmc.XPlane(assembly_size / 2, boundary_type="reflective")
    assembly_bottom = openmc.YPlane(-assembly_size / 2, boundary_type="reflective")
    assembly_top = openmc.YPlane(assembly_size / 2, boundary_type="reflective")
    assembly_lower = openmc.ZPlane(-200, boundary_type="vacuum")
    assembly_upper = openmc.ZPlane(200, boundary_type="vacuum")

    assembly_region = (
        +assembly_left
        & -assembly_right
        & +assembly_bottom
        & -assembly_top
        & +assembly_lower
        & -assembly_upper
    )

    assembly_cell = openmc.Cell(fill=lattice, region=assembly_region)
    root_universe = openmc.Universe(cells=[assembly_cell])
    geometry = openmc.Geometry(root_universe)

    for cell in geometry.get_all_cells().values():
        if cell.fill is fuel:
            cell.temperature = 900
        elif cell.fill in (clad, steel):
            cell.temperature = 600
        elif cell.fill is water:
            cell.temperature = 574

    # —— SETTINGS ——
    settings = openmc.Settings()
    settings.particles = 10000
    settings.batches = 120
    settings.inactive = 20

    source_box = openmc.stats.Box(
        [-assembly_size / 2, -assembly_size / 2, -100],
        [assembly_size / 2, assembly_size / 2, 100],
    )
    settings.source = openmc.IndependentSource(space=source_box)

    # —— TALLIES ——
    tallies = openmc.Tallies()

    assembly_tally = openmc.Tally(name="assembly_avg")
    assembly_tally.filters = [openmc.CellFilter(assembly_cell)]
    assembly_tally.scores = ["flux", "fission", "absorption", "nu-fission"]
    tallies.append(assembly_tally)

    mesh = openmc.RegularMesh()
    mesh.lower_left = [-assembly_size / 2, -assembly_size / 2]
    mesh.upper_right = [assembly_size / 2, assembly_size / 2]
    mesh.dimension = [17, 17]

    mesh_tally = openmc.Tally(name="pin_powers")
    mesh_tally.filters = [openmc.MeshFilter(mesh)]
    mesh_tally.scores = ["kappa-fission"]
    tallies.append(mesh_tally)

    energy_bins = np.logspace(-3, 7, 50)
    energy_filter = openmc.EnergyFilter(energy_bins)

    spectrum_tally = openmc.Tally(name="fuel_spectrum")
    spectrum_tally.filters = [openmc.MaterialFilter([fuel]), energy_filter]
    spectrum_tally.scores = ["flux"]
    tallies.append(spectrum_tally)

    model = openmc.Model(geometry, materials, settings, tallies)

    statepoint_path = model.run()
    sp = openmc.StatePoint(statepoint_path)
    keff = sp.keff
    print(f"k-effective: {keff.nominal_value:.5f}")
    print(f"Standard deviation: {keff.std_dev:.5f}")

    pin_powers = sp.get_tally(name="pin_powers")
    power_array = pin_powers.mean.reshape((17, 17))
    max_power = float(np.max(power_array))
    avg_power = float(np.mean(power_array))
    peaking_factor = max_power / avg_power
    print(f"Peak-to-average power ratio: {peaking_factor:.3f}")
    peak_location = np.unravel_index(int(np.argmax(power_array)), power_array.shape)
    print(f"Peak power at pin ({peak_location[0] + 1}, {peak_location[1] + 1})")


if __name__ == "__main__":
    main()

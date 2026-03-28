#!/usr/bin/env python3
"""PWR pin cell — matches ReactorMC /openmc/example-pin/ (materials, geometry, settings, tallies).

Requires: OpenMC 0.15.x, OPENMC_CROSS_SECTIONS pointing at cross_sections.xml.
"""
from __future__ import annotations

import os
import sys

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

    materials = openmc.Materials([fuel, clad, water])

    # —— GEOMETRY ——
    fuel_radius = 0.4096
    clad_radius = 0.4750
    pitch = 1.26

    fuel_outer = openmc.ZCylinder(r=fuel_radius)
    clad_outer = openmc.ZCylinder(r=clad_radius)

    left = openmc.XPlane(-pitch / 2, boundary_type="reflective")
    right = openmc.XPlane(pitch / 2, boundary_type="reflective")
    bottom = openmc.YPlane(-pitch / 2, boundary_type="reflective")
    top = openmc.YPlane(pitch / 2, boundary_type="reflective")

    fuel_region = -fuel_outer
    clad_region = +fuel_outer & -clad_outer
    water_region = +clad_outer & +left & -right & +bottom & -top

    fuel_cell = openmc.Cell(fill=fuel, region=fuel_region)
    clad_cell = openmc.Cell(fill=clad, region=clad_region)
    water_cell = openmc.Cell(fill=water, region=water_region)

    universe = openmc.Universe(cells=[fuel_cell, clad_cell, water_cell])
    geometry = openmc.Geometry(universe)

    # —— SETTINGS ——
    settings = openmc.Settings()
    settings.particles = 10000
    settings.batches = 100
    settings.inactive = 20

    source_region = openmc.stats.Box(
        [-fuel_radius, -fuel_radius, -1],
        [fuel_radius, fuel_radius, 1],
    )
    settings.source = openmc.IndependentSource(space=source_region)

    # —— TALLIES ——
    tallies = openmc.Tallies()

    fuel_tally = openmc.Tally(name="fuel flux")
    fuel_tally.filters = [openmc.CellFilter(fuel_cell)]
    fuel_tally.scores = ["flux", "nu-fission", "absorption"]
    tallies.append(fuel_tally)

    clad_tally = openmc.Tally(name="clad flux")
    clad_tally.filters = [openmc.CellFilter(clad_cell)]
    clad_tally.scores = ["flux", "absorption"]
    tallies.append(clad_tally)

    water_tally = openmc.Tally(name="water flux")
    water_tally.filters = [openmc.CellFilter(water_cell)]
    water_tally.scores = ["flux", "absorption"]
    tallies.append(water_tally)

    model = openmc.Model(geometry, materials, settings, tallies)

    statepoint_path = model.run()
    sp = openmc.StatePoint(statepoint_path)
    keff = sp.keff
    print(f"k-effective: {keff.nominal_value:.5f} ± {keff.std_dev:.5f}")

    fuel_flux = sp.get_tally(name="fuel flux")
    clad_flux = sp.get_tally(name="clad flux")
    water_flux = sp.get_tally(name="water flux")

    print("\nFlux Results:")
    print(
        f"Fuel flux:  {fuel_flux.mean[0, 0, 0]:.3e} ± {fuel_flux.std_dev[0, 0, 0]:.3e}"
    )
    print(
        f"Clad flux:  {clad_flux.mean[0, 0, 0]:.3e} ± {clad_flux.std_dev[0, 0, 0]:.3e}"
    )
    print(
        f"Water flux: {water_flux.mean[0, 0, 0]:.3e} ± {water_flux.std_dev[0, 0, 0]:.3e}"
    )

    nu_fission_rate = fuel_flux.get_slice(scores=["nu-fission"])
    absorption_rate = fuel_flux.get_slice(scores=["absorption"])

    print("\nReaction Rates in Fuel:")
    print(f"Nu-fission rate: {nu_fission_rate.mean[0, 0, 0]:.3e}")
    print(f"Absorption rate: {absorption_rate.mean[0, 0, 0]:.3e}")
    eta = nu_fission_rate.mean[0, 0, 0] / absorption_rate.mean[0, 0, 0]
    print(f"Eta (η = νΣ_f/Σ_a): {eta:.3f}")
    print("\nSimulation completed successfully!")


if __name__ == "__main__":
    main()

# OpenMC example inputs (ReactorMC)

Runnable Python models aligned with the **OpenMC** tutorial pages on [reactormc.net](https://reactormc.net). A public mirror of this folder (with SCONE decks) lives at **[github.com/caalh/ReactorMC](https://github.com/caalh/ReactorMC)** under `openmc-examples/`. There is **no** bundled nuclear-data library here—you must install OpenMC and HDF5 cross sections locally.

## Tested stack

- **OpenMC 0.15.x** (changelog: 0.15.3 via conda-forge, WSL2 Ubuntu)
- **ENDF/B-VII.1** continuous-energy HDF5 library (typical path set via `OPENMC_CROSS_SECTIONS`)

## Prerequisites

1. Install [OpenMC](https://docs.openmc.org/) and nuclear data (e.g. from [openmc.org](https://openmc.org/) or conda-forge data packages).
2. Set the environment variable pointing at your **cross_sections.xml** (or equivalent):

   ```bash
   export OPENMC_CROSS_SECTIONS=/path/to/cross_sections.xml
   ```

   On PowerShell:

   ```powershell
   $env:OPENMC_CROSS_SECTIONS = "C:\path\to\cross_sections.xml"
   ```

## Layout

| Directory | ReactorMC page |
|-----------|----------------|
| `example_pin/` | [/openmc/example-pin/](https://reactormc.net/openmc/example-pin/) |
| `example_assembly/` | [/openmc/example-assembly/](https://reactormc.net/openmc/example-assembly/) |

## Full-core deck

- `beavrs_fullcore.py` — **BEAVRS Cycle 1 full-core PWR translation (community
  example deck).** Geometry + material number densities translated from the
  author-verified Cambridge SCONE BEAVRS deck and the MIT BEAVRS rev 2.0.2 spec.
  Builds a real 193-assembly loading map (1.6/2.4/3.1 wt% UO2) of 17×17
  `RectLattice` assemblies (24 guide tubes + central instrument tube), Pyrex
  burnable-poison rods, control rods withdrawn, core barrel/RPV; vacuum
  boundaries. Uses `openmc.IndependentSource`, `openmc.Material.set_density`
  with atom densities, temperature (600 K) set on **cells**, `c_H_in_H2O`
  S(α,β) on water only. Run `model.run(threads=N)` then
  `openmc.StatePoint(path)`. **NOT benchmark-validated.** Flagged
  simplifications: number densities are the verified deck's JEF-3.1.1 600 K
  values but whatever library `OPENMC_CROSS_SECTIONS` points at is used
  (cross-library k-eff bias expected); single uniform active-fuel axial zone
  (no grids/plenum/nozzles); representative 20-rod Pyrex pattern; neutron-shield/
  baffle plates omitted. Not an official MIT/CRPG product.

## Run all (optional)

From this directory, after `OPENMC_CROSS_SECTIONS` is set:

```bash
chmod +x run_all.sh
./run_all.sh
```

```powershell
.\run_all.ps1
```

Each example runs in its own working directory so OpenMC XML/HDF5 outputs do not collide.

## Policy (maintainers)

When you change the “complete model” code on `ExamplePin.tsx` or `ExampleAssembly.tsx`, update the matching `build_model.py` here and re-run locally. See `docs/TUTORIAL_STATUS.md` and `VERIFICATION_SUMMARY.md`.

## Related

- **SCONE** machine-checked inputs: `scone-examples/verify/` + `run_all.ps1` (testLib, no full ACE install).

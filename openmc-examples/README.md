# OpenMC example inputs (ReactorMC)

Runnable Python models aligned with the **OpenMC** tutorial pages on [reactormc.net](https://reactormc.net). These are the spiritual counterpart to `scone-examples/verify/`: there is **no** bundled nuclear-data library here—you must install OpenMC and HDF5 cross sections locally.

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

When you change the “complete model” code on `ExamplePin.tsx` or `ExampleAssembly.tsx`, update the matching `build_model.py` here and re-run locally. See `docs/CROSS_CODE_TUTORIAL_REVIEW.md` and `VERIFICATION_SUMMARY.md`.

## Related

- **SCONE** machine-checked inputs: `scone-examples/verify/` + `run_all.ps1` (testLib, no full ACE install).

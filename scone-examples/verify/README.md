# SCONE Verification Tests

These inputs run with SCONE's built-in `IntegrationTestFiles/testLib` (no full ACE library required).

## Policy (ReactorMC)

**Aggressive + verify when needed:** Any SCONE **full deck** on the tutorial site must either appear here (and in `run_all.ps1`) and be shown with `?raw`, **or** be **labeled on the page** as not in this harness (production ACE, excerpt only, etc.). See `.cursor/rules/scone-coding.mdc` → *Full-deck policy*. When you add or change a full deck, prefer adding a testLib twin and registering it here.

## Obtaining these files

They live under **`scone-examples/verify/`** in the ReactorMC website repository. If the canonical Git remote is **private**, use the clone or archive URL your organization provides—the on-disk layout is unchanged. For a **public** educational mirror, prefer linking or cloning that URL so readers can run `run_all.ps1` locally.

## Prerequisites

- SCONE built at `C:\Users\calho\Documents\GitHub\SCONE` (or equivalent)
- WSL (for `run_all.ps1`) or native Linux

## Run All Tests

From this directory:

```powershell
.\run_all.ps1
```

Or manually (from SCONE directory):

```bash
export SCONE_ACE=IntegrationTestFiles/testLib
./build/scone.out ../reactor-monte-carlo-guide/scone-examples/verify/test_simple_bare_sphere
./build/scone.out ../reactor-monte-carlo-guide/scone-examples/verify/test_simple_fuel_pin
```

## Verified Tests (`run_all.ps1`, 15 decks)

| Test | Status | Notes |
|------|--------|------|
| test_simple_bare_sphere | PASS | U-235 cylinder, k-eff ~0.65 |
| test_simple_fuel_pin | PASS | Pin cell with U-235 + water, k-eff ~0.08 |
| tutorial_fuel_pin_testlib | PASS | SimpleExamples fuelPinExample structure |
| tutorial_bare_sphere_testlib | PASS | SimpleExamples bareSphereExample structure |
| tutorial_scone_tsx_testlib | PASS | SCONE landing (`SCONE.tsx` `?raw`); pinUniverse + `$SCONE_ACE` |
| tutorial_config_testlib | PASS | Config.tsx block structure (simplified geometry) |
| tutorial_troubleshooting_smoke | PASS | Small eigen deck (testLib nuclides) |
| tutorial_troubleshooting_boundary | PASS | Single-cylinder boundary check |
| tutorial_shielding_slab | PASS | Fixed-source slab (Water stand-in), testLib |
| tutorial_assembly_5x5_testlib | PASS | 5×5 latUniverse; pin fills sized to match `radii` (incl. trailing `0.0`) |
| tutorial_bare_sphere_clean | PASS | zTruncCylinder stand-in sphere, testLib |
| tutorial_basics_celluniverse_testlib | PASS | Basics page cellUniverse topology; testLib stand-ins |
| tutorial_examples_hub_testlib | PASS | Examples hub merged full input |
| tutorial_parallel_eigen_sample_testlib | PASS | Parallel page complete eigen sample |
| tutorial_nuclear_data_basic_testlib | PASS | NuclearData page; PWR pin names; testLib compositions |

**Not in `run_all.ps1`:** `tutorial_shielding_slab_production` — Air/Concrete + ZAID `.06`; needs a full ACE library on `SCONE_ACE` (geometry parses; testLib fails at ACE load).

## Nuclides in testLib

- 1001.03 (H), 8016.03 (O), 92235.03 (U-235), 92233.03 (U-233), 6012.06 (C)
- Thermal S(α,β): h-h2o.49t, h-h2o.50t, grph30.46t

The tutorial examples on the Simple Examples page use production ZAIDs (.06, Zr, Pu, etc.) and require a full JEF-3.1.1 or ENDF/B-VII.1 ACE library.

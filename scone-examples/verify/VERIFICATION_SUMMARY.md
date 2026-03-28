# SCONE Code Verification Summary

**Status: 15/15 tests in `run_all.ps1`** (90%+ confidence for anchored full decks; see `docs/CROSS_CODE_TUTORIAL_REVIEW.md`)

## Process (maintainers)

All 15 decks in `run_all.ps1` were run locally against a SCONE build with `SCONE_ACE=IntegrationTestFiles/testLib`. Pass = run completed without error. Not in that harness: full BEAVRS, production-only snippets without a verify twin, `tutorial_shielding_slab_production` (full ACE).

## Verified Inputs (testLib)

| Input | Page | Notes |
|-------|------|-------|
| test_simple_fuel_pin | - | Minimal pin cell |
| test_simple_bare_sphere | - | Minimal sphere |
| tutorial_fuel_pin_testlib | SimpleExamples | pinUniverse |
| tutorial_bare_sphere_testlib | SimpleExamples | cellUniverse |
| tutorial_bare_sphere_clean | SimpleExamples / sphere note | zTruncCylinder stand-in |
| tutorial_scone_tsx_testlib | SCONE.tsx (`?raw`) | Landing sample; pinUniverse; `$SCONE_ACE` |
| tutorial_config_testlib | Config | Simplified pin cell |
| tutorial_troubleshooting_smoke | Troubleshooting | UO2+Water only (testLib) |
| tutorial_troubleshooting_boundary | Troubleshooting | Single cylinder |
| tutorial_shielding_slab | ShieldingExamples | fixedSource, Water, box root |
| tutorial_assembly_5x5_testlib | ReactorExamples | 5×5 latUniverse; `radii`/`fills` same length |
| tutorial_basics_celluniverse_testlib | Basics (`?raw`) | cellUniverse pin; testLib stand-ins |
| tutorial_examples_hub_testlib | Examples (`?raw`) | Merged hub patterns, runnable |
| tutorial_parallel_eigen_sample_testlib | Parallel (`?raw`) | Complete eigen deck (no `...`) |
| tutorial_nuclear_data_basic_testlib | NuclearData (`?raw`) | PWR pin names; testLib compositions; `$SCONE_ACE` |

**Manual (full ACE):** `tutorial_shielding_slab_production` — same geometry as slab tutorial; Air/Concrete + ZAID `.06` (geometry verified; testLib fails at ACE load).

## Run Command

```bash
cd /mnt/c/Users/calho/Documents/GitHub/SCONE
export SCONE_ACE=IntegrationTestFiles/testLib
./build/scone.out /path/to/input
```

Or use `run_all.ps1` from `scone-examples/verify/`.

## Fixes Applied

- **ShieldingExamples**: Plane coeffs (1 0 0 d) use F=n·r−d; x=5 needs (1 0 0 5), not -5. Root must encompass cells (use box for bounded domains).
- **Troubleshooting smokeTestExample**: Production uses Zr, He, 92238; testLib version uses UO2+Water only.
- **cellUniverse vs pinUniverse**: Explicit cells with surfaces can cause "undefined material"; pinUniverse form runs reliably.

## Maintainer policy

**Aggressive + verify when needed:** Every SCONE **full deck** on the tutorial site is either listed here + shown via `?raw`, or **explicitly labeled** on the page as outside this harness. See `.cursor/rules/scone-coding.mdc` (*Full-deck policy*) and `docs/CROSS_CODE_TUTORIAL_REVIEW.md`.

**Sweep (2026-03-24):** Tutorial pages were audited so non-verify SCONE inputs/snippets have nearby or page-level “not in `run_all.ps1`” / excerpt language (bash/install blocks excluded).

## Unverified / Partial

- **BEAVRS** (`scone_beavrs_clean.inp`): Needs full ACE library (JEF/ENDF).
- **vizDebugExample**: viz block only; not a full runnable input.
- **cylinderShieldingSnippet**: Partial geometry; no full input.
- **Examples.tsx** top snippets: pedagogical fragments (production-style ZAIDs); full runnable merged deck is `tutorial_examples_hub_testlib`.
- **Materials, Geometry, Transport** (and similar): Snippets/fragments unless linked to a verify file; syntax checked against SCONE docs. **NuclearData:** first block is verified full deck; JEF-style excerpts below it remain paste-only for production ACE.

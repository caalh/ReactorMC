# Staging bundle for [caalh/ReactorMC](https://github.com/caalh/ReactorMC)

This directory is a **copy** of `scone-examples/` from the ReactorMC website repository. It is **not** the canonical copy inside the site repo (`../scone-examples/` at repo root)—that remains unchanged.

## What to upload

Drag the **`scone-examples`** folder inside this bundle into the root of your `ReactorMC` GitHub repository so the layout matches the website:

```text
ReactorMC/   (your repo root)
  scone-examples/
    verify/
      run_all.ps1
      README.md
      VERIFICATION_SUMMARY.md
      tutorial_* / test_simple_*   (input decks, no extension)
    scone_beavrs_clean.inp
    README_BEAVRS_PARITY.md
```

## After upload

1. In `ReactorMC`, add or adjust a top-level `README.md` that points to `scone-examples/verify/README.md` for how to run SCONE against `IntegrationTestFiles/testLib`.
2. Delete this entire **`ReactorMC-upload-bundle`** folder from the website repo (it may be gitignored here so it is not committed).

## What “verified” means

- **`verify/`** — Decks run with SCONE and `SCONE_ACE=IntegrationTestFiles/testLib`; `run_all.ps1` lists the harness set (see `verify/README.md`).
- **`scone_beavrs_clean.inp`** — Full-scale-style deck; needs a full ACE library, not testLib.
- **`README_BEAVRS_PARITY.md`** — Structural parity notes vs in-site BEAVRS material.

OpenMC examples are not included yet; add a sibling tree (e.g. `openmc-examples/verify/`) in `ReactorMC` when you have runnable files and a runner script.

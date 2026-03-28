# Staging bundle for [caalh/ReactorMC](https://github.com/caalh/ReactorMC)

## Not used by the website

The ReactorMC **site** reads SCONE verify files only from repo-root **`scone-examples/`** (`?raw` imports in `src/pages/scone/*`). **`openmc-examples/`** at repo root is the canonical runnable mirror for OpenMC tutorials.

Everything under **`ReactorMC-upload-bundle/scone-examples/`** and **`ReactorMC-upload-bundle/openmc-examples/`** is a **disposable copy** for uploading to the org repo. Edit and maintain **only** the repo-root folders.

## Refresh copies

From the website repo root:

```bash
npm run sync:upload-bundle
```

That runs `scripts/sync-reactormc-upload-bundle.mjs` and overwrites the two subfolders here.

## Upload layout

Drag these **from inside this bundle** into the root of your **`ReactorMC`** repository:

```text
ReactorMC/
  scone-examples/     ← copy from ReactorMC-upload-bundle/scone-examples/
  openmc-examples/    ← copy from ReactorMC-upload-bundle/openmc-examples/
```

## After upload

1. Point the org repo **`README.md`** at `scone-examples/verify/README.md` and `openmc-examples/README.md`.
2. Optionally delete the copied subfolders here and re-run `npm run sync:upload-bundle` only when you need a fresh staging tree.

## What “verified” means

- **`scone-examples/verify/`** — SCONE + `IntegrationTestFiles/testLib`; `run_all.ps1`.
- **`scone_beavrs_clean.inp`** — full-library deck, not testLib.
- **`openmc-examples/`** — pin + assembly Python; needs `OPENMC_CROSS_SECTIONS`; not CI.

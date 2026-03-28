# Upload staging for [caalh/ReactorMC](https://github.com/caalh/ReactorMC)

## Do this (in order)

1. **From the website repo root**, run:
   ```bash
   npm run sync:upload-bundle
   ```
   That refreshes the two folders next to this file: `scone-examples/` and `openmc-examples/`.

2. **Drag both folders** into the **root** of your `ReactorMC` GitHub repo (same level as that repo’s `README.md`).

3. **On the org repo**, update the top-level `README.md` so it links to `scone-examples/verify/README.md` and `openmc-examples/README.md`.

You can delete `scone-examples/` and `openmc-examples/` inside this bundle after upload; run step 1 again whenever you need a fresh copy.

---

## Why this folder exists

The **live site** only reads SCONE inputs from **`scone-examples/` at the repo root** (not from here). This bundle is **just a copy** you sync before uploading to the separate `ReactorMC` repo—edit decks only under repo-root `scone-examples/` and `openmc-examples/`.

## What “verified” means (short)

| Folder | Meaning |
|--------|--------|
| `scone-examples/verify/` | Run with SCONE + `IntegrationTestFiles/testLib`; see `run_all.ps1`. |
| `scone_beavrs_clean.inp` | Full-library deck, not testLib. |
| `openmc-examples/` | Pin + assembly Python; needs `OPENMC_CROSS_SECTIONS`; not run in CI. |

# MCNP examples

Canonical MCNP input decks mirrored on the ReactorMC site and (optionally) the
public examples repo. The SPA reads these via `?raw` imports — keep them in sync
with what the site renders.

## Decks

- `beavrs_fullcore.i` — **BEAVRS Cycle 1 full-core PWR translation (community
  example deck).** Geometry + material number densities translated from the
  author-verified Cambridge SCONE BEAVRS deck (`reactor-test-decks/
  beavrs_scone_fullcore.scone`) and the MIT BEAVRS rev 2.0.2 spec. Real 193-
  assembly loading map (1.6/2.4/3.1 wt% UO2), 17×17 assemblies with 24 guide
  tubes + central instrument tube, Pyrex burnable-poison rods, control rods
  withdrawn, core barrel/RPV shells. **NOT benchmark-validated.** Flagged
  simplifications: ZAID `.80c` (ENDF/B-VII.1) assumed though number densities
  are the verified deck's JEF-3.1.1 600 K values (cross-library k-eff bias
  expected); single uniform active-fuel axial zone (no grids/plenum/nozzles);
  representative 20-rod Pyrex pattern; neutron-shield/baffle plates omitted.
  `lwtr.20t` S(α,β) on water only. Not an official MIT/CRPG product.
- `beavrs_core_mcnp.i` — older BEAVRS-style full-core **example fixture for 3D
  geometry preview / visualization only — NOT benchmark-converged.** ZAID `.80c`
  assumed. Superseded for fidelity by `beavrs_fullcore.i`.

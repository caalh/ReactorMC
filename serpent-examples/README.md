# Serpent examples

Canonical Serpent 2 input decks mirrored on the ReactorMC site and (optionally)
the public examples repo. The SPA reads these via `?raw` imports — keep them in
sync with what the site renders.

## Decks

- `beavrs_fullcore.sss` — **BEAVRS Cycle 1 full-core PWR translation (community
  example deck).** Geometry + material number densities translated from the
  author-verified Cambridge SCONE BEAVRS deck and the MIT BEAVRS rev 2.0.2 spec.
  Real 193-assembly loading map (1.6/2.4/3.1 wt% UO2), `pin`/`lat` universes
  with 24 guide tubes + central instrument tube, Pyrex burnable-poison rods,
  control rods withdrawn, core barrel/RPV. Energies in MeV; run `sss2 -omp N
  beavrs_fullcore.sss`. **NOT benchmark-validated.** Flagged simplifications:
  ZAID `.06c` assumed = 600 K (set `set acelib` to match); single uniform
  active-fuel axial zone; representative 20-rod Pyrex pattern; neutron-shield/
  baffle plates omitted. `therm lwtr` S(α,β) on water only. Not an official
  MIT/CRPG product.
- `beavrs_core_serpent.sss` — older BEAVRS-style full-core **example fixture for
  3D geometry preview / visualization only — NOT benchmark-converged.**
  Superseded for fidelity by `beavrs_fullcore.sss`.

# ReactorMC example decks

Public mirror of the Monte Carlo example input decks taught on
[reactormc.net](https://reactormc.net). One folder per code:

- `mcnp-examples/` — MCNP input decks
- `openmc-examples/` — OpenMC Python models
- `serpent-examples/` — Serpent 2 input decks
- `scone-examples/` — SCONE input files and verification cases

Each folder has its own README describing the decks and their caveats. These are
educational examples, not benchmark-validated models — read the per-deck notes
before using any of them for real work.

## Provenance

Decks here are mirrored from the reactormc.net site repository
(`reactor-monte-carlo-guide`), which is the canonical source. Do not edit deck
physics in this repo; fixes land upstream and are re-synced here.

The four BEAVRS full-core decks (`beavrs_fullcore.i`, `beavrs_fullcore.sss`,
`beavrs_fullcore.scone`, `beavrs_fullcore.py`) were cross-verified in September
2026: all four codes describe the same geometry, agreeing at 100.000% of 60,000
sampled points via OWEN Compare Geometry.

## License

See [LICENSE](LICENSE).

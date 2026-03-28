# BEAVRS SCONE inputs — verified vs clean

| File | Role |
|------|------|
| **`Scone Input`** (repo root) | Author-verified full-core deck as used for successful runs (local `aceLibrary` path, informal comments). |
| **`scone_beavrs_clean.inp`** | Same model: identical lattice maps, surface IDs, cell/universe IDs, and material **active** compositions. Differences are **only** presentation and portability: section headers, consistent spacing, renamed descriptive labels where SCONE keys off **numeric IDs**, portable `aceLibrary` placeholder, and the second `viz` entry uses the same keyword as the verified file (`bmp` for the y-axis image). |

**Restored from verified (was missing in an older clean export):** `clad` and `alClad` material blocks at the end of `nuclearData` (present in `Scone Input`; not used by current pin `fills` but kept for parity).

After pulling the repo, set `aceLibrary` in `scone_beavrs_clean.inp` to your `JEF311.aceXS` (or equivalent).

## Automated parity check (functional equivalence)

The two files are **not** byte-identical (line count, comments, ordering within `surfaces` / `cells` / `universes` / `materials`, and `aceLibrary` path differ). To confirm they still describe the **same physics model**, run:

```bash
npm run verify:beavrs-parity
```

This runs `scripts/compare-beavrs-parity.js`, which:

- Strips `//` comments (without breaking `://` in paths).
- Replaces any `aceLibrary …` path with a placeholder.
- Collapses whitespace and normalizes delimiters.
- Parses **geometry** and **nuclearData**: sorts child blocks by numeric `id` (or material name), ignores leading surface/cell/universe **labels** (so renames like `grid1` vs `gridThick24` do not false-fail).
- Normalizes numeric trivia (e.g. `.56134` vs `0.56134`, `E-002` vs `E-02`) so only real content changes fail the check.

Exit code **0** means **structurally equivalent** under those rules; **1** prints the first mismatching section.

Canonical fingerprint (after normalization): run the script and read the printed **Canonical SHA-256** (updates if either file’s meaningful content changes).

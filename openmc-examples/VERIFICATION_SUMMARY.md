# OpenMC examples — verification summary

**Status:** Manual execution against OpenMC **0.15.3** + ENDF/B-VII.1 HDF5 (see `docs/AI_CHANGELOG.md` → 2026-03-05). **Not** run in GitHub Actions (no nuclear data in CI).

| Example | Script | Site page |
|---------|--------|-----------|
| Pin cell | `example_pin/build_model.py` | `/openmc/example-pin/` |
| 17×17 assembly | `example_assembly/build_model.py` | `/openmc/example-assembly/` |

**Pass criteria:** `python build_model.py` completes; `openmc` exits 0; statepoint loads; printed k-effective and tally summaries run without exception.

**Process (maintainers):** Set `OPENMC_CROSS_SECTIONS`, then `./run_all.sh` or `.\run_all.ps1` from `openmc-examples/`.

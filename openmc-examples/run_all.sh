#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"

if [[ -z "${OPENMC_CROSS_SECTIONS:-}" ]]; then
  echo "ERROR: Set OPENMC_CROSS_SECTIONS to your cross_sections.xml (see openmc-examples/README.md)." >&2
  exit 1
fi

( cd "$ROOT/example_pin" && python3 build_model.py )
( cd "$ROOT/example_assembly" && python3 build_model.py )

echo "openmc-examples: all scripts finished."

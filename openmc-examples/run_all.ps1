# Run OpenMC examples (requires OPENMC_CROSS_SECTIONS and `python` on PATH).
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not $env:OPENMC_CROSS_SECTIONS) {
    Write-Error "Set OPENMC_CROSS_SECTIONS to your cross_sections.xml (see openmc-examples/README.md)."
}

Push-Location (Join-Path $root "example_pin")
try {
    python build_model.py
} finally {
    Pop-Location
}

Push-Location (Join-Path $root "example_assembly")
try {
    python build_model.py
} finally {
    Pop-Location
}

Write-Host "openmc-examples: all scripts finished."

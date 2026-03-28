# Run all SCONE verification tests
# Expects: SCONE at C:\Users\calho\Documents\GitHub\SCONE, scone-examples in this repo
$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $PSScriptRoot   # scone-examples
$repoRoot = Split-Path -Parent $scriptDir       # reactor-monte-carlo-guide
$gitHubRoot = Split-Path -Parent $repoRoot      # GitHub
$drive = $gitHubRoot[0].ToString().ToLower()
$rest = $gitHubRoot.Substring(3).Replace("\", "/")
$wslRoot = "/mnt/$drive/$rest"
$sconeDir = "$wslRoot/SCONE"
$examplesRel = "reactor-monte-carlo-guide/scone-examples/verify"
$ace = "IntegrationTestFiles/testLib"

$tests = @(
    @{ name = "test_simple_fuel_pin"; path = "test_simple_fuel_pin"; expect = "eigen" },
    @{ name = "test_simple_bare_sphere"; path = "test_simple_bare_sphere"; expect = "eigen" },
    @{ name = "tutorial_fuel_pin"; path = "tutorial_fuel_pin_testlib"; expect = "eigen" },
    @{ name = "tutorial_bare_sphere"; path = "tutorial_bare_sphere_testlib"; expect = "eigen" },
    @{ name = "tutorial_bare_sphere_clean"; path = "tutorial_bare_sphere_clean"; expect = "eigen" },
    @{ name = "tutorial_scone_tsx"; path = "tutorial_scone_tsx_testlib"; expect = "eigen" },
    @{ name = "tutorial_config"; path = "tutorial_config_testlib"; expect = "eigen" },
    @{ name = "tutorial_troubleshooting_smoke"; path = "tutorial_troubleshooting_smoke"; expect = "eigen" },
    @{ name = "tutorial_troubleshooting_boundary"; path = "tutorial_troubleshooting_boundary"; expect = "eigen" },
    @{ name = "tutorial_shielding_slab"; path = "tutorial_shielding_slab"; expect = "fixed" },
    @{ name = "tutorial_assembly_5x5"; path = "tutorial_assembly_5x5_testlib"; expect = "eigen" },
    @{ name = "tutorial_basics_celluniverse"; path = "tutorial_basics_celluniverse_testlib"; expect = "eigen" },
    @{ name = "tutorial_examples_hub"; path = "tutorial_examples_hub_testlib"; expect = "eigen" },
    @{ name = "tutorial_parallel_eigen_sample"; path = "tutorial_parallel_eigen_sample_testlib"; expect = "eigen" },
    @{ name = "tutorial_nuclear_data_basic"; path = "tutorial_nuclear_data_basic_testlib"; expect = "eigen" }
)

$passed = 0
$failed = 0
$results = @()

foreach ($t in $tests) {
    $inputPath = "../$examplesRel/$($t.path)"
    Write-Host "`n=== $($t.name) ===" -ForegroundColor Cyan
    $out = wsl -e bash -c "cd $sconeDir && export SCONE_ACE=$ace && timeout 90 ./build/scone.out $inputPath 2>&1"
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        Write-Host "PASS" -ForegroundColor Green
        $passed++
        $results += [PSCustomObject]@{ Test = $t.name; Result = "PASS" }
    } elseif ($exitCode -eq 124) {
        Write-Host "TIMEOUT" -ForegroundColor Yellow
        $results += [PSCustomObject]@{ Test = $t.name; Result = "TIMEOUT" }
    } else {
        Write-Host "FAIL (exit $exitCode)" -ForegroundColor Red
        $failed++
        $results += [PSCustomObject]@{ Test = $t.name; Result = "FAIL" }
        if ($out -match "Fatal|Error|SIGFPE|modulo") { Write-Host $out -ForegroundColor DarkGray }
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Passed: $passed | Failed: $failed"
$results | Format-Table -AutoSize

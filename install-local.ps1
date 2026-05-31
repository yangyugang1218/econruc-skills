$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillsRoot = Join-Path $Root "skills"
$DestRoot = Join-Path $env:USERPROFILE ".codex\skills"

New-Item -ItemType Directory -Force -Path $DestRoot | Out-Null

Get-ChildItem -LiteralPath $SkillsRoot -Directory | ForEach-Object {
    $dest = Join-Path $DestRoot $_.Name
    if (Test-Path -LiteralPath $dest) {
        Write-Host "Skipping existing skill: $($_.Name)"
    }
    else {
        Copy-Item -LiteralPath $_.FullName -Destination $dest -Recurse
        Write-Host "Installed skill: $($_.Name)"
    }
}

Write-Host "Restart Codex to pick up new skills."

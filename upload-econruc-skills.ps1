param(
    [switch]$FirstUpload
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$CodexSkills = Join-Path $env:USERPROFILE ".codex\skills"
$RepoSkills = Join-Path $RepoRoot "skills"
$RemoteUrl = "https://github.com/yangyugang1218/econruc-skills.git"

function Write-Step($Message) {
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Require-Command($Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Missing command: $Name"
    }
}

Require-Command git

Write-Step "Checking repository"
Set-Location $RepoRoot
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    git init
    git branch -M main
}

$origin = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    git remote add origin $RemoteUrl
} elseif ($origin -ne $RemoteUrl) {
    git remote set-url origin $RemoteUrl
}

Write-Step "Syncing latest econruc skills from Codex"
if (-not (Test-Path $RepoSkills)) {
    New-Item -ItemType Directory -Path $RepoSkills | Out-Null
}

Get-ChildItem -LiteralPath $CodexSkills -Directory |
    Where-Object { $_.Name -like "econruc-*" } |
    Sort-Object Name |
    ForEach-Object {
        $dest = Join-Path $RepoSkills $_.Name
        if (-not (Test-Path -LiteralPath $dest)) {
            New-Item -ItemType Directory -Path $dest | Out-Null
        }
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $dest -Recurse -Force
        Write-Host "Synced $($_.Name)"
    }

Write-Step "Staging changes"
git add README.md .gitignore skills

$status = git status --porcelain
if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Update EconRUC skills ($timestamp)"
} else {
    Write-Host "No local changes to commit."
}

Write-Step "Pushing to GitHub"
git branch -M main

if ($FirstUpload) {
    Write-Host "First upload mode: using --force-with-lease to replace GitHub's initial README commit." -ForegroundColor Yellow
    git push --force-with-lease -u origin main
} else {
    git push -u origin main
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "Normal push failed. If the remote only contains GitHub's initial README, rerun with:" -ForegroundColor Yellow
        Write-Host "  .\upload-econruc-skills.ps1 -FirstUpload" -ForegroundColor Yellow
        exit $LASTEXITCODE
    }
}

Write-Step "Done"
Write-Host "Uploaded to: https://github.com/yangyugang1218/econruc-skills" -ForegroundColor Green

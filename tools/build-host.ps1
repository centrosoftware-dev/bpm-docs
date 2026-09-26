param(
    [string]$Configuration = "Release"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "==> mkdocs build (site -> host/wwwroot)"
mkdocs build --strict --site-dir host/wwwroot
if ($LASTEXITCODE -ne 0) { throw "mkdocs build failed" }

Write-Host "==> dotnet publish host"
dotnet publish host -c $Configuration -o publish
if ($LASTEXITCODE -ne 0) { throw "dotnet publish failed" }

Write-Host "==> fatto: output in .\publish"

$ErrorActionPreference = 'Stop'
$sourceRoot = 'C:\Users\Allen\.codex\skills'
$targetRoot = 'C:\Users\Allen\.copilot\skills'
$backupRoot = 'C:\Users\Allen\.copilot\skill-sync-backups'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$backupPath = Join-Path $backupRoot "skills-before-$stamp.zip"
$reportPath = Join-Path $backupRoot "sync-$stamp.json"
$skills = @(Get-ChildItem -LiteralPath $sourceRoot -Directory | Where-Object {
    !$_.Name.StartsWith('.') -and (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md'))
})
if (!(Test-Path -LiteralPath $targetRoot -PathType Container)) { throw 'Target skills directory is missing.' }
foreach ($root in @($sourceRoot, $targetRoot)) {
    $links = @(Get-ChildItem -LiteralPath $root -Recurse -Force | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint })
    if ($links.Count -gt 0) { throw "Review reparse points before syncing: $root" }
}
$plan = @()
foreach ($skill in $skills) {
    foreach ($file in Get-ChildItem -LiteralPath $skill.FullName -File -Recurse) {
        $relative = $file.FullName.Substring($sourceRoot.Length + 1)
        $destination = [IO.Path]::GetFullPath((Join-Path $targetRoot $relative))
        if (!$destination.StartsWith($targetRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Destination outside target root.' }
        $sourceHash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
        $exists = Test-Path -LiteralPath $destination
        $targetHash = if ($exists) { (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash } else { $null }
        $plan += [PSCustomObject]@{ Relative = $relative; Source = $file.FullName; Destination = $destination; Hash = $sourceHash; Action = $(if (!$exists) { 'Add' } elseif ($sourceHash -ne $targetHash) { 'Update' } else { 'Unchanged' }) }
    }
}
New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
Add-Type -AssemblyName System.IO.Compression.FileSystem
[IO.Compression.ZipFile]::CreateFromDirectory($targetRoot, $backupPath, [IO.Compression.CompressionLevel]::Optimal, $true)
$archive = [IO.Compression.ZipFile]::OpenRead($backupPath)
try {
    $existing = @(Get-ChildItem -LiteralPath $targetRoot -File -Recurse)
    if ($archive.Entries.Count -ne $existing.Count) { throw 'Backup entry count mismatch.' }
    foreach ($file in $existing) {
        $relative = $file.FullName.Substring($targetRoot.Length + 1).Replace('\', '/')
        $entry = $archive.GetEntry('skills/' + $relative)
        if (!$entry) { throw "Missing backup entry: $relative" }
        $stream = $entry.Open()
        $sha = [Security.Cryptography.SHA256]::Create()
        try { $hash = [Convert]::ToHexString($sha.ComputeHash($stream)) } finally { $stream.Dispose(); $sha.Dispose() }
        if ($hash -ne (Get-FileHash -LiteralPath $file.FullName).Hash) { throw "Backup content mismatch: $relative" }
    }
} finally { $archive.Dispose() }
foreach ($item in $plan | Where-Object { $_.Action -ne 'Unchanged' }) {
    New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($item.Destination)) -Force | Out-Null
    Copy-Item -LiteralPath $item.Source -Destination $item.Destination -Force
}
foreach ($item in $plan) {
    if ((Get-FileHash -LiteralPath $item.Destination -Algorithm SHA256).Hash -ne $item.Hash) { throw "Verification failed: $($item.Relative)" }
}
$report = [PSCustomObject]@{
    Source = $sourceRoot; Target = $targetRoot; Backup = $backupPath
    Skills = $skills.Count; FilesVerified = $plan.Count
    AddedFiles = @($plan | Where-Object { $_.Action -eq 'Add' }).Count
    UpdatedFiles = @($plan | Where-Object { $_.Action -eq 'Update' }).Count
    DeletedFiles = 0; Changes = @($plan | Where-Object { $_.Action -ne 'Unchanged' } | Select-Object Relative, Action)
}
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $reportPath -Encoding utf8
$report | Select-Object Source, Target, Backup, Skills, FilesVerified, AddedFiles, UpdatedFiles, DeletedFiles | ConvertTo-Json
Write-Output "Report: $reportPath"

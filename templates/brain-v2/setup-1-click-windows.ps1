$ErrorActionPreference = "Stop"

$McpName = if ($env:MCP_NAME) { $env:MCP_NAME } else { "company-brain" }
$McpEndpoint = if ($env:MCP_ENDPOINT) { $env:MCP_ENDPOINT } else { "https://your-mcp.example/sse" }
$McpRemoteVersion = if ($env:MCP_REMOTE_VERSION) { $env:MCP_REMOTE_VERSION } else { "0.1.18" }
$ConfigDir = Join-Path $env:APPDATA "Claude"
$ConfigFile = Join-Path $ConfigDir "claude_desktop_config.json"

function Test-Command {
  param([string]$Name)
  return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Install-NodeLts {
  if ((Test-Command "node") -and (Test-Command "npx")) {
    return
  }

  if (Test-Command "winget") {
    winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements
  } else {
    $index = Invoke-RestMethod "https://nodejs.org/dist/index.json"
    $release = $index | Where-Object { $_.lts } | Select-Object -First 1
    if (-not $release) { throw "Could not resolve latest Node.js LTS release." }

    $arch = if ([Environment]::Is64BitOperatingSystem) { "x64" } else { "x86" }
    $version = $release.version
    $msi = "node-$version-$arch.msi"
    $url = "https://nodejs.org/dist/$version/$msi"
    $tmp = Join-Path $env:TEMP $msi

    Invoke-WebRequest -Uri $url -OutFile $tmp
    Start-Process msiexec.exe -ArgumentList "/i `"$tmp`" /qn" -Wait
  }

  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  if (-not (Test-Command "npx")) {
    throw "npx not found after Node.js install. Restart PowerShell and run again."
  }
}

function Close-Claude {
  Get-Process "Claude" -ErrorAction SilentlyContinue | Stop-Process -Force
}

function Merge-ClaudeConfig {
  New-Item -ItemType Directory -Force -Path $ConfigDir | Out-Null
  if (-not (Test-Path $ConfigFile)) {
    Set-Content -Path $ConfigFile -Value "{`n  `"mcpServers`": {}`n}`n"
  }

  try {
    $json = Get-Content $ConfigFile -Raw | ConvertFrom-Json
  } catch {
    Copy-Item $ConfigFile "$ConfigFile.bak" -Force
    $json = [pscustomobject]@{}
  }

  if (-not $json.PSObject.Properties["mcpServers"]) {
    $json | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value ([pscustomobject]@{})
  }

  $npxPath = (Get-Command "npx").Source
  $server = [ordered]@{
    command = $npxPath
    args = @("-y", "mcp-remote@$McpRemoteVersion", $McpEndpoint, "--transport", "sse-only")
  }

  $existing = $json.mcpServers.PSObject.Properties[$McpName]
  if ($existing) {
    $existing.Value = $server
  } else {
    $json.mcpServers | Add-Member -MemberType NoteProperty -Name $McpName -Value $server
  }

  $json | ConvertTo-Json -Depth 20 | Set-Content -Path $ConfigFile
}

function Verify-ClaudeConfig {
  $json = Get-Content $ConfigFile -Raw | ConvertFrom-Json
  $server = $json.mcpServers.PSObject.Properties[$McpName].Value
  if (-not $server -or (($server.args -join " ") -notmatch "mcp-remote")) {
    throw "MCP config verification failed."
  }
}

Install-NodeLts
Close-Claude
Merge-ClaudeConfig
Verify-ClaudeConfig

Write-Host "LISTO"

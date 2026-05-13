#!/usr/bin/env bash
set -euo pipefail

MCP_NAME="${MCP_NAME:-company-brain}"
MCP_ENDPOINT="${MCP_ENDPOINT:-https://your-mcp.example/sse}"
MCP_REMOTE_VERSION="${MCP_REMOTE_VERSION:-0.1.18}"
CONFIG_DIR="$HOME/Library/Application Support/Claude"
CONFIG_FILE="$CONFIG_DIR/claude_desktop_config.json"

need() {
  command -v "$1" >/dev/null 2>&1
}

install_node_lts() {
  if need node && need npx; then
    return
  fi

  if ! need curl; then
    echo "curl is required to install Node.js LTS." >&2
    exit 1
  fi
  if ! need python3; then
    echo "python3 is required to resolve the latest Node.js LTS installer." >&2
    exit 1
  fi

  arch="$(uname -m)"
  case "$arch" in
    arm64) node_arch="arm64" ;;
    x86_64) node_arch="x64" ;;
    *) echo "Unsupported Mac architecture: $arch" >&2; exit 1 ;;
  esac

  version="$(python3 - <<'PY'
import json, urllib.request
with urllib.request.urlopen("https://nodejs.org/dist/index.json", timeout=20) as r:
    releases = json.load(r)
for item in releases:
    if item.get("lts"):
        print(item["version"])
        break
PY
)"

  pkg="node-${version}.pkg"
  url="https://nodejs.org/dist/${version}/${pkg}"
  tmp="/tmp/${pkg}"

  echo "Installing Node.js LTS ${version}..."
  curl -fsSL "$url" -o "$tmp"
  sudo installer -pkg "$tmp" -target /
}

close_claude() {
  if pgrep -x "Claude" >/dev/null 2>&1; then
    osascript -e 'tell application "Claude" to quit' >/dev/null 2>&1 || true
    sleep 2
  fi
}

merge_config() {
  mkdir -p "$CONFIG_DIR"
  if [ ! -f "$CONFIG_FILE" ]; then
    printf '{\n  "mcpServers": {}\n}\n' > "$CONFIG_FILE"
  fi

  npx_path="$(command -v npx || true)"
  if [ -z "$npx_path" ]; then
    echo "npx not found after Node.js install." >&2
    exit 1
  fi

  python3 - "$CONFIG_FILE" "$MCP_NAME" "$npx_path" "$MCP_REMOTE_VERSION" "$MCP_ENDPOINT" <<'PY'
import json, pathlib, sys

path = pathlib.Path(sys.argv[1])
name, npx_path, version, endpoint = sys.argv[2:6]

try:
    data = json.loads(path.read_text() or "{}")
except json.JSONDecodeError:
    backup = path.with_suffix(path.suffix + ".bak")
    backup.write_text(path.read_text())
    data = {}

servers = data.setdefault("mcpServers", {})
servers[name] = {
    "command": npx_path,
    "args": ["-y", f"mcp-remote@{version}", endpoint, "--transport", "sse-only"],
}

path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
PY
}

verify_config() {
  python3 - "$CONFIG_FILE" "$MCP_NAME" <<'PY'
import json, sys
data = json.load(open(sys.argv[1]))
server = data.get("mcpServers", {}).get(sys.argv[2])
if not server or "mcp-remote" not in " ".join(server.get("args", [])):
    raise SystemExit("MCP config verification failed")
PY
}

install_node_lts
close_claude
merge_config
verify_config

echo "LISTO"

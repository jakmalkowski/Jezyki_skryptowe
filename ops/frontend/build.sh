#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
FRONTEND_DIR=$(cd "$SCRIPT_DIR/../../frontend" && pwd)
PROJECT_ROOT_DIR=$(cd "$SCRIPT_DIR/../../" && pwd)

cd "$PROJECT_ROOT_DIR"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is not installed"
  exit 1
fi

node --version || true
npm --version || true

cd "$FRONTEND_DIR"

# Prefer reproducible installs in CI
if [ -f package-lock.json ]; then
  npm ci >/dev/null 2>&1
else
  npm install >/dev/null 2>&1
fi

npm run build

if [ ! -d dist ]; then
  echo "Frontend build failed: dist/ not found"
  exit 1
fi

echo "Frontend built successfully"
exit 0
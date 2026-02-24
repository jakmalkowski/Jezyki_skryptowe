#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
BACKEND_DIR=$(cd "$SCRIPT_DIR/../../backend" && pwd)
PROJECT_ROOT_DIR=$(cd "$SCRIPT_DIR/../../" && pwd)

cd "$PROJECT_ROOT_DIR"

if ! command -v python >/dev/null 2>&1; then
  echo "python is not installed"
  exit 1
fi

if ! command -v pip >/dev/null 2>&1; then
  echo "pip is not installed"
  exit 1
fi

python --version || true

pip install --upgrade pip >/dev/null 2>&1
pip install -r "$BACKEND_DIR/requirements.txt" >/dev/null 2>&1

cd "$BACKEND_DIR"
pytest

echo "Backend tests passed"
exit 0
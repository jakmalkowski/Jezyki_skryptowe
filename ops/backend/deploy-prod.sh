#!/bin/bash
set -euo pipefail

if [[ -z "${RENDER_BACKEND_PROD_HOOK:-}" ]]; then
  echo "RENDER_BACKEND_PROD_HOOK is not set" >&2
  exit 1
fi

curl -fsS -X POST "$RENDER_BACKEND_PROD_HOOK"
echo "Triggered backend PROD deploy on Render"
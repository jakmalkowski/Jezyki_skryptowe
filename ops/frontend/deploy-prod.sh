#!/bin/bash
set -euo pipefail

if [[ -z "${RENDER_FRONTEND_PROD_HOOK:-}" ]]; then
  echo "RENDER_FRONTEND_PROD_HOOK is not set" >&2
  exit 1
fi

curl -fsS -X POST "$RENDER_FRONTEND_PROD_HOOK"
echo "Triggered frontend PROD deploy on Render"
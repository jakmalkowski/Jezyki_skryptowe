#!/bin/bash
set -euo pipefail

if [[ -z "${RENDER_FRONTEND_DEV_HOOK:-}" ]]; then
  echo "RENDER_FRONTEND_DEV_HOOK is not set" >&2
  exit 1
fi

curl -fsS -X POST "$RENDER_FRONTEND_DEV_HOOK"
echo "Triggered frontend DEV deploy on Render"
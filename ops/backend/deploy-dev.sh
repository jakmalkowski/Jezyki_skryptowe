#!/bin/bash
set -euo pipefail

if [[ -z "${RENDER_BACKEND_DEV_HOOK:-}" ]]; then
  echo "RENDER_BACKEND_DEV_HOOK is not set" >&2
  exit 1
fi

curl -fsS -X POST "$RENDER_BACKEND_DEV_HOOK"
echo "Triggered backend DEV deploy on Render"
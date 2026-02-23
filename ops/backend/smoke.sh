#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
BACKEND_DIR=$(cd "$SCRIPT_DIR/../../backend" && pwd)
PROJECT_ROOT_DIR=$(cd "$SCRIPT_DIR/../../" && pwd)

cd $PROJECT_ROOT_DIR

pip install -r $BACKEND_DIR/requirements.txt >/dev/null 2>&1

export PYTHONPATH="$PROJECT_ROOT_DIR"
PORT=${PORT:-5001}
HOST=${HOST:-127.0.0.1}

(gunicorn -w 1 -b "$HOST:$PORT" --chdir "$BACKEND_DIR" app:app > /tmp/backend_smoke.log 2>&1) &
PID=$!

cleanup() {
    kill "$PID" >/dev/null || true
}

trap cleanup EXIT

ATTEMPTS=10

until curl -fsS http://$HOST:$PORT/health >/dev/null || [ $ATTEMPTS -eq 0 ]; do
    ATTEMPTS=$((ATTEMPTS - 1))
    sleep 1
    echo "Waiting for backend to respond -> $ATTEMPTS attempts left"
    if ! kill -0 "$PID" >/dev/null 2>&1; then
        echo "Backend process died"
        tail -n +1 /tmp/backend_smoke.log || true
        exit 1
    fi
done

curl -fsS http://$HOST:$PORT/health | tee /tmp/health.json

curl -fsS http://$HOST:$PORT/api/url/shorten -X POST -H "Content-Type: application/json" -d '{"url": "https://www.facebook.com"}' | tee /tmp/shorten.json

jq -e '.status == "ok"' </tmp/health.json >/dev/null || { echo "Health check failed"; exit 1; }

jq -e '.short_url' </tmp/shorten.json >/dev/null || { echo "Shorten failed"; exit 1; }

echo "Backend smoke test passed"
exit 0
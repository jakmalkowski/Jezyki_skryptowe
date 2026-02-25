# URL Shortener (Flask + Vue)

Simple URL shortener app with:
- Backend: Python + Flask
- Frontend: Vue 3 + Vite
- CI/CD: GitHub Actions + bash scripts
- Deploy: Render (separate backend + frontend services)

## Project Structure

```text
backend/                  Flask API
frontend/                 Vue app
ops/backend/              backend scripts (build/test/smoke/deploy)
ops/frontend/             frontend scripts (build/deploy)
.github/workflows/        CI/CD pipelines
render.yaml               Render blueprint config
```

## Requirements

- Python 3.13
- Node.js 20+
- npm

## Local Run

### 1) Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Backend URL: `http://127.0.0.1:5000`

### 2) Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL: `http://localhost:5173`

## Backend API

Base path: `/api/url`

- `POST /api/url/shorten` - create short URL
- `GET /api/url/<short_code>` - redirect to original URL
- `GET /api/url/` - list all mappings (key + value)
- `DELETE /api/url/<short_code>` - delete mapping
- `GET /health` - healthcheck

### Example curl

```bash
curl -X POST http://127.0.0.1:5000/api/url/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://google.com"}'
```

### Backend

```bash
bash ops/backend/build.sh
bash ops/backend/test.sh
bash ops/backend/smoke.sh
```

### Frontend

```bash
bash ops/frontend/build.sh
```

## CI/CD

### Backend
- `.github/workflows/backend-ci.yml`
  - build -> test -> smoke -> dev deploy (on `main` push)
- `.github/workflows/backend-deploy.yml`
  - manual dev/prod deploy

### Frontend
- `.github/workflows/frontend-ci.yml`
  - build -> dev deploy (on `main` push)
- `.github/workflows/frontend-deploy.yml`
  - manual dev/prod deploy

## Data storage limitation

Current storage is in-memory hashmap.
Data is not persistent and may reset after restart/redeploy of the render instances.
# URL Shortener Backend

Flask backend API for URL shortener application.

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment variables from `ENV_SETUP.md` and create a `.env` file:

```bash
# Create .env file with required variables
# See ENV_SETUP.md for details
```

**Note:** This application uses in-memory hashmap storage. Data will be lost when the server restarts.

### 4. Run Development Server

```bash
flask run
# Or
python app.py
```

## Testing

Run tests with:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov
```

## Production Deployment

For production, use gunicorn:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Make sure to set all required environment variables in your deployment platform.


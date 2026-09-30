# Simple Web App

Minimal FastAPI app with a single endpoint.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

## Run

From the repository root:

```bash
uvicorn main:app --reload
```

By default the server runs at `http://127.0.0.1:8000`.

## API usage

### `GET /`

Response:

```json
{
  "message": "Hello! Meri pehli Python web app successfully chal rahi hai 🚀"
}
```

Example request:

```bash
curl http://127.0.0.1:8000/
```

FastAPI also provides auto-generated docs at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Testing

There is currently no test suite or test configuration in this repository.

Quick manual check:

```bash
python -c "from main import home; print(home())"
```

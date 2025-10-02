# Modular Django Web App (with Tests & E2E)

## Quickstart (Local)

```bash
# 1) Create and activate a virtualenv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt
python -m playwright install  # for E2E (one-time)

# 3) Initialize DB and create a superuser
python manage.py migrate
python manage.py createsuperuser

# 4) Run local server
python manage.py runserver
# visit http://127.0.0.1:8000
```

## Tests

```bash
# Unit & integration
pytest

# Performance (uses pytest-benchmark)
pytest tests/test_perf.py

# E2E (headless browsers via Playwright)
pytest -m e2e
```

## Load Testing (Locust)

```bash
# In one terminal (Django):
python manage.py runserver

# In another terminal (Locust):
locust -f locustfile.py --host http://127.0.0.1:8000
# Then open http://127.0.0.1:8089 to run load tests
```

## Project Layout

```
modsite/                # Project config (settings, urls, middleware)
core/                   # App with models, services, views
templates/              # Jinja-like Django templates
static/                 # CSS/JS (served via WhiteNoise in prod)
tests/                  # pytest unit/integration/perf + Playwright E2E
```

## Notes on Efficiency

- Django is I/O-bound for web workloads; efficiency is mostly about DB queries and caching.
- Included a lightweight request timing middleware which emits `X-Request-Duration-ms` for quick profiling.
- For heavier throughput, consider running `gunicorn` behind a reverse proxy and enabling GZip + caching headers.
- To scale further: async views, Redis caching, Postgres, and background workers (Dramatiq/Celery).

## Packaging for Production

- Use `gunicorn` + `whitenoise` for static files:
  ```bash
  gunicorn modsite.wsgi:application --bind 0.0.0.0:8000
  ```
- Containerize with a slim Python image and multi-stage build; run `collectstatic` before release.
```


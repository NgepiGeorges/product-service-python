# Product Service (Python / Flask)

Product catalog API for the Algonquin Pet Store (CST8915 Lab 3).
This is a rewrite of the original Rust product-service in Python, because Rust is not natively supported by Azure App Service.

## API

| Method | Path | Response |
|---|---|---|
| GET | `/products` | JSON array of products (`id`, `name`, `price`) |

## 12-Factor (Factors I–IV)

- **I. Codebase:** this service has its own repository.
- **II. Dependencies:** all dependencies are declared and pinned in `requirements.txt`.
- **III. Config:** the port is read from the `PORT` environment variable (`.env` locally, App Settings on Azure). `.env` is ignored by Git; see `.env.example`.
- **IV. Backing services:** none (the catalog is static in this lab).

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env      # Linux/macOS: cp .env.example .env
python app.py
```

Then open http://localhost:3030/products

## Azure App Service

App Service (Python on Linux) detects `app.py` and starts it with gunicorn (`app:app`).

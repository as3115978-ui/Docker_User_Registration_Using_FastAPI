# Complete Project Implementation Guide

## 1. Architecture Overview
- **FastAPI** handles HTTP routing, Pydantic validation, and OpenAPI Swagger documentation.
- **SQLAlchemy + Alembic** manage ORM models and database schema migrations.
- **PostgreSQL 16** stores persistent user records in production/Docker Compose, with SQLite fallback for local testing.
- **Docker & Docker Compose** package the API and database into isolated, reproducible containers.
- **GitHub Actions** runs automated `pytest` suites and verifies Docker builds on every push.

## 2. Database Migrations (Alembic)
Apply migrations inside the container or local environment:
```bash
alembic upgrade head
```

Rollback the latest migration:
```bash
alembic downgrade -1
```

## 3. API Endpoints
- `GET /` — Service health check
- `POST /register` — Register a new user (hashes password with bcrypt, rejects duplicate emails)
- `GET /users` — List all registered users (excludes password hashes)

## 4. Author
**Anshu Singh** — GitHub: https://github.com/as3115978-ui

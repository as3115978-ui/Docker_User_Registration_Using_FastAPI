# Docker User Registration Using FastAPI

[![Python & Docker CI](https://github.com/as3115978-ui/Docker_User_Registration_Using_FastAPI/actions/workflows/python-ci.yml/badge.svg)](https://github.com/as3115978-ui/Docker_User_Registration_Using_FastAPI/actions/workflows/python-ci.yml)

A containerized User Registration REST API built using **Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker Compose**.

## Project Structure

```text
Docker_User_Registration_Using_FastAPI/
├ ─.github/workflows/
│   └── python-ci.yml
├── alembic/
┈   ├── versions/
│   │    └── 0001_create_users.py
│   ├── env.py
┈   └── script.py.mako
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
┈   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── docs/
┈   └── IMPLEMENTATION_GUIDE.md
├── tests/
┈   └── test_main.py
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── .dockerignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message & health check |
| POST | `/register` | Register a new user (bcrypt password hashing) |
| GET | `/users` | Retrieve registered users |

## Run Locally with Docker Compose

```bash
git clone https://github.com/as3115978-ui/Docker_User_Registration_Using_FastAPI.git
cd Docker_User_Registration_Using_FastAPI
docker compose up --build -d
```

Open Swagger UI at `http://localhost:8000/docs`.

## Run Automated Tests

```bash
pip install -r requirements.txt
python -m pytest -v
```

## Author

**Anshu Singh** — GitHub: https://github.com/as3115978-ui

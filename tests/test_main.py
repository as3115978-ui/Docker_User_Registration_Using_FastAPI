import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import User


@pytest.fixture
def client():
    db = SessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()

    with TestClient(app) as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_register_user(client):
    response = client.post("/register", json={
        "name": "Anshu Singh",
        "email": "anshu@example.com",
        "password": "SecurePass123"
    })

    assert response.status_code == 201
    assert response.json()["name"] == "Anshu Singh"
    assert "password" not in response.json()


def test_duplicate_email(client):
    user = {
        "name": "Anshu Singh",
        "email": "anshu@example.com",
        "password": "SecurePass123"
    }

    client.post("/register", json=user)
    response = client.post("/register", json=user)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_invalid_email(client):
    response = client.post("/register", json={
        "name": "Anshu Singh",
        "email": "invalid-email",
        "password": "SecurePass123"
    })

    assert response.status_code == 422

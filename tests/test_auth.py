import os
os.environ["DATABASE_URL"] = "sqlite:///./test_jobtrack.db"
os.environ["SECRET_KEY"] = "test-secret"
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_and_login():
    email = "test@example.com"
    r = client.post("/api/auth/register", json={"name":"Test User","email":email,"password":"password123"})
    assert r.status_code in (201, 409)
    r = client.post("/api/auth/login", json={"email":email,"password":"password123"})
    assert r.status_code == 200
    assert "access_token" in r.json()

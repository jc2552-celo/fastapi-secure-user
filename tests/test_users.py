# tests/test_users.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/", json={
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "johndoe"

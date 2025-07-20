from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/", json={
        "username": "janedoe",
        "email": "janedoe@example.com",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "janedoe"

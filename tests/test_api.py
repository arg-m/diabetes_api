from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"message": "API is working"}

def test_create_risk():
    payload = {
        "age": 35,
        "bmi": 27.5,
        "glucose": 120
    }

    response = client.post("/risk", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["age"] == payload["age"]
    assert data["bmi"] == payload["bmi"]
    assert data["glucose"] == payload["glucose"]
    assert "risk_score" in data

def test_list_risks():
    response = client.get("/risks")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
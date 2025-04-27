from fastapi.testclient import TestClient
from src.app.main import app  # Updated import

client = TestClient(app)

def test_generate_code():
    response = client.post("/api/generate_code", json={
        "task_description": "Print hello world",
        "language": "python"
    })
    assert response.status_code == 200
    assert "print" in response.json()["code"].lower()

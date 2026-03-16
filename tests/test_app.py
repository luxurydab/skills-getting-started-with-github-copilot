import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    # Arrange
    # (No special setup needed for root endpoint)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    # Optionally, check response content if known
    # assert response.json() == {"message": "Hello World"}

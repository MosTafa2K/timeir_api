from starlette.testclient import TestClient
from src.timeir_api.main import app

client: TestClient = TestClient(app)


def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome To Unofficial Timeir API✨"}


def test_current_date_route():
    response = client.get("/api/v1/date/current")
    assert response.status_code == 200
    assert response is not None


def test_random_quote_route():
    response = client.get("/api/v1/quote")
    assert response.status_code == 200
    assert response is not None

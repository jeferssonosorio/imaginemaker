from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_vehicle_by_identifier():
    response = client.get("/vehicle_domain/456975021")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 456975021
    assert data["domain"] == "ZZZZ-020"


def test_read_vehicle_by_identifier_1():
    response = client.get("/vehicle_domain/1")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 1
    assert data["domain"] == "AAAA-000"


def test_read_vehicle_by_identifier_2():
    response = client.get("/vehicle_domain/2222223")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 2222223
    assert data["domain"] == "ADHM-222"


def test_read_vehicle_by_identifier_3():
    response = client.get("/vehicle_domain/440050101")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 440050101
    assert data["domain"] == "ZAZA-100"


def test_read_vehicle_by_domain():
    response = client.get("/vehicle_identifier/AAAA-010")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 11
    assert data["domain"] == "AAAA-010"


def test_read_vehicle_by_domain_1():
    response = client.get("/vehicle_identifier/AAAZ-999")
    assert response.status_code == 200
    data = response.json()
    assert data["identifier"] == 26000
    assert data["domain"] == "AAAZ-999"

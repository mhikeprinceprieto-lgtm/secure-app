from app.main import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_echo_valid():
    client = app.test_client()
    response = client.post("/echo", json={"message": "hello"})
    assert response.status_code == 200
    assert response.get_json()["echo"] == "hello"

def test_echo_invalid():
    client = app.test_client()
    response = client.post("/echo", json={})
    assert response.status_code == 400

def test_echo_empty_message():
    client = app.test_client()
    response = client.post("/echo", json={"message": "   "})
    assert response.status_code == 400

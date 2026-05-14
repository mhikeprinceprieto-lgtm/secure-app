from app.main import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_echo_invalid():
    client = app.test_client()
    response = client.post("/echo", json={})
    assert response.status_code == 400

def test_echo_empty_message():
    client = app.test_client()
    response = client.post("/echo", json={"message": ""})
    # Expected failure: should reject empty message
    assert response.status_code == 400

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_read_call_name():
    name = "chitsanupong"
    response = client.get(f"/callname/${name}")
    assert response.status_code == 200
    assert response.json() == {"Hello": name}

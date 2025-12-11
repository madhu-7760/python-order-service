from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_order():
    resp = client.post("/orders", json={"item": "book", "quantity": 2})
    assert resp.status_code == 200
    data = resp.json()
    order_id = data["id"]

    get_resp = client.get(f"/orders/{order_id}")
    assert get_resp.status_code == 200
    got = get_resp.json()
    assert got["item"] == "book"
    assert got["quantity"] == 2

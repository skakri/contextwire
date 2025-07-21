from fastapi.testclient import TestClient

from contextwire.api.server import app

client = TestClient(app)


def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Hello")
        data = websocket.receive_text()
        assert data == "Message text was: Hello"

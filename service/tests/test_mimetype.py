from app import app
import json

def test_index_mimetype():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type")
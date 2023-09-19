from app import app
import json

def test_roll_response():
    response = app.test_client().get('/roll')
    assert response.status_code == 200
    assert response.is_json
    body = json.loads(response.data)
    assert type(body.get("value")) is int
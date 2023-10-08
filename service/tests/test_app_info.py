from app import app

def test_app_info():
    response = app.test_client().get('/info')
    assert response.status_code == 200
    assert response.is_json
import run_app
import pytest

@pytest.fixture
def app():
    app = run_app.app
    app.debug = True
    return app.test_client()

def test_app(app):
    response = app.get("/")
    assert response.status_code == 200
    assert b"Welcome to Poe library!" in response.data
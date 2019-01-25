import run_app
import pytest

@pytest.fixture
def app():
    app = run_app.app
    app.debug = True
    return app.test_client()

def test_app(app):
    res1 = app.get("/")
    assert res1.status_code == 200
assert b"Welcome to Poe library!" in res1.data
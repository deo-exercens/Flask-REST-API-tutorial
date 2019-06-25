"""
	test client fixture
"""
import pytest
from app import create_app  # flask application factory
from app import DB

@pytest.fixture(scope='session')
def flask_app():
    """ test app """
    app = create_app(mode='test')
    DB.init_app(app)
    return app

@pytest.fixture()
def app_context(flask_app):
    """ test app context """
    app_context_ = flask_app.app_context()
    app_context_.push()
    yield app_context_

@pytest.fixture()
def client(flask_app):
    """ test client """
    yield flask_app.test_client()

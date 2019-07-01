"""
	test client fixture
"""
import pytest
from app import create_app  # flask application factory
from app import DB

@pytest.fixture()
def config_keys():
    """ required config """
    app = ('HOST', 'PORT', 'SECRET_KEY', 'LOG_PATH',)
    database = (
        'MYSQL_DATABASE_USERNAME', 'MYSQL_ROOT_PASSWORD', 'MYSQL_DATABASE', 'MYSQL_DATABASE_HOST',
        'MYSQL_PORT',
    )
    return app + database

@pytest.fixture(scope='session')
def test_app():
    """ test app """
    app = create_app(mode='test')
    DB.init_app(app)
    return app

@pytest.fixture(scope='session')
def production_app():
    """ production app """
    app = create_app(mode='prod')
    DB.init_app(app)
    return app

@pytest.fixture(scope='session')
def development_app():
    """ development app """
    app = create_app(mode='dev')
    DB.init_app(app)
    return app

@pytest.fixture(scope='session')
def ci_app():
    """ ci app """
    app = create_app(mode='ci')
    DB.init_app(app)
    return app

@pytest.fixture()
def app_context(test_app):
    """ test app context """
    app_context_ = test_app.app_context()
    app_context_.push()
    yield app_context_

@pytest.fixture()
def client(test_app):
    """ test client """
    yield test_app.test_client()

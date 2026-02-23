import pytest
from app import create_app
from service.url_service import UrlService


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app
    UrlService.get_instance().clear()


@pytest.fixture
def client(app):
    return app.test_client()


import pytest
from service.url_service import UrlService
from util.url_validator import UrlValidator


class TestUrlGeneration:

    def test_generate_short_url(self):
        service = UrlService.get_instance()
        short_url = service.generate_short_url()
        assert len(short_url) == 6
        assert short_url.isalnum()

    def test_store_set_and_get(self):
        service = UrlService.get_instance()
        service.clear()
        service.url_storage['test'] = 'https://www.google.com'
        assert service.get_original('test') == 'https://www.google.com'
        service.clear()

    def test_store_get_nonexistent(self):
        service = UrlService.get_instance()
        service.clear()
        assert service.get_original('nonexistent') is None

    def test_shorten_and_retrieve(self):
        service = UrlService.get_instance()
        service.clear()
        short = service.shorten('https://www.example.com')
        assert len(short) == 6
        assert service.get_original(short) == 'https://www.example.com'
        service.clear()

    def test_delete(self):
        service = UrlService.get_instance()
        service.clear()
        short = service.shorten('https://www.example.com')
        assert service.delete(short) is True
        assert service.get_original(short) is None
        service.clear()

    def test_delete_nonexistent(self):
        service = UrlService.get_instance()
        service.clear()
        assert service.delete('nonexistent') is False


class TestValidator:

    def test_validate_url_empty(self):
        validator = UrlValidator.get_instance()
        valid, url, error = validator.validate_url('')
        assert not valid
        assert url is None
        assert error == 'Url cannot be empty'

    def test_validate_url_invalid_scheme(self):
        validator = UrlValidator.get_instance()
        valid, url, error = validator.validate_url('ftp://www.google.com')
        assert not valid
        assert url is None
        assert error == 'Url must use http or https'

    def test_validate_url_invalid_domain(self):
        validator = UrlValidator.get_instance()
        valid, url, error = validator.validate_url('https://')
        assert not valid
        assert url is None
        assert error == 'Url must have a valid domain'

    def test_validate_url_valid(self):
        validator = UrlValidator.get_instance()
        valid, url, error = validator.validate_url('https://www.google.com')
        assert valid
        assert url == 'https://www.google.com'
        assert error is None


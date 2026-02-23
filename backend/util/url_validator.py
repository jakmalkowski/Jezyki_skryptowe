from urllib.parse import urlparse
from util.singleton import singleton


@singleton
class UrlValidator:

    def __init__(self):
        self.allowed_schemes = ['http', 'https']

    def validate_url(self, url):
        if not url or not url.strip():
            return False, None, 'Url cannot be empty'

        url = url.strip()
        parsed = urlparse(url)

        if parsed.scheme not in self.allowed_schemes:
            return False, None, 'Url must use http or https'

        if not parsed.netloc:
            return False, None, 'Url must have a valid domain'

        return True, url, None

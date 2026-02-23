import string
import random
from util.singleton import singleton


@singleton
class UrlService:

    def __init__(self):
        self.url_storage = {}

    def generate_short_url(self):
        avail_chars = string.ascii_letters + string.digits
        return ''.join(random.choice(avail_chars) for _ in range(6))

    def shorten(self, original_url):
        short_url = self.generate_short_url()
        self.url_storage[short_url] = original_url
        return short_url

    def get_original(self, short_url):
        return self.url_storage.get(short_url)

    def delete(self, short_url):
        if short_url not in self.url_storage:
            return False
        del self.url_storage[short_url]
        return True

    def get_all(self):
        return dict(self.url_storage)

    def clear(self):
        self.url_storage.clear()

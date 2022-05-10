import requests as req
import random


class ApiClient:
    def __init__(self, url):
        self.url = url

    def random(self):
        pass


class RandomFoxApiClient(ApiClient):
    def __init__(self):
        url = 'https://randomfox.ca/floof/'
        super().__init__(url)

    def random(self):
        result = req.get(self.url)
        return result.json().get('image')


class DogApiClient(ApiClient):
    """
    https://dog.ceo/dog-api/
    Get concrete dog https://dog.ceo/dog-api/breeds-list
    """

    def __init__(self):
        url = 'https://dog.ceo/api/breeds/image/random'
        super().__init__(url)

    def random(self):
        result = req.get(self.url)
        return result.json().get('message')


class RandomFoxApiClient(ApiClient):
    def __init__(self):
        url = 'https://randomfox.ca/floof/'
        super().__init__(url)

    def random(self):
        result = req.get(self.url)
        return result.json().get('image')


class FoxrudorApiClient(ApiClient):
    def __init__(self):
        url = 'https://foxrudor.de/'
        super().__init__(url)

    def random(self):
        return self.url


class TinyfoxApiClient(ApiClient):
    def __init__(self):
        self.base_url = 'https://api.tinyfox.dev';
        url = '/img?animal=%s&json'
        super().__init__(self.resolve_url(url))

    def random(self, animal):
        result = req.get(self.url % animal)
        image_path = result.json().get('loc')
        return self.resolve_url(image_path)

    def resolve_url(self, path):
        return f"{self.base_url}{path}"

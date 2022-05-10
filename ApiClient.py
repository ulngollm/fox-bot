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

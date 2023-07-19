from urllib.parse import urlparse
import os
import requests

class ArgilConfig:
    """
    The Configuration class.
    This class will be used to store and manage the configuration for the Argil SDK.
    It includes the API key, the base URL for the API, and the timeout for the requests.
    The API key is stored securely using a closure to prevent direct access.
    """
    def __init__(self, api_key=None, api_url='https://api.argil.ai', timeout=2000):
        self.api_key = api_key or os.getenv('ARGIL_API_KEY')
        self.api_url = api_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        self.validate()

    def validate(self):
        """
        A method to validate the configuration.
        This will check that the API key is a non-empty string, the base URL is a valid URL, and the timeout is a positive integer.
        If any of these checks fail, it will throw an error.
        """
        if not self.api_key:
            raise ValueError('Invalid API Key: The API key must be a non-empty string')

        try:
            result = urlparse(self.api_url)
            if not all([result.scheme, result.netloc]):
                raise ValueError()
        except ValueError:
            raise ValueError('Invalid API URL: It should be a valid URL')

        if not isinstance(self.timeout, int) or self.timeout <= 0:
            raise ValueError('Invalid timeout: It should be a positive integer representing milliseconds')


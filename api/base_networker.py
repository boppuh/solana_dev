from urllib.parse import urljoin, urlencode

import requests


class BaseNetworker:
    def __init__(self, base_url, default_headers=None):
        """
        Initialize the BaseNetworker with a base URL.
        :param base_url: The base URL for the API.
        """
        self.base_url = base_url
        self.default_headers = default_headers or {}

    def build_url(self, endpoint, params=None):
        """
        Construct the full URL with endpoint and query parameters.
        :param endpoint: API endpoint (relative path).
        :param params: Dictionary of query parameters.
        :return: Full URL as a string.
        """
        url = urljoin(self.base_url, endpoint)
        if params:
            query_string = urlencode(params)
            url = f"{url}?{query_string}"
        return url

    def get(self, endpoint, params=None, headers=None):
        """
        Perform a GET request.
        :param endpoint: API endpoint (relative path).
        :param params: Dictionary of query parameters.
        :param headers: Additional headers for the request.
        :return: JSON response or error message.
        """
        url = self.build_url(endpoint, params)
        combined_headers = {**self.default_headers, **(headers or {})}
        try:
            response = requests.get(url, headers=combined_headers, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()  # Return JSON data
        except requests.exceptions.RequestException as e:

            return {"error": str(e)}

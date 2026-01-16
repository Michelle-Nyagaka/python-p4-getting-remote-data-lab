import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the raw response content (bytes).
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content  # <-- return bytes, not string

    def load_json(self):
        """
        Sends a GET request and returns the response parsed as JSON (dict or list).
        """
        response_bytes = self.get_response_body()
        # Decode bytes to string, then parse JSON
        return json.loads(response_bytes.decode('utf-8'))

import os
import requests


class OAuthClient:
    def __init__(self, client_id: str, client_secret: str, oauth_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_url = oauth_url

    def get_access_token(self, code: str) -> str:
        """Gets the access token."""
        url = f"{self.oauth_url}/token"
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(url, data=data)
        response.raise_for_status()

        return response.json()["access_token"]


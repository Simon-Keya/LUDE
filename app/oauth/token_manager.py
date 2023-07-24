from app.oauth.client import OAuthClient


class TokenManager:
    def __init__(self, client_id: str, client_secret: str, oauth_url: str):
        self.client = OAuthClient(client_id, client_secret, oauth_url)
        self.access_token = None

    def get_access_token(self) -> str:
        """Gets the access token."""
        if self.access_token is None:
            self.access_token = self.client.get_access_token("")

        return self.access_token


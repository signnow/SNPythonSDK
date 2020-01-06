from requests import get, post
from signnow_python_sdk.config import Config
from json import dumps,loads

class OAuth2(object):

    @staticmethod
    def request_token(username, password, scope="*"):
        """Request a new oauth2 token from the Signnow API using unirest

        Args:
            username (str): The email of user you want to create a token for.
            password (str): The account password for the user you want to create a token.
            scope (str): The scope of the token being created.

        Returns:
            dict: The JSON response from the API which includes the attributes of the token
            or the error returned.
        """
        OAUTH2_TOKEN_URL = Config().get_base_url() + '/oauth2/token'
        request = post(OAUTH2_TOKEN_URL, data={
            "username": username,
            "password": password,
            "grant_type": "password",
            "scope": scope
        }, headers={
            "Authorization": "Basic " + Config().get_encoded_credentials(),
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        })

        return loads(request.content)

    @staticmethod
    def verify(access_token=None):
        """Verify whether or not an oauth2 token exists and ha snot expired

        Args:
            access_token (str): The access token being verified on the SignNow system

        Returns:
            dict: The JSON response from the API which includes the attributes of the token
            or the error returned.
        """
        OAUTH2_TOKEN_URL = Config().get_base_url() + '/oauth2/token'
        request = get(OAUTH2_TOKEN_URL, headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return loads(request.content)

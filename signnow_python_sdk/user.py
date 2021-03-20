from requests import get, post
from signnow_python_sdk.config import Config
from json import dumps, loads


class User(object):

    @staticmethod
    def create(email, password, first_name=None, last_name=None):
        """Creates a new user in the signnow system.

        Args:
            email (str): The email of the new user you want to create (It can not already exist in the system).
            password (str): The password for the new user you are creating.
            first_name (str): An optional argument that represents the first name of the new user.
            last_name (str): An optional argument that represents the last name of the new user.

        Returns:
            dict: A dictionary representing the JSON response for the created user API or error returned.
        """
        request = post(Config().get_base_url() + '/user', headers = {
            "Authorization": "Basic " + Config().get_encoded_credentials(),
            "Accept": "application/json",
            "Content-Type": "application/json"
        }, data=dumps({
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }))

        return loads(request.content)

    @staticmethod
    def get(access_token):
        """Retrieves the user information of a user in the SignNow system using an access_token.

        Args:
            access_token (str): An access token that belongs to the user you want to retrieve.

        Returns:
            dict: A dictionary representing the JSON response for the user retrieved from the API or the error returned.
        """
        USER_URL = Config().get_base_url() + '/user'
        request = get(USER_URL , headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return loads(request.content)

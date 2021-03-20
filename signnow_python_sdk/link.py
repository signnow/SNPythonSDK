from requests import post
from signnow_python_sdk.config import Config
from json import dumps, loads



class Link(object):

    @staticmethod
    def create(access_token, document_id):
        """Creates shortened signing link urls that can be clicked be opened in a browser to sign the document

        Args:
            access_token (str): The access token of an account that has access to the document.
            document_id (str): The unique id of the document you want to create the links for.

        Returns:
            dict: A dictionary representing the JSON response containing the signing links for the document.
        """
        response = post(Config().get_base_url() + '/link', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data=dumps({
            "document_id": document_id
        }))
        return loads(response.content)

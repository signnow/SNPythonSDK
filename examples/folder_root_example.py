"""
Example demonstrating root folder functionality.
"""

from signnow.api.folder.request.folder_get_request import FolderGetRequest
from signnow.api.folder.response.folder_get_response import FolderGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN


def main():
    """
    Example of getting root folder.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = FolderGetRequest()

        response: FolderGetResponse = client.send(request).get_response()

        print(f"Root Folder ID: {response.id}")
        print(f"Root Folder Name: {response.name}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

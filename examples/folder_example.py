"""
Example demonstrating folder functionality.
"""

from signnow.api.folder.request.folder_documents_get_request import (
    FolderDocumentsGetRequest,
)
from signnow.api.folder.response.folder_documents_get_response import (
    FolderDocumentsGetResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory


def main():
    """
    Example of getting folder documents.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    from preset_data import PRESET_BEARER_TOKEN, PRESET_FOLDER_ID

    bearer_token = PRESET_BEARER_TOKEN
    folder_id = PRESET_FOLDER_ID

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = FolderDocumentsGetRequest()
        request.with_folder_id(folder_id)

        response: FolderDocumentsGetResponse = client.send(request).get_response()

        print(f"Folder ID: {response.id}")
        print(f"Folder Name: {response.name}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

"""
Example demonstrating download document group functionality.
"""

from signnow.api.documentgroup.request.download_document_group_post_request import (
    DownloadDocumentGroupPostRequest,
)
from signnow.api.documentgroup.response.download_document_group_post_response import (
    DownloadDocumentGroupPostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import (
    PRESET_BEARER_TOKEN,
    PRESET_DOCUMENT_GROUP_DOWNLOAD_ORDER,
    PRESET_DOCUMENT_GROUP_ID,
)


def main():
    """
    Example of downloading a document group.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    document_group_id = PRESET_DOCUMENT_GROUP_ID
    # this order prescribes how downloaded documents will be located in merged file
    document_order = PRESET_DOCUMENT_GROUP_DOWNLOAD_ORDER

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)
        request = DownloadDocumentGroupPostRequest(
            type="zip",
            with_history="no",
            document_order=document_order,
        )
        request.with_document_group_id(document_group_id)
        response: DownloadDocumentGroupPostResponse = client.send(
            request
        ).get_response()
        downloaded_file = response.file_path
        print(f"Downloaded file: {downloaded_file}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

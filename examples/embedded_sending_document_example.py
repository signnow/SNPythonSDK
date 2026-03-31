"""
Example demonstrating embedded sending for document functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.embeddedsending.request.document_embedded_sending_link_post_request import (
    DocumentEmbeddedSendingLinkPostRequest,
)
from signnow.api.embeddedsending.response.document_embedded_sending_link_post_response import (
    DocumentEmbeddedSendingLinkPostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded sending link for a document.

    Important:
    - The following variables are dummy, for example purposes only. Please provide actual data.
    - If you do not specify a Bearer token, it will be generated automatically.
    """
    bearer_token = PRESET_BEARER_TOKEN
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()

        # Create an embedded sending link for the uploaded document.
        embedded_sending_request = DocumentEmbeddedSendingLinkPostRequest(
            type="manage",
            redirect_uri="https://example.com",
            link_expiration=15,
            redirect_target="blank",
        )
        embedded_sending_request.with_document_id(response.id)

        embedded_sending_response: DocumentEmbeddedSendingLinkPostResponse = (
            client.send(embedded_sending_request).get_response()
        )

        print(f"Link for embedded sending: {embedded_sending_response.data.get('url')}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

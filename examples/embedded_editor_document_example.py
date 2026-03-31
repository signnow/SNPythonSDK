"""
Example demonstrating embedded editor for document functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.embeddededitor.request.document_embedded_editor_link_post_request import (
    DocumentEmbeddedEditorLinkPostRequest,
)
from signnow.api.embeddededitor.response.document_embedded_editor_link_post_response import (
    DocumentEmbeddedEditorLinkPostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded editor link for a document.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()

        # Create a link to the document editor
        editor_request = DocumentEmbeddedEditorLinkPostRequest()
        editor_request.with_document_id(response.id)
        editor_response: DocumentEmbeddedEditorLinkPostResponse = client.send(
            editor_request
        ).get_response()

        print(f"Document ID: {response.id}")
        print(
            f"Editor Link: {editor_response.data.get('url') if editor_response.data else 'N/A'}"
        )
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

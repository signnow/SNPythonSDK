"""
Example demonstrating embedded editor for document group functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentgroup.request.document_group_post_request import (
    DocumentGroupPostRequest,
)
from signnow.api.documentgroup.response.document_group_post_response import (
    DocumentGroupPostResponse,
)
from signnow.api.embeddededitor.request.document_group_embedded_editor_link_post_request import (
    DocumentGroupEmbeddedEditorLinkPostRequest,
)
from signnow.api.embeddededitor.response.document_group_embedded_editor_link_post_response import (
    DocumentGroupEmbeddedEditorLinkPostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_GROUP_NAME, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded editor link for a document group.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    group_name = PRESET_GROUP_NAME
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Create first document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id1 = response.id

        # Create second document
        request2 = DocumentPostRequest(file=path_to_document)
        response2: DocumentPostResponse = client.send(request2).get_response()
        document_id2 = response2.id

        # Create document group from both documents
        document_ids = [document_id1, document_id2]
        group_request = DocumentGroupPostRequest(
            document_ids=document_ids, group_name=group_name
        )
        group_response: DocumentGroupPostResponse = client.send(
            group_request
        ).get_response()
        group_id = group_response.id

        # Create a link to the document editor
        editor_request = DocumentGroupEmbeddedEditorLinkPostRequest(
            redirect_uri="https://example.com",
            redirect_target="blank",
            link_expiration=15,
        )
        editor_request.with_document_group_id(group_id)
        editor_response: DocumentGroupEmbeddedEditorLinkPostResponse = client.send(
            editor_request
        ).get_response()

        print(f"Link to embedded editor: {editor_response.data.get('url')}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

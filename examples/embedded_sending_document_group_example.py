"""
Example demonstrating embedded sending for document group functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentgroup.request.document_group_post_request import (
    DocumentGroupPostRequest,
)
from signnow.api.documentgroup.response.document_group_post_response import (
    DocumentGroupPostResponse,
)
from signnow.api.embeddedsending.request.document_group_embedded_sending_link_post_request import (
    DocumentGroupEmbeddedSendingLinkPostRequest,
)
from signnow.api.embeddedsending.response.document_group_embedded_sending_link_post_response import (
    DocumentGroupEmbeddedSendingLinkPostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_GROUP_NAME, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded sending link for a document group.

    Important:
    - The following variables are dummy, for example purposes only. Please provide actual data.
    - If you do not specify a Bearer token, it will be generated automatically.
    """
    bearer_token = PRESET_BEARER_TOKEN
    group_name = PRESET_GROUP_NAME
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Upload documents to create a document group, specify the paths to the files.
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id1 = response.id

        request2 = DocumentPostRequest(file=path_to_document)
        response2: DocumentPostResponse = client.send(request2).get_response()
        document_id2 = response2.id

        # Create a document group by specifying its name
        # and the IDs of the documents it will consist of.
        document_ids = [document_id1, document_id2]
        group_request = DocumentGroupPostRequest(
            document_ids=document_ids, group_name=group_name
        )
        group_response: DocumentGroupPostResponse = client.send(
            group_request
        ).get_response()
        group_id = group_response.id

        # Create an embedded sending link for the created document group.
        embedded_sending_request = DocumentGroupEmbeddedSendingLinkPostRequest(
            redirect_uri="https://example.com",
            link_expiration=15,
            redirect_target="self",
            type="manage",
        )
        embedded_sending_request.with_document_group_id(group_id)
        embedded_sending_response: DocumentGroupEmbeddedSendingLinkPostResponse = (
            client.send(embedded_sending_request).get_response()
        )

        print(f"Link for embedded sending: {embedded_sending_response.data.get('url')}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

"""
Example demonstrating template functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.template.request.clone_template_post_request import (
    CloneTemplatePostRequest,
)
from signnow.api.template.request.template_post_request import TemplatePostRequest
from signnow.api.template.response.clone_template_post_response import (
    CloneTemplatePostResponse,
)
from signnow.api.template.response.template_post_response import TemplatePostResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_TEMPLATE_NAME, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating and cloning a template.
    """
    bearer_token = PRESET_BEARER_TOKEN
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # 1. Upload a regular document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id = response.id

        # 2. Make template from the uploaded document
        template_request = TemplatePostRequest(
            document_id=document_id, document_name=PRESET_TEMPLATE_NAME
        )
        template_response: TemplatePostResponse = client.send(
            template_request
        ).get_response()
        template_id = template_response.id

        # 3. Clone the template as a document
        clone_request = CloneTemplatePostRequest()
        clone_request.with_template_id(template_id)
        clone_response: CloneTemplatePostResponse = client.send(
            clone_request
        ).get_response()
        cloned_template_id = clone_response.id

        print(f"New document ID: {document_id}")
        print(f"Template ID: {template_id}")
        print(f"Cloned from template document ID: {cloned_template_id}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

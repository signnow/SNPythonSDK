"""
Example demonstrating document prefill text field functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.data.field import Field
from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentfield.request.document_prefill_put_request import (
    DocumentPrefillPutRequest,
)
from signnow.api.documentfield.request.data.field import Field as PrefillField
from signnow.api.documentfield.request.data.field_collection import (
    FieldCollection as PrefillFieldCollection,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory
from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of prefilling text fields in a document.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    signer_role = "Product Manager"
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Upload a new document
        # or you can use an existing document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id = response.id

        # Add fields with roles to the new document
        document_fields = FieldCollection()
        document_fields.add(
            Field(
                x=50,
                y=18,
                width=200,
                height=20,
                type="text",
                page_number=0,
                required=True,
                role=signer_role,
                name="field_1",
                label="Reason to sign",
            )
        )
        put_fields_request = DocumentPutRequest(fields=document_fields)
        put_fields_request.with_document_id(document_id)
        client.send(put_fields_request)

        # Prefill an existing field by their name "field_1"
        prefill_fields = PrefillFieldCollection()
        prefill_fields.add(
            PrefillField(
                field_name="field_1", prefilled_text="custom prefilled text here"
            )
        )
        prefill_put_request = DocumentPrefillPutRequest(fields=prefill_fields)
        prefill_put_request.with_document_id(document_id)

        response_prefill_fields = client.send(prefill_put_request)
        print(f"Status code: {response_prefill_fields.get_status_code()}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

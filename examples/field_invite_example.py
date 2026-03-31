"""
Example demonstrating field invite functionality.
"""

from signnow.api.document.request.document_get_request import DocumentGetRequest
from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.data.field import Field
from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.api.document.response.document_get_response import DocumentGetResponse
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentinvite.request.send_invite_post_request import (
    SendInvitePostRequest,
)
from signnow.api.documentinvite.response.send_invite_post_response import (
    SendInvitePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory
from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of sending a field invite.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    sender_email = "sender@example.com"
    signer_email = "signer@example.com"
    signer_role = "General Manager"
    subject = "You have got an invitation to sign the contact"
    message = "Hello, please read and sign the contract"
    path_to_document = TEST_DOCUMENT_PDF  # Path to a document to be signed

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id = response.id

        # Add fields with roles to the document
        fields = FieldCollection()
        fields.add(
            Field(
                x=205,
                y=18,
                width=122,
                height=12,
                type="text",
                page_number=0,
                required=True,
                role=signer_role,
                name="signer_reason_text_field",
                label="Reason to sign",
            )
        )
        put_fields_request = DocumentPutRequest(fields=fields)
        put_fields_request.with_document_id(document_id)
        client.send(put_fields_request)

        # Get the document by id to retrieve the role IDs
        document_request = DocumentGetRequest()
        document_request.with_document_id(document_id)
        document_response: DocumentGetResponse = client.send(
            document_request
        ).get_response()

        # Send an invitation to sign the document
        roles = document_response.roles if hasattr(document_response, "roles") else []
        to = []
        for role in roles:
            if isinstance(role, dict):
                to.append(
                    {
                        "email": signer_email,
                        "role_id": role.get("unique_id", ""),
                        "role": role.get("name", ""),
                        "order": int(role.get("signing_order", "0")),
                        "subject": subject,
                        "message": message,
                    }
                )
            elif hasattr(role, "unique_id"):
                to.append(
                    {
                        "email": signer_email,
                        "role_id": role.unique_id,
                        "role": role.name if hasattr(role, "name") else "",
                        "order": (
                            int(role.signing_order)
                            if hasattr(role, "signing_order")
                            else 0
                        ),
                        "subject": subject,
                        "message": message,
                    }
                )

        invite_request = SendInvitePostRequest(
            to=to,
            from_email=sender_email,
            subject=subject,
            message=message,
        )
        invite_request.with_document_id(document_id)
        invite_response: SendInvitePostResponse = client.send(
            invite_request
        ).get_response()
        print(f"Status: {invite_response.status}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

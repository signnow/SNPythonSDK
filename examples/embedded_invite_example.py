"""
Example demonstrating embedded invite functionality.
"""

from signnow.api.document.request.document_get_request import DocumentGetRequest
from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.data.field import Field
from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.api.document.response.document_get_response import DocumentGetResponse
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.embeddedinvite.request.document_invite_link_post_request import (
    DocumentInviteLinkPostRequest,
)
from signnow.api.embeddedinvite.request.document_invite_post_request import (
    DocumentInvitePostRequest,
)
from signnow.api.embeddedinvite.response.document_invite_link_post_response import (
    DocumentInviteLinkPostResponse,
)
from signnow.api.embeddedinvite.response.document_invite_post_response import (
    DocumentInvitePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded invite.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    signer_role = "Signer 1"
    signer_email = "signer@example.com"
    signer_first_name = "Alex"
    signer_last_name = "Tester"
    embedded_invite_link_expiration_time = 45
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Step 1: Upload 1st document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id = response.id

        # Step 2: Add fields with roles to the document
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
                name="text1_field",
                label="Signing reason",
            )
        )
        put_request = DocumentPutRequest(fields=fields)
        put_request.with_document_id(document_id)
        client.send(put_request)

        # 3. Get the document by id to retrieve the role IDs
        document_request = DocumentGetRequest()
        document_request.with_document_id(document_id)
        document_response: DocumentGetResponse = client.send(
            document_request
        ).get_response()

        # 4. find the roleID by role name
        roles = document_response.roles if hasattr(document_response, "roles") else []
        role_id = ""
        for role in roles:
            if isinstance(role, dict):
                if role.get("name") == signer_role:
                    role_id = role.get("unique_id", "")
                    break
            elif hasattr(role, "name") and role.name == signer_role:
                role_id = role.unique_id if hasattr(role, "unique_id") else ""
                break

        # 5. Send embedded invite
        invites = [
            {
                "email": signer_email,
                "role_id": role_id,
                "order": 1,
                "first_name": signer_first_name,
                "last_name": signer_last_name,
            }
        ]
        invite_request = DocumentInvitePostRequest(invites=invites)
        invite_request.with_document_id(document_id)
        invite_response: DocumentInvitePostResponse = client.send(
            invite_request
        ).get_response()
        embedded_invites = (
            invite_response.data if hasattr(invite_response, "data") else []
        )

        # 6. Find invite ID
        embedded_invite_id = ""
        for embedded_invite in embedded_invites:
            if isinstance(embedded_invite, dict):
                if embedded_invite.get("email") == signer_email:
                    embedded_invite_id = embedded_invite.get("id", "")
                    break
            elif (
                hasattr(embedded_invite, "email")
                and embedded_invite.email == signer_email
            ):
                embedded_invite_id = (
                    embedded_invite.id if hasattr(embedded_invite, "id") else ""
                )
                break

        # 7. Create an embedded invite link for the embedded invite
        link_request = (
            DocumentInviteLinkPostRequest(
                auth_method="none", link_expiration=embedded_invite_link_expiration_time
            )
            .with_document_id(document_id)
            .with_field_invite_id(embedded_invite_id)
        )
        link_response: DocumentInviteLinkPostResponse = client.send(
            link_request
        ).get_response()

        print(f"Document ID: {document_id}")
        print(f"Document embedded invite ID: {embedded_invite_id}")
        print(f"Document embedded invite link: {link_response.data.get('link')}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

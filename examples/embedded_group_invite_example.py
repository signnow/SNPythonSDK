"""
Example demonstrating embedded group invite functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.data.field import Field
from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentgroup.request.document_group_post_request import (
    DocumentGroupPostRequest,
)
from signnow.api.documentgroup.response.document_group_post_response import (
    DocumentGroupPostResponse,
)
from signnow.api.embeddedgroupinvite.request.group_invite_link_post_request import (
    GroupInviteLinkPostRequest,
)
from signnow.api.embeddedgroupinvite.request.group_invite_post_request import (
    GroupInvitePostRequest,
)
from signnow.api.embeddedgroupinvite.response.group_invite_link_post_response import (
    GroupInviteLinkPostResponse,
)
from signnow.api.embeddedgroupinvite.response.group_invite_post_response import (
    GroupInvitePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """
    Example of creating an embedded group invite.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    group_name = "Test Document Group for Embedded Invite"
    signer1_role = "Signer 1"
    signer2_role = "Signer 2"
    signer1_email = "first@example.com"
    signer2_email = "second@example.com"
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Step 1: Upload 1st document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id1 = response.id

        # Step 2: Add fields and roles to the 1st document
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
                role=signer1_role,
                name="text1_field",
                label="First signer reason",
            )
        )
        fields.add(
            Field(
                x=205,
                y=38,
                width=122,
                height=12,
                type="signature",
                page_number=0,
                required=True,
                role=signer1_role,
                name="signature1_field",
                label="First signer signature",
            )
        )
        put_request1 = DocumentPutRequest(fields=fields)
        put_request1.with_document_id(document_id1)
        client.send(put_request1)

        # Step 3: Upload 2nd document
        request2 = DocumentPostRequest(file=path_to_document)
        response2: DocumentPostResponse = client.send(request2).get_response()
        document_id2 = response2.id

        # Step 4: Add fields and roles to the 2nd document
        fields2 = FieldCollection()
        fields2.add(
            Field(
                x=220,
                y=24,
                width=142,
                height=14,
                type="text",
                page_number=0,
                required=True,
                role=signer2_role,
                name="text2_field",
                label="Second signer reason",
            )
        )
        fields2.add(
            Field(
                x=205,
                y=38,
                width=122,
                height=12,
                type="signature",
                page_number=0,
                required=True,
                role=signer2_role,
                name="signature2_field",
                label="Second signer signature",
            )
        )
        put_request2 = DocumentPutRequest(fields=fields2)
        put_request2.with_document_id(document_id2)
        client.send(put_request2)

        # Step 5: Create document group
        document_ids = [document_id1, document_id2]
        group_request = DocumentGroupPostRequest(
            document_ids=document_ids, group_name=group_name
        )
        group_response: DocumentGroupPostResponse = client.send(
            group_request
        ).get_response()
        document_group_id = group_response.id

        # Step 6: Create an embedded invite for document group
        # Note: This is a simplified version. In a full implementation,
        # you would need to create proper data structures for invites
        invites = [
            {
                "order": 1,
                "signers": [
                    {
                        "email": signer1_email,
                        "role": "none",
                        "documents": [
                            {
                                "document_id": document_id1,
                                "action": "sign",
                                "role": signer1_role,
                            }
                        ],
                        "first_name": "Thomas",
                        "last_name": "Rockstar",
                    }
                ],
            },
            {
                "order": 2,
                "signers": [
                    {
                        "email": signer2_email,
                        "role": "none",
                        "documents": [
                            {
                                "document_id": document_id2,
                                "action": "sign",
                                "role": signer2_role,
                            }
                        ],
                        "first_name": "Thomas",
                        "last_name": "Popstar",
                    }
                ],
            },
        ]

        invite_request = GroupInvitePostRequest(invites=invites, sign_as_merged=False)
        invite_request.with_document_group_id(document_group_id)
        invite_response: GroupInvitePostResponse = client.send(
            invite_request
        ).get_response()
        group_invite_id = invite_response.data.get("id")

        # Create an embedded invite link for the embedded group invite
        link_request = (
            GroupInviteLinkPostRequest(
                email=signer1_email, auth_method="none", link_expiration=15
            )
            .with_document_group_id(document_group_id)
            .with_embedded_invite_id(group_invite_id)
        )

        link_response: GroupInviteLinkPostResponse = client.send(
            link_request
        ).get_response()

        print(f"DG: {document_group_id}")
        print(f"DG embedded invite: {group_invite_id}")
        print(f"DG embedded link: {link_response.data.get('link')}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

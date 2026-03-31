"""
Example demonstrating document group invite functionality.
"""

from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.data.field import Field
from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.api.document.response.document_post_response import DocumentPostResponse
from signnow.api.documentgroup.request.document_group_get_request import (
    DocumentGroupGetRequest,
)
from signnow.api.documentgroup.request.document_group_post_request import (
    DocumentGroupPostRequest,
)
from signnow.api.documentgroup.response.document_group_get_response import (
    DocumentGroupGetResponse,
)
from signnow.api.documentgroup.response.document_group_post_response import (
    DocumentGroupPostResponse,
)
from signnow.api.documentgroupinvite.request.group_invite_post_request import (
    GroupInvitePostRequest,
)
from signnow.api.documentgroupinvite.response.group_invite_post_response import (
    GroupInvitePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import (
    PRESET_BEARER_TOKEN,
    PRESET_EMAIL_MESSAGE,
    PRESET_EMAIL_SUBJECT,
    PRESET_GROUP_NAME,
    PRESET_SIGNER_EMAIL,
    PRESET_SIGNER_ROLE,
    TEST_DOCUMENT_PDF,
)


def main():
    """
    Example of creating a document group invite.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    bearer_token = PRESET_BEARER_TOKEN
    group_name = PRESET_GROUP_NAME
    signer_role = PRESET_SIGNER_ROLE
    signer_email = PRESET_SIGNER_EMAIL
    subject = PRESET_EMAIL_SUBJECT
    message = PRESET_EMAIL_MESSAGE
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Step 1: Upload 1st document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()
        document_id1 = response.id

        # Step 2: Add fields with roles to the 1st document
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
                role=signer_role,
                name="text_field",
                label="My reason",
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
        group_id = group_response.id

        # Step 6: Get the newly created document group
        get_group_request = DocumentGroupGetRequest()
        get_group_request.with_document_group_id(group_id)
        doc_group_response: DocumentGroupGetResponse = client.send(
            get_group_request
        ).get_response()

        # Step 7: Create group invite
        # Note: This is a simplified version. In a full implementation,
        # you would need to create InviteStepCollection, InviteActionCollection, etc.
        # For now, we'll use a simplified approach with basic data structures
        invite_data = {
            "invite_steps": [
                {
                    "order": 1,
                    "actions": [
                        {
                            "email": signer_email,
                            "role": signer_role,
                            "action": "sign",
                            "document_id": document_id1,
                        },
                        {
                            "email": signer_email,
                            "role": signer_role,
                            "action": "sign",
                            "document_id": document_id2,
                        },
                    ],
                    "emails": [
                        {"email": signer_email, "subject": subject, "message": message}
                    ],
                }
            ],
            "cc": [],
        }

        invite_request = GroupInvitePostRequest(
            invite_steps=invite_data["invite_steps"], cc=invite_data["cc"]
        )
        invite_request.with_document_group_id(group_id)
        invite_response: GroupInvitePostResponse = client.send(
            invite_request
        ).get_response()

        print(f"Document Group: {doc_group_response.id}")
        print(f"Document Group invite: {invite_response.id}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

"""
Example demonstrating bulk invite functionality.
"""

from signnow.api.template.request.bulk_invite_post_request import BulkInvitePostRequest
from signnow.api.template.response.bulk_invite_post_response import (
    BulkInvitePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory


def main():
    """
    Example of creating a bulk invite from a template.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # Details: https://docs.signnow.com/docs/signnow/template/operations/create-a-template-bulkinvite
    # ----------------------------------------------------
    # if it is empty or None, a new Bearer token will be created automatically
    from preset_data import (
        PRESET_BEARER_TOKEN,
        PRESET_BULK_DOCUMENT_NAME,
        PRESET_BULK_INVITE_MESSAGE,
        PRESET_BULK_INVITE_SUBJECT,
        PRESET_FOLDER_ID_2,
        PRESET_TEMPLATE_ID,
        TEST_BULK_INVITE_CSV,
    )

    bearer_token = PRESET_BEARER_TOKEN
    csv_file_path = TEST_BULK_INVITE_CSV
    template_id = PRESET_TEMPLATE_ID
    folder_id = PRESET_FOLDER_ID_2
    document_name_cloned_from_template = PRESET_BULK_DOCUMENT_NAME
    bulk_invite_subject = PRESET_BULK_INVITE_SUBJECT
    bulk_invite_message = PRESET_BULK_INVITE_MESSAGE
    # The template from which a new document will be cloned for each invite in the bulk.
    # The template must have at least one field assigned the same signing role that exists in your csv file
    # (i.e. "Signer 1")
    # Look at template_example.py to find out how to create a template.
    # Look at field_invite_example.py to find out how to add a field to document or template.
    template_id = PRESET_TEMPLATE_ID
    # The folder to store documents cloned from the template.
    folder_id = PRESET_FOLDER_ID_2
    document_name_cloned_from_template = PRESET_BULK_DOCUMENT_NAME
    bulk_invite_subject = PRESET_BULK_INVITE_SUBJECT
    bulk_invite_message = PRESET_BULK_INVITE_MESSAGE

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        request = BulkInvitePostRequest(
            file=csv_file_path,
            folder_id=folder_id,
            document_name=document_name_cloned_from_template,
            subject=bulk_invite_subject,
            email_message=bulk_invite_message,
        )
        request.with_document_id(template_id)
        response: BulkInvitePostResponse = client.send(request).get_response()

        print(f"Status: {response.status}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

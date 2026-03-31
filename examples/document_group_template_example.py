"""
Example demonstrating document group template functionality.
"""

from signnow.api.documentgrouptemplate.request.document_group_template_post_request import (
    DocumentGroupTemplatePostRequest,
)
from signnow.api.documentgrouptemplate.response.document_group_template_post_response import (
    DocumentGroupTemplatePostResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import (
    PRESET_BEARER_TOKEN,
    PRESET_FOLDER_ID_3,
    PRESET_TEMPLATE_GROUP_ID,
)


def main():
    """
    Example of creating a document group from a template.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    template_group_id = PRESET_TEMPLATE_GROUP_ID
    group_name = "My Document Group"
    client_timestamp = "2024-01-15T10:30:00Z"
    folder_id = PRESET_FOLDER_ID_3

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Create document group from template
        request = DocumentGroupTemplatePostRequest(
            group_name=group_name,
            client_timestamp=client_timestamp,
            folder_id=folder_id,
        ).with_template_group_id(template_group_id)

        response: DocumentGroupTemplatePostResponse = client.send(
            request
        ).get_response()

        print("Document Group created successfully!")
        data = response.data
        print(f"Document Group ID: {data.get('unique_id')}")
        print(f"Document Group Name: {data.get('name')}")
        print(f"Document Group State: {data.get('state')}")
        print(f"Owner Email: {data.get('owner_email')}")
        print(f"Created: {data.get('created')}")

    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

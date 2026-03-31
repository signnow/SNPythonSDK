"""
Example demonstrating document group template recipients functionality.
"""

from signnow.api.documentgrouptemplate.request.document_group_template_recipients_get_request import (
    DocumentGroupTemplateRecipientsGetRequest,
)
from signnow.api.documentgrouptemplate.request.document_group_template_recipients_put_request import (
    DocumentGroupTemplateRecipientsPutRequest,
)
from signnow.api.documentgrouptemplate.response.document_group_template_recipients_get_response import (
    DocumentGroupTemplateRecipientsGetResponse,
)
from signnow.api.documentgrouptemplate.response.document_group_template_recipients_put_response import (
    DocumentGroupTemplateRecipientsPutResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import (
    PRESET_BEARER_TOKEN,
    PRESET_DGT_RECIPIENT_DOCUMENT_ID,
    PRESET_DGT_RECIPIENTS_GROUP_ID,
)


def main():
    """
    Example of getting and updating document group template recipients.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    template_group_id = PRESET_DGT_RECIPIENTS_GROUP_ID
    document_id = PRESET_DGT_RECIPIENT_DOCUMENT_ID

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Get template recipients
        get_request = (
            DocumentGroupTemplateRecipientsGetRequest().with_template_group_id(
                template_group_id
            )
        )
        get_response: DocumentGroupTemplateRecipientsGetResponse = client.send(
            get_request
        ).get_response()

        # Access response data (dict-based)
        if get_response.data:
            for recipient in get_response.data.get("recipients", []):
                print(f"Name: {recipient.get('name')}")
                print(f"Email: {recipient.get('email')}")

            order_type = get_response.data.get("order_type")
            if order_type is not None:
                print(f"Order type: {order_type}")

            expiration = get_response.data.get("general_expiration_days")
            if expiration is not None:
                print(f"Expiration days: {expiration}")

            reminder = get_response.data.get("general_reminder")
            if reminder is not None:
                print(f"Remind before: {reminder.get('remind_before')}")
                print(f"Remind repeat: {reminder.get('remind_repeat')}")
                print(f"Remind after: {reminder.get('remind_after')}")

        # Update template recipients with expiration, reminder, and order type
        put_request = DocumentGroupTemplateRecipientsPutRequest(
            recipients=[
                {
                    "name": "Signer",
                    "email": "signer@example.com",
                    "role": "Recipient 1",
                    "order": 1,
                    "documents": [
                        {
                            "id": document_id,
                            "role": "Recipient 1",
                            "action": "sign",
                        }
                    ],
                }
            ],
            general_expiration_days=30,
            general_reminder={
                "remind_before": 5,
                "remind_repeat": 3,
                "remind_after": 7,
            },
            order_type="recipient_order",
        ).with_template_group_id(template_group_id)

        put_response: DocumentGroupTemplateRecipientsPutResponse = client.send(
            put_request
        ).get_response()

        print("Template recipients updated successfully!")
        if put_response.data:
            print(f"Response data: {put_response.data}")

    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.documentinvite.request import FreeFormInvitePostRequest
from signnow.api.documentinvite.response import FreeFormInvitePostResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_DOCUMENT_ID_3


def main():
    """Main function to demonstrate free form invite creation."""
    bearer_token = PRESET_BEARER_TOKEN
    document_id = PRESET_DOCUMENT_ID_3
    sender_email = "sender@example.com"
    signer_email = "signer@example.com"

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Create free form invite
        request = FreeFormInvitePostRequest(to=signer_email, from_email=sender_email)
        request.with_document_id(document_id)
        response: FreeFormInvitePostResponse = client.send(request).get_response()

        print(f"Invite Request ID: {response.id}")
        print(f"Result: {response.result}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

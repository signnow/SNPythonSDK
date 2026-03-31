"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.documentinvite.request import SigningLinkPostRequest
from signnow.api.documentinvite.response import SigningLinkPostResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_DOCUMENT_ID_2


def main():
    """Main function to demonstrate signing link creation."""
    bearer_token = PRESET_BEARER_TOKEN
    document_id = PRESET_DOCUMENT_ID_2
    redirect_url = None  # URL to redirect after successful signing (optional)

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Create signing link
        request = SigningLinkPostRequest(document_id, redirect_url)
        response: SigningLinkPostResponse = client.send(request).get_response()

        print(f"Signing link: {response.url}")
        print(f"Signing link (no signup): {response.url_no_signup}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

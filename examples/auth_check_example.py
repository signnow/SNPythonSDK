"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.auth.request import TokenGetRequest
from signnow.api.auth.response import TokenGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN


def main():
    """Main function to demonstrate token check."""
    bearer_token = PRESET_BEARER_TOKEN

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)
        response: TokenGetResponse = client.send(TokenGetRequest()).get_response()

        print(f"Token type: {response.token_type}")
        print(f"Token: {response.access_token}")
        print(f"Type: {response.token_type}")
        print(f"Scope: {response.scope}")
        print(f"Expires at: {response.expires_in}")
    except SignNowApiException as e:
        print("Exception when signNow API call TokenGetRequest")
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

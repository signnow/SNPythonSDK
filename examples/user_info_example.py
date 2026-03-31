"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.user.request import UserGetRequest
from signnow.api.user.response import UserGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN


def main():
    """Main function to demonstrate user info retrieval."""
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)
        request = UserGetRequest()
        response: UserGetResponse = client.send(request).get_response()
        print(f"User ID: {response.id}")
        print(f"User name: {response.first_name} {response.last_name}")
        print(f"Primary email: {response.primary_email}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

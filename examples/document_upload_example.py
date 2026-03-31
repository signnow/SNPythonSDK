"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.document.request import DocumentPostRequest
from signnow.api.document.response import DocumentPostResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, TEST_DOCUMENT_PDF


def main():
    """Main function to demonstrate document upload."""
    bearer_token = PRESET_BEARER_TOKEN
    path_to_document = TEST_DOCUMENT_PDF

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Upload document
        request = DocumentPostRequest(file=path_to_document)
        response: DocumentPostResponse = client.send(request).get_response()

        print(f"New document ID: {response.id}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

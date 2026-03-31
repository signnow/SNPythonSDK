"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.document.request import DocumentGetRequest
from signnow.api.document.response import DocumentGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_DOCUMENT_ID


def main():
    """Main function to demonstrate document retrieval."""
    bearer_token = PRESET_BEARER_TOKEN
    document_id = PRESET_DOCUMENT_ID

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)
        request = DocumentGetRequest()
        request.with_document_id(document_id)
        response: DocumentGetResponse = client.send(request).get_response()
        print(f"Document ID: {response.id}")
        print(f"Document Name: {response.document_name}")
        print(f"Document Owner: {response.user_id}")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

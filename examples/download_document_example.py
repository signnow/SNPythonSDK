"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.api.document.request import DocumentDownloadGetRequest
from signnow.api.document.response import DocumentDownloadGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_DOCUMENT_ID_2


def main():
    """Main function to demonstrate document download."""
    bearer_token = PRESET_BEARER_TOKEN
    document_id = PRESET_DOCUMENT_ID_2

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # Download document
        request = DocumentDownloadGetRequest()
        request.with_document_id(document_id)
        # Optional: specify download type
        # request.with_type("collapsed")  # or "zip" or "email"
        # Optional: include history
        # request.with_history("yes")

        response: DocumentDownloadGetResponse = client.send(request).get_response()

        file_path = response.get_file()
        if file_path:
            print(f"Document downloaded to: {file_path}")
        else:
            print("Download failed - no file path returned")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

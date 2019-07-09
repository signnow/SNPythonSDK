import signnow_python_sdk
import os
from datetime import datetime

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_SECRET",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"
    document_ids = ["DOCUMENT_ID1", "DOCUMENT_ID2"]

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')

    dir_path = './downloaded_documents'
    file_name = "signed_document"

    # Merge documents
    signnow_python_sdk.Document.merge_and_download(access_token['access_token'], document_ids, file_name, dir_path)

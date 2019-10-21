import signnow_python_sdk

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"
    document_id = "DOCUMENT_ID"

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')

    dir_path = './downloaded_documents'
    enclose_document_history = False
    file_name = "signed_document"

    # Download signed document
    signnow_python_sdk.Document.download(access_token['access_token'], document_id, file_name, dir_path, enclose_document_history)

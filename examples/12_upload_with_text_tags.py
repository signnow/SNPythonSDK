import signnow_python_sdk
import os

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')

    # Upload a new document
    file_path = os.path.dirname(os.path.realpath(__file__)) + '/TestDocument.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token['access_token'], file_path, True)

    # Get documentdata
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])

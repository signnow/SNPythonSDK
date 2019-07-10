import signnow_python_sdk
import os
from datetime import datetime

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"

    # Create access_token for the user
    print ("Creating access token:")
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')
    print (username + "'s access token: " + access_token['access_token'])
    print ("The access token's scope: " + access_token['scope'])
    print ("\n")

    # Upload a new document
    print ("Uploading a new document:")
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token['access_token'], dir_path)
    print ("Uploaded document's id:", doc_id['id'])
    print ("\n")

    # Update a document with a text element and three fields.
    signer_role1 = "Signer 1"
    signer_role2 = "Signer2"
    # Create the PUT /document payload
    doc_payload = {
        "texts": [
            {
                "size": 22,
                "x": 61,
                "y": 72,
                "page_number": 0,
                "font": "Arial",
                "data": "a sample text element",
                "line_height": 9.075,
                "client_timestamp": datetime.now().strftime("%s")
            }
        ],
        "fields": [
            {
                "x": 61,
                "y": 100,
                "width": 120,
                "height": 34,
                "page_number": 0,
                "role": signer_role1,
                "required": True,
                "type": "signature"
            },
            {
                "x": 61,
                "y": 160,
                "width": 120,
                "height": 12,
                "page_number": 0,
                "label": "New Label",
                "role": signer_role2,
                "required": True,
                "type": "text"
            },
            {
                "x": 61,
                "y": 178,
                "width": 41,
                "height": 26,
                "page_number": 0,
                "role": signer_role1,
                "required": True,
                "type": "initials"
            }
        ]
    }
    print("Updating the document:")
    put_doc_response = signnow_python_sdk.Document.update(access_token['access_token'], doc_id['id'], doc_payload)
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print("The document's id:", document_data['id'])
    print("The document's name:", document_data['document_name'])
    print("The document's owner:", document_data['owner'])
    print("The document's page_count:", document_data['page_count'])
    print("The document's fields:", document_data['fields'])
    print("The document's texts:", document_data['texts'])

    # Create the signing links for a document.
    print ("Creating a signing link for the document:")
    links = signnow_python_sdk.Link.create(access_token['access_token'], doc_id['id'])
    print ("The  link is:", links['url'])
    print ("The no sign up link is:", links['url_no_signup'])

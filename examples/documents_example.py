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
    print ("The access token's scope: " + access_token['scope'] + "\n")

    # Upload a new document
    print ("Uploading a new document:")
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token['access_token'], dir_path)
    print ("Uploaded document's id:" + doc_id['id'] + "\n")


    # Get the document
    print ("Getting the documents data:")
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print ("The document's id:", document_data['id'])
    print ("The document's name:", document_data['document_name'])
    print ("The document's owner:", document_data['owner'])
    print ("The document's page_count:", document_data['page_count'] + '\n')

    # Get document history
    print("Getting the document history:")
    document_history = signnow_python_sdk.Document.get_history(access_token['access_token'], doc_id['id'])
    print("The document's history:", document_history)

    # Update a document with a text element and three fields.
    signer_role = "Signer 1"
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
                "role": signer_role,
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
                "role": signer_role,
                "required": True,
                "type": "text"
            },
            {
                "x": 61,
                "y": 178,
                "width": 41,
                "height": 26,
                "page_number": 0,
                "role": signer_role,
                "required": True,
                "type": "initials"
            }
        ]
    }
    print ("Updating the document:")
    put_doc_response = signnow_python_sdk.Document.update(access_token['access_token'], doc_id['id'], doc_payload)
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print ("The document's id:", document_data['id'])
    print ("The document's name:", document_data['document_name'])
    print ("The document's owner:", document_data['owner'])
    print ("The document's page_count:", document_data['page_count'])
    print ("The document's fields:", document_data['fields'])
    print ("The document's texts:", document_data['texts'])

    # Send an invite for the document
    print ("Sending document invite:")
    #to = []
    for role in document_data['roles']:
        to.append({
            "email": "gene+1@pdffiller.com",
            "role_id": "",
            "role": role['name'],
            "order": role['signing_order']
        })


    to = [{
        "email": "gene+1@pdffiller.com",
        "role_id": "",
        "role": "Signer 1",
        "order": 1
    }]

    invite_payload = {
        "to": to,
        "from":username
    }
    invite_response = signnow_python_sdk.Document.invite(access_token['access_token'], doc_id['id'], invite_payload)
    print ("Invite successfully sent:", invite_response['status'] == 'success')
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print ("The document's id:", document_data['id'])
    print ("The document's name:", document_data['document_name'])
    print ("The document's owner:", document_data['owner'])
    print ("The document's field_invites:", document_data['field_invites'])

    print ("Downloading the document:")
    file_path = './downloaded_documents'
    signnow_python_sdk.Document.download(access_token['access_token'], doc_id['id'], "new_file_for_me",
                                         file_path, False)
    print ("Document downloaded. Check the %s folder." % os.path.abspath(file_path))

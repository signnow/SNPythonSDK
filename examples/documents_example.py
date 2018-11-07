import cba_signnow
import os
from datetime import datetime

if __name__ == '__main__':
    cba_signnow.Config(client_id="0fccdbc73581ca0f9bf8c379e6a96813",
                              client_secret="3719a124bcfc03c534d4f5c05b5a196b",
                              base_url="https://api-eval.signnow.com")

    # Enter your own credentials
    username = ''
    password = ''

    # Create the access_token for the user
    print "Creating access token:"
    access_token = cba_signnow.OAuth2.request_token(username, password, '*')
    print username + "'s access token: " + access_token['access_token']
    print "The access token's scope: " + access_token['scope']
    print "\n"

    # Upload a new document
    print "Uploading a new document:"
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = cba_signnow.Document.upload(access_token['access_token'], dir_path)
    print "Uploaded document's id:", doc_id['id']
    print "\n"

    # Get the documents
    print "Getting the documents data:"
    document_data = cba_signnow.Document.get(access_token['access_token'], doc_id['id'])
    print "The document's id:", document_data['id']
    print "The document's name:", document_data['document_name']
    print "The document's owner:", document_data['owner']
    print "The document's page_count:", document_data['page_count']
    print "\n"

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
    print "Updating the document:"
    put_doc_response = cba_signnow.Document.update(access_token['access_token'], doc_id['id'], doc_payload)
    document_data = cba_signnow.Document.get(access_token['access_token'], doc_id['id'])
    print "The document's id:", document_data['id']
    print "The document's name:", document_data['document_name']
    print "The document's owner:", document_data['owner']
    print "The document's page_count:", document_data['page_count']
    print "The document's fields:", document_data['fields']
    print "The document's texts:", document_data['texts']
    print "\n"

    # Send an invite for the document
    print "Sending document invite:"
    to = []
    for role in document_data['roles']:
        to.append({
            "email": "fakeemail%s@harakirimail.com" % len(to),
            "role_id": "",
            "role": role['name'],
            "order": role['signing_order']
        })
    invite_payload = {
        "to": to,
        "from":username
    }
    invite_response = cba_signnow.Document.invite(access_token['access_token'], doc_id['id'], invite_payload)
    print "Invite successfully sent:", invite_response['status'] == 'success'
    document_data = cba_signnow.Document.get(access_token['access_token'], doc_id['id'])
    print "The document's id:", document_data['id']
    print "The document's name:", document_data['document_name']
    print "The document's owner:", document_data['owner']
    print "The document's field_invites:", document_data['field_invites']
    print "\n"

    print "Downloading the document:"
    file_path = './downloaded_documents'
    cba_signnow.Document.download(access_token['access_token'], doc_id['id'], "new_file_for_me",
                                         file_path, True)
    print "Document downloaded. Check the %s folder." % os.path.abspath(file_path)

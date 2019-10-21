import signnow_python_sdk
from datetime import datetime
import os


if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_SECRET",
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

    # Convert document to a template
    print ("Converting the document into a template:")
    template_id = signnow_python_sdk.Template.create(access_token['access_token'], doc_id['id'], "My New Template")
    template_data = signnow_python_sdk.Document.get(access_token['access_token'], template_id['id'])
    print ("The template's id:", template_data['id'])
    print ("The template's name:", template_data['document_name'])
    print ("The template's owner:", template_data['owner'])
    print ("The template's page_count:", template_data['page_count'])
    print ("\n")

    # Create a document from the template
    print ("Creating a new document from the template:")
    doc_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id['id'], "New Doc From Template")
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print ("The doucments's id:", document_data['id'])
    print ("The document's name:", document_data['document_name'])
    print ("The document's owner:", document_data['owner'])
    print ("The document's page_count:", document_data['page_count'])
    print ("Document was created from our template:", document_data['origin_document_id'] == template_data['id'])
    print ("\n")

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
                "role": "Signer 1",
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
                "role": "Signer 1",
                "required": True,
                "type": "text"
            },
            {
                "x": 61,
                "y": 178,
                "width": 41,
                "height": 26,
                "page_number": 0,
                "role": "Signer 2",
                "required": True,
                "type": "initials"
            }
        ]
    }
    print ("Updating the document:")
    put_doc_response = signnow_python_sdk.Template.update(access_token['access_token'], template_id['id'], doc_payload)

    print(put_doc_response)


    routing_payload = {
      "template_data":[
       {
         "default_email":"",
         "inviter_role": False,
         "name":"Signer 1",
         "role_id":"",
         "signing_order":1,
         "decline_by_signature":False
       },
       {
         "default_email":"",
         "inviter_role":False,
         "name":"Signer 2",
         "role_id":"",
         "signing_order":1,
         "decline_by_signature":False
       }
    ],
     "cc":[],
     "cc_step":[]
    }

    doc_id = signnow_python_sdk.Template.routing_detail(access_token['access_token'], template_id['id'], routing_payload)
    print(doc_id)
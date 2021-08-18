import signnow_python_sdk

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              environment="production")

    # Enter your own credentials
    username = "USER_NAME"
    password = "USER_PASSWORD"
    template_id = "TEMPLATE_ID"

    # Create access_token for the user
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')

    to = [{
        "email": "testemail@signnow.com",
        "role_id": "",
        "role": "Signer 1",
        "order": 1
    },
    {
        "email": "testemail1@signnow.com",
        "role_id": "",
        "role": "Signer 2",
        "order": 2

    }]

    invite_payload = {
        "to": to,
        "from": username
    }

    # Create a document from the template
    document_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id, "New Doc From Template")

    # Get document data
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], document_id['id'])

    webhook_payload = {
        "event": "document.complete",
        "entity_id": document_id['id'],
        "action": "callback",
        "attributes": {
            "callback": "https://webhook.site/1d9d30fb-b128-418d-975b-612eb5b4bf",
            "use_tls_12": True,
        }
    }
    # Create webhook to send POST to custom endpoint when document is signed
    webhook_response = signnow_python_sdk.Webhook.create(access_token['access_token'], webhook_payload)

    # List available webhooks
    list_webhooks = signnow_python_sdk.Webhook.list_all(access_token['access_token'])

    # Send signature invite
    invite_response = signnow_python_sdk.Document.invite(access_token['access_token'], document_id['id'], invite_payload)

    dir_path = './downloaded_documents'
    enclose_document_history = False
    file_name = "signed_document"

    # Once webhook is received, download signed document
    signnow_python_sdk.Document.download(access_token['access_token'], document_id['id'], file_name, dir_path,
                                         enclose_document_history)

    '''
    Webhook response sample  
       {
        "meta": {
           "timestamp": 1571695439,
           "event": "document.complete",
           "environment": "https://api.signnow.com",
           "callback_url": "https://webhook.site/1d9d30fb-b128-418d-975b-612ebeb5bf",
        },
        "content": {
           "document_id": "ce8e7ff332a4d1b820ebd24a065d8111fc0",
           "document_name": "New Doc From Template",
           "user_id": "75b2215f6b72ad45206bdcbe11ed24"
        }
       }
    '''




import signnow_python_sdk

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="CLIENT_SECRET",
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
    }]

    invite_payload = {
        "to": to,
        "from": username
    }

    # Create a document from the template
    doc_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id, "New Doc From Template")

    # Get document data
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])

    # Send signature invite
    invite_response = signnow_python_sdk.Document.invite(access_token['access_token'], doc_id['id'], invite_payload)



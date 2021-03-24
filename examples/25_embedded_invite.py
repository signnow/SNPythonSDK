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
        "invites": to
    }

    # Set embedded link expiration to 30 min
    link_payload = {
        "auth_method": "none",
        "link_expiration": 30
    }

    # Create a document from the template
    doc_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id, "New Doc From Template")

    # Get document data
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])

    # Send signature invite
    invite_response = signnow_python_sdk.Document.embedded_invite(access_token['access_token'], doc_id['id'],
                                                                  invite_payload)
    # Create embedded links for signature invite. Signature invite should be in "pending status".
    for invite in invite_response["data"]:
        if invite["status"] == "pending":
            embedded_link = signnow_python_sdk.Document.embedded_invite_link(access_token['access_token'], doc_id['id'],
                                                                         invite['id'], link_payload)
    # Delete embedded invite
    signnow_python_sdk.Document.delete_embedded_invite(access_token['access_token'], doc_id['id'])
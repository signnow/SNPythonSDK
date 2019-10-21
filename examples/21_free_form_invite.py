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

    to = [{
        "email": "testemail@pdffiller.com",
        "role_id": "",
        "role": "Signer 1",
        "order": 1
    }]

    invite_payload = {
        "to": to,
        "from": username
    }

    # Send document invite
    invite_response = signnow_python_sdk.Document.invite(access_token['access_token'], document_id, invite_payload)



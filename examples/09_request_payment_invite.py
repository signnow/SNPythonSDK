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

    invite_payload = {
        "document_id": 'DOCUMENT_ID_GOES_HERE',
        "to": [
            {
                "email": 'EMAIL_OF_SIGNER',
                "role": 'Signer 1',
                "role_id": '',
                "order": 1,
                "reassign": 0,
                "decline_by_signature": 0,
                "reminder": 4,
                "expiration_days": 27,
                "subject": 'Field invite Signer1',
                "message": 'Message',
                "payment_request": {
                    "type": 'fixed',
                    "amount": 12,
                    "currency": 'US Dollar',
                    "merchant_id": 'MERCHANT_ID',
                 },
            },
        ],
        "from": 'EMAIL_OF_SENDER',
    };

    # Create a document from the template
    doc_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id, "New Doc From Template")

    # Send signature invite
    invite_response = signnow_python_sdk.Document.invite(access_token['access_token'], doc_id['id'], invite_payload)

import signnow_python_sdk
from datetime import datetime

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

    # Update document template with payload
    put_doc_response = signnow_python_sdk.Template.update(access_token['access_token'], template_id, doc_payload)
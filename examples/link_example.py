import signnow_python_sdk
import os

if __name__ == '__main__':
    signnow_python_sdk.Config(client_id="0fccdbc73581ca0f9bf8c379e6a96813",
                              client_secret="3719a124bcfc03c534d4f5c05b5a196b",
                              base_url="https://api-eval.signnow.com")

    # Enter your own credentials
    username = ''
    password = ''

    # Create the access_token for the user
    print "Creating access token:"
    access_token = signnow_python_sdk.OAuth2.request_token(username, password, '*')
    print username + "'s access token: " + access_token['access_token']
    print "The access token's scope: " + access_token['scope']
    print "\n"

    # Upload a new document
    print "Uploading a new document:"
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token['access_token'], dir_path)
    print "Uploaded document's id:", doc_id['id']
    print "\n"

    # Create the signing links for a document.
    print "Creating a signing link for the document:"
    links = signnow_python_sdk.Link.create(access_token['access_token'], doc_id['id'])
    print "The  link is:", links['url']
    print "The no sign up link is:", links['url_no_signup']

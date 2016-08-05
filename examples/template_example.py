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

    # Convert document to a template
    print "Converting the document into a template:"
    template_id = signnow_python_sdk.Template.create(access_token['access_token'], doc_id['id'], "My New Template")
    template_data = signnow_python_sdk.Document.get(access_token['access_token'], template_id['id'])
    print "The template's id:", template_data['id']
    print "The template's name:", template_data['document_name']
    print "The template's owner:", template_data['owner']
    print "The template's page_count:", template_data['page_count']
    print "\n"

    # Create a document from the template
    print "Creating a new document from the template:"
    doc_id = signnow_python_sdk.Template.copy(access_token['access_token'], template_id['id'], "New Doc From Template")
    document_data = signnow_python_sdk.Document.get(access_token['access_token'], doc_id['id'])
    print "The doucments's id:", document_data['id']
    print "The document's name:", document_data['document_name']
    print "The document's owner:", document_data['owner']
    print "The document's page_count:", document_data['page_count']
    print "Document was created from our template:", document_data['origin_document_id'] == template_data['id']
    print "\n"

import signnow_python_sdk

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

    # Create an event subscription
    print ("Creating a new document update event subscription:")
    webhook_response = signnow_python_sdk.Webhook.create(access_token['access_token'], 'document.update',
                                                         "https://enwp1fkcbuagb.x.pipedream.net/")
    print ("The event subscriptions id is:", webhook_response['id'])

    print("Creating a new document complete event subscription:")
    webhook_response = signnow_python_sdk.Webhook.create(access_token['access_token'], 'document.complete',
                                                         "https://enwp1fkcbuagb.x.pipedream.net/")
    print("The event subscriptions id is:", webhook_response['id'])

    # Get a list of all webhooks for a user.
    print ("Getting a list of webhooks:")
    webhooks = signnow_python_sdk.Webhook.list_all(access_token['access_token'])
    for subscription in webhooks['subscriptions']:
        print ("You have a %s subcription" % subscription['event'])
        print ("It has the callback %s" % subscription['callback_url'])

    # Delete all event subscriptions from an account
    # for subscription in webhooks['subscriptions']:
    #     print ("Deleting the %s event subscription:" % subscription['event'])
    #     deleted_response = signnow_python_sdk.Webhook.delete(access_token['access_token'], subscription['id'])
    #     print ("Subscription %s deleted" % deleted_response['id'])
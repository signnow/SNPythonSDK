import cba_signnow

if __name__ == '__main__':
    cba_signnow.Config(client_id="0fccdbc73581ca0f9bf8c379e6a96813",
                              client_secret="3719a124bcfc03c534d4f5c05b5a196b",
                              base_url="https://api-eval.signnow.com")

    # Enter your own credentials
    username = ''
    password = ''

    # Create the access_token for the user
    print "Creating access token:"
    access_token = cba_signnow.OAuth2.request_token(username, password, '*')
    print username + "'s access token: " + access_token['access_token']
    print "The access token's scope: " + access_token['scope']
    print "\n"

    # Create an event subscription
    print "Creating a new document update event subscription:"
    webhook_response = cba_signnow.Webhook.create(access_token['access_token'], 'document.update',
                                                         "http://requestb.in/sdfcflsd")
    print "The event subscriptions id is:", webhook_response['id']

    # Get a list of all webhooks for a user.
    print "Getting a list of webhooks:"
    webhooks = cba_signnow.Webhook.list_all(access_token['access_token'])
    for subscription in webhooks['subscriptions']:
        print "You have a %s subcription" % subscription['event']
        print "It has the callback %s" % subscription['callback_url']

    # Delete all event subscriptions from an account
    for subscription in webhooks['subscriptions']:
        print "Deleting the %s event subscription:" % subscription['event']
        deleted_response = cba_signnow.Webhook.delete(access_token['access_token'], subscription['id'])
        print "Subscription %s deleted" % deleted_response['id']
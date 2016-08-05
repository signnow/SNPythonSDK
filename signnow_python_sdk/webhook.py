from unirest import get, post, delete
from config import Config
from json import dumps


class Webhook(object):

    @staticmethod
    def list_all(access_token):
        """Returns a list of all the event subscriptions/webhooks for an account.

        Args:
            access_token (str): The access token of the account you want to get event subscriptions for.

        Returns:
            dict: A dictionary representing the JSON data of the event subscriptions or the error returned by the API.
        """
        response = get(Config().get_base_url() + '/event_subscription', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return response.body

    @staticmethod
    def create(access_token, event, callback_url):
        """Creates or updates a sevent subscription/webhook for an account.

        Args:
            access_token (str): The access token of the account you want to create the subscription for.
            event (str): The event you want to create the subscription for.
            callback_url (str): The url that will recieve the webhook request from the signnow server.

        Returns:
            dict: The JSON response of the newly created event subscription or the error returned by the API
        """
        response = post(Config().get_base_url() + '/event_subscription', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, params = dumps({
            "event": event,
            "callback_url": callback_url
        }))

        return response.body

    @staticmethod
    def delete(access_token, subscription_id):
        """Deletes an event subscription with the given id

        Args:
            access_token (str): The access token of the account you want to delete the event subscriptiotn from.
            subscription_id (str): The unique id of the subscription being deleted.

        Returns:
            dict: The JSON response from the API with the id of the deleted subscription or an API error.
        """
        response = delete(Config().get_base_url() + '/event_subscription/' + subscription_id, headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return response.body

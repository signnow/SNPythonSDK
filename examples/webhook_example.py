"""
Example demonstrating webhook functionality.
"""

from signnow.api.webhook.request.subscription_delete_request import (
    SubscriptionDeleteRequest,
)
from signnow.api.webhook.request.subscription_get_request import SubscriptionGetRequest
from signnow.api.webhook.request.subscription_post_request import (
    SubscriptionPostRequest,
)
from signnow.api.webhook.request.data.attribute import Attribute
from signnow.api.webhook.response.subscription_get_response import (
    SubscriptionGetResponse,
)
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

from preset_data import PRESET_BEARER_TOKEN, PRESET_USER_ID


def main():
    """
    Example of creating, getting, and deleting webhook subscriptions.
    """
    # Set your actual input data here
    # Note: following values are dummy, just for example
    # ----------------------------------------------------
    # if it is not specified here, a new Bearer token will be created automatically
    bearer_token = PRESET_BEARER_TOKEN
    # Your user ID (from user_info_example response.id)
    user_id = PRESET_USER_ID
    # Your URL to catch webhooks for subscribed events in SignNow
    callback_url = "https://demo.requestcatcher.com/"

    try:
        client: ApiClient = SdkFactory.create_api_client_with_bearer_token(bearer_token)

        # 1. Subscribe to the event, and then you can retrieve payloads
        # at your endpoint (i.e. callback URL)
        subscription_request = SubscriptionPostRequest(
            event="user.document.open",  # event name; the event triggers when a user opens a document
            entity_id=user_id,  # user ID that triggers their events
            action="callback",  # we will send callbacks
            attributes=Attribute(callback=callback_url),  # to the specified URL
            secret_key=None,
        )
        client.send(subscription_request)
        print("Subscription is created")

        # 2. Get all subscriptions
        subscriptions_request = SubscriptionGetRequest()
        subscriptions_response: SubscriptionGetResponse = client.send(
            subscriptions_request
        ).get_response()

        subscription_id = None
        subscriptions = subscriptions_response.data
        for subscription in subscriptions:
            print(f"ID: {subscription.get('id')}")
            print(f"Event: {subscription.get('event')}")
            print(f"Entity ID: {subscription.get('entity_id')}")
            print(f"Action: {subscription.get('action')}")
            attributes = subscription.get("attributes", {})
            headers = (
                attributes.get("headers", {}) if isinstance(attributes, dict) else {}
            )
            print(f"Headers: {headers}")
            print("-" * 10)

            if subscription.get("event") == "user.document.open":
                subscription_id = subscription.get("id")

        # 3. Delete the subscription
        if subscription_id:
            delete_request = SubscriptionDeleteRequest()
            delete_request.with_event_subscription_id(subscription_id)
            client.send(delete_request)
            print("Subscription is deleted")
    except SignNowApiException as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()

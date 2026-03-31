"""
Webhook request classes.
"""

from signnow.api.webhook.request.subscription_delete_request import (
    SubscriptionDeleteRequest,
)
from signnow.api.webhook.request.subscription_get_request import (
    SubscriptionGetRequest,
)
from signnow.api.webhook.request.subscription_post_request import (
    SubscriptionPostRequest,
)
from signnow.api.webhook.request.subscription_put_request import (
    SubscriptionPutRequest,
)

__all__ = [
    "SubscriptionPostRequest",
    "SubscriptionGetRequest",
    "SubscriptionPutRequest",
    "SubscriptionDeleteRequest",
]

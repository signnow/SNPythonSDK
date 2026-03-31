"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="deleteEventSubscription",
    url="/api/v2/events/{event_subscription_id}",
    method="delete",
    auth="basic",
    namespace="webhook",
    entity="subscription",
    content_type="application/json",
)
class SubscriptionDeleteRequest(RequestInterface):
    """
    Represents a request to delete a subscription.
    """

    def __init__(self):
        """Initializes a new SubscriptionDeleteRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_event_subscription_id(
        self, event_subscription_id: str
    ) -> "SubscriptionDeleteRequest":
        """
        Adds the event subscription id to the URI parameters.

        Args:
            event_subscription_id: The id of the event subscription to be deleted.

        Returns:
            The current SubscriptionDeleteRequest instance.
        """
        self._uri_params["event_subscription_id"] = event_subscription_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters map.

        Returns:
            A dictionary containing all URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

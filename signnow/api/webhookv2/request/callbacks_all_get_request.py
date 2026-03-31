"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getEventSubscriptionCallbacksV2",
    url="/v2/event-subscriptions/{event_subscription_id}/callbacks",
    method="get",
    auth="bearer",
    namespace="webhookV2",
    entity="callbacksAll",
    content_type="application/json",
)
class CallbacksAllGetRequest(RequestInterface):
    """
    Represents a request to get all callbacks for a specific event subscription.
    """

    def __init__(self):
        """Initializes a new CallbacksAllGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_event_subscription_id(
        self, event_subscription_id: str
    ) -> "CallbacksAllGetRequest":
        """
        Adds the event subscription ID to the URI parameters.

        Args:
            event_subscription_id: The ID of the event subscription.

        Returns:
            The current request object with the updated URI parameters.
        """
        self._uri_params["event_subscription_id"] = event_subscription_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

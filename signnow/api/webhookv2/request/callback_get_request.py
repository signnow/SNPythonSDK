"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getEventSubscriptionCallback",
    url="/v2/event-subscriptions/{event_subscription_id}/callbacks/{callback_id}",
    method="get",
    auth="bearer",
    namespace="webhookV2",
    entity="callback",
    content_type="application/json",
)
class CallbackGetRequest(RequestInterface):
    """
    Represents a request to get a callback from an event subscription.
    """

    def __init__(self):
        """Initializes a new CallbackGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_event_subscription_id(
        self, event_subscription_id: str
    ) -> "CallbackGetRequest":
        """
        Sets the event subscription ID for the request.

        Args:
            event_subscription_id: The event subscription ID.

        Returns:
            The updated request.
        """
        self._uri_params["event_subscription_id"] = event_subscription_id
        return self

    def with_callback_id(self, callback_id: str) -> "CallbackGetRequest":
        """
        Sets the callback ID for the request.

        Args:
            callback_id: The callback ID.

        Returns:
            The updated request.
        """
        self._uri_params["callback_id"] = callback_id
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

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict

from signnow.api.webhookv2.request.data.attribute import Attribute
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateEventSubscriptionsSubscriptionV2",
    url="/v2/event-subscriptions/{event_subscription_id}",
    method="put",
    auth="bearer",
    namespace="webhookV2",
    entity="eventSubscription",
    content_type="application/json",
)
class EventSubscriptionPutRequest(RequestInterface):
    """
    Represents a request to update an event subscription.
    """

    def __init__(
        self,
        event: str,
        entity_id: str,
        action: str,
        attributes: Attribute,
    ):
        """
        Constructs a new EventSubscriptionPutRequest.

        Args:
            event: The event for the subscription.
            entity_id: The entity ID for the subscription.
            action: The action for the subscription.
            attributes: The attributes for the subscription.
        """
        self.event = event
        self.entity_id = entity_id
        self.action = action
        self.attributes = attributes
        self._uri_params: Dict[str, str] = {}

    def with_event_subscription_id(
        self, event_subscription_id: str
    ) -> "EventSubscriptionPutRequest":
        """
        Adds the event subscription ID to the URI parameters.

        Args:
            event_subscription_id: The event subscription ID.

        Returns:
            This request.
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

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload for this request.

        Returns:
            A dictionary containing event, entity_id, action, and attributes.
        """
        return {
            "event": self.event,
            "entity_id": self.entity_id,
            "action": self.action,
            "attributes": self.attributes.to_dict(),
        }

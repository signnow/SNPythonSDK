"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.api.webhook.request.data.attribute import Attribute
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateEventSubscription",
    url="/api/v2/events/{event_subscription_id}",
    method="put",
    auth="basic",
    namespace="webhook",
    entity="subscription",
    content_type="application/json",
)
class SubscriptionPutRequest(RequestInterface):
    """
    Represents a SubscriptionPutRequest.
    It is used to update an event subscription.
    """

    def __init__(
        self,
        event: str,
        entity_id: str,
        action: str,
        attributes: Optional[Attribute] = None,
    ):
        """
        Constructs a new SubscriptionPutRequest.

        Args:
            event: The event for the subscription.
            entity_id: The entity id for the subscription.
            action: The action for the subscription.
            attributes: The attributes for the subscription. Optional.
        """
        self.event = event
        self.entity_id = entity_id
        self.action = action
        self.attributes = attributes
        self._uri_params: Dict[str, str] = {}

    def with_event_subscription_id(
        self, event_subscription_id: str
    ) -> "SubscriptionPutRequest":
        """
        Adds the event subscription id to the URI parameters.

        Args:
            event_subscription_id: The event subscription id.

        Returns:
            The updated SubscriptionPutRequest.
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
        Returns a dictionary with the payload for the subscription.

        Returns:
            A dictionary containing event, entity_id, action, and attributes.
        """
        payload: Dict[str, Any] = {
            "event": self.event,
            "entity_id": self.entity_id,
            "action": self.action,
        }
        if self.attributes is not None:
            payload["attributes"] = self.attributes.to_dict()
        return payload

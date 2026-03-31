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
    name="createEventSubscription",
    url="/api/v2/events",
    method="post",
    auth="bearer",
    namespace="webhook",
    entity="subscription",
    content_type="application/json",
)
class SubscriptionPostRequest(RequestInterface):
    """
    Represents a Subscription Post Request.
    """

    def __init__(
        self,
        event: str,
        entity_id: str,
        action: str,
        attributes: Optional[Attribute] = None,
        secret_key: Optional[str] = None,
    ):
        """
        Constructs a new SubscriptionPostRequest.

        Args:
            event: The event for the subscription.
            entity_id: The entity ID for the subscription.
            action: The action for the subscription.
            attributes: The attributes for the subscription. Optional.
            secret_key: The secret key for the subscription. Optional.
        """
        self.event = event
        self.entity_id = entity_id
        self.action = action
        self.attributes = attributes
        self.secret_key = secret_key

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload for the subscription post request.

        Returns:
            A dictionary containing event, entity_id, action, attributes, and secret_key.
        """
        payload: Dict[str, Any] = {
            "event": self.event,
            "entity_id": self.entity_id,
            "action": self.action,
        }
        if self.attributes is not None:
            payload["attributes"] = self.attributes.to_dict()
        if self.secret_key is not None:
            payload["secret_key"] = self.secret_key
        return payload

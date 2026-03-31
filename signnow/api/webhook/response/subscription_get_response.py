"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SubscriptionGetResponse:
    """
    Represents the response from the Subscription Get API.
    """

    data: Optional[List[Dict[str, Any]]] = None
    """
    The data property holds the data of the subscription collection.
    Contains list of subscriptions with: id, event, entity_id, action, json_attributes, created, content.
    """

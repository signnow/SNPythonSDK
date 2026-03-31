"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class CallbacksAllGetResponse:
    """
    Represents the response from getting all callbacks for an event subscription.
    """

    data: List[Dict[str, Any]] = field(default_factory=list)
    """The data of EventSubscriptionDataCallbackCollection."""

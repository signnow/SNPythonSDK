"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RoutingDetailsPostResponse:
    """
    Represents the response of the routing details post request.
    """

    routing_details: Optional[Dict[str, Any]] = None
    """The routing details of the post response."""

    cc: Optional[Dict[str, Any]] = None
    """The cc of the post response."""

    cc_step: Optional[Dict[str, Any]] = None
    """The cc step of the post response."""

    viewers: Optional[Dict[str, Any]] = None
    """The viewers of the post response."""

    approvers: Optional[Dict[str, Any]] = None
    """The approvers of the post response."""

    invite_link_instructions: Optional[Dict[str, Any]] = None
    """The invite link instructions of the post response."""

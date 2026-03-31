"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RoutingDetailsGetResponse:
    """
    Represents the response for getting routing details.
    """

    routing_details: Optional[Dict[str, Any]] = None
    """Collection of routing details."""

    cc: Optional[Dict[str, Any]] = None
    """Collection of CCs."""

    cc_step: Optional[Dict[str, Any]] = None
    """Collection of CC steps."""

    viewers: Optional[Dict[str, Any]] = None
    """Collection of viewers."""

    approvers: Optional[Dict[str, Any]] = None
    """Collection of persons who approve the signing."""

    attributes: Optional[Dict[str, Any]] = None
    """Attributes."""

    invite_link_instructions: Optional[Dict[str, Any]] = None
    """Collection of invite link instructions."""

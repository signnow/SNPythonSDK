"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RoutingDetailsPutResponse:
    """
    Represents the response of the routing details put operation.
    """

    id: Optional[str] = None
    """The unique identifier of the routing details."""

    document_id: Optional[str] = None
    """The unique identifier of the document."""

    data: Optional[Dict[str, Any]] = None
    """The data of the routing details."""

    cc: Optional[Dict[str, Any]] = None
    """The collection of CC put operations."""

    cc_step: Optional[Dict[str, Any]] = None
    """The collection of CC step put operations."""

    viewers: Optional[Dict[str, Any]] = None
    """The collection of viewers."""

    approvers: Optional[Dict[str, Any]] = None
    """The collection of approvers."""

    invite_link_instructions: Optional[Dict[str, Any]] = None
    """The collection of invite link instructions."""

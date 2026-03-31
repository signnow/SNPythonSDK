"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class DocumentGroupGetResponse:
    """
    Represents the response from the Document Group Get API.
    """

    id: Optional[str] = None
    """The unique identifier of the document group."""

    group_name: Optional[str] = None
    """The name of the document group."""

    documents: Optional[Dict[str, Any]] = None
    """The collection of documents in the document group."""

    originator_organization_settings: Optional[Dict[str, Any]] = None
    """The settings of the organization that originated the document group."""

    invite_id: Optional[str] = None
    """The unique identifier of the invite."""

    reminder: Optional[Dict[str, Any]] = None
    """The reminder settings for the document group."""

    order_type: Optional[str] = None
    """The signing order type (at_the_same_time, recipient_order, advanced_order)."""

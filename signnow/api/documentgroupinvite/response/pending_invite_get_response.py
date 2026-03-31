"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PendingInviteGetResponse:
    """
    Represents the response of a pending invite get request.
    """

    document_group_name: Optional[str] = None
    """The name of the document group."""

    invites: Optional[List[Dict[str, Any]]] = None
    """The collection of invites."""

    sign_as_merged: Optional[bool] = None
    """Should be signed as a single document."""

    owner_organization_id: Optional[str] = None
    """The owner organization id."""

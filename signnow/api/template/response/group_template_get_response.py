"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class GroupTemplateGetResponse:
    """
    Represents a group template with various details.
    """

    id: Optional[str] = None
    """The unique ID of the group template."""

    user_id: Optional[str] = None
    """Identifier of the user who owns the document group."""

    group_name: Optional[str] = None
    """Name of the group."""

    folder_id: Optional[str] = None
    """Identifier of the folder containing this document group."""

    routing_details: Optional[Dict[str, Any]] = None
    """Routing details related to this document group."""

    templates: Optional[Dict[str, Any]] = None
    """Templates associated with the document group."""

    shared: Optional[int] = None
    """Indicates whether the document group is shared (1) or not (0)."""

    document_group_template_owner_email: Optional[str] = None
    """Email of the owner who created the document group template."""

    shared_team_id: Optional[str] = None
    """Identifier of the team with which the document group is shared."""

    own_as_merged: Optional[bool] = None
    """Indicates if the document group should be owned as merged."""

    email_action_on_complete: Optional[str] = None
    """Action to be taken via email after the completion of a workflow."""

    created: Optional[int] = None
    """Timestamp when the document group was created (Unix epoch)."""

    updated: Optional[int] = None
    """Timestamp when the document group was last updated (Unix epoch)."""

    recently_used: Optional[int] = None
    """Indicates if the document group was recently used (1 = yes, 0 = no)."""

    pinned: Optional[bool] = None
    """Indicates if the document group is pinned for easy access."""

    share_info: Optional[Dict[str, Any]] = None
    """Information about sharing settings and permissions."""

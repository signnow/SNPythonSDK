"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class FolderGetResponse:
    """
    Represents the response received after a request to get a folder.
    """

    id: Optional[str] = None
    """The unique identifier of the folder."""

    created: Optional[str] = None
    """The timestamp when the folder was created."""

    name: Optional[str] = None
    """The name of the folder."""

    user_id: Optional[str] = None
    """The unique identifier of the user who owns the folder."""

    system_folder: Optional[bool] = None
    """Indicates whether the folder is a system folder."""

    shared: Optional[bool] = None
    """Indicates whether the folder is shared."""

    folders: Optional[Dict[str, Any]] = None
    """The collection of folders within this folder."""

    total_documents: Optional[int] = None
    """The total number of documents in the folder."""

    documents: Optional[Dict[str, Any]] = None
    """The collection of documents within this folder."""

    parent_id: Optional[str] = None
    """The unique identifier of the parent folder."""

    team_name: Optional[str] = None
    """The name of the team that owns the folder."""

    team_id: Optional[str] = None
    """The unique identifier of the team that owns the folder."""

    team_type: Optional[str] = None
    """The type of the team that owns the folder."""

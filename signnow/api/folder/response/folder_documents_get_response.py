"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class FolderDocumentsGetResponse:
    """
    Represents the response from the FolderDocumentsGet API.
    """

    id: Optional[str] = None
    """The unique identifier of the folder."""

    created: Optional[str] = None
    """The creation date of the folder."""

    name: Optional[str] = None
    """The name of the folder."""

    user_id: Optional[str] = None
    """The unique identifier of the user who owns the folder."""

    system_folder: Optional[bool] = None
    """A flag indicating whether the folder is a system folder."""

    shared: Optional[bool] = None
    """A flag indicating whether the folder is shared."""

    folders: Optional[Dict[str, Any]] = None
    """The collection of folders within the folder."""

    total_documents: Optional[int] = None
    """The total number of documents in the folder."""

    documents: Optional[Dict[str, Any]] = None
    """The collection of documents in the folder."""

    parent_id: Optional[str] = None
    """The unique identifier of the parent folder."""

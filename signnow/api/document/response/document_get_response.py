"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DocumentGetResponse:
    """
    This class represents the response of a document retrieval request.
    It contains all the details of the document.
    """

    id: Optional[str] = None
    user_id: Optional[str] = None
    document_name: Optional[str] = None
    page_count: Optional[str] = None
    created: int = 0
    updated: int = 0
    original_filename: Optional[str] = None
    owner: Optional[str] = None
    owner_name: Optional[str] = None
    template: bool = False
    parent_id: Optional[str] = None
    originator_logo: Optional[str] = None
    version_time: int = 0
    origin_user_id: Optional[str] = None
    origin_document_id: Optional[str] = None
    recently_used: Optional[str] = None
    default_folder: Optional[str] = None

    # Complex nested objects - simplified for now
    pages: Optional[List[Dict[str, Any]]] = None
    routing_details: Optional[List[Dict[str, Any]]] = None
    thumbnail: Optional[Dict[str, Any]] = None
    signatures: Optional[List[Dict[str, Any]]] = None
    tags: Optional[List[Dict[str, Any]]] = None
    fields: Optional[List[Dict[str, Any]]] = None
    roles: Optional[List[Dict[str, Any]]] = None
    viewer_roles: Optional[List[Dict[str, Any]]] = None
    settings: Optional[Dict[str, Any]] = None
    share_info: Optional[Dict[str, Any]] = None
    field_invites: Optional[List[Dict[str, Any]]] = None

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class DocumentGroupTemplatePostResponse:
    """
    Represents the response received after a document group template post request.
    """

    data: Optional[Dict[str, Any]] = None
    """
    The data associated with the document group template post response.
    Contains: unique_id, name, created, state, owner_email, documents, owner, invite_id, last_invite_id.
    """

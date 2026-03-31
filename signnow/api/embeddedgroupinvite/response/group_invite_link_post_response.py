"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class GroupInviteLinkPostResponse:
    """
    Represents the response from the Group Invite Link Post API.
    """

    data: Optional[Dict[str, Any]] = None
    """The response data from the Group Invite Link Post API."""

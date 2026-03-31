"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class GroupInvitePostResponse:
    """
    Represents the response of a group invite post request.
    """

    id: Optional[str] = None
    """The id of the group invite post response."""

    pending_invite_link: Optional[str] = None
    """The pending invite link of the group invite post response."""

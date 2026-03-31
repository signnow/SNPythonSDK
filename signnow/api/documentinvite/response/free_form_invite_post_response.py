"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FreeFormInvitePostResponse:
    """
    This class represents the response from a FreeFormInvite post request.
    """

    result: Optional[str] = None
    id: Optional[str] = None
    callback_url: Optional[str] = None

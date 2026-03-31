"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenPostResponse:
    """
    This class represents the response received after a token post request.
    """

    expires_in: int = 0
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    scope: Optional[str] = None
    last_login: int = 0

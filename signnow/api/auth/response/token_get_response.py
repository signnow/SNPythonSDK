"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenGetResponse:
    """
    This class represents the response received after a token get request.
    """

    access_token: Optional[str] = None
    token_type: Optional[str] = None
    scope: Optional[str] = None
    expires_in: int = 0

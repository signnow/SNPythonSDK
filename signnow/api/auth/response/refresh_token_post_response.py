"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class RefreshTokenPostResponse:
    """
    Represents the response received after refreshing the token.
    """

    expires_in: int = 0
    """The time in seconds when the token expires."""

    token_type: str = ""
    """The type of the token."""

    access_token: str = ""
    """The access token."""

    refresh_token: str = ""
    """The refresh token."""

    scope: str = ""
    """The scope of the token."""

    last_login: int = 0
    """The last login time in seconds."""

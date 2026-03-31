"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Optional


class TokenInterface:
    """Interface for token classes."""

    def type(self) -> str:
        """Returns the type of the token."""
        raise NotImplementedError

    def token(self) -> str:
        """Returns the token string."""
        raise NotImplementedError


class BasicToken(TokenInterface):
    """
    This class represents a basic token implementation.
    """

    def __init__(self, token: str):
        """
        Constructs a new BasicToken with the specified token string.

        Args:
            token: The token string
        """
        self._token = token

    def type(self) -> str:
        """Returns the type of the token. In this case, it is always 'Basic'."""
        return "Basic"

    def token(self) -> str:
        """Returns the token string."""
        return self._token

    def __str__(self) -> str:
        """Returns the string representation of the token."""
        return self.token()


class BearerToken(TokenInterface):
    """
    This class represents a Bearer token.
    """

    def __init__(
        self,
        access_token: str,
        refresh_token: Optional[str] = None,
        expires: int = 0,
    ):
        """
        Constructs a new BearerToken.

        Args:
            access_token: The access token string
            refresh_token: The refresh token string (optional)
            expires: The expiration time in seconds (optional)
        """
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._expires = expires

    def type(self) -> str:
        """Returns the type of the token. In this case, it is always 'Bearer'."""
        return "Bearer"

    def token(self) -> str:
        """Returns the access token."""
        return self._access_token

    def refresh_token(self) -> Optional[str]:
        """Returns the refresh token."""
        return self._refresh_token

    def expires(self) -> int:
        """Returns the expiration time in seconds."""
        return self._expires

    def is_empty(self) -> bool:
        """Checks if the access token is empty."""
        return not self.token() or len(self.token()) == 0

    def __str__(self) -> str:
        """Returns the string representation of the access token."""
        return self.token()

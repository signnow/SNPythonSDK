"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class UserPostResponse:
    """
    Represents the response from a User POST request.
    """

    id: str = ""
    """The unique identifier of the user."""

    verified: int = 0
    """The verification status of the user."""

    email: str = ""
    """The email address of the user."""

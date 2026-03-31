"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class UserPutResponse:
    """
    Represents the response from a PUT request to the User API.
    """

    id: str = ""
    """The unique identifier for the user."""

    first_name: str = ""
    """The first name of the user."""

    last_name: str = ""
    """The last name of the user."""

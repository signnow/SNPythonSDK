"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class EmailVerifyPutResponse:
    """
    Represents the response from the Email verification API.
    """

    email: str = ""
    """The email address that was verified."""

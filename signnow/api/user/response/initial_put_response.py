"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class InitialPutResponse:
    """
    Represents the initial put response.
    """

    id: str = ""
    """The id of the response."""

    width: str = ""
    """The width of the response."""

    height: str = ""
    """The height of the response."""

    created: str = ""
    """The creation time of the response."""

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class TemplatePostResponse:
    """
    Represents the response from a POST request to a Template API.
    """

    id: str
    """The unique identifier of the template."""

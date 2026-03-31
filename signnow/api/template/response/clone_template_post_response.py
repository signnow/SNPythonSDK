"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class CloneTemplatePostResponse:
    """
    Represents the response received after cloning a template.
    """

    id: str
    """The unique identifier of the cloned template."""

    name: str
    """The name of the cloned template."""

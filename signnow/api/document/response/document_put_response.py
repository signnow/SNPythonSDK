"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class DocumentPutResponse:
    """
    Represents the response from the Document PUT API.
    """

    id: str = ""
    """The ID of the document."""

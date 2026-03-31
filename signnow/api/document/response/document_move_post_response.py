"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DocumentMovePostResponse:
    """
    This class represents the response from the Document Move POST API.
    """

    id: Optional[str] = None
    status: Optional[str] = None

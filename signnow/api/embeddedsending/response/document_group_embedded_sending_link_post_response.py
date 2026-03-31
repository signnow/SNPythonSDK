"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class DocumentGroupEmbeddedSendingLinkPostResponse:
    """
    Represents the response for the Document Group Embedded Sending Link Post request.
    """

    data: Optional[Dict[str, Any]] = None
    """The data URL associated with the response."""

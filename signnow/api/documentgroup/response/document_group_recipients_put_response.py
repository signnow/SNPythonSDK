"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class DocumentGroupRecipientsPutResponse:
    """
    Represents the response for putting document group recipients.
    """

    data: Optional[Dict[str, Any]] = None
    """The data associated with the document group recipients."""

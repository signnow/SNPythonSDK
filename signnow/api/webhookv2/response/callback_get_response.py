"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class CallbackGetResponse:
    """
    Represents the response from the Callback API.
    """

    data: Optional[Dict[str, Any]] = None
    """The data property stores the callback data from the API response."""

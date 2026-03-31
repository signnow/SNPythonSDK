"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FreeFormInviteGetResponse:
    """
    This class represents the response from a FreeFormInviteGet API call.
    """

    meta: Optional[Dict[str, Any]] = None
    data: Optional[List[Dict[str, Any]]] = None

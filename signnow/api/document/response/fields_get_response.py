"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FieldsGetResponse:
    """
    This class represents the response from the Fields GET API.
    """

    # Fields collection - simplified structure
    fields: Optional[List[Dict[str, Any]]] = None
    document_id: Optional[str] = None

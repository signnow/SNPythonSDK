"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FieldExtractPostResponse:
    """
    This class represents the response from the Field Extract POST API.
    """

    id: Optional[str] = None
    fields: Optional[List[Dict[str, Any]]] = None
    extracted_data: Optional[Dict[str, Any]] = None

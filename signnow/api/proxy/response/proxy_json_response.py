"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ProxyJsonResponse:
    """
    This class represents the response received after a request to proxy any unimplemented endpoint
    that returns JSON data.
    """

    raw_json: Dict[str, Any]
    """The raw JSON content returned from the proxied endpoint."""

    def get_raw_json(self) -> Dict[str, Any]:
        """
        Returns the raw JSON content returned from the proxied endpoint.

        Returns:
            The raw JSON content as a dictionary
        """
        return self.raw_json

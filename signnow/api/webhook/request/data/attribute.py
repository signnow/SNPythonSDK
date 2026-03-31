"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class Attribute:
    """
    Represents the attributes of a webhook request.
    """

    callback: str
    """The callback URL for the webhook."""

    use_tls_12: bool = False
    """Flag to indicate if TLS 1.2 should be used."""

    integration_id: Optional[str] = None
    """The ID of the integration."""

    docid_queryparam: bool = False
    """Flag to indicate if document ID should be included in the query parameters."""

    headers: Dict[str, Any] = field(default_factory=dict)
    """The headers for the webhook request."""

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Attribute object to a dictionary.

        Returns:
            A dictionary representation of the Attribute object.
        """
        result: Dict[str, Any] = {
            "callback": self.callback,
            "use_tls_12": self.use_tls_12,
            "docid_queryparam": self.docid_queryparam,
            "headers": self.headers,
        }
        if self.integration_id is not None:
            result["integration_id"] = self.integration_id
        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Attribute":
        """
        Creates an Attribute object from a dictionary.

        Args:
            data: The dictionary to convert to an Attribute object.

        Returns:
            The created Attribute object.
        """
        return cls(
            callback=data.get("callback", ""),
            use_tls_12=data.get("use_tls_12", False),
            integration_id=data.get("integration_id"),
            docid_queryparam=data.get("docid_queryparam", False),
            headers=data.get("headers", {}),
        )

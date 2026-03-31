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

    delete_access_token: bool = False
    """Flag to indicate if the access token should be deleted."""

    use_tls_12: bool = False
    """Flag to indicate if TLS 1.2 should be used."""

    integration_id: Optional[str] = None
    """The integration ID for the webhook."""

    docid_queryparam: bool = False
    """Flag to indicate if the document ID should be included in the query parameters."""

    headers: Dict[str, Any] = field(default_factory=dict)
    """The headers for the webhook request."""

    include_metadata: bool = False
    """Flag to indicate if metadata should be included in the webhook request."""

    secret_key: Optional[str] = None
    """The secret key for the webhook."""

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Attribute object to a dictionary.

        Returns:
            A dictionary representation of the Attribute object.
        """
        result: Dict[str, Any] = {
            "callback": self.callback,
            "delete_access_token": self.delete_access_token,
            "use_tls_12": self.use_tls_12,
            "docid_queryparam": self.docid_queryparam,
            "headers": self.headers,
            "include_metadata": self.include_metadata,
        }
        if self.integration_id is not None:
            result["integration_id"] = self.integration_id
        if self.secret_key is not None:
            result["secret_key"] = self.secret_key
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
            delete_access_token=data.get("delete_access_token", False),
            use_tls_12=data.get("use_tls_12", False),
            integration_id=data.get("integration_id"),
            docid_queryparam=data.get("docid_queryparam", False),
            headers=data.get("headers", {}),
            include_metadata=data.get("include_metadata", False),
            secret_key=data.get("secret_key"),
        )

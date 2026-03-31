"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createEmbeddedInvite",
    url="/v2/documents/{document_id}/embedded-invites",
    method="post",
    auth="bearer",
    namespace="embeddedInvite",
    entity="documentInvite",
    content_type="application/json",
)
class DocumentInvitePostRequest(RequestInterface):
    """
    Represents a request to create an embedded invite.
    """

    def __init__(
        self,
        invites: List[Dict[str, Any]],
        name_formula: Optional[str] = None,
    ):
        """
        Constructs a new DocumentInvitePostRequest.

        Args:
            invites: The collection of invites.
            name_formula: The formula for the name. Optional.
        """
        self.invites = invites
        self.name_formula = name_formula
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentInvitePostRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The document ID.

        Returns:
            The updated DocumentInvitePostRequest.
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Any]:
        """
        Returns the payload for the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Any] = {
            "invites": self.invites,
        }
        if self.name_formula is not None:
            payload["name_formula"] = self.name_formula
        return payload

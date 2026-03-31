"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="deleteEmbeddedInvite",
    url="/v2/documents/{document_id}/embedded-invites",
    method="delete",
    auth="bearer",
    namespace="embeddedInvite",
    entity="documentInvite",
    content_type="application/json",
)
class DocumentInviteDeleteRequest(RequestInterface):
    """
    Represents a request to delete a document invite.
    """

    def __init__(self):
        """Constructs a new DocumentInviteDeleteRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentInviteDeleteRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The ID of the document to be deleted.

        Returns:
            This request object with the updated URI parameters.
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

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

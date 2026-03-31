"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentFreeFormInvites",
    url="/v2/documents/{document_id}/free-form-invites",
    method="get",
    auth="bearer",
    namespace="documentInvite",
    entity="freeFormInvite",
    content_type="application/json",
)
class FreeFormInviteGetRequest(RequestInterface):
    """
    This class represents a request to get free form invites for a document.
    """

    def __init__(self):
        """Constructs a new FreeFormInviteGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "FreeFormInviteGetRequest":
        """
        Sets the document ID for the request.

        Args:
            document_id: The ID of the document

        Returns:
            The current FreeFormInviteGetRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Gets the URI parameters for the request.

        Returns:
            The dict of URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Gets the payload for the request.

        Returns:
            An empty dict as the payload
        """
        return {}

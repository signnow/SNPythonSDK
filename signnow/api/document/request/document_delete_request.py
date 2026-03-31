"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="deleteDocument",
    url="/document/{document_id}",
    method="delete",
    auth="bearer",
    namespace="document",
    entity="document",
    content_type="application/json",
)
class DocumentDeleteRequest(RequestInterface):
    """
    This class represents a request to delete a document.
    """

    def __init__(self):
        """Constructs a new DocumentDeleteRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentDeleteRequest":
        """
        Method to add a document ID to the URI parameters.

        Args:
            document_id: The ID of the document to be deleted

        Returns:
            The current DocumentDeleteRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Method to get the URI parameters for the request.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Method to get the payload for the request.

        Returns:
            An empty dict. As this is a delete request, the payload is empty
        """
        return {}

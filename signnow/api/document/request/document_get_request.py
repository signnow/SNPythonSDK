"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocument",
    url="/document/{document_id}",
    method="get",
    auth="bearer",
    namespace="document",
    entity="document",
    content_type="application/json",
)
class DocumentGetRequest(RequestInterface):
    """
    This class represents a request to get a document.
    """

    def __init__(self):
        """Constructs a new DocumentGetRequest."""
        self._uri_params: Dict[str, str] = {}
        self._query_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentGetRequest":
        """
        Method to add a document ID to the URI parameters.

        Args:
            document_id: The ID of the document to be retrieved

        Returns:
            The current DocumentGetRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def with_include(self, include: str) -> "DocumentGetRequest":
        """
        Add an include query parameter to the request.

        Args:
            include: The include value (e.g. "field_invites")

        Returns:
            The current DocumentGetRequest instance
        """
        self._query_params["include"] = include
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
            An empty dict. As this is a GET request, the payload is empty
        """
        return {}

    def query_params(self) -> Optional[Dict[str, str]]:
        """
        Returns the query parameters for the request.

        Returns:
            A dict containing the query parameters, or None
        """
        return self._query_params if self._query_params else None

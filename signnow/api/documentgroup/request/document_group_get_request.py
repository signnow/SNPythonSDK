"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentGroup",
    url="/documentgroup/{document_group_id}",
    method="get",
    auth="bearer",
    namespace="documentGroup",
    entity="documentGroup",
    content_type="application/json",
)
class DocumentGroupGetRequest(RequestInterface):
    """
    Represents the API endpoint for getting a document group.
    """

    def __init__(self):
        """Constructs a new DocumentGroupGetRequest."""
        self._uri_params: Dict[str, str] = {}
        self._query_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupGetRequest":
        """
        Adds the document group ID to the URI parameters.

        Args:
            document_group_id: The ID of the document group.

        Returns:
            The current instance of DocumentGroupGetRequest.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def with_include(self, include: str) -> "DocumentGroupGetRequest":
        """
        Add an include query parameter to the request.

        Args:
            include: The include value (e.g. "reminder")

        Returns:
            The current instance of DocumentGroupGetRequest.
        """
        self._query_params["include"] = include
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

    def query_params(self) -> Optional[Dict[str, str]]:
        """
        Returns the query parameters for the request.

        Returns:
            A dict containing the query parameters, or None.
        """
        return self._query_params if self._query_params else None

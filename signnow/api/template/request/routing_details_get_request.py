"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getRoutingDetails",
    url="/document/{document_id}/template/routing/detail",
    method="get",
    auth="bearer",
    namespace="template",
    entity="routingDetails",
    content_type="application/json",
)
class RoutingDetailsGetRequest(RequestInterface):
    """
    Represents a request to get routing details.
    """

    def __init__(self):
        """Constructs a new RoutingDetailsGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "RoutingDetailsGetRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The ID of the document.

        Returns:
            The current instance of the request.
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
        Returns an empty payload.

        Returns:
            An empty dictionary.
        """
        return {}

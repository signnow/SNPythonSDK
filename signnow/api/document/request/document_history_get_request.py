"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentHistoryFull",
    url="/document/{document_id}/historyfull",
    method="get",
    auth="bearer",
    namespace="document",
    entity="documentHistory",
    content_type="application/json",
)
class DocumentHistoryGetRequest(RequestInterface):
    """
    This class represents a request to get the full history of a document.
    """

    def __init__(self):
        """Constructs a new DocumentHistoryGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentHistoryGetRequest":
        """
        Method to add a document ID to the URI parameters.

        Args:
            document_id: The ID of the document

        Returns:
            The current DocumentHistoryGetRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Method to get a copy of the URI parameters.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Method to get the payload of the request.

        Returns:
            An empty dict. In this case, it's empty as there's no payload for this request
        """
        return {}

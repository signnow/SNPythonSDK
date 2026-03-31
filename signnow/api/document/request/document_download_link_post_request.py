"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentDownloadLink",
    url="/document/{document_id}/download/link",
    method="post",
    auth="bearer",
    namespace="document",
    entity="documentDownloadLink",
    content_type="application/json",
)
class DocumentDownloadLinkPostRequest(RequestInterface):
    """
    Represents a request to create a document download link.
    """

    def __init__(self):
        """Initializes a new DocumentDownloadLinkPostRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentDownloadLinkPostRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The ID of the document.

        Returns:
            This request object with the added document ID.
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

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="downloadDocument",
    url="/document/{document_id}/download",
    method="get",
    auth="bearer",
    namespace="document",
    entity="documentDownload",
    content_type="application/pdf",
)
class DocumentDownloadGetRequest(RequestInterface):
    """
    This class represents a request to download a document.
    """

    def __init__(self):
        """Constructs a new DocumentDownloadGetRequest."""
        self._uri_params: Dict[str, str] = {}
        self._query_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentDownloadGetRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The ID of the document to download

        Returns:
            The current DocumentDownloadGetRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def with_type(self, type: str) -> "DocumentDownloadGetRequest":
        """
        Specifies file type to download: collapsed|zip|email

        Args:
            type: The type of file to download

        Returns:
            The current DocumentDownloadGetRequest instance
        """
        self._query_params["type"] = type
        return self

    def with_history(self, with_history: str) -> "DocumentDownloadGetRequest":
        """
        The value "yes" allows to include a table containing the document's history into a document.

        Args:
            with_history: "yes" to include history, otherwise omit

        Returns:
            The current DocumentDownloadGetRequest instance
        """
        self._query_params["with_history"] = with_history
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def query_params(self) -> Optional[Dict[str, str]]:
        """
        Returns the query parameters for the request.

        Returns:
            A dict containing the query parameters
        """
        return dict(self._query_params) if self._query_params else None

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dict as this is a GET request.

        Returns:
            An empty dict
        """
        return {}

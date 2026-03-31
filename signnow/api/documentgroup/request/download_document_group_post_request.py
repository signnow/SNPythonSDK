"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="downloadDocumentGroup",
    url="/documentgroup/{document_group_id}/downloadall",
    method="post",
    auth="bearer",
    namespace="documentGroup",
    entity="downloadDocumentGroup",
    content_type="application/json",
)
class DownloadDocumentGroupPostRequest(RequestInterface):
    """
    Represents a request to download a document group.
    """

    def __init__(
        self,
        type: Optional[str] = None,
        with_history: Optional[str] = None,
        document_order: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Constructs a new DownloadDocumentGroupPostRequest.

        Args:
            type: The download type (e.g. "zip", "collapsed"). Optional.
            with_history: The history of the document group. Optional.
            document_order: The order of the documents in the group. Optional.
        """
        self._type = type
        self.with_history = with_history
        self.document_order = document_order or []
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DownloadDocumentGroupPostRequest":
        """
        Adds the specified document group ID to the URI parameters.

        Args:
            document_group_id: The ID of the document group.

        Returns:
            This request, for chaining.
        """
        self._uri_params["document_group_id"] = document_group_id
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
        Returns a dictionary containing the payload of the request.

        Returns:
            A dictionary containing type, with_history, and document_order.
        """
        payload: Dict[str, Any] = {}
        if self._type is not None:
            payload["type"] = self._type
        if self.with_history is not None:
            payload["with_history"] = self.with_history
        if self.document_order:
            payload["document_order"] = self.document_order
        return payload

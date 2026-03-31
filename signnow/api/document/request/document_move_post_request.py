"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="moveDocument",
    url="/document/{document_id}/move",
    method="post",
    auth="bearer",
    namespace="document",
    entity="documentMove",
    content_type="application/json",
)
class DocumentMovePostRequest(RequestInterface):
    """
    This class represents a request to move a document to a different folder.
    """

    def __init__(self, folder_id: str):
        """
        Constructs a new DocumentMovePostRequest with the specified folder ID.

        Args:
            folder_id: The ID of the folder where the document will be moved
        """
        self._folder_id = folder_id
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentMovePostRequest":
        """
        Adds the document ID to the URI parameters and returns this request.

        Args:
            document_id: The ID of the document to be moved

        Returns:
            The current DocumentMovePostRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for this request.

        Returns:
            A dict of the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns the payload for this request.

        Returns:
            A dict of the payload
        """
        return {"folder_id": self._folder_id}

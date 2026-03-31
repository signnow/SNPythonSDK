"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="deleteDocumentGroup",
    url="/documentgroup/{document_group_id}",
    method="delete",
    auth="bearer",
    namespace="documentGroup",
    entity="documentGroup",
    content_type="application/json",
)
class DocumentGroupDeleteRequest(RequestInterface):
    """
    Represents a request to delete a document group.
    """

    def __init__(self):
        """Constructs a new DocumentGroupDeleteRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupDeleteRequest":
        """
        Adds the document group id to the URI parameters.

        Args:
            document_group_id: The id of the document group to be deleted.

        Returns:
            The current instance of DocumentGroupDeleteRequest.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

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

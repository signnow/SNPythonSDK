"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentGroup",
    url="/documentgroup",
    method="post",
    auth="bearer",
    namespace="documentGroup",
    entity="documentGroup",
    content_type="application/json",
)
class DocumentGroupPostRequest(RequestInterface):
    """
    Represents a request to create a document group.
    """

    def __init__(self, document_ids: List[str], group_name: str):
        """
        Constructs a new DocumentGroupPostRequest.

        Args:
            document_ids: List of document IDs to be included in the group.
            group_name: Name of the document group.
        """
        self.document_ids = document_ids
        self.group_name = group_name

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload for the request.

        Returns:
            A dictionary containing document_ids and group_name.
        """
        return {
            "document_ids": self.document_ids,
            "group_name": self.group_name,
        }

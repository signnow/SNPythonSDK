"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentGroupRecipients",
    url="/v2/document-groups/{document_group_id}/recipients",
    method="get",
    auth="bearer",
    namespace="documentGroup",
    entity="documentGroupRecipients",
    content_type="application/json",
)
class DocumentGroupRecipientsGetRequest(RequestInterface):
    """
    Represents a request to get the recipients of a document group.
    """

    def __init__(self):
        """Constructs a new DocumentGroupRecipientsGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupRecipientsGetRequest":
        """
        Sets the document group id in the URI parameters.

        Args:
            document_group_id: The id of the document group.

        Returns:
            The current instance of DocumentGroupRecipientsGetRequest.
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

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

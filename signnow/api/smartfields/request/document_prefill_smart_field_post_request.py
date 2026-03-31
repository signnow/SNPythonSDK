"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict

from signnow.api.smartfields.request.data.data_collection import DataCollection
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="prefillSmartFields",
    url="/document/{document_id}/integration/object/smartfields",
    method="post",
    auth="bearer",
    namespace="smartFields",
    entity="documentPrefillSmartField",
    content_type="application/json",
)
class DocumentPrefillSmartFieldPostRequest(RequestInterface):
    """
    Represents a request to prefill smart fields in a document.
    """

    def __init__(self, data: DataCollection, client_timestamp: str):
        """
        Constructs a new DocumentPrefillSmartFieldPostRequest.

        Args:
            data: The data collection to be sent in the request.
            client_timestamp: The client timestamp to be sent in the request.
        """
        self.data = data
        self.client_timestamp = client_timestamp
        self._uri_params: Dict[str, str] = {}

    def with_document_id(
        self, document_id: str
    ) -> "DocumentPrefillSmartFieldPostRequest":
        """
        Adds the specified document ID to the URI parameters.

        Args:
            document_id: The document ID to be added.

        Returns:
            This request with the added document ID.
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

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload of this request.

        Returns:
            A dictionary containing data and client_timestamp.
        """
        return {
            "data": self.data.to_list(),
            "client_timestamp": self.client_timestamp,
        }

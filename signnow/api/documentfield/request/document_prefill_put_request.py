"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict

from signnow.api.documentfield.request.data.field_collection import FieldCollection
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="prefillTextFields",
    url="/v2/documents/{document_id}/prefill-texts",
    method="put",
    auth="bearer",
    namespace="documentField",
    entity="documentPrefill",
    content_type="application/json",
)
class DocumentPrefillPutRequest(RequestInterface):
    """
    Represents the API endpoint for prefilling text fields in a document.
    """

    def __init__(self, fields: FieldCollection):
        """
        Constructor for DocumentPrefillPutRequest.

        Args:
            fields: Collection of fields to be prefilled in the document.
        """
        self.fields = fields
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentPrefillPutRequest":
        """
        Method to add document ID to the URI parameters.

        Args:
            document_id: ID of the document.

        Returns:
            DocumentPrefillPutRequest object with updated URI parameters.
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Method to get URI parameters.

        Returns:
            Dictionary of URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Any]:
        """
        Method to get payload for the request.

        Returns:
            Dictionary of payload parameters.
        """
        return {
            "fields": self.fields.to_list(),
        }

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.api.document.request.data.field_collection import FieldCollection
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateDocument",
    url="/document/{document_id}",
    method="put",
    auth="bearer",
    namespace="document",
    entity="document",
    content_type="application/json",
)
class DocumentPutRequest(RequestInterface):
    """
    Represents a request to update a document.
    """

    def __init__(
        self,
        fields: Optional[FieldCollection] = None,
        lines: Optional[Any] = None,
        checks: Optional[Any] = None,
        radiobuttons: Optional[Any] = None,
        signatures: Optional[Any] = None,
        texts: Optional[Any] = None,
        attachments: Optional[Any] = None,
        hyperlinks: Optional[Any] = None,
        integration_objects: Optional[Any] = None,
        deactivate_elements: Optional[Any] = None,
        document_name: Optional[str] = None,
        client_timestamp: Optional[str] = None,
    ):
        """
        Constructs a new DocumentPutRequest.

        Args:
            fields: Collection of fields in the document. Optional.
            lines: Collection of lines in the document. Optional.
            checks: Collection of checks in the document. Optional.
            radiobuttons: Collection of radio buttons in the document. Optional.
            signatures: Collection of signatures in the document. Optional.
            texts: Collection of texts in the document. Optional.
            attachments: Collection of attachments in the document. Optional.
            hyperlinks: Collection of hyperlinks in the document. Optional.
            integration_objects: Collection of integration objects in the document. Optional.
            deactivate_elements: Collection of elements to be deactivated in the document. Optional.
            document_name: Name of the document. Optional.
            client_timestamp: Client timestamp. Optional.
        """
        self.fields = fields
        self.lines = lines
        self.checks = checks
        self.radiobuttons = radiobuttons
        self.signatures = signatures
        self.texts = texts
        self.attachments = attachments
        self.hyperlinks = hyperlinks
        self.integration_objects = integration_objects
        self.deactivate_elements = deactivate_elements
        self.document_name = document_name
        self.client_timestamp = client_timestamp
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentPutRequest":
        """
        Sets the document ID for the request.

        Args:
            document_id: The document ID.

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
        Returns a dictionary with the payload for the request.

        Returns:
            A dictionary containing all document update parameters.
        """
        payload: Dict[str, Any] = {}
        if self.fields is not None:
            payload["fields"] = self.fields.to_list()
        if self.lines is not None:
            payload["lines"] = self.lines
        if self.checks is not None:
            payload["checks"] = self.checks
        if self.radiobuttons is not None:
            payload["radiobuttons"] = self.radiobuttons
        if self.signatures is not None:
            payload["signatures"] = self.signatures
        if self.texts is not None:
            payload["texts"] = self.texts
        if self.attachments is not None:
            payload["attachments"] = self.attachments
        if self.hyperlinks is not None:
            payload["hyperlinks"] = self.hyperlinks
        if self.integration_objects is not None:
            payload["integration_objects"] = self.integration_objects
        if self.deactivate_elements is not None:
            payload["deactivate_elements"] = self.deactivate_elements
        if self.document_name is not None:
            payload["document_name"] = self.document_name
        if self.client_timestamp is not None:
            payload["client_timestamp"] = self.client_timestamp
        return payload

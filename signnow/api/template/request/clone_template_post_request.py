"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentWithTemplate",
    url="/template/{template_id}/copy",
    method="post",
    auth="bearer",
    namespace="template",
    entity="cloneTemplate",
    content_type="application/json",
)
class CloneTemplatePostRequest(RequestInterface):
    """
    Represents a request to clone a template.
    """

    def __init__(
        self,
        document_name: Optional[str] = None,
        client_timestamp: Optional[str] = None,
        folder_id: Optional[str] = None,
    ):
        """
        Constructs a new CloneTemplatePostRequest.

        Args:
            document_name: The name of the document. Optional.
            client_timestamp: The client timestamp. Optional.
            folder_id: The ID of the folder. Optional.
        """
        self.document_name = document_name
        self.client_timestamp = client_timestamp
        self.folder_id = folder_id
        self._uri_params: Dict[str, str] = {}

    def with_template_id(self, template_id: str) -> "CloneTemplatePostRequest":
        """
        Adds the template ID to the URI parameters.

        Args:
            template_id: The ID of the template.

        Returns:
            This CloneTemplatePostRequest instance.
        """
        self._uri_params["template_id"] = template_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Optional[str]]:
        """
        Returns the payload for the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Optional[str]] = {}
        if self.document_name is not None:
            payload["document_name"] = self.document_name
        if self.client_timestamp is not None:
            payload["client_timestamp"] = self.client_timestamp
        if self.folder_id is not None:
            payload["folder_id"] = self.folder_id
        return payload

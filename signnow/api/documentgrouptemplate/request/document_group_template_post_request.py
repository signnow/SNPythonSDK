"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentGroupFromTemplate",
    url="/v2/document-group-templates/{template_group_id}/document-group",
    method="post",
    auth="bearer",
    namespace="documentGroupTemplate",
    entity="documentGroupTemplate",
    content_type="application/json",
)
class DocumentGroupTemplatePostRequest(RequestInterface):
    """
    Represents a request to create a document group from a template.
    """

    def __init__(
        self,
        group_name: str,
        client_timestamp: str,
        folder_id: Optional[str] = None,
    ):
        """
        Constructs a new DocumentGroupTemplatePostRequest.

        Args:
            group_name: The name of the group.
            client_timestamp: The client timestamp.
            folder_id: The folder ID. Optional.
        """
        self.group_name = group_name
        self.client_timestamp = client_timestamp
        self.folder_id = folder_id
        self._uri_params: Dict[str, str] = {}

    def with_template_group_id(
        self, template_group_id: str
    ) -> "DocumentGroupTemplatePostRequest":
        """
        Sets the template group ID in the URI parameters.

        Args:
            template_group_id: The template group ID.

        Returns:
            The current instance of DocumentGroupTemplatePostRequest.
        """
        self._uri_params["template_group_id"] = template_group_id
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
        Returns a dictionary with the payload of the request.

        Returns:
            A dictionary containing group_name, client_timestamp, and folder_id.
        """
        payload: Dict[str, Any] = {
            "group_name": self.group_name,
            "client_timestamp": self.client_timestamp,
        }
        if self.folder_id is not None:
            payload["folder_id"] = self.folder_id
        return payload

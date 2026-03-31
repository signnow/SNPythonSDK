"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateDocumentGroupTemplate",
    url="/documentgroup/template/{template_id}",
    method="put",
    auth="bearer",
    namespace="template",
    entity="groupTemplate",
    content_type="application/json",
)
class GroupTemplatePutRequest(RequestInterface):
    """
    Represents a request to update a group template.
    """

    def __init__(
        self,
        routing_details: Optional[Dict[str, Any]] = None,
        template_group_name: Optional[str] = None,
        template_ids_to_add: Optional[List[str]] = None,
        template_ids_to_remove: Optional[List[str]] = None,
    ):
        """
        Constructs a new GroupTemplatePutRequest.

        Args:
            routing_details: The routing details. Optional.
            template_group_name: The template group name. Optional.
            template_ids_to_add: The template IDs to add. Optional.
            template_ids_to_remove: The template IDs to remove. Optional.
        """
        self.routing_details = routing_details
        self.template_group_name = template_group_name
        self.template_ids_to_add = template_ids_to_add or []
        self.template_ids_to_remove = template_ids_to_remove or []
        self._uri_params: Dict[str, str] = {}

    def with_template_id(self, template_id: str) -> "GroupTemplatePutRequest":
        """
        Adds a template ID to the URI parameters.

        Args:
            template_id: The template ID to add.

        Returns:
            This request.
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

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary containing the payload for the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Any] = {}
        if self.template_ids_to_add:
            payload["template_ids_to_add"] = self.template_ids_to_add
        if self.template_ids_to_remove:
            payload["template_ids_to_remove"] = self.template_ids_to_remove
        if self.routing_details is not None:
            payload["routing_details"] = self.routing_details
        if self.template_group_name is not None:
            payload["template_group_name"] = self.template_group_name
        return payload

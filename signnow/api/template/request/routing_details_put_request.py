"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateRoutingDetails",
    url="/document/{document_id}/template/routing/detail",
    method="put",
    auth="bearer",
    namespace="template",
    entity="routingDetails",
    content_type="application/json",
)
class RoutingDetailsPutRequest(RequestInterface):
    """
    Represents a request to update routing details.
    """

    def __init__(
        self,
        template_data: Optional[Dict[str, Any]] = None,
        template_data_object: Optional[list] = None,
        cc: Optional[list] = None,
        cc_step: Optional[list] = None,
        viewers: Optional[list] = None,
        approvers: Optional[list] = None,
        invite_link_instructions: Optional[list] = None,
    ):
        """
        Constructs a new RoutingDetailsPutRequest.

        Args:
            template_data: The template data for the request. Optional.
            template_data_object: The collection of template data objects. Optional.
            cc: The collection of CCs. Optional.
            cc_step: The collection of CC steps. Optional.
            viewers: The collection of viewers. Optional.
            approvers: The collection of approvers. Optional.
            invite_link_instructions: The collection of invite link instructions. Optional.
        """
        self.template_data = template_data
        self.template_data_object = template_data_object or []
        self.cc = cc or []
        self.cc_step = cc_step or []
        self.viewers = viewers or []
        self.approvers = approvers or []
        self.invite_link_instructions = invite_link_instructions or []
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "RoutingDetailsPutRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The document ID to add.

        Returns:
            The updated request.
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Any]:
        """
        Returns the payload for the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Any] = {}
        if self.template_data is not None:
            payload["template_data"] = self.template_data
        if self.template_data_object:
            payload["template_data_object"] = self.template_data_object
        if self.cc:
            payload["cc"] = self.cc
        if self.cc_step:
            payload["cc_step"] = self.cc_step
        if self.viewers:
            payload["viewers"] = self.viewers
        if self.approvers:
            payload["approvers"] = self.approvers
        if self.invite_link_instructions:
            payload["invite_link_instructions"] = self.invite_link_instructions
        return payload

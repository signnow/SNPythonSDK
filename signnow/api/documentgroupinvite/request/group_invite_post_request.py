"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="inviteToSignDocumentGroup",
    url="/documentgroup/{document_group_id}/groupinvite",
    method="post",
    auth="bearer",
    namespace="documentGroupInvite",
    entity="groupInvite",
    content_type="application/json",
)
class GroupInvitePostRequest(RequestInterface):
    """
    Represents a request to invite a group to sign a document.
    """

    def __init__(
        self,
        invite_steps: Optional[List[Dict[str, Any]]] = None,
        cc: Optional[List[Dict[str, Any]]] = None,
        email_groups: Optional[List[Dict[str, Any]]] = None,
        completion_emails: Optional[List[Dict[str, Any]]] = None,
        sign_as_merged: bool = False,
        client_timestamp: int = 0,
        cc_subject: Optional[str] = None,
        cc_message: Optional[str] = None,
    ):
        """
        Constructs a new GroupInvitePostRequest.

        Args:
            invite_steps: Collection of invite steps. Optional.
            cc: Collection of CC recipients. Optional.
            email_groups: Collection of email groups. Optional.
            completion_emails: Collection of completion emails. Optional.
            sign_as_merged: Flag indicating whether to sign as merged. Default: False.
            client_timestamp: Client timestamp. Default: 0.
            cc_subject: Subject of the CC email. Optional.
            cc_message: Message of the CC email. Optional.
        """
        self.invite_steps = invite_steps or []
        self.cc = cc or []
        self.email_groups = email_groups or []
        self.completion_emails = completion_emails or []
        self.sign_as_merged = sign_as_merged
        self.client_timestamp = client_timestamp
        self.cc_subject = cc_subject
        self.cc_message = cc_message
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "GroupInvitePostRequest":
        """
        Adds the document group ID to the URI parameters.

        Args:
            document_group_id: The document group ID.

        Returns:
            This GroupInvitePostRequest instance.
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

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary representing the payload of the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Any] = {}
        if self.invite_steps:
            payload["invite_steps"] = self.invite_steps
        if self.email_groups:
            payload["email_groups"] = self.email_groups
        if self.completion_emails:
            payload["completion_emails"] = self.completion_emails
        payload["sign_as_merged"] = self.sign_as_merged
        if self.client_timestamp:
            payload["client_timestamp"] = self.client_timestamp
        if self.cc:
            payload["cc"] = self.cc
        if self.cc_subject is not None:
            payload["cc_subject"] = self.cc_subject
        if self.cc_message is not None:
            payload["cc_message"] = self.cc_message
        return payload

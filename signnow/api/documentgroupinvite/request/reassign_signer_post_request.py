"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="reassignSignerForDocumentGroupInvite",
    url="/documentgroup/{document_group_id}/groupinvite/{invite_id}/invitestep/{step_id}/update",
    method="post",
    auth="bearer",
    namespace="documentGroupInvite",
    entity="reassignSigner",
    content_type="application/json",
)
class ReassignSignerPostRequest(RequestInterface):
    """
    Represents a request to reassign a signer for a document group invite.
    """

    def __init__(
        self,
        user_to_update: str,
        replace_with_this_user: str,
        invite_email: Optional[Dict[str, Any]] = None,
        update_invite_action_attributes: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Constructs a new ReassignSignerPostRequest.

        Args:
            user_to_update: The user to be updated.
            replace_with_this_user: The user to replace the current user with.
            invite_email: The invite email. Optional.
            update_invite_action_attributes: The update invite action attributes. Optional.
        """
        self.user_to_update = user_to_update
        self.replace_with_this_user = replace_with_this_user
        self.invite_email = invite_email
        self.update_invite_action_attributes = update_invite_action_attributes or []
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "ReassignSignerPostRequest":
        """
        Sets the document group id in the URI parameters.

        Args:
            document_group_id: The document group id.

        Returns:
            The current ReassignSignerPostRequest instance.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def with_invite_id(self, invite_id: str) -> "ReassignSignerPostRequest":
        """
        Sets the invite id in the URI parameters.

        Args:
            invite_id: The invite id.

        Returns:
            The current ReassignSignerPostRequest instance.
        """
        self._uri_params["invite_id"] = invite_id
        return self

    def with_step_id(self, step_id: str) -> "ReassignSignerPostRequest":
        """
        Sets the step id in the URI parameters.

        Args:
            step_id: The step id.

        Returns:
            The current ReassignSignerPostRequest instance.
        """
        self._uri_params["step_id"] = step_id
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
        Constructs the payload for the request.

        Returns:
            A dictionary containing the payload data.
        """
        payload: Dict[str, Any] = {
            "user_to_update": self.user_to_update,
            "replace_with_this_user": self.replace_with_this_user,
        }
        if self.invite_email is not None:
            payload["invite_email"] = self.invite_email
        if self.update_invite_action_attributes:
            payload["update_invite_action_attributes"] = (
                self.update_invite_action_attributes
            )
        return payload

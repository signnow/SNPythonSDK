"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="resendDocumentGroupInvite",
    url="/documentgroup/{document_group_id}/groupinvite/{invite_id}/resendinvites",
    method="post",
    auth="bearer",
    namespace="documentGroupInvite",
    entity="resendGroupInvite",
    content_type="application/json",
)
class ResendGroupInvitePostRequest(RequestInterface):
    """
    Represents a request to resend a group invite.
    """

    def __init__(self, email: str):
        """
        Constructs a new ResendGroupInvitePostRequest.

        Args:
            email: The email address to which the invite is to be sent.
        """
        self.email = email
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "ResendGroupInvitePostRequest":
        """
        Adds the document group ID to the URI parameters.

        Args:
            document_group_id: The document group ID.

        Returns:
            This ResendGroupInvitePostRequest, for chaining.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def with_invite_id(self, invite_id: str) -> "ResendGroupInvitePostRequest":
        """
        Adds the invite ID to the URI parameters.

        Args:
            invite_id: The invite ID.

        Returns:
            This ResendGroupInvitePostRequest, for chaining.
        """
        self._uri_params["invite_id"] = invite_id
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
        Returns a dictionary representing the payload for this request.

        Returns:
            A dictionary containing the email.
        """
        return {"email": self.email}

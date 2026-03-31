"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createLinkForEmbeddedInviteDocumentGroup",
    url="/v2/document-groups/{document_group_id}/embedded-invites/{embedded_invite_id}/link",
    method="post",
    auth="bearer",
    namespace="embeddedGroupInvite",
    entity="groupInviteLink",
    content_type="application/json",
)
class GroupInviteLinkPostRequest(RequestInterface):
    """
    Represents a request to create a link for an embedded invite document group.
    """

    def __init__(
        self,
        email: Optional[str] = None,
        auth_method: Optional[str] = None,
        link_expiration: Optional[int] = None,
    ):
        """
        Constructs a new GroupInviteLinkPostRequest.

        Args:
            email: The email of the user. Optional.
            auth_method: The authentication method used. Optional.
            link_expiration: The expiration time of the link. Optional.
        """
        self.email = email
        self.auth_method = auth_method
        self.link_expiration = link_expiration
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "GroupInviteLinkPostRequest":
        """
        Adds the document group ID to the URI parameters.

        Args:
            document_group_id: The document group ID.

        Returns:
            This request.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def with_embedded_invite_id(
        self, embedded_invite_id: str
    ) -> "GroupInviteLinkPostRequest":
        """
        Adds the embedded invite ID to the URI parameters.

        Args:
            embedded_invite_id: The embedded invite ID.

        Returns:
            This request.
        """
        self._uri_params["embedded_invite_id"] = embedded_invite_id
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
        Returns a dictionary containing the payload for this request.

        Returns:
            A dictionary containing email, auth_method, and link_expiration.
        """
        payload: Dict[str, Any] = {}
        if self.email is not None:
            payload["email"] = self.email
        if self.auth_method is not None:
            payload["auth_method"] = self.auth_method
        if self.link_expiration is not None:
            payload["link_expiration"] = self.link_expiration
        return payload

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createLinkForEmbeddedInvite",
    url="/v2/documents/{document_id}/embedded-invites/{field_invite_id}/link",
    method="post",
    auth="bearer",
    namespace="embeddedInvite",
    entity="documentInviteLink",
    content_type="application/json",
)
class DocumentInviteLinkPostRequest(RequestInterface):
    """
    Represents a request to create a link for an embedded invite.
    """

    def __init__(
        self,
        auth_method: Optional[str] = None,
        link_expiration: Optional[int] = None,
    ):
        """
        Constructs a new DocumentInviteLinkPostRequest.

        Args:
            auth_method: The authentication method used for the request. Optional.
            link_expiration: The expiration time for the link. Optional.
        """
        self.auth_method = auth_method
        self.link_expiration = link_expiration
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "DocumentInviteLinkPostRequest":
        """
        Adds the document ID to the URI parameters.

        Args:
            document_id: The document ID.

        Returns:
            This request.
        """
        self._uri_params["document_id"] = document_id
        return self

    def with_field_invite_id(
        self, field_invite_id: str
    ) -> "DocumentInviteLinkPostRequest":
        """
        Adds the field invite ID to the URI parameters.

        Args:
            field_invite_id: The field invite ID.

        Returns:
            This request.
        """
        self._uri_params["field_invite_id"] = field_invite_id
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
            A dictionary containing auth_method and link_expiration.
        """
        payload: Dict[str, Any] = {}
        if self.auth_method is not None:
            payload["auth_method"] = self.auth_method
        if self.link_expiration is not None:
            payload["link_expiration"] = self.link_expiration
        return payload

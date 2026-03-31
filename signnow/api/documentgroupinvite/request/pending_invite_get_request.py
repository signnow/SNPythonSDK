"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getPendingDocumentGroupInvites",
    url="/documentgroup/{document_group_id}/groupinvite/{invite_id}/pendinginvites",
    method="get",
    auth="bearer",
    namespace="documentGroupInvite",
    entity="pendingInvite",
    content_type="application/json",
)
class PendingInviteGetRequest(RequestInterface):
    """
    API endpoint for getting pending document group invites.
    """

    def __init__(self):
        """Constructs a new PendingInviteGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "PendingInviteGetRequest":
        """
        Sets the document group ID for the request.

        Args:
            document_group_id: The ID of the document group.

        Returns:
            The current request instance.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def with_invite_id(self, invite_id: str) -> "PendingInviteGetRequest":
        """
        Sets the invite ID for the request.

        Args:
            invite_id: The ID of the invite.

        Returns:
            The current request instance.
        """
        self._uri_params["invite_id"] = invite_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

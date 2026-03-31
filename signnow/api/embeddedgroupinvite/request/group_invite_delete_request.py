"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="deleteEmbeddedDocGroupInvites",
    url="/v2/document-groups/{document_group_id}/embedded-invites",
    method="delete",
    auth="bearer",
    namespace="embeddedGroupInvite",
    entity="groupInvite",
    content_type="application/json",
)
class GroupInviteDeleteRequest(RequestInterface):
    """
    Represents a request to delete a group invite.
    """

    def __init__(self):
        """Constructs a new GroupInviteDeleteRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "GroupInviteDeleteRequest":
        """
        Adds a document group id to the URI parameters.

        Args:
            document_group_id: The id of the document group.

        Returns:
            The current GroupInviteDeleteRequest instance.
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

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}

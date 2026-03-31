"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createEmbeddedInviteForDocumentGroup",
    url="/v2/document-groups/{document_group_id}/embedded-invites",
    method="post",
    auth="bearer",
    namespace="embeddedGroupInvite",
    entity="groupInvite",
    content_type="application/json",
)
class GroupInvitePostRequest(RequestInterface):
    """
    Represents a request to create an embedded invite for a document group.
    """

    def __init__(self, invites: List[Dict[str, Any]], sign_as_merged: bool = False):
        """
        Constructs a new GroupInvitePostRequest.

        Args:
            invites: Collection of invites.
            sign_as_merged: Flag to indicate if the document should be signed as merged. Default: False.
        """
        self.invites = invites
        self.sign_as_merged = sign_as_merged
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "GroupInvitePostRequest":
        """
        Sets document group id in URI parameters.

        Args:
            document_group_id: Document group id.

        Returns:
            Current instance of GroupInvitePostRequest.
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
        Returns the payload for the request.

        Returns:
            A dictionary containing invites and sign_as_merged.
        """
        return {
            "invites": self.invites,
            "sign_as_merged": self.sign_as_merged,
        }

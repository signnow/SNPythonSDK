"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="cancelInvite",
    url="/document/{document_id}/fieldinvitecancel",
    method="put",
    auth="bearer",
    namespace="documentInvite",
    entity="cancelInvite",
    content_type="application/json",
)
class CancelInvitePutRequest(RequestInterface):
    """
    This class represents a request to cancel an invite.
    """

    def __init__(self, reason: str):
        """
        Constructs a new CancelInvitePutRequest with the specified reason.

        Args:
            reason: The reason for cancelling the invite
        """
        self._reason = reason
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "CancelInvitePutRequest":
        """
        Adds the document ID to the URI parameters.

        Args:
            document_id: The ID of the document

        Returns:
            The current CancelInvitePutRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns the payload for the request.

        Returns:
            A dict containing the payload for the request
        """
        return {"reason": self._reason}

"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="cancelFreeFormInvite",
    url="/invite/{invite_id}/cancel",
    method="put",
    auth="bearer",
    namespace="documentInvite",
    entity="cancelFreeFormInvite",
    content_type="application/json",
)
class CancelFreeFormInvitePutRequest(RequestInterface):
    """
    API endpoint for cancelling a free form invite.
    """

    def __init__(self, reason: str):
        """
        Constructor for CancelFreeFormInvitePutRequest.

        Args:
            reason: The reason for cancelling the invite
        """
        self._reason = reason
        self._uri_params: Dict[str, str] = {}

    def with_invite_id(self, invite_id: str) -> "CancelFreeFormInvitePutRequest":
        """
        Method to add invite id to the URI parameters.

        Args:
            invite_id: The id of the invite

        Returns:
            The updated CancelFreeFormInvitePutRequest object
        """
        self._uri_params["invite_id"] = invite_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Method to get the URI parameters.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Method to get the payload for the request.

        Returns:
            A dict containing the payload for the request
        """
        return {"reason": self._reason}

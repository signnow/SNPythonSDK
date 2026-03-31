"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getUserInfo",
    url="/user",
    method="get",
    auth="bearer",
    namespace="user",
    entity="user",
    content_type="application/json",
)
class UserGetRequest(RequestInterface):
    """
    This class represents a user get request.
    It is used to get user information from the server.
    """

    def uri_params(self) -> Dict[str, str]:
        """
        This method is used to get the URI parameters for the request.
        It returns an empty dict as there are no URI parameters for this request.

        Returns:
            An empty dict
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        This method is used to get the payload for the request.
        It returns an empty dict as there is no payload for this request.

        Returns:
            An empty dict
        """
        return {}

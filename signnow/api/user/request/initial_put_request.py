"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateUserInitials",
    url="/user/initial",
    method="put",
    auth="bearer",
    namespace="user",
    entity="initial",
    content_type="application/json",
)
class InitialPutRequest(RequestInterface):
    """
    Represents a request to update user initials.
    """

    def __init__(self, data: str):
        """
        Constructs a new InitialPutRequest.

        Args:
            data: The data to be updated.
        """
        self.data = data

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the data to be updated.

        Returns:
            A dictionary containing the data.
        """
        return {
            "data": self.data,
        }

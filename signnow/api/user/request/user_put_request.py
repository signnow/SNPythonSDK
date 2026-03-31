"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateUser",
    url="/user",
    method="put",
    auth="bearer",
    namespace="user",
    entity="user",
    content_type="application/json",
)
class UserPutRequest(RequestInterface):
    """
    Represents a user update request.
    """

    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        password: Optional[str] = None,
        old_password: Optional[str] = None,
        logout_all: Optional[str] = None,
    ):
        """
        Constructs a new UserPutRequest.

        Args:
            first_name: The first name of the user. Optional.
            last_name: The last name of the user. Optional.
            password: The new password of the user. Optional.
            old_password: The old password of the user. Optional.
            logout_all: The logout all flag of the user. Optional.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.old_password = old_password
        self.logout_all = logout_all

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the payload parameters.

        Returns:
            A dictionary containing first_name, last_name, password, old_password, and logout_all.
        """
        payload: Dict[str, str] = {}
        if self.first_name is not None:
            payload["first_name"] = self.first_name
        if self.last_name is not None:
            payload["last_name"] = self.last_name
        if self.password is not None:
            payload["password"] = self.password
        if self.old_password is not None:
            payload["old_password"] = self.old_password
        if self.logout_all is not None:
            payload["logout_all"] = self.logout_all
        return payload

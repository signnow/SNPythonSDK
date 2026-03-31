"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createUser",
    url="/user",
    method="post",
    auth="basic",
    namespace="user",
    entity="user",
    content_type="application/json",
)
class UserPostRequest(RequestInterface):
    """
    Represents a user post request.
    Used to create a new user.
    """

    def __init__(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        number: Optional[str] = None,
    ):
        """
        Constructs a new UserPostRequest.

        Args:
            email: The email of the user.
            password: The password of the user.
            first_name: The first name of the user.
            last_name: The last name of the user.
            number: The number of the user. Optional.
        """
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the user's details as the payload.

        Returns:
            A dictionary containing email, password, first_name, last_name, and number.
        """
        payload: Dict[str, str] = {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
        if self.number is not None:
            payload["number"] = self.number
        return payload

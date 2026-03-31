"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="resetPassword",
    url="/user/forgotpassword",
    method="post",
    auth="basic",
    namespace="user",
    entity="resetPassword",
    content_type="application/json",
)
class ResetPasswordPostRequest(RequestInterface):
    """
    Represents a request to reset password.
    """

    def __init__(self, email: str):
        """
        Constructs a new ResetPasswordPostRequest.

        Args:
            email: The email of the user who wants to reset the password.
        """
        self.email = email

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the email of the user.

        Returns:
            A dictionary containing the email.
        """
        return {
            "email": self.email,
        }

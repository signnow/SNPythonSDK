"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="userEmailVerify",
    url="/user/email/verify",
    method="put",
    auth="basic",
    namespace="user",
    entity="emailVerify",
    content_type="application/json",
)
class EmailVerifyPutRequest(RequestInterface):
    """
    Represents a request to verify a user's email.
    """

    def __init__(self, email: str, verification_token: str):
        """
        Constructs a new EmailVerifyPutRequest.

        Args:
            email: The email of the user to be verified.
            verification_token: The verification token for the user's email.
        """
        self.email = email
        self.verification_token = verification_token

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the payload for the request.

        Returns:
            A dictionary containing email and verification_token.
        """
        return {
            "email": self.email,
            "verification_token": self.verification_token,
        }

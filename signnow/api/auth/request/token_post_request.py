"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="generateAccessToken",
    url="/oauth2/token",
    method="post",
    auth="basic",
    namespace="auth",
    entity="token",
    content_type="application/x-www-form-urlencoded",
)
class TokenPostRequest(RequestInterface):
    """
    This class represents a request to generate an access token.
    """

    def __init__(
        self,
        user: str,
        password: str,
        scope: str,
        grant_type: str,
        code: str,
    ):
        """
        Constructs a new TokenPostRequest.

        Args:
            user: The username of the user
            password: The password of the user
            scope: The scope of the request
            grant_type: The grant type of the request
            code: The code of the request
        """
        self._user = user
        self._password = password
        self._scope = scope
        self._grant_type = grant_type
        self._code = code

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dict with the payload of the request.

        Returns:
            A dict with the payload of the request
        """
        return {
            "username": self._user,
            "password": self._password,
            "scope": self._scope,
            "grant_type": self._grant_type,
            "code": self._code,
        }

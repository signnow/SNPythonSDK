"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="refreshAccessToken",
    url="/oauth2/token",
    method="post",
    auth="basic",
    namespace="auth",
    entity="refreshToken",
    content_type="application/x-www-form-urlencoded",
)
class RefreshTokenPostRequest(RequestInterface):
    """
    Represents a request to refresh an access token.
    """

    def __init__(
        self,
        refresh_token: str,
        scope: str,
        expiration_time: str,
        grant_type: str,
    ):
        """
        Constructs a new RefreshTokenPostRequest.

        Args:
            refresh_token: The refresh token.
            scope: The scope of the request.
            expiration_time: The expiration time of the token.
            grant_type: The grant type of the request.
        """
        self.refresh_token = refresh_token
        self.scope = scope
        self.expiration_time = expiration_time
        self.grant_type = grant_type

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the payload of the request.

        Returns:
            A dictionary containing refresh_token, scope, expiration_time, and grant_type.
        """
        return {
            "refresh_token": self.refresh_token,
            "scope": self.scope,
            "expiration_time": self.expiration_time,
            "grant_type": self.grant_type,
        }

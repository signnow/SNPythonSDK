"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getToken",
    url="/oauth2/token",
    method="get",
    auth="bearer",
    namespace="auth",
    entity="token",
    content_type="application/json",
)
class TokenGetRequest(RequestInterface):
    """
    This class represents a request to get token information.
    """

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, str]:
        """Returns an empty dict as this is a GET request."""
        return {}
